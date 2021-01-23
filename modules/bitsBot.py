from asyncio import sleep

import discord
from discord.ext import commands
from discord.ext.commands import cooldown

from get_enviroment import TOKEN, COMMAND_PREFIX
from modules.commands.biene import Biene
from modules.commands.cat import Cat
from modules.commands.clear import Clear
from modules.commands.dog import Dog
from modules.commands.joke import Joke
from modules.commands.parrot import Parrot


class BitsBot:

    prefix = ""
    client = None
    token = ""

    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.members = True
        self.client = commands.Bot(COMMAND_PREFIX, guild_subscriptions=True, self_bot=False, intents=intents)
        self.token = TOKEN
        self.client.remove_command('help')

        @self.client.event
        async def on_message(message):
            message_text = message.content.lower().split(' ')
            if len(message_text) > 1 and message_text[0].startswith(COMMAND_PREFIX):
                command = message_text[1]
                channel = message.channel
                author = message.author
                if command == 'parrot':
                    await Parrot(channel=channel, author=author).apply()
                elif command == 'cat':
                    await Cat(channel=channel, author=author).apply()
                elif command == 'dog':
                    await Dog(channel=channel, author=author).apply()
                elif command == 'joke':
                    await Joke(channel=channel, author=author, option=1).apply()
                elif command == 'projoke':
                    await Joke(channel=channel, author=author, option=0).apply()
                elif command == 'parjoke':
                    await Joke(channel=channel, author=author, option=2).apply()
                elif command == 'biene':
                    await Biene(channel=channel, author=author).apply()
                elif command == 'ping':
                    await channel.send('pong')
                elif command == 'clearyesimsure':
                    await Clear(channel=channel, author=author).apply()

    def start(self):
        print("Starting modules!")
        self.client.run(self.token)
