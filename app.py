import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
 
USERNAME_PASSWORD_PAIRS = [
    ['nethu', '12345'],['guvi', 'guvi'],['tstn','testn']
]
df = pd.read_csv('https://raw.githubusercontent.com/nethajinirmal13/Training-datasets/main/matches.csv')
app = dash.Dash()
auth = dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)
server = app.server
app.layout = html.Div([
    dcc.Dropdown(['Mumbai Indians', 'Chennai Super Kings', 'Royal Challengers Bangalore'], 'Mumbai Indians', id='baseddown'),
    html.Div(dcc.Graph(
       id='graph-1',
      ))
])


@app.callback(
    Output('graph-1','figure'),
    Input('baseddown', 'value')
)
def update_graph(value):
      df1 = df[df['winner'] ==value]
      fig5=px.bar(df1,x='venue',title='Luckiest Venue')
      
      return fig5
 
if __name__ == '__main__':
    app.run_server(debug=True)
