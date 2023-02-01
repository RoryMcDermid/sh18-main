import json
import pandas as pd
import matplotlib.pyplot as plt


with open('data/single_sensor.json', 'r') as f:
    data = json.load(f) 

df = pd.DataFrame(data)

df['values'] = df['values'].map(lambda x: x['pulse_count'])

df['record_date'] = pd.to_datetime(df['record_date'])

# print(df.head)

date = '2022-02-02'
day_df = df[df['record_date'].dt.date == pd.to_datetime(date).date()]
unique_dates = df['record_date'].dt.date.unique()
print(len(unique_dates))