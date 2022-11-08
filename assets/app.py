# DASHBOARD JIRI EXERCISE 

# SETUP
import pandas as pd
import dash
from dash import dcc,html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go 
from dash.dependencies import Input, Output
from flask_caching import Cache

# GET DATA


# DASHBOARD LAYOUT 
external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, prevent_initial_callbacks=True, url_base_pathname='/', update_title=None)
app.title = " SUBSCRIPTION PLANS DASHBOARD"

cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})


