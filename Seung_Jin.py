import discord
import asyncio
import os
import datetime
import time
import warnings
import re

from discord.ext import tasks, commands
from discord.ext import commands
from datetime import datetime
from typing import Optional
from discord import Embed, Member
from asyncio import sleep


Custom_Message = input("[>] Input Custom Message1 : ")

Token = "NzUyMDcxODA3OTcxODg1MTQ5.X1STcw.8UTTiqnkgGZSc0NRWXkvkaQCkqI"

client = discord.Client()
client = commands.Bot(command_prefix="/")

#EVENT#
@client.event
async def on_ready():
    print("[-]", client.user.id)
    print("[-]", client.user.name)
    await client.change_presence(activity=discord.Streaming(name=Custom_Message, url="https://twitch.tv/Discord"))

@client.event
async def on_member_join(member):
    mention = member.mention
    guild = member.guild
    await member.create_dm()
    await member.dm_channel.send(str(f"{mention}\n**{guild} 에 오신걸 진심으로 환영합니다**").format(mention, guild = guild))

    embed = discord.Embed(title=str("***New Member Joined***"), colour = 0x11ff00, description = str(f"{mention} Joined to the {guild} ").format(mention = mention, guild = guild))
    embed.set_thumbnail(url = f"{member.avatar_url}")
    embed.set_author(name = f"{member.name}", icon_url = f"{member.avatar_url}")
    embed.set_footer(text = f"{member.guild}", icon_url = f"{member.guild.icon_url}")
    ## embed.timestamp = datetime.datetime.utcnow()
    embed.add_field(name = "User ID : ", value = member.id)
    embed.add_field(name = "User Name : ", value = member.display_name)
    embed.add_field(name = "Server Name : ", value = guild)
    embed.add_field(name = "User Serial : ", value = len(list(guild.members)))
    embed.add_field(name = "Created_at : ", value = member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name = "Joined_at : ", value = member.joined_at.strftime("%a, %#d %B %Y %I:%M %p UTC"))

    channel = discord.utils.get(member.guild.channels, id = int("710102459585921037" and "752031432477638778"))
    await channel.send(embed=embed)

@client.event
async def on_member_remove(member):
    mention = member.mention
    guild = member.guild

    embed = discord.Embed(title=str("***Member Leaved***"), colour = 0xff0000, description = str(f"{mention} leaved from {guild} ").format(mention = mention, guild = guild))
    embed.set_thumbnail(url = f"{member.avatar_url}")
    embed.set_author(name = f"{member.name}", icon_url = f"{member.avatar_url}")
    embed.set_footer(text = f"{member.guild}", icon_url = f"{member.guild.icon_url}")
    ## embed.timestamp = datetime.datetime.utcnow()
    embed.add_field(name = "User ID : ", value = member.id)
    embed.add_field(name = "User Name : ", value = member.display_name)
    embed.add_field(name = "Server Name : ", value = guild)
    embed.add_field(name = "User Serial : ", value = len(list(guild.members)))
    embed.add_field(name = "Created_at : ", value = member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name = "Joined_at : ", value = member.joined_at.strftime("%a, %#d %B %Y %I:%M %p UTC"))

    channel = discord.utils.get(member.guild.channels, id = int("710102459585921037" and "752031432477638778"))
    await channel.send(embed=embed)

#COMMAND#
@client.command()
async def 청소(ctx, amount : int):
    try:
        if ctx.author.guild_permissions.manage_messages:
            await ctx.channel.purge(limit=amount)
            await ctx.send("``메시지를 삭제했습니다.``")
        else:
            await ctx.send("``해당 명령어를 사용할 권한이 없습니다.``")
    except:
        pass

@client.command()
@commands.has_permissions(kick_members=True)
async def 강퇴(ctx, member  : discord.Member, *, reason=None):
    try:
        if ctx.author.guild_permissions.manage_messages:
            await member.kick(reason=reason)
            await ctx.send("``강퇴 완료``")
        else:
            await ctx.send("``해당 명령어를 사용할 권한이 없습니다.``")
    except:
        pass

@client.command()
@commands.has_permissions(ban_members=True)
async def 밴(ctx, user: discord.Member, *, reason=None):
    try:
        if ctx.author.guild_permissions.manage_messages:
            await user.ban(reason=reason)
            await ctx.send(f"``{user} 님을 밴했습니다.``")
        else:
            await ctx.send("``해당 명령어를 사용할 권한이 없습니다.``")
    except:
        pass

