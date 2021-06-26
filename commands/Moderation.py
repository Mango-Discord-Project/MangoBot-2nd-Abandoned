import discord
from discord.ext import commands
from discord import User
from core.classes import Cog_Extension
from plugin.MUT import MUT

class Moderation(Cog_Extension):
    @commands.has_guild_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, member:User=None, *, reason:str=None):
        if not member:
            await ctx.send('請選定一個成員以進行踢除動作')
            return
        if not reason:
            reason = '無'
        await ctx.send(f'{ctx.author.mention} 已踢除 {member.mention}\n原因：\n> {reason}')
        await ctx.guild.kick(member, reason=reason)
        print(f'{MUT.now()}{ctx.author} 已踢除 {member}，原因：{reason}')
    
    @commands.has_guild_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member:User=None, *, reason:str=None):
        if not member:
            await ctx.send('請選定一個成員以進行停權')
            return
        if not reason:
            reason = '無'
        await ctx.send(f'{ctx.author.mention} 已停權 {member.mention}\n原因：\n> {reason}')
        await ctx.guild.ban(member, reason=reason)
        print(f'{MUT.now()}{ctx.author} 已停權 {member}，原因：{reason}')

def setup(bot):
    bot.add_cog(Moderation(bot))