import pandas as pd


# column name with specific values should be "Price", data should be sorted from newest to oldest
def read_samples(csv_filename):
    data = pd.read_csv(csv_filename)
    samples = data['Price'].values
    samples = samples[::-1]
    return samples
