# %%
import pandas as pd
import matplotlib.pyplot as plt
# %%
df = pd.read_csv("consolidate_mpox.csv")
df['date'] = pd.to_datetime(df['date'])
#df_brazil = df[df['country'] == 'Brazil']

df_brazil_confirmed = df[
    (df["country"] == "Brazil") &
    (df["classification"] == "Confirmed")
]

df_series = (
    df_brazil_confirmed
    .groupby("date", as_index=False)["new_cases"]
    .sum()
    .sort_values("date")
)

# %%

semana = (
    df_series
    .set_index("date")
    .resample("W")["new_cases"]
    .sum()
)

semana.head(50)

# %%
df_series.head(50)