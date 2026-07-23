""" import numpy as np

from data_science.ml.features.dataset_splitter import DatasetSplitter


def test_split_returns_train_and_test_sets():
    # Arrange
    X = np.arange(100).reshape(10, 10)
    y = np.arange(10)

    splitter = DatasetSplitter()

    # Act
    X_train, X_test, y_train, y_test = splitter.split(X, y)

    # Assert
    assert len(X_train) == 8
    assert len(X_test) == 2
    assert len(y_train) == 8
    assert len(y_test) == 2

    ------------------------ """
import numpy as np

from data_science.ml.features.dataset_splitter import DatasetSplitter


def test_split_is_reproducible():
        # Arrange
        X = np.arange(100).reshape(10, 10)
        y = np.arange(10)

        splitter = DatasetSplitter()

        # Act
        result1 = splitter.split(X, y)
        result2 = splitter.split(X, y)

        # Assert
        for left, right in zip(result1, result2):
            assert np.array_equal(left, right)