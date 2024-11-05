import os
from dotenv import load_dotenv
import requests

load_dotenv()

def postLendCardFromOwnerToUser(ownerId, borrowerId, cardId, count):
     requestParams = {
         "owner_id": ownerId,
         "borrower_id": borrowerId,
         "card_id": cardId,
         "count": count
     }
     lendCardResponse = requests.request('POST', os.getenv('BACKEND_API_URL') + '/lending/lend', json=requestParams)
     print(lendCardResponse.status_code)
     if lendCardResponse.status_code == 200:
         return lendCardResponse.text
     else:
         raise Exception('lend card failed')

def postReturnCardFromUserToOwner(ownerId, borrowerId, cardId, count):
    requestParams = {
        "owner_id": ownerId,
        "borrower_id": borrowerId,
        "card_id": cardId,
        "count": count
    }
    lendCardResponse = requests.request('POST', os.getenv('BACKEND_API_URL') + '/lending/return', json=requestParams)
    print(lendCardResponse.status_code)
    if lendCardResponse.status_code == 200:
        return lendCardResponse.text
    else:
        raise Exception('lend card failed')

def getListCardsLentByOwner(ownerId):
    lentCardsResponse = requests.request('GET', os.getenv('BACKEND_API_URL') + '/lending/lentCards/' + str(ownerId))
    print(lentCardsResponse.status_code)
    if lentCardsResponse.status_code == 200:
        print(lentCardsResponse.json())
        return lentCardsResponse.json()
    else:
        raise Exception('getListCardsLentByOwner failed')


def getListCardsBorrowedByUser(borrowerId):
    borrowedCardsResponse = requests.request('GET', os.getenv('BACKEND_API_URL') + '/lending/borrowedCards/' + str(borrowerId))
    print(borrowedCardsResponse.status_code)
    if borrowedCardsResponse.status_code == 200:
        print(borrowedCardsResponse.json())
        return borrowedCardsResponse.json()
    else:
        raise Exception('getListCardsBorrowedByUser failed')