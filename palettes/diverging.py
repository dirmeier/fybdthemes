import seaborn as sns


def discrete_diverging_colors(n_colors: int = 4, reverse: bool = False):
    """
    A discrete diverging color palette

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

    return _diverging_colors(n_colors=n_colors, reverse=reverse)


def continuous_diverging_colors(reverse: bool = False):
    """
    A continuous diverging color palette

    Parameters
    ----------
    reverse : boolean
        reverse colors or not

    Returns
    -------
    :class:`matplotlib.colors.Colormap`
    """

    return _diverging_colors(as_cmap=True, reverse=reverse)


def _diverging_colors(n_colors=3, as_cmap=False, reverse=False):
    diverging = ["#233B43",
                 "#004B87",
                 "#B04A5A",
                 "#532026FF"]
    if reverse:
        diverging = diverging[::-1]
    return sns.blend_palette(diverging, n_colors=n_colors, as_cmap=as_cmap)
