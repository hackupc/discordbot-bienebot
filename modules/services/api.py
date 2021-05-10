from get_enviroment import DOMAIN, headers
import requests
from modules.database.decorator import singleton


@singleton
class Api:

    def __init__(self):
        self.headers = headers
        self.api_url = DOMAIN

    def get_user_info(self, userid, param):
        response = requests.get("%s%s%s/" % (self.api_url, "/discord/api/", str(userid)), headers=self.headers)
        response_json = self.check_errors(response)
        if param == 'team_name':
            return response_json['team_name'].lower()
        if param == 'type':
            return response_json['type']
        if param == 'all':
            return response_json

    def get_all_users(self):
        response = requests.get("%s%s" % (self.api_url, "/discord/api/"), headers=self.headers)
        return self.check_errors(response)

    def check_in(self, userid):
        data = {'checked_in': True}
        response = requests.put("%s%s%s/" % (self.api_url, "/discord/api/", str(userid)), headers=self.headers,
                                data=data)
        return self.check_errors(response)

    def change_team_name(self, userid, team_name):
        data = {
            "team_name": team_name,
            "team_changed": True
        }
        response = requests.put("%s%s%s/" % (self.api_url, "/discord/api/", str(userid)), headers=self.headers,
                                data=data)
        return self.check_errors(response)

    def add_member_to_team(self, userid, team_name):
        data = {"team_name": team_name}
        response = requests.put("%s%s%s/" % (self.api_url, "/discord/api/", str(userid)), headers=self.headers,
                                data=data)
        return self.check_errors(response)

    def create_new_team(self, userid, team_name):
        data = {
            "team_name": team_name,
            "team_created": True
        }
        response = requests.put("%s%s%s/" % (self.api_url, "/discord/api/", str(userid)), headers=self.headers,
                                data=data)
        return self.check_errors(response)

    def add_sticker(self, userid, sticker):
        data = {
            "stickers": sticker
        }
        response = requests.put("%s%s%s/" % (self.api_url, "/discord/api/", str(userid)), headers=self.headers,
                                data=data)
        return self.check_errors(response)

    def check_errors(self, response):
        if response.status_code == 404:
            raise self.USER_NOT_FOUND(response.json())
        if response.status_code == 400:
            raise self.BAD_REQUEST(response.json())
        if response.status_code == 500:
            raise self.SERVER_ERROR
        if response.status_code == 200:
            return response.json()

    class BAD_REQUEST(Exception):
        def __init__(self, message):
            self.message = "Error: %s" % message
            super().__init__(self.message)

    class USER_NOT_FOUND(Exception):
        def __init__(self, message):
            self.message = "User not found in database. Error: %s" % message
            super().__init__(self.message)

    class SERVER_ERROR(Exception):
        def __init__(self):
            self.message = "Server error"
            super().__init__(self.message)
