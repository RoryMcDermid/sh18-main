import requests
import numpy as np
import datetime as dt
def getWholesaleEnergyPrice(start_date, end_date):

    headers ={
        'Accept': 'application/json'
    }

    r = requests.get(f'https://odegdcpnma.execute-api.eu-west-2.amazonaws.com/development/prices?dno=10&voltage=HV&start={start_date}&end={end_date}', 
                    params={}, headers = headers)

    r = r.json()["data"]["data"]
    time = np.repeat([dt.datetime.strptime(x["Timestamp"], "%H:%M %d-%m-%Y") for x in r[:-1]], 2)
    price = np.repeat([x["Overall"] for x in r[:-1]], 2)
    
    time[1::2] += dt.timedelta(minutes=15)
    num_of_days = len(time) // 96
    time_price = np.column_stack((time, price)).reshape(num_of_days, 96, 2)
    
    return time_price

getWholesaleEnergyPrice("12-02-2023", "15-02-2023")   
 


