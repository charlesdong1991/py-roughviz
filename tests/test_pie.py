import pytest
import pandas as pd

from roughviz.charts.pie import Pie


def test_wrong_input_data():
    wrong_data = {
        "loc": ["North", "South", "East", "West"],
        "values": [10, 5, 8, 3]
    }
    with pytest.raises(ValueError):
        Pie(data=wrong_data)


def test_wrong_data_path():
    fpath = "test_data/wrong.csv"
    with pytest.raises(FileNotFoundError):
        Pie(data=fpath)


def test_change_options_dict_data():
    data = {
        "labels": ["North", "South", "East", "West"],
        "values": [10, 5, 8, 3]
    }

    pie = Pie(data=data)

    # Since Pie Plot does not have axisFontSize option, so should raise error
    with pytest.raises(KeyError):
        assert pie.opts["axisFontSize"]

    assert pie.opts["highlight"] == "coral"
    pie.set_options(highlight="skyblue")
    assert pie.opts["highlight"] == "skyblue"


def test_dataframe_input():
    df = pd.DataFrame({"a": ["a", "b"], "b": [1, 2], "c": [3, 4]})

    with pytest.raises(ValueError):
        pie = Pie(data=df, values="a", labels="d")

    pie = Pie(data=df, labels="a", values="b")

    assert pie.opts["legendPosition"] == "right"
    pie.set_options(legend_position="left")
    assert pie.opts["legendPosition"] == "left"
