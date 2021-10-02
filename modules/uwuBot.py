import discord
from discord.ext import commands

from get_enviroment import TOKEN, COMMAND_PREFIX
from modules.commands.announce import Announce
from modules.commands.biene import Biene
from modules.commands.cat import Cat
from modules.commands.clear import Clear
from modules.commands.createAllTeams import CreateAllTeams
from modules.commands.deletehackerchannels import DeleteHackerChannels
from modules.commands.dog import Dog
from modules.commands.ball import Ball
from modules.commands.help import Help
from modules.commands.joke import Joke
from modules.commands.memes import Memes
from modules.commands.parrot import Parrot
from modules.commands.changeTeamName import ChangeTeamName
from modules.commands.addToTeam import AddToTeam
from modules.commands.createTeam import CreateTeam
from modules.commands.getUserInfo import GetUserInfo
from modules.commands.getReactions import GetReactions
from modules.commands.addSticker import AddSticker
from modules.models.user import User


class UwuBot:

    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.members = True
        self.client = commands.Bot(COMMAND_PREFIX, guild_subscriptions=True, self_bot=False, intents=intents)
        self.token = TOKEN
        self.client.remove_command('help')

        @self.client.event
        async def on_ready():
            await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming,
                                                                        name="HackUPC 2021",
                                                                        url="https://www.twitch.tv/hackersupc"))

        @self.client.event
        async def on_member_join(member):
            await User(member=member, client=self.client).save()

        @self.client.event
        async def on_message(message):
            message_text = message.content.lower().split(' ')
            if len(message_text) > 1 and message_text[0].startswith(COMMAND_PREFIX):
                command = message_text[1]
                meme_text = ' '.join(message_text[2:])
                channel = message.channel
                author = message.author
                if command == 'parrot':
                    await Parrot(channel=channel, author=author).apply()
                elif command == 'cat':
                    await Cat(channel=channel, author=author).apply()
                elif command == '8ball' or command == 'decide':
                    await Ball(channel=channel, author=author).apply()
                elif command == 'dog':
                    await Dog(channel=channel, author=author).apply()
                elif command == 'joke':
                    await Joke(channel=channel, author=author, option=1).apply()
                elif command == 'projoke':
                    await Joke(channel=channel, author=author, option=0).apply()
                elif command == 'parjoke':
                    await Joke(channel=channel, author=author, option=2).apply()
                elif command == 'biene':
                    if len(message_text) > 2:
                        await Biene(channel=channel, author=author, message=message_text[2]).apply()
                    else:
                        await Biene(channel=channel, author=author).apply()
                elif command == 'ping':
                    await channel.send('pong')
                elif command == 'clearyesimsure':
                    await Clear(channel=channel, author=author).apply()
                elif command == 'meme':
                    await Memes(channel=channel, author=author, message=meme_text).apply()
                elif command == 'help':
                    await Help(channel=channel, author=author).apply()
                elif command == 'createteam':
                    await CreateTeam(channel=channel, author=author, message=message_text[2],
                                     user=message.mentions[0], client=self.client).apply()
                elif command == 'changeteamname':
                    await ChangeTeamName(channel=channel, author=author, message=message_text[2], client=self.client)\
                        .apply()
                elif command == 'jointeam':
                    await AddToTeam(channel=channel, author=author, message=message_text[2], users=message.mentions)\
                        .apply()
                elif command == 'userinfo':
                    await GetUserInfo(channel=channel, author=author, user=message.mentions[0]).apply()
                elif command == 'reactions':
                    await GetReactions(channel=channel, author=author, message=message).apply()
                elif command == 'addsticker':
                    await AddSticker(channel=channel, author=author, message=message_text[2],
                                     user=message.mentions[0]).apply()
                elif command == 'createallteams':
                    await CreateAllTeams(channel=channel, author=author, client=self.client).apply()
                elif command == 'announce':
                    await Announce(channel=channel, author=author, channels=message.channel_mentions,
                                   message=message.content.lower(), attachments=message.attachments).apply()
                elif command == 'loaduser':
                    await User(member=message.mentions[0], client=self.client).apply(channel, author)
                elif command == 'deletehackerchannels':
                    await DeleteHackerChannels(author=author, channel=channel).apply()

    def start(self):
        print("Starting modules!")
        self.client.run(self.token)
