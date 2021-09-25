import nextcord
from nextcord.ext import commands
import asyncio

from goldy_func import *
from goldy_utility import *
import config.msg as msg

cog_name = "simp"

class simp(commands.Cog, name="😘Simp"):
    def __init__(self, client):
        self.client = client
        self.cog_name = cog_name
        self.help_command_index = None

    @commands.command()
    async def simp(self, ctx):
        if await can_the_command_run(ctx, cog_name) == True:
            pass

def setup(client):
    client.add_cog(simp(client))

#Need Help? Check out this: {youtube playlist}