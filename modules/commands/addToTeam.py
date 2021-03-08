import requests
from discord.utils import get
from get_enviroment import API_URL, headers
from modules.commands.utils import get_user_info


class AddToTeam:

    def __init__(self, channel, author, message, users):
        self.channel = channel
        self.author = author
        self.users = users
        self.team_name = message

    async def apply(self):
        role = get(self.author.roles, name=self.team_name)
        if role is None:
            await self.channel.send("You are not in this team")
            return
        data = {
            "team_name": self.team_name,
            "checked_in": True
        }
        for user in self.users:
            if get_user_info(user.id, 'team_name') == "":
                await user.add_roles(role)
                requests.put("%s%s/" % (API_URL, str(user.id)), headers=headers, data=data)
                await self.channel.send("%s has joined the team!" % user.name)
            else:
                await self.channel.send("The user %s has a team already" % user.name)
