import pytest
import pandas as pd

from roughviz.charts.scatter import Scatter


def test_wrong_input_data():
    wrong_data = {
        "x": ["North", "South", "East", "West"],
        "values": [10, 5, 8, 3]
    }
    with pytest.raises(ValueError):
        Scatter(data=wrong_data)


def test_set_xlabel():
    fpath = "tests/test_data/vis1.csv"
    sc = Scatter(data=fpath, x="b", y="a")

    assert sc.opts["xLabel"] == ""
    assert sc.opts["labelFontSize"] == 2
    sc.set_xlabel("x label", fontsize=1.5)
    assert sc.opts["xLabel"] == "x label"
    assert sc.opts["labelFontSize"] == 1.5


def test_dataframe_input():
    df = pd.DataFrame({"a": ["a", "b"], "b": [1, 2], "c": [3, 4]})

    with pytest.raises(ValueError):
        sc = Scatter(data=df, x="a", y="d")

    sc = Scatter(data=df, x="b", y="c")

    assert sc.opts["axisStrokeWidth"] == 0.5
    sc.set_options(axis_stroke_width=1)
    assert sc.opts["axisStrokeWidth"] == 1
