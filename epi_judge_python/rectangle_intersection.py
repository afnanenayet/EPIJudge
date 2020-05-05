import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple("Rect", ("x", "y", "width", "height"))


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    if not intersects(r1, r2):
        return Rect(0, 0, -1, -1)
    return Rect(
        max(r1.x, r2.x),
        max(r1.y, r2.y),
        min(r1.x + r1.width, r2.x + r2.width) - max(r1.x, r2.x),
        min(r1.y + r1.height, r2.y + r2.height) - max(r1.y, r2.y),
    )


def intersects(r1: Rect, r2: Rect) -> bool:
    """Return whether two rectangles intersect
    """
    # Check if there's an intersection on the x-axis
    x_isect = r1.x <= r2.x + r2.width and r2.x <= r1.x + r1.width
    # Check if there's an intersection on the y-axis
    y_isect = r1.y <= r2.y + r2.height and r2.y <= r1.y + r1.height
    return x_isect and y_isect


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "rectangle_intersection.py",
            "rectangle_intersection.tsv",
            intersect_rectangle_wrapper,
            res_printer=res_printer,
        )
    )
