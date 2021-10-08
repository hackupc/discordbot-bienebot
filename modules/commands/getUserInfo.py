from discord.utils import get
from modules.services.api import Api
import json
from get_enviroment import DISCORD_ORGANIZER_ROLE_NAME


class GetUserInfo:

    def __init__(self, channel, author, user):
        self.channel = channel
        self.author = author
        self.user = user
        self.api = Api()

    async def apply(self):
        if get(self.author.roles, name=DISCORD_ORGANIZER_ROLE_NAME) is None:
            await self.channel.send("You have no permissions to see the required information")
            return
        try:
            info = self.api.get_user_info(self.user.id, 'all')
            await self.author.send(json.dumps(info, indent=1))

        except (self.api.USER_NOT_FOUND, self.api.BAD_REQUEST, self.api.SERVER_ERROR) as e:
            await self.channel.send(e.message)
