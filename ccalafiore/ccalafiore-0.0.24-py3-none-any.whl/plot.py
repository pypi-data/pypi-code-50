import matplotlib.pyplot as plt


def save(plt, id_figures=None, directories=None, frm=['svg', 'png']):
    
    if id_figures is None:
        id_figures = plt.get_fignums()
        
    n_figures = len(id_figures)

    if directories is None:
        directories = id_figures
    else:
        n_directories = len(directories)
        if n_figures != n_directories:
            raise ValueError('n_figures and n_directories must be equal.\n'
                             'Now, n_figures = {} and n_directories = {}'.format(n_figures, n_directories))

    n_formats = len(frm)
    for i in range(n_figures):

        plt.figure(id_figures[i])

        for j in range(n_formats):

            plt.subplots_adjust(hspace=0.5)
            directory_i_j = '.'.join([directories[i], format_images[j]])
            plt.savefig(directory_i_j, format=frm[j], bbox_inches='tight', pad_inches=0.0)

    return None
