from discord.utils import get
from modules.commands.utils import get_bits_server
from modules.services.api import Api


class ChangeTeamName:

    def __init__(self, channel, author, message, client):
        self.channel = channel
        self.guild = get_bits_server(client)
        self.author = author
        self.new_name = message
        self.api = Api()

    async def apply(self):
        try:
            old_name = self.api.get_user_info(self.author.id, 'team_name')
            role = get(self.author.roles, name=old_name)
            if role is None:
                await self.channel.send("Sync error. Contact an organizer")
                return
            if get(self.guild.roles, name=self.new_name) is not None:
                await self.channel.send("There is already a team with name: %s" % self.new_name)
                return
            text_channel = get(self.guild.text_channels, name=old_name)
            voice_channel = get(self.guild.voice_channels, name=old_name)
            await role.edit(name=self.new_name)
            await text_channel.edit(name=self.new_name)
            await voice_channel.edit(name=self.new_name)
            self.api.change_team_name(self.author.id, self.new_name)
            await self.channel.send("Team name changed!")

        except (self.api.USER_NOT_FOUND, self.api.BAD_REQUEST, self.api.SERVER_ERROR) as e:
            await self.channel.send(e.message)
