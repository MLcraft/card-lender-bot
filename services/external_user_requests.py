import requests

def getUserIdFromAPI(discordId):
    userIdResponse = requests.request('GET', 'http://localhost:8080/users/getUserByDiscord/' + str(discordId))
    print(userIdResponse.text)
    return userIdResponse.text