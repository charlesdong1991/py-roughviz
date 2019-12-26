import pytest

from roughviz.charts.base import BaseChart


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


@pytest.mark.parametrize(
    "size, expected", [(0.5, "0.5rem"), (3, "3rem"), ("3rem", "3rem")]
)
def test_fontsize_converter(size, expected):
    assert BaseChart._fontsize_converter(size) == expected


@pytest.mark.parametrize("x, expected", [("a", "a"), ("", ""), (None, "")])
def test_xstr(x, expected):
    assert BaseChart._xstr(x) == expected
