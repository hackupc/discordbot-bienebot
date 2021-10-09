from discord.utils import get
from get_enviroment import DISCORD_ORGANIZER_ROLE_NAME


class GetReactions:

    def __init__(self, channel, author, message):
        self.channel = channel
        self.author = author
        self.received = message

    async def apply(self):
        if get(self.author.roles, name=DISCORD_ORGANIZER_ROLE_NAME) is None:
            await self.channel.send("You have no permissions to see the required information")
            return
        message_id = await self.channel.fetch_message(self.received.reference.message_id)
        reactions = message_id.reactions
        text = ''
        for reaction in reactions:
            emoji = reaction.emoji
            users = await reaction.users().flatten()
            ids = [user.name for user in users]
            text += "%s:\n%s\n" % (emoji, '\n'.join(ids))
        await self.author.send(text)
