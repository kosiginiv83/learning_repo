import json
import requests
import time
from typing import Iterable
from tqdm import tqdm
from socket import timeout

"""
Макимальное количество друзей, у которых могут совпадать
группы с исследуемым пользователем.
"""
MATCH = 3

VERSION = '5.68'

with open('info.json', encoding='utf-8') as f:
    data = json.load(f)
    TOKEN = data[0]['token']
    USER_ID = data[0]['user_id']


class LinkedListNode:
    
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self, values: Iterable):
        previous = None
        self.head = None
        for value in values:
            current = LinkedListNode(value)
            if previous:
                previous.next = current
            self.head = self.head or current
            previous = current
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next


class Users:
    
    def __init__(self, user_id):
        self.user_id = user_id
        params = {
            'v': VERSION,
            'user_id': user_id,
            'access_token': TOKEN,
        }
        try:
            response = requests.get("https://api.vk.com/method/groups.get",
                                    params)
        except timeout:
            time.sleep(5)
        except:
            time.sleep(2)
        data = response.json()
        if 'response' in data:
            self.user_groups = data['response']['items']
            self.groups_count = len(self.user_groups)
        else:
            self.user_groups = 'None'
            self.groups_count = 'None'
        
        if user_id == USER_ID:
            try:
                response = requests.get("https://api.vk.com/method/friends.get",
                                        params)
            except timeout:
                time.sleep(5)
            except:
                time.sleep(2)
            data = response.json()
            self.user_friends = data['response']['items']
            self.friends_count = len(self.user_friends)


def main():
    user = Users(USER_ID)
    user_friends_ids = LinkedList(user.user_friends)
    friends_groups_ids = []
    current = user_friends_ids.head
    print('\nПолучение групп друзей:')
    with tqdm(total=user.friends_count, mininterval=0.5) as pbar:
        while current:
            try:
                friend = Users(current.data)
                friends_groups_ids += friend.user_groups
                current = current.next
                pbar.update()
            except timeout:
                time.sleep(5)
            except:
                time.sleep(2)
    secret_groups_list = []
    for group_id in user.user_groups:
        if friends_groups_ids.count(group_id) <= MATCH:
            secret_groups_list.append(group_id)
    user_groups_ids_link_list = LinkedList(secret_groups_list)
    
    groups_list = []
    current = user_groups_ids_link_list.head
    print('Получение данных по секретным группам:')
    with tqdm(total=len(secret_groups_list), mininterval=0.5) as pbar:
        while current:
            try:
                group_dict = {}
                params = {
                    'v': VERSION,
                    'access_token': TOKEN,
                    'group_id': current.data,
                    'fields': 'members_count',
                }
                response = requests.get("https://api.vk.com/method/groups.getById",
                                        params)
                data = response.json()
                group_dict['gid'] = data['response'][0]['id']
                group_dict['name'] = data['response'][0]['name']
                if 'deactivated' in data['response'][0]:
                    group_dict['members_count'] = 'group banned'
                elif 'members_count' in data['response'][0]:
                    group_dict['members_count'] = data['response'][0]['members_count']
                else:
                    group_dict['members_count'] = 'Not available'
                groups_list.append(group_dict)
                current = current.next
                pbar.update()
            except timeout:
                time.sleep(5)
            except:
                time.sleep(2)
    
    with open('groups.json', 'w', encoding='utf-8') as f:
        json.dump(groups_list, f, sort_keys=True,
                  indent=2, ensure_ascii=False)
    print("\n\tЗапись в файл выполнена.")


if __name__ == '__main__':
    try:
        main()
    except:
        print("\tAn Error Occured")
        raise