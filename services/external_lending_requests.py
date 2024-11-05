import os
from dotenv import load_dotenv
import requests

load_dotenv()

def postLendCardFromOwnerToUser(owner_id, borrower_id, card_id, count):
     request_params = {
         "owner_id": owner_id,
         "borrower_id": borrower_id,
         "card_id": card_id,
         "count": count
     }
     lend_card_response = requests.request('POST', os.getenv('BACKEND_API_URL') + '/lending/lend', json=request_params)
     print(lend_card_response.status_code)
     if lend_card_response.status_code == 200:
         return lend_card_response.text
     else:
         raise Exception('lend card failed')

def postReturnCardFromUserToOwner(owner_id, borrower_id, card_id, count):
    request_params = {
        "owner_id": owner_id,
        "borrower_id": borrower_id,
        "card_id": card_id,
        "count": count
    }
    lend_card_response = requests.request('POST', os.getenv('BACKEND_API_URL') + '/lending/return', json=request_params)
    print(lend_card_response.status_code)
    if lend_card_response.status_code == 200:
        return lend_card_response.text
    else:
        raise Exception('lend card failed')

def getListCardsLentByOwner(owner_id):
    lent_cards_response = requests.request('GET', os.getenv('BACKEND_API_URL') + '/lending/lentCards/' + str(owner_id))
    print(lent_cards_response.status_code)
    if lent_cards_response.status_code == 200:
        print(lent_cards_response.json())
        return lent_cards_response.json()
    else:
        raise Exception('getListCardsLentByOwner failed')


def getListCardsBorrowedByUser(borrower_id):
    borrowed_cards_response = requests.request('GET', os.getenv('BACKEND_API_URL') + '/lending/borrowedCards/' + str(borrower_id))
    print(borrowed_cards_response.status_code)
    if borrowed_cards_response.status_code == 200:
        print(borrowed_cards_response.json())
        return borrowed_cards_response.json()
    else:
        raise Exception('getListCardsBorrowedByUser failed')