from symbol import decorator
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import sqlite3
from sqlite3 import Cursor
import random

Client = discord.Client()
client = commands.Bot(command_prefix = '!')
client.remove_command('help')

@client.event
async def on_ready():
    print("BotOfHype is online")
    await client.change_presence(game=discord.Game(name="!help", type=0))

@client.event
async def on_member_join(member):
    channel = client.get_channel('439442628103241739')
    emb = (discord.Embed(description = "{0} Welcome to the server!".format(member.mention), color = 0xfffafa))
    emb.set_author(name = "Joined")
    await client.send_message(channel, embed=emb)

@client.event
async def on_member_leave(member):
    channel = client.get_channel('439442628103241739')
    emb = (discord.Embed(description = "{0} Welcome to the server!".format(member.mention), color = 0xfffafa))
    emb.set_author(name = "Joined")


@client.command(pass_context=True)
async def info(ctx):
    embed = discord.Embed(title="BotOfHype", description="A Bot that will have many more updates to come :thumbsup:", color= 0xfffafa)
    embed.add_field(name="Author", value="Hype#0980")
    embed.add_field(name="Server count", value=f"{len(client.servers)}")
    embed.add_field(name="Invite", value="https://discord.gg/E9WmZN6")
    embed.add_field(name="Bot Invite", value="https://discordapp.com/api/oauth2/authorize?client_id=454762016310165506&permissions=0&scope=bot")
    await client.say(embed=embed)

@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="BotOfHype", color=0xfffafa)
    embed.set_thumbnail(url="https://i.pinimg.com/originals/07/71/4f/07714f27254fd9a4771c3e604c7a62fd.jpg")
    embed.add_field(name="Progress", value="BotOfHype is still in progress please wait in the following week in order for it to work and it will have many updates to come")
    embed.set_footer(text="BotOfHype Made by Hype#0980")
    await client.say(embed=embed)

@client.command(pass_context=True)
async def user(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="This is what I could find.", color= 0xfffafa)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def suggest(ctx, *, suggestion: str):
    embed = discord.Embed(title="{} suggestion".format(ctx.message.author.name), description="```{}```".format(suggestion), color = 0xfffafa)
    embed.set_thumbnail(url=ctx.message.author.avatar_url)
    embed.add_field(name="Channel", value='<#444885303002660864>', inline=True)
    suggest_channel = client.get_channel('467412143843573772')
    suggest_send = await client.send_message(suggest_channel, embed=embed)
    await client.say("{}. Your suggestion has been sent <a:thinkloading:456846926994997259>".format(ctx.message.author.name))
    await client.add_reaction(suggest_send, "\N{Thumbs Up Sign}")
    await client.add_reaction(suggest_send, "\N{Thumbs Down Sign}")

@client.command(pass_context=True)
async def memes(ctx):
    embed = discord.Embed(title = 'Memes', color = 0xfffafa)
    memes = random.choice(['https://scontent-arn2-1.xx.fbcdn.net/v/t1.0-9/32588537_1666484800095556_7221967081359540224_n.png?_nc_cat=0&oh=14a9181c3c192f41b9f6c7d94759f2af&oe=5B8F8B0C',
                           "https://scontent-lhr3-1.xx.fbcdn.net/v/t1.0-9/32423257_2821407631210139_3517029460337491968_n.jpg?_nc_cat=0&oh=cb6680a7d83a22b8a6b7b9b7c5720e2b&oe=5B8A393E",
                           "https://scontent-lhr3-1.xx.fbcdn.net/v/t1.0-9/32349681_2821026131248289_2786726170652049408_n.jpg?_nc_cat=0&oh=0454f293adf574d0fc5dce0d1754437e&oe=5B8BE46A",
                           "https://scontent-lhr3-1.xx.fbcdn.net/v/t1.0-9/32145845_2818368094847426_2713064273185079296_n.jpg?_nc_cat=0&oh=1618b2bac96ebc256f7ab7aca2026e0c&oe=5B9A61DC",
                           "https://scontent-lhr3-1.xx.fbcdn.net/v/t1.0-9/32407101_1683422221772606_451741718140682240_n.jpg?_nc_cat=0&oh=3b1c082e3f62341f2b31cfb5b6d4bce4&oe=5B7DEF0D",
                           "https://scontent-lhr3-1.xx.fbcdn.net/v/t1.0-9/32323119_1683570305091131_235651923384991744_n.jpg?_nc_cat=0&oh=aca738c250f44c2c7274e12dafd93472&oe=5B899FCB",
                           "https://cdn.discordapp.com/attachments/391471297139572736/446403016170536961/unknown.png",
                           "https://cdn.discordapp.com/attachments/391471297139572736/446696904785657867/CommieMeme.png",
                           "https://scontent-lhr3-1.xx.fbcdn.net/v/t1.0-9/32900282_2832146943469541_7043111161251758080_n.jpg?_nc_cat=0&oh=98f561b954894d07ea7eb0917333f923&oe=5B7BB4A6",
                           "https://scontent-lhr3-1.xx.fbcdn.net/v/t1.0-9/32722745_2087000408209083_6532180069308170240_n.jpg?_nc_cat=0&oh=bb553ff7caeac54aeab0352a5121f66a&oe=5B992972",
                           "https://fthmb.tqn.com/3K4sQEYGzUwtxpY7RcZYJH8pkLQ=/768x0/filters:no_upscale():max_bytes(150000):strip_icc()/success-56a9fd1f3df78cf772abee09.jpg",
                           "https://cdn.discordapp.com/attachments/391471297139572736/455438246676004864/3AM.jpg",
                           "https://cdn-img.essence.com/sites/default/files/styles/pronto_original/public/1478865384/Trump%20Memes-1.jpg?itok=hTB_GpGT",
                           "https://i.pinimg.com/736x/2f/49/bf/2f49bf2989e37482c32c6c3ba0bf6af8--work-funnies-work-humor.jpg"])
    embed.set_image(url=memes)
    embed.set_footer(text="BotOfHype Made by Hype#0980")
    await client.say(embed=embed)


