import discord
from discord.ext import commands


class kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, *, reason=None):
        if member == None:
            embed = discord.Embed(
                description='❎ Please specify a user to kick', color=discord.Color.dark_purple())
            await ctx.send(embed=embed)
        else:
            await member.kick(reason=reason)
            embed = discord.Embed(
                description='✅ Kicked {} for ``{}``'.format(
                    member.mention, reason),
                colour=discord.Colour.dark_purple()
            )
            await ctx.send(embed=embed)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                description='You dont have permission to do that',
                colour=discord.Colour.dark_purple()
            )
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(kick(client))
