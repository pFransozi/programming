'''
It is an example of a greedy algorithm. The algorithm chooses the optimal path. For that,
in our example, the denominations must be in order.
'''
from unittest import TestCase

def make_change(target_amount):
    denominations = [200, 100, 50, 20, 10, 5, 2, 1]

    coin_count = 0
    values = []

    for coin in denominations:
        while target_amount >= coin:
            target_amount -= coin
            values.append(coin)
            coin_count += 1

    return coin_count, values


coin_count, values = make_change(24)
TestCase().assertEqual(coin_count, 3)
TestCase().assertEqual(values, [20, 2, 2])

coin_count, values = make_change(163)
TestCase().assertEqual(coin_count, 5)
TestCase().assertEqual(values, [100, 50, 10, 2, 1])


