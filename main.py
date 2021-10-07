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

MainCommands = ["help","youtube","twitch","var change"]
commandvar = (")")
yescom = 0
count1 = 0
cmdout=["**" + commandvar + "help** it helps, **" + commandvar + "youtube** gives my yt, **"+ commandvar +"twitch** gives my twitch","https://www.youtube.com/channel/UC1t5jysqg7S1Pwsb-MAZi7Q","https://www.twitch.tv/grey_eag","You ran change var command"]
#command function it should find what command ur doin then do it
#Find in the API where you can look at the beginning of the message and...
#see if it has the variable that u can change for the beginning of the message
#IF non exist try to find how to make into string and look at that string for it
#Think small first, make simply 2 commands they can be hard codded its ok.
#Just make 1 to change the variable and 1 to set the announcement channel
#Get ur upload working so itll @ people when you upload (Why u need the announcement command)
#Fun features can come later first get the basics!
async def commsearch(pmsg,msg):
  if any(word in msg for word in MainCommands):
    if ((msg) == ")help"):
      await pmsg.channel.send(msg,"Type help for help")

#Once it has started this is run once
@client.event
async def on_ready():
  print ("Bot has started and We have logged in as {0.user}".format(client))
  print ("\n-------------------------------------------------------------\n")
  general = client.fetchchannel(general)
  #announcements = client.fectchchannel(announcements)
  await general.send("Hello World! :)")

#YT CODE FROM https://stackoverflow.com/questions/43118114/notified-when-youtube-video-is-uploaded-api

  youtube=build('youtube','v3',developerKey=os.getenv("googlekey"))
  req=youtube.playlistItems().list(playlistId="844936644523065354",part='snippet',maxResults=1)
  res=req.execute()
  vedioid=res['items'][0]['snippet']['resourceId']['videoId']
  link="https://www.youtube.com/channel/UC1t5jysqg7S1Pwsb-MAZi7Q"
  ch=await client.fetch_channel(844938598449283073)
  await ch.send(link)
  yt.start()#Starting tasks loop which is made below for checking every minu


@tasks.loop(seconds=60)
async def yt():
  youtube=build('youtube','v3',developerKey='Enter your key here')
  req=youtube.playlistItems().list(
      playlistId='844936644523065354',
      part='snippet',
      maxResults=1
  )
  res=req.execute()
  vedioid=res['items'][0]['snippet']['resourceId']['videoId']
  link="https://www.youtube.com/watch?v="+vedioid
  ch=await client.fetch_channel(844938598449283073)

  async for message in ch.history(limit=1):#looping through the channel to get  the latest message i can do this using last message also but I prefer using channel.history        
    if str(link) != str(message.content):
      ch2=await client.fetch_channel(844936644523065354)
        
      await ch2.send(f'@everyone,**User** just posted a vedio!Go and check it out!\n{link}')
      
      await ch.send(link2)#this is important as after posting the video the link must also be posted to the check channel so that the bot do not send other link
    else:
      pass

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

#GAVEN GREY EAGLESON!
#MAKE
#A
#COMMAND
#LIBRARY
#OR DIE
client.run(os.getenv("token"))