#%%
import folium.plugins
import pandas as pd
import folium
from folium.plugins import HeatMap

#%%
data = pd.read_csv("../__datasets__/seoul-metro-2021.logs.csv")
data.info()
data.head()
# %%
station_sum = data.groupby('station_code').sum()
print(station_sum)
# %%
# 필요한 컬럼만 선택하여 인덱스 설정
station_info = pd.read_csv("../__datasets__/seoul-metro-station-info.csv")
station_info = station_info[['station.code', 'geo.latitude', 'geo.longitude']]
station_info.set_index('station.code', inplace=True)
print(station_info.head())
# %%
station_info.head()
station_info.info()

# %%
joined_data = station_sum.join(station_info)

#%%
joined_data.head()
# %%
seoul_in = folium.Map(location=[37.55,126.98],zoom_start=12)
seoul_in

#%%
HeatMap(data=joined_data[['geo.latitude','geo.longitude','people_in']]).add_to(seoul_in)
#%%
joined_data.info()
# %%
seoul_in

# %%
