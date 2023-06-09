from dash import Dash
from dash_bootstrap_components.themes import LUX

from src.components.layout import create_layout

import pandas as pd
import numpy as np
import json
import os

processed_dir = "data/processed"

ANIMATION_FRAMES_PATH = os.path.join(
    processed_dir, "billboardAnimationFramesDecade.json"
)
BILLBOARD_WEEKS_PATH = os.path.join(
    processed_dir, 'unique_billboard_weeks.npy'
)
YEAR_START = 1960
YEAR_END = 2022

app = Dash(__name__, external_stylesheets=[LUX, os.path.join('assets', 'style.css')])
server = app.server

# Load Billboard-Spotify Data
with open(ANIMATION_FRAMES_PATH, "r") as json_file:
    json_data = json.load(json_file)
data_animation = pd.DataFrame(json_data)

# Load saved unique Billboard weeks numpy array
unique_billboard_weeks = np.load(BILLBOARD_WEEKS_PATH, allow_pickle=True)

app.title = "Popular Tracks' Audio Feature Exploration:"
app.subtitle = "Interactive Data App"
app.card_2 = "Joint Distributions of Audio Features Over Time"

app.layout = create_layout(app, unique_billboard_weeks, data_animation)
port = int(os.environ.get('PORT', 5000))
app.run_server(host='0.0.0.0', port=port)
