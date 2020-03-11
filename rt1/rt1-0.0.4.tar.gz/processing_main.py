# disable numpy's internal multithreading to avoid parallel overhead
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
os.environ['NUMEXPR_NUM_THREADS'] = '1'

from rt1.rtread.rtread import Read
from rt1.rtfits import RT1_configparser
from rt1.processing_config import rt1_processing_config

# initialize the ascat reader
# this must be done in the main file to allow pickling of the reader object!!!
ASCAT_prop = dict(usebeams='fma')
rt1_reader = Read(
    ASCAT_cfg_fullpath=r"D:\_warp_datasets\itchy_ishka_2019\rt1.cfg",
    ASCAT_prop=ASCAT_prop)


# subclass the configuration and add a reader
class processing_cfg(rt1_processing_config):
    def __init__(self, config_path, **kwargs):
        super().__init__(**kwargs)
        self.config_path = config_path


    def reader(self, **reader_arg):
        # initialize a reader
        df = rt1_reader.read_ASCAT(reader_arg['gpi'])

        df = df[df.index.year.isin([2018])]
        return df


    def run_procesing(self, reader_args, ncpu):

        print('############################################################\n')

        # get fit object by using a config-file
        config = RT1_configparser(self.config_path)
        rt1_fits = config.get_fitobject()

        res = rt1_fits.processfunc(ncpu=ncpu,
                                   reader_args=reader_args,
                                   lsq_kwargs=None,
                                   pool_kwargs=None,
                                   reader=self.reader,
                                   preprocess=self.preprocess,
                                   postprocess=self.postprocess,
                                   exceptfunc=self.exceptfunc,
                                   finaloutput=self.finaloutput
                                   )


if __name__ == '__main__':

    ncpu = 4
    config_path = r"H:/python_modules/rt_model_python/rt1/processing_config.ini"
    finalout_name = 'results.h5'
    save_path = r'D:\__rt1_test'
    dumpfolder='cfg_with_properties3'

    gpis = [2430123, 2434397, 2430127, 2430119]
    reader_args = [dict(gpi=gpi) for gpi in gpis]

    proc = processing_cfg(config_path=config_path,
                          save_path=save_path,
                          dumpfolder=dumpfolder,
                          error_dumpfolder=dumpfolder,
                          finalout_name=finalout_name)

    proc.run_procesing(reader_args=reader_args,
                       ncpu=ncpu)




