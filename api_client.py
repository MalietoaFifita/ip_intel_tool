"""
make HTTP request

return JSON
"""
import requests

#Fetches Ip data from ip-api.com using the request module from python
def fetch_ip_data(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    return response.json()
