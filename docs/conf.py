"""Sphinx configuration."""
from datetime import datetime


project = "Cookiecutter Test Instance"
author = "Claudio Jolowicz"
copyright = f"{datetime.now().year}, {author}"  # pylint: disable=redefined-builtin
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "sphinx_rtd_theme",
]
autodoc_typehints = "description"
html_theme = "sphinx_rtd_theme"
