def solution(input):
    # no profit from trading in 1 day
    if len(prices) == 0:
        return 0

    # the idea is that if the current price is lower than the last bought price,
    # "refund" the last bought stock and buy this one instead.
    #
    # sell if the price is higher than purchased price
    # we will buy the same stock for now and "refund" later on if price drops

    lastBought = prices[0]
    profit = 0

    for p in prices[1:]:
        if p < lastBought:
            lastBought = p
        else:
            profit += p - lastBought
            lastBought = p

    return profit if profit > 0 else 0

if __name__ == "__main__":
    print(solution("")) # insert input in the quotes
