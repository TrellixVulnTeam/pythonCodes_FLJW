import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

colors={
    'background':'#111111',
    'text':'#7DFBFF'
}

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/' +
    '5d1ea79569ed194d432e56108a04d188/raw/' +
    'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
    'gdp-life-exp-2007.csv')

app.layout = html.Div(children=[
    html.H1(
        children='Hello World from Dash',
        style={
            'textAlign':'center',
            'color':colors['text'],
            'backgroundColor':colors['background']
        }
    ),
    dcc.Graph(
        id = 'file-exp-vs-gdp',
        figure = {
            'data':[
                go.Scatter(
                    x=df[df['continent']==i]['gdp per capita'],
                    y=df[df['continent']==i]['life expectancy'],
                    text=df[df['continent']==i]['country'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size':15,
                        'line':{
                            'width':0.5,
                            'color':'white'
                        },
                    },
                    name=i
                ) for i in df.continent.unique()
            ],
            'layout':go.Layout(
                xaxis={'type':'lol','title':'GDP Per Capita'},
                yaxis={'title':'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x':0,'y':1},
                hovermode='closest',
            )
        }
    )
])


def main():
    app.run_server()

if __name__ == '__main__':
    main()