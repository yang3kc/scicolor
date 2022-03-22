import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
import logging

def get_logger(name):
    # Create a custom logger
    logger = logging.getLogger(name)
    # Create handlers
    handler = logging.StreamHandler()
    # Create formatters and add it to handlers
    logger_format = logging.Formatter(
        "%(asctime)s@%(name)s:%(levelname)s: %(message)s")
    handler.setFormatter(logger_format)
    # Add handlers to the logger
    logger.addHandler(handler)
    # Set level
    level = logging.getLevelName("INFO")
    logger.setLevel(level)
    return logger

logger = get_logger(__name__)

color_data_root = os.path.join(
    os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
)

color_info_list = [
    ["tab20", "matplotlib", "multi_sequential", "categorical", False, False],
    ["tab20b", "matplotlib", "multi_sequential", "categorical", False, False],
    ["tab20c", "matplotlib", "multi_sequential", "categorical", False, False],
    ["Royal2", "wesanderson", "categorical", "categorical", False, False],
    ["Zissou1", "wesanderson", "categorical", "categorical", False, False],
    ["Darjeeling1", "wesanderson", "categorical", "categorical", False, False],
    ["FantasticFox1", "wesanderson", "categorical", "categorical", False, False],
    ["Moonrise3", "wesanderson", "categorical", "categorical", False, False],
    ["Cavalcanti1", "wesanderson", "categorical", "categorical", False, False],
    ["GrandBudapest2", "wesanderson", "categorical", "categorical", False, False],
    ["IsleofDogs2", "wesanderson", "categorical", "categorical", False, False],
    ["batlow10", "scientific_colors", "sequential", "discrete", True, True],
    ["batlow25", "scientific_colors", "sequential", "discrete", True, True],
    ["acton10", "scientific_colors", "sequential", "discrete", True, True],
    ["acton25", "scientific_colors", "sequential", "discrete", True, True],
    ["oslo10", "scientific_colors", "sequential", "discrete", True, True],
    ["oslo25", "scientific_colors", "sequential", "discrete", True, True],
    ["turku10", "scientific_colors", "sequential", "discrete", True, True],
    ["turku25", "scientific_colors", "sequential", "discrete", True, True],
    ["vik10", "scientific_colors", "diverging", "discrete", True, True],
    ["vik25", "scientific_colors", "diverging", "discrete", True, True],
    ["roma10", "scientific_colors", "diverging", "discrete", True, True],
    ["roma25", "scientific_colors", "diverging", "discrete", True, True],
    ["broc10", "scientific_colors", "diverging", "discrete", True, True],
    ["broc25", "scientific_colors", "diverging", "discrete", True, True],
    ["oleron10", "scientific_colors", "multi_sequential", "discrete", True, True],
    ["oleron25", "scientific_colors", "multi_sequential", "discrete", True, True],
    ["batlowS", "scientific_colors", "categorical", "categorical", True, True],
    ["glasbey", "cet", "categorical", "categorical", True, False],
    ["viridis", "matplotlib", "sequential", "continuous", True, True],
    ["inferno", "matplotlib", "sequential", "continuous", True, True],
    ["cividis", "matplotlib", "sequential", "continuous", True, True],
    ["batlow", "scientific_colors", "sequential", "continuous", True, True],
    ["acton", "scientific_colors", "sequential", "continuous", True, True],
    ["oslo", "scientific_colors", "sequential", "continuous", True, True],
    ["turku", "scientific_colors", "sequential", "continuous", True, True],
    ["vik", "scientific_colors", "diverging", "continuous", True, True],
    ["roma", "scientific_colors", "diverging", "continuous", True, True],
    ["broc", "scientific_colors", "diverging", "continuous", True, True],
    ["cwr", "cet", "diverging", "continuous", True, True],
    ["isolum", "cet", "misc", "continuous", True, True],
    ["oleron", "scientific_colors", "multi_sequential", "continuous", True, True],
    ["topo", "ocean", "multi_sequential", "continuous", True, True],
    ["Archambault", "metbrewer", "categorical", "categorical", False, True],
    ["Cassatt1", "metbrewer", "diverging", "discrete", False, True],
    ["Cassatt2", "metbrewer", "multi_sequential", "discrete", False, True],
    ["Demuth", "metbrewer", "diverging", "discrete", False, True],
    ["Derain", "metbrewer", "categorical", "categorical", False, True],
    ["Egypt", "metbrewer", "categorical", "categorical", False, True],
    ["Greek", "metbrewer", "sequential", "discrete", False, True],
    ["Hiroshige", "metbrewer", "diverging", "discrete", False, True],
    ["Hokusai2", "metbrewer", "sequential", "discrete", False, True],
    ["Ingres", "metbrewer", "multi_sequential", "discrete", False, True],
    ["Isfahan1", "metbrewer", "diverging", "discrete", False, True],
    ["Isfahan2", "metbrewer", "categorical", "categorical", False, True],
    ["Java", "metbrewer", "categorical", "categorical", False, True],
    ["Johnson", "metbrewer", "categorical", "categorical", False, True],
    ["Kandinsky", "metbrewer", "categorical", "categorical", False, True],
    ["Morgenstern", "metbrewer", "diverging", "discrete", False, True],
    ["OKeeffe1", "metbrewer", "diverging", "discrete", False, True],
    ["OKeeffe2", "metbrewer", "categorical", "categorical", False, True],
    ["Pillement", "metbrewer", "sequential", "discrete", False, True],
    ["Tam", "metbrewer", "sequential", "discrete", False, True],
    ["Troy", "metbrewer", "diverging", "discrete", False, True],
    ["Veronese", "metbrewer", "multi_sequential", "discrete", False, True],
]

