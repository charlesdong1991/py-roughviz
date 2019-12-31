import pytest
import pandas as pd

from roughviz.charts.bar import Bar


def test_wrong_input_data():
    wrong_data = {
        "loc": ["North", "South", "East", "West"],
        "values": [10, 5, 8, 3]
    }
    with pytest.raises(ValueError):
        Bar(data=wrong_data)


def test_wrong_data_path():
    fpath = "test_data/wrong.csv"
    with pytest.raises(FileNotFoundError):
        Bar(data=fpath)


def test_change_options():
    fpath = "tests/test_data/vis2.csv"

    bar = Bar(data=fpath, values="b", labels="a")

    assert bar.opts["axisFontSize"] == 1.5
    bar.set_options(axis_fontsize=2)
    assert bar.opts["axisFontSize"] == 2

    assert bar.opts["highlight"] == "green"
    bar.set_options(highlight="coral")
    assert bar.opts["highlight"] == "coral"


def test_dataframe_input():
    df = pd.DataFrame({"a": ["a", "b"], "b": [1, 2], "c": [3, 4]})

    with pytest.raises(ValueError):
        bar = Bar(data=df, values="a", labels="d")

    bar = Bar(data=df, labels="a", values="b")

    assert bar.opts["width"] == 800
    bar.set_figsize(figsize=(600, 600))
    assert bar.opts["width"] == 600
