import dash
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

# fuellevel_FL
# fuellevel_FA
# fuellevel_TEMP
# fuellevel_ERROR