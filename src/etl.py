import pandas as pd


def transform_data(data: pd.DataFrame) -> pd.DataFrame:
    # Transform data
    df = filter_by_key_word(data, "ingredients", "Chilies")
    add_sum_of_two_columns(df, "totalTime", "prepTime", "cookTime")
    add_category_derived_from_time_sum(
        df, column_name="difficulty", time_sum_column="totalTime"
    )

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    return df


def filter_by_key_word(
    df: pd.DataFrame, column_name: str, key_word: str
) -> pd.DataFrame:
    # TODO: add word similarity.
    return df[df[column_name].str.contains(key_word, case=False)].copy()


def add_sum_of_two_columns(
    df: pd.DataFrame, sum_column_name: str, column_1: str, column_2: str
) -> None:
    df[sum_column_name] = df[column_1] + df[column_2]


def categorize_time(minutes):
    if pd.isna(minutes):
        return "Unknown"
    elif minutes > 60:
        return "Hard"
    elif minutes > 30:
        return "Medium"
    else:
        return "Easy"


def add_category_derived_from_time_sum(
    df: pd.DataFrame,
    column_name: str,
    time_sum_column: str,
) -> None:
    df[column_name] = df[time_sum_column].dt.total_seconds() / 60
    df[column_name] = df[column_name].apply(categorize_time)


def aggregate_by_category(
    df: pd.DataFrame, category_column: str
) -> pd.DataFrame:
    # Group by category, calculate avg total time and count entries.
    groped_df = (
        df.groupby(category_column)
        .agg({"totalTime": "mean", "name": "size"})
        .reset_index()
    )
    groped_df.rename(
        columns={"totalTime": "avgTotalTime", "name": "count"}, inplace=True
    )
    groped_df.set_index(category_column, inplace=True)
    # Drop unknown category
    if "Unknown" in groped_df.index:
        groped_df.drop("Unknown", inplace=True)
    return groped_df
