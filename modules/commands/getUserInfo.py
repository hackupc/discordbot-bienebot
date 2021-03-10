from discord.utils import get
from modules.commands.utils import get_user_info
import json


class GetUserInfo:

    def __init__(self, channel, author, user):
        self.channel = channel
        self.author = author
        self.user = user

    async def apply(self):
        if get(self.author.roles, name='Organizer') is None:
            await self.channel.send("You have no permissions to see the required information")
            return
        info = get_user_info(self.user.id, 'all')
        if info is None:
            await self.author.send("User %s not found in the database" % self.user.name)
        else:
            await self.author.send(json.dumps(info, indent=1))
