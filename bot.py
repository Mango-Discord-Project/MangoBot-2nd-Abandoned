import discord
import json
import os
from discord.ext import commands
from datetime import datetime

def timestamp():
    return f"[{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}]"

with open('./setting/Token.json') as TokenFile:
    TokenData = json.load(TokenFile)

with open('./setting/botSetting.json') as SettingFile:
    SettingData = json.load(SettingFile)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=SettingData['Prefix'], intents=intents)

for Filename in os.listdir('./commands'):
    if Filename.endswith('.py'):
        bot.load_extension(f'commands.{Filename[:-3]}')

if __name__ == '__main__':
    bot.run(TokenData['Token'])