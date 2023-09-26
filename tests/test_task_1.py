from task_1.task_1 import *
import pytest


# -------------
# Circle class
# -------------
@pytest.mark.parametrize("radius, result", [
    (4, 50.26548245743669),
    (1, 3.141592653589793)
])
def test_circle_calculate_area(radius, result):
    circle = Circle(radius)
    assert circle.calculate_area() == result


@pytest.mark.parametrize("radius, exception", [
    (0, ValueError),
    (-2, ValueError),
    ("key", TypeError)
])
def test_circle_size_errors(radius, exception):
    with pytest.raises(exception):
        Circle(radius)


# ---------------
# Triangle class
# ---------------
@pytest.mark.parametrize("side1, side2, side3, exception", [
    (0,4,5, ValueError),
    (2,-1,4, ValueError),
    (1,4,5, ValueError),
    ("в",4,5, TypeError)
])
def test_triangle_size_errors(side1, side2, side3, exception):
    with pytest.raises(exception):
        Triangle(side1, side2, side3)


@pytest.mark.parametrize("side1, side2, side3, result", [
    (2,4,5, 3.799671038392666),
    (7,24,25, 84.0)
])
def test_triangle_calculate_area(side1, side2, side3, result):
    triangle = Triangle(side1, side2, side3)
    assert triangle.calculate_area() == result


@pytest.mark.parametrize("side1, side2, side3, result", [
    (7,24,25, True),
    (3,4,5, True),
    (2,4,3, False),
])
def test_is_right_triangle(side1, side2, side3, result):
    triangle = Triangle(side1, side2, side3)
    assert triangle.is_right_triangle() == result


# ---------------------------
# calculate_all_figures_area
# ---------------------------
@pytest.mark.parametrize("args_result", [
    ((1,), 3.141592653589793),
    ((7,24,25), 84.0),
])
def test_calculate_all_figures_area(args_result):
    args, result = args_result
    assert calculate_all_figures_area(*args) == result


@pytest.mark.parametrize("args_result", [
    ((1,3), NotImplementedError),
    ((7,24,25,8), NotImplementedError),
])
def test_calculate_all_figures_area_errors(args_result):
    args, exception = args_result
    with pytest.raises(exception):
        calculate_all_figures_area(*args)

