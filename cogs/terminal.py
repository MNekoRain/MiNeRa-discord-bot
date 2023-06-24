from disnake import Option, Permissions, NotFound
from disnake.ext import commands
from ..helpers import console
from lang.language import get_lang


class Terminal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="send",
                            description="A send message in specified channel",
                            default_member_permissions=Permissions(send_messages=True, send_messages_in_threads=True),
                            options=[
                                Option(
                                    name="message",
                                    description="Message whom need send to channel",
                                    required=True,
                                    type=3
                                ),
                                Option(
                                    name="channel_id",
                                    description="A channel id where will be send a message. If not found then is this channel",
                                    required=False,
                                    type=3
                                )
                            ])
    async def send(self, ctx, message: str, channel_id: int = None):
        channel = ctx.channel
        if channel_id is not None:
            channel = self.bot.get_channel(channel_id)
            if channel is None:
                channel = ctx.channel
        return await channel.send(message)

    @commands.slash_command(name="respond",
                            description="A send respond to message in specified channel",
                            default_member_permissions=Permissions(send_messages=True, send_messages_in_threads=True),
                            options=[
                                Option(
                                    name="message",
                                    description="A respond to message whom need send to channel",
                                    required=True,
                                    type=3
                                ),
                                Option(
                                    name="channel_id",
                                    description="A channel id where will be send a respond to message. If not found then is this channel",
                                    required=False,
                                    type=3
                                ),
                                Option(
                                    name="respond_message_id",
                                    description="A message id which nees send respond",
                                    required=False,
                                    type=3
                                )
                            ])
    async def respond(self, ctx, message: str, channel_id: str = None, respond_message_id: str = None):
        channel = ctx.channel
        if channel_id is not None:
            channel = self.bot.get_channel(channel_id)
            if channel is None:
                channel = ctx.channel
        try:
            respond_message = await channel.get_partial_message(respond_message_id)
        except NotFound:
            return await ctx.channel.send(message)
        return await respond_message.reply(message)


async def setup(bot):
    await bot.add_cog(Terminal(bot))