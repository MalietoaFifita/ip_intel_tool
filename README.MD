Overview
A command line tool where the user will enter an IP and this program will grab real world intelligence on that IP using API's.

Features
- It will pull this data
    - Geolocation
    - ISP
    - Organization
    - Hostname
    - VPN/proxy status
    - Threat score
    - Abuse reports
    - ASN (autonomous system number)
    - Reverse DNS
    - Country/city/timezone

Why I’m building this
It is very common in IT to come across very suspicious websites. It can be time consuming to go to different ip address checkers, this can help automate the process by taking the IPv4 of these suspicious IP's and pull data on them.

APIs used
- ip-api.com
- abuseIP?
- One other IP checker maybe?

How to run
- download and install python 3 on your computer
- ensure you have the requests module on your python
- Download all the files
- navigate the saved files in the command prompt
- run this command
    - python main.py

Future improvements
- Multi-threading?