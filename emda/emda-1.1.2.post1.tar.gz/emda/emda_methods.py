# Caller script
from __future__ import absolute_import, division, print_function, unicode_literals

def read_map(mapname):
    import emda.iotools
    uc,arr,origin = emda.iotools.read_map(mapname)
    return uc,arr,origin

def read_mtz(mtzfile):
    import emda.iotools
    uc,df = emda.iotools.read_mtz(mtzfile)
    return uc,df

def write_mrc(mapdata,filename,unit_cell,map_origin=[0.0,0.0,0.0]):
    import emda.iotools
    emda.iotools.write_mrc(mapdata,
                           filename,
                           unit_cell,
                           map_origin)

def write_mtz(uc,arr,outfile='output.mtz'):
    import emda.iotools
    emda.iotools.write_3d2mtz(uc,
                              arr,
                              outfile='output.mtz')

def resample_data(target_pix_size,target_dim,uc,arr):
    import emda.iotools
    new_arr = emda.iotools.resample2staticmap(target_pix_size,
                                         target_dim,
                                         uc,
                                         arr)
    return new_arr

def estimate_map_resol(hfmap1name,hfmap2name):
    import emda.maptools
    map_resol = emda.maptools.estimate_map_resol(hfmap1name,hfmap2name)
    return map_resol

def get_map_power(mapname):
    import emda.maptools
    res_arr,power_spectrum = emda.maptools.get_map_power(mapname)
    return res_arr,power_spectrum

def get_biso_from_model(mmcif_file):
    import emda.maptools
    biso = emda.maptools.get_biso_from_model(mmcif_file)
    return biso

def get_biso_from_map(halfmap1,halfmap2):
    import emda.maptools
    biso = emda.maptools.get_biso_from_map(halfmap1,halfmap2)
    return biso

def apply_bfactor_to_map(mapname,bf_arr,mapout):
    import emda.maptools
    all_mapout = emda.maptools.apply_bfactor_to_map(mapname,
                                                    bf_arr,
                                                    mapout)
    return all_mapout
    
def map2mtz(mapname,mtzname='map2mtz'):
    import emda.maptools
    emda.maptools.map2mtz(mapname,mtzname='map2mtz')

def mtz2map(mtzname,map_size):
    import emda.maptools
    data2write = emda.maptools.mtz2map(mtzname,map_size)
    return data2write

def lowpass_map(mapname, resol):
    import emda.lowpass_map
    emda.lowpass_map.lowpass_map(mapname, resol)

def half2full(half1name,half2name):
    import emda.half2full
    uc,arr1,origin = read_map(half1name)
    uc,arr2,origin = read_map(half2name)
    fullmap = emda.half2full.half2full(arr1, arr2)
    write_mrc(fullmap,'fullmap.mrc',uc,origin)
    return fullmap

def map_transform(mapname,t,r,ax,outname):
    import emda.transform_map
    transformed_map = emda.transform_map.map_transform(mapname,
                                                       t,
                                                       r,
                                                       tuple(ax),
                                                       outname)
    return transformed_map

def halfmap_fsc(half1name,half2name,filename=None):
    import emda.restools
    import emda.fsc
    import numpy as np
    import os
    uc,arr1,origin = read_map(half1name)
    uc,arr2,origin = read_map(half2name)
    hf1 = np.fft.fftshift(np.fft.fftn(arr1))
    hf2 = np.fft.fftshift(np.fft.fftn(arr2))
    nbin,res_arr,bin_idx = emda.restools.get_resolution_array(uc,hf1)
    bin_fsc,noisevar,signalvar,totalvar,_,_ = emda.fsc.halfmaps_fsc_variance(hf1,
                                                            hf2,bin_idx,nbin)
    if filename is not None: 
        tdata = open(filename, "w") 
        tdata.write('halfmap1 file: %s\n' %os.path.abspath(half1name))
        tdata.write('halfmap2 file: %s\n' %os.path.abspath(half2name))
        tdata.write('\n')
        tdata.write('bin # \n')  
        tdata.write('resolution (Ang.) \n') 
        tdata.write('signal variance \n')  
        tdata.write('noise variance \n')  
        tdata.write('total variance \n')  
        tdata.write('halfmap fsc \n')                                                   
        for i in range(len(res_arr)):
            sv = signalvar[i]
            nv = noisevar[i]
            tv = totalvar[i]
            fsc = bin_fsc[i]
            tdata.write("{:-3d} {:-6.2f} {:-14.4f} {:-14.4f} {:-14.4f} {:-14.4f}\n".format(i, 
                                                                      res_arr[i], 
                                                                      sv, nv, tv, 
                                                                      fsc))
    print('Bin    Resolution     FSC')
    for i in range(len(res_arr)):
        print("{:.2f} {:14.4f}".format(res_arr[i], bin_fsc[i]))
    return res_arr,bin_fsc

