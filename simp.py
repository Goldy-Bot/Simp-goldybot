import nextcord
from nextcord.ext import commands
import asyncio
import datetime
import random

from goldy_func import *
from goldy_utility import *
import config.msg as msg

from cogs.database import database

from cogs.simp_cog import msg as simp_msg

cog_name = "simp"

class simp(commands.Cog, name="😘Simp"):
    def __init__(self, client):
        self.client = client
        self.cog_name = cog_name
        self.help_command_index = None

    @commands.command()
    @commands.cooldown(1, 180, commands.BucketType.user)
    async def simp(self, ctx, member:nextcord.Member = None):
        if await can_the_command_run(ctx, cog_name) == True:
            if await database.member.checks.has_item(ctx, "!simp"):
                if member == None:
                    await ctx.send(msg.help.command_usage.format(ctx.author.mention, "!simp {member}"))
                    ctx.command.reset_cooldown(ctx)
                else:
                    (ctx, member_ctx) = await goldy_methods.ctx_merger.merge(ctx, member)

                    #Check if member mentioned is simpable first.
                    member_data = await database.member.pull(member_ctx)
                    if await simp.member.checks.is_simpable(ctx, member_data):
                        #Get random image.
                        random_image = await simp.random_simp_image.get()
                        random_image_2 = await simp.random_simp_image.get()

                        #Send embeds
                        (guild_embed, dm_embed) = await simp.embed.create(member_ctx)

                        guild_embed.set_image(url=random_image.url)
                        await ctx.send(embed=guild_embed)

                        dm_embed.set_image(url=random_image_2.url)
                        await member_ctx.author.send(embed=dm_embed)

                    else:
                        await ctx.send(simp_msg.simp.failed.not_simpable.format(ctx.author.mention))
                        ctx.command.reset_cooldown(ctx)
            else:
                await ctx.send(msg.error.do_not_have_item.format(ctx.author.mention))
                ctx.command.reset_cooldown(ctx)

    @simp.error
    async def command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.author.send(msg.error.cooldown.format(datetime.timedelta(seconds=round(error.retry_after))))
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(msg.error.member_not_found.format(ctx.author.mention))
        else:
            await goldy.log_error(ctx, self.client, error, f"{cog_name}.simp")

    class member():
        class checks():
            @staticmethod
            async def is_simpable(ctx, member_data): #Checks if member is simpable or not.
                simpable = await simp.member.get(ctx, member_data)

                if simpable == True:
                    return True
                else:
                    return False

        @staticmethod
        async def get(ctx, member_data): #Get's the "simpable" object from the member data.
            try:
                simpable = member_data.simpable #The new object name.
                return simpable
            except AttributeError as e:
                try:
                    simpable = member_data.simpAble #The old object name.
                    return simpable
                except AttributeError as e:
                    await database.member.add_object(ctx, "simpable", False)
                    return False

    class random_simp_image():
        @staticmethod
        async def update(): #Checks if "simp_images.json" is in config.
            json_file_name = "simp_images.json"

            if not json_file_name in os.listdir("config\\"):
                #Create and write to level_up_msgs.json
                simp_images_file = open(f"config\\{json_file_name}", "x")
                simp_images_file = open(f"config\\{json_file_name}", "w")
                
                json.dump({"1" : {"name": "Gawr Gura", 
                "url" : "https://i1.sndcdn.com/artworks-pNNuvE1yQkD4BByH-DMCDdw-t500x500.jpg"}}, simp_images_file) #Dumping the example layout in the json file.

        @staticmethod
        async def get(): #Get's random simp image from "simp_images.json".
            json_file_name = "simp_images.json"

            try:
                f = open (f'config\\{json_file_name}', "r", encoding="utf8")
                simp_images_normal = json.loads(f.read())

            except FileNotFoundError as e:
                print_and_log("warn", f"'{json_file_name}' was not found. Running update function and trying again. >>> {e}")
                await simp.random_simp_image.update()

                f = open (f'config\\{json_file_name}', "r", encoding="utf8")
                simp_images_normal = json.loads(f.read())


            max_images_num = len(simp_images_normal.keys())
            random_num = random.randint(1, max_images_num) #Test to see what happends if max num is also 1.

            level_up_message = json.dumps(simp_images_normal[str(random_num)])
            level_up_message_formatted = json.loads(level_up_message, object_hook=lambda d: SimpleNamespace(**d))

            return level_up_message_formatted

    class embed():
        @staticmethod
        async def create(ctx): #Creates the images needed.
            guild_embed = nextcord.Embed(title="**💕 SIMP EXPOSED!!!**", 
            description=simp_msg.simp.embed.guild_context.format(ctx.author.mention, ctx.author.mention, ctx.author.mention), 
            color=settings.Aki_Pink)
            guild_embed.set_footer(text=simp_msg.footer.type_1)

            dm_embed = nextcord.Embed(title="**💗 YOUR A SIMP!!!**", description=simp_msg.simp.embed.dm_context, color=settings.Aki_Pink)
            dm_embed.set_footer(text=simp_msg.footer.type_1)

            return guild_embed, dm_embed

def setup(client):
    client.add_cog(simp(client))

#Need Help? Check out this: {youtube playlist}