import matplotlib.pyplot as plt
from constants import DAYS_NUMBER


def get_days_arr():
    days_ago = [0] * DAYS_NUMBER
    for i in range(0, DAYS_NUMBER):
        days_ago[i] = DAYS_NUMBER - i - 1

    return days_ago


def plot_index(title, caption, samples_arr):
    plt.plot(get_days_arr(), samples_arr, color='#2d862d', label=caption)
    plt.gca().invert_xaxis()
    plt.title(title)
    plt.xlabel('Days ago')
    plt.ylabel('Price')
    plt.legend(loc='lower right')
    plt.show()


def plot_macd(title, macd_arr, signal_arr):
    plt.plot(get_days_arr(), macd_arr, color='#0086b3', label='MACD')  # MACD indicator has blue color
    plt.plot(get_days_arr(), signal_arr, color='#e60000', label='SIGNAL')  # Signal indicator has red color
    plt.gca().invert_xaxis()
    plt.title(title + ': MACD/SIGNAL')
    plt.xlabel('Days ago')
    plt.ylabel('Value')
    plt.legend(loc='lower center')
    plt.show()