def twomap_fsc(map1name,map2name,fobj=None):
    import emda.restools
    import emda.fsc
    import numpy as np
    import os
    uc,arr1,origin = read_map(map1name)
    uc,arr2,origin = read_map(map2name)
    f1 = np.fft.fftshift(np.fft.fftn(arr1))
    f2 = np.fft.fftshift(np.fft.fftn(arr2))
    nbin,res_arr,bin_idx = emda.restools.get_resolution_array(uc,f1)
    bin_fsc,f1f2_covar = emda.fsc.anytwomaps_fsc_covariance(f1,f2,bin_idx,nbin)
    if fobj is not None: 
        fobj.write('map1 file: %s\n' %os.path.abspath(map1name))
        fobj.write('map2 file: %s\n' %os.path.abspath(map2name))
        fobj.write('\n')
        fobj.write('bin # \n')  
        fobj.write('resolution (Ang.) \n')  
        fobj.write('fsc \n')                                                   
        for bin, fsc in enumerate(bin_fsc):
            fobj.write("{:5d} {:6.2f} {:6.3f}\n".format(bin, 
                                                         res_arr[bin], 
                                                         fsc))
    print('Bin      Resolution     FSC')
    for bin, fsc in enumerate(bin_fsc):
        print("{:5d} {:6.2f} {:6.3f}".format(bin, res_arr[bin], fsc))
    return res_arr,bin_fsc

def singlemap_fsc(map1name):
    import emda.restools
    import emda.fsc
    import numpy as np
    from emda.fakehalf import fakehalf
    uc,arr1,origin = read_map(map1name)
    f1 = np.fft.fftshift(np.fft.fftn(np.fft.fftshift(arr1)))
    f2 = fakehalf(f1)
    data2write = np.real(np.fft.ifftshift(np.fft.ifftn(np.fft.ifftshift(f2))))
    write_mrc(data2write,'fakehalf.mrc',uc,origin)
    nbin,res_arr,bin_idx = emda.restools.get_resolution_array(uc,f1)
    #bin_fsc,f1f2_covar = emda.fsc.anytwomaps_fsc_covariance(f1,f2,bin_idx,nbin)
    bin_fsc,noisevar,signalvar,totalvar,fo,eo = emda.fsc.halfmaps_fsc_variance(f1,
                                                            f2,bin_idx,nbin)
    print('Resolution bin     FSC')
    for i in range(len(res_arr)):
        print("{:.2f} {:.4f}".format(res_arr[i], bin_fsc[i]))
    return res_arr,bin_fsc

def mask_from_halfmaps(half1name, half2name, maskname='halfmap_mask.mrc'):
    import emda.maskmap_class
    uc,arr1,origin = read_map(half1name)
    uc,arr2,origin = read_map(half2name)
    obj_maskmap = emda.maskmap_class.MaskedMaps()
    obj_maskmap.generate_mask(arr1, arr2)
    mask = obj_maskmap.mask
    write_mrc(mask,maskname,uc,origin)
    return mask

def sphere_kernel_softedge(radius=5):
    import emda.restools
    kernel = emda.restools.create_soft_edged_kernel_pxl(radius)
    return kernel

def overlay_maps(maplist,masklist,tra,rot,ax,ncy,res,fobj,interp):
    from emda.mapfit import mapoverlay
    theta_init = [tuple(ax),rot]
    mapoverlay.main(maplist=maplist,
                    masklist=masklist,
                    ncycles=ncy,
                    t_init=tra,
                    theta_init=theta_init,
                    smax=res,
                    fobj=fobj,
                    interp=interp)

def average_maps(maplist,masklist,tra,rot,ax,ncy,res,fobj):
    from emda.mapfit import mapaverage
    theta_init = [tuple(ax),rot]
    mapaverage.main(maplist=maplist,
                    masklist=masklist,
                    ncycles=ncy,
                    t_init=tra,
                    theta_init=theta_init,
                    smax=res,
                    fobj=fobj)

def realsp_correlation(half1map, half2map, kernel_size, model=None, model_resol=None, mask_map=None):
    from emda.realsp_corr_3d import rcc
    rcc(half1map, half2map, kernel_size, model, model_resol, mask_map)

def fouriersp_correlation(half1_map, half2_map, kernel_size):
    from emda.fouriersp_corr_3d import fcc
    fcc(half1_map, half2_map, kernel_size)

def map_model_validate(half1map, half2map, modelfpdb, model1pdb, mask, mapsize, modelresol):
    from emda.map_fsc import map_model_fsc
    map_model_fsc(half1map, half2map, modelfpdb, model1pdb, mask, mapsize, modelresol)

def difference_map(mapname1, mapname2):
    import numpy as np
    from emda.mapfit import difference
    uc,arr1,origin = read_map(mapname1)
    _,arr2,_ = read_map(mapname2)
    f1 = np.fft.fftshift(np.fft.fftn(np.fft.fftshift(arr1)))
    f2 = np.fft.fftshift(np.fft.fftn(np.fft.fftshift(arr2)))
    difference.difference_map(f1, f2, uc,origin)
    '''dm1_dm2 = np.real(np.fft.ifftshift(
                         np.fft.ifftn(
                         np.fft.ifftshift(f1 - f2))))
    dm2_dm1 = np.real(np.fft.ifftshift(
                         np.fft.ifftn(
                         np.fft.ifftshift(f2 - f1))))
    write_mrc(dm1_dm2,'diffmap_m1-m2.mrc',uc,origin)
    write_mrc(dm2_dm1,'diffmap_m2-m1.mrc',uc,origin)'''

def applymask(mapname, maskname, outname):
    uc,arr1,origin = read_map(mapname)
    _,mask,_ = read_map(maskname)
    write_mrc(arr1*mask,outname,uc,origin)
