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


class Pie(BaseChart):
    CHART_TYPE = "Pie"

    PIE_KWARGS = {
        "legend": "legend",
        "legend_position": "legendPosition",
        "font": "font",
        "highlight": "highlight",
        "inner_stroke_width": "innerStrokeWidth",
        "colors": "colors",
        "simplification": "simplification",
        "padding": "padding",
    }

    def __init__(
        self,
        data,
        values=None,
        labels=None,
        font=0,
        highlight="coral",
        inner_stroke_width=0,
        colors=None,
        simplification=0.2,
        padding=0.1,
        legend=True,
        legend_position="right",
        **kwargs
    ):
        super().__init__(data, values, labels)

        self.opts["colors"] = colors or DEFAULT_COLORS

        self.opts["font"] = font
        self.opts["highlight"] = highlight
        self.opts["innerStrokeWidth"] = inner_stroke_width
        self.opts["simplification"] = simplification
        self.opts["padding"] = padding
        self.opts["legend"] = legend
        self.opts["legendPosition"] = legend_position

        self._set_kwargs(**kwargs)

    def set_options(self, **kwargs):
        mapping = {**self.BASE_KWARGS, **self.PIE_KWARGS}
        self._set_kwargs(mapping, **kwargs)
