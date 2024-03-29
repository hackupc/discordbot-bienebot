from time import sleep

from discord.utils import get
from modules.commands.utils import get_bits_server, create_channel_rol
from modules.services.api import Api


class CreateAllTeams:

    def __init__(self, channel, author, client):
        self.channel = channel
        self.author = author
        self.guild = get_bits_server(client)
        self.api = Api()

    async def apply(self):
        # Check if has Admin permission on Top Role
        if not self.author.top_role.permissions.administrator:
            await self.channel.send("You have no permissions to execute this command")
            return
        try:
            all_users = self.api.get_all_users()
            all_teams = [e['team_name'].lower() for e in all_users if e['team_name'].lower() != ""]
            unique_teams = list(set(all_teams))
            for team in unique_teams:
                # Check if role does exist on Discord Server.
                if get(self.guild.roles, name=team) is not None:
                    await self.channel.send("Team %s was already created!" % team)
                else:
                    # create role
                    await create_channel_rol(self.guild, team)
                    await self.channel.send("Team %s created!" % team)
                sleep(1)

        except (self.api.USER_NOT_FOUND, self.api.BAD_REQUEST, self.api.SERVER_ERROR) as e:
            await self.channel.send(e.message)
