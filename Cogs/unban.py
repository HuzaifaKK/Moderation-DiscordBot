import discord
from discord.ext import commands


class idk(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member=None):
        if member == None:
            embed = discord.Embed(
                description='❎ Please specify a user to unban', color=discord.Color.dark_purple())
            await ctx.send(embed=embed)
        else:
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split('#')

            for ban_entry in banned_users:
                user = ban_entry.user

                if(user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    embed = discord.Embed(
                        description='✅ Unbanned {}'.format(
                            user.mention),
                        colour=discord.Colour.dark_purple()
                    )
                    await ctx.send(embed=embed)
                    return

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                description='You dont have permission to do that',
                colour=discord.Colour.dark_purple()
            )
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(idk(client))
