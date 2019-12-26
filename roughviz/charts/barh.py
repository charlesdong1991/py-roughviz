from roughviz.charts.base import BaseChart


class Barh(BaseChart):
    CHART_TYPE = "BarH"

    BARH_KWARGS = {
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
        highlight="coral",
        inner_stroke_width=0,
        padding=0.1,
        stroke="black",
        simplification=0.2,
        **kwargs
    ):
        super().__init__(data)

        self.opts["xLabel"] = self._xstr(xlabel)
        self.opts["yLabel"] = self._xstr(ylabel)

        self.opts["axisFontSize"] = axis_fontsize
        self.opts["labelFontSize"] = label_fontsize

        self.opts["axisRoughness"] = axis_roughness
        self.opts["highlight"] = highlight
        self.opts["innerStrokeWidth"] = inner_stroke_width
        self.opts["padding"] = padding
        self.opts["simplification"] = simplification
        self.opts["stroke"] = stroke

        self._set_kwargs(**kwargs)

    def set_options(self, **kwargs):
        mapping = {**self.BASE_KWARGS, **self.BARH_KWARGS}
        self._set_kwargs(mapping, **kwargs)
