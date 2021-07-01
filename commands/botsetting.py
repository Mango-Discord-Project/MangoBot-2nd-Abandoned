import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension
from plugin.MUT import MUT

def save(jsonName, data:dict):
    with open(f'./setting/{jsonName}.json', mode='w', encoding='utf8') as File:
        json.dump(data, File, sort_keys=True, indent=4, ensure_ascii=False)

with open('./setting/channels.json', mode='r', encoding='utf8') as cFile:
    cData = json.load(cFile)

class botsetting(Cog_Extension):
    @commands.is_owner()
    @commands.command()
    async def setguild(self, ctx, setupType):
        if setupType == 'channel':
            with open('./setting/channels.json', mode='r', encoding='utf8') as cFile:
                cData = json.load(cFile)
            cData['index'][str(ctx.guild.id)] = {
                'member_join': {
                    'id': None, 
                    'message': '{mmention} Join {guildname}', 
                    'used': False
                    }, 
                'member_remove': {
                    'id': None, 
                    'message': '{mmention} leave {guildname}', 
                    'used': False
                    }, 
                'log': {
                    'id': None, 
                    'message': '{now} Bot is Ready', 
                    'used': False
                    }
                }
            save(jsonName='channels', data=cData)
        elif setupType == 'role':
            pass
        await ctx.send(f'{ctx.guild.name} Setup {setupType.title()} Setting')
    
    @commands.has_guild_permissions(administrator=True)
    @commands.group()
    async def channel(self, ctx):
        pass

    @commands.has_guild_permissions(administrator=True)
    @channel.command()
    async def set(self, ctx, changeType, dataType, data):
        changeType = changeType.lower()
        if changeType in ('join', 'j'):
            changeData = 'member_join'
        elif changeType in ('remove', 'r'):
            changeData = 'member_remove'
        elif changeType == 'log':
            changeData = 'log'
        else:
            await ctx.send(f'Value changeType:`{changeType}` is Invalid')
            return

        if dataType not in ('id', 'message', 'used'):
            await ctx.send(f'Value dataType:`{dataType}` is Invalid')
            return
        
        if dataType == 'id' and not data.isdigit():
            await ctx.send(f'Value data:`{data}` is Invalid')
            return
        if dataType == 'used' and data.lower() not in ('true', 't', 'false', 'f'):
            await ctx.send(f'Value data:`{data}` is Invalid')
            return
        elif dataType == 'used' and data.lower() in ('true', 't', 'false', 'f'):
            data = data.lower()
            if data in ('true', 't'):
                data = True
            elif data in ('false', 'f'):
                data = False
        
        cData['index'][str(ctx.guild.id)][changeData][dataType] = data
        save(jsonName='channels', data=cData)

        await ctx.send(f'`{changeData}: {{{dataType}: {data}}}`')

def setup(bot):
    bot.add_cog(botsetting(bot))