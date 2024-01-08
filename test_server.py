import requests

if __name__ == '__main__':
    print(requests.get("http://127.0.0.1:9999/items?count=20").json())
