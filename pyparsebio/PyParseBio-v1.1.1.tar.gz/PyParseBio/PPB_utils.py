import os
import copy
import numpy as np
import skimage.util
import skimage.exposure
import skimage.transform
from skimage.external import tifffile
from nd2reader import ND2Reader

def dtype_conversion(image, to_dtype = 'uint16', in_range='image', forcecopy=False):

    conv_dict = {'float64': skimage.util.img_as_float64,
                 'float32': skimage.util.img_as_float32,
                 'uint16': skimage.util.img_as_uint,
                 'uint8': skimage.util.img_as_ubyte}
    
    assert to_dtype in conv_dict.keys(), \
    f'Conversion to {to_dtype} is not implemented. Available conversions are limited to {list(conv_dict.keys())}'
    
    if image.dtype == 'float64':
        # Scale between 0:1 required for skimage conversions from float.
        # Loop ensures that if in_range='image', internal min/max must be calculated per-channel, 
        # in order to preserve maximum precision. 
        if len(in_range) == 2: in_range = tuple([int(i) for i in in_range])
        else: in_range = in_range[0]
        for c in range(image.shape[1]): 
            image[:,c,...] = skimage.exposure.rescale_intensity(image[:,c,...], in_range=in_range)

    return conv_dict[to_dtype](image, forcecopy)


def get_addmeta(ims, wishdict={}):
    
    # key: value pairs expected to be present in nd2 files.
    # since the 'channels' key in the loaded metadata has the same name as the 'channels' key
    # generated by tifffile.imagej_description(), 'renaming' metadata 'channels' key to 'ch_names' 
    defaults = {'pixel_microns': 'pixel_microns',
                'ch_names': 'channels',
                'date': 'date'}
    
    # Appending wishdict.
    mdict = {**defaults, **wishdict}
    mmd = {}
    for k in mdict.keys(): 
        try: mmd[k] = ims.metadata[mdict[k]]
        except (KeyError):
            pass
            print(f"Warning: key \'{k}\' not found in source metadata; skipped.")
    
    # Source definition: 
    try: mmd['Source'] = [os.path.basename(ims.filename), ims.metadata['experiment']['description']]
    except (KeyError):
        pass
        print(f"Warning: Source definition failed")
    
    return mmd
 
def projectz(im, pmode: str):
    if pmode == 'max_project': im = np.amax(im, axis=0)
    if pmode == 'avg_project': im = np.mean(im, axis=0)
    return im

def resize(im, size, order=3):
    
    # im: array of shape (z,c,y,x). Z-dimension optional.
    # size: int/tuple of desired output shape (y,x).
    # order: interpolation mode, 3=bicubic.
    
    assert isinstance(size, tuple) and len(size) == 2, f"Please specify size as (y,x)"
    if np.argmax(im.shape[:2]) != np.argmax(size): 
        size = sorted(size, reverse=True)
        # print(f"Auto-selected size dimension {size[0]} as target for image dimension {np.argmax(im.shape[:2])}")
    
    # reshape to shape (x,y,c,z) expected by skimage
    im = np.transpose(im) 
    
    # for z-stacks:
    if im.ndim == 4:
        im = np.stack([skimage.transform.resize(im[...,z], size, order) for z in range(im.shape[3])], axis=3)
        
    # for non z-stacks:
    else: 
        im = skimage.transform.resize(im, size, order)

    return np.transpose(im)

def selectch(im, channels: list, copychannels=False):
    # function allows the generation of duplicate channels with copychannels=True,
    # e.g. channels=[0,0,1,2,3] will result in a 5-channel image with channel 0 duplicated. 
    
    chs = np.array(channels) # faster than indexing with list
    if copychannels == True and len(chs) != len(set(chs)):
        print('WARNING: channels are being duplicated!')
        return im[:,chs,...]
    else:
        assert len(chs) == len(set(chs)),  \
        f"Channels input contains duplicate indeces, which would be duplicated. Set copychannels=True to override."
        assert im.shape[1] >= chs.shape[0], \
        f"Shape missmatch: selected {chs.shape[0]} channels, but input image only has {im.shape[1]} channels "  
        return im[:,chs,...]

def savetiff(im, out_path, res=None, addMeta=None, verbose=False):
    tifffile.imsave(out_path, im, resolution = (res, res, None), metadata = addMeta, imagej=True)
    if verbose: print(f"Saved file: {out_path}")