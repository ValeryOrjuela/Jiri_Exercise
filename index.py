# ========================== [Main menu] ===============================.#
# [Bookstores] ===============================================================.#
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
# Import Layout for the board -----------------------------------------.#
from app import app
## Information slide
from apps import  NewPlan, home
print('Carga layout')
## [board components] ------------------------------------------------.#
### CreditStage menus available ........................................................#
Home = dbc.NavItem(dbc.NavLink("Home", href="/Home"))
New_Plan = dbc.NavItem(dbc.NavLink("NewPlan", href="/NewPlan"))
### CreditStage navigation bar ......................................................#
Logo = html.Img(src='./assets/credit.png', style={'height': '2rem'})
navbar = dbc.Navbar(
    [
     dbc.Col(Logo),
     dbc.Col(dbc.Nav([Home,New_Plan],navbar=True),width="auto"),
    ],
    color="#174173",
    dark=True
    )
## [Board components] ------------------------------------------------.#
app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    # Store to save the filter variables
    dcc.Store(id='session_t1', storage_type='session'),
    # board content
    #navbar,
    html.Div(id='navbar'),
    html.Div(id='page-content'),
])
## [Link to the another boards] ----------------------------------------------.#
@app.callback([Output('navbar', 'children'), Output('page-content', 'children')],Input('url', 'pathname'))
def display_page(pathname):
    print('display_page', pathname)
    sel_navbar = navbar
    if pathname == '/NewPlan':
        return sel_navbar, NewPlan.layout
    else :
        return sel_navbar, home.layout
if __name__ == '__main__':
    app.run_server(debug=True)
