from distutils.core import setup, Extension

module1 = Extension('twobits',
                    sources = ['./two_bits_encoding.c', 'twobitsmodule.c'])

setup (name = 'twobits',
       version = '1.0',
       #define_macros = [('MAJOR_VERSION', '1'),
       #                              ('MINOR_VERSION', '0')],
       description = 'Encodind/decoding k-mers in 2bits-per-base ',
       include_dirs = ['./include'],
       ext_modules = [module1])

