import pandas as pd

import pytest

from data_science.ml.features.target_builder import TargetBuilder


def test_build_raises_error_when_target_column_does_not_exist():
    # Arrange
    dataset = pd.DataFrame(
        {
            "title": ["Doc 1"],
        }
    )

    builder = TargetBuilder()

    # Act / Assert
    with pytest.raises(ValueError):
        builder.build(dataset)