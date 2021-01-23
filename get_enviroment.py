import json
import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
COMMAND_PREFIX = os.getenv('COMMAND_PREFIX')
MUDAE_CHANNEL = os.getenv('MUDAE_CHANNEL')
with open('files/parrots.json', 'r') as fp:
    PARROTS = json.load(fp)
