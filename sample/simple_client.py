import requests
params = {'sessionKey': 'nithin k anil', 'format': 'xml', 'platformId': 1}
r = requests.post("http://130.211.138.165:8000/quote", params=params)
print(r.status_code, r.reason)
print(r.text)