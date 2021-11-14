import pandas as pd

obesity_df = pd.read_csv("data_processing/ObesityDataSet_raw_and_data_sinthetic.csv")  # Reading preprocessed data
for col in obesity_df:
    if obesity_df[col].dtype == object:
        print(col)
        print(obesity_df[col].unique())