# Introduction

This python package contains a collection of nice color maps for scientific visualizations and provides a convinient and unified way to pick the color maps. Some color maps are perceptually uniform and/or color blind friendly.

# Quick start

### Import the package

```python
import scicolor
```

### Get a color map

```py
scicolor.get_cmap('viridis')
```

`scicolor.get_cmap()` works just like `plt.get_cmap()`.
The returned value can be instances of either `matplotlib.colors.ListedColormap` or `matplotlib.colors.LinearSegmentedColormap`.

You can access the colors of `matplotlib.colors.ListedColormap` instances by `.colors`.


### List available color maps

List all color maps

```py
scicolor.list_cmaps()
```

List the color maps that are sequential, discrete, and color blind friendly.

```py
scicolor.plot_cmaps(cm_class='sequential', cm_type="discrete", color_blind_friendly=True)
```
### 

# Installation

## Installation instruction

The package is not on PyPI.
In order to use it, please clone or donwload this repo, go the root directory

```
cd /path/to/scicolor
```

and use the following command to install the package locally:

```
pip install -e ./
```

## Requirements

- python3
- matplotlib
- pandas
- numpy



 
# Availble color mpas

![list](list_of_cms.png)

# Guideline for choosing color maps

![guideline](guideline.png)
