# post_calls.py
import requests
from headers import get_headers

def post_data_to_endpoint_1(payload):
    """Send data to API endpoint 1."""
    url = "https://api.example.com/endpoint1"
    response = requests.post(url, headers=get_headers(), json=payload)
    return {"name": "POST /endpoint1", "response": response}

def post_data_to_endpoint_2(payload):
    """Send data to API endpoint 2."""
    url = "https://api.example.com/endpoint2"
    response = requests.post(url, headers=get_headers(), json=payload)
    return {"name": "POST /endpoint2", "response": response}
