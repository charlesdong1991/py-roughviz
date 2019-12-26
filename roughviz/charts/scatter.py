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
DEFAULT_MARGIN = {"top": 50, "right": 20, "bottom": 70, "left": 100}


class Scatter(BaseChart):
    CHART_TYPE = "Scatter"
    SCATTER_KWARGS = {
        "xlabel": "xLabel",
        "ylabel": "yLabel",
        "axisFontSize": "axis_fontsize",
        "labelFontSize": "label_fontsize",
        "axisRoughness": "axis_roughness",
        "axisStrokeWidth": "axis_stroke_width",
        "highlight": "highlight",
        "inner_stroke_width": "innerStrokeWidth",
        "padding": "padding",
        "stroke": "stroke",
        "simplification": "simplification",
    }

    def __init__(
        self,
        data,
        xlabel=None,
        ylabel=None,
        axis_fontsize=1.5,
        label_fontsize=2,
        axis_roughness=0.5,
        colors=None,
        color_zero=False,
        margin=None,
        font="Gaegu",
        highlight="green",
        inner_stroke_width=0,
        title_fontsize=0.95,
        stroke="black",
        simplification=0.2,
        radius=8,
        **kwargs
    ):
        super().__init__(data)
        if colors is None:
            colors = DEFAULT_COLORS

        if margin is None:
            self.opts["margin"] = DEFAULT_MARGIN

        self.opts["xLabel"] = self._xstr(xlabel)
        self.opts["yLabel"] = self._xstr(ylabel)

        self.opts["axisFontSize"] = axis_fontsize
        self.opts["labelFontSize"] = label_fontsize
        self.opts["colorZero"] = color_zero
        self.opts["font"] = font
        self.opts["radius"] = radius
        self.opts["titleFontSize"] = title_fontsize
        self.opts["axisRoughness"] = axis_roughness
        self.opts["highlight"] = highlight
        self.opts["innerStrokeWidth"] = inner_stroke_width
        self.opts["colors"] = colors
        self.opts["simplification"] = simplification
        self.opts["stroke"] = stroke

        self._set_kwargs(**kwargs)

    @staticmethod
    def _check_data(data):
        if isinstance(data, dict) and set(data.keys()) != {"x", "y"}:
            raise ValueError("Has to be x and y")

    def set_options(self, **kwargs):

        mapping = {**self.BASE_KWARGS, **self.SCATTER_KWARGS}
        self._set_kwargs(mapping, **kwargs)
