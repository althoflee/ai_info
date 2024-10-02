#%%
import pandas as pd
import numpy as np

#%%
pd.show_versions()
# %%
raw_df = pd.read_csv("C:\\Users\\user\\Desktop\\seokjunlee\\aiwork\\datasets\\owid-covid-data.csv")
# %%
raw_df.head()

# %%
raw_df.info()
# %%
revise_df = raw_df[
    ["iso_code","location",
     "date",
     "total_cases",
     "population"     
     ]
    ]
revise_df.head()
# %%
locations = revise_df["location"].unique()
print(locations)
# %% south korea
korea_df = revise_df[revise_df["location"] == "South Korea" ]
korea_df.head()

# %%
korea_date_index_df = korea_df.set_index('date')
korea_date_index_df.head()

# %%
kor_total_case = korea_date_index_df["total_cases"]
kor_total_case.head()
# %%
kor_total_case.plot()
# %%
usa_df = revise_df[revise_df["location"] == "United States"]
usa_df.head()


# %%
usa_date_index_df = usa_df.set_index("date")
usa_date_index_df.head()
# %%
usa_total_case = usa_date_index_df["total_cases"]
usa_total_case.head()
# %%
final_df = pd.DataFrame(
    {
        'kor' : kor_total_case,
        'usa' : usa_total_case
    },index=kor_total_case.index
)
final_df.head()
# %%
final_df.plot(rot=45)
# %%
usa_population = usa_date_index_df['population']['2022-01-01']
print(usa_population)
kor_population = korea_date_index_df['population']['2022-01-01']
print(kor_population)
# %%
_rate = round(usa_population/kor_population,2)

print(_rate)

# %%
_final_df = pd.DataFrame({
    'kor' : kor_total_case * _rate,
    'usa' : usa_total_case
},index=korea_date_index_df.index)

_final_df.plot(rot=45)

# %%
