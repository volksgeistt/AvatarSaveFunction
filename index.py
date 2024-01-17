import discord
from discord.ext import commands
import colorama
from colorama import Fore

client = commands.Bot(command_prefix='@', intents=discord.Intents.all())
@client.event
async def on_ready():
    print(f"{Fore.MAGENTA}[ READY ] -> Connected To {client.user}")

def AvatarSaveFunction(member):
    v = member.avatar.url if member.avatar else member.default_avatar_url
    try:
        with open("saved.txt", "a") as f:
            f.write(f"{v}\n")
            print(f"{Fore.GREEN}[ LOG ] -> Saved PFP: @{member}")
    except Exception as e:
        print(f"{Fore.RED}[ LOG ] -> Unable To Save PFP -> {e}")

@client.event
async def on_member_join(member):
    AvatarSaveFunction(member)

client.run("ADD_CLIENT_TOKEN")
