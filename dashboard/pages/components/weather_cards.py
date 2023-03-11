from dash import dcc, html
import dash_bootstrap_components as dbc

weather_CUR = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Weather"),
                html.Div(id="weather_CUR", children="no Value received")
            ]
        ),
    ],
)

weather_TEMP = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Temperature"),
                html.Div(id="weather_TEMP", children="no Value received")
            ]
        ),
    ],
)

weather_VIS = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Visibility"),
                html.Div(id="weather_VIS", children="no Value received")
            ]
        ),
    ],
)

weather_W_SPD = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Wind speed"),
                html.Div(id="weather_W_SPD", children="no Value received")
            ]
        ),
    ],
)

weather_W_DEG = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Wind direction"),
                html.Div(id="weather_W_DEG", children="no Value received")
            ]
        ),
    ],
)

weather_W_GUST = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Gust"),
                html.Div(id="weather_W_GUST", children="no Value received")
            ]
        ),
    ],
)

weather_SUNRISE = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Sunrise"),
                html.Div(id="weather_SUNRISE", children="no Value received")
            ]
        ),
    ],
)

weather_SUNSET = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Sunset"),
                html.Div(id="weather_SUNSET", children="no Value received")
            ]
        ),
    ],
)