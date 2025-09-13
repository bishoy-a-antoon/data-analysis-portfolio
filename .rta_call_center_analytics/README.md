
## Project Structure
```shell
rta_call_center_analytics/
│
├── data/
│   ├── raw/        # Raw/generated CSV data files
│   ├── processed/  # Cleaned and feature-engineered data files
│   └── scripts/    # Scripts that generate or update data (e.g. data_generation.py)
│
├── notebooks/
│   ├── 01_data_generation.ipynb    # Explore and build data generation logic (shifts, breaks, agents)
│   ├── 02_data_cleaning.ipynb      # Data cleaning and feature engineering
│   ├── 03_eda.ipynb                # Exploratory analysis
│   └── 04_static_report.ipynb      # Full narrative report with visualizations & summary stats
│
├── streamlit_app/
│   ├── app.py              # Streamlit app entrypoint (interactive dashboard)
│   ├── metrics.py          # Key metrics calculation functions
│   ├── data_processing.py  # Data loading, caching, and preprocessing functions
│   ├── visuals.py          # Plotly figures and visualization helpers
│   └── config.py           # Config/constants for the app (e.g. paths, thresholds)
│
├── requirements.txt    # Python dependencies (pandas, plotly, streamlit, etc)
├── README.md           # Project overview, how to run notebooks & app, etc.
└── .gitignore          # Ignore data files, pycache, env, etc
```

## SLAs
### Examples:
- Service level %: Percent of calls answered within X seconds (e.g., 80% within 20 seconds)
- Average speed of answer (ASA): Average wait time before call is answered
- Abandonment rate: % calls dropped or abandoned before answer
- First call resolution rate

