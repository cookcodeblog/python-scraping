import json
from urllib.error import HTTPError
from urllib.request import urlopen


def get_title(post_id):
    url = "https://jsonplaceholder.typicode.com/posts/" + post_id
    try:
        response = urlopen(url).read().decode("utf-8")
        response_json = json.loads(response)
        return response_json.get("title")
    except HTTPError:
        print("Could not find the page.")


print(get_title("1"))
