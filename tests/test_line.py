import pytest

from roughviz.charts.line import Line


def test_wrong_type_input_data():
    wrong_type_data = {
        "loc": ["North", "South", "East", "West"],
        "values": [10, 5, 8, 3]
    }
    with pytest.raises(TypeError):
        Line(data=wrong_type_data)


def test_wrong_data_path():
    fpath = "test_data/wrong.csv"
    with pytest.raises(FileNotFoundError):
        Line(data=fpath)


def test_set_ylabel():
    fpath = "tests/test_data/vis1.csv"
    line = Line(data=fpath, y1="b", y2="a")

    assert line.opts["yLabel"] == ""
    assert line.opts["labelFontSize"] == 2
    line.set_ylabel("y label", fontsize=1.5)
    assert line.opts["yLabel"] == "y label"
    assert line.opts["labelFontSize"] == 1.5
