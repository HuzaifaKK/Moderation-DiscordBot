import discord
from discord.ext import commands


class ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason=None):
        if member == None:
            embed = discord.Embed(
                description='❎ Please specify a user to ban', color=discord.Color.dark_purple())
            await ctx.send(embed=embed)
        else:
            await member.ban(reason=reason)
            embed = discord.Embed(
                description='✅ Banned {} for ``{}``'.format(
                    member.mention, reason),
                colour=discord.Colour.dark_purple()
            )

            await ctx.send(embed=embed)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                description='You dont have permission to do that',
                colour=discord.Colour.dark_purple()
            )
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(ban(client))
