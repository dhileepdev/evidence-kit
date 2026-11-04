import pytest


def test_package_imports():
    import evidence

    assert evidence.__version__ == "0.1.0"
