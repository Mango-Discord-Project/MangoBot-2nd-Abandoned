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
            await ctx.send('Please enter a love match')
            return
        if member.id == ctx.author.id:
            await ctx.send('~~Don\'t be so self-absorbed, okay??~~')
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
            await ctx.send('Please enter the correct number')
            return
        if int(times) > 10:
            await ctx.send('Up to 10 dice can be rolled at a time')
            return
        point = [random.randint(1, 6) for i in range(int(times))]
        await ctx.send(f'You have rolled `{times}` dice, which are\n> `{", ".join([str(i) for i in point])}`\nTotal `{sum(point)}` points')
    
    @commands.group()
    async def me(self, ctx):
        pass

    @me.command()
    async def avatar(self, ctx, member:discord.User=None):
        member = member or ctx.author
        avatar_url = member.avatar_url
        embed = discord.Embed(title=f'{str(member)}\'s Avatar', description=f'URL：[>> Click Me <<]({avatar_url})')
        embed.set_image(url=avatar_url)
        await ctx.send(embed=embed)
    
    @me.command()
    async def id(self, ctx, member:User=None):
        member = member or ctx.author
        await ctx.send(f'Your ID is: `{member.id}`')

def setup(bot):
    bot.add_cog(funny(bot))