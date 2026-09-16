"""
Dashboard Page 1 — Admission Trends (Nafisa) + Department-wise Patient Load (Tanvi)
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

import dash
from dash import html
from page1_admissions_component import admissions_section

dash.register_page(__name__, path="/page1", name="Page 1: Patient Flow")
layout = html.Div(
    [
        admissions_section,
        html.Hr(),
        html.H3("Department-wise Patient Load"),
        html.Iframe(
            src="/assets/reports/dept_load.html",
            style={"width": "100%", "height": "1400px", "border": "none"},
        ),
    ],
    style={"padding": "24px"},
)
