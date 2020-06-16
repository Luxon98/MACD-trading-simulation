from indicators import compute_signal, compute_macd, compute_profit
from data_reader import read_samples
from plotter import plot_index, plot_macd
from trader_functions import run_simulation


def main():
    print("Trading simulation on the BitBay cryptocurrency exchange - BTC/EUR")
    btc_samples = read_samples('csv/bitcoin_euro.csv')
    plot_index('BitBay', 'Bitcoin price', btc_samples)

    btc_macd = compute_macd(btc_samples)
    btc_signal = compute_signal(btc_macd)
    plot_macd('Bitcoin', btc_macd, btc_signal)

    btc_initial_value, btc_final_value = run_simulation(btc_samples, btc_macd, btc_signal)
    btc_profit = compute_profit(btc_initial_value, btc_final_value)
    print("The profit is ", round(btc_profit, 2), '%', sep='')

    print("Trading simulation on the Binance cryptocurrency exchange - ETH/USD")
    eth_samples = read_samples('csv/ethereum_usd.csv')
    plot_index('Binance', 'Ethereum price', eth_samples)

    eth_macd = compute_macd(eth_samples)
    eth_signal = compute_signal(eth_macd)
    plot_macd('Ethereum', eth_macd, eth_signal)

    eth_initial_value, eth_final_value = run_simulation(eth_samples, eth_macd, eth_signal)
    eth_profit = compute_profit(eth_initial_value, eth_final_value)
    print("The profit is ", round(eth_profit, 2), '%', sep='')


if __name__ == "__main__":
    main()
