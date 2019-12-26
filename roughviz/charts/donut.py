from roughviz.charts.base import BaseChart


class Donut(BaseChart):
    CHART_TYPE = "Donut"

    DONUT_KWARGS = {
        "font": "font",
        "titleFontSize": "title_fontsize",
        "highlight": "highlight",
        "inner_stroke_width": "innerStrokeWidth",
        "margin": "margin",
        "simplification": "simplification",
        "tooltipFontSize": "tooltip_fontsize"
    }

    def __init__(self,
                 data,
                 font=0,
                 title_fontsize=3,
                 highlight="green",
                 inner_stroke_width=0,
                 tooltip_fontsize=3,
                 simplification=0.2,
                 **kwargs):
        super().__init__(data)

        self.opts["font"] = font
        self.opts["titleFontSize"] = title_fontsize
        self.opts["tooltipFontSize"] = tooltip_fontsize

        self.opts["highlight"] = highlight
        self.opts["innerStrokeWidth"] = inner_stroke_width
        self.opts["simplification"] = simplification

        self._set_kwargs(**kwargs)

    def set_options(self, **kwargs):
        mapping = {**self.BASE_KWARGS, **self.DONUT_KWARGS}
        self._set_kwargs(mapping, **kwargs)
