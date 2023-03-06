import datetime as dt


def get_midnight(date: dt.datetime) -> dt.datetime:
    return dt.datetime.combine(date, dt.datetime.min.time())
