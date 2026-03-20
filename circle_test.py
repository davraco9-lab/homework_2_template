from circle import circle_class

test_circle = circle_class(1)
try:
    assert test_circle.area() == round(3.1416 * (1 ** 2), 4)
    assert test_circle.perimeter() == round(3.1416 * 2 * 1, 4)
    print('Test with radius 1 passed.')
except AssertionError:
    print('Test with radius 1 failed.')
