import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=0)

layout = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col([
                    html.H3(children="Fuellevel")
                ],xs=12, sm=12, md=12, lg=12, xl=12, xxl=12)
            ], className="row-title"
        ),
        dbc.Row(
            [
                dbc.Col([],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
    ],
)