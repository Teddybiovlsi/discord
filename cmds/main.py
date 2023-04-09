import discord
from discord.ext import commands
from core.classes import Cog_Extension
from core import check
import json
import os
import random
import requests as req

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

with open('keywords.json', 'r', encoding='utf8') as keyfile:
    keywordsdata = json.load(keyfile)


class Main(Cog_Extension):

    '''
    等待使用者回覆檢查 (需要時複製使用)
    async def user_respone():
            def check(m):
                    return m.author == ctx.author and m.channel == ctx.channel
            respone = await self.bot.wait_for('message', check=check)
            return respone

    respone_msg = await user_respone
    '''

    @commands.command()
    async def ping(self, ctx):
        '''Bot 延遲'''
        await ctx.send(f'{round(self.bot.latency*1000)} ms')

    @commands.command()
    @check.valid_user()  # 檢查權限, 是否存在於效人員清單中, 否則無法使用指令
    async def test(self, ctx):
        '''有效人員 指令權限測試'''
        await ctx.send('你好 !')

    @commands.command()
    async def sayd(self, ctx, *, content: str):
        '''訊息覆誦'''
        if "@everyone" in content:
            await ctx.send(f"{ctx.author.mention} 請勿標註 `everyone` !")
            return
        else:
            await ctx.message.delete()
        await ctx.send(content)

    @commands.command()
    async def add_keyword(self, ctx, keyword: str, *, content: int):
        '''新增關鍵字'''
        if keyword in keywordsdata:
            await ctx.send(f"關鍵字 `{keyword}` 已存在 !")
            return
        else:
            keywordsdata[keyword] = content
            with open('keywords.json', 'w', encoding='utf8') as keyfile:
                json.dump(keywordsdata, keyfile, indent=4)
            await ctx.send(f"新增關鍵字 `{keyword}` 成功 !")

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(title="About P_Base-Bot",
                              description="Made Bot Easier !", color=0x28ddb0)
        # embed.set_thumbnail(url="#")
        embed.add_field(name="開發者 Developers",
                        value="Proladon#7525 (<@!149772971555160064>)", inline=False)
        embed.add_field(
            name="源碼 Source", value="[Link](https://github.com/Proladon/Proladon-DC_BaseBot)", inline=True)
        embed.add_field(name="協助 Support Server",
                        value="[Link](https://discord.gg/R75DXHH)", inline=True)
        embed.add_field(name="版本 Version", value="0.1.0 a", inline=False)
        embed.add_field(name="Powered by", value="discord.py v{}".format(
            discord.__version__), inline=True)
        embed.add_field(name="Prefix", value=jdata['Prefix'], inline=False)
        embed.set_footer(text="Made with ❤")
        await ctx.send(embed=embed)

    @commands.command()
    async def show_keyword(self, ctx):
        '''顯示關鍵字'''
        keyword_list = ""
        for keyword in keywordsdata:
            keyword_list += f"{keyword} : {keywordsdata[keyword]} \n"
        embed = discord.Embed(title="關鍵字列表 Keyword List",
                              description=keyword_list, color=0x28ddb0)
        await ctx.send(embed=embed)

    # 顯示命令列表
    @commands.command()
    async def show_command(self, ctx):
        '''顯示指令列表'''
        command_list = ""
        for command in self.bot.commands:
            command_list += f"{command} : {command.help} \n"
        embed = discord.Embed(title="指令列表 Command List",
                              description=command_list, color=0x28ddb0)
        await ctx.send(embed=embed)

    @commands.command()
    async def vote(self, ctx, question: str, *options):
        '''投票'''
        reactions = ['👍', '👎']
        message = f"{question}\n"
        for i, option in enumerate(options):
            message += f"{i+1}. {option}\n"
        message += "\n請以 👍 或 👎 進行投票."

        poll = await ctx.send(message)
        for reaction in reactions:
            await poll.add_reaction(reaction)


def setup(bot):
    bot.add_cog(Main(bot))
