#!/usr/bin/env python
from __future__ import print_function

import os
import astropy.io.fits as pf
import numpy as np
import subprocess

try:
	import commands
except:
	pass




def run(cmd,verbose=True):
	print
	print("------------------------------------------------------------------------------------------------")
	print("running ",cmd)


	try:
		out=subprocess.getstatusoutput(cmd)
	except:
		out = commands.getstatusoutput(cmd)

	if verbose==True:
		print(out[1])

	print("------------------------------------------------------------------------------------------------")
	print


def get_resolution_array(rmf):

	ind_matrix=-1
	ind_ebounds=-1

	pf_buffer=pf.open(rmf)


	for i in range(1,len(pf_buffer)):
		extname=pf_buffer[i].header['EXTNAME']
		print(extname)
		if extname == 'MATRIX' or extname == 'SPI.-RMF.-RSP' or extname == 'ISGR-RMF.RSP' or extname == 'SPECRESP MATRIX':
			print('Found matrix')
			ind_matrix=i
		if extname == 'EBOUNDS' or extname =='SPI.-EBDS-MOD' or extname == 'ISGR-EBDS-MOD':
			print('Found energy boundaries')
			ind_ebounds=i

	if(ind_matrix < 0 or ind_ebounds <0):
		print("Could not find Extensions in matrix, exit")
		raise RuntimeError('Error')


	buffer=pf_buffer[ind_ebounds].data
	channel=buffer['CHANNEL']
	#print channel
	emin=buffer['E_MIN']
	emax=buffer['E_MAX']

	chan_offset=int(pf_buffer[ind_matrix].header['TLMIN4'])
	buffer=pf_buffer[ind_matrix].data

	matrix=buffer['MATRIX']
	emin_rmf=buffer['ENERG_LO']
	emax_rmf=buffer['ENERG_HI']
	n_grp=buffer['N_GRP']
	f_chan=buffer['F_CHAN']
	n_chan=buffer['N_CHAN']

	res_array=np.zeros(len(emin_rmf))

	for i in range(len(emin_rmf)):
		if n_grp[i] == 0:
			#This avoids empty bins
			res_array[i]=emax_rmf[i]-emin_rmf[i]
			continue
		max_rsp_local=np.max(matrix[i])
		if max_rsp_local == 0:
			res_array[i]=emax_rmf[i]-emin_rmf[i]
			continue

		## These are ill-built matrixes, typically Suzaku


		#print f_chan[i][0],n_chan[i][0]
		#print type(f_chan[i]).__name__
		#print isinstance(f_chan[i], (list, tuple, np.ndarray))
		#type(f_chan[i]).__name__ in 'int':
		if isinstance(f_chan[i], (list, tuple, np.ndarray)):
			emin_local=emin[f_chan[i][0]-chan_offset:f_chan[i][0]-chan_offset+n_chan[i][0]]
			emax_local=emax[f_chan[i][0]-chan_offset:f_chan[i][0]-chan_offset+n_chan[i][0]]
			#print i, n_grp[i],f_chan[i][0],n_chan[i][0]
			for j in range(1,n_grp[i]):
				#print('concatenate with instance')
				emin_local=np.concatenate([emin_local,emin[f_chan[i][j]-chan_offset:f_chan[i][j]-chan_offset+n_chan[i][j]]])
				emax_local=np.concatenate([emax_local,emax[f_chan[i][j]-chan_offset:f_chan[i][j]-chan_offset+n_chan[i][j]]])
		else:

			emin_local=emin[f_chan[i]-chan_offset:f_chan[i]-chan_offset+n_chan[i]]
			emax_local=emax[f_chan[i]-chan_offset:f_chan[i]-chan_offset+n_chan[i]]
			#print n_grp[i],f_chan[i],n_chan[i]
			for j in range(1,n_grp[i]):
				#print('concatenate')
				emin_local=np.concatenate([emin_local,emin[f_chan[i]-chan_offset:f_chan[i]-chan_offset+n_chan[i]]])
				emax_local=np.concatenate([emax_local,emax[f_chan[i]-chan_offset:f_chan[i]-chan_offset+n_chan[i]]])

		#print("len e_min_local %d len_matrix %d"%(len(emin_local),len(matrix[i])))

		if len(matrix[i]) != len(emin_local):
			print('Inconsistency with matrix and binning, something has gone wrong, aborting')
			print(i, len(emin_local),len(matrix[i]))
			raise RuntimeError('Error')

		ind_fwhm=matrix[i]>(max_rsp_local/2.)
		if(np.count_nonzero(ind_fwhm)==0):
			print("There are no bins larger than half the response, something wrong")
			raise RuntimeError('Error')

		res_array[i]=np.max(emax_local[ind_fwhm])-np.min(emin_local[ind_fwhm])

	pf_buffer.close()

	res_array_resampled=np.interp((emin+emax)/2,(emin_rmf+emax_rmf)/2,res_array)

	# import matplotlib.pyplot as p
    #
	# for i in range(len(emin)):
	# 	print(res_array[i], res_array_resampled[i], emin[i], emax[i])
	# 	i_step = 3
	# 	if (i > 0 and (i / i_step) * i_step == i and matrix[i].max() > 0):
	# 		p.clf()
	# 		p.step((emin_local+emax_local)/2,matrix[i])
	# 		p.yscale('log')
	# 		p.xscale('log')
	# 		p.title('Energy %.3f FWHM %.3f'%( (emin_rmf[i]+emax_rmf[i])/2, res_array[i]))
	# 		p.xlabel('Energy[keV]')
	# 		p.ylabel('SPECRESP')
	# 		p.xlim([10., 1000.])
	# 		p.savefig('plot_%06.3f.png'%( (emin_rmf[i]+emax_rmf[i])/2) )

	return channel,emin,emax,res_array_resampled

