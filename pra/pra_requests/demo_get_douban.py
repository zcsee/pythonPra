import requests


def main():
    url_basic = 'https://accounts.douban.com/j/mobile/login/basic'
    url = 'https://www.douban.com/'
    ua_headers = {"user-agent": 'mozilla/4.0 (compatible; msie 8.0; windows nt 6.0; trident/4.0)'}
    data = {
        'ck': '',
        'name': '18682266706',
        'password': 'SZCheng1',
        'remember': 'false',
        'ticket': ''
    }

    s = requests.session()
    s.post(url=url_basic, headers=ua_headers, data=data)
    response = s.get(url=url, headers=ua_headers)
    with open('douban.html', 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    main()