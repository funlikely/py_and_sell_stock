"""
   Best Time to Buy and Sell Stock
    Descripton:

    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    Find the maximum profit you can achieve. You may complete at most two transactions (Buy → Sell → Buy → Sell). (
    one transaction here means Buy and Sell)
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/

"""
import time
import ast

debug = True


lookup = {}


def read_file(file_path):
    file = open(file_path)

    lines = [line[:-1] for line in file]
    return [ast.literal_eval(line) for line in lines]


def buy_sell(prices, current_return=0):
    global lookup

    if str(prices) in lookup.keys:
        max_return = current_return + lookup[str(prices)]
    elif len(prices) < 2:
        max_return = current_return
    elif len(prices) == 2 and prices[1] > prices[0]:
        max_return = current_return + prices[1] - prices[0]
    else:
        max_return = max([buy_sell(prices[1:], current_return)] +
                         [buy_sell(prices[(i+1):], current_return + prices[i+1] - prices[0]) for i in range(len(prices)) if prices[i+1] > prices[0]])

    lookup[str(prices)] = max_return

    return max_return


def main():
    data = read_file('data/prices.txt')
    start = time.time()
    for row in data:
        answer = buy_sell(row)
        print(f"The Answer to {row} is '{answer}'")
    end = time.time()
    print(f"time taken: {end - start}")


if __name__ == "__main__":
    main()
