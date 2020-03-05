from os import path
import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt
from matplotlib import ticker
from matplotlib.colors import Normalize, ListedColormap
import matplotlib.cm
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation

normalize_rad = Normalize(vmin=0, vmax=2*np.pi)

# Colormap from Li et al., (2019)
clist = list('ckkbbkkggkkrrkkc')
clist = ['#00da00' if c is 'g' else c for c in clist]
clist = ['#0800da' if c is 'b' else c for c in clist]
clist = ['#ed0912' if c is 'r' else c for c in clist]
clist = ['#00ccff' if c is 'c' else c for c in clist]

cmap = ListedColormap(clist)
matplotlib.cm.register_cmap('li2019', cmap)

def quadrilaterals(X):
    dX = X[1:]-X[:-1]
    dX = np.pad(dX, 1, mode='edge')
    dX[:-1] *= -1 # subtract dX/2 from all but last element, where we add dX/2
    # quads needs one more value (see pcolormesh)
    quads = np.pad(X, (0,1), mode='edge').astype(float)
    quads += dX/2
    return quads

def format_label(label, format_spec='{:g}'):
    if isinstance(label, tuple):
        lbl = ', '.join(map(format_label, label))
        return f'({lbl})'

    if isinstance(label, list):
        return ', '.join(map(format_label, label))

    try:
        return format_spec.format(label)
    except:
        return str(label)

def format_labels(labels, format_spec='{:g}'):
    return [format_label(l, format_spec) for l in labels]

def heatmap2(X, Y, Z, xlabel='x', ylabel='y', zlabel='z', xlabels=None, ylabels=None, **kwargs):
    X = np.array(X)
    Y = np.array(Y)
    Z = np.array(Z)
    print(X.shape, Y.shape, Z.shape)
    print(X.dtype, Y.dtype, Z.dtype)

    if not xlabels:
        xlabels = format_labels(X)

    #if X.dtype == object:
    #    X = np.arange(len(X))

    if not ylabels:
        ylabels = format_labels(Y)

    #if Y.dtype == object:
    #    Y = np.arange(len(Y))

    Xi = np.arange(len(X))
    Yi = np.arange(len(Y))
    print(Yi)
    qX = quadrilaterals(Xi)
    qY = quadrilaterals(Yi)

    def format_coord(x, y):
        # find nearest x,y
        #idx = np.abs(x-Xi).argmin()
        #idy = np.abs(y-Yi).argmin()
        idx = int(x + 0.5)
        idy = int(y + 0.5)
        x = xlabels[idx]
        y = ylabels[idy]
        z = Z[idy, idx]
        return f'{xlabel}={x}, {ylabel}={y}, {zlabel}={z:g}'

    ax = plt.gca()
    ax.format_coord = format_coord
    ax.xaxis.set_major_locator(ticker.FixedLocator(Xi, nbins=min(len(Xi), 10)))
    ax.yaxis.set_major_locator(ticker.FixedLocator(Yi, nbins=min(len(Yi), 10)))
    ax.xaxis.set_major_formatter(ticker.FuncFormatter((lambda x,pos: xlabels[x])))
    ax.yaxis.set_major_formatter(ticker.FuncFormatter((lambda y,pos: ylabels[y])))
    #ax.xaxis.set_major_formatter(ticker.FuncFormatter((lambda x,pos: (x,pos))))
    #ax.yaxis.set_major_formatter(ticker.FuncFormatter((lambda y,pos: (y,pos))))
    #ax.set_xticklabels(xlabels)
    #ax.set_yticklabels(ylabels)
    return plt.pcolormesh(qX, qY, Z, **kwargs)

