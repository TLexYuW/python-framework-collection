import requests

if __name__ == "__main__":
    print(requests.get("http://127.0.0.1:9999/item?count=20").json())

    print("")

    print(requests.get("http://127.0.0.1:9999/item?category=tools").json())

    print("")

    print(requests.get("http://127.0.0.1:9999/item/1").json())

    print("")

    print(requests.get("http://127.0.0.1:9999/item?name=Hammer").json())

    print("")

    print(requests.get("http://127.0.0.1:9999/item?category=ingredient").json())

    print("")

    print(requests.get("http://127.0.0.1:9999/items/?count=Hello").json())

    print("")

    print(
        requests.post(
            "http://127.0.0.1:9999/item",
            json={
                "name": "Screwdriver",
                "price": 3.99,
                "count": 200,
                "id": 3,
                "category": "tools",
            },
        ).json()
    )

    print("")

    print(requests.get("http://127.0.0.1:9999/item/list").json())
