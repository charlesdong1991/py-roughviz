import json
import uuid
from numbers import Number
from typing import Optional

from roughviz.render.engine import RenderEngine


DATA_TYPE = (".csv", ".tsv")
DATA_KEYS = {"labels", "values"}


class BaseChart(RenderEngine):
    BASE_KWARGS = {
        "title": "title",
        "interactive": "interactive",
        "bowing": "bowing",
        "fill_style": "fillStyle",
        "fill_weight": "fillWeight",
        "stroke_width": "strokeWidth",
        "roughtness": "roughness",
        "tooltip_fontsize": "tooltipFontSize",
        "title_fontsize": "titleFontSize",
        "width": "width",
        "height": "height",
    }

    def __init__(
        self,
        data,
        values=None,
        labels=None,
        title: Optional[str] = None,
        title_fontsize=0.95,
        width=800,
        height=600,
        interactive=True,
        bowing=0.2,
        fill_style="cross-hatch",
        fill_weight=0,
        stroke_width=1,
        roughness=1,
        tooltip_fontsize=0.95,
        **kwargs,
    ):
        super().__init__()
        self.opts: dict = {}

        self.data = data
        self._check_input_data(data)

        self._assign_input_values(labels, values)
        self.opts["data"] = data

        self.opts["title"] = self._xstr(title)
        self.opts["width"] = width
        self.opts["height"] = height
        self.opts["interactive"] = interactive
        self.opts["bowing"] = bowing
        self.opts["fillStyle"] = fill_style
        self.opts["fillWeight"] = fill_weight
        self.opts["strokeWidth"] = stroke_width
        self.opts["roughness"] = roughness
        self.opts["tooltipFontSize"] = tooltip_fontsize
        self.opts["titleFontSize"] = title_fontsize

    def render_to_tmpl(self):
        self.element_id = uuid.uuid4().hex
        self.opts["element"] = "#" + self.element_id

        self._addition_conversion()
        self.json_content = json.dumps(self.opts)

    @staticmethod
    def _check_input_data(data):
        if not isinstance(data, (str, dict)):
            raise TypeError("Only valid type of data is str and dictionary.")
        elif isinstance(data, str) and not data.endswith(DATA_TYPE):
            raise ValueError("Wrong type of data")
        elif isinstance(data, dict) and set(data.keys()) != DATA_KEYS:
            raise ValueError(
                "If input data is dictionary, you must provide both values and labels as keys"
            )

    def _assign_input_values(self, labels, values):
        if isinstance(self.data, str) and (not labels or not values):
            raise ValueError(
                "You need to specify labels and values as separate" "attributes."
            )
        self.opts["labels"] = labels
        self.opts["values"] = values

    def _addition_conversion(self):
        self._convert_fontsize_unit()

    def _convert_fontsize_unit(self):
        fontsize_opts = [opt for opt in self.opts if opt.endswith("FontSize")]

        for opt in fontsize_opts:
            self.opts[opt] = self._fontsize_converter(self.opts[opt])

    @staticmethod
    def _xstr(s):
        return "" if s is None else s

    @staticmethod
    def _fontsize_converter(size):
        if isinstance(size, Number):
            return str(size) + "rem"
        return size

    def set_title(self, title, fontsize=None):
        self.opts["title"] = self._xstr(title)
        if fontsize:
            self.opts["titleFontSize"] = fontsize
        return self

    def set_xlabel(self, xlabel, fontsize=None):
        self.opts["xLabel"] = self._xstr(xlabel)
        if fontsize:
            self.opts["labelFontSize"] = fontsize
        return self

    def set_ylabel(self, ylabel, fontsize=None):
        self.opts["yLabel"] = self._xstr(ylabel)
        if fontsize:
            self.opts["labelFontSize"] = fontsize
        return self

    def set_figsize(self, figsize):
        if not isinstance(figsize, tuple):
            raise ValueError("figsize has to be a tuple.")
        self.opts["width"] = figsize[0]
        self.opts["height"] = figsize[1]

        return self

    def set_legend(self, legend=True, legend_position="right"):
        if legend:
            self.opts["legendPosition"] = legend_position
        else:
            self.opts["legend"] = legend
        return self

    def _set_kwargs(self, mapping=None, **kwargs):
        if mapping is None:
            mapping = self.BASE_KWARGS
        for kw, kw_value in kwargs.items():
            self.opts[mapping[kw]] = kw_value
