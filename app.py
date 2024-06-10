import dash
from dash import Dash, html, dcc, Input, Output, callback, State
import dash_bootstrap_components as dbc
from pages.callbacks import allCallbacks


app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
)


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("About", href="/about")),
        dbc.NavItem(dbc.NavLink("Input Field", href="/inputField")),
        dbc.NavItem(dbc.NavLink("Simulation", href="simulation")),
        dbc.NavItem(dbc.NavLink("Logout", href="/logout")),
    ],
    color="primary",
)

# app.layout = html.Div(
#     html.H1('testing')
# )

app.layout = html.Div(
    children=[
        dcc.Store(id="session", storage_type="session"),
        dcc.Location(id="url", refresh=False),
        dcc.Location(id="redirect", refresh=True),
        html.Div(
            children=[
                html.Img(
                    src="asssets/tiger_analytics_img.png", className="company_logo"
                ),
                navbar,
            ],
            className="topNav_container",
        ),
        html.Div(id="page-content"),
    ],
)

@app.callback(
    Output('redirect', 'pathname'),
    Output('incorrectCredentials', 'children'),
    Input('loginUser', 'n_clicks'),
    [State('usernameField', 'value'),
     State('passwordField', 'value')
     ],
    prevent_initial_call=True
)

# for testing now
def checkLogin():
    pass

allCallbacks()

if __name__ == '__main__':
    app.run(debug=True)