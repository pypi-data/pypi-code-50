"""
Author: "Rangana Warshamanage, Garib N. Murshudov"
MRC Laboratory of Molecular Biology
    
This software is released under the
Mozilla Public License, version 2.0; see LICENSE.
"""
from __future__ import absolute_import, division, print_function, unicode_literals
import numpy as np
import argparse
import sys
import datetime

cmdl_parser = argparse.ArgumentParser(prog='emda', 
                                      usage='%(prog)s [commands] [arguments]')
subparsers = cmdl_parser.add_subparsers(dest='command')#, title="Options")

mapinfo = subparsers.add_parser('info', 
                                description='Output basic information of map')
mapinfo.add_argument('--map',required=True, help='input map')

anyfsc = subparsers.add_parser('fsc', 
                                description='Calculates FSC between any two maps')
anyfsc.add_argument('--map1',required=True, help='input map1 map')
anyfsc.add_argument('--map2',required=True, help='input map2 map')

halffsc = subparsers.add_parser('halffsc', 
                                 description='Calculates FSC between half-maps')
halffsc.add_argument('--h1',required=True, help='input map1 map')
halffsc.add_argument('--h2',required=True, help='input map2 map')
halffsc.add_argument('--out',required=False, 
                            default='table_variances.txt', help='output data table')

singlemapfsc = subparsers.add_parser('singlemapfsc', 
                                     description='Calculates FSC using neighbour average')
singlemapfsc.add_argument('--h1',required=True, help='input map1 map')

ccmask = subparsers.add_parser('ccmask', 
                                description='Generates mask based on halfmaps correlation')
ccmask.add_argument('--h1',required=True, help='input halfmap1 map')
ccmask.add_argument('--h2',required=True, help='input halfmap2 map')

lowpass = subparsers.add_parser('lowpass',
                                description='lowpass filter to specified resolution')
lowpass.add_argument('--map',required=True, help='input map (mrc/map)')
lowpass.add_argument('--res',required=True, type=float, help='lowpass resolution (A)')

power = subparsers.add_parser('power', description='calculates power spectrum')
power.add_argument('--map',required=True, help='input map (mrc/map)')

applybfac = subparsers.add_parser('bfac', description='apply a B-factor to map')
applybfac.add_argument('--map',required=True, help='input map (mrc/map)')
applybfac.add_argument('--bfc',required=True, nargs='+', 
                        type=float, help='bfactor(s) to apply')
#applybfac.add_argument('--out',required=False, 
#                        default=False, type=bool, help='if use write out maps')
applybfac.add_argument('--out', action='store_true', help='write out map')

map_resol = subparsers.add_parser('resol', 
                                   description='estimates map resolution based on FSC')
map_resol.add_argument('--h1',required=True, help='input halfmap1 map')
map_resol.add_argument('--h2',required=True, help='input halfmap2 map')

half2full = subparsers.add_parser('half2full', 
                                   description='combine two halfmaps to give fullmap')
half2full.add_argument('--h1',required=True, help='input halfmap1 map')
half2full.add_argument('--h2',required=True, help='input halfmap2 map')

conv_mrc2mtz = subparsers.add_parser('mrc2mtz', description='MRC/MAP to MTZ conversion')
conv_mrc2mtz.add_argument('--map',required=True, help='input map (mrc/map)')
conv_mrc2mtz.add_argument('--out',required=True, help='output map (mtz)')

transform_map = subparsers.add_parser('transform', 
                                       description='apply a transformation to the map')
transform_map.add_argument('--map',required=True, help='input map (mrc/map)')
transform_map.add_argument('--tra',required=False, default=[0.0, 0.0, 0.0], 
                            nargs='+', type=float, help='translation vec.')
transform_map.add_argument('--rot',required=False, default=0.0, 
                            type=float, help='rotation in deg')
transform_map.add_argument('--axr',required=False, default=[1,0,0], 
                            nargs='+', type=int, help='rotation axis')
transform_map.add_argument('--out',required=False, 
                            default='transformed.mrc', help='output map (mrc/map)')

