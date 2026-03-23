
from src.audit_rules import *

def run_baseline_audit(df):
    report = {
        "missing_values": check_missing_values(df),
        "negative_values": check_negative_values(df),
        "invalid_ranges": check_invalid_ranges(df),
        "invalid_categories": check_invalid_categories(df),
        "duplicates": check_duplicates(df)
    }
    return report
