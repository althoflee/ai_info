#%%
import pandas as pd
import numpy as np

print(pd.__version__)

# %%
raw_data = pd.read_csv("survey_results_public.csv")
# %%
raw_data.info()
# %%
raw_data.head()
# %%
