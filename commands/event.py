import discord
from discord.ext import commands
from core.classes import Cog_Extension
from datetime import datetime

def timestamp():
    return f"[{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}]"

class event(Cog_Extension):
    @commands.is_owner()
    @commands.command()
    async def tevent(self, ctx):
        await ctx.send('event is ready')

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{timestamp()} Bot is Ready')
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{timestamp()} {member}( {member.id} ) join {member.guild}( {member.guild.id} )')
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{timestamp()} {member}( {member.id} ) leave {member.guild}( {member.guild.id} )')
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        print(f'{timestamp()} Bot Join a Guild: {guild.name}( {guild.id} )')

def setup(bot):
    bot.add_cog(event(bot))