help='\nPURPOSE:\nGroup the spectra using Kaastra & Bleeker\'s recipe plus an option for a minimal number of counts\n'
help+='the input spectrum file is grouped using grppha and the output has the _rbn.pi extension added to the root file name\n'
help+='It is recommended not to set a minimum number of counts for spectral fitting of high-resolution spectra\n'
help+='with a line-rich spectrum to avoid large bins that would bias the line centroid determination.\n'
help+='However, it should be noted that Xspec has a problem with C-statistics when there are empmty bins.\n\n'
help+='REFERENCE: Kaastra & Bleeker, 2016, A&A, 587, 151, Sect.5.3\n\n'
help+='The response and background files are taken from the keywords in the input spectrum, but can be overriden by setting the optional parameters.\n\n'
help+='The following parameters can be provided for a custom resolution, otherwise the optimal resolution is derived from the RMF file:\n'
help+='eref = reference energy for energy resolution (keV)\n'
help+='res = resolution at the reference energy (keV)\n'
help+='en_dep = dependence of the resolution on energy (power-law index)\n'
help+='\n\nExamples:\noptimal_binning.py PNspectrum.fits -e 1.7 -E 11 -m 10\n'
help+='optimal_binning.py -r acisf_heg_p1.rmf -a acisf_heg_p1.arf heg_p1.fits -e 2.0\n'
help+='optimal_binning.py hxd_pin_sr.fits -e 12.  -E 60.\n'
help+='optimal_binning.py xi0.pi -e 0.4 -E 11\n'
help+='optimal_binning.py xi0_rbn.pi -e 0.4 -E 11. --eref 6 --en_dep -0.5 --res 0.6\n'
help+='\n\n'
help+='To mimic the typical resolution of current instrumewnts, we provide the following suggestions\n'
help+='Suzaku XIS1 eref=6 res=0.168 en_dep = -0.5\n'
help+='Suzaku XIS0,XIS3 eref=6 res=0.153 en_dep = -0.5\n'
help+='Suzaku PIN eref=15 res=4.125 en_dep = 0\n'
help+='XMM EpicPN eref=6 res=0.175 en_dep = -0.5\n'
help+='XMM EpicMOS eref=6 res=0.155 en_dep = -0.5\n'
help+='\n\nFor bugs and requests email to carlo.ferrigno AT unige.ch\n'
help+='The script can be downloaded from the page http://www.isdc.unige.ch/~ferrigno/index.php/optimal-binning-script\n'
#
# parser = argparse.ArgumentParser(description='Optimal grouping for the spectrum',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
# parser.add_argument('Spectrum', metavar='fname', type=str, nargs=1,
# 					help='Spectrum PHA1 file')
# parser.add_argument("-b", "--backname", help="Background file", type=str, default='none')
# parser.add_argument("-r", "--respname", help="RMF or RSP file (response matrix)", type=str, default='none')
# parser.add_argument("-a", "--ancrname", help="ARF file (effective area)", type=str, default='none')
# parser.add_argument("-e", "--mine", help="Minimum energy (keV), default is minimum of response", type=float, default=-10)
# parser.add_argument("-E", "--maxe", help="Maximum energy (keV), default is maximum of response", type=float, default=1e10)
# parser.add_argument("-m", "--mincounts", help="Minimum number of counts per bin (for Xspec >0, for other instruments also 0)", type=float, default=-1e10)
# parser.add_argument("--eref", help="reference energy for custom resolution (keV)", type=float, default=-1)
# parser.add_argument("--res", help="resolution at the reference energy for custom input (keV)", type=float, default=-1)
# parser.add_argument("--en_dep", help="energy dependence of resolution (power-law index) for custom input (keV)", type=float, default=-1)


