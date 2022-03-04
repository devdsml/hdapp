import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
 
USERNAME_PASSWORD_PAIRS = [
    ['nethu', '12345'],['guvi', 'guvi'],['tstn','testn']
]
 
app = dash.Dash()
auth = dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)
server = app.server
 
 
 
app.layout = html.Div([
    dcc.RangeSlider(
        id='range-slider',
        min=-5,
        max=6,
        marks={i:str(i) for i in range(-5, 7)},
        value=[-3, 4]
    )]),
    html.H1(id='product')  # this is the output,
 html.Div([dcc.Dropdown(['NYC', 'MTL', 'SF'], 'NYC', id='demo-dropdown'),
    html.Div(id='dd-output-container')
], style={'width':'50%'})
 
@app.callback(
     Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value'))
def update_output(value):
    return f'You have selected {value}'
    
 
if __name__ == '__main__':
    app.run_server(debug=True)
