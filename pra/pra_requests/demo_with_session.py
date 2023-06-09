import requests

url = "http://httpbin.org/get"

with requests.Session() as s:
    s.headers.update({"user-agent": "lsp"})
    r = s.get(url)
    print(r.text)


