"""
make HTTP request

return JSON
"""
import requests

def fetch_ip_data(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    return response.json()