@client.command(pass_context=True)
async def clear(ctx, *, amount : int):
    if ctx.message.author.server_permissions.manage_messages:
         channel = ctx.message.channel
         messages = []
         async for message in client.logs_from(channel, limit=int(amount) + 1):
            messages.append(message)
         await client.delete_messages(messages)
    else:
        await client.say("{} You are not allowed to use this command.").format(ctx.message.author.name)

@client.command(pass_context=True)
async def kick(ctx, user: discord.Member, *, reason: str):
    msg = "{} was kicked by {}, because {}".format (user.mention, ctx.message.author.mention, reason)
    await client.say(msg)
    await client.kick(user)

@client.command(pass_context=True)
async def mute(ctx, user: discord.Member, *, reason: str):
    msg = "{} was muted by {}, because {}".format (user.mention, ctx.message.author.mention, reason)
    await client.say(msg)
    await client.mute(user)

@client.command(pass_context = True)
async def unmute(ctx, member: discord.Member=None, reason: str=None):
  if ctx.message.author.server_permissions.manage_roles:
   if not member or not reason:
    await client.say("Invalid args provided.")
   else:
    role = discord.utils.get(member.server.roles, name='Muted')
    await client.remove_roles(member, role)
       await client.say(f"{member} has been unmuted!")
   else:
    await client.say(":x: You do not have permission to execute this command!")

conn = sqlite3.connect('MoneyBot.db', isolation_level=None)
db = conn.cursor()

conn.execute("""CREATE TABLE IF NOT EXISTS Users(
                            UserID TEXT,
                            COINS INTERGER)""")

def create_user_if_not_exist(user_id):
    user_id = str(user_id)
    if user_id.startswith("('"):
        user_id = user_id[2:-3]
    res = conn.execute("SELECT COUNT(*) From Users WHERE UserID=?", (user_id,))
    user_count = res.fetchone()[0]
    if user_count < 1:
        print("Creating user with id " + str(user_id))
        conn.execute("INSERT INTO Users VALUES (?, ?)", (user_id, 0))
    conn.commit()

def get_coins(user_id):
    create_user_if_not_exist(user_id)
    res =  conn.execute("SELECT Coins FROM Users WHERE UserID=?", (user_id,))
    user_coins = int(res.fetchone()[0])
    conn.commit()
    return user_coins

def update_coins(user_id, what, amount):
    if what == '+':
        user_coins = get_coins(user_id)
        user_coins = user_coins + amount
        conn.execute("UPDATE Users Set Coins=? WHERE UserID=?", (user_coins, user_id))
        conn.commit()
    if what == '-':
        user_coins = get_coins(user_id)
        user_coins = user_coins - amount
        conn.execute("UPDATE Users Set Coins=? WHERE UserID=?", (user_coins, user_id))
        conn.commit()

@client.command(pass_context=True)
@commands.cooldown(1, 86400, commands.BucketType.user)
async def coins(ctx):
    print('coins')
    await client.say(str(get_coins(ctx.message.author.id)))

#
@client.event
async def on_command_error(ctx, error):
    if isinstance(ctx, discord.ext.commands.errors.CommandOnCooldown):
        await client.send_message(error.message.channel, ctx)

@client.command(pass_context=True)
async def leaderboard(ctx):
    res1 = conn.execute("SELECT Coins FROM Users ORDER BY Coins DESC;")
    res1 = res1.fetchall()
    embed = discord.Embed(title="Most coins", description="The top users with the most Coins", color=0xfffafa)
    res2 = conn.execute("SELECT UserID FROM Users ORDER BY Coins DESC;")
    res2 = res2.fetchall()
    for counter in range(0, 1):
        for member in ctx.message.server.members:
            counter_id = str(res2[counter])[2:-3]
            print(counter_id)
            print(member.id)
            if counter_id == member.id:
                embed.add_field(name=member.display_name, value=str(res1[counter])[1:-4], inline=False)
                break
    await client.say(embed=embed)

@client.event
async def on_message(message):
    await client.process_commands(message)
    update_coins(message.author.id, "+" ,1)
    if_coin = random.choice([1, 2])
    if if_coin == 1:
        update_coins(message.author.id, "+", 1)

client.run("NDY3NDI0OTE0MDA2MDgxNTM2.Diqelg.4nZ3YHgHeTEYqoQiKzheBrhf3_8")
