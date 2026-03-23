import pandas as pd
from src.mcp_tools import (
    read_data,
    run_missing_value_check,
    run_negative_value_check,
    run_invalid_range_check,
    run_invalid_category_check,
    run_duplicate_check,
)

class MCPAutonomousDataAuditor:
    def __init__(self, file_path="data/audit_dataset.csv"):
        self.file_path = file_path
        self.tool_calls = []

    def _record_tool_call(self, tool_name):
        self.tool_calls.append(tool_name)

    def run_audit(self):
        df = pd.read_csv(self.file_path)

        summary = read_data(self.file_path)
        self._record_tool_call("read_data")

        missing_report = run_missing_value_check(df)
        self._record_tool_call("run_missing_value_check")

        negative_report = run_negative_value_check(df)
        self._record_tool_call("run_negative_value_check")

        range_report = run_invalid_range_check(df)
        self._record_tool_call("run_invalid_range_check")

        category_report = run_invalid_category_check(df)
        self._record_tool_call("run_invalid_category_check")

        duplicate_report = run_duplicate_check(df)
        self._record_tool_call("run_duplicate_check")

        final_report = {
            "dataset_summary": summary,
            "audit_findings": {
                "missing_values": missing_report["result"],
                "negative_values": negative_report["result"],
                "invalid_ranges": range_report["result"],
                "invalid_categories": category_report["result"],
                "duplicates": duplicate_report["result"]
            },
            "tool_calls": self.tool_calls,
            "tool_call_count": len(self.tool_calls)
        }

        return final_report
