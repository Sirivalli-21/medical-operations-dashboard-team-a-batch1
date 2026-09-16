import os
import dash
from dash import html
import pandas as pd

dash.register_page(
    __name__,
    path="/page8",
    name="Data Integration",
    order=8,
)

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "milestone3", "data", "processed")

DATASETS = [
    ("Admissions", "admissions_clean.csv"),
    ("Departments", "departments_clean.csv"),
    ("Doctors", "doctors_preprocessed.csv"),
    ("Patients", "patients_clean.csv"),
    ("Billing", "billing_clean.csv"),
    ("Lab Results", "lab_results_clean.csv"),
    ("Surgeries", "surgeries_clean_fixed.csv"),
]

def format_number(value):
    if value is None or pd.isna(value):
        return "0"
    return f"{int(float(value)):,}"

def load_stats():
    rows = []
    total_rows = 0
    total_nulls = 0
    total_dupes = 0

    for label, filename in DATASETS:
        path = os.path.join(DATA_DIR, filename)
        if not os.path.exists(path):
            rows.append({
                "label": label, "filename": filename,
                "row_count": "Missing", "null_count": "-", "dupe_count": "-",
            })
            continue

        df = pd.read_csv(path)
        row_count = int(len(df))
        null_count = int(df.isnull().sum().sum())
        dupe_count = int(df.duplicated().sum())

        total_rows += row_count
        total_nulls += null_count
        total_dupes += dupe_count

        rows.append({
            "label": label, "filename": filename,
            "row_count": format_number(row_count),
            "null_count": format_number(null_count),
            "dupe_count": format_number(dupe_count),
        })

    return rows, total_rows, total_nulls, total_dupes

ROWS, TOTAL_ROWS, TOTAL_NULLS, TOTAL_DUPES = load_stats()

def dataset_row(row):
    return html.Tr([
        html.Td(row["label"], style={"padding": "12px", "color": "#0F172A", "fontWeight": "600"}),
        html.Td(row["filename"], style={"padding": "12px", "color": "#64748B", "fontFamily": "monospace", "fontSize": "13px"}),
        html.Td(row["row_count"], style={"padding": "12px", "color": "#0F172A"}),
        html.Td(str(row["null_count"]), style={"padding": "12px", "color": "#0F172A"}),
        html.Td(str(row["dupe_count"]), style={"padding": "12px", "color": "#0F172A"}),
    ], style={"borderBottom": "1px solid #E2E8F0"})

layout = html.Div([
    html.H1("Data Integration Overview", style={
        "fontSize": "26px", "fontWeight": "700", "color": "#0F172A", "marginBottom": "6px",
    }),
    html.P("Consolidated view of cleaned datasets from Milestone 1 preprocessing.", style={
        "fontSize": "14px", "color": "#64748B", "marginBottom": "24px",
    }),

    html.Div([
        kpi_card("DATASETS INTEGRATED", str(len(DATASETS)), "Cleaned CSVs from Milestone 1", icon="fa-database", color="#3B82F6"),
        kpi_card("TOTAL RECORDS", format_number(TOTAL_ROWS), "Combined rows across all datasets", icon="fa-table", color="#0F172A"),
        kpi_card("NULL VALUES FOUND", format_number(TOTAL_NULLS), "Post-cleaning validation check", icon="fa-triangle-exclamation", color="#F59E0B"),
        kpi_card("DUPLICATE ROWS FOUND", format_number(TOTAL_DUPES), "Post-cleaning validation check", icon="fa-clone", color="#EF4444"),
    ], style={
        "display": "grid", "gridTemplateColumns": "repeat(4, 1fr)", "gap": "16px",
        "marginBottom": "28px",
    }),
])