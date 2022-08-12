import discord
from discord.ext import commands
import asyncio


class banlist(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def banlist(self, ctx):
        page = 1
        bans = await ctx.guild.bans()

        def check(reaction, user):
            return user != self.client.user
        message = None

        while True:
            header = f"List Of Banned Users (Page #{page}):"
            embed = discord.Embed(
                title=f"{header}", color=discord.Color.dark_purple())
            for ban_entry in bans[(page-1)*10:page*10]:
                embed.add_field(
                    name=f"**{ban_entry.user}**", value=f"Reason: *{ban_entry.reason}*")
            if message == None:
                message = await ctx.send(embed=embed)
            else:
                await message.edit(embed=embed)
            if len(bans) > 10 and not page*10 - len(bans) <= 10:
                await message.add_reaction("◀️")
                await message.add_reaction("▶️")
                try:
                    reaction, user = await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                except asyncio.TimeoutError:
                    await message.clear_reaction("◀️")
                    await message.clear_reaction("▶️")
                    break
                if str(reaction) == "▶️":
                    page += 1
                elif str(reaction) == "◀️" and page > 1:
                    page -= 1
                else:
                    print("none of the reactions")
            else:
                break

    @banlist.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                description='You dont have permission to do that',
                colour=discord.Colour.dark_purple()
            )
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(banlist(client))