color_info_df = pd.DataFrame(
    color_info_list,
    columns=[
        "cm_name",
        "source",
        "cm_class",
        "cm_type",
        "perceptually_uniform",
        "color_blind_friendly"
    ]
)

def _get_matplotlib_cmap(cm_name):
    """
    Function to load the color maps from matplotlib
    """
    return plt.get_cmap(cm_name)


def _get_scientific_colors(cm_name):
    """
    Function to load the color maps from scientific colors
    Color files ending with digits contain discrete color maps
    Color files ending with the letter S contain categorical color maps
    """
    color_path = os.path.join(color_data_root, "scientific_colors", cm_name + '.txt')
    if cm_name[-1].isdigit():
        with open(color_path) as f:
            colors = [
                line.strip().split(' ')[-1] for line in f.readlines()[2:]
            ]
        return ListedColormap(colors)

    cm_data = np.loadtxt(color_path)
    if cm_name[-1] == "S":
        return ListedColormap(cm_data, cm_name)

    return LinearSegmentedColormap.from_list(cm_name, cm_data)


def _get_cet_cmap(cm_name):
    """
    Function to load the color maps from CET
    """
    cm_data = np.loadtxt(
        os.path.join(color_data_root, "cet_colors", cm_name + '.txt'),
        delimiter=','
    )
    return LinearSegmentedColormap.from_list(cm_name, cm_data)


def _get_ocean_cmap(cm_name):
    """
    Function to load the color mpas from Ocean
    """
    cm_data = np.loadtxt(
        os.path.join(color_data_root, "ocean_colors", cm_name + '.txt'),
    )
    return LinearSegmentedColormap.from_list(cm_name, cm_data)


def _get_wesanderson_cmap(cm_name):
    """
    Function to load the color maps from Wes Anderson
    """
    wes_mapping = {
        "Royal2": ["#9A8822", "#F5CDB4", "#F8AFA8", "#FDDDA0", "#74A089"],
        "Zissou1": ["#3B9AB2", "#78B7C5", "#EBCC2A", "#E1AF00", "#F21A00"],
        "Darjeeling1": ["#FF0000", "#00A08A", "#F2AD00", "#F98400", "#5BBCD6"],
        "FantasticFox1": ["#DD8D29", "#E2D200", "#46ACC8", "#E58601", "#B40F20"],
        "Moonrise3": ["#85D4E3", "#F4B5BD", "#9C964A", "#CDC08C", "#FAD77B"],
        "Cavalcanti1": ["#D8B70A", "#02401B", "#A2A475", "#81A88D", "#972D15"],
        "GrandBudapest2": ["#E6A0C4", "#C6CDF7", "#D8A499", "#7294D4"],
        "IsleofDogs2" : ["#EAD3BF", "#AA9486", "#B6854D", "#39312F", "#1C1718"]
    }
    return ListedColormap(wes_mapping[cm_name], cm_name)


