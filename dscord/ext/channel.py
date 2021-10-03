from typing import Union

import discord
from discord.ext import commands

from dscord.func import clamp, randoms

AnyChannel = Union[
    discord.CategoryChannel, 
    discord.VoiceChannel, 
    discord.StageChannel, 
    discord.TextChannel
]


class Channel(commands.Cog):
    @commands.command('ccat', brief='Create category channel')
    async def create_category_channel(
        self, ctx, *, name: str = randoms()
    ) -> None:
        await ctx.guild.create_category_channel(name)
 
    @commands.command('cstg', brief='Create stage channel')
    async def create_stage_channel(
        self, ctx, *, name: str = randoms()
    ) -> None:
        await ctx.guild.create_stage_channel(name)
   
    @commands.command('ctxt', brief='Create text channel')
    async def create_text_channel(
        self, ctx, *, name: str = randoms()
    ) -> None:
        await ctx.guild.create_text_channel(name)

    @commands.command('cvo', brief='Create voice channel')
    async def create_voice_channel(
        self, ctx, name: str = randoms()
    ) -> None:
        await ctx.guild.create_voice_channel(name)

    @commands.command('ctxts', brief='Create text channels')
    async def create_text_channels(
        self, ctx, amount: int, *, name: str = None
    ) -> None:
        if name is None: 
            name = randoms()
        category = await ctx.guild.create_category_channel(name)
        amount = clamp(amount, min_i=1, max_i=50)
        for i in range(amount):
            if name is None:
                name = randoms()
            else:
                name += f'-{i}'
            await category.create_text_channel(name)

    @commands.command('cdel', brief='Delete channel')
    async def delete_any_channel(
        self, ctx, *channels: AnyChannel
    ) -> None:
        if not channels:
            await ctx.channel.delete()
        for channel in channels:
            if channel is discord.CategoryChannel:
                for c in channel.channels: 
                    await c.delete()
            await channel.delete()


def setup(bot):
    bot.add_cog(Channel())
