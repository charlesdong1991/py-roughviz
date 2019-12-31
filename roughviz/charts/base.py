import os
import json
import uuid
from numbers import Number
from typing import Optional, Union

import pandas as pd

from roughviz.render.engine import RenderEngine


DATA_TYPE = (".csv", ".tsv")
DATA_KEYS = {"labels", "values"}
DEFAULT_MARGIN = {"top": 50, "right": 20, "bottom": 70, "left": 100}


class BaseChart(RenderEngine):
    """
    This is the base class where all charts are inherited from
    """

    BASE_KWARGS = {
        "title": "title",
        "interactive": "interactive",
        "bowing": "bowing",
        "fill_style": "fillStyle",
        "fill_weight": "fillWeight",
        "stroke_width": "strokeWidth",
        "roughness": "roughness",
        "tooltip_fontsize": "tooltipFontSize",
        "title_fontsize": "titleFontSize",
        "width": "width",
        "height": "height",
        "margin": "margin",
    }

    def __init__(
        self,
        data,
        values: Optional[str] = None,
        labels: Optional[str] = None,
        title: Optional[str] = None,
        title_fontsize: Optional[Union[int, float]] = 0.95,
        width: Optional[int] = 800,
        height: Optional[int] = 600,
        interactive: bool = True,
        bowing: Optional[float] = 0.2,
        fill_style: Optional[str] = "cross-hatch",
        fill_weight: Optional[Union[int, float]] = 0,
        stroke_width: Optional[Union[int, float]] = 1,
        roughness: Optional[Union[int, float]] = 1,
        margin: Optional[dict] = None,
        tooltip_fontsize: Optional[Union[int, float]] = 0.95,
        **kwargs,
    ):
        super().__init__()
        self.opts: dict = {}

        self.data = data
        self._check_input_data(data)

        # Allow pd.DataFrame as inputs
        if isinstance(data, pd.DataFrame):
            if not (labels in data and values in data):
                raise ValueError("values and labels must be dataframe column names")
            data = {
                "values": data[values].values.tolist(),
                "labels": data[labels].values.tolist(),
            }

        self._assign_input_values(labels, values)
        self.opts["data"] = data

        self.opts["title"] = self._xstr(title)
        self.opts["margin"] = margin or DEFAULT_MARGIN

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
        """This method is used to render the content to the template
        """
        # Assign an id for container.
        self.element_id = uuid.uuid4().hex
        self.opts["element"] = "#" + self.element_id

        self._addition_conversion()
        self.json_content = json.dumps(self.opts)

    @staticmethod
    def _check_input_data(data):
        """Check the input data type and format.
        """
        if not isinstance(data, (str, dict, pd.DataFrame)):
            raise TypeError(
                "Only valid type of data is str and dictionary and pandas DataFrame."
            )
        elif isinstance(data, str) and not data.endswith(DATA_TYPE):
            raise ValueError("Wrong type of data")
        elif isinstance(data, str) and not os.path.exists(data):
            raise FileNotFoundError("The data file is not found.")
        elif isinstance(data, dict) and set(data.keys()) != DATA_KEYS:
            raise ValueError(
                "If input data is dictionary, you must provide both values and labels as keys"
            )

    def _assign_input_values(self, labels, values):
        """Assign the values for input data.
        """
        if isinstance(self.data, (str, pd.DataFrame)) and (not labels or not values):
            raise ValueError(
                "You need to specify labels and values as separate attributes."
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
        """Convert the fontsize if it is numeric. Since the unit of fontsize in roughviz is `rem`."""
        if isinstance(size, Number):
            return str(size) + "rem"
        return size

    def set_title(self, title: str, fontsize: Optional[Union[int, float]] = None):
        """Set the title for plots.

        Args:
            title: the title of the plot
            fontsize: the fontsize of the title, if None, use the default size.
        """
        self.opts["title"] = self._xstr(title)
        if fontsize:
            self.opts["titleFontSize"] = fontsize
        return self

    def set_xlabel(self, xlabel: str, fontsize: Optional[Union[int, float]] = None):
        """Set the xlabel for plots.

        Args:
            xlabel: the xlabel of the plot
            fontsize: the fontsize of the xlabel, if None, use the default size.
        """
        self.opts["xLabel"] = self._xstr(xlabel)
        if fontsize:
            self.opts["labelFontSize"] = fontsize
        return self

    def set_ylabel(self, ylabel: str, fontsize: Optional[Union[int, float]] = None):
        """Set the ylabel for plots.

        Args:
            ylabel: the ylabel of the plot
            fontsize: the fontsize of the ylabel, if None, use the default size.
        """
        self.opts["yLabel"] = self._xstr(ylabel)
        if fontsize:
            self.opts["labelFontSize"] = fontsize
        return self

    def set_figsize(self, figsize: tuple):
        """Set the figsize for plots, in a format of (width, height).

        Args:
            figsize: the figsize of the plot
        """
        if not isinstance(figsize, tuple):
            raise ValueError("figsize has to be a tuple.")
        self.opts["width"] = figsize[0]
        self.opts["height"] = figsize[1]

        return self

    def set_legend(self, legend: bool = True, legend_position: Optional[str] = "right"):
        """Set the legend for plots.

        Args:
            legend: if having legend or not, default is True.
            legend_position: the fontsize of the title, default is right.
        """
        if legend:
            self.opts["legendPosition"] = legend_position
        else:
            self.opts["legend"] = legend
        return self

    def _set_kwargs(self, mapping: Optional[dict] = None, **kwargs):
        """Making a mapping for keyword arguments due to syntax difference and assign corresponding
        values to mapped keywords.
        """
        if mapping is None:
            mapping = self.BASE_KWARGS
        for kw, kw_value in kwargs.items():
            self.opts[mapping[kw]] = kw_value
