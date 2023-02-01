import json
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

def getDataFromDay(df, date):

    return df.loc[pd.to_datetime(df['record_date']).dt.strftime("%m-%d") == f"{date[0]}-{date[1]}"]