conv_mtz2mrc = subparsers.add_parser('mtz2mrc', description='MTZ to MRC/MAP conversion')
conv_mtz2mrc.add_argument('--mtz',required=True, help='input map (mtz)')
conv_mtz2mrc.add_argument('--map',required=True, help='input map (mrc/map)')
conv_mtz2mrc.add_argument('--out',required=True, help='output map (mrc/map)')

resample_d = subparsers.add_parser('resample', description='resample map')
resample_d.add_argument('--map',required=True, help='input map (mrc/map)')
resample_d.add_argument('--pix',required=True, type=float, help='target pixel size (A)')
resample_d.add_argument('--dim', required=False, 
                         default=None, nargs='+', type=np.int, help='target map dim ')
#resample_d.add_argument('--cel', required=False, 
#                         default=None, nargs='+', type=np.float, help='target unit cell ')
resample_d.add_argument('--out',required=False, 
                         default='resampled.mrc', help='output map name')

realspc = subparsers.add_parser('rcc', description='real space correlation')
realspc.add_argument('--h1',required=True, help='input halfmap1 map')
realspc.add_argument('--h2',required=True, help='input halfmap2 map')
realspc.add_argument('--mdl', required=False, help='Input model (map/mrc/mtz/pdb)')
realspc.add_argument('--res', required=False, type=float, help='Resolution (A)')
realspc.add_argument('--msk', required=False, help='input mask (mrc/map)')
realspc.add_argument('--knl', required=False, 
                      type=int, default=5, help='Kernel size (pixels)')

fourierspc = subparsers.add_parser('fcc', description='Fourier space correlation')
fourierspc.add_argument('--h1',required=True, help='input halfmap1 map')
fourierspc.add_argument('--h2',required=True, help='input halfmap2 map')
fourierspc.add_argument('--knl', required=False, 
                         type=int, default=5, help='Kernel size (pixels)')

mapmodelfsc = subparsers.add_parser('mapmodelfsc', description='map-model correlation')
mapmodelfsc.add_argument('--h1', required=True, help='input halfmap1 map')
mapmodelfsc.add_argument('--h2', required=True, help='input halfmap2 map')
mapmodelfsc.add_argument('--mdf', required=True, help='input full atomic model')
mapmodelfsc.add_argument('--md1', required=True, help='input halfmap1 atomic model')
mapmodelfsc.add_argument('--msk', required=False, help='input mask (mrc/map)')
mapmodelfsc.add_argument('--res', required=False, type=float, help='Resolution (A)')
mapmodelfsc.add_argument('--dim', required=False, nargs='+', type=np.int, help='map dim ')

mapoverlay = subparsers.add_parser('overlay', description='overlay maps')
mapoverlay.add_argument('--map',required=True, nargs='+', 
                         type=str, help='maplist for overlay')
mapoverlay.add_argument('--msk',required=False, default=None, 
                         nargs='+', type=str, help='masklist for overlay')
mapoverlay.add_argument('--tra',required=False, default=[0.0, 0.0, 0.0], 
                         nargs='+', type=float, help='translation vec.')
mapoverlay.add_argument('--rot',required=False, default=0.0, 
                         type=float, help='rotation in deg')
mapoverlay.add_argument('--axr',required=False, default=[1,0,0], 
                         nargs='+', type=int, help='rotation axis')
mapoverlay.add_argument('--ncy',required=False, default=5, 
                         type=int, help='number of fitting cycles')
mapoverlay.add_argument('--res',required=False, default=6, 
                         type=float, help='starting fit resol. (A)')
mapoverlay.add_argument('--int',required=False, default='linear', 
                         type=str, help='interpolation method ([linear]/cubic)')

mapaverage = subparsers.add_parser('average', description='weighted average of several maps')
mapaverage.add_argument('--map',required=True, nargs='+', 
                         type=str, help='maplist to average')
mapaverage.add_argument('--msk',required=False, default=None, 
                         nargs='+', type=str, help='masklist for maps')
mapaverage.add_argument('--tra',required=False, default=[0.0, 0.0, 0.0], 
                         nargs='+', type=float, help='translation vec.')
