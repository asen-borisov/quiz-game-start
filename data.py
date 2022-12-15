import requests

parms = {
    "amount" : 10,
    "type" : "boolean"
}

result = requests.get(url="https://opentdb.com/api.php", params=parms)
result.raise_for_status()
data = result.json()


question_data = data["results"]



