"""
:Authors: Warren Hack

:License: :doc:`LICENSE`

"""
import os, sys
import copy
from distutils.version import LooseVersion

import numpy as np
#import pywcs
import astropy
from astropy import wcs as pywcs
import astropy.coordinates as coords
from astropy import units as u
from stsci.tools import logutil, textutil
from stsci.skypac.utils import basicFITScheck, get_extver_list

import stwcs
from stwcs import wcsutil
from astropy.io import fits
import stsci.imagestats as imagestats
import stregion as pyregion

#import idlphot
from . import tweakutils, util
from .mapreg import _AuxSTWCS


COLNAME_PARS = ['xcol','ycol','fluxcol']
CATALOG_ARGS = ['sharpcol','roundcol','hmin','fwhm','maxflux','minflux','fluxunits','nbright']+COLNAME_PARS

REFCOL_PARS = ['refxcol','refycol','rfluxcol']
REFCAT_ARGS = ['rmaxflux','rminflux','rfluxunits','refnbright']+REFCOL_PARS

sortKeys = ['minflux','maxflux','nbright','fluxunits']


log = logutil.create_logger(__name__, level=logutil.logging.NOTSET)


def generateCatalog(wcs, mode='automatic', catalog=None,
                    src_find_filters=None, **kwargs):
    """ Function which determines what type of catalog object needs to be
    instantiated based on what type of source selection algorithm the user
    specified.

    Parameters
    ----------
    wcs : obj
        WCS object generated by STWCS or PyWCS

    catalog : str or ndarray
        Filename of existing catalog or ndarray of image for generation of
        source catalog.

    kwargs : dict
        Parameters needed to interpret source catalog from input catalog
        with `findmode` being required.

    Returns
    -------
    catalog : obj
        A Catalog-based class instance for keeping track of WCS and
        associated source catalog

    """
    if not isinstance(catalog,Catalog):
        if mode == 'automatic': # if an array is provided as the source
            # Create a new catalog directly from the image
            catalog = ImageCatalog(wcs,catalog,src_find_filters,**kwargs)
        else: # a catalog file was provided as the catalog source
            catalog = UserCatalog(wcs,catalog,**kwargs)

    return catalog


