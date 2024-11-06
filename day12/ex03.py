#%%
import folium.plugins
import pandas as pd
import folium
#%%
data = pd.read_csv("..\__datasets__\seoul-metro-2015.logs.csv")
station_info = pd.read_csv("..\__datasets__\seoul-metro-station-info.csv")
# %%
data.info()
# %%
data.head()
# %%
station_sum = data.groupby('station_code').sum()
print(station_sum)
# %%
station_info.info()
# %%
station_info.head()

# %%
joined_data = station_sum.join(station_info)

#%%
joined_data.head()
# %%
seoul_in = folium.Map(location=[37.55,126.98],zoom_start=12)
seoul_in

# %%
from folium.plugins import HeatMap

#%%
joined_data[['geo.latitude','geo.longitude','people_in']].head()
#%%
HeatMap(data=joined_data[['geo.latitude','geo.longitude','people_in']]).add_to(seoul_in)
#%%
joined_data.info()
# %%
