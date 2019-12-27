from roughviz.charts.base import BaseChart


class Donut(BaseChart):
    CHART_TYPE = "Donut"

    DONUT_KWARGS = {
        "font": "font",
        "highlight": "highlight",
        "inner_stroke_width": "innerStrokeWidth",
        "margin": "margin",
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
        simplification=0.2,
        **kwargs
    ):
        super().__init__(data, values, labels)

        self.opts["font"] = font
        self.opts["highlight"] = highlight
        self.opts["innerStrokeWidth"] = inner_stroke_width
        self.opts["simplification"] = simplification

        self._set_kwargs(**kwargs)

    def set_options(self, **kwargs):
        mapping = {**self.BASE_KWARGS, **self.DONUT_KWARGS}
        self._set_kwargs(mapping, **kwargs)
