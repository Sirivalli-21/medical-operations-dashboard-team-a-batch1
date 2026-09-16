"""
Dashboard Page 6 - Data Integration Overview
Member 6 - Module 1 Integration
"""

import os
import dash
from dash import html
import pandas as pd

dash.register_page(
    __name__,
    path="/page8",
    name="Data Integration",
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
        row_count = len(df)
        null_count = int(df.isnull().sum().sum())
        dupe_count = int(df.duplicated().sum())

        total_rows += row_count
        total_nulls += null_count
        total_dupes += dupe_count

        rows.append({
            "label": label, "filename": filename,
            "row_count": f"{row_count:,}",
            "null_count": null_count,
            "dupe_count": dupe_count,
        })

    return rows, total_rows, total_nulls, total_dupes


ROWS, TOTAL_ROWS, TOTAL_NULLS, TOTAL_DUPES = load_stats()


# ---------------------------------------------------------
# Reusable KPI card (same style as page0)
# ---------------------------------------------------------

def kpi_card(title, value, description):
    return html.Div(
        [
            html.P(title, style={
                "margin": "0 0 8px 0", "fontSize": "13px", "fontWeight": "700",
                "color": "#64748B", "letterSpacing": "0.5px",
            }),
            html.H2(value, style={
                "margin": "0", "fontSize": "30px", "fontWeight": "700", "color": "#0F172A",
            }),
            html.P(description, style={
                "margin": "8px 0 0 0", "fontSize": "13px", "color": "#64748B",
            }),
        ],
        style={
            "backgroundColor": "#FFFFFF", "padding": "22px", "borderRadius": "12px",
            "border": "1px solid #E2E8F0", "boxShadow": "0 2px 6px rgba(15, 23, 42, 0.06)",
        },
    )


# ---------------------------------------------------------
# Dataset table row
# ---------------------------------------------------------

def dataset_row(row):
    return html.Tr([
        html.Td(row["label"], style={"padding": "12px", "color": "#0F172A", "fontWeight": "600"}),
        html.Td(row["filename"], style={"padding": "12px", "color": "#64748B", "fontFamily": "monospace", "fontSize": "13px"}),
        html.Td(row["row_count"], style={"padding": "12px", "color": "#0F172A"}),
        html.Td(str(row["null_count"]), style={"padding": "12px", "color": "#0F172A"}),
        html.Td(str(row["dupe_count"]), style={"padding": "12px", "color": "#0F172A"}),
    ], style={"borderBottom": "1px solid #E2E8F0"})


# ---------------------------------------------------------
# Page layout
# ---------------------------------------------------------

layout = html.Div([
    html.H1("Data Integration Overview", style={
        "fontSize": "26px", "fontWeight": "700", "color": "#0F172A", "marginBottom": "6px",
    }),
    html.P("Consolidated view of cleaned datasets from Milestone 1 preprocessing.", style={
        "fontSize": "14px", "color": "#64748B", "marginBottom": "24px",
    }),

    html.Div([
        kpi_card("TOTAL DATASETS", str(len(DATASETS)), "Cleaned CSV files integrated"),
        kpi_card("TOTAL ROWS", f"{TOTAL_ROWS:,}", "Across all datasets"),
        kpi_card("TOTAL NULLS", f"{TOTAL_NULLS:,}", "Remaining null values"),
        kpi_card("TOTAL DUPLICATES", f"{TOTAL_DUPES:,}", "Remaining duplicate rows"),
    ], style={
        "display": "grid", "gridTemplateColumns": "repeat(4, 1fr)", "gap": "16px",
        "marginBottom": "28px",
    }),

    html.Div([
        html.H3("Dataset Summary", style={
            "fontSize": "16px", "fontWeight": "700", "color": "#0F172A", "marginBottom": "14px",
        }),
        html.Table([
            html.Thead(html.Tr([
                html.Th("Dataset", style={"padding": "12px", "textAlign": "left", "color": "#64748B", "fontSize": "13px"}),
                html.Th("File", style={"padding": "12px", "textAlign": "left", "color": "#64748B", "fontSize": "13px"}),
                html.Th("Rows", style={"padding": "12px", "textAlign": "left", "color": "#64748B", "fontSize": "13px"}),
                html.Th("Nulls", style={"padding": "12px", "textAlign": "left", "color": "#64748B", "fontSize": "13px"}),
                html.Th("Duplicates", style={"padding": "12px", "textAlign": "left", "color": "#64748B", "fontSize": "13px"}),
            ])),
            html.Tbody([dataset_row(row) for row in ROWS]),
        ], style={
            "width": "100%", "borderCollapse": "collapse",
        }),
    ], style={
        "backgroundColor": "#FFFFFF", "padding": "22px", "borderRadius": "12px",
        "border": "1px solid #E2E8F0",
    }),
])
