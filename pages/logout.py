from dash import  html
import dash_bootstrap_components as dbc


logout_layout = html.Div(children=[
    html.Div('You are logged out'),
    dbc.Button(children='Login',href='/login')
])

def logoutLayout():
    return logout_layout