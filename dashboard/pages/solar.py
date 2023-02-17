import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
# import plotly.io as pio
# import my_themes

dash.register_page(__name__, order=1)

# pio.templates.default = "htwg_color_style"
fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = 270,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Speed"},
    gauge = {  'bar': {'color': "darkblue"}} 
    ))

bar = go.Figure(
    go.Pie(values=[10,10,10,10,10,10])
)

layout = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Graph(figure=fig)
                    ],xs=6, sm=6, md=6, lg=6, xl=6, xxl=6),
                dbc.Col(
                    [
                        dcc.Graph(figure=bar)
                    ],xs=6, sm=6, md=6, lg=6, xl=6, xxl=6),
            ]
        )
        
    ],
    className="container"
)
