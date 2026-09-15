"""
Dashboard Page 0 — Executive Overview
Member 5 — Executive Dashboard Design
"""

import dash
from dash import html


# ---------------------------------------------------------
# Register page
# ---------------------------------------------------------

dash.register_page(
    __name__,
    path="/",
    name="Executive Overview",
)


# ---------------------------------------------------------
# Reusable KPI card
# ---------------------------------------------------------

def kpi_card(title, value, description):
    return html.Div(
        [
            html.P(
                title,
                style={
                    "margin": "0 0 8px 0",
                    "fontSize": "13px",
                    "fontWeight": "700",
                    "color": "#64748B",
                    "letterSpacing": "0.5px",
                },
            ),

            html.H2(
                value,
                style={
                    "margin": "0",
                    "fontSize": "30px",
                    "fontWeight": "700",
                    "color": "#0F172A",
                },
            ),

            html.P(
                description,
                style={
                    "margin": "8px 0 0 0",
                    "fontSize": "13px",
                    "color": "#64748B",
                },
            ),
        ],
        style={
            "backgroundColor": "#FFFFFF",
            "padding": "22px",
            "borderRadius": "12px",
            "border": "1px solid #E2E8F0",
            "boxShadow": "0 2px 6px rgba(15, 23, 42, 0.06)",
        },
    )


# ---------------------------------------------------------
# Executive Overview Layout
# ---------------------------------------------------------

layout = html.Div(
    [

        # -------------------------------------------------
        # Header
        # -------------------------------------------------

        html.Div(
            [
                html.H1(
                    "Healthcare Operations Intelligence Dashboard",
                    style={
                        "margin": "0",
                        "fontSize": "32px",
                        "fontWeight": "700",
                        "color": "#0F172A",
                    },
                ),

                html.P(
                    "Executive Overview | Decision Support",
                    style={
                        "marginTop": "8px",
                        "marginBottom": "0",
                        "color": "#64748B",
                        "fontSize": "16px",
                    },
                ),
            ],
            style={
                "marginBottom": "28px",
            },
        ),

        # -------------------------------------------------
        # Executive Snapshot
        # -------------------------------------------------

        html.H2(
            "Executive Snapshot",
            style={
                "marginBottom": "16px",
                "color": "#0F172A",
            },
        ),

        html.Div(
            [

                kpi_card(
                    "TOTAL ADMISSIONS",
                    "5,001",
                    "Patient flow volume",
                ),

                kpi_card(
                    "BED UTILIZATION",
                    "Page 4",
                    "Department occupancy analysis",
                ),

                kpi_card(
                    "WORKFORCE",
                    "Page 4",
                    "Staffing efficiency analysis",
                ),

                kpi_card(
                    "CAPACITY GAPS",
                    "Page 5",
                    "Benchmark comparison",
                ),

            ],
            style={
                "display": "grid",
                "gridTemplateColumns": "repeat(4, 1fr)",
                "gap": "18px",
                "marginBottom": "32px",
            },
        ),

        # -------------------------------------------------
        # Operational Overview
        # -------------------------------------------------

        html.Div(
            [

                html.H2(
                    "Operational Overview",
                    style={
                        "marginTop": "0",
                        "color": "#0F172A",
                    },
                ),

                html.P(
                    "This executive view brings together the major healthcare "
                    "operations areas analyzed across the dashboard. "
                    "Management can use the detailed pages to review patient "
                    "flow, discharge and treatment demand, operational "
                    "bottlenecks, workforce utilization, and resource "
                    "capacity gaps.",
                    style={
                        "lineHeight": "1.7",
                        "color": "#475569",
                        "marginBottom": "0",
                    },
                ),

            ],
            style={
                "backgroundColor": "#F8FAFC",
                "padding": "24px",
                "borderRadius": "12px",
                "border": "1px solid #E2E8F0",
                "marginBottom": "28px",
            },
        ),

        # -------------------------------------------------
        # Detailed Operational Views
        # -------------------------------------------------

        html.H2(
            "Detailed Operational Views",
            style={
                "marginBottom": "16px",
                "color": "#0F172A",
            },
        ),

        html.Div(
            [

                html.A(
                    [
                        html.H3(
                            "Patient Flow",
                            style={"marginTop": "0"},
                        ),
                        html.P(
                            "Admissions and department patient load",
                            style={"marginBottom": "0"},
                        ),
                    ],
                    href="/page1",
                    style={
                        "textDecoration": "none",
                        "color": "#0F172A",
                        "backgroundColor": "#FFFFFF",
                        "padding": "20px",
                        "borderRadius": "12px",
                        "border": "1px solid #E2E8F0",
                    },
                ),

                html.A(
                    [
                        html.H3(
                            "Discharge & Treatment",
                            style={"marginTop": "0"},
                        ),
                        html.P(
                            "Discharge flow and treatment demand",
                            style={"marginBottom": "0"},
                        ),
                    ],
                    href="/page2",
                    style={
                        "textDecoration": "none",
                        "color": "#0F172A",
                        "backgroundColor": "#FFFFFF",
                        "padding": "20px",
                        "borderRadius": "12px",
                        "border": "1px solid #E2E8F0",
                    },
                ),

                html.A(
                    [
                        html.H3(
                            "Bottlenecks & Surgery",
                            style={"marginTop": "0"},
                        ),
                        html.P(
                            "Operational bottlenecks and surgery workload",
                            style={"marginBottom": "0"},
                        ),
                    ],
                    href="/page3",
                    style={
                        "textDecoration": "none",
                        "color": "#0F172A",
                        "backgroundColor": "#FFFFFF",
                        "padding": "20px",
                        "borderRadius": "12px",
                        "border": "1px solid #E2E8F0",
                    },
                ),

                html.A(
                    [
                        html.H3(
                            "Bed & Workforce",
                            style={"marginTop": "0"},
                        ),
                        html.P(
                            "Bed utilization and staffing efficiency",
                            style={"marginBottom": "0"},
                        ),
                    ],
                    href="/page4",
                    style={
                        "textDecoration": "none",
                        "color": "#0F172A",
                        "backgroundColor": "#FFFFFF",
                        "padding": "20px",
                        "borderRadius": "12px",
                        "border": "1px solid #E2E8F0",
                    },
                ),

                html.A(
                    [
                        html.H3(
                            "Resources & Benchmarks",
                            style={"marginTop": "0"},
                        ),
                        html.P(
                            "Resource utilization and capacity gaps",
                            style={"marginBottom": "0"},
                        ),
                    ],
                    href="/page5",
                    style={
                        "textDecoration": "none",
                        "color": "#0F172A",
                        "backgroundColor": "#FFFFFF",
                        "padding": "20px",
                        "borderRadius": "12px",
                        "border": "1px solid #E2E8F0",
                    },
                ),

            ],
            style={
                "display": "grid",
                "gridTemplateColumns": "repeat(3, 1fr)",
                "gap": "16px",
            },
        ),

    ],
    style={
        "padding": "32px",
        "fontFamily": "Arial, sans-serif",
        "backgroundColor": "#FFFFFF",
        "minHeight": "100vh",
    },
)