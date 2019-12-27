import pytest

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
