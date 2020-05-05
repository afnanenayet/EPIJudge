from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    if len(prices) < 1:
        return 0

    max_profit = 0
    current_min = prices[0]

    # Keep track of the minimums as we iterate, since we can only sell after
    # we buy (meaning we don't have to look back). We can evaluate the
    # potential profit as we go along.
    for i, current_price in enumerate(prices):
        current_min = min(current_min, current_price)
        profit = current_price - current_min
        max_profit = max(max_profit, profit)
    return max(0, max_profit)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
