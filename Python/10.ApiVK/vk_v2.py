import requests
import sys
from functools import reduce

VERSION = '5.68'
TOKEN = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
USER_ID = 2515220000


def get_data(user_id, query):
    params = {
        'v': VERSION,
        'user_id': user_id,
        'access_token': TOKEN
    }
    response = requests.get(f"https://api.vk.com/method/{query}.get", params)
    return response.json()


def user_fio(friend_info):
    user_firstname = friend_info['response'][0]['first_name']
    user_lastname = friend_info['response'][0]['last_name']
    fio = f"{user_lastname} {user_firstname}"
    return fio


if __name__ == '__main__':
    try:
        my_friends = get_data(USER_ID, 'friends')
        my_friends_id_list = my_friends['response']['items']
    except KeyError:
        print("Ошибка:", my_friends['error']['error_msg'])
        request_params = my_friends['error']['request_params']
        print("Метод:", [x['value'] for x in request_params if
                         x['key'] == 'method'][0])
    except:
        print('Unexpected error:', sys.exc_info())

    else:
        friends_friends_list = []
        print("\n\tИмена друзей:")
        for friend_id in my_friends_id_list:
            user_status = '- OK'
            try:
                friend_info = get_data(friend_id, 'users')
                my_friend_friends = get_data(friend_id, 'friends')
                friends_friends_list.append(set(my_friend_friends['response']['items']))
            except KeyError:
                user_status = f"- {my_friend_friends['error']['error_msg']}"
            except:
                print('Unexpected error:', sys.exc_info())
            finally:
                print(user_fio(friend_info), user_status)
        
        print('\n\tОбщие друзья друзей:')
        try:
            inter = reduce(friends_friends_list[0].intersection, friends_friends_list[1:])
            for user_id in inter:
                user = get_data(user_id, 'users')
                print(user_fio(user))
        except IndexError:
            print("Совпадений нет. Проверьте правильность id исследуемого пользователя.")
        except:
            print('Unexpected error:', sys.exc_info())