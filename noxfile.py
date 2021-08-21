"""Nox sessions."""
import shutil
import sys
from pathlib import Path
from textwrap import dedent

import nox

try:
    from nox_poetry import Session, session
except ImportError:
    message = f"""\
    Nox failed to import the 'nox-poetry' package.

    Please install it using the following command:

    {sys.executable} -m pip install nox-poetry"""
    raise SystemExit(dedent(message))  # pylint: disable=raise-missing-from


package = "instance"
python_versions = ["3.7"]
nox.needs_version = ">= 2021.6.6"
nox.options.sessions = (
    "safety",
    "tests",
    "typeguard",
    "xdoctest",
    "docs-build",
)


@session(python=python_versions)
def safety(sess: Session) -> None:
    """Scan dependencies for insecure packages."""
    requirements = sess.poetry.export_requirements()
    sess.install("safety")
    sess.run("safety", "check", "--full-report", f"--file={requirements}")


@session(python=python_versions)
def tests(sess: Session) -> None:
    """Run the test suite."""
    sess.install(".")
    sess.install("coverage[toml]", "pytest", "pygments")
    try:
        sess.run("coverage", "run", "--parallel", "-m", "pytest", *sess.posargs)
    finally:
        if sess.interactive:
            sess.notify("coverage", posargs=[])


@session
def coverage(sess: Session) -> None:
    """Produce the coverage report."""
    args = sess.posargs or ["report"]

    sess.install("coverage[toml]")

    if not sess.posargs and any(Path().glob(".cache/.coverage.*")):
        sess.run("coverage", "combine")

    sess.run("coverage", *args)


@session(python=python_versions)
def typeguard(sess: Session) -> None:
    """Runtime type checking using Typeguard."""
    sess.install(".")
    sess.install("pytest", "typeguard", "pygments")
    sess.run("pytest", f"--typeguard-packages={package}", *sess.posargs)


@session(python=python_versions)
def xdoctest(sess: Session) -> None:
    """Run examples with xdoctest."""
    args = sess.posargs or ["all"]
    sess.install(".")
    sess.install("xdoctest[colors]")
    sess.run("python", "-m", "xdoctest", package, *args)


@session(name="docs-build", python=python_versions)
def docs_build(sess: Session) -> None:
    """Build the documentation."""
    args = sess.posargs or ["docs", "docs/_build"]
    sess.install(".")
    sess.install("sphinx", "sphinx-click", "sphinx-rtd-theme")

    build_dir = Path("docs", "_build")
    if build_dir.exists():
        shutil.rmtree(build_dir)

    sess.run("sphinx-build", *args)


@session(python=python_versions)
def docs(sess: Session) -> None:
    """Build and serve the documentation with live reloading on file changes."""
    args = sess.posargs or ["--open-browser", "docs", "docs/_build"]
    sess.install(".")
    sess.install("sphinx", "sphinx-autobuild", "sphinx-click", "sphinx-rtd-theme")

    build_dir = Path("docs", "_build")
    if build_dir.exists():
        shutil.rmtree(build_dir)

    sess.run("sphinx-autobuild", *args)
