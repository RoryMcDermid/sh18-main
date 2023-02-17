import datetime
import numpy as np

# turns (96,) 2d array into [(isoTime, reading),(isoTime, reading),...(isoTime, reading)]
# time will be today's real time, starting from 00:00


def formatPlotData(dataset) -> np.array:
    start_time = datetime.datetime.now(tz=datetime.timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    time_points = [start_time + datetime.timedelta(minutes=15 * i) for i in range(96)]
    data = np.zeros(96)
    time_list = [time.isoformat() for time in time_points]
    data_list = [float(value) for value in data]
    chart_data = list(zip(time_list, data_list))

    return chart_data
