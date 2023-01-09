# Import section
import random                               # random function will help the bot to play a card
from game_objects import Player
from chat_bot.bot import ChatBot            # both imports there are from github to get togheter our work

'''Function that removes/deletes cards played from deck and inserts new ones'''
def after_battle(user, bot, userOption, botOption):
 user.deck.remove(userOption)
 bot.deck.remove(botOption)
 user.add_card()
 bot.add_card()

'''Define a function which compares played cards ( user and bot inputs ) and if they played the same element,
the function will compare the value associated with the card. The line comments will indicated the places
were we analize the player input! At every end of a round, the winner will receive a point.'''
def competition(user, bot, userOption, botOption):    #target: redesign this function
 if userOption.element == "fire":                                   #User played fire
  if botOption.element == "fire":
   if userOption.value > botOption.value:
    print("User card won!")
    after_battle(user, bot, userOption, botOption)
    user.points += 1
   elif userOption.value < botOption.value:
    print("The chatbot won the duel!")
    after_battle(user, bot, userOption, botOption)
    bot.points += 1
   else:
    print("It is a draw! Try again!")
  elif botOption.element == "water":
   print("Water beats fire! The chatbot won the duel!")
   after_battle(user, bot, userOption, botOption)
   bot.points += 1
  elif botOption.element == "earth":
   print("Fire beats Earth! Congratulations, you won this round!")
   after_battle(user, bot, userOption, botOption)
   user.points += 1

 elif userOption.element == "water":                              # User played water
  if botOption.element == "fire":
   print("Water beats fire! Great job, you won the duel!")
   after_battle(user, bot, userOption, botOption)
   user.points += 1
  elif botOption.element == "water":
   if userOption.value > botOption.value:
    print("User won!")
    after_battle(user, bot, userOption, botOption)
    user.points += 1
   elif userOption.value < botOption.value:
    print("The chatbot won the duel!")
    after_battle(user, bot, userOption, botOption)
    bot.points += 1
   else:
    print("It is a draw!")
  elif botOption.element == "earth": # Clear case
   print("Earth beats water! You lost this duel!")
   after_battle(user, bot, userOption, botOption)
   bot.points += 1

 elif userOption.element == "earth":                    # User played earth
  if botOption.element == "fire":
   print("Fire beats Earth! The chatbot won this duel!")
   after_battle(user, bot, userOption, botOption)
   bot.points += 1
  elif botOption.element == "water":
   print("Earth beats Water! You won this duel!")
   after_battle(user, bot, userOption, botOption)
   user.points += 1
  elif botOption.element == "earth":
   if userOption.value > botOption.value:
    print("You won it!")
    after_battle(user, bot, userOption, botOption)
    user.points += 1
   if userOption.value < botOption.value:
    print("Next time! You lost it this time!")
    after_battle(user, bot, userOption, botOption)
    bot.points += 1
   else:
    print("It is a draw!")

''' Define a function which starts the game! The function will run until the player or the bot will get the maximum number
 of points ( passed as argument at the end of the file )'''
def game(max_points):
 player = Player("S", 5, True)
 bot = Player("Jarvis", 5, True)
 chatbot = ChatBot()

 while player.points < max_points and bot.points < max_points:
 # Print the option list to let the user know his options
  print("Your cards are:")
  player.show_d()k()

  try:
   user_inputs = chatbot.phrase_recognition(1)                                       # Let the user to input their card
   userPlayedCard = player.find_card(user_inputs[0], user_inputs[1])
   if userPlayedCard is not None:
    print("")
    botPlayedCard = random.choice(bot.deck)                                       # Random card played by the bot
    competition(player, bot, userPlayedCard, botPlayedCard)
   else:                                                                    # For invalid inputs
    print("\nYou tried to play an invalid card! Please try again!")
  except TypeError:
   print("\nYou tried to play an invalid card! Please try again!")

   print("\n*********************")
   print("User " + str(player.points) + " vs. Bot " + str(bot.points))
   print("*********************\n")

  if player.points < bot.points:
   print("The player is a machine, so it is able to make better calculations! Train yourself and come bacK!")
   print("Do not let a robot to be better than you!")
  elif player.points == bot.points:
   print("A draw! Search a sudoku website to train your brain!")
  else:
   print("Congrats! You won the battle with robots!")
   print("If they will invade us, you will be a great person to defend the humanity!")
game(5)
