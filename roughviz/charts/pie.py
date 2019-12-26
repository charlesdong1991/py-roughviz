from roughviz.charts.base import BaseChart

DEFAULT_MARGIN = {"top": 50, "right": 20, "bottom": 70, "left": 100}


class Pie(BaseChart):
    CHART_TYPE = "Pie"

    PIE_KWARGS = {
        "font": "font",
        "titleFontSize": "title_fontsize",
        "highlight": "highlight",
        "inner_stroke_width": "innerStrokeWidth",
        "margin": "margin",
        "simplification": "simplification",
    }

    def __init__(
        self,
        data,
        font=0,
        title_fontsize=3,
        highlight="green",
        inner_stroke_width=0,
        margin=None,
        tooltip_fontsize=3,
        simplification=0.2,
        **kwargs
    ):
        super().__init__(data)

        if margin is None:
            self.opts["margin"] = DEFAULT_MARGIN

        self.opts["font"] = font
        self.opts["titleFontSize"] = title_fontsize

        self.opts["highlight"] = highlight
        self.opts["innerStrokeWidth"] = inner_stroke_width
        self.opts["simplification"] = simplification

        self._set_kwargs(**kwargs)

    def set_options(self, **kwargs):
        mapping = {**self.BASE_KWARGS, **self.PIE_KWARGS}
        self._set_kwargs(mapping, **kwargs)
