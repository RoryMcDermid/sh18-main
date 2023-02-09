import pandas as pd
import datetime as dt

def get_data_from_day(df, date):

    return df.loc[pd.to_datetime(df['record_date']).dt.strftime("%m-%d") == f"{date[0]}-{date[1]}"]