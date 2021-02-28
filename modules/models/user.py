import requests
from get_enviroment import API_URL, headers
from modules.commands.utils import get_team_name


class User:

    def __init__(self, name, userid, roles):
        self.name = name
        self.id = userid
        self.roles = roles
        self.team = get_team_name(userid)
        self.is_in_team = self.team is not None

    def save(self):
        data = {'checked_in': True}
        response = requests.put("%s%s/" % (API_URL, str(self.id)), headers=headers, data=data)
        print(response.json())

    def connect(self):
        print(self)
        print('Get info')
