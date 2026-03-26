import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/page3", name="Page 3")

# Lecture des fichiers markdown
with open("expli1.md", "r", encoding="utf-8") as f:
    md1 = f.read()

with open("expli2.md", "r", encoding="utf-8") as f:
    md2 = f.read()

with open("expli3.md", "r", encoding="utf-8") as f:
    md3 = f.read()

layout = dbc.Container(
    [
        dbc.Card(
            [
                dbc.CardHeader(
                    "Explications (Markdown)",
                    className="card-header-custom"
                ),
                dbc.CardBody(
                    [
                        dcc.Tabs(
                            [
                                dcc.Tab(
                                    label="Explication 1",
                                    children=[dcc.Markdown(md1)],
                                ),
                                dcc.Tab(
                                    label="Explication 2",
                                    children=[dcc.Markdown(md2)],
                                ),
                                dcc.Tab(
                                    label="Explication 3",
                                    children=[dcc.Markdown(md3)],
                                ),
                            ]
                        )
                    ]
                )
            ],
            className="card-custom"
        )
    ],
    fluid=True
)