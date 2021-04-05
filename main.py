print ("Running code")
#I bet the solutions to my problems probably take less code than mine :)

print ("Importing packages...")

import discord
import os
import random
import youtube3
from googleapiclient.discovery import build
from replit import db



print ("Starting Up...")
#Make categories for U

client = discord.Client()

MainCommands = ["help","youtube","twitch"]
cumwords = ["cum","coom","baby batter","semen","life liquid","splooge"]

async def commsearch(pmsg,msg):
  if any(word in msg for word in MainCommands):
    if ((msg) == ")help"):
      await pmsg.channel.send(msg,"Type help for help")

@client.event
async def on_ready():
  print ("Bot has started and We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  pmsg = message
  msg = message.content.lower()
  if message.author == client.user:
    return
  command = msg.split(")",1)[1]
  if any(word in msg for word in cumwords):
    await message.channel.send(msg)
    await message.channel.send("Kris eats cum.")
 # if message.content.startswith(")"):
  #  await commsearch(pmsg,msg)
    print ("It was a command")

client.run(os.getenv("token"))
client.run(os.getenv("googlekey"))