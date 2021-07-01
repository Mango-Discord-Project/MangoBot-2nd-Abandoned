import discord
from discord.ext import commands
from discord import User
from core.classes import Cog_Extension
from plugin.MUT import MUT

class Moderation(Cog_Extension):
    @commands.has_guild_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, member:User=None, *, reason:str='無'):
        if not member:
            await ctx.send('請選定一個成員以踢除')
            return
        await ctx.send(f'{ctx.author.mention} 已踢除 {member.mention}\n原因：\n> {reason}')
        await ctx.guild.kick(member, reason=reason)
        print(f'{MUT.now()} {ctx.author} 已踢除 {member}，原因：{reason}')
    
    @commands.has_guild_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member:User=None, *, reason:str='無'):
        if not member:
            await ctx.send('請選定一個成員以停權')
            return
        await ctx.send(f'{ctx.author.mention} 已停權 {member.mention}\n原因：\n> {reason}')
        await ctx.guild.ban(member, reason=reason)
        print(f'{MUT.now()} {ctx.author} 已停權 {member}，原因：{reason}')
    
    @commands.is_owner()
    @commands.command()
    async def guilds(self, ctx):
        index = [f'{guild.name}: {guild.id} / {guild.member_count}' for  guild in self.bot.guilds]
        totalGuild = len(self.bot.guilds)
        totalMember = sum(guild.member_count for guild in self.bot.guilds)
        string = '\n'.join(index)

        embed = discord.Embed(title='Server List', description=f'```{string}```')
        embed.add_field(name='Total Servers Count', value=totalGuild)
        embed.add_field(name='Total Member Count', value=totalMember)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Moderation(bot))