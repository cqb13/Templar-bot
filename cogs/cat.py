from discord.ext import commands
from discord.utils import get
import discord

from main import client


class cat(commands.Cog):  # all admin commands go here

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()  # says if cog is loaded
    async def on_ready(self):
        print("cat cog online")

    @commands.command()  # clears mesages
    @commands.has_permissions(kick_members=True)  # checks for manage message perm
    async def clear(self, ctx, *, amount=5):  # amount = amount of messages to clear if number not found
        user_id = ctx.author
        print(f'{user_id} used clear {amount}')
        await ctx.channel.purge(limit=amount + 1)

    @commands.command()  # kicks people from the server
    @commands.has_permissions(kick_members=True)  # checks for kick member perm
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        user_id = ctx.author
        print(f'{user_id} used kick {member}')
        myid = '<@565976415065997312>'
        await ctx.send('%s IMPORTANT ' % myid)
        await member.kick(reason=reason)
        await ctx.send(f'User {member} has kicked for {reason}.')  # send who and why they were banned

    @commands.command()  # bans people from the server
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        user_id = ctx.author
        print(f'{user_id} used ban {member}')
        myid = '<@565976415065997312>'
        await ctx.send('%s IMPORTANT ' % myid)
        await ctx.send(f'{member} was banned for {reason}')
        await member.ban(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def mute(self, ctx, member: discord.Member = None, reason=None):
        user_id = ctx.author
        print(f'{user_id} used mute {member}')
        if member is None:
            await ctx.send('I need to know the user you want to mute')
        else:
            myid = '<@565976415065997312>'
            await ctx.send('%s IMPORTANT ' % myid)
            role = get(member.guild.roles, name="stop talking")
            await member.add_roles(role)
            await ctx.send(f'{member} was muted for {reason}')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unmute(self, ctx, member: discord.Member = None, reason=None):
        user_id = ctx.author
        print(f'{user_id} used unmute {member}')
        if member is None:
            await ctx.send('I need to know the user you want to mute')
        else:
            myid = '<@565976415065997312>'
            await ctx.send('%s IMPORTANT ' % myid)
            role = get(member.guild.roles, name="stop talking")
            await member.remove_roles(role)
            await ctx.send(f'{member} was unmuted for {reason}')

    @commands.command()
    # @commands.has_permissions(ban_members=True)
    async def location(self, ctx, loc=None):
        activeservers = client.guilds
        channel = client.get_channel(932300104805797928)  # 932300104805797928
        set = 6
        count = 0
        for guild in activeservers:
            count += 1
            print(guild.name)
        await ctx.send('sent')
        await channel.send('--- server output ---')
        await channel.send(f'servers: {count}')
        if loc == 'loc':
            await channel.send('locations:')
            for guild in activeservers:
                await channel.send(guild.name)
        elif count > set:
            await ctx.send('WARNING: server count too high')
            await channel.send('WARNING:')
            await channel.send(f'server amount is to high')
            await channel.send(f'bot should be in {set} servers')
            await channel.send(f'bot is in {count} servers')
        await channel.send(f'---------------------')


def setup(client):
    client.add_cog(cat(client))
