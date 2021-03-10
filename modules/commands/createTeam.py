import requests
from discord.utils import get
from get_enviroment import API_URL, headers
from modules.commands.utils import get_user_info, create_channel_rol, get_bits_server


class CreateTeam:

    def __init__(self, channel, author, message, user, client):
        self.channel = channel
        self.author = author
        self.user = user
        self.team_name = message
        self.guild = get_bits_server(client)

    async def apply(self):
        if get(self.author.roles, name='Organizer') is None:
            await self.channel.send("You have no permissions to create a new team. Contact an organizer")
            return

        user_info = get_user_info(self.user.id, 'team_name')
        if user_info is None:
            await self.channel.send("User not found in database")
        elif user_info == "":
            data = {
                "team_name": self.team_name
            }
            requests.put("%s%s/" % (API_URL, str(self.user.id)), headers=headers, data=data)
            team_role = await create_channel_rol(self.guild, self.team_name)
            await self.user.add_roles(team_role)
            await self.channel.send("Team created!")
        else:
            await self.channel.send("This user has a team already")
