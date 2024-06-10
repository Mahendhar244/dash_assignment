import dash
from dash import dcc, html, Input, Output, callback_context
import dash_bootstrap_components as dbc

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app = dash.Dash(external_stylesheets = [dbc.themes.BOOTSTRAP])

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("About", href="/about")),
        dbc.NavItem(dbc.NavLink("Input Field", href="/inputField")),
        dbc.NavItem(dbc.NavLink("Simulation", href="simulation")),
        dbc.NavItem(dbc.NavLink("Logout", href="/logout")),
    ],
    # brand="NavbarSimple",
    # brand_href="#",
    color="primary",
    # dark=True,
)

layout = html.Div(
    children=[
        # dcc.Store(id='session', storage_type='session'),
        # dcc.Location(id='url', refresh=False),
        # dcc.Location(id='redirect', refresh=True),
        dbc.Col([
            html.Div(children=[
            html.Img(src='tiger_analytics.png',
                     className='company_logo',style = {"display":"flex"}),
            navbar,
        ]),
        ]),
        html.Div(id='page-content')
    ], )


# Define the layout
input_layout = html.Div([
    dbc.Row(layout),
    
    html.P("User Input", className="text-primary fw-bold", style={'float': 'left', 'color': 'black' ,'font-style':'bold','margin-top':'10px'}),
    
    html.P("Calculated Output", className="text-primary fw-bold", style={'text-align': 'center', 'color': 'black','margin-top':'10px'}),
    html.Hr(style = {'width':"100%", 'size':"5"}),
    
    
    dbc.Row([
        dbc.Col([
            html.Label("Latitude :*", style={'margin-right': '10px'}),
            dcc.Input(id='latitude', type='number', value='', style={'width': '100%', 'color': 'black'}, placeholder="Latitude Eg: 39.6491"),
        ], md=6, className="mb-3"),
    ],className = "border-start"),
    dbc.Row([
        dbc.Col([
            html.Label("Longitude :*", style={'margin-right': '10px'}),
            dcc.Input(id='longitude', type='number', value='', style={'width': '100%', 'color': 'black'}, placeholder="Longitude Eg: 79.922"),
        ], md=6, className="mb-3"),
    ]),
    dbc.Row([
        dbc.Col([
            html.Label("Data :*", style={'margin-right': '10px'}),
            dcc.Input(id='data', type='text', value='', style={'width': '100%', 'color': 'black'}, placeholder="Enter dataset GDP vs (country or year)"),
        ], md=6, className="mb-3"),
    ]),
    dbc.Row([
        dbc.Col([
            html.Label("Country :*", style={'margin-right': '10px'}),
            dcc.Input(id='country', type='text', value='', style={'width': '100%', 'color': 'black'}, placeholder="Enter a country name"),
        ], md=6, className="mb-3 "),
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Button('Simulate', id='simulate-button', n_clicks=0, color="primary", className="mt-3" ),
        ], md=6),
    ], className = 'align-center'),
])

app.layout = html.Div([
    dcc.Location(id = 'url',refresh = False),
    html.Div(id = 'content')
])

@app.callback(Output('content','children'),
              [Input('url','pathname')],suppress_callback_exceptions=True)

def display_page(pathname):
    if pathname =='/':
        return  layout
    
    elif pathname == '/inputField':
        return input_layout
    
    else:
        return '404 - Page not Found'


if __name__ == "__main__":
    app.run_server(debug=True)