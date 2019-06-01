import requests
from functools import reduce

VERSION = '5.68'
TOKEN = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
USER_ID = 2515220000


def get_friends(user_id):
    params = {
        'v': VERSION,
        'user_id': user_id,
        'access_token': TOKEN
    }
    response = requests.get('https://api.vk.com/method/friends.get', params)
    return response.json()


def get_user(user_id):
    params = {
        'v': VERSION,
        'user_id': user_id,
        'access_token': TOKEN
    }
    response = requests.get('https://api.vk.com/method/users.get', params)
    return response.json()


def user_fio(friend_info):
    user_firstname = friend_info['response'][0]['first_name']
    user_lastname = friend_info['response'][0]['last_name']
    fio = f"{user_lastname} {user_firstname}"
    print(fio)
    return fio


if __name__ == '__main__':
    my_friends = get_friends(USER_ID)
    response_type = list(my_friends.keys())[0]

    if response_type == 'response':
        my_friends_id_list = my_friends['response']['items']
        
        friends_friends_dict = {}
        print("\n\tИмена друзей:")
        for friend_id in my_friends_id_list:
            friend_info = get_user(friend_id)
            if list(friend_info.keys())[0] == 'response':
                my_friend_friends = get_friends(friend_id)
                fio = user_fio(friend_info)
                if list(my_friend_friends.keys())[0] == 'response':
                    friends_friends_dict[fio] = set(my_friend_friends['response']['items'])
                else:
                    print(my_friend_friends['error']['error_msg'])
            else:
                print("Ошибка:", friend_info['error']['error_msg'])
                request_params = friend_info['error']['request_params']
                print("Метод:", [x['value'] for x in request_params if
                                 x['key'] == 'method'][0])

        if friends_friends_dict:
            print('\n\tОбщие друзья друзей:')
            ids_list = list(friends_friends_dict.values())
            inter = reduce(ids_list[0].intersection, ids_list[1:])
            for user_id in inter:
                user = get_user(user_id)
                user_fio(user)
            
    elif response_type == 'error':
        print("Ошибка:", my_friends['error']['error_msg'])
        request_params = my_friends['error']['request_params']
        print( "Метод:", [x['value'] for x in request_params if
                          x['key'] == 'method'][0] )