def _get_metbrewer_cmap(cm_name):
    """
    Function to load the color maps from MetBrewer
    """
    met_mapping = {
         "Archambault": ["#88a0dc", "#381a61", "#7c4b73", "#ed968c", "#ab3329", "#e78429", "#f9d14a"],
         "Cassatt1": ["#b1615c", "#d88782", "#e3aba7", "#edd7d9", "#c9c9dd", "#9d9dc7", "#8282aa", "#5a5a83"],
         "Cassatt2": ["#2d223c", "#574571", "#90719f", "#b695bc", "#dec5da", "#c1d1aa", "#7fa074", "#466c4b", "#2c4b27", "#0e2810"],
         "Demuth": ["#591c19", "#9b332b", "#b64f32", "#d39a2d", "#f7c267", "#b9b9b8", "#8b8b99", "#5d6174", "#41485f", "#262d42"],
         "Derain": ["#efc86e", "#97c684", "#6f9969", "#aab5d5", "#808fe1", "#5c66a8", "#454a74"],
         "Egypt": ["#dd5129", "#0f7ba2", "#43b284", "#fab255"],
         "Greek": ["#3c0d03", "#8d1c06", "#e67424", "#ed9b49", "#f5c34d"],
         "Hiroshige": ["#e76254", "#ef8a47", "#f7aa58", "#ffd06f", "#ffe6b7", "#aadce0", "#72bcd5", "#528fad", "#376795", "#1e466e"],
         "Hokusai2": ["#abc9c8", "#72aeb6", "#4692b0", "#2f70a1", "#134b73", "#0a3351"],
         "Hokusai3": ["#d8d97a", "#95c36e", "#74c8c3", "#5a97c1", "#295384", "#0a2e57"],
         "Ingres": ["#041d2c", "#06314e", "#18527e", "#2e77ab", "#d1b252", "#a97f2f", "#7e5522", "#472c0b"],
         "Isfahan1": ["#4e3910", "#845d29", "#ae8548", "#e3c28b", "#4fb6ca", "#178f92", "#175f5d", "#054544"],
         "Isfahan2": ["#d7aca1", "#ddc000", "#79ad41", "#34b6c6", "#4063a3"],
         "Java": ["#663171", "#cf3a36", "#ea7428", "#e2998a", "#0c7156"],
         "Johnson": ["#a00e00", "#d04e00", "#f6c200", "#0086a8", "#132b69"],
         "Kandinsky": ["#3b7c70", "#ce9642", "#898e9f", "#3b3a3e"],
         "Morgenstern": ["#98768e", "#b08ba5", "#c7a2b6", "#dfbbc8", "#ffc680", "#ffb178", "#db8872", "#a56457"],
         "OKeeffe1": ["#6b200c", "#973d21", "#da6c42", "#ee956a", "#fbc2a9", "#f6f2ee", "#bad6f9", "#7db0ea", "#447fdd", "#225bb2", "#133e7e"],
         "OKeeffe2": ["#fbe3c2", "#f2c88f", "#ecb27d", "#e69c6b", "#d37750", "#b9563f", "#92351e"],
         "Pillement": ["#a9845b", "#697852", "#738e8e", "#44636f", "#2b4655", "#0f252f"],
         "Tam": ["#ffd353", "#ffb242", "#ef8737", "#de4f33", "#bb292c", "#9f2d55", "#62205f", "#341648"],
         "Troy": ["#421401", "#6c1d0e", "#8b3a2b", "#c27668", "#7ba0b4", "#44728c", "#235070", "#0a2d46"],
         "VanGogh3": ["#e7e5cc", "#c2d6a4", "#9cc184", "#669d62", "#3c7c3d", "#1f5b25", "#1e3d14", "#192813"],
         "Veronese": ["#67322e", "#99610a", "#c38f16", "#6e948c", "#2c6b67", "#175449", "#122c43"]
    }
    return ListedColormap(met_mapping[cm_name], cm_name)

