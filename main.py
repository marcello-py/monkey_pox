# %%
<<<<<<< HEAD
=======

import plotly.graph_objs as go
import plotly.offline as py
>>>>>>> 7d7c68c18a2eb52eecdfd94b408ab1fbce73e2ad
import pandas as pd
import matplotlib.pyplot as plt
# %%

<<<<<<< HEAD
df = pd.read_csv(r'..\plot_monkeypox\monkeypox_data.csv')
df

# %%
location_brazil = df['location'] == 'Brazil'
df_brazil = df[location_brazil]
df_brazil
# %%
df_group_brazil = df_brazil[['date', 'location', 'total_cases', 'total_deaths']].reset_index()
df_group_brazil
# %%
df_group_brazil.drop(columns='index', inplace=True)
# %%
df_group_brazil['avg_cases_deaths(%)'] = (df_group_brazil['total_deaths'] / df_group_brazil['total_cases'] * 100).round(2)
df_group_brazil
# %%
plt.figure(figsize=(10, 5))
#.style.use('classic')
plt.scatter(df_group_brazil['total_cases'], df_group_brazil['date'], color='gray')
plt.xlabel('total_cases')
plt.ylabel('date')
plt.yticks(df_group_brazil['date'][::31])
plt.grid()
plt.savefig('monkey_pox_total_cases.jpg', format='jpg')

# %%
pd.set_option('display.max_rows', None)
df_group_brazil
# %%
plt.figure(figsize=(10, 5))
#.style.use('classic')
plt.scatter(df_group_brazil['total_deaths'], df_group_brazil['date'], color='gray')
plt.xlabel('total_deaths')
plt.ylabel('date')
plt.yticks(df_group_brazil['date'][::31])
plt.grid()
plt.savefig('monkey_pox_total_deaths.jpg', format='jpg')
=======
pd.set_option('display.max_rows', 500)  # Padronizar a quantidade de "linhas"
df_monkeypox = pd.read_csv('../monkey_pox/monkeypox_data.csv')
# %%

location_brazil = df_monkeypox['location'] == 'Brazil'
df_brazil = df_monkeypox[location_brazil]
# %%

group_brazil = df_brazil[['date', 'location', 'total_deaths', 'total_cases']].reset_index()
group_brazil
# %%

group_brazil['avg_cases_deaths(%)'] = (group_brazil['total_deaths'] / group_brazil['total_cases'] * 100).round(2)
group_brazil
# %%

trace_cases = go.Scatter(
    x=group_brazil['total_cases'],
    y=group_brazil['date'],
    mode='markers',
    marker={'color': '#0077ff', 'line': {'width': 1, 'color': 'black'}},
    opacity=0.9
)

data_cases = [trace_cases]

layout_cases = go.Layout(
    title='Dados dos casos relacionados à data',
    width=900,
    yaxis={'title': 'Mês'},
    xaxis={'title': 'Casos'}
)
fig_cases = go.Figure(data=data_cases, layout=layout_cases)
# %%

trace_deaths = go.Scatter(
    x=group_brazil['total_deaths'],
    y=group_brazil['date'],
    mode='markers',
    marker={'color': '#0077ff', 'line': {'width': 1, 'color': 'black'}},
    opacity=0.9
)
data_deaths = [trace_deaths]
layout_deaths = go.Layout(
    title='Dados das mortes relacionadas à data',
    width=900,
    yaxis={'title': 'Mês'},
    xaxis={'title': 'Mortes'},    
)

fig_deaths = go.Figure(data=data_deaths, layout=layout_deaths)

# %%

py.iplot(fig_cases)
py.iplot(fig_deaths)
>>>>>>> 7d7c68c18a2eb52eecdfd94b408ab1fbce73e2ad
