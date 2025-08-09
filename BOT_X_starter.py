
import discord
from discord.ext import commands, tasks
import random
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# --- EVENTS ---

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    for guild in bot.guilds:
        me = guild.me
        try:
            await me.edit(nick="BOT X")
        except Exception as e:
            print(f"Couldn't change nickname in {guild.name}: {e}")
    check_youtube.start()

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="welcome")
    if channel:
        await channel.send(f"👋 Welcome {member.mention} to the world of Cobblemon! Enjoy your stay!")

# --- COMMANDS ---

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! 🏓 `{round(bot.latency * 1000)}ms`")

@bot.command()
async def shinyluck(ctx):
    luck = random.randint(1, 100)
    await ctx.send(f"✨ Your shiny luck today is: **{luck}%**!")

@bot.command()
async def trivia(ctx):
    questions = [
        "Which Pokémon evolves into Charizard?",
        "What type is super effective against Water?",
        "Which Pokémon is known as the Electric Mouse?",
        "What is the name of the Pokémon professor in Kanto?"
    ]
    await ctx.send(f"🧠 Trivia Time! {random.choice(questions)}")

# --- YOUTUBE PLACEHOLDER TASK ---

@tasks.loop(minutes=5)
async def check_youtube():
    # Placeholder: You can integrate YouTube RSS feed or YouTube API here
    # to check for new uploads and post them in a designated channel.
    pass

# --- RUN BOT ---

bot.run("YOUR_DISCORD_BOT_TOKEN")
