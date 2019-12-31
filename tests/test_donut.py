import pytest
import pandas as pd

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


def test_dataframe_input():
    df = pd.DataFrame({"a": ["a", "b"], "b": [1, 2], "c": [3, 4]})

    with pytest.raises(ValueError):
        donut = Donut(data=df, values="a", labels="d")

    donut = Donut(data=df, labels="a", values="b")

    assert donut.opts["font"] == 0
    donut.set_options(font=1)
    assert donut.opts["font"] == 1
