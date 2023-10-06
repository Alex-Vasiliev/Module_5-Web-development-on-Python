import requests
import json


def get_json_response(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        response_json = response.json()
        return response_json

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")


api_url = "https://jsonplaceholder.typicode.com/todos/1"
json_response = get_json_response(api_url)
print(json.dumps(json_response, indent=3))
