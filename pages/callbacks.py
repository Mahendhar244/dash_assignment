from dash import dcc, Input, Output, callback, State, no_update,html
import dash
import plotly.express as px
import json
from dash.exceptions import PreventUpdate
from pages.About_page import getUpdatedDataFrame
import dash_leaflet as dl
from pages.About_page import dataFrame
from pages.About_page import aboutlogout
from pages.dash_input import inputLayout
from pages.simulation import simulationLayout
# from flask_login import current_user, logout_user


def updatePageSize():
    @callback(
        Output('table', 'page_size'),
        Input('page_dropdown', 'value')
    )
    def update_output(value):
        return value


def updateTableData():
    @callback(
        Output('table', 'data'),
        Input('continent_dropdown', 'value'),
        Input('country_dropdown', 'value'),
        Input('population_slider', 'value'),
        Input('lifeExp_slider', 'value')
    )
    def update_output(continent, country, popValue, lifeExpValue):
        return getUpdatedDataFrame(continent, country, popValue, lifeExpValue).to_dict('records')


def generateCSV():
    @callback(
        Output("download", "data"),
        [Input("download_CSV", "n_clicks")],
        [State('continent_dropdown', 'value'),
         State('country_dropdown', 'value'),
         State('population_slider', 'value'),
         State('lifeExp_slider', 'value'),
         ],
        prevent_initial_call=True,)
    def generate_csv(n_nlicks, continent, country, popValue, lifeExpValue):
        dataFrame = getUpdatedDataFrame(
            continent, country, popValue, lifeExpValue)
        return dcc.send_data_frame(dataFrame.to_csv, filename="filtered_data.csv")


def storeInSession():
    @callback(
        Output('session', 'data', allow_duplicate=True),
        Output('generatedOutput', 'children'),
        Input('simulate_input_field', 'n_clicks'),
        [State('latitude', 'value'),
         State('longitude', 'value'),
         State('data', 'value'),
         State('country', 'value'),
         ],
        prevent_initial_call=True
    )
    def store_data(n_clicks, latitude, longitude, data, country):
        if not n_clicks:
            raise PreventUpdate
        input_field_Data = {
            'latitude': latitude,
            'longitude': longitude,
            'data': data,
            'country': country
        }
        return json.dumps(input_field_Data, indent=4), 'Output Generated'


def getStoredData():
    @callback(
        Output('latitude1', 'value'),
        Output('longitude1', 'value'),
        Output('data1', 'value'),
        Output('country1', 'value'),
        Input('session', 'data')
    )
    def getStoredData(data):
        res = json.loads(data)

        return res['latitude'], res['longitude'], res['data'], res['country']


def simulationMap():
    @callback(
        Output("map-output", "children"),
        Output("map-output", "center"),
        Input('session', 'data')
    )
    def simulation_map(data):
        res = json.loads(data)
        marker = dl.Marker(
            position=[res['latitude'], res['longitude']],
            children=[dl.Tooltip(
                f"Latitude: {res['latitude']}, Longitude: {res['longitude']}")],
        )
        center = [res['latitude'], res['longitude']]
        return [dl.TileLayer(), marker], center


def updateSimulationOutput():
    @callback(
        Output('bar-chart', 'figure'),
        Output('country-bar-chart', 'figure'),
        Output('totalgdpSim', 'children'),
        Output('totalpopSim', 'children'),
        Output('avgExpSim', 'children'),
        Output('headingOfChart','children'),
        Input('session', 'data')
    )
    def update_output(data):
        res = json.loads(data)
        actualDataFrame = dataFrame()
        isSelected = 'country'
        df = actualDataFrame[actualDataFrame['country'] == res['country']]
        fig = px.bar(df, x=df['year'],
                     hover_data=['continent', 'country', 'pop', 'lifeExp'],
                     y=df['pop'], color=df['lifeExp'],
                     labels={'pop': 'population of' + ' ' + f"{res['country']}"})
        if res['data'] == 'country':
            isSelected = 'country'
        else:
            isSelected = 'year'
        fig1 = px.bar(actualDataFrame, x=actualDataFrame[isSelected],
                      y=actualDataFrame['gdpPercap'], color='country',
                      labels={'gdpPercap': 'GDP Per Capita'})
        a, b, c = calculateCountrySpecificData(df)
        return fig, fig1, a, b, c,f'GDP per capita Over {isSelected}'


def calculateCountrySpecificData(dataFrame):
    totalgdp = dataFrame['gdpPercap'].max()
    totalPopulation = dataFrame['pop'].max()
    averageLifeExp = dataFrame.loc[:, 'lifeExp'].mean()
    return totalgdp, totalPopulation, averageLifeExp


def displayPages():
    @callback(Output('page-content', 'children'),
              Output('redirect', 'pathname', allow_duplicate=True),
              [Input('url', 'pathname')],
              prevent_initial_call=True)
    def display_page(pathname):
        view = None
        url = dash.no_update
        if pathname == "/about":
            view = aboutlogout()  
        elif pathname == "/inputField":
            view = inputLayout()  
        elif pathname == "/simulation":
            view = simulationLayout()  
        else:
            view = html.Div("Page not found")
        return view, url


def allCallbacks():
    updatePageSize()
    updateTableData()
    generateCSV()
    storeInSession()
    updateSimulationOutput()
    simulationMap()
    getStoredData()
    displayPages()