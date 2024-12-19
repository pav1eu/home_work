import os
from unittest.mock import patch

import pandas as pd
import pytest

from src.file_reader import read_csv, read_excel


@pytest.mark.parametrize(
    "test_path, test_df, expected",
    [("test_a.csv", [{"a": 1, "b": 2}, {"a": 3, "b": 4}], [{"a": 1, "b": 2}, {"a": 3, "b": 4}])],
)
def test_read_csv(test_path: str, test_df: list, expected: list) -> None:
    df = pd.DataFrame(test_df)
    df.to_csv(test_path, sep=";")

    with patch("pandas.read_csv") as mock_read_csv:
        mock_read_csv.return_value = df
        result = read_csv(test_path)
        assert result == expected

    os.remove(test_path)


def test_read_excel_error() -> None:
    assert read_excel("error") == "FileNotFoundError"


def test_read_csv_error() -> None:
    assert read_csv("error") == "FileNotFoundError"
