import requests
import pandas as pd
import json

headers = {'Accept': 'application/json'}

r = requests.get('https://odegdcpnma.execute-api.eu-west-2.amazonaws.com/development/prices?dno=10&voltage=HV&start=01-06-2021&end=03-06-2021',
                 params={}, headers=headers)

data_dict = r.json()
data_df = pd.DataFrame(data_dict['data']['data']).head(48)
data_df = data_df[['Overall', 'Timestamp']]

data_df.rename(columns={'Overall': 'Price'}, inplace=True)
data_df['Timestamp'] = data_df['Timestamp'].apply(lambda x: x[:5])


data_dict = data_df.to_dict(orient='records')

data_json = { 'priceData' : data_dict}

with open("../../web-app/src/mock-data/priceData.json", "w") as outfile:
	json.dump(data_json, outfile)

