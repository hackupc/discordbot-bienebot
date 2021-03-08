import requests
from discord.utils import get
from get_enviroment import API_URL, headers
from modules.commands.utils import get_bits_server, get_user_info


class ChangeTeamName:

    def __init__(self, channel, author, message, client):
        self.channel = channel
        self.guild = get_bits_server(client)
        self.author = author
        self.new_name = message

    async def apply(self):
        old_name = get_user_info(self.author.id, 'team_name')
        role = get(self.guild.roles, name=old_name)
        if role is None:
            await self.channel.send("You are not in this team")
            return
        text_channel = get(self.guild.text_channels, name=old_name)
        voice_channel = get(self.guild.voice_channels, name=old_name)
        await role.edit(name=self.new_name)
        await text_channel.edit(name=self.new_name)
        await voice_channel.edit(name=self.new_name)

        data = {
            "team_name": self.new_name,
            "team_changed": True
        }
        requests.put("%s%s/" % (API_URL, str(self.author.id)), headers=headers, data=data)
        await self.channel.send("Team name changed!")
