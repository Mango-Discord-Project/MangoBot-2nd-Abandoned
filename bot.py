import discord
import json
import os
from discord.ext import commands

with open('./setting/Token.json') as TokenFile:
    TokenData = json.load(TokenFile)

with open('./setting/botSetting.json') as SettingFile:
    SettingData = json.load(SettingFile)

bot = commands.Bot(
    command_prefix = SettingData['Prefix'],
    # help_command = 'sos',
    # owner_ids = (467532880625664000),
    strip_after_prefix = True,
    intents = discord.Intents.all()
    )

for Filename in os.listdir('./commands'):
    if Filename.endswith('.py'):
        bot.load_extension(f'commands.{Filename[:-3]}')

if __name__ == '__main__':
    bot.run(TokenData['Token'])