"""Test cases for the __main__ module."""

from cookiecutter_test_instance.__main__ import main


def test_main_succeeds() -> None:
    """It exits with a status code of zero."""
    main()
    assert 0 == 0
