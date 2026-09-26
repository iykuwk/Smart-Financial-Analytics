# Smart Financial Planning Analytics

Enterprise **Financial Planning & Analysis (FP&A)** solution built using **Power BI**, **Python**, **Excel**, **Power Query**, and **DAX**.

This project simulates a multinational organization's budgeting and financial planning process by generating realistic financial transactions and transforming them into interactive executive dashboards.

---

## Project Highlights

- Executive Financial Dashboard
- Budget vs Actual Analysis
- Financial Forecasting
- Variance Analysis
- Budget Utilization Monitoring
- Department Performance Analysis
- General Ledger Account Analysis
- Transaction Explorer
- Automated Python Data Generator
- Star Schema Data Model
- Interactive Power BI Reports

---

# Business Problem

Finance teams often rely on multiple spreadsheets and manual reporting processes to prepare monthly management reports.

Common challenges include:

- Budget overruns identified too late
- Slow month-end reporting
- Limited visibility into departmental spending
- Poor forecast monitoring
- Difficult variance investigations
- Manual consolidation of financial information
- Limited executive self-service reporting

These challenges delay decision-making and reduce the finance team's ability to provide timely business insights.

---

# Project Objectives

This project was developed to demonstrate how Power BI can modernize Financial Planning & Analysis by:

- Automating financial data preparation
- Monitoring Budget vs Actual performance
- Measuring Forecast Accuracy
- Analysing Budget Utilization
- Investigating Financial Variances
- Monitoring Department Performance
- Tracking General Ledger spending
- Providing executive-level financial reporting
- Enabling transaction-level analysis

---

# Solution Architecture

```

Python

↓

Synthetic Financial Dataset

↓

Excel

↓

Power Query

↓

Star Schema

↓

DAX Measures

↓

Interactive Power BI Dashboard

```

---

# Technology Stack

| Technology | Purpose |
|------------|---------|
| Power BI | Dashboard Development |
| Power Query | Data Transformation |
| DAX | Financial Calculations |
| Python | Automated Data Generation |
| Pandas | Data Processing |
| NumPy | Financial Simulation |
| Excel | Data Storage |
| GitHub | Version Control |
| Markdown | Documentation |

---

# Dataset Overview

The project contains approximately **5,000 financial transactions** covering:

| Metric | Value |
|--------|------:|
| Reporting Period | Jan 2025 – Dec 2026 |
| Transactions | 5,000 |
| Business Entities | 5 |
| Departments | 10 |
| Cost Centres | 10 |
| GL Accounts | 14 |
| Financial Scenarios | Budget, Actual, Forecast |

---

# Repository Structure

```text
Smart-Financial-Planning-Analytics
│
├── dashboard/
│   └── Smart Financial Planning Analytics.pbix
│
├── data/
│   ├── financial_transactions.xlsx
│   ├── entities.xlsx
│   ├── departments.xlsx
│   ├── cost_centers.xlsx
│   └── gl_accounts.xlsx
│
├── docs/
│   └── CASE_STUDY.md
│
├── python/
│   ├── config.py
│   ├── generate_lookup_tables.py
│   ├── generate_financial_data.py
│   └── requirements.txt
│
├── screenshots/
│   ├── 01_Executive Financial Overview.png
│   ├── 02_Budget Performance.png
│   ├── 03_Department Analysis.png
│   ├── 04_GL Account Analysis.png
│   ├── 05_Forecast & Variance Analysis.png
│   └── 06_Transaction Explorer.png
│
└── README.md
```

---

# Data Model

The solution follows a **Star Schema** to improve performance and simplify reporting.

### Fact Table

- Financial Transactions

### Dimension Tables

- Calendar
- Entities
- Departments
- Cost Centres
- GL Accounts

This dimensional model enables efficient filtering, reusable DAX measures, and scalable report development.

---

# Key Performance Indicators (KPIs)

The executive dashboard includes the following KPIs:

- Total Budget
- Total Actual
- Total Forecast
- Total Variance
- Variance %
- Budget Utilization %
- Forecast Accuracy %
- Number of Transactions
- Number of Departments
- Number of Business Entities
- Number of GL Accounts

These KPIs provide management with a concise summary of financial performance before drilling into detailed analysis.

---

# Dashboard Pages

## 1. Executive Financial Overview

![Executive Financial Overview](screenshots/01_Executive%20Financial%20Overview.png)

Executive summary page showing:

- Executive KPIs
- Budget vs Actual vs Forecast
- Monthly Variance Trend
- Department Spending
- Entity Performance
- GL Account Allocation
- Scenario Distribution

---

## 2. Budget Performance

![Budget Performance](screenshots/02_Budget%20Performance.png)

