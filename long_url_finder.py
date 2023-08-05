import requests


def find_long_url(url):
    try:
        response = requests.head(url, allow_redirects=True)
        long_url = response.url
        return long_url
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
        return None
