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
            await self.channel.send("You have no permissions to create a new team. Contact an organizer")
            return
        info = get_user_info(self.user.id, 'all')
        await self.author.send(json.dumps(info, indent=1))
