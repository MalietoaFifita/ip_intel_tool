"""
validate IP

helper functions
"""

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