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


class Pie(BaseChart):
    CHART_TYPE = "Pie"

    PIE_KWARGS = {
        "font": "font",
        "highlight": "highlight",
        "inner_stroke_width": "innerStrokeWidth",
        "margin": "margin",
        "colors": "colors",
        "simplification": "simplification",
    }

    def __init__(
        self,
        data,
        values=None,
        labels=None,
        font=0,
        highlight="green",
        inner_stroke_width=0,
        margin=None,
        colors=None,
        simplification=0.2,
        **kwargs
    ):
        super().__init__(data, values, labels)

        self.opts["colors"] = colors or DEFAULT_COLORS
        self.opts["margin"] = margin or DEFAULT_MARGIN

        self.opts["font"] = font

        self.opts["highlight"] = highlight
        self.opts["innerStrokeWidth"] = inner_stroke_width
        self.opts["simplification"] = simplification

        self._set_kwargs(**kwargs)

    def set_options(self, **kwargs):
        mapping = {**self.BASE_KWARGS, **self.PIE_KWARGS}
        self._set_kwargs(mapping, **kwargs)
