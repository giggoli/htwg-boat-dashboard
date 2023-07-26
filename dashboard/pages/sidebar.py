import dash
from dash import dcc, html, callback, Input, Output, State
import dash_bootstrap_components as dbc

sidebar = dbc.Nav(
    [
        dbc.NavLink([html.Div("Overview")], href="/", active="exact"),
        dbc.NavLink([html.Div("Battery")], href="/battery", active="exact"),
        dbc.NavLink([html.Div("Fuelcell")], href="/fuelcell", active="exact"),
        dbc.NavLink([html.Div("Fuellevel")], href="/fuellevel", active="exact"),
        dbc.NavLink([html.Div("GPS")], href="/gps", active="exact"),
        dbc.NavLink([html.Div("Solar")], href="/solar", active="exact"),
        dbc.NavLink([html.Div("Weather")], href="/weather", active="exact"),
    ],
    vertical = True,
    pills = True,
    id="menu"
)