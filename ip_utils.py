"""
validate IP

helper functions
"""
from datetime import datetime

#validates an ip by splitting it at the . checks if there are four parts. Then checks each part to make sure they are only digits, then checks to make sure it is between 0 - 255
def valid_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for p in parts:
        if not p.isdigit():
            return False
        if not 0 <= int(p) <= 255:
            return False
        
    return True

def save_report(fields):
    with open("ip_reports.txt", "a") as f:
        timestamp = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
        f.write(f"IP REPORT - {timestamp}\n")
        for key, value in fields.items():
            f.write(f"{key}: {value}\n")
        f.write("\n")