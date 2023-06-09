from dash import Dash, html
import pandas as pd
import numpy as np

from . import (
    density_heatmap_text,
    density_heatmap_radio,
    density_heatmap_plot,
)


def create_layout(
    app: Dash,
    unique_billboard_weeks: np.ndarray,
    data_animation: pd.DataFrame,
) -> html.Div:
    return html.Div(
        className="app-div bg-light",
        children=[
            html.H1(
                app.title,
                className="text-center text-weight-bold",
            ),
            html.H2(
                app.subtitle,
                className="text-center text-weight-bold",
            ),
            html.Hr(),
            # Spotify Audio Feature Visualization - Density Heatmaps
            html.Div(
                [
                    html.H2(
                        app.card_2,
                        className="card-header text-left align-vertical border-custom-light-gray",
                    ),
                    html.Div(
                        className="card-body text-justify m-auto",
                        children=[density_heatmap_text.render()],
                    ),
                    html.Div(
                        className="card-body",
                        children=[
                            density_heatmap_radio.render(app),
                            density_heatmap_plot.render(
                                app, unique_billboard_weeks, data_animation
                            ),
                        ],
                    ),
                ],
                className="card text-white bg-plotly-dark mb-3 border-custom-light-gray m-auto",
                style={"width": "85vw"},
            ),
        ],
    )
