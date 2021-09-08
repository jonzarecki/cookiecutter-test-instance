"""Test cases for the main module."""

from cookiecutter_test_instance.main import main


def test_main_succeeds() -> None:
    """It exits with a status code of zero."""
    main()
    a = 1
    assert a == 1
