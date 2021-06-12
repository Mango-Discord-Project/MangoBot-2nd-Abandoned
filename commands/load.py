import discord
from discord.ext import commands
from core.classes import Cog_Extension
from datetime import datetime

def timestamp():
    return f"[{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}]"

def loadLog(loadType, author, extension):
    return f'{timestamp()} {author} {loadType} {extension}.py'

def loadMsg(loadType, extension, status):
    return f'{loadType} {extension} {status}'

class load(Cog_Extension):
    @commands.has_guild_permissions(administrator=True)
    @commands.command()
    async def load(self, ctx, extension):
        print(loadLog('load', ctx.author, extension))
        try:
            self.bot.load_extension(f'commands.{extension}')
        except:
            out = loadMsg('Load', extension, 'failed')
        else:
            out = loadMsg('Load', extension, 'success')
        finally:
            await ctx.send(out)

    @commands.has_guild_permissions(administrator=True)
    @commands.command()
    async def unload(self, ctx, extension):
        print(loadLog('unload', ctx.author, extension))
        try:
            self.bot.unload_extension(f'commands.{extension}')
        except:
            out = loadMsg('Unload', extension, 'failed')
        else:
            out = loadMsg('Unload', extension, 'failed')
        finally:
            await ctx.send(out)

    @commands.has_guild_permissions(administrator=True)
    @commands.command()
    async def reload(self, ctx, extension):
        print(loadLog('reload', ctx.author, extension))
        try:
            self.bot.reload_extension(f'commands.{extension}')
        except:
            out = loadMsg('Reload', extension, 'failed')
        else:
            out = loadMsg('Reload', extension, 'success')
        finally:
            await ctx.send(out)

def setup(bot):
    bot.add_cog(load(bot))