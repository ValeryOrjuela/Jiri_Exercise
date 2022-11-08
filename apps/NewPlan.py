# =================== [Tablero Mis recomendados] ==========================.#
from app import app
# [Librerias] ===============================================================.#
# Liberias manejo de tablas y listas
import numpy as np
# Librerias manejo de dash
from dash import dcc,html
import dash_bootstrap_components as dbc
import dash_table
from dash.dependencies import Input, Output, State
from apps.functions_NewPlan import *

##   ---------------------------------------------------.#
CVRNewPlan_G = dbc.CardBody(children = [html.H2("Inbound CVR - New Plan:", className="card-title",id="CVR_NewPlan"),
                html.P(children = "0", className="card-text",id="CVRNewPlan")],style={'display': 'inline-block',
                        'text-align': 'center','color':'#FFFFFF','fontSize': 40})
CVROldPlan_G = dbc.CardBody(children = [html.H2("Inbound CVR - Old Plan:", className="card-title",id="CVR_OldPlan"),
                html.P(children = "0", className="card-text",id="CVROldPlan")],style={'display': 'inline-block',
                        'text-align': 'center','color':'#FFFFFF','fontSize': 40})
FutStartDate_G = dbc.CardBody(children = [html.H4("Future Start Dates - New Plan:", className="card-title",id="Fut_StartDate"),
                html.P(children = "0", className="card-text",id="FutStartDate")],style={'display': 'inline-block',
                        'text-align': 'center','color':'#000000','fontSize': 40})
CVRNewPlan   = dbc.CardGroup([dbc.Card(CVRNewPlan_G, color='#019EC6')], className="fafa-list")
CVROldPlan   = dbc.CardGroup([dbc.Card(CVROldPlan_G, color='#0A66A5')], className="fafa-list")
FutStartDate   = dbc.CardGroup([dbc.Card(FutStartDate_G, color='#FFFFFF')], className="fafa-list")
## Gráfico 1 
CS_graph_1 = dcc.Graph(id="CS_bar1")  
##   ---------------------------------------------------.#
PrNewPlan_G = dbc.CardBody(children = [html.H2("Ratio failed payments - New Plan:", className="card-title",id="Pr_NewPlan"),
                html.P(children = "0", className="card-text",id="PrNewPlan")],style={'display': 'inline-block',
                        'text-align': 'center','color':'#FFFFFF','fontSize': 40})
PrOldPlan_G = dbc.CardBody(children = [html.H2("Ratio failed payments - Old Plan:", className="card-title",id="Pr_OldPlan"),
                html.P(children = "0", className="card-text",id="PrOldPlan")],style={'display': 'inline-block',
                        'text-align': 'center','color':'#FFFFFF','fontSize': 40})
PrNewPlan   = dbc.CardGroup([dbc.Card(PrNewPlan_G, color='#019EC6')], className="fafa-list")
PrOldPlan   = dbc.CardGroup([dbc.Card(PrOldPlan_G, color='#0A66A5')], className="fafa-list")
## Gráfico 2 
CS_graph_2 = dcc.Graph(id="CS_bar2")  
## Boton  ---------------------------------------------------.#
Botton_CS = html.Img(id='start_button', src='assets/Start.jpg', n_clicks=0, 
                        className='info-icon',height='70px', style={'display': 'inline-block'})                
### Estructura encabezado
t9_encabezado = html.Div([
                    # Boton de busqueda
                    html.Div([Botton_CS],style={'display': 'inline-block','padding': '2px 20px 30px 700px'}),
                    html.Div([
                        html.Div([CVRNewPlan], style={'width': '50%', 'display': 'inline-block','padding': '10px 5px 10px 140px'}),
                        html.Div([CVROldPlan], style={'width': '50%', 'display': 'inline-block','padding': '10px 100px 10px 50px'}),
                    ],style={'width': '100%','display': 'inline-block'}),
                    dbc.Row([
                            dbc.Col([CS_graph_1], width=8, style={'padding': '5px 5px 5px 150px'}),
                            dbc.Col([FutStartDate], width=3, style={'padding': '150px 0px 0px 0px'})
                            ]),
                    html.Div([
                        html.Div([PrNewPlan], style={'width': '50%', 'display': 'inline-block','padding': '10px 5px 10px 140px'}),
                        html.Div([PrOldPlan], style={'width': '50%', 'display': 'inline-block','padding': '10px 100px 10px 50px'}),
                    ],style={'width': '100%','display': 'inline-block'}),
                    dbc.Row([
                            dbc.Col([CS_graph_2], style={'padding': '5px 5px 5px 150px'})
                            ]),

                ],style={'padding': '5px 5px 5px 5px','border': '2px solid #FFFFFF', 'border-radius':'6px','marginBottom': 5})

layout = html.Div([
    html.H1(" "),
    t9_encabezado,
    html.H1("  "),
    html.H1(" "),
    html.H1(" ")
    ])

#
get_callbacks_CS(app)
# [Fin del codigo] ==========================================================.#