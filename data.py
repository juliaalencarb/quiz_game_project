import requests

PARAMETERS = {
    "amount": 10,
    "type": "boolean",
    "category": 9,
}
API_URL = "https://opentdb.com/api.php"

response = requests.get(url=API_URL, params=PARAMETERS)
response.raise_for_status()

data = response.json()

question_data = data['results']
