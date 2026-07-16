"""
CLI input

call API client

call report generator
"""
from api_client import fetch_ip_data
from ip_utils import valid_ip

while True:

    ip = input("Enter ip: ")
    if not valid_ip(ip):
        print("Sorry that is not a valid ip")
        continue

    data = fetch_ip_data(ip)
    print(data)