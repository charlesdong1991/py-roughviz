import pytest

from roughviz.charts.donut import Donut


def test_wrong_input_data():
    wrong_data = {
        "loc": ["North", "South", "East", "West"],
        "values": [10, 5, 8, 3]
    }
    with pytest.raises(ValueError):
        Donut(data=wrong_data)


def test_wrong_data_path():
    fpath = "test_data/wrong.csv"
    with pytest.raises(FileNotFoundError):
        Donut(data=fpath)


def test_change_options_dict_data():
    data = {
        "labels": ["North", "South", "East", "West"],
        "values": [10, 5, 8, 3]
    }

    donut = Donut(data=data)

    # Since Pie Plot does not have axisFontSize option, so should raise error
    with pytest.raises(KeyError):
        assert donut.opts["axisFontSize"]

    assert donut.opts["legendPosition"] == "right"
    donut.set_options(legend_position="left")
    assert donut.opts["legendPosition"] == "left"
