from roughviz.charts.base import BaseChart

DEFAULT_COLORS = [
    "coral",
    "skyblue",
    "#66c2a5",
    "tan",
    "#8da0cb",
    "#e78ac3",
    "#a6d854",
    "#ffd92f",
    "tan",
    "orange",
]


class StackedBar(BaseChart):

    CHART_TYPE = "StackedBar"
    STACKED_BAR_KWARGS = {
        "xlabel": "xLabel",
        "ylabel": "yLabel",
        "colors": "colors",
        "axis_fontsize": "axisFontSize",
        "label_fontsize": "labelFontSize",
        "axis_roughness": "axisRoughness",
        "axis_stroke_width": "axisStrokeWidth",
        "highlight": "highlight",
        "inner_stroke_width": "innerStrokeWidth",
        "padding": "padding",
        "stroke": "stroke",
        "simplification": "simplification",
    }

    def __init__(
        self,
        data,
        labels,
        xlabel=None,
        ylabel=None,
        axis_fontsize=1,
        label_fontsize=2,
        axis_roughness=0.5,
        colors=None,
        highlight="coral",
        inner_stroke_width=1,
        axis_stroke_width=0.5,
        padding=0.1,
        stroke="black",
        simplification=0.2,
        **kwargs
    ):
        super().__init__(data, labels)

        self.opts["colors"] = colors or DEFAULT_COLORS

        self.opts["xLabel"] = self._xstr(xlabel)
        self.opts["yLabel"] = self._xstr(ylabel)

        self.opts["axisFontSize"] = axis_fontsize
        self.opts["labelFontSize"] = label_fontsize

        self.opts["axisRoughness"] = axis_roughness
        self.opts["axisStrokeWidth"] = axis_stroke_width
        self.opts["highlight"] = highlight
        self.opts["innerStrokeWidth"] = inner_stroke_width
        self.opts["padding"] = padding
        self.opts["simplification"] = simplification
        self.opts["stroke"] = stroke

        self._set_kwargs(**kwargs)

    @staticmethod
    def _check_input_data(data):
        if not isinstance(data, list):
            raise TypeError("Only valid type of data is list.")
        if not all([isinstance(element, dict) for element in data]):
            raise TypeError("All elements in data need to be dictionary")

    def _assign_input_values(self, values, labels):
        data_keys = self.data[0].keys()
        if labels not in data_keys:
            raise ValueError("Label has be to one of labels in data.")
        self.opts["labels"] = labels

    def set_options(self, **kwargs):
        mapping = {**self.BASE_KWARGS, **self.STACKED_BAR_KWARGS}
        self._set_kwargs(mapping, **kwargs)
