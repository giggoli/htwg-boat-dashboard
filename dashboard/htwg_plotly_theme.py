import plotly.graph_objects as go
import plotly.io as pio

pio.templates["htwg_color_style"] = go.layout.Template(

    layout = {
        "font": {"color": "#008b83"},
        "colorway": [
            "#009a91",
            "#00b3a7",
            "#00ccbe",
            "#00e6d6",
            "#00ffff"
        ],
        "font": {'color': '#2a3f5f'},
    }
)
