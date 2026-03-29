
import pandas as pd

def validate(path):
    df = pd.read_csv(path)
    assert "text" in df.columns
    assert "label" in df.columns
    return df
