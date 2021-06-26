import discord
from discord.ext import commands
from core.classes import Cog_Extension
from datetime import datetime

def timestamp(): return f"[{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}]"

def round(num:int):
    if num % 1 >= 0.5:
        return int(num//1+1)
    return int(num)

class botinfo(Cog_Extension):
    @commands.command()
    async def latency(self, ctx):
        await ctx.send(f'> Bot latency: `{abs(round(self.bot.latency*1000))}(ms)`')

def setup(bot):
    bot.add_cog(botinfo(bot))