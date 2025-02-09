"""
   Best Time to Buy and Sell Stock
    Descripton:

    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    Find the maximum profit you can achieve. You may complete at most two transactions (Buy → Sell → Buy → Sell). (
    one transaction here means Buy and Sell)
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/

"""
import time

debug = True


def read_file(file_path):
    file = open(file_path)

    lines = [line[:-1] for line in file]
    return lines


def get_answer(row):
    total = row[0]

    return total


def main():
    data = read_file('data/prices.txt')
    start = time.time()
    for row in data:
        answer = get_answer(row)
        print(f"The Answer to {row} is '{answer}'")
    end = time.time()
    print(f"time taken: {end - start}")


if __name__ == "__main__":
    main()
