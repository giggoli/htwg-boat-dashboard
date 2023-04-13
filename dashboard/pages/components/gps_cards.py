from dash import dcc, html
import dash_bootstrap_components as dbc



gps_HEAD = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Heading"),
                html.Div(id="gps_HEAD", children="no Value received")
            ]
        ),
    ],
)

gps_VALID = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Validity"),
                html.Div(id="gps_VALID", children="no Value received")
            ]
        ),
    ],
)

gps_LAT = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Latitude"),
                html.Div(id="gps_LAT", children="no Value received")
            ]
        ),
    ],
)

gps_NS = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="North/South"),
                html.Div(id="gps_NS", children="no Value received")
            ]
        ),
    ],
)

gps_LONG = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Longitude"),
                html.Div(id="gps_LONG", children="no Value received")
            ]
        ),
    ],
)

gps_EW = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Eath/West"),
                html.Div(id="gps_EW", children="no Value received")
            ]
        ),
    ],
)

gps_SPEED = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Speed over ground"),
                html.Div(id="gps_SPEED", children="no Value received")
            ]
        ),
    ],
)

gps_VARIAT = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Variation"),
                html.Div(id="gps_VARIAT", children="no Value received")
            ]
        ),
    ],
)

gps_VARIAT_EW = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Variation East/West"),
                html.Div(id="gps_VARIAT_EW", children="no Value received")
            ]
        ),
    ],
)

gps_MAP = dbc.Card(
    [
        dbc.CardBody(
            [
                html.Div(id="gps_MAP", children="no Value to show on Map")
            ]
        ),
    ],
)
