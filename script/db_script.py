import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# =============================================
# RUTAS
# =============================================
base_dir   = os.path.dirname(os.path.abspath(__file__))
data       = os.path.join(base_dir, "..", "data", "cybersecurity_attacks.csv")
output_csv = os.path.join(base_dir, "..", "output", "cybersecurity_clean.csv")
output_db  = os.path.join(base_dir, "..", "output", "cybersecurity_clean.db")

# =============================================
# EXTRACCION
# =============================================
df = pd.read_csv(data)
print(f"Datos cargados: {df.shape}")

# =============================================
# TRANSFORMACION
# =============================================
# Limpiar nulos
df["Malware Indicators"] = df["Malware Indicators"].fillna("no malware")
df["Alerts/Warnings"]    = df["Alerts/Warnings"].fillna("no alert")
df["Proxy Information"]  = df["Proxy Information"].fillna("no proxy")
df["Firewall Logs"]      = df["Firewall Logs"].fillna("no firewall")
df["IDS/IPS Alerts"]     = df["IDS/IPS Alerts"].fillna("no IDS/IPS alerts")

# Tipo de dato y columnas nuevas
df["Timestamp"]   = pd.to_datetime(df["Timestamp"])
df["Year"]        = df["Timestamp"].dt.year
df["Month"]       = df["Timestamp"].dt.month
df["Hour"]        = df["Timestamp"].dt.hour
df["year_month"]  = df["Timestamp"].dt.to_period("M").astype(str)

df["time_of_day"] = pd.cut(df["Hour"],
    bins=[0, 6, 12, 18, 24],
    labels=["madrugada", "mañana", "tarde", "noche"])

df["risk_category"] = pd.cut(df["Anomaly Scores"],
    bins=[0, 33, 66, 100],
    labels=["bajo", "medio", "alto"])

# =============================================
# CARGA
# =============================================
engine = create_engine(f"sqlite:///{output_db}")
df.to_sql("cybersecurity_attacks", con=engine, if_exists="replace", index=False)
df.to_csv(output_csv, index=False)

print("Script ejecutado correctamente!")

