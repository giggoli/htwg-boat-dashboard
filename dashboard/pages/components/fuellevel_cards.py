from dash import dcc, html
import dash_bootstrap_components as dbc



fuellevel_ID = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Fuellevel sensor ID"),
                html.Div(id="fuellevel_ID", children="no Value received")
            ]
        ),
    ],
)

fuellevel_FL = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Fuellevel"),
                html.Div(id="fuellevel_FL", children="no Value received")
            ]
        ),
    ],
)

fuellevel_FA = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Fuelamount"),
                html.Div(id="fuellevel_FA", children="no Value received")
            ]
        ),
    ],
)

fuellevel_TEMP = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Fuel temperature"),
                html.Div(id="fuellevel_TEMP", children="no Value received")
            ]
        ),
    ],
)

fuellevel_ERROR = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Fuellevel error"),
                html.Div(id="fuellevel_ERROR", children="no Value received")
            ]
        ),
    ],
)