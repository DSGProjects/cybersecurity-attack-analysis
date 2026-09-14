# Cybersecurity Attack Analysis

End-to-end data analysis project using Python and Power BI to explore cybersecurity attack patterns across a dataset of 40,000 records.

---

## Project Objective

Analyze cybersecurity attack patterns (type, time, day of week, severity) to identify when and how attacks occur most frequently, supporting decisions on security monitoring priorities and resource allocation.

This project simulates a real-world scenario for a security team needing to answer: *when are we most exposed, and which type of attack should we watch for first?*

---

## Project Structure

```
Proyecto_cyberseguridad/

├── data/
│   ├── raw/
│   │   └── cybersecurity_attacks.csv      # Raw dataset
│   ├── processed/
│   │   ├── cybersecurity_clean.csv        # Cleaned dataset
│   │   └── cybersecurity_clean.db         # SQLite database (clean)
│   └── cybersecurity.db                   # SQLite database (raw load)
│
├── notebooks/
│   ├── cargar_sqlite.ipynb                # Load raw data into SQLite
│   └── eda.ipynb                          # Exploratory data analysis & cleaning
│
├── script/
│   └── db_script.py                       # ETL pipeline script
│
├── dashboard/
│   └── visualizacion.pbix                 # Power BI dashboard
│
└── README.md
```

---

## Tools & Technologies

- **Python** → Data cleaning, transformation and EDA
- **Pandas / NumPy** → Data manipulation
- **Seaborn / Matplotlib** → Exploratory visualizations
- **SQLAlchemy / SQLite** → Data storage
- **Power BI** → Interactive dashboard

---

## ETL Pipeline

### 1. Extraction
- Loaded raw CSV with 40,000 records and 25+ columns

### 2. Transformation
- Filled null values in: `Malware Indicators`, `Alerts/Warnings`, `Proxy Information`, `Firewall Logs`, `IDS/IPS Alerts`
- Converted `Timestamp` to datetime
- Created new features:
  - `Year`, `Month`, `Day`, `Hour`
  - `DayOfWeekName`, `DayOfWeekNumber`
  - `time_of_day` → dawn / morning / afternoon / night
  - `year_month` → timeline grouping
  - `risk_category` → low / medium / high based on Anomaly Score

### 3. Load
- Exported cleaned data to SQLite database and CSV

---

## Power BI Dashboard

### Page 1 - Overview
![Overview](assets/Overview.png)
- KPIs: % Blocked, % High Severity, Avg Anomaly Score, Total Attacks
- Attack Type Distribution
- Actions Taken by Attack Type
- Attacks by Time of Day
- Monthly Attack Trends
- Attacks by Protocol

### Page 2 - Temporal Analysis
![Temporal Analysis](assets/Temporal%20Analysis.png)
- Hourly Attack Patterns
- Monthly Attacks by Type
- Attacks by Time of Day and Severity
- Peak Hour: 13:00
- Busiest Day: Tuesday

---

## Key Findings

- Attack types (DDoS, Malware, Intrusion) are evenly distributed (~33% each)
  → *Recommendation: no single attack type can be prioritized over the others; defense strategy should cover all three fronts equally.*

- Peak attack hour is **1:00 PM**
  → *Recommendation: reinforce active monitoring and automated alerts during the midday window.*

- **Tuesday** registers the highest number of attacks
  → *Recommendation: investigate whether this correlates with deployments, system changes, or reduced security staffing that day, and adjust monitoring shifts accordingly.*

- Attack volume remained stable from 2020 to mid-2023, with no anomalous spikes
  → *Recommendation: use this stable behavior as a baseline; any future deviation should trigger a priority investigation alert.*

---

## Dataset

- Source: [Kaggle - Cybersecurity Attacks Dataset](https://www.kaggle.com/datasets/laodeikhwanuluzlah/cybersecurity-attacks-dataset)
- Records: 40,000
- Period: 2020 - 2023

> Note: The original dataset did not include derived temporal variables or risk categorization. The `time_of_day`, `year_month`, and `risk_category` columns were engineered as part of the transformation process to enable temporal and severity analysis.

---

## Author

David Fernando Solano Garcia - Data Analyst & Industrial Engineer

[LinkedIn](https://www.linkedin.com/in/david-fernando-solano-garcia-840230348)
