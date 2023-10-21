import seaborn as sns


def discrete_sequential_colors(n_colors: int = 3, reverse: bool = False):
    """
    A discrete sequential color palette

    Parameters
    ----------
    n_colors : int
        number of colors
    reverse : boolean
        reverse colors or not

    Returns
    -------
    list of RGB tuples
    """

    return _sequential_colors(n_colors=n_colors, reverse=reverse)


def continuous_sequential_colors(reverse: bool = False):
    """
    A continuous sequential color palette

    Parameters
    ----------
    reverse : boolean
        reverse colors or not

    Returns
    -------
    :class:`matplotlib.colors.Colormap`
    """

    return _sequential_colors(as_cmap=True, reverse=reverse)


def _sequential_colors(n_colors=3, as_cmap=False, reverse=False):
    sequential = ["#61829CFF", "#004B87", "#252525"]
    if reverse:
        sequential = sequential[::-1]
    return sns.blend_palette(sequential, as_cmap=as_cmap, n_colors=n_colors)
