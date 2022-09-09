import requests
from urllib.parse import urlsplit
import os
from dotenv import load_dotenv
import sys


def shorten_link(token, url):
    bitlink = requests.post('https://api-ssl.bitly.com/v4/bitlinks',
                            headers={'Authorization': f'Bearer {token}'},
                            json={'long_url': url})
    bitlink.raise_for_status()
    return bitlink.json()['link']


def count_clicks(token, url):
    parsed_url = urlsplit(url)
    bitlink = f'{parsed_url.netloc}{parsed_url.path}'
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks/'
    clicks_count = requests.get(f'{api_url}{bitlink}/clicks/summary',
                                headers={'Authorization': f'Bearer {token}'})
    clicks_count.raise_for_status()
    return clicks_count.json()['total_clicks']


def is_bitlink(url, token):
    parsed_url = urlsplit(url)
    bitlink = f'{parsed_url.netloc}{parsed_url.path}'
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks/'
    bitlink_info = requests.get(f'{api_url}{bitlink}',
                                headers={'Authorization': f'Bearer {token}'})
    return bitlink_info.ok


def main():
    load_dotenv()
    token = os.getenv('BITLY_TOKEN')
    if len (sys.argv) > 1:
        input_url = sys.argv[1]
    else:
        input_url = input('Введите URL: ')
    try:
        if is_bitlink(input_url, token):
            print('Количество кликов:', count_clicks(token, input_url))
        else:
            print('Битлинк:', shorten_link(token, input_url))
    except requests.exceptions.HTTPError as error:
        print(f'Ошибка:\n{error}')


if __name__ == '__main__':
    main()
