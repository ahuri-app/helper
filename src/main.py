# ahuri helper
if __name__ == "__main__":
    print("Loading...")
import os
import nextcord
import config
import textwrap
import time
import functools
import datetime
from traceback import format_exception
from nextcord.ext import commands
from dotenv import load_dotenv
from errors import errors
from utils import *
from config import *
errors = errors()
p = prefix

load_dotenv()

bot = commands.Bot(
    intents=nextcord.Intents.all(),
    activity=nextcord.Game(
        name="Amogus Gaem"
    )
)
token = os.getenv("BOT_TOKEN", "env variable not set")

@bot.event
async def on_ready():
    print(f"Connected to Discord!\nLogged in as {bot.user}.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.guild == None:
        return
    
    if message.author.id in config.full_access:
        if message.content.startswith(p+"reload "):
            cog = message.content.split(p+"reload ", 1)[1]
            info = cogreload(cog, bot)
            await message.reply(info[0]+": "+repr(info[1]))
        elif message.content.startswith(p+"load "):
            cog = message.content.split(p+"load ", 1)[1]
            info = cogload(cog, bot)
            await message.reply(info[0]+": "+repr(info[1]))
        elif message.content.startswith(p+"unload "):
            cog = message.content.split(p+"unload ", 1)[1]
            info = cogunload(cog, bot)
            await message.reply(info[0]+": "+repr(info[1]))
        elif message.content == p+"reloadallcogs":
            info = reloadallcogs(bot)
            t = ""
            for x in info:
                t = t + f"{x}: {info[x][0]}\n"
                if info[x][0] == "ERROR":
                    t = t + f" - Reason: {repr(info[x][1])}\n"
            await message.reply(t)
        elif message.content == p+"loadallcogs":
            info = loadallcogs(bot)
            t = ""
            for x in info:
                t = t + f"{x}: {info[x][0]}\n"
                if info[x][0] == "ERROR":
                    t = t + f" - Reason: {repr(info[x][1])}\n"
            await message.reply(t)
        elif message.content == p+"unloadallcogs":
            info = unloadallcogs(bot)
            t = ""
            for x in info:
                t = t + f"{x}: {info[x][0]}\n"
                if info[x][0] == "ERROR":
                    t = t + f" - Reason: {repr(info[x][1])}\n"
            await message.reply(t)
        elif message.content == p+"createrules":
            embeds = [
                #nextcord.Embed(color=theme_color).set_image(rules_img),
                nextcord.Embed(title="<:i_rules:1021393242308235275> Rules", description="""
**1)** No NSFW
**2)** Be kind to all members
**3)** Do not cause drama (If you have a problem with someone, create a ticket <#1017795438600015985>)
**4)** No advertising
**5)** Don't discuss religion or politics
**6)** Listen to moderators
**7)** Do not impersonate people (and even if you do we can find the real you and take action 😎)
**8)** Swearing is allowed, but don't swear excessively
**9)** Don't be toxic
**10)** just be a gentleman/woman bro ;-;
**And lastly,** Comply with Discord's **[Community Guidelines](https://discord.com/guidelines)** and **[Terms of Service (TOS)](https://discord.com/terms)**.

||Please also read <#1017795675972444182> if you haven't already||
""", color=theme_color)
            ]
            await message.channel.send(embeds=embeds)
        elif message.content == p+"createinfo":
            embeds = [
                nextcord.Embed(color=theme_color).set_image(info_img),
                nextcord.Embed(title=f"{e_ahuri} What is Ahuri?", description="""
**Ahuri** is a secure & simple chat app made by <@477683725673693184>. It has **End-to-End Encryption** so no one can see your chats except you or the recipient(s).
""", color=theme_color).set_thumbnail(ahuri2),
                nextcord.Embed(title="<:i_info:1021393239649042503> Info", description="""
First of all, **read the rules** <#1017793915941818399>.
Not only just read, **but also follow them**. ||or get punished 😎||

**For website related support, reporting a user in this discord server, talking to a staff member, giving suggestions, making bug reports or if you have any questions or queries please see <#1017795438600015985>.**

Refer to <#1017795601397723336> for useful links.
Get pingable roles like <@&1017806135845212220> and <@&1017806228971339797> from <#1017795902313877535>.

Announcements are posted to <#1017795568602447963> and updates on Ahuri is posted to <#1017795827240026193>.

If you are not able to access any channels please verify yourself in <#1017802489497649245> and then you can gain access to this server.
""", color=theme_color)
            ]
            await message.channel.send(embeds=embeds)
        elif message.content == p+"createlinks":
            embeds = [
                nextcord.Embed(color=theme_color).set_image(links_img),
                nextcord.Embed(title="<:i_links:1021393237170192504> Links", description="""
**Site:**
http://18.169.99.65/
**Discord Server Invite:**
https://discord.gg/VgFuy4aw3q
""", color=theme_color)
            ]
            await message.channel.send(embeds=embeds)
            await message.channel.send("http://18.169.99.65/")
        elif message.content == p+"createsupport":
            embeds = [
                nextcord.Embed(color=theme_color).set_image(support_img),
                nextcord.Embed(title="<:i_supportteam:1021385236027805696> Support", description="""
<:i_timeout:1021386093297414165> **If you make a ticket for no reason you will be timed out for a week.**
""", color=theme_color),
                nextcord.Embed(title=f"{e_ahuri_b} Website Related Support", description="""
**For Website Related Support, make a post in the forum <#1020786736189685882>.**
**Website Related Support** means that if you are facing any problems in the website and cannot resolve it by your own.
""", color=theme_color),
                nextcord.Embed(title="<:i_person:1021383776951074887> Reporting a User", description="""
**For Reporting a User, make a ticket from <#1017795496737243207> from the message in the image.**
**Report a User** means that if a user is troubling you or has inappropriate username or profile picture or is troubling you by DMing you or breaking any of the rules.
""", color=theme_color).set_image(report_a_user_img),
                nextcord.Embed(title="<:i_headphone:1021383870467280996> General Support", description="""
**For General Support, make a ticket from <#1017795496737243207> from the message in the image.**
**General Support** means that you want to talk to a staff member for matters like getting falsely banned or want to make a ban appeal or getting falsely punished in this server, etc.
""", color=theme_color).set_image(general_support_img),
                nextcord.Embed(title="<:i_people:1021383900871786587> Giving Suggestions", description="""
**For giving suggestions on improving this Discord Server or Ahuri, please give your suggestion by creating a post in forum <#1020787042336112690>.**
""", color=theme_color),
                nextcord.Embed(title="<:i_bug:1021383821167443999> Reporting Bugs", description="""
**For reporting a bug in Ahuri, please tell us in detail about the bug and how it can be fixed if possible with screenshots or video recording by creating a post in forum <#1020787084283367444>.**
""", color=theme_color),
                nextcord.Embed(title="<:i_question:1021385305149947974> Questions or queries", description="""
**If you have any questions or queries, please ask it in <#1018098169424379964>.**
""", color=theme_color)
            ]
            a = await message.channel.send(embeds=embeds)
            await a.reply("Click the reply to go to the top.")
        elif message.content == p+"createteam":
            embeds = [
                nextcord.Embed(title="<:i_people:1021383900871786587> Team", description=f"""
{e_ahuri} **Founder**
<@477683725673693184>

> **Developers** (<@&1018809111124639765>)
**Full Stack Developers** (<@&1017793074442801172>)
<@477683725673693184>
<@842457844724400142>

**Backend Developers** (<@&1021032160938954824>)
<@1005756074973990922>

> **Graphic Designers** (<@&1017792998064533585>)
<@734033646423375903>
<@594791174892683274>

> **Discord Server**
**Administrators** (<@&1017792865595822171>)
<@842457844724400142>

**Staff** (<@&1017792935917539429>)
<@734033646423375903>
""", color=theme_color).set_thumbnail(ahuri_bg_round)
            ]
            await message.channel.send(embeds=embeds)
        elif message.content.startswith(p+"eval "):
            evalstr = message.content.split(p+"eval ", 1)[1]
            main_message = await message.channel.send("Working on it...")
            t = time.monotonic()
            try:
                returned = await bot.loop.run_in_executor(None, functools.partial(eval, evalstr, globals(), locals()))
                returned_as_str = str(returned)
                if token.lower() in returned_as_str.lower():
                    raise errors.BotTokenInEval
            except Exception as e:
                #returned = repr(e)
                returned = "".join(format_exception(e, e, e.__traceback__))
                returned_as_str = str(returned)
            tt = time.monotonic() - t
            mstaken = round(tt*1000, 2)
            staken = round(tt, 2)
            try:
                    await main_message.edit("Done!", embed=nextcord.Embed(title=f"Eval by {message.author}", color=nextcord.Colour.green()).add_field(name="📥 Input:", value=f"```py\n{evalstr}\n```").add_field(name="📤 Output:", value=f"```py\n{returned if ''.join(''.join(returned_as_str.strip().splitlines()).split()) != '' else 'No output.'}\n```**Return type:** {type(returned)}\n**Time Taken:** {mstaken}ms ({staken}s)").set_footer(text=f"Python {sys.version}"))
            except nextcord.errors.HTTPException:
                try:
                    await main_message.edit("Done!", embeds=[nextcord.Embed(title=f"Eval by {message.author}", color=nextcord.Colour.green()).add_field(name="📥 Input:", value=f"```py\n{evalstr}\n```").add_field(name="📤 Output:", value=f"```\nCannot fit the output in this field. Check the embed below.\n```**Return type:** {type(returned)}\n**Time Taken:** {mstaken}ms ({staken}s)").set_footer(text=f"Python {sys.version}"), nextcord.Embed(title="📤 Output:", description=f"```py\n{returned if ''.join(''.join(returned_as_str.strip().splitlines()).split()) != '' else 'No output.'}\n```", color = nextcord.Colour.green())])
                except nextcord.errors.HTTPException:
                    filename = str(datetime.datetime.now())+".txt"
                    filename = filename.replace(":", "-")
                    with open("./outputs/"+filename, "w", encoding="utf-8") as outputfile:
                        outputfile.write(returned_as_str)
                    await main_message.edit("Done!", embed=nextcord.Embed(title=f"Eval by {message.author}", color=nextcord.Colour.green()).add_field(name="📥 Input:", value=f"```py\n{evalstr}\n```").add_field(name="📤 Output:", value=f"```\nCannot fit the output in this field or in a new embed. Output is saved in './outputs/{filename}`\n```**Return type:** {type(returned)}\n**Time Taken:** {mstaken}ms ({staken}s)").set_footer(text=f"Python {sys.version}"))
        elif message.content.startswith(p+"exec "):
            execstr = message.content.split(p+"exec ", 1)[1]
            main_message = await message.channel.send("Working on it...")
            t = time.monotonic()
            local_variables = {
                "os": os,
                "nextcord": nextcord,
                "config": config,
                "commands": commands,
                "bot": bot,
                "message": message,
                "main_message": main_message,
                "local": locals(),
                "global": globals()
            }
            try:
                old_stdout = sys.stdout
                redirected_output = sys.stdout = StringIO()
                await bot.loop.run_in_executor(None, functools.partial(exec, f"async def execfunc():\n{textwrap.indent(execstr, '    ')}", local_variables))
                obj = await local_variables["execfunc"]()
                sys.stdout = old_stdout
                returned = f"{redirected_output.getvalue()}\n-- {obj}\n"
                returned_as_str = str(returned)
                if token.lower() in returned_as_str.lower():
                    raise errors.BotTokenInEval
            except Exception as e:
                obj = e
                returned = "".join(format_exception(e, e, e.__traceback__))
                returned_as_str = str(returned)
            tt = time.monotonic() - t
            mstaken = round(tt*1000, 2)
            staken = round(tt, 2)
            try:
                    await main_message.edit("Done!", embed=nextcord.Embed(title=f"Exec by {message.author}", color=nextcord.Colour.green()).add_field(name="📥 Input:", value=f"```py\n{execstr}\n```").add_field(name="📤 Output:", value=f"```py\n{returned if ''.join(''.join(returned_as_str.strip().splitlines()).split()) != '' else 'No output.'}\n```**Return type:** {type(obj)}\n**Time Taken:** {mstaken}ms ({staken}s)").set_footer(text=f"Python {sys.version}"))
            except nextcord.errors.HTTPException:
                try:
                    await main_message.edit("Done!", embeds=[nextcord.Embed(title=f"Exec by {message.author}", color=nextcord.Colour.green()).add_field(name="📥 Input:", value=f"```py\n{execstr}\n```").add_field(name="📤 Output:", value=f"```\nCannot fit the output in this field. Check the embed below.\n```**Return type:** {type(obj)}\n**Time Taken:** {mstaken}ms ({staken}s)").set_footer(text=f"Python {sys.version}"), nextcord.Embed(title="📤 Output:", description=f"```py\n{returned if ''.join(''.join(returned_as_str.strip().splitlines()).split()) != '' else 'No output.'}\n```", color = nextcord.Colour.green())])
                except nextcord.errors.HTTPException:
                    filename = str(datetime.datetime.now())+".txt"
                    filename = filename.replace(":", "-")
                    with open("./outputs/"+filename, "w", encoding="utf-8") as outputfile:
                        outputfile.write(returned_as_str)
                    await main_message.edit("Done!", embed=nextcord.Embed(title=f"Exec by {message.author}", color=nextcord.Colour.green()).add_field(name="📥 Input:", value=f"```py\n{execstr}\n```").add_field(name="📤 Output:", value=f"```\nCannot fit the output in this field or in a new embed. Output is saved in './outputs/{filename}`\n```**Return type:** {type(obj)}\n**Time Taken:** {mstaken}ms ({staken}s)").set_footer(text=f"Python {sys.version}"))

if __name__ == "__main__":
    print("\nLoading all cogs...")
    cogsinfo = loadallcogs(bot)
    for x in cogsinfo:
        print(f"{x}: {cogsinfo[x][0]}")
        if cogsinfo[x][0] == "ERROR":
            print(f" - Reason: {repr(cogsinfo[x][1])}")
    print("Loaded.\n")
    
    print("Logging in...")
    try:
        bot.run(token)
    except nextcord.errors.LoginFailure:
        print("Improper token passed.")
        print(f"Token: '{token}'")