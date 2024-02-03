import pandas as pd
import pytest
from pathlib import Path


@pytest.fixture
def data() -> pd.DataFrame:
    file_path = Path(__file__).parent / "data/sample.csv"
    df = pd.read_csv(file_path, index_col=0)
    # Convert the 'duration' columns to Pandas Timedelta
    df["prepTime"] = pd.to_timedelta(df["prepTime"], errors="coerce")
    df["cookTime"] = pd.to_timedelta(df["cookTime"], errors="coerce")
    return df
