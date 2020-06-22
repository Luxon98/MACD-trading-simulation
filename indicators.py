from constants import DAYS_NUMBER


# calculates the percentage of profit
def compute_profit(initial_value, final_value):
    profit = (final_value / initial_value) * 100 - 100
    return profit


# calculates the exponential moving average
def compute_ema(samples, current_day, days):
    a, b = samples[DAYS_NUMBER - current_day - 1], 1
    multiplier = 1 - (2 / (days + 1))  # one minus alpha

    for i in range(1, days):
        if DAYS_NUMBER - current_day - i - 1 < 0:
            a += (multiplier ** i) * samples[0]
        else:
            a += (multiplier ** i) * samples[DAYS_NUMBER - current_day - i - 1]

        b += (multiplier ** i)

    return a / b


# calculates values of MACD indicator
def compute_macd(samples):
    ema12, ema26, macd = [0] * DAYS_NUMBER, [0] * DAYS_NUMBER, [0] * DAYS_NUMBER
    for i in range(0, DAYS_NUMBER):
        ema12[i] = compute_ema(samples, DAYS_NUMBER - i - 1, 12)
        ema26[i] = compute_ema(samples, DAYS_NUMBER - i - 1, 26)
        macd[i] = ema12[i] - ema26[i]

    return macd


# calculates values of Signal indicator
def compute_signal(macd):
    signal = [0] * DAYS_NUMBER
    for i in range(0, DAYS_NUMBER):
        signal[i] = compute_ema(macd, DAYS_NUMBER - i - 1, 9)

    return signal
