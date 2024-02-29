"""Test florestsdk."""

import florestsdk


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(florestsdk.__name__, str)
