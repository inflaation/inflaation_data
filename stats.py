import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import numpy as np
import os.path
from datetime import datetime
from dash import Dash, dcc, html, Input, Output, ctx
import glob
import os

app = Dash(__name__,external_stylesheets=[dbc.themes.VAPOR])    #, meta_tags=[{'name': 'viewport', 'content': 'width=device-width'}])
server = app.server

app.layout = html.Div([
    dbc.Row(dbc.Col(html.H1('Current Farming Rates'))),
    dbc.Row(dbc.Col(html.H6(id='last-update'))),
    dcc.RadioItems(['Alchemica', 'FUD Equivalent'],'Alchemica',id='alchemica-type-radio',
        ),
    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(children='FUD'),
                    html.H3(id='fud-rate'),
                    html.H4(id='fud-quantity')
                ],style={'textalign': 'center','color': 'green'})
            )
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(children='FOMO'),
                    html.H3(id='fomo-rate'),
                    html.H4(id='fomo-quantity'),
                ],style={'textalign': 'center','color': 'red'})
            )
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(children='ALPHA'),
                    html.H3(id='alpha-rate'),
                    html.H4(id='alpha-quantity')
                ],style={'textalign': 'center','color': 'blue'})
            )
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H2(children='KEK'),
                    html.H3(id='kek-rate'),
                    html.H4(id='kek-quantity')
                ],style={'textalign': 'center','color': 'purple'})
            )
        )
    ]),
    dcc.Graph(id='graph1'),
    dcc.Graph(id='graph2'),
    dcc.Graph(id='graph3')
])


@app.callback(
    Output('graph1', 'figure'),
    Output('graph2', 'figure'),
    Output('graph3', 'figure'),
    Output('last-update', 'children'),
    Output('fud-rate', 'children'),
    Output('fud-quantity', 'children'),
    Output('fomo-rate', 'children'),
    Output('fomo-quantity', 'children'),
    Output('alpha-rate', 'children'),
    Output('alpha-quantity', 'children'),
    Output('kek-rate', 'children'),
    Output('kek-quantity', 'children'),
    Input('alchemica-type-radio', 'value'))