Focused on monitoring budget execution across the organisation through:

- Monthly Budget vs Actual
- Department Variance
- Budget Utilization
- Entity Performance
- Budget Detail Table

---

## 3. Department Analysis

![Department Analysis](screenshots/03_Department%20Analysis.png)

Provides detailed departmental financial analysis including:

- Department Budget Trends
- Budget Utilization %
- GL Account Spending
- Department Variance
- Department Detail Table

---

## 4. GL Account Analysis

![GL Account Analysis](screenshots/04_GL%20Account%20Analysis.png)

Analyse expenditure across General Ledger accounts through:

- Actual Spend by GL Account
- Budget vs Actual Comparison
- Variance by GL Account
- Monthly GL Trends
- Detailed GL Account Table

Business Value:

Helps finance teams understand spending patterns by expense category and identify accounts contributing most to overall expenditure.

---

## 5. Forecast & Variance Analysis

![Forecast & Variance Analysis](screenshots/05_Forecast%20%26%20Variance%20Analysis.png)

Provides visibility into forecasting performance using:

- Forecast Accuracy Trend
- Monthly Variance Trend
- Variance by Entity
- Department Variance Waterfall
- Forecast vs Actual Analysis
- Variance Detail Table

Business Value:

Improves financial planning by identifying forecasting gaps, monitoring budget performance, and highlighting areas requiring management attention.

---

## 6. Transaction Explorer

![Transaction Explorer](screenshots/06_Transaction%20Explorer.png)

Interactive page designed for detailed financial investigation.

Features include:

- Monthly Transaction Volume
- Largest Financial Transactions
- Transaction Detail Table
- Interactive slicers
- Drill-down analysis

Business Value:

Allows finance analysts to move from executive summaries to transaction-level detail for reconciliation, audit support, and financial investigations.

---

# Python Automation

The project includes automated Python scripts that generate realistic FP&A datasets.

### Included Scripts

```text
config.py

generate_lookup_tables.py

generate_financial_data.py
```

The generator automatically creates:

- Financial transactions
- Budget values
- Actual values
- Forecast values
- Variance calculations
- Variance %
- Lookup tables
- Financial scenarios

This allows the project to be regenerated with new synthetic data whenever required.

---

# Business Value

This solution demonstrates practical Financial Planning & Analysis capabilities including:

- Budget Planning
- Forecasting
- Variance Analysis
- Budget Monitoring
- Department Performance Reporting
- General Ledger Analysis
- Executive Dashboard Reporting
- Financial Data Automation
- Interactive Business Intelligence

---

# How to Run

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Smart-Financial-Planning-Analytics.git
```

---

## 2. Install Python Dependencies

```bash
pip install -r python/requirements.txt
```

---

## 3. Generate Lookup Tables

```bash
python python/generate_lookup_tables.py
```

---

## 4. Generate Financial Dataset

```bash
python python/generate_financial_data.py
```

This will automatically generate:

- Financial Transactions
- Business Entities
- Departments
- Cost Centres
- General Ledger Accounts

inside the **data** folder.

---

## 5. Open the Dashboard

Open:

```text
dashboard/Smart Financial Planning Analytics.pbix
```

Refresh the data model if required.

---

# Documentation

A detailed implementation walkthrough is available in:

```text
docs/CASE_STUDY.md
```

The case study includes:

- Business Problem
- Solution Architecture
- Dataset Design
- Data Model
- Dashboard Development
- Business Insights
- Challenges
- Lessons Learned
- Future Improvements

---

# Future Enhancements

Future versions of this project may include:

- Rolling Forecasts
- Profit & Loss Dashboard
- Balance Sheet Dashboard
- Cash Flow Forecasting
- Scenario Planning
- AI-assisted Forecasting
- Power BI Service Deployment
- Scheduled Refresh
- Row-Level Security (RLS)
- Live Currency Exchange Rates

---

# Portfolio Roadmap

This project forms part of a complete Finance Analytics Portfolio.

## Completed Projects

- ✅ Smart Accounts Payable Analytics
- ✅ Smart Procurement Analytics
- ✅ Smart Financial Planning Analytics (FP&A)

## Upcoming Projects

- Smart Accounts Receivable Analytics
- Treasury Analytics
- Cash Flow Analytics
- Payroll Analytics
- Fixed Assets Analytics
- Financial Statement Analytics
- Audit Analytics
- Executive Finance Dashboard

---

# Author

## Peter Njoroge

Finance Analytics | Power BI | Python | SQL | Excel | DAX

Building end-to-end analytics solutions that transform finance data into actionable business insights.

---

If you found this project useful, consider giving it a ⭐ on GitHub.
