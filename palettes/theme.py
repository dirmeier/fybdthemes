
import matplotlib as mpl


def set_theme():
    """
    Set a custom theme

    Theme removes axis spines right and top and adds a grid
    """

    mpl.rcParams['axes.spines.right'] = False
    mpl.rcParams['axes.spines.top'] = False
    mpl.rcParams['grid.color'] = "grey"
    mpl.rcParams['grid.linewidth'] = 0.5
    mpl.rcParams['legend.loc'] = "center right"
