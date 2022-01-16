from skingrabber import skingrabber
from discord.ext import commands
from mojang import MojangAPI
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

    @commands.command()
    async def spawn(self, ctx):
        user_id = ctx.author
        print(f'{user_id} used !spawn')
        await ctx.send(
            'I am asking everyone here why there is no one coming to spawn? Are you all too pussy? Or are all of you like tyrannosaurus u only come with a stack of Egaps, eat all of them and die in 5 minutes to people who have been playing a week? Sincerely - come to spawn retards \n\n- best sleepylessons quote')

    @commands.command()
    async def skin(self, ctx, player=None, direction='right'):
        user_id = ctx.author
        print(f'{user_id} used skin')
        if player is None:
            await ctx.send('I need a player name to do that')
        else:
            uuid = MojangAPI.get_uuid(player)
            embed = discord.Embed(title=f'{player}\'s skin', url=f'https://mc-heads.net/body/{uuid}/{direction}',
                                  colour=discord.Colour.blue())
            embed.set_image(url=f'https://mc-heads.net/body/{uuid}/{direction}')
            await ctx.send(embed=embed)

    @commands.command()  # says the message that the person says
    @commands.has_permissions(kick_members=True)
    async def say(self, ctx, *, message=None, amount=0):
        user_id = ctx.author
        print(f'{user_id} used say')
        if message is None:
            await ctx.send('bro just say something not that hard')
            return
        else:
            await ctx.channel.purge(limit=amount + 1)  # deletes user message
            await ctx.send(f'{message}')  # sends bot message

    @commands.command()
    async def IA(self, ctx):
        user_id = f'{ctx.author}'
        print(f'{user_id} used IA')
        embed = discord.Embed(title='fuck IA', description=f'why IA is bad',
                              colour=discord.Colour.blue())
        embed.add_field(name='IA',
                        value=f'IA is a shit server with a owner who does not know how to run an anarchy server.'
                              f'joining the server is a waist of time as it is a dead server.'
                              f'ecme is better server than IA and that is saying a lot.'
                              f'PA on top')
        await ctx.send(embed=embed)

    @commands.command()
    async def PA(self, ctx):
        user_id = f'{ctx.author}'
        print(f'{user_id} used PA')
        embed = discord.Embed(title='PA', description=f'PA Am I Right',
                              colour=discord.Colour.blue())
        embed.add_field(name='PA',
                        value=f'from the ashes of NA, PA will rise')
        await ctx.send(embed=embed)

    @commands.command()
    async def NA(self, ctx):
        user_id = f'{ctx.author}'
        print(f'{user_id} used na')
        embed = discord.Embed(title='RIP nether anarchy',
                              colour=discord.Colour.blue())
        embed.add_field(name='goodbye',
                        value=f'Nether Anarchy was and will be the best anarchy server I have ever played on.\n'
                              f'It was perfect it had everything an anarchy server could have ever wanted.\n'
                              f'It had a lot of players but not too many, it had no dupes,\n'
                              f'it was up to date, its anti cheat was not too strict\n'
                              f'and most of all it had the best owner an anarchy server could have had.'
                              f'But all good things come to an end and the server was shutdown, and now it will be remembered\n'
                              f'as the best anarchy server in minecraft.')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(fun(client))
