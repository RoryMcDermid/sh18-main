import requests
import pandas as pd

headers = {'Accept': 'application/json'}

r = requests.get('https://odegdcpnma.execute-api.eu-west-2.amazonaws.com/development/prices?dno=10&voltage=HV&start=01-06-2021&end=03-06-2021',
                 params={}, headers=headers)

data_dict = r.json()
data_df = pd.DataFrame(data_dict['data']['data'])

data_array = data_df[['Overall', 'Timestamp']].values

print(data_array)

print('hello')
