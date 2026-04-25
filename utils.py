import time
import requests

class NetworkError(Exception):
    pass

def retry_request(method, url, retries=3, delay=1, **kwargs):
    for attempt in range(retries):
        try:
            response = requests.request(method, url, **kwargs)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise NetworkError(f'Request failed after {retries} attempts: {e}') from e
