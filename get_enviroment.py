import json
import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
COMMAND_PREFIX = os.getenv('COMMAND_PREFIX')
SERVER_NAME = os.getenv('SERVER_NAME')
API_TOKEN = os.getenv('API_TOKEN')
DOMAIN = os.getenv('DOMAIN')
headers = {'Authorization': 'Token ' + API_TOKEN}
ANNOUNCEMENTS_CHANNEL = os.getenv('ANNOUNCEMENTS_CHANNEL')
WANTS_ORIGINAL_MEME_HELP = os.getenv('WANTS_ORIGINAL_MEME_HELP', "True")
DISCORD_ORGANIZER_ROLE_NAME = os.getenv('DISCORD_ORGANIZER_ROLE_NAME')

with open('files/parrots.json', 'r') as fp:
    PARROTS = json.load(fp)
with open('files/memes.json', 'r') as fp:
    MEMES = json.load(fp)
