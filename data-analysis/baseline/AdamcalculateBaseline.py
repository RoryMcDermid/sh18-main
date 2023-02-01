import json
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from helpers.getDataFromDay import *


with open('data/single_sensor.json', 'r') as f:
    data = json.load(f) 

df = pd.DataFrame(data)

df['values'] = df['values'].map(lambda x: x['pulse_count'])

df['record_date'] = pd.to_datetime(df['record_date'])

unique_dates = [(x.strftime("%m"),y.strftime("%d")) for x,y in zip(df['record_date'].dt.date.unique(), df['record_date'].dt.date.unique())]

for date in unique_dates:
    x = getDataFromDay(df, date)
    print(x)
