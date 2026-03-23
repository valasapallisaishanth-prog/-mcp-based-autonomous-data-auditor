import pandas as pd
from src.audit_rules import (
    check_missing_values,
    check_negative_values,
    check_invalid_ranges,
    check_invalid_categories,
    check_duplicates,
)

def read_data(file_path="data/audit_dataset.csv"):
    df = pd.read_csv(file_path)
    return {
        "status": "success",
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "column_names": df.columns.tolist()
    }

def run_missing_value_check(df):
    return {
        "tool_name": "run_missing_value_check",
        "result": check_missing_values(df)
    }

def run_negative_value_check(df):
    return {
        "tool_name": "run_negative_value_check",
        "result": check_negative_values(df)
    }

def run_invalid_range_check(df):
    return {
        "tool_name": "run_invalid_range_check",
        "result": check_invalid_ranges(df)
    }

def run_invalid_category_check(df):
    return {
        "tool_name": "run_invalid_category_check",
        "result": {
            "invalid_category_count": check_invalid_categories(df)
        }
    }

def run_duplicate_check(df):
    return {
        "tool_name": "run_duplicate_check",
        "result": {
            "duplicate_count": check_duplicates(df)
        }
    }
