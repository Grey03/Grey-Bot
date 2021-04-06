print ("Starting up...")
#I bet the solutions to my problems probably take less code than mine :)

print ("Importing packages...")
import discord
import os
import random
import youtube3
from googleapiclient.discovery import build
from replit import db
print ("Packages Imported...")

print ("Starting Up...")
#Make categories for U

client = discord.Client()

MainCommands = ["help","youtube","twitch"]
cmdout=["**)help** it helps, **)youtube** gives my yt, **)twitch** gives my twitch","https://www.youtube.com/channel/UC1t5jysqg7S1Pwsb-MAZi7Q","https://www.twitch.tv/grey_eag"]
commandvar = (")")
yescom = 0
count1 = 0
#command function it should find what command ur doin then do it
async def commsearch(pmsg,msg):
  if any(word in msg for word in MainCommands):
    if ((msg) == ")help"):
      await pmsg.channel.send(msg,"Type help for help")

#Once it has started this is run once
@client.event
async def on_ready():
  print ("Bot has started and We have logged in as {0.user}".format(client))
  print ("\n-------------------------------------------------------------\n")
  channel = client.get_channel(828470652368977962)
  await channel.send("I've started")

#On every message this is run
@client.event
async def on_message(msg):
  cmsg = msg.content
  lmsg = msg.content.lower()
  msga = msg.author
  grey = 246792121313394689
  chancestfu = random.randint(0,100)
  #this checks if the author is the bot or not if its not the bot continue
  if msg.author == client.user:
    return
  if msg.author.id == 246792121313394689:
    if chancestfu == 3:
      await msg.channel.send("Stfu Grey")
    if chancestfu == 69:
      await msg.channel.send("I wish I was never created")
    if chancestfu == 50:
      await msg.channel.send("I wish my creator was a competent programmer")
  #tryin somethin with thei command split
  #command = msg.split(") ",1)[1]
  #this is a meme it sees if coom was mentioned and makes fun of kris, very important
  #COMMANDS?????/
  count1 = 0
  yescom = 0
  while count1 != len(MainCommands):
    count1 = count1 + 1
    tmp = count1 - 1
    if lmsg.startswith(commandvar+MainCommands[tmp]):
      yescom = 1
      count1 = len(MainCommands)
      await msg.channel.send(cmdout[tmp])
  if any(word in lmsg for word in commandvar):
    if (yescom != 1):
      await msg.channel.send("That's not a command do " + str(commandvar) + "help for help")

  #im tryin to add the command key detector here but ur a dingus
 # if message.content.startswith(")"):
  #  await commsearch(pmsg,msg)
    #print ("It was a command")
  #else:
    #this is kinda a log for me to see in the console
    #print (str(msga) + "\n" + cmsg + " : not a command\n")
#these get the keys for the APIs
client.run(os.getenv("token"))
client.run(os.getenv("googlekey"))