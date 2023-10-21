import matplotlib as mpl


def set_theme():
    """
    Set a custom theme

    Theme removes axis spines right and top and adds a grid
    """

    mpl.rcParams["axes.linewidth"] = 1.5
    mpl.rcParams["axes.spines.right"] = False
    mpl.rcParams["axes.spines.top"] = False
    mpl.rcParams["font.size"] = 15
    mpl.rcParams["grid.color"] = "grey"
    mpl.rcParams["grid.linewidth"] = 0.5
    mpl.rcParams["legend.fontsize"] = "smaller"
    mpl.rcParams["legend.loc"] = "center right"
    mpl.rcParams["xtick.labelsize"] = "x-small"
    mpl.rcParams["ytick.labelsize"] = "x-small"
    mpl.rcParams["xaxis.labellocation"] = "right"
    mpl.rcParams["yaxis.labellocation"] = "top"
