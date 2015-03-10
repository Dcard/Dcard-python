import requests
import json

login_url = 'https://www.dcard.tw/api/member/login'
user_agent = 'Dcard Python'


class Dcard:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.Session()

        self.__getToken()
        self.__login()

    def __getToken(self):
        # get xsrf token
        res = self.session.get(login_url)
        token = res.cookies['XSRF-TOKEN']

        # update session's cookie
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': user_agent,
            'X-XSRF-TOKEN': token,
        }
        self.session.headers.update(headers)

    def __login(self):
        data = {
            'user': self.username,
            'password': self.password,
        }
        self.session.post(login_url, data=json.dumps(data))
        self.session.headers.update({
            'Content-Type': 'text/plain'})