def get_cmap(cm_name):
    """
    Function to return the specific color map
    The response is similar to plt.get_camp
    """
    if not isinstance(cm_name, str):
        logger.error("Invalid color map name. Please input a string.")
        return None

    if cm_name not in set(color_info_df.cm_name):
        logger.error("Color map {} doesn't exist".format(cm_name))
        return None

    source = color_info_df.query("cm_name == '{}'".format(
        cm_name)).iloc[0]['source']

    cm = {
        'matplotlib': _get_matplotlib_cmap,
        'scientific_colors': _get_scientific_colors,
        'wesanderson': _get_wesanderson_cmap,
        'cet': _get_cet_cmap,
        'ocean': _get_ocean_cmap,
        'metbrewer': _get_metbrewer_cmap
    }[source](cm_name)
    return cm


def list_cmaps(
    cm_class=None,
    cm_type=None,
    perceptually_uniform=None,
    color_blind_friendly=None
):
    """
    Function to list available color maps
    Different parameters are used to filter the results
    """
    temp_df = color_info_df.drop('source', axis=1)
    if cm_class is not None:
        cm_class_set = set(color_info_df.cm_class)
        if cm_class not in cm_class_set:
            logger.info("Invalid cm_class value, try: {}, or None".format(
                ', '.join(list(cm_class_set))
            ))
        temp_df = temp_df.query("cm_class == '{}'".format(cm_class))

    if cm_type is not None:
        cm_type_set = set(color_info_df.cm_type)
        if cm_type not in cm_type_set:
            logger.info("Invalid cm_type value, try: {}, or None".format(
                ', '.join(list(cm_type_set))
            ))
        temp_df = temp_df.query("cm_type == '{}'".format(cm_type))
    if perceptually_uniform:
        temp_df = temp_df.query("perceptually_uniform == True")
    if color_blind_friendly:
        temp_df = temp_df.query("color_blind_friendly == True")

    return temp_df


def _plot_cmaps_gradients(cm_list):
    """
    Function to plot the color maps in bars
    """
    nrows = len(cm_list)
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))

    fig, axes = plt.subplots(nrows=nrows, figsize=(8, nrows*0.5))
    if nrows == 1:
        axes = [axes]

    for ax, (cm_name, cm) in zip(axes, cm_list):
        ax.imshow(gradient, aspect='auto', cmap=cm)
        pos = list(ax.get_position().bounds)
        x_text = pos[0] - 0.01
        y_text = pos[1] + pos[3]/2.
        fig.text(x_text, y_text, cm_name, va='center', ha='right', fontsize=14)

    for ax in axes:
        ax.set_axis_off()
    #plt.show()


def plot_cmaps(
    cm_name=None,
    cm_class=None,
    cm_type=None,
    perceptually_uniform=None,
    color_blind_friendly=None
):
    """
    Function to plot the color maps in bars for easy selection
    Different parameters are used to filter the results
    """
    if cm_name is None:
        color_df = list_cmaps(
            cm_class=cm_class,
            cm_type=cm_type,
            perceptually_uniform=perceptually_uniform,
            color_blind_friendly=color_blind_friendly
        )
        if len(color_df) == 0:
            logger.error("No matched color map found.")
            return None
        cm_name_list = list(color_df.cm_name)
    else:
        if isinstance(cm_name, str):
            cm_name_list = [cm_name]
        elif isinstance(cm_name, list):
            cm_name_list = cm_name
        else:
            logger.error(
                "Invalid color map name(s). Please input a string or a list of strings."
            )
    cm_list = [[temp_name, get_cmap(temp_name)] for temp_name in cm_name_list]
    _plot_cmaps_gradients(cm_list)
