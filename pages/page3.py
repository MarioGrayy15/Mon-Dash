import os
import dash
from dash import html, dcc

dash.register_page(__name__, path="/page3", name="Page 3")

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

with open(os.path.join(BASE_DIR, "expli1.md"), "r", encoding="utf-8") as f:
    md1 = f.read()

with open(os.path.join(BASE_DIR, "expli2.md"), "r", encoding="utf-8") as f:
    md2 = f.read()

with open(os.path.join(BASE_DIR, "expli3.md"), "r", encoding="utf-8") as f:
    md3 = f.read()

layout = html.Div(
    [
        html.Div("PRÉSENTATION DE DASH", className="page3-header"),

        dcc.Tabs(
            id="page3-tabs",
            value="tab-2",
            parent_className="page3-tabs-container",
            className="page3-tabs",
            children=[
                dcc.Tab(
                    label="Accueil",
                    value="tab-1",
                    className="page3-tab",
                    selected_className="page3-tab-selected",
                    children=[
                        html.Div(
                            dcc.Markdown(md3, className="page3-markdown"),
                            className="page3-content"
                        )
                    ],
                ),
                dcc.Tab(
                    label="Layout",
                    value="tab-2",
                    className="page3-tab",
                    selected_className="page3-tab-selected",
                    children=[
                        html.Div(
                            dcc.Markdown(md2, className="page3-markdown"),
                            className="page3-content"
                        )
                    ],
                ),
                dcc.Tab(
                    label="CallBack",
                    value="tab-3",
                    className="page3-tab",
                    selected_className="page3-tab-selected",
                    children=[
                        html.Div(
                            dcc.Markdown(md1, className="page3-markdown"),
                            className="page3-content"
                        )
                    ],
                ),
            ],
        ),
    ],
    className="page3-wrapper",
)