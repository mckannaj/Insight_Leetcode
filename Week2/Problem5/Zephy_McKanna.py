"""
Say you have an array for which the ith element is the price of
a given stock on day i. If you were only permitted to complete at
most one transaction (ie, buy one and sell one share of the stock)
design an algorithm to find the maximum profit.

Example 1:

Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be
larger than buying price)

Example 2:

Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""


def max_profit_helper(price):
    if (type(price) is not list):
        print('Unknown input; max_profit_helper takes a list. Returning 0.')
        return 0
    if (len(price) < 2): # can't trade with less than two time points
        return 0

    max_out = 0
    min_seen = price[0]

    for x in price:
        if (x > min_seen): # we could sell here
            if (max_out < (x - min_seen)): # this is the best profit we've seen
                max_out = x - min_seen
        elif (x < min_seen): # on the other hand, we could buy here
            min_seen = x

    return max_out


# DON"T CHANGE THIS
def max_profit(price):
    return max_profit_helper(price)


def main():
    # Please feel free to come up with your own testcases below:
    # Test case: all same price.
    msg_same = "failed test case where all elements are the same"
    assert max_profit([3, 3, 3, 3, 3]) == 0, msg_same
    # Test case: empty list
    msg_empty = "failed test case where empty list was passed in"
    assert max_profit([]) == 0, msg_empty
    # Test case: two options for selling give the same profit.
    msg_two = "failed test case where two options with the same profit exists"
    assert max_profit([1, 6, 6]) == 5, msg_two
    # Test case: only one element in list
    msg_one = "failed test case where only one element was available in list"
    assert max_profit([3]) == 0, msg_one

    print("Expecting 0 (all same element); your output is {}".format(max_profit([3, 3, 3, 3, 3])))
    print("Expecting some kind of error; your output is {}".format(max_profit({})))
    print("Expecting 5; your output is {}".format(max_profit([7, 1, 5, 3, 6, 4])))
    print("Expecting 0; your output is {}".format(max_profit([7, 6, 4, 3, 1])))
    print("Expecting 8; your output is {}".format(max_profit([10, 1, 9, 2, 8, 3, 7, 4, 6, 5])))
    print("Expecting 9; your output is {}".format(max_profit([5, 6, 4, 7, 3, 8, 2, 9, 1, 10])))


if __name__ == "__main__":
    main()