def set_alchemica_type(selected_alchemica):
    list_of_jsons = glob.glob('*.json')  # * means all if need specific format then *.csv
    latest_json = max(list_of_jsons, key=os.path.getctime)
    latest_timestamp = latest_json[14:-5]

    query_df = pd.read_json(latest_json)

    #Associate type.id & harvest rate from the recipe book
    fud_harvester_quantity = [len(query_df[(query_df['type.id'] == 56)]), len(query_df[(query_df['type.id'] == 57)]),
                              len(query_df[(query_df['type.id'] == 58)]), len(query_df[(query_df['type.id'] == 59)]),
                              len(query_df[(query_df['type.id'] == 60)]), len(query_df[(query_df['type.id'] == 61)]),
                              len(query_df[(query_df['type.id'] == 62)]), len(query_df[(query_df['type.id'] == 63)]),
                              len(query_df[(query_df['type.id'] == 64)])]
    fud_harvester_rate = [fud_harvester_quantity[0] * 4.2, fud_harvester_quantity[1] * 10,
                          fud_harvester_quantity[2] * 18, fud_harvester_quantity[3] * 30,
                          fud_harvester_quantity[4] * 50, fud_harvester_quantity[5] * 85,
                          fud_harvester_quantity[6] * 150, fud_harvester_quantity[7] * 277,
                          fud_harvester_quantity[8] * 527]

    fomo_harvester_quantity = [len(query_df[(query_df['type.id'] == 65)]), len(query_df[(query_df['type.id'] == 66)]),
                               len(query_df[(query_df['type.id'] == 67)]), len(query_df[(query_df['type.id'] == 68)]),
                               len(query_df[(query_df['type.id'] == 69)]), len(query_df[(query_df['type.id'] == 70)]),
                               len(query_df[(query_df['type.id'] == 71)]), len(query_df[(query_df['type.id'] == 72)]),
                               len(query_df[(query_df['type.id'] == 73)])]
    fomo_harvester_rate = [fomo_harvester_quantity[0] * 2.1, fomo_harvester_quantity[1] * 4.6,
                           fomo_harvester_quantity[2] * 8.3, fomo_harvester_quantity[3] * 14,
                           fomo_harvester_quantity[4] * 22, fomo_harvester_quantity[5] * 38,
                           fomo_harvester_quantity[6] * 68, fomo_harvester_quantity[7] * 125,
                           fomo_harvester_quantity[8] * 238]

    alpha_harvester_quantity = [len(query_df[(query_df['type.id'] == 74)]), len(query_df[(query_df['type.id'] == 75)]),
                                len(query_df[(query_df['type.id'] == 76)]), len(query_df[(query_df['type.id'] == 77)]),
                                len(query_df[(query_df['type.id'] == 78)]), len(query_df[(query_df['type.id'] == 79)]),
                                len(query_df[(query_df['type.id'] == 80)]), len(query_df[(query_df['type.id'] == 81)]),
                                len(query_df[(query_df['type.id'] == 82)])]
    alpha_harvester_rate = [alpha_harvester_quantity[0] * 1.5, alpha_harvester_quantity[1] * 2.8,
                            alpha_harvester_quantity[2] * 4.8, alpha_harvester_quantity[3] * 7.8,
                            alpha_harvester_quantity[4] * 13, alpha_harvester_quantity[5] * 22,
                            alpha_harvester_quantity[6] * 39, alpha_harvester_quantity[7] * 73,
                            alpha_harvester_quantity[8] * 138]

    kek_harvester_quantity = [len(query_df[(query_df['type.id'] == 83)]), len(query_df[(query_df['type.id'] == 84)]),
                              len(query_df[(query_df['type.id'] == 85)]), len(query_df[(query_df['type.id'] == 86)]),
                              len(query_df[(query_df['type.id'] == 87)]), len(query_df[(query_df['type.id'] == 88)]),
                              len(query_df[(query_df['type.id'] == 89)]), len(query_df[(query_df['type.id'] == 90)]),
                              len(query_df[(query_df['type.id'] == 91)])]
    kek_harvester_rate = [kek_harvester_quantity[0] * 0.3, kek_harvester_quantity[1] * 0.71,
                          kek_harvester_quantity[2] * 1.6, kek_harvester_quantity[3] * 2.7,
                          kek_harvester_quantity[4] * 4.1, kek_harvester_quantity[5] * 7,
                          kek_harvester_quantity[6] * 13, kek_harvester_quantity[7] * 24,
                          kek_harvester_quantity[8] * 45]

    if (selected_alchemica == 'FUD Equivalent'):
        harvesters_df_fud_eq = pd.DataFrame(np.zeros((36, 4)), columns=['Type', 'Level', 'Quantity', 'Rate'])
        for i in range(0, 9):
            harvesters_df_fud_eq.loc[i, 'Type'] = 'FUD'
            harvesters_df_fud_eq.loc[i + 9, 'Type'] = 'FOMO in FUD eq'
            harvesters_df_fud_eq.loc[i + 18, 'Type'] = 'ALPHA in FUD eq'
            harvesters_df_fud_eq.loc[i + 27, 'Type'] = 'KEK in FUD eq'
            harvesters_df_fud_eq.loc[i, 'Level'] = i + 1
            harvesters_df_fud_eq.loc[i + 9, 'Level'] = i + 1
            harvesters_df_fud_eq.loc[i + 18, 'Level'] = i + 1
            harvesters_df_fud_eq.loc[i + 27, 'Level'] = i + 1
            harvesters_df_fud_eq.loc[i, 'Quantity'] = fud_harvester_quantity[i]
            harvesters_df_fud_eq.loc[i + 9, 'Quantity'] = fomo_harvester_quantity[i]
            harvesters_df_fud_eq.loc[i + 18, 'Quantity'] = alpha_harvester_quantity[i]
            harvesters_df_fud_eq.loc[i + 27, 'Quantity'] = kek_harvester_quantity[i]
            harvesters_df_fud_eq.loc[i, 'Rate'] = fud_harvester_rate[i]
            harvesters_df_fud_eq.loc[i + 9, 'Rate'] = 2 * fomo_harvester_rate[i]
            harvesters_df_fud_eq.loc[i + 18, 'Rate'] = 4 * alpha_harvester_rate[i]
            harvesters_df_fud_eq.loc[i + 27, 'Rate'] = 10 * kek_harvester_rate[i]

        fig1 = px.histogram(harvesters_df_fud_eq, x='Type', y='Rate', color='Level', template='plotly_dark',
                            color_discrete_sequence=px.colors.sequential.Plasma_r,
                            #              color_discrete_map={'1': '#c4ec74', '2': '#92dc7e','3': '#64c987','4': '#39b48e', '5' : '#089f8f', '6' : '#00898a', '7' : '#08737f', '8' : '#215d6e', '9' : '#2a4858'},
                            title='Harvest Rate', text_auto=True)
        fig2 = px.bar(harvesters_df_fud_eq, x='Level', y='Rate', color='Type', barmode='group', template='plotly_dark',
                      color_discrete_map={'FUD': '#00cc96', 'FOMO in FUD eq': '#ef553b', 'ALPHA in FUD eq': '#636efa', 'KEK in FUD eq': '#ab63fa'},
                      title='Harvest Rate by Level', text_auto=True)
        fig3 = px.bar(harvesters_df_fud_eq, x='Level', y='Quantity', color='Type', barmode='group', template='plotly_dark',
                      color_discrete_map={'FUD': '#00cc96', 'FOMO in FUD eq': '#ef553b', 'ALPHA in FUD eq': '#636efa', 'KEK in FUD eq': '#ab63fa'},
                      title='Harvesters equipped', log_y=True, text_auto=True)

        fud_df = harvesters_df_fud_eq[(harvesters_df_fud_eq['Type'] == 'FUD')]
        fomo_df = harvesters_df_fud_eq[(harvesters_df_fud_eq['Type'] == 'FOMO in FUD eq')]
        alpha_df = harvesters_df_fud_eq[(harvesters_df_fud_eq['Type'] == 'ALPHA in FUD eq')]
        kek_df = harvesters_df_fud_eq[(harvesters_df_fud_eq['Type'] == 'KEK in FUD eq')]

        return fig1, fig2, fig3, f'Last updated: {str(datetime.fromtimestamp(int(latest_timestamp)))}', f"{fud_df['Rate'].sum():,.0f} / day", f"{fud_df['Quantity'].sum():,.0f} / day", f"{fomo_df['Rate'].sum():,.0f} / day", f"{fomo_df['Quantity'].sum():,.0f} / day", f"{alpha_df['Rate'].sum():,.0f} / day", f"{alpha_df['Quantity'].sum():,.0f} / day", f"{kek_df['Rate'].sum():,.0f} / day", f"{kek_df['Quantity'].sum():,.0f} / day"

    else:

        harvesters_df = pd.DataFrame(np.zeros((36, 4)), columns=['Type', 'Level', 'Quantity', 'Rate'])
        for i in range(0, 9):
            harvesters_df.loc[i, 'Type'] = 'FUD'
            harvesters_df.loc[i + 9, 'Type'] = 'FOMO'
            harvesters_df.loc[i + 18, 'Type'] = 'ALPHA'
            harvesters_df.loc[i + 27, 'Type'] = 'KEK'
            harvesters_df.loc[i, 'Level'] = i + 1
            harvesters_df.loc[i + 9, 'Level'] = i + 1
            harvesters_df.loc[i + 18, 'Level'] = i + 1
            harvesters_df.loc[i + 27, 'Level'] = i + 1
            harvesters_df.loc[i, 'Quantity'] = fud_harvester_quantity[i]
            harvesters_df.loc[i + 9, 'Quantity'] = fomo_harvester_quantity[i]
            harvesters_df.loc[i + 18, 'Quantity'] = alpha_harvester_quantity[i]
            harvesters_df.loc[i + 27, 'Quantity'] = kek_harvester_quantity[i]
            harvesters_df.loc[i, 'Rate'] = fud_harvester_rate[i]
            harvesters_df.loc[i + 9, 'Rate'] = fomo_harvester_rate[i]
            harvesters_df.loc[i + 18, 'Rate'] = alpha_harvester_rate[i]
            harvesters_df.loc[i + 27, 'Rate'] = kek_harvester_rate[i]

        fig1 = px.histogram(harvesters_df, x='Type', y='Rate', color='Level', template='plotly_dark',
                            color_discrete_sequence=px.colors.sequential.Plasma_r,
                            #              color_discrete_map={'1': '#c4ec74', '2': '#92dc7e','3': '#64c987','4': '#39b48e', '5' : '#089f8f', '6' : '#00898a', '7' : '#08737f', '8' : '#215d6e', '9' : '#2a4858'},
                            title='Harvest Rate', text_auto=True)
        fig2 = px.bar(harvesters_df, x='Level', y='Rate', color='Type', barmode='group', template='plotly_dark',
                      color_discrete_map={'FUD': '#00cc96', 'FOMO': '#ef553b', 'ALPHA': '#636efa', 'KEK': '#ab63fa'},
                      title='Harvest Rate by Level', text_auto=True)
        fig3 = px.bar(harvesters_df, x='Level', y='Quantity', color='Type', barmode='group', template='plotly_dark',
                      color_discrete_map={'FUD': '#00cc96', 'FOMO': '#ef553b', 'ALPHA': '#636efa', 'KEK': '#ab63fa'},
                      title='Harvesters equipped', log_y=True, text_auto=True)

        fud_df = harvesters_df[(harvesters_df['Type'] == 'FUD')]
        fomo_df = harvesters_df[(harvesters_df['Type'] == 'FOMO')]
        alpha_df = harvesters_df[(harvesters_df['Type'] == 'ALPHA')]
        kek_df = harvesters_df[(harvesters_df['Type'] == 'KEK')]

        return fig1, fig2, fig3, f'Last updated: {str(datetime.fromtimestamp(int(latest_timestamp)))}', f"{fud_df['Rate'].sum():,.0f} / day", f"{fud_df['Quantity'].sum():,.0f} / day", f"{fomo_df['Rate'].sum():,.0f} / day", f"{fomo_df['Quantity'].sum():,.0f} / day", f"{alpha_df['Rate'].sum():,.0f} / day", f"{alpha_df['Quantity'].sum():,.0f} / day", f"{kek_df['Rate'].sum():,.0f} / day", f"{kek_df['Quantity'].sum():,.0f} / day"

if __name__ == '__main__':
    app.run_server(debug=False)