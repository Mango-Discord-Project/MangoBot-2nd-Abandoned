import discord
import random
from discord.ext import commands
from discord import User
from core.classes import Cog_Extension

def randomInt(min, max):
    return random.randint(min, max)


class funny(Cog_Extension):
    @commands.group()
    async def random(self, ctx):
        pass

    @random.command()
    async def love(self, ctx, member:User=None):
        if not member:
            await ctx.send('請輸入戀愛相性對象')
            return
        if member.id == ctx.author.id:
            await ctx.send('~~不要這麼自戀好嗎?~~')
            return
        await ctx.send(f'{ctx.author.mention} 與 {member.mention} 的相性為 {randomInt(0, 100)}')
    
    @random.command()
    async def lucky(self, ctx):
        luckyList = ['大吉', '中吉', '小吉', '吉', '半吉', '末吉', '末小吉', '凶', '小凶', '半凶', '末凶', '大凶']
        point = random.choice(luckyList)
        await ctx.send(f'{ctx.author.mention} 抽到的籤是 `{point}`')
    
    @random.command()
    async def dice(self, ctx, times:str='1'):
        if not times.isdigit():
            await ctx.send('請輸入正確的數字')
            return
        if int(times) > 10:
            await ctx.send('一次最多能擲10顆骰子')
            return
        point = [random.randint(1, 6) for i in range(int(times))]
        await ctx.send(f'你丟出了`{times}`顆骰子，分別是\n> `{", ".join([str(i) for i in point])}`\n共計`{sum(point)}`點')
    
    @commands.group()
    async def me(self, ctx):
        pass

    @me.command()
    async def avatar(self, ctx, member:User=None):
        if not member:
            await ctx.send(ctx.author.avatar_url)
            return
        await ctx.send(member.avatar_url)
    
    @me.command()
    async def id(self, ctx, member:User=None):
        if not member:
            await ctx.send(ctx.author.id)
            return
        await ctx.send(member.id)

def setup(bot):
    bot.add_cog(funny(bot))