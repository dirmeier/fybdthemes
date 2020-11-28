import seaborn as sns


def discrete_qualitative_colors(n_colors: int = 6, reverse: bool = False):
    """
    A discrete qualitative color palette

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

    return _qualitative_colors(n_colors=n_colors, reverse=reverse)


def _qualitative_colors(n_colors=3, as_cmap=False, reverse=False):
    qualitative = [
        "#004787", "#0D0B0C", "#A25050",
        "#61829CFF", "#B2AAA2", "#532026FF"
    ]
    assert n_colors <= len(qualitative), \
        f"color palette only has {len(qualitative)}"
    if reverse:
        qualitative = qualitative[::-1]
    return sns.color_palette(qualitative, as_cmap=as_cmap, n_colors=n_colors)
