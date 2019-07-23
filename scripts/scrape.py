import json
import http.client
from sys import argv


def get_response(function, symbol, outputsize, json, apikey):
    conn = http.client.HTTPSConnection("www.alphavantage.co")
    url = "/query?function=" + function
    url += "&symbol=" + symbol
    url += "&outputsize=" + outputsize
    url += "&apikey=" + apikey
    url += ("&datatype=json" if json else "&datatype=csv")
    print("www.alphavantage.co" + url)
    conn.request("GET", url)
    r1 = conn.getresponse()
    if r1.status != 200:
        return None
    return r1.read().decode('utf-8')

if len(argv)<2:
    print("Needs a argument to download data")
    exit()
function_name=argv[1]
symbol_name=argv[2]
level=argv[3]
print(get_response(function_name, symbol_name, level, True, "key"))
