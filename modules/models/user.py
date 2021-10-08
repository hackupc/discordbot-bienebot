from discord.utils import get
from modules.commands.utils import get_bits_server
from modules.services.api import Api
from get_enviroment import DISCORD_ORGANIZER_ROLE_NAME


class User:

    def __init__(self, member, client):
        self.guild = get_bits_server(client)
        self.user = member
        self.api = Api()

    # Check in user + add roles
    async def save(self):
        try:
            response = self.api.check_in(self.user.id)
            type_role = get(self.guild.roles, name=response['type'])
            team_role = get(self.guild.roles, name=response['team_name'].lower())
            if type_role is not None:
                await self.user.add_roles(type_role)
            if team_role is not None:
                await self.user.add_roles(team_role)

        except (self.api.USER_NOT_FOUND, self.api.BAD_REQUEST, self.api.SERVER_ERROR):
            await self.user.send("Sync error. Contact an organizer")

    async def apply(self, channel, user):
        if get(user.roles, name=DISCORD_ORGANIZER_ROLE_NAME) is None:
            await channel.send("You have no permissions. Contact an organizer")
            return
        try:
            response = self.api.check_in(self.user.id)
            type_role = get(self.guild.roles, name=response['type'])
            team_role = get(self.guild.roles, name=response['team_name'].lower())
            if type_role is not None:
                await self.user.add_roles(type_role)
            if team_role is not None:
                await self.user.add_roles(team_role)

        except (self.api.USER_NOT_FOUND, self.api.BAD_REQUEST, self.api.SERVER_ERROR):
            await channel.send("Sync error. Contact an organizer")
