from skingrabber import skingrabber
from discord.ext import commands
from mojang import MojangAPI
import discord


class utility(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.sg = skingrabber()

    @commands.Cog.listener()  # says if cog is loaded
    async def on_ready(self):
        print("utility cog online")

    @commands.command()  # give some basic info about the user
    async def userinfo(self, ctx, user: discord.User = None, amount=0):
        user_id = ctx.author
        print(f'{user_id} used userinfo')
        if user is None:
            await ctx.send('im sorry but I cant do that if you dont give me a user')
            return
        await ctx.channel.purge(limit=amount + 1)
        embed = discord.Embed(title='userinfo', description=f'some info about {user.name}',
                              colour=discord.Colour.blue())
        embed.add_field(name=user.name,
                        value=f'- User\'s name: {user.name}\n- User\'s ID: {user.id}\n- User\'s discriminator: {user.discriminator}\n'
                              f'- User\'s account created: {user.created_at}\n- User is a bot: {user.bot}')
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()  # the questions you need to answer to apply
    @commands.has_permissions(kick_members=True)
    async def apply(self, ctx):
        user_id = f'{ctx.author}'
        print(f'{user_id} used apply')
        embed = discord.Embed(title='how to apply', description=f'how to fill out aplication',
                              colour=discord.Colour.blue())
        embed.add_field(name='example aplication form',
                        value=f'- when did you join the server?\n- what are your account names? (main and alt)\n'
                              f'- what is your irl age? (not mandetory)\n- what is your playtime\n - what groups are you in?\n'
                              f'- are you willing to join and talk in a vc?\n- what farms can you make?\n- why you want to join?\n'
                              f'- do you know someone in the group who can vouch for you? (Who are they)\n'
                              f'- do you use a hacked client? (what client is it)\n- mods do you use?')
        await ctx.send(embed=embed)

    @commands.command()  # ping of discord bot
    async def servers(self, ctx):
        user_id = f'{ctx.author}'
        print(f'{user_id} used servers')
        embed = discord.Embed(title='servers', description=f'important discord servers',
                              colour=discord.Colour.blue())
        embed.add_field(name='--Servers--',
                        value=f'- PA: https://discord.gg/PRJff9MJ9d\n'
                              f'- NAT: https://discord.gg/n3dSyKjfQM\n'
                              f'- PAT: https://discord.gg/AK4KtDZUaD\n'
                              f'- Frat: https://discord.gg/Q3BDdn2xag\n'
                              f'- Cat Pack: https://discord.gg/yKd2h4gkzu')
        await ctx.send(embed=embed)

    @commands.command()  # ping of discord bot
    async def ping(self, ctx):
        user_id = ctx.author
        print(f'{user_id} used ping')
        embed = discord.Embed(title='bot latency', description=f'the latency(ping) of the bot',
                              colour=discord.Colour.blue())
        embed.add_field(name='ping',
                        value=f'- ping is: {self.client.latency}')
        await ctx.send(embed=embed)

    @commands.command()  # ping of discord bot
    async def uuid(self, ctx, player=None):
        user_id = ctx.author
        print(f'{user_id} used uuid')
        uid = MojangAPI.get_uuid(player)
        if player is None:
            await ctx.send('I need a minecraft player name to do that')
        elif uid is None:
            await ctx.send('The name you gave me is not a real minecraft player name')
        else:
            embed = discord.Embed(title='UUID', description=f'- {player}\'s UUID: {uid}',
                                  colour=discord.Colour.blue())
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(utility(client))