mapaverage.add_argument('--rot',required=False, default=0.0, 
                         type=float, help='rotation in deg')
mapaverage.add_argument('--axr',required=False, default=[1,0,0], 
                         nargs='+', type=int, help='rotation axis')
mapaverage.add_argument('--ncy',required=False, default=10, 
                         type=int, help='number of fitting cycles')
mapaverage.add_argument('--res',required=False, default=6, 
                         type=float, help='starting fit resol. (A)')

diffmap = subparsers.add_parser('diffmap', 
                                   description='difference map using average maps')
diffmap.add_argument('--m1',required=True, help='input map1')
diffmap.add_argument('--m2',required=True, help='input map2')

applymask = subparsers.add_parser('applymask', 
                                   description='apply mask on the map')
applymask.add_argument('--map',required=True, help='map to be masked')
applymask.add_argument('--msk',required=True, help='mask to be applied')
applymask.add_argument('--out',required=False, 
                         default='mapmasked.mrc', help='output map name')

'''rebox = subparsers.add_parser('rebox', 
                                   description='rebox map to given dimensions')
rebox.add_argument('--map',required=True, help='input map')
rebox.add_argument('--out',required=True, help='output map')
rebox.add_argument('--dim', required=True, nargs='+', type=np.int, help='map dim ')'''

def apply_mask(args):
    from emda.emda_methods import applymask
    applymask(args.map, args.msk, args.out)

def map_info(args):
    from emda.emda_methods import read_map
    uc,arr,origin = read_map(args.map)
    print('Unit cell: ', uc)
    print('Sampling: ', arr.shape)
    print('Pixel size: ', round(uc[0]/arr.shape[0], 3))
    print('Origin: ', origin)

def anymap_fsc(args,fobj):
    from emda.emda_methods import twomap_fsc
    from emda import plotter
    res_arr, bin_fsc = twomap_fsc(args.map1, args.map2, fobj=fobj)
    plotter.plot_nlines(res_arr,
                        [bin_fsc],
                        'twomap_fsc.eps',
                        curve_label=["twomap_fsc"])

def halfmap_fsc(args):
    from emda.emda_methods import halfmap_fsc
    from emda import plotter
    res_arr, bin_fsc = halfmap_fsc(args.h1, args.h2, args.out)
    plotter.plot_nlines(res_arr,
                        [bin_fsc],
                        'halfmap_fsc.eps',
                        curve_label=["halfmap_fsc"])

def singlemap_fsc(args):
    from emda.emda_methods import singlemap_fsc as sfsc
    from emda import plotter
    res_arr, bin_fsc = sfsc(args.h1)
    plotter.plot_nlines(res_arr,
                        [bin_fsc],
                        'map_fsc.eps',
                        curve_label=["map_fsc"])

def cc_mask(args):
    from emda.emda_methods import mask_from_halfmaps
    _ = mask_from_halfmaps(args.h1,args.h2)

def lowpass_map(args):
    from emda.emda_methods import lowpass_map
    lowpass_map(args.map,args.res)

def power_map(args):
    from emda.emda_methods import get_map_power
    from emda import plotter
    res_arr, power_spectrum = get_map_power(args.map)
    plotter.plot_nlines_log(res_arr,
                            [power_spectrum],
                            curve_label=["Power"],
                            mapname='map_power.eps')

def mapresol(args):
    from emda.emda_methods import estimate_map_resol
    resol = estimate_map_resol(args.h1, args.h2)
    print('Map resolution (A):', resol)

def mrc2mtz(args):
    import numpy as np
    from emda.iotools import read_map,write_3d2mtz
    uc,ar1,origin = read_map(args.map)
    hf1 = np.fft.fftshift(np.fft.fftn(ar1))
    write_3d2mtz(uc,hf1,outfile=args.out+'.mtz')

def mtz2mrc(args):
    from emda.iotools import read_map,write_mrc
    from emda.maptools import mtz2map
    uc,ar,origin = read_map(args.map)
    dat = mtz2map(args.mtz,ar.shape)
    outfile=args.out+'.mrc'
    write_mrc(dat,outfile,uc,origin)

