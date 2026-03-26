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

        # 🔥 TITRE GLOBAL
        html.H2(
            "Dashboard Avocado",
            style={
                "color": "white",
                "textAlign": "center",
                "marginTop": "15px"
            }
        ),

        # 🔥 NAVBAR
        dbc.Nav(
            [
                dbc.NavLink("Page 1", href="/", active="exact", className="nav-link-custom"),
                dbc.NavLink("Page 2", href="/page2", active="exact", className="nav-link-custom"),
                dbc.NavLink("Page 3", href="/page3", active="exact", className="nav-link-custom"),
            ],
            pills=True,
            justified=True,
            className="mb-4 mt-3"
        ),

        dash.page_container

    ],
    fluid=True
)

server = app.server

if __name__ == "__main__":
    app.run(debug=True)