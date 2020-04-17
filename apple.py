import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.close('all')

data = pd.read_csv("./applemobilitytrends-2020-04-14.csv")
df = pd.DataFrame(data)
df_kl = df[df['region']=="Kuala Lumpur"]

#print(df_kl.head())
#print(df_kl[:1])
#print(df_kl['2020-04-01'])

df_kl_date = df_kl.transpose()[3:]
df_kl_date.columns = ['driving', 'walking']
df_kl_date = df_kl_date.rename_axis('date', axis=0)

#print(df_kl_date.head())
#print(df_kl_date.tail())

[df_kl_date[col].update((df_kl_date[col] - df_kl_date[col].min()) / (df_kl_date[col].max() - df_kl_date[col].min())) for col in df_kl_date.columns]
[df_kl_date[col].update((df_kl_date[col] - df_kl_date[col].iloc[0]) * 100) for col in df_kl_date.columns]

df_kl_date.plot(title='Apple Mobility Trends', figsize=(15,10), legend=True, fontsize=12)

plt.show()
