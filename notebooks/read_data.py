import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_split(train_size: float=0.66, random_state: int = 42, verbose: bool = False):
    """
    Since the original data for the superconducting materials list obtained from
    [Japan's National Institute for Materials Science (NIMS)]
    (http://supercon.nims.go.jp/index_en.html) is no longer available, we have
    not found a way to reproduce the preprocessing steps outlined in the paper.
    """
    # Utilizes provided preprocessed training data
    data_df = pd.read_csv('../uci_supercondutor_data/train.csv')

    # Splits training and testing data.
    train, test = train_test_split(
        data_df,
        train_size=train_size,
        random_state=random_state
    )

    training_data = np.array(train)
    testing_data = np.array(test)

    # The total number of headers (81 features and 1 label)
    headers_length = len(training_data[0])

    # The first 81 columns are features.
    training_X = training_data[:,:headers_length-1]
    testing_X = testing_data[:,:headers_length-1]

    # The last column is temperature critical (labels).
    training_y = training_data[:,headers_length-1:headers_length]
    testing_y = testing_data[:,headers_length-1:headers_length]

    if verbose:
        # Prints shape of csv, training, and testing data.
        print(f"Data Shape: {np.shape(data_df)}")
        print(f"Training Features Shape: {training_X.shape}")
        print(f"Training Labels Shape: {training_y.shape}")
        print(f"Testing Features Shape: {testing_X.shape}")
        print(f"Testing Labels Shape: {testing_y.shape}")
        print(f"Training Size: {train_size} vs. Testing Size: {1 - train_size}")

    return training_X, training_y, testing_X, testing_y
