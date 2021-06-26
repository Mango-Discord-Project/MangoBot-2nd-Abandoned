import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension
from plugin.MUT import MUT

with open('./setting/channels.json', mode='r', encoding='utf8') as cFile:
    cData = json.load(cFile)

def JLmessage(string:str, member):
    return string.format(mmention=member.mention, guildname=member.guild.name)

def save(jsonName, data:dict):
    with open(f'./setting/{jsonName}.json', mode='r', encoding='utf8') as File:
        json.dump(data, File, sort_keys=True, indent=4, ensure_ascii=False)

class event(Cog_Extension):
    @commands.is_owner()
    @commands.command()
    async def tevent(self, ctx):
        await ctx.send('event is ready')

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{MUT.now()} Bot is Ready')
        for guild in self.bot.guilds:
            if cData['index'][str(guild.id)]['log']['used']:
                channel = self.bot.get_channel(cData[str(guild.id)]['log']['id'])
                await channel.send()
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{MUT.now()} {member}( {member.id} ) join {member.guild}( {member.guild.id} )')
        if cData['index'][str(member.guild.id)]['member_join']['used']:
            channel = self.bot.get_channel(cData[str(member.guild.id)]['member_join']['id'])
            await channel.send(JLmessage(cData[str(member.guild.id)]['member_join']['message']))
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{MUT.now()} {member}( {member.id} ) leave {member.guild}( {member.guild.id} )')
        if cData['index'][str(member.guild.id)]['member_remove']['used']:
            channel = self.bot.get_channel(cData[str(member.guild.id)]['member_remove']['id'])
            await channel.send(JLmessage(cData[str(member.guild.id)]['member_join']['message']))
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        print(f'{MUT.now()} Bot Join a Guild: {guild.name}( {guild.id} )')
        cData['index'][str(guild.id)] = {
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
        MUT.save('./settings/channel.json', data=cData)
    
    @commands.Cog.listener()
    async def on_invite_delete(self, invite):
        pass


def setup(bot):
    bot.add_cog(event(bot))