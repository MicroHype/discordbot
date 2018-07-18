import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import random

Client = discord.Client
client = commands.Bot(command_prefix = "!")
client.remove_command('help')

@client.event
async def on_ready():
    print("active")
    await client.change_presence(game=discord.Game(name="working in progress"))

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.content.upper().startswith('*SAY'):
        if message.author.id == "382207229182607361":
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
            await client.delete_message(message)
        else:
            await client.send_message(message.channel, "I don't think your allowed to use this command!")

@client.event
async def on_member_join(member):
    channelj = client.get_channel('444886297514082335')
    emb = (discord.Embed(description = " {0} Welcome to the server!".format(member.mention), color = 0xfffafa))
    emb.set_author(name = "Joined")
    await client.send_message(channelj, embed=emb)

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
async def server(ctx):
    embed = discord.Embed(title="{ctx.message.author.mention} this server info", color = 0xfffafa)
    embed.add_field(name="Members", value="len(_iterable_)")
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
    embed = discord.Embed(title="{} suggestion".format(ctx.message.author.name), description="{}".format(suggestion), color = 0xfffafa)
    embed.set_thumbnail(url=ctx.message.author.avatar_url)
    suggest_channel = client.get_channel('454336836345659397')
    suggest_send = await client.send_message(suggest_channel, embed=embed)
    await client.say("{}. Your suggestion has been sent :white_check_mark:".format(ctx.message.author.name))
    await client.add_reaction(suggest_send, "\N{Thumbs Up Sign}")
    await client.add_reaction(suggest_send, "\N{Thumbs Down Sign}")

@client.command(pass_context=True)
@commands.cooldown(5, BucketType.default.user)
async def memes(ctx):
    embed = discord.Embed(title = 'Memes', color =0xfffafa)
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
                           "https://fthmb.tqn.com/3K4sQEYGzUwtxpY7RcZYJH8pkLQ=/768x0/filters:no_upscale():max_bytes(150000):strip_icc()/success-56a9fd1f3df78cf772abee09.jpg"])
    embed.set_image(url=memes)
    await client.say(embed=embed)

client.run("NDU0NzYyMDE2MzEwMTY1NTA2.DfyKEA.rkSiQ8nM37tFPZ59mcmCHOnLckY")