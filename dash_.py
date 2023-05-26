from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv(r'C:\Users\sclifford\OneDrive - Gallarus Industry Solutions\MscDataAnalytics\MScDataAnalyticsCA2\Data\MLdata_df.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Construction Data', style={'textAlign':'center'}),
    dcc.Dropdown(df.country_name.unique(), 'Ireland', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country_name==value]
    return px.line(dff, x='TIME_PERIOD', y='IS-IP')

if __name__ == '__main__':
    app.run_server(debug=True)
