#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import urllib.request
import json

URL= "https://opentdb.com/api.php?amount=10&type=boolean"
def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()

## Call the webservice with our key
    apodurlobj = urllib.request.urlopen(URL)

    ## read the file-like object
    apodread = apodurlobj.read()

    ## decode JSON to Python data structure
    apod = json.loads(apodread.decode("utf-8"))

    ## display our Pythonic data
    print(apod)

if __name__ == "__main__":
    main()
