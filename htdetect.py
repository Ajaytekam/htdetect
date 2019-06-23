#!/usr/bin/python3

import requests
import sys
from threading import Thread

def CheckSchema(url):
    header={"Connection":"close"}
    try:
        http = requests.get("http://"+url, headers=header, timeout=4)
        print("http://"+url)
    except:
        pass
    try:
        https = requests.get("https://"+url, headers=header, timeout=4) 
        print("https://"+url)
    except:
        pass
    
if __name__ == "__main__":
    while True:
        try:
            base_url=input()
            url = str(base_url.strip('\n'))
            t = Thread(target=CheckSchema, args=(url,))
            child = t.start()
        except EOFError:
            t.join()
            sys.exit() 
