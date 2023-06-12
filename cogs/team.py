import discord
from discord.ext import commands
from dislash import InteractionClient


class Team(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

