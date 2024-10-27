import requests

def postCardInfoSearch(name, setcode, collector_number):
     requestParams = {
         "name": name,
         "set_code": setcode,
         "collector_number": collector_number,
     }
     print(requestParams)
     searchCardResults = requests.request('POST', 'http://localhost:8080/scryfall/search', json=requestParams)
     print(searchCardResults.status_code)
     if searchCardResults.status_code == 200:
         return searchCardResults.json()
     else:
         raise Exception('lend card failed')