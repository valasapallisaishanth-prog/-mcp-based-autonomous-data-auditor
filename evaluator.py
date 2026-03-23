
def compute_precision_recall(predicted, actual):
    tp = 0
    fp = 0
    fn = 0

    for key in actual:
        pred_val = predicted.get(key, 0)
        true_val = actual.get(key, 0)

        if pred_val > 0 and true_val > 0:
            tp += 1
        elif pred_val > 0 and true_val == 0:
            fp += 1
        elif pred_val == 0 and true_val > 0:
            fn += 1

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0

    return precision, recall


def evaluate_audit(mcp_report, ground_truth):
    results = {}

    for category in ground_truth:
        predicted = mcp_report["audit_findings"].get(category, {})
        actual = ground_truth[category]

        precision, recall = compute_precision_recall(predicted, actual)

        results[category] = {
            "precision": round(precision, 2),
            "recall": round(recall, 2)
        }

    return results


def evaluate_tool_calls(tool_calls):
    expected_tools = {
        "read_data",
        "run_missing_value_check",
        "run_negative_value_check",
        "run_invalid_range_check",
        "run_invalid_category_check",
        "run_duplicate_check"
    }

    used_tools = set(tool_calls)

    correct_calls = len(expected_tools.intersection(used_tools))
    false_calls = len(used_tools - expected_tools)

    accuracy = correct_calls / len(expected_tools)

    return {
        "tool_call_accuracy": round(accuracy, 2),
        "false_tool_calls": false_calls
    }
