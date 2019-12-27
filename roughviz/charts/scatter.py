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
SCATTER_DATA_KEYS = {"x", "y"}


class Scatter(BaseChart):
    CHART_TYPE = "Scatter"
    SCATTER_KWARGS = {
        "xlabel": "xLabel",
        "ylabel": "yLabel",
        "axis_fontsize": "axisFontSize",
        "label_fontsize": "labelFontSize",
        "axis_roughness": "axisRoughness",
        "axis_stroke_width": "axisStrokeWidth",
        "inner_stroke_width": "innerStrokeWidth",
        "padding": "padding",
        "highlight": "highlight",
        "stroke": "stroke",
        "simplification": "simplification",
    }

    def __init__(
        self,
        data,
        x=None,
        y=None,
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
        stroke="black",
        simplification=0.2,
        radius=8,
        **kwargs
    ):
        super().__init__(data, x, y)
        self._assign_input_values(x, y)

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
        self.opts["axisRoughness"] = axis_roughness
        self.opts["highlight"] = highlight
        self.opts["innerStrokeWidth"] = inner_stroke_width
        self.opts["colors"] = colors
        self.opts["simplification"] = simplification
        self.opts["stroke"] = stroke

        self._set_kwargs(**kwargs)

    @staticmethod
    def _check_data_keys(data):
        if isinstance(data, dict) and set(data.keys()) != SCATTER_DATA_KEYS:
            raise ValueError("Has to be x and y")

    def _assign_input_values(self, x, y):
        if not x or not y:
            raise ValueError("You need to specify x and y as separate" "attributes.")
        self.opts["x"] = x
        self.opts["y"] = y

    def set_options(self, **kwargs):

        mapping = {**self.BASE_KWARGS, **self.SCATTER_KWARGS}
        self._set_kwargs(mapping, **kwargs)
