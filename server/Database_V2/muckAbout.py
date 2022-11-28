from datetime import datetime
import datetime as dt

today = datetime.now()
yesterday = today - dt.timedelta(days=1)

print(today > yesterday)