def heatmap(X, Y, Z, xlabel='x', ylabel='y', zlabel='z',
        xlim=None, ylim=None, zlim=None, nticks=10,
        xlabel_format='{:g}', ylabel_format='{:g}',
        **kwargs):

    xlabels = format_labels(X, xlabel_format)
    ylabels = format_labels(Y, ylabel_format)

    X = np.array(X)
    Y = np.array(Y)
    Z = np.array(Z)

    Xi = np.arange(len(X))
    Yi = np.arange(len(Y))

    def format_coord(x, y):
        try:
            idx = int(x)
            idy = int(y)
            x = xlabels[idx]
            y = ylabels[idy]
            z = Z[idy, idx]
            return f'{xlabel}={x}, {ylabel}={y}, {zlabel}={z:g}'
        except IndexError:
            return ''

    ax = plt.gca()
    ax.format_coord = format_coord
    nbins = min(len(Xi), nticks) if X.dtype != 'object' else None
    ax.xaxis.set_major_locator(ticker.FixedLocator(Xi+.5, nbins=nbins))
    nbins = min(len(Yi), nticks) if Y.dtype != 'object' else None
    ax.yaxis.set_major_locator(ticker.FixedLocator(Yi+.5, nbins=nbins))
    ax.xaxis.set_major_formatter(ticker.FuncFormatter((lambda x,pos: xlabels[int(x)])))
    ax.yaxis.set_major_formatter(ticker.FuncFormatter((lambda y,pos: ylabels[int(y)])))

    if zlim:
        kwargs['vmin'], kwargs['vmax'] = zlim

    pcolor = plt.pcolormesh(Z, **kwargs)

    # We have integer indexes on the axes, so need to map x values to x indexes
    if xlim and X.dtype != 'object':
        xmin, xmax = xlim
        ximin = np.argmax(X >= xmin)
        ximax = np.argmax(X > xmax)
        plt.xlim(ximin, ximax)

    if ylim and Y.dtype != 'object':
        ymin, ymax = ylim
        yimin = np.argmax(Y >= ymin)
        yimax = np.argmax(Y > ymax)
        plt.ylim(yimin, yimax)

    return pcolor

def vector_colors(U, V):
    C = np.arctan2(V, U) # color
    C[C<0] = 2*np.pi + C[C<0]
    return C

def mask_zero_vectors(UV):
    # mask out zero vectors
    mag = norm(UV, axis=-1)
    mask = np.repeat(mag <= 1e-12, 2).reshape(UV.shape)
    return np.ma.array(UV, mask=mask)

def plot_vectors(XY, UV, C=None, arrows=True, relim=True, mask_zero=True, replace=False, **kwargs):
    X = XY[...,0] # x components
    Y = XY[...,1] # y components

    if mask_zero:
        UV = mask_zero_vectors(UV)

    U = UV[..., 0] # x components
    V = UV[..., 1] # y components
    if C is None:
        C = vector_colors(U, V)
    #C = np.arctan2(V, U) # color
    #C[C<0] = 2*np.pi + C[C<0]

    ax = plt.gca()

    if replace and len(ax.collections) > 0:
        # Replace current quiver data
        quiv = ax.collections[0]
        quiv.set_UVC(U, V, C)
        return quiv

    # determine scale
    width = np.max(X) - np.min(X)
    height = np.max(Y) - np.min(Y)
    div = max(width, height)
    if div > 0:
        numx = len(np.unique(X))
        numy = len(np.unique(Y))
        scale = max(numx, numy) / div
    else:
        scale = 1

    kwargs.setdefault('cmap', 'hsv')
    kwargs.setdefault('scale', scale)
    kwargs.setdefault('width', 0.2/scale)
    if arrows:
        kwargs.setdefault('headwidth', 3)
        kwargs.setdefault('headlength', 2)
        kwargs.setdefault('headaxislength', 2)
    else:
        kwargs.setdefault('headwidth', 0)
        kwargs.setdefault('headlength', 0)
        kwargs.setdefault('headaxislength', 0)

    quiv = ax.quiver(X, Y, U, V, C, pivot='middle',
            norm=normalize_rad, units='xy', angles='xy',
            scale_units='xy', **kwargs)

    ax.set_aspect('equal')

    if relim:
        # Make space for the whole arrow
        xmin, xmax = ax.get_xlim()
        ymin, ymax = ax.get_ylim()
        ax.set_xlim(xmin - 1/scale, xmax + 1/scale)
        ax.set_ylim(ymin - 1/scale, ymax + 1/scale)

    return quiv

