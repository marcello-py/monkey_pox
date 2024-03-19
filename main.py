import pandas as pd
import matplotlib.pyplot as plt
# %%
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
plt.style.use('classic')
plt.scatter(df_group_brazil['total_cases'], df_group_brazil['date'], color='gray')
plt.xlabel('total_cases')
plt.ylabel('date')
plt.yticks(df_group_brazil['date'][::31])
plt.grid()
plt.savefig('monkey_pox_total_cases.jpg', format='jpg')
# %%
plt.figure(figsize=(10, 5))
#.style.use('classic')
plt.scatter(df_group_brazil['total_deaths'], df_group_brazil['date'], color='gray')
plt.xlabel('total_deaths')
plt.ylabel('date')
plt.yticks(df_group_brazil['date'][::31])
plt.grid()
plt.savefig('monkey_pox_total_deaths.jpg', format='jpg')
