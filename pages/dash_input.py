from dash import html
import dash_bootstrap_components as dbc

input_field_layout = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.H3(children="User Input", className="tab"),
                        html.Div(
                            children=[
                                html.Div(
                                    children=[
                                        dbc.Label("Latitude *", className="header"),
                                        dbc.Input(
                                            valid="",
                                            placeholder="Latitude Eg:39.54",
                                            id="latitude",
                                        ),
                                    ],
                                    className="UserInput",
                                ),
                                html.Hr(),
                                html.Div(
                                    children=[
                                        dbc.Label("Longitude *", className="header"),
                                        dbc.Input(
                                            valid="",
                                            placeholder="Longitude Eg:79.54",
                                            id="longitude",
                                        ),
                                    ],
                                    className="UserInput",
                                ),
                                html.Hr(),
                                html.Div(
                                    children=[
                                        dbc.Label("Data *", className="header"),
                                        dbc.Input(
                                            valid="",
                                            placeholder="Enter Dataset GDP vs (country or year)",
                                            id="data",
                                        ),
                                    ],
                                    className="UserInput",
                                ),
                                html.Hr(),
                                html.Div(
                                    children=[
                                        dbc.Label("Country *", className="header"),
                                        dbc.Input(
                                            valid="",
                                            placeholder="Enter a Country Name",
                                            id="country",
                                        ),
                                    ],
                                    className="UserInput",
                                ),
                                html.Hr(),
                            ],
                            className="formContainer",
                        ),
                    ],
                    className="cont",
                ),
                html.Div(
                    children=[
                        html.H3(children="Calculated Input", className="tab"),
                        html.Div(id="generatedOutput"),
                    ],
                    className="cont",
                ),
            ],
            className="inputFieldContainer",
        ),
        html.Div(
            children=[
                html.Button(
                    children="SIMULATE",
                    className="btn btn-primary",
                    id="simulate_input_field",
                )
            ],
            className="simulateButton",
        ),
    ]
)


def inputLayout():
    return input_field_layout