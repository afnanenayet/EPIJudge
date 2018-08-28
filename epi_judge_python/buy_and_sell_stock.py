from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    diff = 0
    curr_min = prices[0]

    for price in prices:
        diff = max(diff, price - curr_min)
        curr_min = min(curr_min, price)
    return max(0.0, diff)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "buy_and_sell_stock.py", "buy_and_sell_stock.tsv", buy_and_sell_stock_once
        )
    )