class Catalog:
    """ Base class for keeping track of a source catalog for an input WCS

        .. warning:: This class should never be instantiated by itself,
                     as necessary methods are not defined yet.
    """
    PAR_PREFIX = ''
    PAR_NBRIGHT_PREFIX = ''

    def __init__(self, wcs, catalog_source, **kwargs):
        """
        This class requires the input of a WCS and a source for the catalog,
        along with any arguments necessary for interpreting the catalog.

        Parameters
        ----------
        wcs : obj
            Input WCS object generated using STWCS or HSTWCS

        catalog_source : str
            Name of the file from which to read the catalog.

        kwargs : dict
            Parameters for interpreting the catalog file or for performing the
            source extraction from the image. These will be set differently
            depending on the type of catalog being instantiated.

        """
        self.wcs = wcs # could be None in case of user-supplied catalog
        self.xypos = None
        self.in_units = 'pixels'
        self.sharp = None
        self.round1 = None
        self.round2 = None
        self.numcols = None

        self.flux_col = True # keep track of whether fluxes were read in
        self.sharp_col = True # keep track of whether sharpness was read in

        self.origin = 1 # X,Y coords will ALWAYS be FITS 1-based, not numpy 0-based
        self.pars = kwargs
        if 'use_sharp_round' in self.pars:
            self.use_sharp_round = self.pars['use_sharp_round']
        else:
            self.use_sharp_round = False

        self.start_id = 0
        if 'start_id' in self.pars:
            self.start_id = self.pars['start_id']

        self.fname = catalog_source
        self.source = catalog_source
        self.catname = None

        self.num_objects = None

        self.radec = None # catalog of sky positions for all sources on this chip/image
        self.set_colnames()

        self._apply_flux_limits = False # used in child class to control
                                        # source filtering on flux

        # parse task parameters to find flux limits:
        self.minflux = self.pars.get(self.PAR_PREFIX + 'minflux')
        self.maxflux = self.pars.get(self.PAR_PREFIX + 'maxflux')
        self.fluxunits = self.pars.get(self.PAR_PREFIX + 'fluxunits')
        self.nbright = self.pars.get(self.PAR_NBRIGHT_PREFIX + 'nbright')

    def generateXY(self, **kwargs):
        """ Method to generate source catalog in XY positions
            Implemented by each subclass
        """
        pass

    def set_colnames(self):
        """ Method to define how to interpret a catalog file
            Only needed when provided a source catalog as input
        """
        pass

    def _readCatalog(self):
        pass

    def generateRaDec(self):
        """ Convert XY positions into sky coordinates using STWCS methods. """
        self.prefix = self.PAR_PREFIX

        if not isinstance(self.wcs,pywcs.WCS):
            print(
                textutil.textbox(
                    'WCS not a valid PyWCS object. '
                    'Conversion of RA/Dec not possible...'
                    ),
                file=sys.stderr
            )
            raise ValueError

        if self.xypos is None or len(self.xypos[0]) == 0:
            self.xypos = None
            warnstr = textutil.textbox(
                'WARNING: \n'
                'No objects found for this image...'
            )

            for line in warnstr.split('\n'):
                log.warning(line)

            print(warnstr)
            return

        if self.radec is None:
            print('     Found {:d} objects.'.format(len(self.xypos[0])))
            if self.wcs is not None:
                ra, dec = self.wcs.all_pix2world(self.xypos[0], self.xypos[1], self.origin)
                self.radec = [ra, dec] + copy.deepcopy(self.xypos[2:])
            else:
                # If we have no WCS, simply pass along the XY input positions
                # under the assumption they were already sky positions.
                self.radec = copy.deepcopy(self.xypos)

    def apply_exclusions(self,exclusions):
        """ Trim sky catalog to remove any sources within regions specified by
            exclusions file.
        """
        # parse exclusion file into list of positions and distances
        exclusion_coords = tweakutils.parse_exclusions(exclusions)
        if exclusion_coords is None:
            return

        excluded_list = []
        radec_indx = list(range(len(self.radec[0])))
        for ra,dec,indx in zip(self.radec[0],self.radec[1],radec_indx):
            src_pos = coords.SkyCoord(ra=ra,dec=dec,unit=(u.hourangle,u.deg))

            # check to see whether this source is within an exclusion region
            for reg in exclusion_coords:
                if reg['units'] == 'sky':
                    regpos = reg['pos']
                    regdist = reg['distance'] # units: arcsec
                else:
                    regradec = self.wcs.all_pix2world([reg['pos']],1)[0]
                    regpos = (regradec[0],regradec[1])
                    regdist = reg['distance']*self.wcs.pscale # units: arcsec

                epos = coords.SkyCoord(ra=regpos[0],dec=regpos[1],unit=(u.hourangle,u.deg))
                if float(epos.separation(src_pos).to_string(unit=u.arcsec,decimal=True)) <= regdist:
                    excluded_list.append(indx)
                    break
        # create a list of all 'good' sources outside all exclusion regions
        for e in excluded_list: radec_indx.remove(e)
        radec_indx = np.array(radec_indx,dtype=int)
        num_excluded = len(excluded_list)
        if num_excluded > 0:
            radec_trimmed = []
            xypos_trimmed = []
            for arr in self.radec:
                radec_trimmed.append(arr[radec_indx])
            for arr in self.xypos:
                xypos_trimmed.append(arr[radec_indx])
            xypos_trimmed[-1] = np.arange(len(xypos_trimmed[0]))
            self.radec = radec_trimmed
            self.xypos = xypos_trimmed
            log.info('Excluded %d sources from catalog.'%num_excluded)

    def apply_flux_limits(self):
        """ Apply any user-specified limits on source selection
            Limits based on fluxes.

        """
        if not self._apply_flux_limits:
            return

        # only if limits are set should they be applied
        if ((self.maxflux is None and self.minflux is None) or
            self.fluxunits is None):
            return

        print("\n     Applying flux limits...")
        print("         minflux = {}".format(self.minflux))
        print("         maxflux = {}".format(self.maxflux))
        print("         fluxunits = '{:s}'".format(self.fluxunits))
        print("         nbright = {}".format(self.nbright))

        # start by checking to see whether fluxes were read in to use for
        # applying the limits
        if not self.flux_col:
            print("    WARNING: Catalog did not contain fluxes for use in trimming...")
            return

        if self.xypos is not None and self.radec is not None:
            if len(self.xypos) < len(self.radec):
                src_cat = self.radec
            else:
                src_cat = self.xypos
        else:
            src_cat = self.radec if self.xypos is None else self.xypos

        if src_cat is None:
            raise RuntimeError("No catalogs available for filtering")

        if len(src_cat) < 3:
            print("    WARNING: No fluxes read in for catalog for use in trimming...")
            return

        fluxes = copy.deepcopy(src_cat[2])

        # apply limits equally to all .radec and .xypos entries
        # Start by clipping by any specified flux range
        if self.fluxunits == 'mag':
            if self.minflux is None:
                flux_mask = fluxes >= self.maxflux
            elif self.maxflux is None:
                flux_mask = fluxes <= self.minflux
            else:
                flux_mask = (fluxes <= self.minflux) & (fluxes >= self.maxflux)
        else:
            if self.minflux is None:
                flux_mask = fluxes <= self.maxflux
            elif self.maxflux is None:
                flux_mask = fluxes >= self.minflux
            else:
                flux_mask = (fluxes >= self.minflux) & (fluxes <= self.maxflux)

        if self.radec is None:
            all_radec = None
        else:
            all_radec = [rd[flux_mask].copy() for rd in self.radec]

        if self.xypos is None:
            all_xypos = None
        else:
            all_xypos = [xy[flux_mask].copy() for xy in self.xypos]

        nrem = flux_mask.size - np.count_nonzero(flux_mask)
        print("     Removed {:d} sources based on flux limits.".format(nrem))

        if self.nbright is not None:
            print("Selecting catalog based on {} brightest sources".format(self.nbright))
            fluxes = fluxes[flux_mask]

            # find indices of brightest sources
            idx = np.argsort(fluxes)
            if self.fluxunits == 'mag':
                idx = idx[:self.nbright]
            else:
                idx = (idx[::-1])[:self.nbright]

            # pick out only the brightest 'nbright' sources
            if all_radec is not None:
                all_radec = [rd[idx] for rd in all_radec]
            if all_xypos is not None:
                all_xypos = [xy[idx] for xy in all_xypos]

        self.radec = all_radec
        self.xypos = all_xypos

        if len(self.radec[0]) == 0:
            print("Trimming of catalog resulted in NO valid sources! ")
            raise ValueError

    def buildCatalogs(self, exclusions=None, **kwargs):
        """ Primary interface to build catalogs based on user inputs.
        """
        self.generateXY(**kwargs)
        self.generateRaDec()
        if exclusions:
            self.apply_exclusions(exclusions)

        # apply selection limits as specified by the user:
        self.apply_flux_limits()

    def plotXYCatalog(self, **kwargs):
        """
        Method which displays the original image and overlays the positions
        of the detected sources from this image's catalog.

        Plotting `kwargs` that can be provided are:

            vmin, vmax, cmap, marker

        Default colormap is `summer`.

        """
        try:
            from matplotlib import pyplot as pl
        except:
            pl = None

        if pl is not None: # If the pyplot package could be loaded...
            pl.clf()
            pars = kwargs.copy()

            if 'marker' not in pars:
                pars['marker'] = 'b+'

            if 'cmap' in pars:
                pl_cmap = pars['cmap']
                del pars['cmap']
            else:
                pl_cmap = 'summer'
            pl_vmin = None
            pl_vmax = None
            if 'vmin' in pars:
                pl_vmin = pars['vmin']
                del pars['vmin']
            if 'vmax' in pars:
                pl_vmax = pars['vmax']
                del pars['vmax']

            pl.imshow(self.source,cmap=pl_cmap,vmin=pl_vmin,vmax=pl_vmax)
            pl.plot(self.xypos[0]-1,self.xypos[1]-1,pars['marker'])

    def writeXYCatalog(self,filename):
        """ Write out the X,Y catalog to a file
        """
        if self.xypos is None:
            warnstr = textutil.textbox(
                'WARNING: \n    No X,Y source catalog to write to file. ')
            for line in warnstr.split('\n'):
                log.warning(line)
            print(warnstr)
            return

        f = open(filename,'w')
        f.write("# Source catalog derived for %s\n"%self.wcs.filename)
        f.write("# Columns: \n")
        if self.use_sharp_round:
            f.write('#    X      Y         Flux       ID      Sharp       Round1       Round2\n')
        else:
            f.write('#    X      Y         Flux       ID\n')
        f.write('#   (%s)   (%s)\n'%(self.in_units,self.in_units))

        for row in range(len(self.xypos[0])):
            for i in range(len(self.xypos)):
                f.write("%g  "%(self.xypos[i][row]))
            f.write("\n")

        f.close()


