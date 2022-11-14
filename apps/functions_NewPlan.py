# =================== [Dashboard New Plan] ==========================.#
from app import app
# [Libraries] ===============================================================.#
# Liberias manejo de tablas y listas
import numpy as np
import pandas as pd
import plotly.express as px
# Librerias manejo de dash
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State
# [Call Excel] ------------------------------------------------------------.#
FutureStartDates  = pd.read_csv('aux_tables/FutureStartDates.csv').squeeze()
Day_New     = pd.read_excel('aux_tables/Day_New.xlsx').squeeze()
Day_Old     = pd.read_excel('aux_tables/Day_Old.xlsx').squeeze()

def get_callbacks_CS(app):
    # Add Callbacks
    # First question, CVR inbounds (New)
    @app.callback(Output('CVRNewPlan','children'),
                [Input('start_button','n_clicks')])
    def cardvalue(Button):
        if Button == 0:
            CVR = 0
        if Button == 1:
            PLAN_SOLD = 45
            CALLS_DONE = 5007 
            CVR = round((PLAN_SOLD/CALLS_DONE) * 100,2)
        return f'{CVR}%'
    # First question, CVR inbounds (Old)  
    @app.callback(Output('CVROldPlan','children'),
                [Input('start_button','n_clicks')])
    def cardvalue(Button):
        if Button == 0:
            CVR = 0
        if Button == 1:
            PLAN_SOLD = 46235
            CALLS_DONE = 829501
            CVR = round((PLAN_SOLD/CALLS_DONE) * 100,2)
        return f'{CVR}%' 
    # Define the type of the date 
    def categorise(row):  
        if row['difference'] > 0:
            return 2
        return 1
    def categorise_1(row):  
        if row['difference'] == 1:
            return 'NowDate'
        return 'FutureDate'
    # Bar Graph fo Future and Now Dates
    @app.callback(Output('CS_bar1','figure'),
                  Output('FutStartDate','children'),
                [Input('start_button','n_clicks')])
    def cardvalue(Button):
        Table = FutureStartDates
        Table['difference'] = Table.apply(lambda row: categorise(row), axis=1)
        NowDates = Table[Table.difference == 1].shape[0]
        FutureDates = Table[Table.difference == 2].shape[0]
        Future_Dates = round((FutureDates / (FutureDates + NowDates)) * 100,2)
        Table['Type_Date'] = Table.apply(lambda row: categorise_1(row), axis=1)
        fig = px.bar(Table,x='Type_Date',y='no_calls',template="simple_white",color='Type_Date')
        fig.update_yaxes(title_text='Subscriptions')
        fig.update_xaxes(title_text='Type date')
        fig.update_layout(showlegend=False)
        return fig,f'{Future_Dates}%'
    # Proportion no pay billling  
    @app.callback(Output('PrNewPlan','children'),
                [Input('start_button','n_clicks')])
    def cardvalue(Button):
        if Button == 0:
            CVR = 0
        if Button == 1:
            ALL_INVOICES = 45
            NOT_PAID = 4
            PR = round((NOT_PAID/ALL_INVOICES) * 100,2)
        return f'{PR}%'    
    @app.callback(Output('PrOldPlan','children'),
                [Input('start_button','n_clicks')])
    def cardvalue(Button):
        if Button == 0:
            CVR = 0 
        if Button == 1:
            ALL_INVOICES = 46235 
            NOT_PAID = 2506 
            PR = round((NOT_PAID/ALL_INVOICES) * 100,2)
        return f'{PR}%'    
    @app.callback(Output('CS_bar2','figure'),
                [Input('start_button','n_clicks')])
    def cardvalue(Button):
        Old = Day_Old
        Old = Old.groupby(['day_name']).count().reset_index()
        New = Day_New
        New = New.groupby(['name_day']).count().reset_index()
        # 58 de 321
        fig = px.line(Old, x = 'day_name', y = 'created_at',template = "simple_white" )
        fig.update_xaxes(title_text= 'Day Name')
        fig.update_yaxes(title_text= 'Frequency')
        return fig

    @app.callback(Output('CS_bar3','figure'),
                [Input('start_button','n_clicks')])
    def cardvalue(Button):
        Old_H = Day_Old
        Old_H['Hour'] = Old_H['created_at'].str[11:13]
        Old_H = Old_H.groupby(['Hour']).count().reset_index()
        New = Day_New
        New['Hour'] = New['created_at'].str[11:13]
        New = New.groupby(['Hour']).count().reset_index()
        # 58 de 321
        fig = px.line(Old_H, x = 'Hour', y = 'created_at',template = "simple_white" )
        fig.update_xaxes(title_text= 'Hour')
        fig.update_yaxes(title_text= 'Frequency')
        return fig