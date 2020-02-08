import os

from jinja2 import Template
from IPython.core.display import display, HTML

from roughviz.constant import TEMPLATE_PATH


class RenderEngine:
    def __init__(self, tmpl_file: str = "jupyter_notebook.html"):
        tmpl_file = os.path.join(TEMPLATE_PATH, tmpl_file)
        self.tmpl_file = tmpl_file

    def render_notebook(self):
        if hasattr(self, "render_to_tmpl"):
            self.render_to_tmpl()

        with open(self.tmpl_file) as f:
            tmpl_file = f.read()
        tmpl = Template(tmpl_file)

        output = tmpl.render(chart=self)
        return display(HTML(output))

    show = render_notebook
