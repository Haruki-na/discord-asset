import discord
from discord.ext import commands
from discord.utils import get
from algorithm import statusVoiceBot

intents = discord.Intents.default()
# intents.members = True


bot = commands.Bot(command_prefix='/', description=None, intents=intents)



@bot.event
async def on_ready():
    print(f"successfully runing {bot.user}")



@bot.event
async def on_voice_state_update(member, after, before):
    botID = 554940282831896579  # ตั้งไอดีบอท
    if member.id == botID:
        print("bot working..")
        # print("After", after)
        # print("============================================")
        # print("Before", before)
        if after.channel == None and before.channel is not None:
            statusVoiceBot.statusSet(True)
        else:
            statusVoiceBot.statusSet(False)





@bot.command(aliases=['sta', 's'])
async def status(ctx):
    if statusVoiceBot.statusCheck():
        emBed = discord.Embed(title=f"Status BOT",url="https://media.com", description="status: active\nchannel: None", color=0x42f5a7)
        emBed.set_footer(text='Powered by mantvmass', icon_url='icon.jpg')
        await ctx.channel.send(embed=emBed)
    else:
        emBed = discord.Embed(title=f"Status BOT",url="https://media.com", description="status: unactive\nchannel: None", color=0x42f5a7)
        emBed.set_footer(text='Powered by mantvmass', icon_url='icon.jpg')
        await ctx.channel.send(embed=emBed)




bot.run("")