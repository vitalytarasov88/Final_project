import plotly.graph_objects as go
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from numpy import mean
from regressor import predict


sub_regions = ['Bibirevo', 'Nagatinskij Zaton', "Tekstil'shhiki", 'Mitino',
               'Basmannoe', 'Nizhegorodskoe', "Sokol'niki", 'Koptevo', 'Kuncevo',
               'Kosino-Uhtomskoe', 'Zapadnoe Degunino', 'Presnenskoe',
               'Lefortovo', "Mar'ino", "Kuz'minki", 'Nagornoe', "Gol'janovo",
               'Vnukovo', 'Juzhnoe Tushino', 'Severnoe Tushino',
               "Chertanovo Central'noe", 'Fili Davydkovo', 'Otradnoe',
               'Novo-Peredelkino', 'Bogorodskoe', 'Jaroslavskoe', 'Strogino',
               'Hovrino', "Moskvorech'e-Saburovo", 'Staroe Krjukovo', 'Ljublino',
               'Caricyno', 'Veshnjaki', 'Danilovskoe', 'Preobrazhenskoe',
               "Kon'kovo", 'Brateevo', 'Vostochnoe Izmajlovo', 'Vyhino-Zhulebino',
               'Donskoe', 'Novogireevo', 'Juzhnoe Butovo', 'Sokol', 'Kurkino',
               'Izmajlovo', 'Severnoe Medvedkovo', 'Rostokino',
               'Orehovo-Borisovo Severnoe', 'Ochakovo-Matveevskoe', 'Taganskoe',
               'Dmitrovskoe', 'Orehovo-Borisovo Juzhnoe', 'Teplyj Stan',
               'Babushkinskoe', 'Pokrovskoe Streshnevo', 'Obruchevskoe',
               'Filevskij Park', 'Troparevo-Nikulino', 'Severnoe Butovo',
               'Hamovniki', 'Solncevo', 'Dorogomilovo', 'Timirjazevskoe',
               'Lianozovo', 'Pechatniki', 'Krjukovo', 'Jasenevo',
               'Chertanovo Severnoe', 'Rjazanskij', 'Silino', 'Ivanovskoe',
               'Golovinskoe', 'Novokosino', 'Nagatino-Sadovniki',
               'Birjulevo Vostochnoe', 'Severnoe Izmajlovo', 'Sokolinaja Gora',
               'Vostochnoe Degunino', 'Prospekt Vernadskogo', 'Savelki',
               'Ajeroport', 'Vojkovskoe', 'Beskudnikovskoe', 'Krylatskoe',
               'Juzhnoportovoe', 'Perovo', 'Akademicheskoe', 'Horoshevo-Mnevniki',
               'Shhukino', 'Kapotnja', 'Horoshevskoe', 'Marfino',
               'Chertanovo Juzhnoe', 'Savelovskoe', 'Birjulevo Zapadnoe',
               'Nekrasovka', 'Cheremushki', 'Sviblovo', 'Alekseevskoe',
               "Krasnosel'skoe", 'Kotlovka', 'Zjuzino', 'Ostankinskoe',
               'Tverskoe', 'Losinoostrovskoe', 'Butyrskoe', 'Matushkino',
               'Metrogorodok', 'Juzhnoe Medvedkovo', 'Lomonosovskoe', 'Jakimanka',
               'Mozhajskoe', 'Levoberezhnoe', "Mar'ina Roshha", 'Gagarinskoe',
               "Zamoskvorech'e", "Altuf'evskoe", 'Ramenki', 'Zjablikovo',
               'Meshhanskoe', 'Severnoe', 'Begovoe', 'Arbat',
               'Poselenie Sosenskoe', 'Poselenie Moskovskij',
               'Poselenie Pervomajskoe', 'Poselenie Desjonovskoe',
               'Poselenie Voskresenskoe', 'Poselenie Mosrentgen',
               'Troickij okrug', 'Poselenie Shherbinka',
               'Poselenie Filimonkovskoe', 'Poselenie Vnukovskoe',
               'Poselenie Marushkinskoe', 'Poselenie Shhapovskoe',
               'Poselenie Rjazanovskoe', 'Poselenie Kokoshkino', 'Vostochnoe',
               'Poselenie Krasnopahorskoe', 'Poselenie Novofedorovskoe',
               'Poselenie Voronovskoe', 'Poselenie Klenovskoe',
               'Poselenie Rogovskoe', 'Poselenie Kievskij', 'Molzhaninovskoe',
               'Poselenie Mihajlovo-Jarcevskoe']

sub_regions.sort()

app = dash.Dash()
server = app.server
data = pd.read_csv('shirota dolgota rajonov.csv')
d = pd.DataFrame(data)

