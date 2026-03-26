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
        dbc.Nav(
            [
                dbc.NavLink("Page 1", href="/", active="exact", className="nav-link-custom"),
                dbc.NavLink("Page 2", href="/page2", active="exact", className="nav-link-custom"),
            ],
            pills=True,
            className="mb-4 mt-3"
        ),
        dash.page_container
    ],
    fluid=True
)

server = app.server

if __name__ == "__main__":
    app.run(debug=True)