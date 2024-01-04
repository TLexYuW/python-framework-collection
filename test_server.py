import requests

print("__name__ : " + __name__ )

print(requests.get("http://127.0.0.1:9999/").json())
