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