map_ = go.Scattermapbox(
    customdata=d,
    name='DISTRICT OF MOSCOW',
    lon=d['longitude'],
    lat=d['Latitude'],
    mode='markers',
    text=d['District'],
    fillcolor='mediumturquoise',
    showlegend=True,

    marker=go.scattermapbox.Marker(
        size=30,
        color="BLUE",
        opacity=1,
    ),
    opacity=0.5,

)
layout = go.Layout(
    height=800,
    mapbox_style="stamen-watercolor",
    autosize=True,
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"

    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)
data = [map_]

fig = go.Figure(data=data, layout=layout)
fig.update_layout(title='HOUSE PRICE PREDICTION')
map_center = go.layout.mapbox.Center(lat=55.5900, lon=37.6156)
fig.update_layout(mapbox_style="open-street-map", clickmode="event+select", mapbox=dict(center=map_center, zoom=7.9))

app.layout = html.Div([
    dcc.Graph(id='map', figure=fig),

    html.Div([
        dcc.Markdown("Please select the **Name of your district:**")
    ], style={'display': 'inline-block', 'width': '100%', 'margin': '1vh'}),

    html.Div([
        dcc.Dropdown(
            options=[{'label': name, 'value': name} for name in sub_regions],
            id='sub_region'
        )], style={'display': 'inline-block', 'width': '20%', 'margin': '1vh'}),

    html.Div([
        dcc.Markdown("Please input the **total area** in square meters, including _loggias,"
                     " balconies and other non-residential areas_:")
    ], style={'display': 'inline-block', 'width': '100%', 'margin': '1vh'}),
    html.Div([
        dcc.Input(
            placeholder='Full area',
            type='number',
            value='',
            step=1,
            id='full_area'
        )], style={'display': 'inline-block', 'width': '100%', 'margin': '1.5vh'}),

    html.Div([
        dcc.Markdown("Please set the approximate distance range from your home to nearest"
                     " **Public Transportation Station** (km):")
    ], style={'display': 'inline-block', 'width': '100%', 'margin': '1.5vh'}),
    html.Div([
        dcc.RangeSlider(
            min=0,
            max=5,
            step=0.1,
            value=[1, 3],
            marks={
                0: {'label': '0'},
                0.5: {'label': '0.5'},
                1: {'label': '1'},
                1.5: {'label': '1.5'},
                2: {'label': '2'},
                2.5: {'label': '2.5'},
                3: {'label': '3'},
                3.5: {'label': '3.5'},
                4: {'label': '4'},
                4.5: {'label': '4.5'},
                5: {'label': '5'},
            },
            id='transport_distance'
        )], style={'display': 'inline-block', 'width': '100%', 'margin': '1.5vh'}),

    html.Div([
        dcc.Markdown("Please input the approximate number of **Shopping Malls** within 2 km from the  house:")
    ], style={'display': 'inline-block', 'width': '100%', 'margin': '1.5vh'}),
    html.Div([
        dcc.Input(
            placeholder='Shopping Malls within 2km',
            type='number',
            value='',
            step=1,
            id='mall_count'
        )], style={'display': 'inline-block', 'width': '100%', 'margin': '1.5vh'}),

    html.Div([
        dcc.Markdown(
            "Please input the approximate number of **Leisure Facilities** within 500m from your house:")
    ], style={'display': 'inline-block', 'width': '100%', 'margin': '1.5vh'}),
    html.Div([
        dcc.Input(
            placeholder='Leisure facilities',
            type='number',
            value='',
            step=1,
            id='leisure_facilities'
        )], style={'display': 'inline-block', 'width': '100%', 'margin': '1.5vh'}),

    html.Button('Submit', id='button', style={'display': 'inline-block', 'margin': '1.5vh'}),

    html.Div(id="output")
    
])


@app.callback(dash.dependencies.Output('output', 'children'),
              [dash.dependencies.Input('button', 'n_clicks'),
               dash.dependencies.Input('sub_region', 'value'),
               dash.dependencies.Input('full_area', 'value'),
               dash.dependencies.Input('transport_distance', 'value'),
               dash.dependencies.Input('mall_count', 'value'),
               dash.dependencies.Input('leisure_facilities', 'value')])
def update_rank_plot(n_clicks, sub_region, full_area, transport_distance, mall_count, leisure_facilities):

    if n_clicks is None:
        return ""

    prediction = predict(mean(transport_distance), mall_count, leisure_facilities, full_area, sub_region)

    return dcc.Markdown("### The calculated value for your house is approximately: **"
                        + str(round(prediction[0])) + " RUB**")


@app.callback(dash.dependencies.Output('sub_region', 'value'),
              dash.dependencies.Input('map', 'clickData'))
def set_sub_region(clickData):
    if clickData:
        return clickData['points'][0]['text']
    else:
        return None


if __name__ == '__main__':
    app.run_server(debug=True)
