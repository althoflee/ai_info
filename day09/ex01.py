#%%
import pandas as pd
import numpy as np
import os

print(f'pandas version : {pd.__version__}')

#%%
raw_hawaii_df = pd.read_csv("../__datasets__/hawii_covid.csv")
raw_hawaii_df.info()
# %%
raw_hawaii_df.head()
# %%
_hawaii_data = raw_hawaii_df[['date_updated','tot_cases']]
_hawaii_data.info()

#%%
hawaii_data_index = _hawaii_data.set_index('date_updated')
hawaii_data_index.info()
# %%
hawaii_data = hawaii_data_index['tot_cases']
hawaii_data.head()

# %%
raw_df = pd.read_csv('../__datasets__/owid-covid-data.csv')
raw_df.info()

#%%
print(raw_df['location'].unique())
# %%
revise_df = raw_df[['date','total_cases','location']]
korea_df = revise_df[revise_df['location'] == 'South Korea']
#%%
korea_df.head()
# %%
korea_data_index_df = korea_df.set_index('date')
korea_data_index_df.head()
#%%
kor_data = korea_data_index_df['total_cases']
kor_data.head()
# %%
print(hawaii_data_index.index.dtype)
print(korea_data_index_df.index.dtype)
# %%
hawaii_data_index.index = pd.to_datetime(
    hawaii_data_index.index,
    format='%m/%d/%Y')
korea_data_index_df.index = pd.to_datetime(
    korea_data_index_df.index)

#%%
hawaii_data_index.info()
#%%
filtered_korean_df = korea_data_index_df[korea_data_index_df.index.isin(hawaii_data_index.index)]
# %%
final_df = pd.DataFrame(
    {
        'Korea' : filtered_korean_df['total_cases'] * 0.03,
        'Hawaii' : hawaii_data_index['tot_cases']
    },
    index=hawaii_data_index.index
)

#%%
final_df.head()
# %%
final_df.plot.line(rot=45)
# %%
