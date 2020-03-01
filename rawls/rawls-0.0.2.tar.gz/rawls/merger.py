# main imports
import os
import numpy as np

# image imports
from PIL import Image

# class import
from .classes.rawls import Rawls
from .converter import rawls_to_png, rawls_to_pil


def merge_mean_rawls(filepaths):
    """Merge mean `.rawls` samples images from list of files
    
    Arguments:
        filepaths: {[str]} image filepaths list
    
    Returns:
        new rawls object with mean data of rawls files
    """

    # read rawls
    rawls_images = []

    for filepath in filepaths:
        rawls_images.append(Rawls.fromfile(filepath))

    # getting and check shapes of images
    shapes = []

    for img in rawls_images:
        shapes.append(img.shape)

    if not shapes[1:] == shapes[:-1]:
        raise Exception('Input rawls images do not have same shapes')

    # compute merge mean values
    merged_values = np.array([img.data for img in rawls_images])
    merged_values_mean = np.mean(merged_values, axis=0)

    # construct output data
    return Rawls(rawls_images[0].shape, merged_values_mean,
                 rawls_images[0].comments)


def merge_mean_rawls_to_pil(filepaths):
    """Return mean merged image into PNG
    
    Arguments:
        filepaths: {[str]} image filepaths list
    
    Returns:
        PNG PIL mean merged image
    """
    merged_image = merge_mean_rawls(filepaths)
    return rawls_to_pil(merged_image)


def merge_mean_rawls_to_png(filepaths, outfile):
    """Return mean merged image into PNG
    
    Arguments:
        filepaths: {[str]} image filepaths list
        outfile: {str} output path of the .png image to save
    
    Returns:
        save mean merged image as png
    """
    merged_image = merge_mean_rawls(filepaths)
    return rawls_to_png(merged_image, outfile)


def merge_var_rawls(filepaths):
    """Merge variance `.rawls` samples images from list of files
    
    Arguments:
        filepaths: {[str]} image filepaths list
    
    Returns:
        new rawls object with variance data of rawls files
    """

    # read rawls
    rawls_images = []

    for filepath in filepaths:
        rawls_images.append(Rawls.fromfile(filepath))

    # getting and check shapes of images
    shapes = []

    for img in rawls_images:
        shapes.append(img.shape)

    if not shapes[1:] == shapes[:-1]:
        raise Exception('Input rawls images do not have same shapes')

    # compute merge mean values
    merged_values = np.array([img.data for img in rawls_images])
    merged_values_mean = np.var(merged_values, axis=0)

    # construct output data
    return Rawls(rawls_images[0].shape, merged_values_mean,
                 rawls_images[0].comments)


def merge_var_rawls_to_pil(filepaths):
    """Return var merged image into PNG
    
    Arguments:
        filepaths: {[str]} image filepaths list
    
    Returns:
        PNG PIL var merged image
    """
    merged_image = merge_var_rawls(filepaths)
    return rawls_to_pil(merged_image)


def merge_var_rawls_to_png(filepaths, outfile):
    """Return var merged image into PNG
    
    Arguments:
        filepaths: {[str]} image filepaths list
        outfile: {str} output path of the .png image to save
    
    Returns:
        save var merged image as png
    """
    merged_image = merge_var_rawls(filepaths)
    return rawls_to_png(merged_image, outfile)
