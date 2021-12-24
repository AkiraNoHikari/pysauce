#!/usr/bin/env python3

import discord
import saucenao_api
import platform
import datetime
from os import environ

client = discord.Bot()
start = datetime.datetime.now()
sauce_nao = saucenao_api.SauceNao(environ.get("SAUCENAO_TOKEN"))


def embed_from_result(result: saucenao_api.BasicSauce):
    embed = discord.Embed(title="Found the Sauce", description="\n".join(result.urls))
    embed.set_thumbnail(url=result.thumbnail)
    embed.add_field(name="Title", value=result.title, inline=True)
    embed.add_field(name="Author", value=result.author, inline=True)
    embed.add_field(name="Similarity", value=f"{result.similarity}%", inline=True)
    return embed


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    activity = discord.Activity(name="/help", type=discord.ActivityType.playing)
    await client.change_presence(activity=activity)


@client.message_command(name="Get Sauce", guild_ids=[923228837968511056])
async def get_sauce(ctx, msg: discord.Message):

    if len(msg.attachments) == 0:
        await ctx.response.send_message(
            content="No image attachment detected!", ephemeral=True
        )
        return

    if len(msg.attachments) > 1:

        embed_list = list()

        for attachment in msg.attachments:
            response = sauce_nao.from_url(attachment.url)

        if not response.results:
            embed = discord.Embed(title="No Sauce found", description="Sowwy I could not find the Sauce!", ephemeral=True)
            await ctx.response.send_message(embeds=embed_list, ephemeral=True)
        else:
            embed = embed_from_result(response.results[0])
            embed_list.append(embed)
            await ctx.response.send_message(embeds=embed_list, ephemeral=True)

    else:
        response = sauce_nao.from_url(msg.attachments[0].url)
        embed = embed_from_result(response.results[0])

        await ctx.response.send_message(embed=embed, ephemeral=True)


@client.slash_command(
    name="help", description="Prints the Sauce manual", guild_ids=[923228837968511056]
)
async def help(ctx):
    embed = discord.Embed(
        title="Sauce Manual",
        description=f"This is the manual of Sauce which shows you what Sauce can do\n_Note that Sauce currently only supports desktop environments_",
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/434850895394766868.png")
    embed.add_field(
        name="How do I use Sauce?",
        value="To get the sauce of an image follow this instruction\n`Right click (on a message containing an image) > Apps > Get Sauce`",
        inline=False,
    )
    embed.add_field(
        name="Found an issue?",
        value="Let me know and create an entry on the repo, you can find the link to the repo by using `/about`",
        inline=False,
    )
    embed.add_field(name="Available commands", value=f"`/help`\n`/about`")
    await ctx.response.send_message(embed=embed, ephemeral=True)


@client.slash_command(
    name="about",
    description="Prints information about the bot",
    guild_ids=[923228837968511056],
)
async def about(ctx):

    now = datetime.datetime.now()
    uptime = now.strftime("%H:%M:%S %d/%m/%Y")

    embed = discord.Embed(
        title=f"About Pysauce",
        description="This is the information tab which shows you stats about Pysauce",
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/434850897273815062.png")
    embed.set_author(
        name="AkiraNoHikari",
        url="https://github.com/AkiraNoHikari",
        icon_url="https://avatars.githubusercontent.com/u/38864051",
    )
    embed.add_field(
        name="Pysauce",
        value=f"`Guilds {len(client.guilds)}`\n`Up since {uptime}`",
        inline=False,
    )
    embed.add_field(name="Tools", value=f"`Python {platform.python_version()}`")
    embed.add_field(
        name="External Modules",
        value=f"`py-cord {discord.__version__}`\n`saucenao-api {saucenao_api.__version__}`",
    )
    embed.add_field(
        name="Author",
        value=f"`Akira アキラ#8840`\n[Github | AkiraNoHikari](https://github.com/AkiraNoHikari)",
    )
    embed.add_field(
        name="Github Repository",
        value=f"Found an issue? Let me know and create an entry on the repo!\nhttps://github.com/AkiraNoHikari/pysauce\nLicensed under the [MIT](https://github.com/AkiraNoHikari/pysauce/blob/master/LICENSE) license",
        inline=False,
    )
    await ctx.response.send_message(embed=embed, ephemeral=True)


client.run(environ.get("BOT_TOKEN"))