import streamlit as st
import pandas as pd
import json
import sys
import os

sys.path.append("/content")

from src.baseline_auditor import run_baseline_audit
from src.mcp_agent import MCPAutonomousDataAuditor
from src.evaluator import evaluate_audit, evaluate_tool_calls


st.set_page_config(page_title="MCP-Based Autonomous Data Auditor", layout="wide")


GROUND_TRUTH = {
    "missing_values": {
        "quantity": 1
    },
    "negative_values": {
        "price": 1,
        "delivery_days": 1
    },
    "invalid_ranges": {
        "customer_rating_invalid": 1
    },
    "invalid_categories": {
        "invalid_category_count": 1
    },
    "duplicates": {
        "duplicate_count": 1
    }
}


@st.cache_data
def load_data():
    return pd.read_csv("data/audit_dataset.csv")


@st.cache_resource
def run_mcp_audit():
    auditor = MCPAutonomousDataAuditor(file_path="data/audit_dataset.csv")
    return auditor.run_audit()


df = load_data()
mcp_report = run_mcp_audit()
baseline_report = run_baseline_audit(df)
audit_eval = evaluate_audit(mcp_report, GROUND_TRUTH)
tool_eval = evaluate_tool_calls(mcp_report["tool_calls"])

st.title("MCP-Based Autonomous Data Auditor")
st.markdown(
    "Autonomous data auditing system using **MCP-style tool orchestration** to inspect datasets, detect issues, and generate structured audit reports."
)

st.subheader("Dataset Preview")
st.dataframe(df.head(10), use_container_width=True)

st.subheader("Dataset Summary")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Rows", mcp_report["dataset_summary"]["rows"])
with col2:
    st.metric("Columns", mcp_report["dataset_summary"]["columns"])
with col3:
    st.metric("Tool Calls", mcp_report["tool_call_count"])

st.markdown("---")

st.subheader("Baseline Audit Report (Without MCP)")
st.json(baseline_report)

st.subheader("MCP Audit Findings")
st.json(mcp_report["audit_findings"])

st.subheader("Tool Calls Used")
st.write(mcp_report["tool_calls"])

st.markdown("---")

st.subheader("Evaluation Metrics")

metric_rows = []
for category, metrics in audit_eval.items():
    metric_rows.append({
        "category": category,
        "precision": metrics["precision"],
        "recall": metrics["recall"]
    })

metric_df = pd.DataFrame(metric_rows)
st.dataframe(metric_df, use_container_width=True)

col4, col5 = st.columns(2)
with col4:
    st.metric("Tool Call Accuracy", tool_eval["tool_call_accuracy"])
with col5:
    st.metric("False Tool Calls", tool_eval["false_tool_calls"])

st.markdown("---")

st.subheader("Final Audit Summary")

summary_points = [
    f"Missing value issues detected: {mcp_report['audit_findings']['missing_values']}",
    f"Negative value issues detected: {mcp_report['audit_findings']['negative_values']}",
    f"Invalid range issues detected: {mcp_report['audit_findings']['invalid_ranges']}",
    f"Invalid category issues detected: {mcp_report['audit_findings']['invalid_categories']}",
    f"Duplicate issues detected: {mcp_report['audit_findings']['duplicates']}",
]

for point in summary_points:
    st.write("-", point)

st.markdown("---")

st.subheader("Why This Project Matters")
st.write(
    """
    This project demonstrates how an autonomous agent can use tools through an MCP-style interface
    to inspect structured business data, detect quality issues, and generate explainable audit reports.
    It highlights tool usage, structured reasoning, and measurable evaluation.
    """
)
