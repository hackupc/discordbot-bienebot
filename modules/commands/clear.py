from asyncio import sleep

from modules.commands.base import BaseCommand


class Clear(BaseCommand):

    async def apply(self):
        if self.author.server_permissions.administrator:
            deleted = await self.channel.purge(limit=10000)
            msg = await self.channel.send('purged %d messages' % len(deleted))
            await sleep(2)
            await msg.delete()
