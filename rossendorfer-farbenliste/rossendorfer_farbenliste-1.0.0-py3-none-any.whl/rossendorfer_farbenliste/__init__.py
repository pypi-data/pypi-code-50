from matplotlib.image import imread
from matplotlib.colors import LinearSegmentedColormap
#import matplotlib.pyplot as plt

img = imread('Gradients.png')
#plt.imshow(img[50:60,:])
# img is 30 x 280 but we need just one col
# commonly cmpas have 256 entries, but since img is 280 px => N=280

colors_from_img = img[40, :, :]
rofl_old = LinearSegmentedColormap.from_list('my_cmap', colors_from_img, N=694)

colors_from_img = img[70, :, :]
rofl = LinearSegmentedColormap.from_list('my_cmap2', colors_from_img, N=694)

colors_from_img = img[100, :, :]
rofl_nw = LinearSegmentedColormap.from_list('my_cmap3', colors_from_img, N=694)


#import matplotlib as mpl
