import os

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
DATA_TYPE = (".csv", ".tsv")


class Line(BaseChart):
    CHART_TYPE = "Line"
    LINE_KWARGS = {
        "xlabel": "xLabel",
        "ylabel": "yLabel",
        "axis_fontsize": "axisFontSize",
        "label_fontsize": "labelFontSize",
        "axis_roughness": "axisRoughness",
        "axis_stroke_width": "axisStrokeWidth",
        "inner_stroke_width": "innerStrokeWidth",
        "padding": "padding",
        "highlight": "highlight",
        "colors": "colors",
        "stroke": "stroke",
        "simplification": "simplification",
        "legend": "legend",
        "legend_position": "legendPosition",
        "circle": "circle",
        "circle_radius": "circleRadius",
        "circle_roughness": "circleRoughness",
    }

    def __init__(
        self,
        data,
        xlabel=None,
        ylabel=None,
        axis_fontsize=1,
        label_fontsize=2,
        axis_roughness=0.5,
        axis_stroke_width=0.5,
        colors=None,
        font="Gaegu",
        highlight="green",
        inner_stroke_width=0,
        stroke="black",
        simplification=0.2,
        legend=True,
        legend_position="right",
        circle=True,
        circle_radius=10,
        circle_roughness=2,
        **kwargs
    ):
        super().__init__(data)

        self.opts["colors"] = colors or DEFAULT_COLORS

        # Line plot is slightly different than other plots, therefore, preprocessing
        # is needed beforehand
        ys = [kw for kw in kwargs if kw.startswith("y") and kw != "ylabel"]
        ys_dict = {y: kwargs.pop(y) for y in ys}

        self._assign_input_values(None, None, **ys_dict)

        self.opts["xLabel"] = self._xstr(xlabel)
        self.opts["yLabel"] = self._xstr(ylabel)

        self.opts["axisFontSize"] = axis_fontsize
        self.opts["labelFontSize"] = label_fontsize
        self.opts["font"] = font
        self.opts["axisRoughness"] = axis_roughness
        self.opts["axisStrokeWidth"] = axis_stroke_width
        self.opts["highlight"] = highlight
        self.opts["innerStrokeWidth"] = inner_stroke_width
        self.opts["simplification"] = simplification
        self.opts["stroke"] = stroke
        self.opts["legend"] = legend
        self.opts["legendPosition"] = legend_position
        self.opts["circle"] = circle
        self.opts["circleRoughness"] = circle_roughness
        self.opts["circleRadius"] = circle_radius

        self._set_kwargs(**kwargs)

        # The fillStyle seems should not be assigned
        if "fillStyle" in self.opts:
            self.opts.pop("fillStyle")

    @staticmethod
    def _check_input_data(data):
        if not isinstance(data, str):
            raise TypeError("Only valid type of data is objects")
        elif isinstance(data, str) and not data.endswith(DATA_TYPE):
            raise ValueError(
                "Wrong format of data, has be to either csv or tsv format."
            )
        elif isinstance(data, str) and not os.path.exists(data):
            raise FileNotFoundError("The data file is not found.")

    def _assign_input_values(self, values, labels, **ys_dict):
        for y, value in ys_dict.items():
            self.opts[y] = value

    def set_options(self, **kwargs):

        mapping = {**self.BASE_KWARGS, **self.LINE_KWARGS}
        self._set_kwargs(mapping, **kwargs)
