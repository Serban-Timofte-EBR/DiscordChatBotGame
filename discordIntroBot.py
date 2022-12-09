import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive



client = discord.Client()



starter_introString = "Let me introduce my rules:"

starter_introString2 = "Let me know if you know the rules of the game! Just say something like I want to know the rules."

starter_introString3 = "If you are scared or afraid about the start of the game, just tell me that you are! I can give you some courage!"

starter_introString4 = "I know a lot of quotes! Type $quote if you want to give you one!"

starter_introString5 = "Using $new you can add a new answer for somebody else who is scared! If you type $del you can delete an answer using the index in the answer list!"

starter_introString6 = "Tell me if you are afraid to start the game! I can give you some courage!"



get_introWords = [
"Hi", "hi", "Hey", "hey", "Hello", "hello",
"Good morning", "good morning", "Good Morning", "good morning",
"Good evening", "good evening", "good Evening", "Good Evening",
"Cheers", "cheers"
]



get_knowhow = [
'I don not know', 'idk', 'IDK', 'Idk', 'IDk',
'I don t know', 'I would like to know', 'I want know', 'I want to know'
]



starter_knowhow = [
"I am sure that the team prepared clear instructions! Just search it in the project!",
"The team putted everything to point! Just search in the menu!",
]



starter_intro =[
"Hola!", "Hey!", "Hi", "I am here!", "May I help you?"
]



get_gameRules = ["rules", "help", "game law", "control"]



starter_gameRules = [
"My team prepared a dedicated menu with all the rules!",
"All the rules all available in our team project ( we created a special menu for this )!",
"Rules are easy! Element vs Element, Same element => compare the power! Do you know that we have 2 modes of this game? Check all the rules of both modes in others tabs!"
]



get_courage = ["courage", "afraid", "emotions", "sad"]



starter_getCourage =[
"Do not be afraid! It is a game! The bots did not take the control yet!",
"It is just a game! Try it! If you lose, try again and train your brain!",
"Poker is not just about how lucky you are! Our poker game keeps the same idea!, Go and try it!",
"Just do it!"
]



api_key = "775adde453a78d614cc44c9ec3b0df15"



def getUpdate_courage(encMessage):
 if "encouragements" in db.keys():
  encouragements = db["encouragements"]
  encouragements.append(encMessage)
  db["encouragements"] = encouragements
 else:
  db["encouragments"] = [encMessage]



def getDowngrade_courage(toBeDelMess):
 encouragements = db["encouragements"]
 if len(encouragements) > toBeDelMess:
  del encouragements[toBeDelMess]
  db["encouragements"] = encouragements



def reply_quote():
 inpt = requests.get("https://zenquotes.io/api/random")
 json_data = json.loads(inpt.text)
 quote = json_data[0]['q'] + " -" + json_data[0]['a']
 return (quote) 



@client.event
async def on_ready():
 print('Logged in as {0.user}'.format(client))
 print('Let me introduce my rules: ')
 print('Let me know if you know the rules of the game!')
 print("If you are scared or afraid about the start of the game, just tell me that you are! I can give you some courage ;)!")
 print("I know a lot of quotes! Type $quote if you want to give you one!")
 print("Using $new you can add a new answer for somebody else who is scared! If you type $del you can delete an answer using the index in the answer list!")



@client.event
async def on_message(message):
 if message.author == client.user:
  return

 if message.content.startswith('$hello'):
  await message.channel.send('Hello!')
 if message.content.startswith('$quote'):
  quote = reply_quote()
  await message.channel.send(quote)



 option = starter_getCourage
 if "encouragements" in db.keys():
  option = option + db["encouragements"]
 if any(word in message.content for word in get_gameRules):
  await message.channel.send(random.choice(starter_gameRules))

 if any(word in message.content for word in get_courage):
  await message.channel.send(random.choice(option))
 if any(word in message.content for word in get_introWords):
  await message.channel.send(random.choice(starter_intro))
  await message.channel.send(starter_introString)
  await message.channel.send(starter_introString2)
  await message.channel.send(starter_introString3)
  await message.channel.send(starter_introString4)
  await message.channel.send(starter_introString5)
     await message.channel.send(starter_introString6)


 if any(word in message.content for word in get_knowhow):
  await message.channel.send(random.choice(starter_knowhow))



 if message.content.startswith("$new"):
  enc_message = message.content.split("$new ",1)[1]
  getUpdate_courage(enc_message)
  await message.channel.send("New answer added!")



 if message.content.startswith("$del"):
  encouragements = []
 if "encouragements" in db.keys():
  index = int(message.content.split("$del",1)[1])
  getDowngrade_courage(index)
  encouragements = db["encouragements"]
  await message.channel.send(encouragements)



keep_alive()
my_secret = os.environ['Token']
client.run(my_secret)
