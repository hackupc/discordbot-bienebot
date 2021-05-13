from discord.utils import get


class Announce:
    def __init__(self, channel, author, message, channels, attachments):
        self.channel = channel
        self.author = author
        self.channels = channels
        self.message = message
        self.attachment = None
        if len(attachments) != 0:
            self.attachment = attachments[0]

    async def apply(self):
        if get(self.author.roles, name='Organizer') is None:
            await self.channel.send("You have no permissions. Contact an organizer")
            return
        if len(self.channels) == 0:
            await self.channel.send('Error: No channels mentioned')
            return
        start = self.message.find('"')
        end = self.message.rfind('"')
        if start == -1 or end == -1:
            await self.channel.send('Error: "" not found')
            return
        message_to_send = self.message[start+1:end]
        file = None
        if self.attachment is not None:
            file = await self.attachment.to_file()
        for channel in self.channels:
            await channel.send(message_to_send, file=file)
