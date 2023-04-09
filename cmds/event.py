import discord
from discord.ext import commands
from core.classes import Cog_Extension, Gloable_Data
from core.errors import Errors
import json
import datetime
import asyncio

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        '''指令錯誤觸發事件'''
        Gloable_Data.errors_counter += 1
        error_command = '{0}_error'.format(ctx.command)
        if hasattr(Errors, error_command):  # 檢查是否有 Custom Error Handler
            error_cmd = getattr(Errors, error_command)
            await error_cmd(self, ctx, error)
            return
        else:  # 使用 Default Error Handler
            await Errors.default_error(self, ctx, error)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        '''成員加入觸發事件'''
        channel = self.bot.get_channel(int(jdata['Welcome_Channel']))
        await channel.send(f'{member.mention} 歡迎加入!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        '''成員離開觸發事件'''
        channel = self.bot.get_channel(int(jdata['Leave_Channel']))
        await channel.send(f'{member.mention} 離開了!')

    @commands.Cog.listener()
    async def on_message(self, msg):
        with open('keywords.json', 'r', encoding='utf8') as keyfile:
            kdata = json.load(keyfile)
        '''訊息觸發事件'''
        for keyword in kdata:
            if keyword == msg.content:

                # fetch user by id
                user = await self.bot.fetch_user(int(kdata[keyword]))
                # mention the id of the target user
                await msg.channel.send(user.mention)
            else:
                pass


def setup(bot):
    bot.add_cog(Event(bot))
