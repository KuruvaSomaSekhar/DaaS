import requests
params = {'sessionKey': 'appu', 'format': 'xml', 'platformId': 1}
r = requests.post("http://104.198.219.92:8000/quote", params=params)
print(r.status_code, r.reason)
print(r.text)