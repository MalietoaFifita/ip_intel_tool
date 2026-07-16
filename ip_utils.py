"""
validate IP

helper functions
"""

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