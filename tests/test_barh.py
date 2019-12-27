import pytest

from roughviz.charts.barh import Barh


def test_wrong_input_data():
    wrong_data = {
        "loc": ["North", "South", "East", "West"],
        "values": [10, 5, 8, 3]
    }
    with pytest.raises(ValueError):
        Barh(data=wrong_data)


def test_wrong_data_path():
    fpath = "test_data/wrong.csv"
    with pytest.raises(FileNotFoundError):
        Barh(data=fpath)


def test_change_options():
    fpath = "tests/test_data/vis2.csv"

    barh = Barh(data=fpath, values="b", labels="a")

    assert barh.opts["axisFontSize"] == 1.5
    barh.set_options(axis_fontsize=2)
    assert barh.opts["axisFontSize"] == 2

    assert barh.opts["highlight"] == "coral"
    barh.set_options(highlight="skyblue")
    assert barh.opts["highlight"] == "skyblue"
