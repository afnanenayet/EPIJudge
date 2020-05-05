from test_framework import generic_test


def power(x: float, y: int) -> float:
    if y == 0:
        return 1
    if y == 1:
        return x

    if y < 0:
        x = 1.0 / x
        y = -y

    power = y
    result = 1

    while power > 0:
        if power & 1 == 1:
            result *= x
        x = x * x
        power = power >> 1
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
