from roughviz.charts.base import BaseChart


class Bar(BaseChart):
    CHART_TYPE = "Bar"
    BAR_KWARGS = {
        "xlabel": "xLabel",
        "ylabel": "yLabel",
        "color": "color",
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
        values=None,
        labels=None,
        xlabel=None,
        ylabel=None,
        axis_fontsize=1.5,
        label_fontsize=2,
        axis_roughness=0.5,
        axis_stroke_width=0.5,
        color="skyblue",
        highlight="green",
        inner_stroke_width=0,
        padding=0.1,
        stroke="black",
        simplification=0.2,
        **kwargs
    ):
        super().__init__(data, values, labels)

        self.opts["xLabel"] = self._xstr(xlabel)
        self.opts["yLabel"] = self._xstr(ylabel)

        self.opts["axisFontSize"] = axis_fontsize
        self.opts["labelFontSize"] = label_fontsize

        self.opts["color"] = color
        self.opts["axisRoughness"] = axis_roughness
        self.opts["axisStrokeWidth"] = axis_stroke_width
        self.opts["highlight"] = highlight
        self.opts["innerStrokeWidth"] = inner_stroke_width
        self.opts["padding"] = padding
        self.opts["simplification"] = simplification
        self.opts["stroke"] = stroke

        self._set_kwargs(**kwargs)

    def set_options(self, **kwargs):
        mapping = {**self.BASE_KWARGS, **self.BAR_KWARGS}
        self._set_kwargs(mapping, **kwargs)
