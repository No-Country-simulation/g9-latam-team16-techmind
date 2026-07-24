import numpy as np
import pytest


@pytest.fixture
def sample_training_data():
    return {
        "features": np.array(
            [
                [0, 0],
                [0, 1],
                [1, 0],
                [1, 1],
            ]
        ),
        "target": np.array(
            [
                0,
                0,
                1,
                1,
            ]
        ),
    }