#%%
import folium

print(f"folium version  {folium.__version__}")
#%%
wku_location = (35.967835,126.957068)

#%%
m = folium.Map(location=wku_location,zoom_start=16)

# %%
m

# %%
m.show_in_browser()

# %%
folium.Marker(
    location=(35.968726, 126.957917),
    tooltip="click me",
    popup="프라임관",
    icon=folium.Icon("cloud")    
).add_to(m)
m
# %%
