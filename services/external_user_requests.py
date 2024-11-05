import os
from dotenv import load_dotenv
import requests

load_dotenv()

def getUserIdFromAPI(discord_id):
    user_id_response = requests.request('GET', os.getenv('BACKEND_API_URL') + '/users/getUserByDiscord/' + str(discord_id))
    print(user_id_response.json())
    return user_id_response.json().get('id')

def getDiscordIdFromAPI(user_id):
    user_id_response = requests.request('GET', os.getenv('BACKEND_API_URL') + '/users/getDiscordByUser/' + str(user_id))
    print(user_id_response.json())
    return user_id_response.json().get('id')

