import requests
responce=requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
print(responce.json())
