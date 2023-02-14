import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
from pocketbase import PocketBase
import json

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

all_intents = discord.Intents.all()
client = discord.Client(intents=all_intents)
bot = commands.Bot(intents=all_intents, command_prefix='pushups!')
pb = PocketBase('http://127.0.0.1:8090')

@bot.event
async def on_ready():
  for guild in bot.guilds:
    if guild.name == GUILD:
      break
    print(
      f'{client.user} is connected to the following guild:\n'
      f'{guild.name}(id: {guild.id})\n'
    )
  members = '\n - '.join([member.name for member in guild.members])
  print(f'Guild Members:\n - {members}')



@bot.command(name='add', help="Add your pushups to the server's total!")
async def addResponse(ctx, pushups):

  addQuotes = [
    'Nice work out! ',
    (
      "Amazeballs! "
    ),
  ]

  data = {
    "userId": f"{ctx.author}",
    "pushups": f"{int(pushups)}",
  }


  createContributionResponse = None
  def createContribution():
    nonlocal createContributionResponse
    createContributionResponse = (pb.collection('contributions').create(data)).__dict__
  createContribution()

  netContributionId = ""
  pastPushups = 0

  async def readNetContribution():
    list = (pb.collection('netContribution').get_list(1,1,{"filter": f'userId="{(createContributionResponse)["user_id"]}"'})).__dict__
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
      return pb.collection('netContribution').create(data) #!!!!!!!!!!!!!!!!!!!!!!!!!
    else:
      data = {
        "pushups": f"{pastPushups + int(pushups)}",
      }
      return pb.collection('netContribution').update(netContributionId, data)
  await createOrUpdateNetContribution()


  print(f"{client.guilds}")
  message = message + f"You added {pushups} pushups, {ctx.author}. " + random.choice(addQuotes)
  await ctx.send(message)
  


@bot.command(name='remove', help="Remove your pushups from the server's total!")
async def removeResponse(ctx, pushups):
  removeQuotes = [
    'We all make mistakes! ',
    (
      "Thank you for being honest. "
    ),
  ]

  data = {
    "userId": f"{ctx.author}",
    "pushups": -int(pushups),
  }

  createContributionResponse = None
  def createContribution():
    nonlocal createContributionResponse
    createContributionResponse = (pb.collection('contributions').create(data)).__dict__
  createContribution()

  netContributionId = ""
  pastPushups = 0

  async def readNetContribution():
    list = (pb.collection('netContribution').get_list(1,1,{"filter": f'userId="{(createContributionResponse)["user_id"]}"'})).__dict__
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

  response = f"You removed {pushups}, {ctx.author}. " + random.choice(removeQuotes)
  await ctx.send(response)



@bot.command(name='leaderboard', help="Who is carrying?")
async def leaderboard(ctx):

  #fetch a paginated records list
  async def resultList():
    return pb.collection('contributions').get_list(1, 50, {
    "filter": 'created >= "2022-01-01 00:00:00"',
  })
  await resultList()
  print((await resultList()).items[0])

   #you can also fetch all records at once via getFullList
  # async def records():
  #   return pb.collection('contributions').get_full_list(200 , {
  #   "sort": '-created',
  # })
  # await records()
  # print((await records()))

  #or fetch only the first record that matches the specified filter
  # async def record():
  #   return pb.collection('contributions')._get_first_list_item('someField="test"', {
  #   "expand": 'relField1,relField2.subRelField',
  # })
  # await record()
  # print(f'{record}')






bot.run(TOKEN)


