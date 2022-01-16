from discord.ext import commands
import requests
import discord
import json


class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()  # says if cog is loaded
    async def on_ready(self):
        print("pic cog online")

    @commands.command()
    async def cat(self, ctx):
        user_id = ctx.author
        print(f'{user_id} used cat')
        f = r"http://aws.random.cat/meow"
        page = requests.get(f)
        data = json.loads(page.text)
        embed = discord.Embed(title=f'cat pic',
                              colour=discord.Colour.blue())
        embed.set_image(url=data['file'])
        await ctx.send(embed=embed)

    @commands.command()
    async def fox(self, ctx):
        user_id = ctx.author
        print(f'{user_id} used fox')
        response = requests.get("https://randomfox.ca/floof/")
        fox = response.json()
        url = fox['image']
        embed = discord.Embed(title=f'fox pic',
                              colour=discord.Colour.blue())
        embed.set_image(url=url)  # puts file in embed
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(fun(client))
