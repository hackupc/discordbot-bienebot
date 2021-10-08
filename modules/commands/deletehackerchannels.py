from discord.utils import get
from get_enviroment import DISCORD_ORGANIZER_ROLE_NAME


class DeleteHackerChannels:
    def __init__(self, author, channel):
        self.author = author
        self.channel = channel

    async def apply(self):
        if get(self.author.roles, name=DISCORD_ORGANIZER_ROLE_NAME) is None:
            await self.channel.send("You have no permissions. Contact an organizer")
            return
        if not self.author.top_role.permissions.administrator:
            await self.channel.send("You have no permissions. Contact an organizer")
            return
        for category in self.author.guild.categories:
            if category.name.startswith("Hackers-"):
                for channel in category.channels:
                    await channel.delete()
