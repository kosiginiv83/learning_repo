"""
id исследуемого пользователя вводится в файле info.json
"""

import json
import requests
import sys
import time


VERSION = '5.68'

with open('info.json', encoding='utf-8') as f:
    data = json.load(f)
    TOKEN = data[0]['token']
    USER_ID = data[0]['user_id']


def get_data(user_id, query):
    params = {
        'v': VERSION,
        'user_id': user_id,
        'access_token': TOKEN,
    }
    response = requests.get(f"https://api.vk.com/method/{query}.get", params)
    return response.json()


def get_group_info(group_id):
    params = {
        'v': VERSION,
        'access_token': TOKEN,
        'group_id': group_id,
        'fields': 'members_count',
    }
    response = requests.get("https://api.vk.com/method/groups.getById", params)
    return response.json()


def console_output(*args):
    sys.stdout.write('\r')
    message = args[0]
    count = None
    if len(args) > 1:
        count = args[1]
        t = '|/-\\'
        count = 0 if count == 4 else count
        out = t[count]
        count += 1
        sys.stdout.write(f"{message} {out}")
    else:
        sys.stdout.write(f"{message}")
    sys.stdout.flush()
    return count


def get_friends_groups():
    friends_groups_list = []
    friends_info = get_data(USER_ID, 'friends')
    friends_ids = friends_info['response']['items']
    count = 1
    for friend_id in friends_ids:
        status = 'error'
        while status != 'ok':
            try:
                friend_groups_raw = get_data(friend_id, 'groups')
                count = console_output("Получение данных с ВК:", count)
                if 'response' in friend_groups_raw:
                    friend_groups_ids = friend_groups_raw['response']['items']
                    friends_groups_list += friend_groups_ids
                status = 'ok'
            except:
                status = 'error'
                time.sleep(2)
    friends_groups_set = set(friends_groups_list)
    return friends_groups_set


def main():
    groups_list = []
    user_groups_raw = get_data(USER_ID, 'groups')
    user_groups_set = set(user_groups_raw['response']['items'])
    friends_groups_set = get_friends_groups()
    user_groups_set.difference_update(friends_groups_set)
    console_output("Получение данных с ВК: выполнено.\n")
    count = 1
    for group_id in user_groups_set:
        status = 'error'
        while status != 'ok':
            try:
                count = console_output("Обработка данных и запись в файл:",
                                       count)
                group_dict = {}
                group_info = get_group_info(group_id)
                group_dict['gid'] = group_info['response'][0]['id']
                group_dict['name'] = group_info['response'][0]['name']
                if 'deactivated' in group_info['response'][0]:
                    group_dict['members_count'] = 'group banned'
                elif 'members_count' in group_info['response'][0]:
                    group_dict['members_count'] = group_info['response'][0]\
                                                ['members_count']
                else:
                    group_dict['members_count'] = 'Not available'
                groups_list.append(group_dict)
                status = 'ok'
            except:
                status = 'error'
                time.sleep(2)
    with open('groups.json', 'w', encoding='utf-8') as f:
        json.dump(groups_list, f, sort_keys=True,
                  indent=2, ensure_ascii=False)
    console_output("Обработка данных и запись в файл: выполнено.\n")


if __name__ == '__main__':
    try:
        main()
    except:
        print("\tAn Error Occured")
        raise
