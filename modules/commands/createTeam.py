from discord.utils import get
from modules.commands.utils import create_channel_rol, get_bits_server
from modules.services.api import Api
from get_enviroment import DISCORD_ORGANIZER_ROLE_NAME


class CreateTeam:

    def __init__(self, channel, author, message, user, client):
        self.channel = channel
        self.author = author
        self.user = user
        self.team_name = message
        self.guild = get_bits_server(client)
        self.api = Api()

    async def apply(self):
        if get(self.author.roles, name=DISCORD_ORGANIZER_ROLE_NAME) is None:
            await self.channel.send("You have no permissions to create a new team. Contact an organizer")
            return
        try:
            user_info = self.api.get_user_info(self.user.id, 'team_name')
            if user_info == "":
                self.api.create_new_team(self.user.id, self.team_name)
                team_role = await create_channel_rol(self.guild, self.team_name)
                await self.user.add_roles(team_role)
                await self.channel.send("Team created!")
            else:
                await self.channel.send("This user has a team already")

        except (self.api.USER_NOT_FOUND, self.api.BAD_REQUEST, self.api.SERVER_ERROR) as e:
            await self.channel.send(e.message)
