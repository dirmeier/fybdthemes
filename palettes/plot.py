import numpy as np
import matplotlib.colors
import matplotlib.pyplot as plt


def plot_palette(palette):
    """
    Plot a color palette

    Parameters
    ----------
    palette : list of RGB tuples | matplotlib.colors.Colormap
        the palette to plot
    """

    if isinstance(palette, matplotlib.colors.LinearSegmentedColormap):
        figsize = (8, 1)
        gradient = np.linspace(0, 1, 256)
        gradient = np.vstack((gradient, gradient))
    else:
        figsize = (len(palette), 1)
        gradient = np.linspace(0, 1, len(palette))
        gradient = np.vstack((gradient, gradient))
        palette = matplotlib.colors.ListedColormap(palette)
    fig, axis = plt.subplots(figsize=figsize)
    axis.imshow(gradient, aspect="auto", cmap=palette)
    axis.set_axis_off()
    plt.close()

    return fig
