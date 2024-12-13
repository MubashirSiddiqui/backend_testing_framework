# get_calls.py
import requests
from headers import get_headers

def get_data_from_endpoint_1():
    """Fetch data from API endpoint 1."""
    url = "https://api.example.com/endpoint1"
    response = requests.get(url, headers=get_headers())
    return {"name": "GET /endpoint1", "response": response}

def get_data_from_endpoint_2():
    """Fetch data from API endpoint 2."""
    url = "https://api.example.com/endpoint2"
    response = requests.get(url, headers=get_headers())
    return {"name": "GET /endpoint2", "response": response}
