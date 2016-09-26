import requests
params = {'sessionKey': '9ebbd0b25760557393a43064a92bae539d962103', 'format': 'xml', 'platformId': 1}
r = requests.post("http://127.0.0.1:8000/quote", params=params)
print(r.status_code, r.reason)
print(r.text)