import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

dash.register_page(__name__, path="/")

df = pd.read_csv("datas/avocado.csv")

regions = df["region"].unique()

layout = dbc.Container([
    
    dbc.Card([
        
        # HEADER
        dbc.CardHeader(
            "Quantités vendues (Total Volume)",
            className="card-header-custom"
        ),

        # BODY
        dbc.CardBody([
            
            dbc.Row([
                
                # 📊 COLONNE GAUCHE
                dbc.Col([
                    dcc.Graph(id="graph-total")
                ], width=6),

                # 📊 COLONNE DROITE
                dbc.Col([
                    
                    html.Div("Sélectionnez une région :", className="badge-custom"),

                    dcc.Dropdown(
                        id="region-dropdown",
                        options=[{"label": r, "value": r} for r in regions],
                        value="Albany",
                        className="select-custom"
                    ),

                    dcc.Graph(id="graph-region")

                ], width=6)

            ])

        ])

    ], className="card-custom")

], fluid=True)