### Resources:
- [Erlang C formula](https://en.wikipedia.org/wiki/Erlang_(unit)#Erlang_C_formula)
- [Queueing theory](https://en.wikipedia.org/wiki/Queueing_theory)





Got it ✅
Here’s a **clean Markdown doc** that summarizes everything we’ve discussed about your RTA portfolio project setup, tools, and reasoning. You can drop this into a `README.md` in your project repo.

---

# 📊 RTA Portfolio Project — Documentation & Reasoning

This document outlines the design decisions, workflow, and technical setup for the **Real-Time Analytics (RTA) Portfolio Project**. The goal is to build a project that both **demonstrates analytical skills** and **stands out to recruiters** for junior RTA or BI analyst roles.

---

## 🎯 Project Goals

* Build a realistic **real-time analytics simulation** (calls, agents, shifts, SLAs).
* Show **practical BI/analytics workflow**: data → cleaning → analysis → dashboards → reporting.
* Keep the setup **minimal but professional**, balancing recruiter accessibility and technical credibility.
* Make outputs **shareable** (static reports) and **interactive** (dashboards/notebooks).

---

## 📂 Project Structure

```
rta-portfolio/
│
├── config/                   # Shared imports, constants, settings
│   ├── __init__.py
│   ├── imports.py            # All Python imports
│   └── constants.py          # Business constants (SLA, shift rules, etc.)
│
├── notebooks/                # Jupyter notebooks (analysis, dashboards)
│   ├── 01_data_generation.ipynb
│   ├── 02_analysis.ipynb
│   └── 03_reporting.ipynb
│
├── scripts/                  # Python scripts (reusable logic)
│   └── utils.py
│
├── data/                     # Input/output datasets
│   ├── raw/
│   ├── processed/
│   └── exports/
│
├── reports/                  # Static reports for recruiters/ops
│   └── weekly_dashboard.pdf
│
├── notebook_init.py          # Auto-path setup for notebooks
├── requirements.txt
└── README.md
```

---

## ⚙️ Imports & Constants

Instead of repeating imports and constants across every notebook:

* **Centralize imports**

  ```python
  # config/imports.py
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  import seaborn as sns
  import duckdb
  ```

* **Centralize constants**

  ```python
  # config/constants.py
  SLA_TARGET = 0.8  # 80% calls answered within 20s
  SHIFT_HOURS = 8
  BREAKS = [15, 30, 15]  # minutes
  ```

* **Use a helper init**

  ```python
  # notebook_init.py
  import sys, os
  sys.path.append(os.path.abspath(".."))
  ```

  Then in a notebook:

  ```python
  %run ../notebook_init.py
  from config.imports import *
  from config.constants import *
  ```

✅ Benefits:

* No duplication across notebooks.
* Cleaner, recruiter-friendly notebooks.
* Easier maintenance (one edit updates all).

---

## 📊 Data Storage & Analysis

### Chosen Options:

* **CSV** → Simple, universally readable, good for sharing raw data.

<!-- * **DuckDB** → In-process database, perfect for analytical queries and avoids heavy setup (Postgres). -->

* **Jupyter + Pandas/Seaborn/Matplotlib** → Core data analysis and visualizations.
* **Metabase** → (Optional) if showcasing SQL-based dashboards.
* **Streamlit** → For live interactive apps (optional, recruiter demo).

---

## 📑 Reporting Strategy

* **Interactive (Metabase/Streamlit)**
* **Static (PDF via nbconvert/Quarto)**
---

## 🔄 Workflow Summary

1. **Data Simulation**

   * Generate call arrivals, agent shifts, breaks, emergencies.
   * Store in CSV and DuckDB.

2. **Analysis in Jupyter**

   * Use Pandas for data wrangling.
   * Apply SLA/coverage calculations.
   * Plot KPIs (AHT, ASA, FCR, Occupancy, etc.).

3. **Reporting**

   * Export static dashboards as PDFs.
   * Optionally provide interactive dashboard (Streamlit or Metabase).

4. **Project Organization**

   * Imports and constants centralized.
<!--   * Notebook path setup automated via `notebook_init.py`.
!-->
---

## ✅ Key Design Choices & Why

| Decision                           | Reason                                                               |
| ---------------------------------- | -------------------------------------------------------------------- |
| **CSV + DuckDB**                   | Lightweight, recruiter-friendly, supports SQL + Python seamlessly.   |
| **Static PDF reports**             | Recruiters can view instantly; no setup needed.                      |
| **Metabase (optional)**            | Showcases SQL/BI skills with visual dashboards.                      |
| **Streamlit (optional)**           | Demonstrates Python dashboarding, but not mandatory.                 |
| **Imports/constants in `config/`** | Clean, DRY (don’t repeat yourself), professional.                    |
| **`notebook_init.py`**             | Avoids repeating sys.path hacks in every notebook.                   |
| **Project structure**              | Mirrors real-world analytics repos; easy for recruiters to navigate. |

---

## 🚀 Next Steps

* Build **baseline data simulation** (calls + agents + shifts).
* Implement **KPI calculations** (SLA, ASA, AHT, occupancy).
* Create **weekly dashboard notebook** → export PDF.
* Add optional **interactive dashboard** (Streamlit or Metabase).
* Polish repo with `README.md`, requirements, and sample outputs.


Metrics:
- Call Volume → total calls per interval/day/week.
- Arrival Rate → calls per minute/hour.
- Service Level (SL) → % of calls answered within SLA wait time.
- Average Wait Time (AWT) → mean time customers spend waiting.
- Max Wait Time → longest wait experienced.
- Queue Length → how many customers are waiting per interval.
- Abandonment Rate → % of calls dropped before answer.
- Re-Queue Rate → % of calls transferred between queues.

👩‍💻 Agent Performance Metrics
- Average Handle Time (AHT) → talk + wrap-up.
- Occupancy → % of agent time spent on calls vs idle.
- Utilization → calls handled vs capacity.
- First Call Resolution (FCR) → % resolved on first attempt.
- Agent Transfers → number of transfers per agent.
- Calls per Agent → workload distribution.
- Adherence → time agents stick to scheduled shifts.

😊 Customer Experience Metrics
- Customer Satisfaction (CSAT) → post-call ratings (1–5).
- Net Promoter Score (NPS) (if you simulate it).
- Sentiment Analysis → positive/neutral/negative tone of call.
- Resolution Rate → % of calls resolved successfully.
- Repeat Calls → same customer calling multiple times in period.

💰 Business/Strategic Metrics
- Call Distribution by Queue → e.g., tech vs billing vs sales.
- Trend Analysis → by day, week, peak vs off-peak.

Main Metrics:

- Call Volume
- Service Level
- Average Wait Time
- Abandonment Rate
- Average Handle Time
- FCR
- CSAT
- Sentiment


| Column      | Example Value | Notes                          |
|-------------+---------------+--------------------------------|
| id          | a83bcd19c45a1 | unique per call                |
| customer    | 1209432       | repeat callers                 |
| queue       | support       | support/billing/sales          |
| agent       | 105543        | null if abandoned              |
| channel     | voice         | voice/chat/email               |
| call_type   | inbound       | mostly inbound                 |
| outcome     | answered      | answered/abandoned/transferred |
| date        | 2025-08-03    | YYYY-MM-DD                     |
| time        | 09:32:00      | hh:mm:ss                       |
| day_of_week | Sunday        | useful for pivot               |
| hour_of_day | 9             | useful for charts              |
| interval    | 20            | 30-min bucket                  |
| wait_t      | 22            | seconds                        |
| abandoned   | False         | boolean                        |
| handle_t    | 240           | seconds                        |
| resolved    | True          | boolean                        |
| fcr         | True          | boolean                        |
| sentiment   | neutral       | positive/neutral/negative      |
| csat        | 4             | Likert 1–5                     |
| sla_target  | 30            | SLA threshold                  |
| sla_met     | True          | wait ≤ sla_target              |
| queue_len   | 3             | simulated backlog              |
