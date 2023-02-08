import plotly.graph_objects as go
import plotly.io as pio

pio.templates["htwg_color_style"] = go.layout.Template(

    layout = {
        "paper_bgcolor": "#d9e5ec",
        "plot_bgcolor": "#d9e5ec",
        "font": {"color": "#008b83"},
        "colorway": [
            "#00e6d8",
            "#00ccc0",
            "#66c2bd",
            "#009a91",
            "#005c57",
            "#002e2b"
        ]
    }
)
