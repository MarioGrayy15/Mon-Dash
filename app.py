import dash
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)

app.layout = dbc.Container(
    [
        html.Div(
            [
                dbc.NavLink("Page 1", href="/", style={"marginRight": "15px", "color": "white"}),
            ],
            style={"padding": "15px"}
        ),
        dash.page_container
    ],
    fluid=True
)

server = app.server

if __name__ == "__main__":
    app.run(debug=True)