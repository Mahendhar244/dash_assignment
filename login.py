from dash import html
import dash_bootstrap_components as dbc


login_layout = html.Div(children=[
    html.Label('Login', style={'fontSize': 'xx-large'}),
    html.Div(children=[
        html.Div(children=[
            dbc.Label('Username *', className='username'),
            dbc.Input(placeholder='Enter your Username', id='usernameField')
        ], className='loginForm'),
        html.Div(children=[
            dbc.Label('Password *', className='password'),
            dbc.Input(placeholder='Enter your password', id='passwordField')
        ], className='loginForm'),
        html.Button('Login', className='btn btn-primary',
                    id='loginUser', style={'width': '200px'})
    ], style={'display': 'flex', 'flexDirection': 'column', 'rowGap': '1rem', 'alignItems': 'center'}),
    html.Div(id='incorrectCredentials')
], className='loginPage')


def loginLayout():
    return login_layout