import requests
import time
import os
import sys

def try_request(link, iter = 10):
    
    while iter > 0:
        resp = requests.get(link)
        if resp.status_code == 200:
            return resp
        time.sleep(1)
        iter -= 1
    sys.exit('Server not responding correctly')