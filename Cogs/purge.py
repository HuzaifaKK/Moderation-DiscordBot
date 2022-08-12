import discord
from discord.ext import commands


class purge(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, limit: int = None):
        if limit == None:
            embed = discord.Embed(
                description='❎ Please specify a limit to purge', color=discord.Color.dark_purple())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                description='✅ Purged {} Messages'.format(limit),
                colour=discord.Colour.dark_purple()
            )
            await ctx.channel.purge(limit=limit+1)
            await ctx.send(embed=embed)
            await ctx.message.delete()

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                description='You dont have permission to do that',
                colour=discord.Colour.dark_purple()
            )
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(purge(client))
