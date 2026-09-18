from pathlib import Path

import pandas as pd


def load_data():
    repo_root = Path(__file__).resolve().parent.parent
    candidates = [
        repo_root / "data" / "data-selected-columns.csv",
        Path.cwd() / "data" / "data-selected-columns.csv",
        Path("../data/data-selected-columns.csv"),
    ]

    for path in candidates:
        if path.exists():
            return pd.read_csv(path)

    raise FileNotFoundError(
        "Could not find data-selected-columns.csv. "
        "Expected it under the project data folder."
    )


df = load_data()

print("First 5 rows:")
print(df.head())
print("\nShape:", df.shape)
print("Columns:", list(df.columns))
print("\nData types:\n", df.dtypes)
print("\nPrice summary:\n", df["price"].describe())
print("\nMissing values:\n", df.isna().sum())
