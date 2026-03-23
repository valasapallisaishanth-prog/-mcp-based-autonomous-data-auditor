# MCP-Based Autonomous Data Auditor

##  Overview

This project implements an **autonomous data auditing system** using **MCP-style tool orchestration** to inspect structured datasets, detect data quality issues, and generate explainable audit reports.

Unlike traditional rule-based data validation pipelines, this system simulates an **agentic workflow** where an auditing agent:

- interacts with tools  
- gathers structured evidence  
- performs multi-step reasoning  
- produces actionable insights  

The goal is to demonstrate how **tool-augmented agents** can be used for real-world data quality monitoring in business systems.

---

##  Problem Statement

Data quality issues are common in operational systems and can lead to:

- incorrect business decisions  
- financial losses  
- poor customer experience  

Typical problems include:

- missing values  
- negative or invalid values  
- inconsistent categories  
- out-of-range values  
- duplicate records  

Traditional validation systems:

- rely on static rules  
- lack flexibility  
- do not provide structured reasoning  

This project addresses these limitations using an **agentic + tool-based auditing system**.

---

##  System Architecture

### End-to-End Pipeline

Dataset
→ MCP Tool Layer
→ Autonomous Audit Agent
→ Audit Findings
→ Evaluation Metrics
→ Final Report


---

##  MCP-Style Tool Layer

The system exposes auditing functions as **tools**, simulating an MCP-style interface.

### Tools Implemented

- `read_data` → loads dataset and returns schema summary  
- `run_missing_value_check` → detects null values  
- `run_negative_value_check` → detects invalid negative values  
- `run_invalid_range_check` → detects out-of-range values  
- `run_invalid_category_check` → detects invalid categories  
- `run_duplicate_check` → detects duplicate rows  

---

##  Autonomous Audit Agent

The agent:

- calls tools sequentially  
- gathers structured outputs  
- tracks tool usage  
- consolidates findings into a report  

### Output Includes:

- dataset summary  
- audit findings  
- tool call list  
- total tool calls  

---

##  Evaluation Framework

The system is evaluated using measurable metrics:

### Audit Evaluation

- **Precision** → correctness of detected issues  
- **Recall** → completeness of detected issues  

### Tool Evaluation

- **Tool Call Accuracy** → correct tools used  
- **False Tool Calls** → unnecessary tool usage  

---

##  Sample Results

- Successfully identified all injected data anomalies  
- **Precision:** ~1.00  
- **Recall:** ~1.00  
- **Tool Call Accuracy:** 1.00  
- **False Tool Calls:** 0  

The MCP-based system demonstrates reliable detection of structured data issues with consistent tool usage.

---

##  Streamlit Demo

The interactive interface provides:

- dataset preview  
- baseline vs MCP audit comparison  
- detected issues  
- tool usage visualization  
- evaluation metrics  
- final audit summary  

---

##  Tech Stack

- Python  
- Pandas / NumPy  
- Rule-based validation  
- Streamlit  

---

##  Project Structure
mcp-based-autonomous-data-auditor/
│
├── data/
│ └── audit_dataset.csv
│
├── src/
│ ├── audit_rules.py
│ ├── baseline_auditor.py
│ ├── mcp_tools.py
│ ├── mcp_agent.py
│ └── evaluator.py
│
├── results/
│ ├── mcp_report.json
│ └── evaluation_results.json
│
├── streamlit_app.py
├── requirements.txt
└── README.md


---

##  How to Run

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py


**Key Insights**
Tool-based agents improve transparency and explainability
Structured auditing enables better debugging and validation
Evaluation metrics provide measurable system performance
MCP-style interfaces allow modular and extensible agent design

**Future Improvements**
Integrate LLM-based reasoning for dynamic tool selection
Add anomaly detection models
Support real-time streaming data auditing
Deploy as scalable microservice

**Relevance to Real Systems**

This project reflects real-world data pipelines where:

data validation is critical
automated auditing reduces manual effort
explainability is required for debugging

It demonstrates how Agentic AI + Tool Orchestration can improve data quality workflows.

**Summary**

This project demonstrates how an autonomous agent can use tools to audit datasets, detect issues, and produce structured, explainable reports with measurable performance.







