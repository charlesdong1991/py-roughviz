import pytest
import pandas as pd

from roughviz.charts.stacked_bar import StackedBar


def test_wrong_type_data():
    wrong_data = {"loc": ["North", "South", "East", "West"], "values": [10, 5, 8, 3]}
    match = "Only valid type of data is list"

    with pytest.raises(TypeError, match=match):
        StackedBar(data=wrong_data, labels="loc")


def test_wrong_list_data():
    wrong_data = [
        {"month": "Jan", "A": 20, "B": 5},
        {"month": "Feb", "A": 25, "B": 10},
        [1, 2, 3],
    ]
    match = "All elements in data need to be dictionary"

    with pytest.raises(TypeError, match=match):
        StackedBar(data=wrong_data, labels="month")


def test_wrong_label():
    data = [{"month": "Jan", "A": 20, "B": 5}, {"month": "Feb", "A": 25, "B": 10}]
    match = "Label has be to one of labels in data"

    with pytest.raises(ValueError, match=match):
        StackedBar(data=data, labels="not_exist")


def test_change_options_dict_data():
    data = [{"month": "Jan", "A": 20, "B": 5}, {"month": "Feb", "A": 25, "B": 10}]

    sb = StackedBar(data=data, labels="month")

    # Since Pie Plot does not have axisFontSize option, so should raise error
    with pytest.raises(KeyError):
        assert sb.opts["legend"]

    assert sb.opts["title"] == ""
    sb.set_options(title="StackBar")
    assert sb.opts["title"] == "StackBar"


def test_raise_error_with_dataframe():
    df = pd.DataFrame({"a": [1, 2], "b": ["a", "b"]})

    with pytest.raises(TypeError):
        StackedBar(data=df, labels="a")
