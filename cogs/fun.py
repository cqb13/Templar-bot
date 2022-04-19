from skingrabber import skingrabber
from discord.ext import commands
from mojang import MojangAPI
import requests
import discord


class fun(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.sg = skingrabber()

    @commands.Cog.listener()  # says if cog is loaded
    async def on_ready(self):
        print("fun cog online")

    @commands.command()
    async def better(self, ctx):
        user_id = ctx.author
        print(f'{user_id} used better')
        await ctx.send('yes I am better than NetherBot')

    @commands.command()  # finds minecraft player skins and sends them in discord
    async def skin(self, ctx, player=None, direction='right'):
        user_id = ctx.author
        uuid = MojangAPI.get_uuid(player)
        print(f'{user_id} used skin [{player}]')
        address = f'https://mc-heads.net/body/{uuid}/{direction}'
        url = address
        page = requests.get(url)
        if player is None:
            await ctx.send('I need a player name to do that')
        elif page.status_code != 200:
            print(f'>>> error {page.status_code} website could not be reached using backup')
            response = self.sg.get_skin_rendered(user=player)
            embed = discord.Embed(title=f'{player}\'s skin',
                                  colour=discord.Colour.blue())
            embed.set_image(url=response)
            await ctx.send(embed=embed)
        elif address == f'https://mc-heads.net/body/None/{direction}':
            await ctx.send('That name has either not been taken, or an invalid name')
        else:
            embed = discord.Embed(title=f'{player}\'s skin', url=address,
                                  colour=discord.Colour.blue())
            embed.set_image(url=address)
            await ctx.send(embed=embed)

    @commands.command()  # says the message that the person says
    @commands.has_permissions(kick_members=True)
    async def say(self, ctx, *, message=None, amount=0):
        user_id = ctx.author
        print(f'{user_id} used say [{message}]')
        if message is None:
            await ctx.send('You need to enter a message to send')
            return
        else:
            await ctx.channel.purge(limit=amount + 1)  # deletes user message
            await ctx.send(f'{message}')  # sends bot message

    @commands.command()  # says the message that the person says
    async def cqb13(self, ctx, *, message=None, amount=0):
        user_id = ctx.author
        print(f'{user_id} used say [{message}]')
        if message is None:
            await ctx.send('You need to enter a message to send')
            return
        else:
            await ctx.channel.purge(limit=amount + 1)  # deletes user message
            await ctx.send(f'{message}')  # sends bot message
          


def setup(client):
    client.add_cog(fun(client))
