"""
CLI input

call API client

call report generator
"""
from api_client import fetch_ip_data
from ip_utils import valid_ip
from report import extract_data, print_report

#while loop to continue to ask user for an IP they would like to pull data on. If the IP is invalid using the validation function from utils, then it will prompt the user to for an IP again
#uses the fetch_ip_data function to get the data on that ip
while True:

    ip = input("Enter ip: ")
    if not valid_ip(ip):
        print("Sorry that is not a valid ip")
        continue

    data = fetch_ip_data(ip)
    fields = extract_data(data)
    print_report(fields)