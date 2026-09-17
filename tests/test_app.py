from pytest import approx
from src.app import square, cube


def test_square_positive_integer():
    assert square(5) == 25


def test_square_negative_integer():
    assert square(-4) == 16


def test_square_float():
    assert square(2.5) == approx(6.25)


def test_square_negative_float():
    assert square(-2.5) == approx(6.25)


def test_cube_positive_integer():
    assert cube(3) == 27


def test_cube_negative_integer():
    assert cube(-2) == -8


def test_cube_float():
    assert cube(1.5) == approx(3.375)


def test_cube_negative_float():
    assert cube(-1.5) == approx(-3.375)


def test_square_zero():
    assert square(0) == 0


def test_cube_zero():
    assert cube(0) == 0