def resample_data(args):
    import numpy as np
    from emda.emda_methods import read_map, resample_data, write_mrc
    import emda.mapfit.utils as utils
    uc, arr, org = read_map(args.map)
    arr = utils.set_dim_even(arr)
    target_uc = uc
    if args.pix is None: 
        pix = uc[0] / arr.shape[0]
    else: 
        pix = args.pix
    if args.dim is None: 
        dim = int(round(uc[0] / pix))
        new_arr = resample_data(pix, [dim,dim,dim], target_uc, arr)
    if args.dim is not None: 
        new_arr = resample_data(pix, args.dim, target_uc, arr)
        target_uc = round(pix,3) * np.asarray(args.dim, dtype='int')
    write_mrc(new_arr,args.out,target_uc,org)

def realsp_corr(args):
    from emda.emda_methods import realsp_correlation
    realsp_correlation(args.h1, args.h2, args.knl, args.mdl, args.res, args.msk)

def fouriersp_corr(args):
    from emda.emda_methods import fouriersp_correlation
    fouriersp_correlation(args.h1, args.h2, args.knl)

def map_model_fsc(args):
    from emda.emda_methods import map_model_validate
    map_model_validate(args.h1, args.h2, args.mdf, args.md1, args.msk, args.dim, args.res)

def map_overlay(args,fobj):
    from emda.emda_methods import overlay_maps
    overlay_maps(args.map, args.msk, args.tra, args.rot, args.axr, args.ncy, args.res, fobj, args.int)

def map_transform(args):
    from emda.emda_methods import map_transform
    map_transform(args.map, args.tra, args.rot, args.axr, args.out)

def map_average(args,fobj):
    from emda.emda_methods import average_maps
    fobj.write('***** Map Average *****\n')
    average_maps(args.map, args.msk, args.tra, args.rot, args.axr, args.ncy, args.res, fobj)

def apply_bfac(args):
    from emda.emda_methods import apply_bfactor_to_map
    all_maps = apply_bfactor_to_map(args.map,args.bfc,args.out)

def half_to_full(args):
    from emda.emda_methods import half2full
    fullmap = half2full(args.h1, args.h2)

def diff_map(args):
    from emda.emda_methods import difference_map
    difference_map(args.m1, args.m2)





def main(command_line=None):
    f=open("EMDA.txt", 'w')
    f.write('EMDA session recorded at %s.\n\n' % 
               (datetime.datetime.now()))
    args = cmdl_parser.parse_args(command_line)
    if args.command == 'info':
        map_info(args)    
    if args.command == 'fsc':
        anymap_fsc(args,f)
        f.close()
    if args.command == 'halffsc':
        halfmap_fsc(args)
    if args.command == 'ccmask':
        cc_mask(args)
    if args.command == 'lowpass':
        lowpass_map(args)
    if args.command == 'power':
        power_map(args)
    if args.command == 'resol':
        mapresol(args)
    if args.command == 'mrc2mtz':
        mrc2mtz(args)
    if args.command == 'mtz2mrc':
        mtz2mrc(args)
    if args.command == 'resample':
        resample_data(args)
    if args.command == 'rcc':
        realsp_corr(args)
    if args.command == 'fcc':
        fouriersp_corr(args)
    if args.command == 'mapmodelfsc':
        map_model_fsc(args)
    if args.command == 'overlay':
        map_overlay(args,f)
        f.close()
    if args.command == 'average':
        map_average(args,f)
        f.close()
    if args.command == 'transform':
        map_transform(args)
    if args.command == 'bfac':
        apply_bfac(args)
    if args.command == 'singlemapfsc':
        singlemap_fsc(args)
    if args.command == 'half2full':
        half_to_full(args)
    if args.command == 'diffmap':
        diff_map(args)
    if args.command == 'applymask':
        apply_mask(args)


if __name__ == '__main__':
    #f=open("test.txt", 'w')
    main()
    #f.close()


