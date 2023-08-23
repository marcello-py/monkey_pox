# %%

import plotly.graph_objs as go
import plotly.offline as py
import pandas as pd
import matplotlib.pyplot as plt
# %%
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




# %%
import plotly.express as px


# %%
date_brazil = group_brazil['date'] < '2022-08-01'
df_date = group_brazil[date_brazil]
df_date
df['date'] = pd.DatetimeIndex(df['Date Attribute']).month


# %%
fig = px.scatter(df_date, x="total_cases", y="date", color='total_deaths')
fig.show()

# %%
import matplotlib.pyplot  as plt


# %%

fig, ax = plt.subplots(figsize=(20, 10))
ax.plot(df_date['total_cases'], 
        df_date['date'], 
        marker='o', color='orange', 
        label='Casos')
plt.show()