class ImageCatalog(Catalog):
    """ Class which generates a source catalog from an image using
        Python-based, daofind-like algorithms

        Required input `kwargs` parameters::

            computesig, skysigma, threshold, peakmin, peakmax,
            hmin, conv_width, [roundlim, sharplim]

    """
    def __init__(self, wcs, catalog_source, src_find_filters=None, **kwargs):
        # 'src_find_filters' - None or a dictionary. The dictionary
        # MUST contain keys 'region_file' and 'region_file_mode':
        # - 'region_file': the name of the region file that indicates regions
        #   of the image that should be used for source finding
        #   ("include" regions) or regions of the image that should NOT be used
        #   for source finding ("exclude" regions). If it is None - the entire
        #   image will be used for source finding.
        # - 'region_file_mode': 'exclude only' or 'normal' - if 'exclude only' then regular regions are
        #   interpretted as 'exclude' regions and exclude regions (with '-' in front)
        #   are ignored. If 'region_file_mode' = 'normal' then normal DS9 interpretation
        #   of the regions will be applied.
        self.src_find_filters = src_find_filters
        super().__init__(wcs, catalog_source, **kwargs)
        extind = self.fname.rfind('[')
        self.fnamenoext = self.fname if extind < 0 else self.fname[:extind]
        if self.wcs.extname == ('',None):
            self.wcs.extname = (0)
        self.source = fits.getdata(self.wcs.filename,ext=self.wcs.extname, memmap=False)
        self.nbright = None # No GUI parameter defined yet for this filtering

    def _combine_exclude_mask(self, mask):
        # create masks from exclude/include regions and combine it with the
        # input DQ mask:
        #
        regmask = None
        if self.src_find_filters is not None and \
           'region_file' in self.src_find_filters:
            reg_file_name = self.src_find_filters['region_file']
            if not os.path.isfile(reg_file_name):
                raise IOError("The 'exclude' region file '{:s}' does not exist."
                              .format(reg_file_name))
        else:
            return mask

        # get data image size:
        (img_ny, img_nx) = self.source.shape

        # find out if user provided a region file or a mask FITS file:
        reg_file_ext = os.path.splitext(reg_file_name)[-1]
        if reg_file_ext.lower().strip() in ['.fits', '.fit'] and \
           basicFITScheck(reg_file_name):
            # likely we are dealing with a FITS file.
            # check that the file is a simple with 2 axes:
            hdulist = fits.open(reg_file_name, memmap=False)
            extlist = get_extver_list(hdulist,extname=None)
            for ext in extlist:
                usermask = hdulist[ext].data
                if usermask.shape == (img_ny, img_nx):
                    regmask = usermask.astype(np.bool)
                    break
            hdulist.close()
            if regmask is None:
                raise ValueError("None of the image-like extensions in the "
                                 "user-provided exclusion mask '{}' has a "
                                 "correct shape".format(reg_file_name))

        else:
            # we are dealing with a region file:
            reglist = pyregion.open(reg_file_name)

            ## check that regions are in image-like coordinates:
            ##TODO: remove the code below once 'pyregion' package can correctly
            ##      (DS9-like) convert sky coordinates to image coordinates for all
            ##      supported shapes.
            #if not all([ (x.coord_format == 'image' or \
            #              x.coord_format == 'physical') for x in reglist]):
            #    print("WARNING: Some exclusion regions are in sky coordinates.\n"
            #          "         These regions will be ignored.")
            #    # filter out regions in sky coordinates:
            #    reglist = pyregion.ShapeList(
            #        [x for x in reglist if x.coord_format == 'image' or \
            #         x.coord_format == 'physical']
            #    )

            #TODO: comment out next lines if we do not support region files
            #      in sky coordinates and uncomment previous block:
            # Convert regions from sky coordinates to image coordinates:
            auxwcs    = _AuxSTWCS(self.wcs)
            reglist = reglist.as_imagecoord(auxwcs, rot_wrt_axis=2)

            # if all regions are exclude regions, then assume that the entire image
            # should be included and that exclude regions exclude from this
            # rectangular region representing the entire image:
            if all([x.exclude for x in reglist]):
                # we slightly widen the box to make sure that
                # the entire image is covered:
                imreg = pyregion.parse("image;box({:.1f},{:.1f},{:d},{:d},0)"
                                       .format((img_nx+1)/2.0, (img_ny+1)/2.0,
                                               img_nx+1, img_ny+1)
                                       )

                reglist = pyregion.ShapeList(imreg + reglist)

            # create a mask from regions:
            regmask = np.asarray(
                reglist.get_mask(shape=(img_ny, img_nx)),
                dtype=np.bool
            )

        if mask is not None and regmask is not None:
            mask = np.logical_and(regmask, mask)
        else:
            mask = regmask

        #DEBUG:
        if mask is not None:
            fn = os.path.splitext(self.fname)[0] + '_srcfind_mask.fits'
            fits.writeto(fn, mask.astype(dtype=np.uint8), overwrite=True)

        return mask

    def generateXY(self, **kwargs):
        """ Generate source catalog from input image using DAOFIND-style algorithm
        """
        #x,y,flux,sharp,round = idlphot.find(array,self.pars['hmin'],self.pars['fwhm'],
        #                    roundlim=self.pars['roundlim'], sharplim=self.pars['sharplim'])
        print("  #  Source finding for '{}', EXT={} started at: {}"
              .format(self.fnamenoext, self.wcs.extname, util._ptime()[0]))
        if self.pars['computesig']:
            # compute sigma for this image
            sigma = self._compute_sigma()
        else:
            sigma = self.pars['skysigma']
        skymode = sigma**2
        log.info('   Finding sources using sky sigma = %f'%sigma)
        if self.pars['threshold'] in [None,"INDEF",""," "]:
            hmin = skymode
        else:
            hmin = sigma*self.pars['threshold']

        if 'mask' in kwargs and kwargs['mask'] is not None:
            dqmask = np.asarray(kwargs['mask'], dtype=bool)
        else:
            dqmask = None

        # get the mask for source finding:
        mask = self._combine_exclude_mask(dqmask)

        x, y, flux, src_id, sharp, round1, round2 = tweakutils.ndfind(
            self.source,
            hmin,
            self.pars['conv_width'],
            skymode,
            sharplim=[self.pars['sharplo'],self.pars['sharphi']],
            roundlim=[self.pars['roundlo'],self.pars['roundhi']],
            peakmin=self.pars['peakmin'],
            peakmax=self.pars['peakmax'],
            fluxmin=self.pars['fluxmin'],
            fluxmax=self.pars['fluxmax'],
            nsigma=self.pars['nsigma'],
            ratio=self.pars['ratio'],
            theta=self.pars['theta'],
            mask=mask,
            use_sharp_round=self.use_sharp_round,
            nbright=self.nbright
        )

        if len(x) == 0:
            if  not self.pars['computesig']:
                sigma = self._compute_sigma()
                hmin = sigma * self.pars['threshold']
                log.info('No sources found with original thresholds. Trying automatic settings.')
                x, y, flux, src_id, sharp, round1, round2 = tweakutils.ndfind(
                    self.source,
                    hmin,
                    self.pars['conv_width'],
                    skymode,
                    sharplim=[self.pars['sharplo'],self.pars['sharphi']],
                    roundlim=[self.pars['roundlo'],self.pars['roundhi']],
                    peakmin=self.pars['peakmin'],
                    peakmax=self.pars['peakmax'],
                    fluxmin=self.pars['fluxmin'],
                    fluxmax=self.pars['fluxmax'],
                    nsigma=self.pars['nsigma'],
                    ratio=self.pars['ratio'],
                    theta=self.pars['theta'],
                    mask = mask,
                    use_sharp_round = self.use_sharp_round,
                    nbright=self.nbright
                )
        if len(x) == 0:
            xypostypes = 3*[float]+[int]+(3 if self.use_sharp_round else 0)*[float]
            self.xypos = [np.empty(0, dtype=i) for i in xypostypes]
            warnstr = textutil.textbox('WARNING: \n'+
                'No valid sources found with the current parameter values!')
            for line in warnstr.split('\n'):
                log.warning(line)
            print(warnstr)
        else:
            # convert the positions from numpy 0-based to FITS 1-based
            if self.use_sharp_round:
                self.xypos = [x+1, y+1, flux, src_id+self.start_id, sharp, round1, round2]
            else:
                self.xypos = [x+1, y+1, flux, src_id+self.start_id]

        log.info('###Source finding finished at: %s'%(util._ptime()[0]))

        self.in_units = 'pixels' # Not strictly necessary, but documents units when determined
        self.sharp = sharp
        self.round1 = round1
        self.round2 = round2
        self.numcols = 7 if self.use_sharp_round else 4
        self.num_objects = len(x)
        self._apply_flux_limits = False # limits already applied by 'ndfind'

    def _compute_sigma(self):
        src_vals = self.source
        if np.any(np.isnan(self.source)):
            src_vals = self.source[np.where(np.isnan(self.source) == False)]
        istats = imagestats.ImageStats(src_vals, nclip=3,
                                       fields='mode,stddev', binwidth=0.01)
        sigma = np.sqrt(2.0 * np.abs(istats.mode))
        return sigma


