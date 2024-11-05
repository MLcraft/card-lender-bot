import os
import requests

from dotenv import load_dotenv

load_dotenv()

def postCardInfoSearch(name, setcode, collector_number):
     request_params = {
         "name": name,
         "set_code": setcode,
         "collector_number": collector_number,
     }
     print(request_params)
     search_card_results = requests.request('POST', os.getenv('BACKEND_API_URL') + '/scryfall/search', json=request_params)
     print(search_card_results.status_code)
     if search_card_results.status_code == 200:
         return search_card_results.json()
     else:
         raise Exception('search card failed')