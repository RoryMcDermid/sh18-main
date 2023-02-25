import datetime as dt
import numpy as np
import pandas as pd


def get_group_info(date_string):
    date = dt.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")
    month = date.month
    day_of_week = date.weekday()
    return month, day_of_week


def get_average_from_group(dataset, date_string):
    month, day_of_week = get_group_info(date_string)

    df = pd.DataFrame(dataset, columns=["timestamp", "energy_usage"])
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    df["month"] = df["timestamp"].dt.month
    df["day_of_week"] = df["timestamp"].dt.dayofweek

    group_df = df.loc[(df["month"] == month) & (df["day_of_week"] == day_of_week)]

    result = group_df["energy_usage"].to_numpy()
    result = result.reshape(-1, 96)
    average = np.mean(result, axis=0)
    return average.tolist()
