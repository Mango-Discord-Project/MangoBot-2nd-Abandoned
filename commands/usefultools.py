import discord
from discord.ext import commands
from core.classes import Cog_Extension
from plugin.MUT import MUT

class UsefulTools(Cog_Extension):
    pass
    # @commands.command()
    # async def invite(self, ctx):
    #     invite_ = await ctx.channel.create_invite(
    #         max_age=600, 
    #         reason=f'{ctx.author} created'
    #         )
    #     await ctx.send(f'Invite: \n{invite_}')
    #     print(f'{MUT.now()}{ctx.author} create a invite link')
    
    # @commands.command()
    # async def afk(self, ctx, reason=None):
    #     if str(ctx.author.id) in afkDict:
    #         await ctx.send('You are AFK')
    #         print(f'{timestamp()}{ctx.author} try to afk, but failled')
    #         return
    #     afkDict[str(ctx.author.id)] = [True, reason]
    #     await ctx.send(f'{ctx.author} is AFK', f'\nreason: {reason}' if reason else '')
    #     await ctx.author.edit(nick='[AFK]'+ctx.author.nick)
    #     print(f'{timestamp()}{ctx.author} is AFK')

def setup(bot):
    bot.add_cog(UsefulTools(bot))