class UserCatalog(Catalog):
    """ Class to manage user-supplied catalogs as inputs.

        Required input `kwargs` parameters::

            xyunits, xcol, ycol[, fluxcol, [idcol]]

    """
    COLNAMES = COLNAME_PARS
    IN_UNITS = None

    def __init__(self, wcs, catalog_source, **kwargs):
        super().__init__(wcs, catalog_source, **kwargs)
        self._apply_flux_limits = True

    def set_colnames(self):
        self.colnames = []

        cnum = 1
        for cname in self.COLNAMES:
            if cname in self.pars and not util.is_blank(self.pars[cname]):
                self.colnames.append(self.pars[cname])
            else:
                # Insure that at least x and y columns had default values
                if 'fluxcol' not in cname:
                    self.colnames.append(str(cnum))
                cnum += 1

        # count the number of columns
        self.numcols = len(self.colnames)

        if self.IN_UNITS is not None:
            self.in_units = self.IN_UNITS
        else:
            self.in_units = self.pars['xyunits']

    def _readCatalog(self):
        # define what columns will be read
        # The following loops
        #colnums = [self.pars['xcol']-1,self.pars['ycol']-1,self.pars['fluxcol']-1]

        # read the catalog now, one for each chip/mosaic
        # Currently, this only supports ASCII catalog files
        # Support for FITS tables needs to be added
        catcols = tweakutils.readcols(self.source, cols=self.colnames)
        if not util.is_blank(catcols) and len(catcols[0]) == 0:
            catcols = None
        return catcols

    def generateXY(self, **kwargs):
        """
        Method to interpret input catalog file as columns of positions and fluxes.
        """
        self.num_objects = 0
        xycols = self._readCatalog()

        if xycols is not None:
            # convert the catalog into attribute
            self.xypos = xycols[:3]
            # convert optional columns if they are present
            if self.numcols > 3:
                self.xypos.append(np.asarray(xycols[3], dtype=int)) # source ID
            if self.numcols > 4:
                self.sharp = xycols[4]
            if self.numcols > 5:
                self.round1 = xycols[5]
            if self.numcols > 6:
                self.round2 = xycols[6]
            self.num_objects = len(xycols[0])

        if self.numcols < 3: # account for flux column
            self.xypos.append(np.zeros(self.num_objects, dtype=float))
            self.flux_col = False

        if self.numcols < 4: # add source ID column
            self.xypos.append(np.arange(self.num_objects)+self.start_id)

        if self.use_sharp_round:
            for i in range(len(self.xypos), 7):
                self.xypos.append(np.zeros(self.num_objects, dtype=float))
            self.sharp_col = False

        if self.pars['xyunits'] == 'degrees':
            self.radec = [x.copy() for x in self.xypos]
            if self.wcs is not None:
                self.xypos[:2] = list(self.wcs.all_world2pix(np.array(self.xypos[:2]).T, self.origin).T)

    def plotXYCatalog(self, **kwargs):
        """
        Plots the source catalog positions using matplotlib's `pyplot.plot()`

        Plotting `kwargs` that can also be passed include any keywords understood
        by matplotlib's `pyplot.plot()` function such as::

            vmin, vmax, cmap, marker

        """
        try:
            from matplotlib import pyplot as pl
        except:
            pl = None

        if pl is not None:
            pl.clf()
            pl.plot(self.xypos[0],self.xypos[1],**kwargs)


class RefCatalog(UserCatalog):
    """ Class which manages a reference catalog.

    Notes
    -----
    A *reference catalog* is defined as a catalog of undistorted source positions
    given in RA/Dec which would be used as the master list for subsequent
    matching and fitting.

    """
    COLNAMES = REFCOL_PARS
    IN_UNITS = 'degrees'
    PAR_PREFIX = "r"
    PAR_NBRIGHT_PREFIX = 'ref'

    def __init__(self, wcs, catalog_source, **kwargs):
        super().__init__(wcs, catalog_source, **kwargs)
        self._apply_flux_limits = True

    def generateXY(self, **kwargs):
        return

    def generateRaDec(self):
        self.prefix = self.PAR_PREFIX
        if isinstance(self.source,list):
            self.radec = self.source
        else:
            self.radec = self._readCatalog()

    def buildXY(self,catalogs):
        return
