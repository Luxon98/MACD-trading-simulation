from constants import *


def buy_shares(current_price, quantity, no_units, money):
    no_units += quantity
    money -= current_price * quantity
    return no_units, money


def sell_shares(current_price, quantity, no_units, money):
    no_units -= quantity
    money += current_price * quantity
    return no_units, money


def run_simulation(samples, macd, signal):
    current_money, no_units = INITIAL_MONEY, INITIAL_SHARES_NUMBER
    initial_value = no_units * samples[0] + current_money

    change_flag, bs_flag = False, False
    for i in range(1, DAYS_NUMBER):
        if macd[i - 1] <= signal[i - 1] and macd[i] > signal[i]:
            change_flag = True
            bs_flag = True
        elif macd[i - 1] >= signal[i - 1] and macd[i] < signal[i]:
            change_flag = True
            bs_flag = False
        else:
            change_flag = False

        if change_flag and bs_flag:
            if current_money >= 10 * samples[i]:
                no_units, current_money = buy_shares(samples[i], 10, no_units, current_money)
        elif change_flag and not bs_flag:
            if no_units >= 10:
                no_units, current_money = sell_shares(samples[i], 10, no_units, current_money)

    final_value = no_units * samples[999] + current_money
    return initial_value, final_value
