import requests

get = ['info', 'ticker', 'depth', 'trades']
url = 'https://yobit.net/api/3/'
urls = []
for i in get:
    urls.append(url + i)

coin1: str = 'btc'
coin2: str = 'eth'
coin3: str = 'usdt'


def get_info():
    response = requests.get(url=urls[0])
    with open('info.csv', 'w') as f:
        f.write(response.text)
    return response.text


def get_ticker():
    response = requests.get(url=f'{urls[1]}/{coin2}_{coin1}-{coin1}_{coin3}-{coin2}_{coin3}?ignore_invalid=1')
    with open('ticker.csv', 'w') as f:
        f.write(response.text)
    return response.text


def get_depth(limit=150):
    response = requests.get(url=f'{urls[2]}/{coin2}_{coin1}-{coin1}_{coin3}-{coin2}_{coin3}'
                                f'?limit={limit}&ignore_invalid=1')
    with open('depth.csv', 'w') as f:
        f.write(response.text)
    return response.text


def get_trades(limit=150):
    response = requests.get(url=f'{urls[2]}/'
                                f'{coin2}_{coin1}-{coin1}_{coin3}-{coin2}_{coin3}?limit={limit}&ignore_invalid=1')
    with open('trades.csv', 'w') as f:
        f.write(response.text)
    return response.text


def main():
    get_info()
    get_ticker()
    get_depth()
    get_trades()


if __name__ == '__main__':
    main()
