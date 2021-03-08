import requests
from discord.utils import get
from get_enviroment import API_URL, headers
from modules.commands.utils import get_bits_server


class User:

    def __init__(self, member, client):
        self.guild = get_bits_server(client)
        self.user = member

    # Check in user + add roles
    async def save(self):
        data = {'checked_in': True}
        response = requests.put("%s%s/" % (API_URL, str(self.user.id)), headers=headers, data=data)

        type_role = get(self.guild.roles, name=response.json()['type'])
        team_role = get(self.guild.roles, name=response.json()['team_name'])
        if type_role is not None:
            await self.user.add_roles(type_role)
        if team_role is not None:
            await self.user.add_roles(team_role)
        print(response.json())
