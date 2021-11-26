import numpy as np
import pandas as pd

data = pd.read_csv('./ObesityDataSet_raw_and_data_sinthetic.csv')
print(min(data['Age']))
print(max(data['Age']))
print(min(data['NCP']))
print(max(data['NCP']))