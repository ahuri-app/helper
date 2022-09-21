import nextcord
from config import guilds
from nextcord.ext import commands
from nextcord import slash_command
from nextcord import SlashOption

# cog
class poll(commands.Cog):
    def __init__(self, bot): self.bot = bot
    
    @slash_command(name="poll", description="Make a poll!", guild_ids=guilds)
    async def poll(
        self,
        interaction: nextcord.Interaction,
        poll_title: str = SlashOption(
            required = True,
            description = "Name of poll",
        ),
        anonymous: bool = SlashOption(
            required = True,
            description = "Send as anonymous"
        ),
        option1: str = SlashOption(
            required = True,
            description = "1st Option"
        ),
        option2: str = SlashOption(
            required = False,
            description = "2nd Option"
        ),
        option3: str = SlashOption(
            required = False,
            description = "3rd Option"
        ),
        option4: str = SlashOption(
            required = False,
            description = "4th Option"
        ),
        option5: str = SlashOption(
            required = False,
            description = "5th Option"
        ),
        option6: str = SlashOption(
            required = False,
            description = "6th Option"
        ),
        option7: str = SlashOption(
            required = False,
            description = "7th Option"
        ),
        option8: str = SlashOption(
            required = False,
            description = "8th Option"
        ),
        option9: str = SlashOption(
            required = False,
            description = "9th Option"
        ),
        option10: str = SlashOption(
            required = False,
            description = "10th Option"
        )
    ):
        userroles = []
        for x in interaction.user.roles:
            userroles.append(x.id)
        
        if not anonymous:
            try:
                uavatar = interaction.user.avatar.url
            except:
                uavatar = interaction.user.default_avatar.url
        
        channel = interaction.channel
        
        options = [option1]
        if option2 != None:
            options.append(option2)
        if option3 != None:
            options.append(option3)
        if option4 != None:
            options.append(option4)
        if option5 != None:
            options.append(option5)
        if option6 != None:
            options.append(option6)
        if option7 != None:
            options.append(option7)
        if option8 != None:
            options.append(option8)
        if option9 != None:
            options.append(option9)
        if option10 != None:
            options.append(option10)

        numbers = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
        optionstr = ""
        for x in range(len(options)):
            y = numbers[x]
            z = options[x]
            optionstr = optionstr + f"{y} {z}\n"
        
        try:
            await interaction.response.send_message("Sending poll message...", ephemeral=True)                
        except:
            pass
        
        embed = nextcord.Embed(title=poll_title, description=optionstr, color=nextcord.Colour.random())
        if not anonymous:
            embed.set_footer(text=f"Poll by {interaction.user.name}", icon_url=uavatar)
        message = await channel.send(embed=embed)
        for x in range(len(options)):
            await message.add_reaction(numbers[x])

def setup(bot):
    bot.add_cog(poll(bot))