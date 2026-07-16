"""
format output

color

summary
"""

#ANSI color escape codesGREEN = "\033[92m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

#function used to extract data from the json and put it into a dictionary format for python use
def extract_data(data):
    return {
        "ip" : data.get("query"),
        "status" : data.get("status"),
        "country" : data.get("country"),
        "city" : data.get("city"),
        "isp" : data.get("isp"),
        "org" : data.get("org"),
        "timezone" : data.get("timezone"),
        "latitude" : data.get("lat"),
        "longitude" : data.get("lon")
    }

#function used to print data from the dictionary object and format the data into a user friendly way
def print_report(fields):
    print("++++++++++++++++++++++++++++++++++++++++++++++")
    print("+                                            +")
    print("+                 REPORT                     +")
    print("+                                            +")
    print("++++++++++++++++++++++++++++++++++++++++++++++")

    if fields["status"] != "success":
        print(f"{RED}IP lookup {fields['status']}. IP invalid or unreachable{RESET}")
        return
    
    print(f"{GREEN}IP: {fields['ip']}{RESET}")
    print(f"Country: {fields['country']}")
    print(f"City: {fields['city']}")
    print(f"Internet Service Provider: {fields['isp']}")
    print(f"Organization: {fields['org']}")
    print(f"TimeZone: {fields['timezone']}")
    print(f"Latitude and Longitude: {fields['latitude']} , {fields['longitude']}")

