# analysis.py
import pandas as pd
import numpy as np

def load_data(filepath):
    """Load data from CSV file."""
    return pd.read_csv(filepath)

def basic_statistics(data):
    """Calculate basic statistics."""
    return data.describe()

if __name__ == "__main__":
    print("Data Science Project - Analysis Module")
