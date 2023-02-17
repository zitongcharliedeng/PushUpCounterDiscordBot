import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
from pocketbase import PocketBase
#(FOR DEPLOYMENT) from keep_alive import keep_alive

#(FOR DEPLOYMENT) keep_alive()
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN') #(FOR DEPLOYMENT) TOKEN = os.environ['DISCORD_TOKEN']
GUILD = os.getenv('DISCORD_GUILD') #(FOR DEPLOYMENT) GUILD = os.environ['DISCORD_TOKEN']
#(FOR DEPLOYMENT) IMAGE_SECRET = os.environ['IMAGE_SECRET']
#(FOR DEPLOYMENT) THUMBNAIL_SECRET = os.environ['THUMBNAIL_SECRET']

all_intents = discord.Intents.all()
client = discord.Client(intents=all_intents)
bot = commands.Bot(intents=all_intents, command_prefix='pushups!')
pb = PocketBase('http://127.0.0.1:8090') #(FOR DEPLOYMENT) pb = PocketBase('https://YOURAPPNAME.fly.dev/')


@bot.event
async def on_ready():
  for guild in bot.guilds:
    if guild.name == GUILD:
      break
    print(f'{client.user} is connected to the following guild:\n'
          f'{guild.name}(id: {guild.id})\n')
  members = '\n - '.join([member.name for member in guild.members])
  print(f'Guild Members:\n - {members}')


@bot.command(name='add', help="Add your pushups to the server's total!")
async def addResponse(ctx, pushups):

  addQuotes = [
    'Nice work out! ',
    ("Amazeballs! "),
  ]

  data = {
    "userId": f"{ctx.author}",
    "pushups": f"{int(pushups)}",
  }

  createContributionResponse = None

  def createContribution():
    nonlocal createContributionResponse
    createContributionResponse = (
      pb.collection('contributions').create(data)).__dict__

  createContribution()

  netContributionId = ""
  pastPushups = 0

  async def readNetContribution():
    list = (pb.collection('netContribution').get_list(
      1, 1, {"filter": f'userId="{(createContributionResponse)["user_id"]}"'
             })).__dict__
    if (len(list["items"]) == 0):
      response = "no NetContribution record exists yet"
    else:
      response = list["items"][0].__dict__
      nonlocal netContributionId
      netContributionId = response["id"]
      nonlocal pastPushups
      pastPushups = response["pushups"]
    return response

  await readNetContribution()

  message = ""

  async def createOrUpdateNetContribution():
    if (await readNetContribution() == "no NetContribution record exists yet"):
      nonlocal message
      message = "Congrats on your first pushups! "
      data = {
        "userId": f"{ctx.author}",
        "pushups": f"{int(pushups)}",
      }
      return pb.collection('netContribution').create(
        data)  #!!!!!!!!!!!!!!!!!!!!!!!!!
    else:
      data = {
        "pushups": f"{pastPushups + int(pushups)}",
      }
      return pb.collection('netContribution').update(netContributionId, data)

  await createOrUpdateNetContribution()

  print(f"{client.guilds}")
  message = f"{message} You added {pushups} pushups, {ctx.author}. {random.choice(addQuotes)}"
  await ctx.send(message)


@bot.command(name='remove',
             help="Remove your pushups from the server's total!")
async def removeResponse(ctx, pushups):
  removeQuotes = [
    'We all make mistakes! ',
    ("Thank you for being honest. "),
  ]

  data = {
    "userId": f"{ctx.author}",
    "pushups": -int(pushups),
  }

  createContributionResponse = None

  def createContribution():
    nonlocal createContributionResponse
    createContributionResponse = (
      pb.collection('contributions').create(data)).__dict__

  createContribution()

  netContributionId = ""
  pastPushups = 0

  async def readNetContribution():
    list = (pb.collection('netContribution').get_list(
      1, 1, {"filter": f'userId="{(createContributionResponse)["user_id"]}"'
             })).__dict__
    if (len(list["items"]) == 0):
      response = "no NetContribution record exists yet"
    else:
      response = list["items"][0].__dict__
      nonlocal netContributionId
      netContributionId = response["id"]
      nonlocal pastPushups
      pastPushups = response["pushups"]
    return response

  await readNetContribution()

  message = ""

  async def createOrUpdateNetContribution():
    if (await readNetContribution() == "no NetContribution record exists yet"):
      nonlocal message
      message = "Congrats on your first... anti-pushups? "
      return pb.collection('netContribution').create(data)
    else:
      data = {
        "pushups": f"{pastPushups - int(pushups)}",
      }
      return pb.collection('netContribution').update(netContributionId, data)

  await createOrUpdateNetContribution()

  message = f"{message} You removed {pushups}, {ctx.author}. {random.choice(removeQuotes)}"
  await ctx.send(message)


@bot.command(name='leaderboard', help="See who is carrying?")
async def leaderboard(ctx):
  totalPushups = 0

  def readAllNetContributions():
    list = (pb.collection('netContribution').get_list(
      1, 10, {"sort": '-pushups'})).__dict__["items"]

    for record in list:
      nonlocal totalPushups
      totalPushups = totalPushups + int(record.__dict__['pushups'])

    if (len(list) == 0):
      response = False
    else:
      response = list
    return response

  def leaderboard():
    list = readAllNetContributions()
    if list == False:
      return "Empty records :("
    else:
      bulletpoints = []
      for record in list:
        bulletpoints.append(
          f"- {record.__dict__['user_id']}  |  {record.__dict__['pushups']} pushups"
        )
      formatted_bulletpoints = "\n".join(bulletpoints)
    return formatted_bulletpoints

  embed = discord.Embed(
    description=
    f'{leaderboard()}',  # run description first to update totalPushups
    title=f'Top 10 Pushers (Their Total: {totalPushups}): ',
    color=discord.Colour.blue())
  embed.set_image(url=f"{IMAGE_SECRET}")
  embed.set_thumbnail(url=f"{THUMBNAIL_SECRET}")

  await ctx.send(embed=embed)


bot.run(TOKEN)



