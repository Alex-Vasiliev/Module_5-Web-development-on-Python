# https://www.pexels.com/ru-ru/
import requests


def search_pictures(api_key, search):
    try:
        url = "https://api.pexels.com/v1/search"
        headers = {'Authorization': f'{api_key}'}
        params = {'query': f'{search}'}
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        response.raise_for_status()

        if data['photos']:
            pictures_url = data["photos"][0]["src"]["original"]
            pictures = requests.get(pictures_url)
            name_photo = input("Please enter the name of the photo: ").strip()

            if name_photo:
                with open(f'{name_photo}.jpg', 'wb') as i:
                    i.write(pictures.content)

                print(f"Picture saved as {name_photo}")
            else:
                print("Invalid input. Please enter a valid name.")
                return

        else:
            print("No pictures were found.")

    except requests.exceptions.HTTPError as err:
        print("!" * 50)
        print(f"HTTP request error: {err}")
        print("!" * 50, "\n")
    except requests.exceptions.RequestException as err:
        print("!" * 50)
        print(f"Request error: {err}")
        print("!" * 50, "\n")
    except Exception as err:
        print("!" * 50)
        print(f"Unexpected error: {err}")
        print("!" * 50, "\n")


with open("API.txt", "r") as key:
    key.seek(43)
    api_key = key.readline()
search = input("Enter a topic for your search: ").strip()
if search:
    search_pictures(api_key, search)
else:
    print("No search subject entered")

