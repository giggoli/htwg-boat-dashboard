import plotly.graph_objects as go
import plotly.io as pio

pio.templates["htwg_color_style"] = go.layout.Template(

    layout = {
        "font": {"color": "#008b83"},
        "colorway": [
            "#00e6d8",
            "#00ccc0",
            "#66c2bd",
            "#009a91",
            "#005c57",
            "#002e2b"
        ],
        "font": {'color': '#2a3f5f'},
    }
)