def execute_binning(spectrum, bkg, rmf, arf, mine=-10, maxe=1e10, min_counts=0, eref=-1, res=-1, en_dep=-1):

    if mine >= maxe:
        raise RuntimeError("MinE > = MaxE (%f,%f)"%(mine,maxe))


    if (eref <=0 and res >= 0) or (eref >=0 and res <=0):
        raise RuntimeError('Optional arguments must be provided with positive reference energy and resolution\n\n'+help)

    if os.environ.get('HEADAS') is None:
        raise RuntimeError('Please, initialize the Heasoft environemnt, we use the \"grppha\" program for grouping the spectrum')

    if not os.path.isfile(spectrum):

        raise RuntimeError('Error: file %s does not exist'%(spectrum))

    #
    # Read counts from the spectral files
    #
    buffer=pf.open(spectrum)
    ind_spectrum=-1
    for i in range(1,len(buffer)):
        extname=buffer[i].header['EXTNAME']
        print(extname)
        if extname in ['SPECTRUM','ISGR-EVTS-SPE', 'ISGR-PHA1-SPE', 'JMX1-PHA1-SPE', 'JMX2-PHA1-SPE']:
            ind_spectrum=i

    if ind_spectrum <0:
        raise RuntimeError("Cannot find spectrum")

    src_exposure=float(buffer[ind_spectrum].header['EXPOSURE'])


    #src_channel=buffer[ind_spectrum].data['CHANNEL']
    try:
        src_counts=buffer[ind_spectrum].data['COUNTS']
    except:
        try:
            src_counts=buffer[ind_spectrum].data['RATE'] * src_exposure
        except (KeyError):
            raise RuntimeError("No COUNTS or RATE column in spectrum")

    try:
        src_backscal=float(buffer[ind_spectrum].header['BACKSCAL'])
    except (KeyError):
        print("No BACKSCAL keyword in %s defaulting to 1"%(spectrum))
        src_backscal=1

    try:
        quality=buffer[ind_spectrum].data['QUALITY']
    except (KeyError):
        quality=np.zeros(len(src_counts))


    if rmf == 'none':
        rmf=buffer[ind_spectrum].header['RESPFILE']

    if arf =='none':
        arf=buffer[ind_spectrum].header['ANCRFILE']

    if bkg == 'none':
        bkg=buffer[ind_spectrum].header['BACKFILE']

    buffer.close()

    if not os.path.isfile(rmf):
        print('The response file %s does not exist, check if you provided a custom resolution'%(rmf))
        if (eref <=0 or res <= 0):
            raise RuntimeError("The values of \"eref\"=%f or \"res\"=%f are negative and you have not provided a valid RMF, the script cannot be used with this input"%(eref,res))

    else:
        #
        # Read energy grid from the RMF file
        #
        channel,emin,emax,res_array=get_resolution_array(rmf)

    #Use energy grid and set minimum energy to the boundaries of RMF, if not selected by the user
    energy=(emin+emax)/2.0

    #The implementation assumes a monothonic ascending energy, we use this for RGS spectra
    if energy[0] > energy[-1]:
        energy *= -1
        tmp=mine
        mine=-maxe
        maxe=-tmp


    if mine == -10 or mine == -1e10:
        mine=energy.min()
    if maxe == 1e10 or maxe == -10:
        maxe=energy.max()

    if mine < energy.min():
        mine = energy.min()
    if maxe > energy.max():
        maxe = energy.max()

    #
    # Print input values
    #

    parameter_string="\nWe will use the following input parameters:\n"
    parameter_string+="spectrum   = %s\n"%(spectrum)
    if(eref >0 and res >0):
        parameter_string+="res        = %g keV\n"%(res)
        parameter_string+="E_ref      = %g keV\n"%(eref)
        parameter_string+="E_dep      = %g\n"%(en_dep)
    else:
        parameter_string+="RMF        = %s\n"%(rmf)

    parameter_string+="ARF        = %s\n"%(arf)
    parameter_string+="background = %s\n"%(bkg)
    parameter_string+="min_counts = %g\n"%(min_counts)
    parameter_string+="Emin       = %g\n"%(mine)
    parameter_string+="Emax       = %g\n"%(maxe)
    parameter_string+="\n"

    print(parameter_string)



    #
    # Read counts from the spectral files
    #

    #bkg_channel=src_channel
    bkg_counts=np.zeros(len(src_counts))
    bkg_exposure=1
    bkg_backscal=1

    #for lower case test
    bkg_test=bkg

    print(bkg_test)

    if(bkg_test.lower() != 'none'):

        buffer = pf.open(bkg)
        try:
            bkg_exposure = float(buffer[1].header['EXPOSURE'])
        except:
            print("Not found background exposure, defaulting to the source exposure %g s"%src_exposure)
            bkg_exposure=src_exposure

        try:
            bkg_backscal = float(buffer[1].header['BACKSCAL'])
        except (KeyError):
            print("No BACKSCAL keyword in %s defaulting to 1" % (bkg))
            bkg_backscal = 1

        bkg_channel = buffer[1].data['CHANNEL']

        try:
            bkg_counts = buffer[1].data['COUNTS']
            bkg_err = np.sqrt(bkg_counts)
        except:
            try:
                bkg_rate = buffer[1].data['RATE']
                bkg_rate_err = buffer[1].data['STAT_ERR']
                bkg_counts = bkg_rate * bkg_exposure
                bkg_err = bkg_rate_err * bkg_exposure
            except:
                print("ERROR: Impossible to read COUNTS or RATE from background")
                os.exit(1)


        buffer.close()

    #print "SRC", src_exposure, src_backscal
    #print "BKG", bkg_exposure, bkg_backscal

    #
    # Calculates the oversample factor as an array
    #
    #if res <=0:
    #	res=np.mean(res_array)

    r=(maxe-mine)/res
    if r>1e4:
        print('Warning: the resolution is not accurate')

    net_counts=src_counts - bkg_counts * src_backscal / bkg_backscal
    summed_net_counts = np.zeros(len(net_counts))

    #Equations are not defined for negative or zero counts
    ind=net_counts <= 0
    net_counts[ind] = 1

    #Builds net counts in FWHM
    #Eq. B2-B4 with h_r=1.314
    for i,de in enumerate(res_array):
        ind1 = emin >= (emin[i] - res_array[i]/2)
        ind2 = emax <= (emax[i] + res_array[i]/2)

        ind = np.logical_and(ind1,ind2)
        summed_net_counts[i] = np.sum(net_counts[ind])  *  1.314 #Not matrix derivative is available


    #Eq. B1
    r_vec =  (emax - emin) / res_array #This was a possible implementation
    r = np.sum(r_vec)

    print ("resolution elements %g"%(r))

    #Eq. 37
    x = np.log(summed_net_counts*(1+0.20*np.log(r)))

    #tot_logcounts=np.log(np.sum(src_counts)*(1+0.20*np.log(r)))
    #Eq. 19
    #y=1.404 / x **0.25 * (1+18/x)

    #Eq. 36
    oversample=np.ones(len(x))
    ind = x > 2.119
    oversample[ind] = (0.08 + 7.0 /x[ind] + 1.8 / x[ind]**2) / (1+5.9/x[ind])

    #
    # print('Oversample factor=\n')
    # for oo in oversample:
    # 	print("%.2f "%oo)
    # print("\n")

    #
    # Build the rebinning file
    #
    outfile=('.').join(spectrum.split('.')[:-1])+'.rbn'
    outspectrum=('.').join(spectrum.split('.')[:-1])+'_rbn.pi'
    lun=open(outfile,'w')

    #index_min=len(channel)
    nbins=0

    ind_start=(np.abs(energy - mine)).argmin()
    ind_stop =(np.abs(energy - maxe)).argmin()

    chanmin=channel[ind_start]
    #chanmax=channel[ind_start]
    energymin=mine
    energymax=mine
    ind_min=ind_start
    #ind_max=ind_start


    #print ind_start, ind_stop
    #print energy
    #print res_array


    while energymax < maxe:
        this_energy=(energymin+energymax)/2.0
        ind_energy=(np.abs(energy - this_energy)).argmin()
        if(eref >0 and res >0):
            this_resolution=res*(this_energy/eref)**en_dep
        #print this_energy,this_resolution, res_array[ind_energy], this_resolution-res_array[ind_energy]
        else:
            this_resolution=res_array[ind_energy]
        #print this_energy,this_resolution, res_array[ind_energy], this_resolution-res_array[ind_energy]

        energymax=energymin+this_resolution * oversample[ind_energy]

        #This is an attempt
        #energymax = this_energy + this_resolution / oversample

        if ind_energy < len(energy)-1:
            if (energymax <= energy[ind_energy+1]):
                energymax = energy[ind_energy+1]
                #print "Make a change"
        else:
            energymax=energy.max()


        ind_max=np.argmin(np.abs(energy-energymax))
        chanmax=channel[ind_max]

        #print(energymin, energymax, this_energy, this_resolution, res_array[ind_energy],
        #	  this_resolution - res_array[ind_energy], chanmin, chanmax)

        #    if chanmax < chanmin:
    #        chanmax=chanmin
    #        ind_max=np.argmin(np.abs(channel-chanmax))
    #        energymin=energy[ind_max]
    #        energymax=energy[ind_max]
        #This is the minimal resolution, now accumulates enough photons in each bin
        bs_totcounts=0
        nbins=1
    #This loops increment nbins for option min_counts>0
        while chanmax <= np.max(channel):


        #Quality check
            #print quality[ind_min:ind_max]
            if np.sum(quality[ind_min:ind_max]) > 0:
                print("Interval of channels with index %d-%d has bad quality, skip"%(ind_min,ind_max))
                quality[ind_min:ind_max]=quality[ind_min:ind_max]*0+1
                chanmin=chanmax+1
                ind_min=ind_max
                energymin=energymax
                nbins=1
                break
            src_totcounts=np.sum(src_counts[ind_min:ind_max])
            bkg_totcounts=np.sum(bkg_counts[ind_min:ind_max])
            bs_totcounts=src_totcounts-bkg_totcounts*(src_exposure/bkg_exposure)*(src_backscal/bkg_backscal)
            #print energymin, energymax, chanmin, chanmax, ind_min, ind_max, src_totcounts, bkg_totcounts, bs_totcounts, nbins
    #        if energymin==energymax:
    #            print "REQRWEREWRW"
    #            raise RuntimeError('Error')
            if (bs_totcounts >= min_counts):
                lun.write("%d %d %d\n"%(chanmin, chanmax, chanmax-chanmin+1))
                #print "Found one rebin"
                #reset to start over
                chanmin=chanmax+1
                ind_min=ind_max
                energymin=energymax
                nbins=1
                break
            else:
                chanmax=chanmin+nbins
                ind_max=ind_min+nbins
                if (chanmax >= np.max(channel) or ind_min+nbins >= len(energy) ):
                    lun.write("%d %d %d\n"%(chanmin, chanmax, chanmax-chanmin+1))
                    print("Got to the end, exiting loop")
                    energymax=maxe
                    break #i0=len(channel)
                else:
                    energymax=energy[ind_min+nbins]
                    nbins+=1


    #chanmax=chanmax+nbins

       #print index_min, nbins, len(energy)-1


    lun.close()

    print('Rebinning file: '+outfile)
    #
    # Apply the rebinning file through grppha
    #




    print("Applying rebinning via grppha ...")
    os.system('/bin/rm -rf '+outspectrum+' > /dev/null')
    cmd='grppha infile='+spectrum+' outfile='+outspectrum+' comm=\"reset grouping & bad %d-%d %d-%d & group '%(channel.min(),channel[ind_start],channel[ind_stop],channel.max())+outfile+' & chkey RESPFILE '+os.path.basename(rmf)+' & chkey ANCRFILE '+os.path.basename(arf)+' & chkey BACKFILE '+os.path.basename(bkg)+' & exit\" > /dev/null'
    if run(cmd):
        print("Attention: probable error with \"grppha\" program execution")
    os.system('/bin/rm -rf '+outfile+' > /dev/null')

    if np.sum(quality) >0 :
        #print quality
        print("Update the quality column with the new values discard 0-%d, %d-"%(ind_start,ind_stop))
        quality[0:ind_start]=1
        quality[ind_stop:]=1
        #print quality
        outptr=pf.open(outspectrum,"update")
        outptr[1].data['QUALITY']=quality
        outptr.close()


    #convert   -delay 50   -loop 0   `ls plot_??.???.gif | sort -r`   animated_rmf_PN_timing_mode.gif
