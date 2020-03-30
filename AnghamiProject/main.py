import requests
import pprint


#https://bus.anghami.com/public/song/data?song_id=59353178
#My id:68184704
#Yara's id:73758790

headers1 = {'XAT': 'interns', 'XATH' : 'c497b2f056036c83f176a691'}
relation_URL = 'https://bus.anghami.com/public/relations'

def max_and_index(list):
    max_elem = 0
    index = 0
    for i in range(list):
        if list[i] > max_elem:
            max_elem = list[i]
            index = i
    return (max_elem,index)

def best_match(id): #Find the user that has the closest match

    user = str(id)

    request = relation_URL + '?requested_user_id=' + user

    friendlist = requests.get(request, headers = headers1)

    followed_users = friendlist.json()['following']

    max = 0
    best_match = followed_users[0]
    second_best_match = followed_users[0]

    for i in range(len(followed_users)):

        if followed_users[i]['music_match'] > max:
            second_best_match = best_match
            best_match = followed_users[i]
            max = followed_users[i]['music_match']

    return (best_match,second_best_match)


def FR(user): #Friend recommender

    best_friend = str(best_match(user)[0]['user_id'])
    recommendation = best_match(best_friend)[0]
    if  str(recommendation['user_id']) == user:
        recommendation = best_match(best_friend)[1]  #If the user and the best match are mutual best matches, the recommender will just return the initial user. Here we account for this by returning the second best match instead.

    name = recommendation['first_name'] + ' ' + recommendation['last_name']
    message = "We think that you would enjoy following " + name
    return message


user = str(input("Please enter your user ID:"))

print(FR(user))


