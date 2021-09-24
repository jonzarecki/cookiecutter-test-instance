"""Sphinx configuration."""
import os
import sys
from datetime import datetime
from typing import List, Optional

from sphinx.ext import autodoc

sys.path.insert(0, os.path.abspath("../.."))  # Source code dir relative to this file

project = "Cookiecutter Test Instance"
author = "Claudio Jolowicz"
copyright = f"{datetime.now().year}, {author}"  # noqa
extensions = [
    "sphinx.ext.napoleon",
    "sphinx_rtd_theme",
    "sphinx.ext.autodoc",  # Core library for html generation from docstrings
    "sphinx.ext.autosummary",  # Create neat summary tables
    "sphinx.ext.coverage",
    "sphinx.ext.viewcode",
    "myst_parser",
    "notfound.extension",  # Generates 404 page
]
autodoc_typehints = "description"
autodoc_default_flags = ["members", "special-members", "private-members", "undoc-members"]
autosummary_generate = True  # Turn on sphinx.ext.autosummary

html_theme = "sphinx_rtd_theme"
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]


class VariableDocumenter(autodoc.DataDocumenter):
    def get_doc(self, _ignore: Optional[int] = None) -> Optional[List[List[str]]]:
        # Check the variable has a docstring-comment
        comment = self.get_module_comment(self.objpath[-1])
        if comment:
            return [comment]
        else:
            return [["No documentation. Add with ``#: member doc``"]]


def setup(app):  # type: ignore
    app.add_autodocumenter(VariableDocumenter)
