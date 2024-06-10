import dash 
from dash import dash_table
import pandas as pd
import json as json

import dash_bootstrap_components as dbc
from dash import Dash, html, dcc
from dash.dependencies import Input,Output,State
import dash_lazy_load

# dash.register_page(__name__,path = "/About")



with open('config.json','r') as file:
    tables = json.load(file)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")
df = df[['continent','country','pop','lifeExp']]

LAYOUT_STYLE = {
    "padding":"1rem 1rem",
    "background-color":"rgb(29,25,250)",
    "border-style":"outset",
    "fontsize":"100%"

}


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


about_layout = html.Div(
    [
        dbc.Row([layout]),
        dbc.Row([html.H2(["Introduction to GapMinder"])],style={"text-align":"center"}),
        dbc.Row(
            dash_lazy_load.LazyLoad([html.P([tables["intro_part_1"]])],debounce = 1000)
        ),
        dbc.Row(
            [
                html.Ol(
                [
                    html.Li([tables["intro_list1"]]),
                    html.Li([tables["intro_list2"]]),
                    html.Li([tables["intro_list3"]]),
                    html.Li([tables["intro_list4"]])
                ],style = {"padding-left":"50px"}
                )
            ]
        ),

        dbc.Label("show number of rows"),
    row_drop := dcc.Dropdown(value = 10,clearable = False,style = {'width':'35%'},
                             options = [10,25,50,100]),

    my_table := dash_table.DataTable(
        columns = [
            {'name':'Continent', 'id':'continent','type':'numeric'},
            {'name':'Country','id':'country','type':'text'},
            {'name':'Population','id':'pop','type':'numeric'},
            {'name':'Life Expectancy','id':'lifeExp','type':'numeric'}
        ],
        data = df.to_dict('records'),
        filter_action = 'native',
        page_size = 10,

        style_data = {
            'width':'150px','minWidth':'150px','maxWidth':'150px',
            'overflow':'hidden',
            'textOverflow': 'ellipsis'
        }
    ),

    dbc.Row([
        dbc.Col([
            continent_drop := dcc.Dropdown([x for x in sorted(df.continent.unique())])
        ],width = 3),
        dbc.Col([
            country_drop := dcc.Dropdown([x for x in sorted(df.country.unique())],multi = True)
        ],width = 3),
        dbc.Col([
            pop_slider := dcc.Slider(0,1500000000,5000000 ,marks = {'100000000':'1 billion', '150000000':'1.5 billion'},
                                     value = 0,tooltip = {"placement":"bottom","always_visible":True})
        ],width = 3),
        dbc.Col([
            lifeExp_slider := dcc.Slider(0,100,1 ,marks = {'100':'100'},
                                     value = 0,tooltip = {"placement":"bottom","always_visible":True})
        ],width = 3),
        
    ],justify = "between"),

    ]
)

@app.callback(
    Output(my_table,'data'),
    Output(my_table,'page_size'),
    Input(continent_drop,'value'),
    Input(country_drop,'value'),
    Input(pop_slider,'value'),
    Input(lifeExp_slider,'value'),
    Input(row_drop,'value'),
suppress_callback_exceptions=True)
def update_dropdown_options(cont_v,country_v,pop_v,life_v,row_v):
    dff = df.copy()

    if cont_v:
        dff = dff[dff.continent == cont_v]
    if country_v:
        dff = dff[dff.country.isin(country_v)]
    
    dff = dff[(dff['pop'] >= pop_v) & (dff['pop'] < 150000000)]
    dff = dff[(dff['lifeExp'] >= life_v) & (dff['lifeExp'] < 100)]

    return dff.to_dict('records'), row_v


app.layout = html.Div([
    dcc.Location(id = 'url',refresh = False),
    html.Div(id = 'content')
])

@app.callback(Output('content','children'),
              [Input('url','pathname')],suppress_callback_exceptions=True)

def display_page(pathname):
    if pathname =='/':
        return  about_layout
    elif pathname == '/about':
        return about_layout
    else:
        return '404 - Page not Found'


if __name__ == "__main__":
    app.run_server(debug=True)