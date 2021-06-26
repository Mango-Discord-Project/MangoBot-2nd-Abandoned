import discord
from discord.ext import commands
from core.classes import Cog_Extension
from datetime import datetime

def timestamp(): return f"[{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}]"

afkDict = {}
inviteDict = {}

class UsefulTools(Cog_Extension):
    @commands.command()
    async def invite(self, ctx):
        if str(ctx.author.id) in inviteDict:
            await ctx.send('You are created a invite link\n')
            print(f'{timestamp()}{ctx.author} try to create a invite link, but failled.')
            return
        invite_ = await ctx.channel.create_invite(
            max_age=600, 
            reason=f'{ctx.author} created'
            )
        inviteDict[str(ctx.author.id)] = invite_.url
        await ctx.send(f'Invite: \n{invite_}')
        print(f'{timestamp()}{ctx.author} create a invite link')
    
    @commands.command()
    async def afk(self, ctx, reason=None):
        if str(ctx.author.id) in afkDict:
            await ctx.send('You are AFK')
            print(f'{timestamp()}{ctx.author} try to afk, but failled')
            return
        afkDict[str(ctx.author.id)] = [True, reason]
        await ctx.send(f'{ctx.author} is AFK', f'\nreason: {reason}' if reason else '')
        await ctx.author.edit(nick='[AFK]'+ctx.author.nick)
        print(f'{timestamp()}{ctx.author} is AFK')

def setup(bot):
    bot.add_cog(UsefulTools(bot))