import discord
from discord.ext import commands
from pathlib import Path
import os
from discord.utils import get

TOKEN = 'Your Bot Token Here'

intents = discord.Intents.all()
client = commands.Bot(command_prefix='-')
client.remove_command('help')
cwd = Path(__file__).parents[0]
cwd = str(cwd)

extensions = ['ban', 'unban', 'banlist', 'kick', 'purge']

for file in os.listdir(cwd+'/Cogs'):
    if file.endswith(".py"):
        extensions.append("Cogs."+file[:-3])


@client.event
async def on_ready():
    print('Brine Bot Is Ready!')

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            err = '[Error {}]'.format(error)
            print('Loading {}... '.format(extension, err))

client.run(TOKEN)
