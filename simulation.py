from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_leaflet as dl


map = dl.Map(
    dl.TileLayer(),
    id="map-output",
    center=[20, 20],  # default values
    zoom=6,
    style={
        "height": 400,
        "width": "95%",
        "margin": "auto",
        "marginTop": "30px",
    },
)

simulation_layout = html.Div(
    children=[
        map,
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Label(
                            "User Provided Fields", className="userProvidedField"
                        ),
                        html.Div(
                            children=[
                                html.Div(
                                    children=[
                                        html.Div(
                                            children=[
                                                html.Div(
                                                    children=[
                                                        dbc.Label(
                                                            "Latitude: ",
                                                            className="header",
                                                        ),
                                                        dbc.Input(
                                                            valid="",
                                                            id="latitude1",
                                                            disabled=True,
                                                        ),
                                                    ],
                                                    className="UserInput",
                                                ),
                                                html.Hr(),
                                                html.Div(
                                                    children=[
                                                        dbc.Label(
                                                            "Longitude: ",
                                                            className="header",
                                                        ),
                                                        dbc.Input(
                                                            valid="",
                                                            id="longitude1",
                                                            disabled=True,
                                                        ),
                                                    ],
                                                    className="UserInput",
                                                ),
                                                html.Hr(),
                                                html.Div(
                                                    children=[
                                                        dbc.Label(
                                                            "Data: ", className="header"
                                                        ),
                                                        dbc.Input(
                                                            valid="",
                                                            id="data1",
                                                            disabled=True,
                                                        ),
                                                    ],
                                                    className="UserInput",
                                                ),
                                                html.Hr(),
                                                html.Div(
                                                    children=[
                                                        dbc.Label(
                                                            "Country: ",
                                                            className="header",
                                                        ),
                                                        dbc.Input(
                                                            valid="",
                                                            id="country1",
                                                            disabled=True,
                                                        ),
                                                    ],
                                                    className="UserInput",
                                                ),
                                                html.Hr(),
                                            ],
                                            className="formContainer",
                                        )
                                    ]
                                ),
                                html.Div(children="Output generated"),
                            ],
                            className="inputedFields",
                        ),
                    ],
                    style={"width": "100%"},
                ),
                html.Div(
                    children=[
                        html.Label("Country Data: ", className="userProvidedField"),
                        html.Div(
                            children=[
                                html.Div(
                                    children=[
                                        html.Label("Total GDP: "),
                                        html.Span(id="totalgdpSim"),
                                    ],
                                    className="countryItem",
                                ),
                                html.Hr(),
                                html.Div(
                                    children=[
                                        html.Label("Total Population: "),
                                        html.Span(id="totalpopSim"),
                                    ],
                                    className="countryItem",
                                ),
                                html.Hr(),
                                html.Div(
                                    children=[
                                        html.Label("Average life Expectancy: "),
                                        html.Span(id="avgExpSim"),
                                    ],
                                    className="countryItem",
                                ),
                                html.Hr(),
                            ],
                            className="countryclass",
                        ),
                    ],
                    style={"width": "50%"},
                ),
            ],
            className="inputandcountry",
        ),
        html.Div(
            children=[
                html.Label(
                    "Calculated Bar Chart",
                    className="userProvidedField calculatedBarChart",
                ),
                html.Div(
                    children=[dcc.Graph(id="bar-chart")], className="calculatedBarChart"
                ),
            ]
        ),
        html.Div(
            children=[
                html.Label(
                    " ",
                    id="headingOfChart",
                    className="userProvidedField calculatedBarChart",
                ),
                html.Div(
                    children=[dcc.Graph(id="country-bar-chart")],
                    className="calculatedBarChart",
                ),
            ]
        ),
    ],
    id="simulation",
)


def simulationLayout():
    return simulation_layout