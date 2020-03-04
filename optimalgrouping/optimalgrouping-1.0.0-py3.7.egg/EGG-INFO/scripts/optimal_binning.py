#!/home/ferrigno/Soft/myVE-py37-test/bin/python
from __future__ import print_function

import argparse
import sys
from optimalgrouping.optimalgrouping import execute_binning

try:
	import commands
except:
	pass

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

parser = argparse.ArgumentParser(description='Optimal grouping for the spectrum',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('Spectrum', metavar='fname', type=str, nargs=1,
					help='Spectrum PHA1 file')
parser.add_argument("-b", "--backname", help="Background file", type=str, default='none')
parser.add_argument("-r", "--respname", help="RMF or RSP file (response matrix)", type=str, default='none')
parser.add_argument("-a", "--ancrname", help="ARF file (effective area)", type=str, default='none')
parser.add_argument("-e", "--mine", help="Minimum energy (keV), default is minimum of response", type=float, default=-10)
parser.add_argument("-E", "--maxe", help="Maximum energy (keV), default is maximum of response", type=float, default=1e10)
parser.add_argument("-m", "--mincounts", help="Minimum number of counts per bin (for Xspec >0, for other instruments also 0)", type=float, default=-1e10)
parser.add_argument("--eref", help="reference energy for custom resolution (keV)", type=float, default=-1)
parser.add_argument("--res", help="resolution at the reference energy for custom input (keV)", type=float, default=-1)
parser.add_argument("--en_dep", help="energy dependence of resolution (power-law index) for custom input (keV)", type=float, default=-1)

#print len(sys.argv)

if len(sys.argv) == 1:
	parser.print_help()
	print(help)
	RuntimeError('Error')


args = parser.parse_args()
#

spectrum = args.Spectrum[0]
bkg=args.backname
rmf=args.respname
arf=args.ancrname
mine=args.mine
maxe=args.maxe
min_counts=args.mincounts
eref=args.eref
res=args.res
en_dep=args.en_dep

execute_binning(spectrum, bkg, rmf, arf, mine, maxe, min_counts, eref, res, en_dep)
