# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['unrolr',
 'unrolr.core',
 'unrolr.feature_extraction',
 'unrolr.plotting',
 'unrolr.sampling',
 'unrolr.utils']

package_data = \
{'': ['*']}

install_requires = \
['MDAnalysis>=0.17.0',
 'h5py>=2.5.0',
 'matplotlib>=1.4.3',
 'numpy>=1.11.3',
 'pandas>=0.17.1',
 'pyopencl>=2015.1',
 'scipy>=1.2.1']

setup_kwargs = {
    'name': 'unrolr',
    'version': '0.5',
    'description': 'Dimensionality reduction method for MD trajectories',
    'long_description': '[![Documentation Status](https://readthedocs.org/projects/unrolr/badge/?version=latest)](https://unrolr.readthedocs.io/en/latest/?badge=latest)\n\n# Unrolr\nConformational analysis of MD trajectories based on (pivot-based) Stochastic Proximity Embedding using dihedral distance as a metric (https://github.com/jeeberhardt/unrolr).\n\n## Prerequisites\n\nYou need, at a minimum (requirements.txt):\n\n* Python\n* NumPy\n* H5py\n* Pandas\n* Matplotlib\n* PyOpenCL\n* MDAnalysis\n\n## Installation on UNIX (Debian/Ubuntu)\n\n1 . First, you have to install OpenCL:\n* MacOS: Good news, you don\'t have to install OpenCL, it works out-of-the-box. (Update: bad news, OpenCL is now depreciated in macOS 10.14. Thanks Apple.)\n* AMD:  You have to install the [AMDGPU graphics stack](https://amdgpu-install.readthedocs.io/en/amd-18.30/index.html).\n* Nvidia: You have to install the [CUDA toolkit](https://developer.nvidia.com/cuda-downloads).\n* Intel: And of course it\'s working also on CPU just by installing this [runtime software package](https://software.intel.com/en-us/articles/opencl-drivers). Alternatively, the CPU-based OpenCL driver can be also installed through the package ```pocl``` (http://portablecl.org/) using Anaconda.\n\nFor any other informations, the official installation guide of PyOpenCL is available [here](https://documen.tician.de/pyopencl/misc.html).\n\n2 . I highly recommand you to install the Anaconda distribution (https://www.continuum.io/downloads) if you want a clean python environnment with nearly all the prerequisites already installed. To install everything properly, you just have to do this:\n\n```bash\n$ conda create -n unrolr python=3\n$ conda activate unrolr\n$ conda install -c conda-forge mkl numpy scipy pandas matplotlib h5py MDAnalysis pyopencl ocl-icd-system\n```\n\n3 . Install unrolr\n```bash\n$ pip install unrolr\n```\n... or from the source directly\n\n```bash\n$ git clone https://github.com/jeeberhardt/unrolr\n$ cd unrolr\n$ python setup.py build install\n```\n\n## OpenCL context\n\nBefore running Unrolr, you need to define the OpenCL context. And it is a good way to see if everything is working correctly.\n\n```bash\n$ python -c \'import pyopencl as cl; cl.create_some_context()\'\n```\n\nHere in my example, I have the choice between 3 differents computing device (2 graphic cards and one CPU). \n\n```bash\nChoose platform:\n[0] <pyopencl.Platform \'AMD Accelerated Parallel Processing\' at 0x7f97e96a8430>\nChoice [0]:0\nChoose device(s):\n[0] <pyopencl.Device \'Tahiti\' on \'AMD Accelerated Parallel Processing\' at 0x1e18a30>\n[1] <pyopencl.Device \'Tahiti\' on \'AMD Accelerated Parallel Processing\' at 0x254a110>\n[2] <pyopencl.Device \'Intel(R) Core(TM) i7-3820 CPU @ 3.60GHz\' on \'AMD Accelerated Parallel Processing\' at 0x21d0300>\nChoice, comma-separated [0]:1\nSet the environment variable PYOPENCL_CTX=\'0:1\' to avoid being asked again.\n```\n\nNow you can set the environment variable.\n\n```bash\n$ export PYOPENCL_CTX=\'0:1\'\n```\n\n## Example\n\n```python\nfrom unrolr import Unrolr\nfrom unrolr.feature_extraction import Dihedral\nfrom unrolr.utils import save_dataset\n\n\ntop_file = \'examples/inputs/villin.psf\'\ntrj_file = \'examples/inputs/villin.dcd\'\n\n# Extract all calpha dihedral angles from trajectory and store them into a HDF5 file\nd = Dihedral(top_file, trj_file, selection=\'all\', dihedral_type=\'calpha\').run()\nX = d.result\nsave_dataset(\'dihedral_angles.h5\', "dihedral_angles", X)\n\n# Fit X using Unrolr (pSPE + dihedral distance) and save the embedding into a csv file\n# The initial embedding is obtained using PCA (init = \'pca\') with the OpenCL implementation\n# to run SPE, a CPU implementation can be used as an alternative (platform=\'CPU\')\nU = Unrolr(r_neighbor=0.27, n_iter=50000, init=\'pca\', platform=\'OpenCL\', verbose=1)\nU.fit(X)\nU.save(fname=\'embedding.csv\')\n\nprint(\'%4.2f %4.2f\' % (U.stress, U.correlation))\n```\n\n## Todo list\n- [ ] Compare SPE performance with UMAP\n- [x] Compatibility with python 3\n- [x] Compatibility with the latest version of MDAnalysis (==0.17)\n- [ ] Unit tests\n- [x] Accessible directly from pip\n- [ ] Improve OpenCL performance (global/local memory)\n\n## Citation\nEberhardt, J., Stote, R. H., & Dejaegere, A. (2018). Unrolr: Structural analysis of protein conformations using stochastic proximity embedding. Journal of Computational Chemistry, 39(30), 2551-2557. https://doi.org/10.1002/jcc.25599\n\n## License\nMIT\n',
    'author': 'jeeberhardt',
    'author_email': 'qksoneo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jeeberhardt/unrolr',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
