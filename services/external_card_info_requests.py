import os
import requests

from dotenv import load_dotenv

load_dotenv()

def postCardInfoSearch(name, setcode, collector_number):
     requestParams = {
         "name": name,
         "set_code": setcode,
         "collector_number": collector_number,
     }
     print(requestParams)
     searchCardResults = requests.request('POST', os.getenv('BACKEND_API_URL') + '/scryfall/search', json=requestParams)
     print(searchCardResults.status_code)
     if searchCardResults.status_code == 200:
         return searchCardResults.json()
     else:
         raise Exception('search card failed')