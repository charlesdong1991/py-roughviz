import pytest

from roughviz.charts.base import BaseChart


@pytest.fixture
def input_data():
    data = {"labels": ["a", "b"], "values": [1, 2]}
    return data


@pytest.mark.parametrize(
    "input_data, error, match_message",
    [
        (
            {"labels": ["a"], "value": [1]},
            ValueError,
            "must provide both values and labels as keys",
        ),
        ([1, 2, 3], TypeError, "Only valid type of data is str and dictionary"),
        ("wrong_data.txt", ValueError, "Wrong type of data"),
    ],
)
def test_invalid_input_data(input_data, error, match_message):
    with pytest.raises(error, match=match_message):
        BaseChart(data=input_data)


def test_data_file_not_found():
    fpath = "tests_data/wrong.csv"
    with pytest.raises(FileNotFoundError):
        BaseChart(data=fpath)


@pytest.mark.parametrize(
    "size, expected", [(0.5, "0.5rem"), (3, "3rem"), ("3rem", "3rem")]
)
def test_fontsize_converter(size, expected):
    assert BaseChart._fontsize_converter(size) == expected


@pytest.mark.parametrize("x, expected", [("a", "a"), ("", ""), (None, "")])
def test_xstr(x, expected):
    assert BaseChart._xstr(x) == expected


def test_set_title(input_data):
    bc = BaseChart(data=input_data)

    assert bc.opts["title"] == ""
    assert bc.opts["titleFontSize"] == 0.95

    bc.set_title("good", fontsize=2)

    assert bc.opts["title"] == "good"
    assert bc.opts["titleFontSize"] == 2


def test_set_figsize(input_data):
    bc = BaseChart(data=input_data)

    assert bc.opts["width"] == 800
    assert bc.opts["height"] == 600

    bc.set_figsize(figsize=(300, 400))

    assert bc.opts["width"] == 300
    assert bc.opts["height"] == 400
