def exchange_money(budget, exchange_rate):
    exchanged_money = budget / exchange_rate

    return exchanged_money


print(exchange_money(127.5, 1.2))


def get_change(budget, exchanging_value):
    exchanged_money = budget - exchanging_value
    return exchanged_money


print(get_change(127.5, 120))


def get_value_of_bills(denomination, number_of_bills):
    bills = denomination * number_of_bills
    return bills


print(get_value_of_bills(5, 128))


def get_number_of_bills(budget, denomination):
    number_of_bills = budget // denomination
    return number_of_bills


print(get_number_of_bills(127.5, 5))


def get_leftover_of_bills(budget, denomination):
    leftover_of_bills = budget % denomination
    return leftover_of_bills


print(get_leftover_of_bills(127.5, 20))


def exchangeable_value(budget, exchange_rate, spread, denomination):
    spread = spread/100
    additional_fee = spread * exchange_rate  # 0.12
    exchange_rate = exchange_rate + additional_fee  # 1.2+0.12 = 1.32
    exchanged_money = budget / exchange_rate
    bills = exchanged_money // denomination
    maximum_value_new_currency = bills * denomination
    return maximum_value_new_currency


print(exchangeable_value(127.25, 1.20, 10, 20))
print(exchangeable_value(127.25, 1.20, 10, 5))
