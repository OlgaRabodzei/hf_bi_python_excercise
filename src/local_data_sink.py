from pathlib import Path
import pandas as pd
import csv

FILE_PATH_BASE = Path("results")


def save_data(df: pd.DataFrame, file_name: str) -> None:
    if not FILE_PATH_BASE.exists():
        FILE_PATH_BASE.mkdir()

    file_path = FILE_PATH_BASE / file_name
    df.to_csv(file_path, sep="|", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