def plot_vector_image(XY, UV, mask_zero=True, replace=False, cmap='hsv'):
    if mask_zero:
        UV = mask_zero_vectors(UV)

    U = UV[...,0] # x components
    V = UV[...,1] # y components
    C = vector_colors(U, V)

    cmap = plt.get_cmap(cmap)
    mag = norm(UV, axis=-1)
    alpha = mag

    # print(f'alpha {np.min(alpha)} {np.max(alpha)}')
    im = cmap(normalize_rad(C))
    im[:,:,-1] = alpha
    # print(f'im {im.shape} {im}')

    ax = plt.gca()
    if replace and len(ax.images) > 0:
        # Replace current image data
        ax.images[0].set_data(im)
        return ax.images[0]

    X = np.unique(XY[..., 0]) # x components
    Y = np.unique(XY[..., 1]) # y components
    Xi = np.arange(len(X))
    Yi = np.arange(len(Y))

    xmin, xmax = X.min(), X.max()
    ymin, ymax = Y.min(), Y.max()

    def format_coord(x, y):
        x = xmin + (xmax-xmin) * x / (im.shape[1] - 1)
        y = ymin + (ymax-ymin) * y / (im.shape[0] - 1)
        return f'x={x:g}, y={y:g}'

    ax = plt.gca()
    ax.format_coord = format_coord
    nbins = min(len(Xi), 10)
    ax.xaxis.set_major_locator(ticker.FixedLocator(Xi, nbins=nbins))
    nbins = min(len(Yi), 10)
    ax.yaxis.set_major_locator(ticker.FixedLocator(Yi, nbins=nbins))
    ax.xaxis.set_major_formatter(ticker.FuncFormatter((lambda x,pos: "{:g}".format(X[int(x)]))))
    ax.yaxis.set_major_formatter(ticker.FuncFormatter((lambda y,pos: "{:g}".format(Y[int(y)]))))

    return ax.imshow(im, origin='lower')

def montage_fig(n_axes, title=False):
    """ Create a figure with n_axes subplots on a grid """
    n_rows = int(np.ceil(np.sqrt(n_axes)))
    n_cols = int(np.ceil(n_axes / n_rows))
    gs = dict(wspace=0.05, hspace=0.25, left=0.05, right=0.95, top=0.95, bottom=0.05)
    figsize = [6.4, 6.4]

    if title:
        gs.update(top=0.85) # todo: fixme

    fig, axes = plt.subplots(n_rows, n_cols, gridspec_kw=gs, figsize=figsize, squeeze=False)
    axes = axes.flatten()

    for ax in axes:
        ax.set_axis_off()

    # hide unused axes
    for ax in axes[n_axes:]:
        ax.set_visible(False)

    return fig, axes

def vector_montage(axes, positions, vectors, labels=None, arrows=False, **kwargs):
    for i, (XY, UV, ax) in enumerate(zip(positions, vectors, axes)):
        plt.sca(ax)

        if arrows:
            plot_vectors(XY, UV, arrows=arrows, replace=True, **kwargs)
        else:
            plot_vector_image(XY, UV, replace=True, **kwargs)

        if labels:
            ax.set_title(labels[i], size='x-small', pad=2)

def save_animation(ani, outfile, fps):
    base, ext = path.splitext(outfile)
    ext = ext.lstrip('.')

    if ext == 'mp4':
        print(f"Saving video {outfile}...")
        Writer = animation.writers['ffmpeg']
        writer = Writer(fps=fps, codec='h264', extra_args=['-crf', '0', '-g', '1'])
        ani.save(outfile, writer=writer)
        return

    if ext in animation.writers['imagemagick_file'].supported_formats:
        print(f"Saving image(s) {outfile}...")
        Writer = animation.writers['imagemagick_file']
        writer = Writer(fps=fps)
        ani.save(outfile, writer=writer)
        return

    if ext == 'gif':
        print(f"Saving GIF {outfile}...")
        Writer = animation.writers['imagemagick']
        writer = Writer(fps=fps)
        ani.save(outfile, writer=writer)
        return

    raise ValueError(f"Don't know how to write '{ext}', sorry")
