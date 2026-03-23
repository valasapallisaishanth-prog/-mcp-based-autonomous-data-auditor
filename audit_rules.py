
def check_missing_values(df):
    return df.isnull().sum().to_dict()

def check_negative_values(df):
    issues = {}
    for col in ["price", "quantity", "delivery_days"]:
        issues[col] = int((df[col] < 0).sum())
    return issues

def check_invalid_ranges(df):
    issues = {}
    issues["customer_rating_invalid"] = int(((df["customer_rating"] < 1) | (df["customer_rating"] > 5)).sum())
    return issues

def check_invalid_categories(df):
    valid = ["electronics", "clothing", "home"]
    return int((~df["category"].isin(valid)).sum())

def check_duplicates(df):
    return int(df.duplicated().sum())
