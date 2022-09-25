import random

import nextcord
from nextcord.ext import commands


EMOTICONS = [
    " >_<",
    " >w<",
    "~",
    " o.o",
    " >~<",
]


class Uwu(commands.Cog):
    """UwU"""

    @nextcord.slash_command("uwu", "u- uwuify a giwen piece ow text >_<")
    async def uwu(
        self,
        interaction: nextcord.Interaction,
        text: str = nextcord.SlashOption(required=True, description="The text to uwuify"),
        stutter_amount: int = nextcord.SlashOption(
            description="The amount of stuttering.", min_value=1, max_value=100, default=2
        ),
    ) -> None:
        await interaction.response.send_message(
            Uwu.stutter(Uwu.add_random_emoticon(Uwu.replace_r_l_with_w(text.lower())), stutter_amount)
        )

    @staticmethod
    def replace_r_l_with_w(text: str) -> str:
        """Replace R and L with W to give the effect of "uwuifying"."""
        return text.replace("r", "w").replace("l", "w").replace("R", "W").replace("L", "W")

    @staticmethod
    def add_random_emoticon(text: str) -> str:
        """Add a random emoticon to the given text."""
        return text + random.choice(EMOTICONS)

    @staticmethod
    def stutter(text: str, amount=2) -> str:
        """Stutter some text.

        Here's an example if you don't get it:

            hello world
            -> h- hello world
        """

        for _ in range(amount):
            text = f"{text[0]}- {text}"

        return text


def setup(bot: commands.Bot) -> None:
    """Add the :class:`Uwu` cog."""
    bot.add_cog(Uwu())
