def get_leftover_of_bills(amount = 127.5, denomination = 20):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """
    result = amount % denomination
    return result
    
print(get_leftover_of_bills())

def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    result = (exchange_rate * spread)/100
    result_2 = budget * (1 - result)
    result_3 = result_2 // denomination
    result_4 = result_3 * denomination
    result_5 = result_4 - denomination
    return result_5
    
    
print(exchangeable_value(127.25, 1.20, 10, 20))
print(exchangeable_value(127.25, 1.20, 10, 5))