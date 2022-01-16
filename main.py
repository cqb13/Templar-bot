from discord.ext import commands
import discord

client = commands.Bot(command_prefix='!', help_command=None)

TOKEN = ''  # the key of the bot


cogs = ['cogs.utility', 'cogs.fun', 'cogs.pic', 'cogs.cat']
for cog in cogs:
    try:
        client.load_extension(cog)  # loads cogs
    except Exception as e:  # error if cogs dont load
        print(f'could not load cog {cog}: {str(e)}')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('with cats'))
    print('Templar bot online')


@client.command()
async def talk(ctx):
    error = False
    user_id = f'{ctx.author}'
    embed = discord.Embed(title='talk',
                          description=f'information from talk command',
                          colour=discord.Colour.blue())
    ID = input('enter channel ID')
    channel = client.get_channel(int(ID))
    message = input('enter a message')
    try:
        a = await channel.send(message)

    except Exception as e:
        print(e)
        embed.add_field(name="info", value=f'channel ID: {ID}\nmessage: {message}\nerror: {e}')
        error = True
    # noinspection PySimplifyBooleanCheck
    if error != True:
        embed.add_field(name="info", value=f'channel ID: {ID}\nmessage: {message}')  # lazy so did it again
        await ctx.send(embed=embed)
    else:
        await ctx.send(embed=embed)
    print(f'{user_id} used talk\nchannel ID: {ID}\nmessage: {message}')


@client.command()
async def help(ctx):
    embed = discord.Embed(title='help',
                          colour=discord.Colour.blue())
    embed.add_field(name='utility',
                    value=f'- userinfo\n'
                          f'- servers\n'
                          f'- uuid\n'
                          f'- ping')
    embed.add_field(name='fun',
                    value=f'- better\n'
                          f'- spawn\n'
                          f'- skin\n'
                          f'- say\n'
                          f'- cat\n'
                          f'- fox\n'
                          f'- NA\n'
                          f'- IA\n'
                          f'- PA')
    await ctx.send(embed=embed)


@client.command()  # unloads cogs
@commands.has_permissions(ban_members=True)
async def uld(ctx, cogname=None, amount=1):
    user_id = ctx.author
    print(f'{user_id} used uld')
    if cogname is None:
        await ctx.send('I need a cog name to do that')  # error if no cog name
        return
    try:
        client.unload_extension(cogname)  # unloads cog
        await ctx.channel.purge(limit=amount)  # deletes cog command
    except Exception as e:
        await ctx.send(f'faild to unload {cogname}: {str(e)}')  # send error if cog does not unload
        print(f'faild to unload {cogname}: {str(e)}')  # prints error if cog does not unload
    else:
        print(f'{cogname} unloaded')  # prints if cog laoded


@client.command()  # loads cogs
@commands.has_permissions(kick_members=True)
async def ld(ctx, cogname=None, amount=1):
    user_id = ctx.author
    print(f'{user_id} used ld')
    if cogname is None:
        await ctx.send('I need a cog name to do that')  # error if not cog name
        return
    try:
        client.load_extension(cogname)  # gets cog name to load cog
        await ctx.channel.purge(limit=amount)  # deletes cog command
    except Exception as e:
        await ctx.send(f'faild to load {cogname}: {str(e)}')  # send error if cog did not load
        print(f'faild to load {cogname}: {str(e)}')  # prints error if cog did not load
    else:
        print(f'{cogname} loaded')  # prints if cog loaded


client.run(TOKEN)
