import dash
from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

dash.register_page(__name__, path="/page2", name="Page 2")

df = pd.read_csv("datas/avocado.csv")

regions = sorted(df["region"].dropna().unique())
types_avocat = sorted(df["type"].dropna().unique())

COLUMNS_TO_HIDE = [
    "Unnamed: 0",
    "4046",
    "4225",
    "4770",
    "Small Bags",
    "Large Bags",
    "XLarge Bags",
]

table_df = df.drop(columns=[col for col in COLUMNS_TO_HIDE if col in df.columns]).copy()

layout = dbc.Container(
    [
        dbc.Card(
            [
                dbc.CardHeader(
                    "Données du jeu de données",
                    className="card-header-custom"
                ),
                dbc.CardBody(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Div("Région", className="badge-custom"),
                                        dcc.Dropdown(
                                            id="page2-region-dropdown",
                                            options=[{"label": r, "value": r} for r in regions],
                                            value=regions[0] if regions else None,
                                            clearable=False,
                                        ),
                                    ],
                                    xs=12, md=6,
                                    className="mb-3"
                                ),
                                dbc.Col(
                                    [
                                        html.Div("Type d'avocat", className="badge-custom"),
                                        dcc.Checklist(
                                            id="page2-type-checklist",
                                            options=[
                                                {"label": " Tous", "value": "ALL"},
                                                *[
                                                    {"label": f" {t}", "value": t}
                                                    for t in types_avocat
                                                ]
                                            ],
                                            value=["ALL"],
                                            inline=True,
                                            inputStyle={"marginRight": "6px", "marginLeft": "10px"},
                                            labelStyle={"color": "white", "marginRight": "12px"},
                                        ),
                                    ],
                                    xs=12, md=6,
                                    className="mb-3"
                                ),
                            ]
                        ),

                        html.Div(
                            id="page2-badge-count",
                            className="badge-custom mb-3"
                        ),

                        dash_table.DataTable(
                            id="page2-table",
                            columns=[{"name": col, "id": col} for col in table_df.columns],
                            data=table_df.to_dict("records"),
                            sort_action="native",
                            page_size=12,
                            style_table={"overflowX": "auto"},
                            style_header={
                                "backgroundColor": "#2c8ed6",
                                "color": "white",
                                "fontWeight": "bold",
                                "textAlign": "center",
                                "border": "1px solid #444",
                            },
                            style_cell={
                                "backgroundColor": "rgba(20,20,20,0.95)",
                                "color": "white",
                                "textAlign": "center",
                                "padding": "10px",
                                "border": "1px solid #444",
                                "minWidth": "120px",
                                "width": "120px",
                                "maxWidth": "180px",
                                "whiteSpace": "normal",
                            },
                            style_data={
                                "backgroundColor": "rgba(30,30,30,0.95)",
                                "color": "white",
                            },
                        ),
                    ]
                )
            ],
            className="card-custom"
        )
    ],
    fluid=True
)