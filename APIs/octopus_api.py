import requests

res = requests.get(
    "https://api.octopus.energy/v1/products/",
    params={"is_restricted": False},
)

res_json = res.json()

print(res_json)

for result in res_json["results"]:
    print(result)

