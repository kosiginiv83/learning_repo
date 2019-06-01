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
            print('Error:', response.json()['errors'][0]['message'])
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
        print('====================Количество визитов========================')
        return response

    @property
    def get_users(self):
        params = {
            'id': counter_id,
            'metrics': 'ym:s:users',
            'oauth_token': self.token,
        }
        response = requests.get('https://api-metrika.yandex.ru/stat/v1/data', params)
        print('=============Количество уникальных посетителей================')
        return response

    @property
    def get_pageviews(self):
        params = {
            'id': counter_id,
            'metrics': 'ym:s:pageviews',
            'oauth_token': self.token,
        }
        response = requests.get('https://api-metrika.yandex.ru/stat/v1/data', params)
        print('===============Количество просмотров страниц==================')
        return response

    @property
    def get_mobilePercentage(self):
        params = {
            'id': counter_id,
            'metrics': 'ym:s:mobilePercentage',
            'oauth_token': self.token,
        }
        response = requests.get('https://api-metrika.yandex.ru/stat/v1/data', params)
        print('===========Процент использования мобильных устройств==========')
        return response


class Users(YMManagement, Counter):
    pass


try:
    user_1 = Users(TOKEN)
    counters = user_1.get_counters()
    print("ID счетчиков:", *counters)
    queries = ['get_visits', 'get_users', 'get_pageviews', 'get_mobilePercentage']

    for counter_id in counters:
        print('\n==================Информация о счетчике=======================')
        try:
            counter_info = user_1.get_counter_info(counter_id)
            print(counter_info['counter']['site'])
            print("ID счетчика:", counter_id)
            for query in queries:
                exec (f"response = user_1.{query}")
                data = response.json()
                print(f"За период c {data['query']['date1']} по {data['query']['date2']}")
                print("Минимум:", round(data['min'][0]))
                print("Максимум:", round(data['max'][0]))
                print("Всего:", round(data['totals'][0]))
        except KeyError:
            print('Error:', data['errors'][0]['message'])
        except:
            print('Unexpected error:', sys.exc_info()[1])
            
except TypeError:
    pass
except:
    print('Unexpected error:', sys.exc_info()[1])