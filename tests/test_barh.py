import pytest
import pandas as pd

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


def test_dataframe_input():
    df = pd.DataFrame({"a": ["a", "b"], "b": [1, 2], "c": [3, 4]})

    with pytest.raises(ValueError):
        barh = Barh(data=df, values="a", labels="d")

    barh = Barh(data=df, labels="a", values="b")

    assert barh.opts["height"] == 600
    barh.set_figsize(figsize=(600, 800))
    assert barh.opts["height"] == 800