@client.command()
async def 언밴(ctx, *, member):
    banned_user = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    try:
        if ctx.author.guild_permissions.manage_messages:

            for ban_entry in banned_user:
                user = ban_entry.user

                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    await ctx.send(f"``{user} 님을 언밴했습니다.``")
                    return
        else:
            await ctx.send("``해당 명령어를 사용할 권한이 없습니다.``")
    except:
        pass


@client.command()
async def ping(ctx):
    await ctx.send(f"``{round(client.latency * 1000)}ms``")

@client.command()
async def 사용불가1(ctx):
        try:
            if ctx.author.guild_permissions.manage_messages:
                author = ctx.guild.get_member(int(ctx.author.id))
                embed = discord.Embed(color=0xff0000)
                channel2 = "752031568528408589"
                embed.set_author(name=author, icon_url = ctx.author.avatar_url)
                embed.add_field(name='봇 사용불가', value="오프라인 또는 점검 중")
                ##embed.set_image(url="https://cdn.discordapp.com/attachments/748818001414848582/752053618835718184/GIF.gif")
                await client.get_channel(int(channel2)).send(embed=embed)
            else:
                ctx.send("``해당 명령어를 사용할 권한이 없습니다.``")
        except:
            pass

@client.command()
async def 사용불가2(ctx):
        try:
            if ctx.author.guild_permissions.manage_messages:
                author = ctx.guild.get_member(int(ctx.author.id))
                embed = discord.Embed(color=0xff0000)
                channel3 = "710104551277068288"
                embed.set_author(name=author, icon_url = ctx.author.avatar_url)
                embed.add_field(name='봇 사용불가', value="오프라인 또는 점검 중")
                ##embed.set_image(url="https://cdn.discordapp.com/attachments/748818001414848582/752053618835718184/GIF.gif")
                await client.get_channel(int(channel3)).send(embed=embed)
            else:
                ctx.send("``해당 명령어를 사용할 권한이 없습니다.``")
        except:
            pass

@client.command()
async def 사용가능1(ctx):
        try:
            # 메시지 관리 권한 있을시 사용가능
            if ctx.author.guild_permissions.manage_messages:
                author = ctx.guild.get_member(int(ctx.author.id))
                embed = discord.Embed(color=0x00ff4c)
                channel2 = "752031568528408589"
                embed.set_author(name=author, icon_url = ctx.author.avatar_url)
                embed.add_field(name='봇 사용가능', value="온라인 또는 점검 완료")
                ##embed.set_image(url="https://cdn.discordapp.com/attachments/748818001414848582/752053618835718184/GIF.gif")
                await client.get_channel(int(channel2)).send(embed=embed)
            else:
                ctx.send("``해당 명령어를 사용할 권한이 없습니다.``")
        except:
            pass

@client.command()
async def 사용가능2(ctx):
        try:
            # 메시지 관리 권한 있을시 사용가능
            if ctx.author.guild_permissions.manage_messages:
                author = ctx.guild.get_member(int(ctx.author.id))
                embed = discord.Embed(color=0x00ff4c)
                channel2 = "710104551277068288s"
                embed.set_author(name=author, icon_url = ctx.author.avatar_url)
                embed.add_field(name='봇 사용가능', value="온라인 또는 점검 완료")
                ##embed.set_image(url="https://cdn.discordapp.com/attachments/748818001414848582/752053618835718184/GIF.gif")
                await client.get_channel(int(channel2)).send(embed=embed)
            else:
                ctx.send("``해당 명령어를 사용할 권한이 없습니다.``")
        except:
            pass

@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    #메시지 관리권한이 있을시 사용가능
                    if message.author.guild_permissions.manage_messages:    
                        author = message.guild.get_member(int(message.author.id))
                        embed = discord.Embed(color=0x1DDB16)
                        embed.set_author(name=author, icon_url = message.author.avatar_url)
                        embed.add_field(name="752030459944239165", value=msg, inline=True)
                        embed.set_footer(text = "Pleasant DM Bot#6646")
                        await i.send(embed=embed)
                except:
                    pass

client.run(Token)