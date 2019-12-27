# py-roughviz

<p align="left">
    <a href="https://badge.fury.io/py/py-roughviz">
        <img src="https://badge.fury.io/py/py-roughviz.svg" alt="Package Version">
    </a>
        <a href="https://badge.fury.io/py/py-roughviz">
        <img src="https://travis-ci.org/charlesdong1991/py-roughviz.svg?branch=master" alt="build">
    </a>
     <a href="https://github.com/charlesdong1991/py-roughviz/pulls">
        <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="Contributions welcome">
    </a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg" alt="License">
    </a>
</p>

This is the Python wrapper of the JaveScript Library RoughViz which you could
use to visualize sketchy/hand-drawn styled charts.
You could check out original JS libarary here: [RoughViz](https://github.com/jwilber/roughViz)

## Implemented Charts

Currently, there are seven types of charts available on JS RoughViz project, and I implemented all of them:

- Bar
- Barh
- Pie
- Line
- Scatter
- Donut
- StackedBar

## Before Use it

- Cloning:
If you clone the repo, please install the dependencies in order to use them, and simply do below if you are using
`pip`.

```bash
pip install -r requirements.txt
```

- Downloading the pakcage:
This package is also available on PyPi, so you could do below to download the package
```bash
pip install py-roughviz
```


## How to use it

Due to design of original RoughViz, there are some restrictions on the format of input data. The
detailed description can be found in the documentation.

To use the tool, you could either define all options during chart in the initialization, or to 
define the options later. And in order to make it easier to use, there are several options provided.

1. You could define all options using `set_options`
2. For common options shared across different charts, you could define it in a more intuitive way, e.g.
`set_title(title="The plot", fontsize=2)`, or `set_xlabel("X Label", fontsize=3)`

Currently available options are:
- `set_options`: this can be used to set all available options for charts
- `set_title`: this can be used to set title and title fontsize
- `set_xlabel`: this can be used to set xlabel and its fontsize
- `set_ylabel`: this can be used to set ylabel and its fontsize
- `set_figsize`: this can be used to set the figsize for plots
- `set_legend`: this can be used to determine if legend is presented, and if so, which position to put legend


## Examples

- Example 1

```python
from roughviz.charts.line import Line

line = Line(data="examples/example_datasets/vis1.csv", y1="a", y2="b", y3="c")
line.set_legend(legend_position="left")
line.set_title("Line Plot", fontsize=2)
line.set_options(colors=["tan", "orange", "coral"])

line.show()
```


![Example 1](https://github.com/charlesdong1991/py-roughviz/blob/master/examples/example_plots/example1.png)



- Example 2

```python
from roughviz.charts.bar import Bar

data = {
    "labels": ["North", "South", "East", "West"],
    "values": [10, 5, 8, 3]
}

bar = Bar(data=data, title="Regions", title_fontsize=3)
bar.set_xlabel("Region", fontsize=2)
bar.set_ylabel("Number", fontsize=2)

bar.show()
```

![Example 2](https://github.com/charlesdong1991/py-roughviz/blob/master/examples/example_plots/example2.png)
