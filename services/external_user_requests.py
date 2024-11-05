import os
from dotenv import load_dotenv
import requests

load_dotenv()

def getUserIdFromAPI(discordId):
    userIdResponse = requests.request('GET', os.getenv('BACKEND_API_URL') + '/users/getUserByDiscord/' + str(discordId))
    print(userIdResponse.json())
    return userIdResponse.json().get('id')

