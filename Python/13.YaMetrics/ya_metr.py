import requests
import sys
from urllib.parse import urljoin

TOKEN = 'AgAAAAAPYnwKAASbhnF4cBNXWEEQqhdwYnRNcPw'


class YMManagement:
    management_url = 'https://api-metrika.yandex.ru/management/v1/'
    
    def __init__(self, token):
        self.token = token
    
    def get_headers(self):
        headers = {
            'Authorization': f'OAuth {self.token}',
            'Content-Type': 'application/x-yametrika+json',
        }
        return headers
    
    def get_counters(self):
        try:
            url = urljoin(self.management_url, 'counters')
            headers = self.get_headers()
            response = requests.get(url, headers=headers)
            return [c['id'] for c in response.json()['counters']]
        except KeyError:
            print(response.json()['errors'][0]['message'])
        except:
            print('Unexpected error:', sys.exc_info()[1])
    
    def get_counter_info(self, counter_id):
        url = urljoin(self.management_url, f'counter/{counter_id}')
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        return response.json()


class Counter:
    stat_url = 'https://api-metrika.yandex.ru/stat/v1/data'
    
    @property
    def get_visits(self):
        params = {
            'id': counter_id,
            'metrics': 'ym:s:visits',
            'oauth_token': self.token,
        }
        response = requests.get('https://api-metrika.yandex.ru/stat/v1/data', params)
        return response
    
    @property
    def get_users(self):
        params = {
            'id': counter_id,
            'metrics': 'ym:s:users',
            'oauth_token': self.token,
        }
        response = requests.get('https://api-metrika.yandex.ru/stat/v1/data', params)
        return response
    
    @property
    def get_mobilePercentage(self):
        params = {
            'id': counter_id,
            'metrics': 'ym:s:mobilePercentage',
            'oauth_token': self.token,
        }
        response = requests.get('https://api-metrika.yandex.ru/stat/v1/data', params)
        return response
    
    @property
    def get_pageviews(self):
        params = {
            'id': counter_id,
            'metrics': 'ym:s:pageviews',
            'oauth_token': self.token,
        }
        response = requests.get('https://api-metrika.yandex.ru/stat/v1/data', params)
        return response


class Users(YMManagement, Counter):
    pass


try:
    user_1 = Users(TOKEN)
    counters = user_1.get_counters()
    print("ID счетчиков:", counters)
    
    for counter_id in counters:
        counter_info = user_1.get_counter_info(counter_id)
        print('=======================counter_info===============================')
        print(counter_info['counter']['site'])
    
    for counter_id in counters:
        response = user_1.get_visits
        data = response.json()
        print('======================Количество визитов==========================')
        print(f"За период c {data['query']['date1']} по {data['query']['date2']}")
        print("Минимум:", round(data['min'][0]))
        print("Максимум:", round(data['max'][0]))
        print("Всего:", round(data['totals'][0]))
    
    for counter_id in counters:
        response = user_1.get_users
        data = response.json()
        print('==============Количество уникальных посетителей===================')
        print(f"За период c {data['query']['date1']} по {data['query']['date2']}")
        print("Минимум:", round(data['min'][0]))
        print("Максимум:", round(data['max'][0]))
        print("Всего:", round(data['totals'][0]))
    
    for counter_id in counters:
        response = user_1.get_pageviews
        data = response.json()
        print('================Количество просмотров страниц=====================')
        print(f"За период c {data['query']['date1']} по {data['query']['date2']}")
        print("Минимум:", round(data['min'][0]))
        print("Максимум:", round(data['max'][0]))
        print("Всего:", round(data['totals'][0]))
    
    for counter_id in counters:
        response = user_1.get_mobilePercentage
        data = response.json()
        print('=============Процент использования мобильных устройств============')
        print(f"За период c {data['query']['date1']} по {data['query']['date2']}")
        print("Минимум:", round(data['min'][0]))
        print("Максимум:", round(data['max'][0]))
        print("Всего:", round(data['totals'][0]))
        
except TypeError:
    pass
except:
    print('Unexpected error:', sys.exc_info()[1])