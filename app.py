# DASHBOARD JIRI EXERCISE 

# SETUP
import pandas as pd
import dash
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go 
from dash.dependencies import Input, Output

# GET DATA


# DASHBOARD LAYOUT 
external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, prevent_initial_callbacks=True, url_base_pathname='/', update_title=None)
app.title = " SUBSCRIPTION PLANS DASHBOARD"


