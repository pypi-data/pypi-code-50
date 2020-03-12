from astropy.io import fits
import random
import os


def extract_metadata_from_fits_file(fits_file_path):
    hdulist = fits.open(fits_file_path)
    hdr = hdulist[0].header
    randon_prop = random.randint(1, 101)
    return {
        'id': randon_prop,
        'title': os.path.basename(fits_file_path),
        'description': randon_prop,
        'path': fits_file_path,
        'primaryHDU': {
            'SIMPLE': hdr['EXTEND'],
            'BITPIX': hdr['BITPIX'],
            'NAXIS': hdr['NAXIS'],
            'EXTEND': hdr['EXTEND']
        }
    }
