from constants import NO_DAYS


# calculates the percentage of profit
def compute_profit(initial_value, final_value):
    profit = (final_value / initial_value) * 100 - 100
    return profit


# calculates the exponential moving average
def compute_ema(samples, current_day, days):
    a, b = samples[NO_DAYS - current_day - 1], 1
    multiplier = 1 - (2 / (days + 1))  # one minus alpha

    for i in range(1, days):
        if NO_DAYS - current_day - i - 1 < 0:
            a += (multiplier ** i) * samples[0]
        else:
            a += (multiplier ** i) * samples[NO_DAYS - current_day - i - 1]

        b += (multiplier ** i)

    return a / b


# calculates values of MACD indicator
def compute_macd(samples):
    ema12, ema26, macd = [0] * NO_DAYS, [0] * NO_DAYS, [0] * NO_DAYS
    for i in range(0, NO_DAYS):
        ema12[i] = compute_ema(samples, NO_DAYS - i - 1, 12)
        ema26[i] = compute_ema(samples, NO_DAYS - i - 1, 26)
        macd[i] = ema12[i] - ema26[i]

    return macd


# calculates values of Signal indicator
def compute_signal(macd):
    signal = [0] * NO_DAYS
    for i in range(0, NO_DAYS):
        signal[i] = compute_ema(macd, NO_DAYS - i - 1, 9)

    return signal
