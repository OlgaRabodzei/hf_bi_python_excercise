import pandas as pd
import pytest

from src.etl import (
    filter_by_key_word,
    add_sum_of_two_columns,
    categorize_time,
    add_category_derived_from_time_sum,
    aggregate_by_category,
)

@pytest.mark.parametrize(
    "key_word, expected",
    [
        ("Chilies", 3),
        ("Chiles", 3),
        ("cream", 1),
        ("pork", 0)
    ]
)
def test_filter_by_key_word(data: pd.DataFrame, key_word: str, expected: int):
    result = filter_by_key_word(data, "ingredients", key_word)
    assert result.shape[0] == expected


def test_add_sum_of_two_columns(data: pd.DataFrame):
    df = data.copy()
    add_sum_of_two_columns(
        df,
        sum_column_name="totalTime",
        column_1="prepTime",
        column_2="cookTime"
    )
    assert df["totalTime"].equals(df["prepTime"] + df["cookTime"])


@pytest.mark.parametrize(
    "minutes, expected",
    [
        (None, "Unknown"),
        (15, "Easy"),
        (45, "Medium"),
        (90, "Hard")
    ]
)
def test_categorize_time(minutes: int, expected: str):
    result = categorize_time(minutes)
    assert result == expected


def test_add_category_derived_from_time_sum(data: pd.DataFrame):
    # Prepare
    df = data.copy()
    # Set values to check category.
    df["prepTime"].iloc[0] = pd.NaT
    df["cookTime"].iloc[0] = pd.NaT
    add_sum_of_two_columns(
        df,
        sum_column_name="totalTime",
        column_1="prepTime",
        column_2="cookTime"
    )
    # Run
    add_category_derived_from_time_sum(
        df,
        column_name="difficulty",
        time_sum_column="totalTime"
    )
    # Assert
    assert df["difficulty"].isin(["Easy", "Medium", "Hard", "Unknown"]).all()
    assert df["difficulty"].iloc[0] == "Unknown"


def test_aggregate_by_category(data: pd.DataFrame):
    # Prepare
    df = data.copy()
    # Make sure that we have one row with Unknown difficulty
    df["prepTime"].iloc[1] = pd.NaT
    df["cookTime"].iloc[1] = pd.NaT
    add_sum_of_two_columns(
        df,
        sum_column_name="totalTime",
        column_1="prepTime",
        column_2="cookTime"
    )
    add_category_derived_from_time_sum(
        df,
        column_name="difficulty",
        time_sum_column="totalTime"
    )
    # Run
    result = aggregate_by_category(df, "difficulty")
    # Assert
    assert result.shape[0] == 2
    assert result.index.isin(["Easy", "Medium", "Hard"]).all()
    assert result.columns.isin(["avgTotalTime", "count"]).all()
