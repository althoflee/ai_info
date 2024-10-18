#%%
import pandas as pd
import numpy as np
import os
print(f'pd version : {pd.__version__}')
#%%
raw_df = pd.read_csv('..\__datasets__\survey_results_public.csv')
raw_df.info()
#%%
for col in raw_df.columns :
    print(col)

# %%
reversed_df = raw_df[["Age","Country","LearnCode",
                      "LanguageHaveWorkedWith",
                      "LanguageWantToWorkWith"]]
reversed_df.head()

# %%
print(reversed_df['Age'])
# %%
print(reversed_df["Age"].drop_duplicates())
# %%
size_by_age = reversed_df.groupby("Age").size()
print(size_by_age)
# %%
size_by_age.plot.bar()
# %%
reindex_size_by = size_by_age.reindex(index=[
    "Under 18 years old",
    "18-24 years old",
    "25-34 years old",
    "35-44 years old",
    "45-54 years old",
    "55-64 years old",
    "65 years or older",
    "Prefer not to say"
])
# %%
reindex_size_by.plot.bar()
# %%
reindex_size_by.plot.barh()
# %%
reindex_size_by.plot.pie()

# %%
size_by_country = reversed_df.groupby("Country").size()
size_by_country.head()
#%%
size_by_country.plot.pie()
# %%
size_by_country.nlargest(20).plot.pie()
# %%
languages = reversed_df["LanguageHaveWorkedWith"].str.split(';',
                                                            expand=True)
print(languages)

# %%
languages.head()
# %%
size_by_language = languages.stack().value_counts()
size_by_language.head()
# %%

size_by_language.plot.pie()
# %%
size_by_language.nlargest(10).plot.pie()
# %%
