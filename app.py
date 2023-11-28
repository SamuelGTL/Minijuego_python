#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

#print("--Paper, Rock, Scissors Game--!")
#create a loop that repeat the actions till the user wants to stop
win = 0
games = 0;
while True:
    games += 1;
    #import the random module
    import random
    #create a list of play options
    t = ["rock", "paper", "scissors"]
    #assign a random play to the computer
    computer = t[random.randint(0,2)]
    #set player to False
    player = False
    while player == False:
        #set player to True
        player = input("Rock, Paper, Scissors?")
        player = player.lower()
        if player == computer:
            print("-----------------------------------")
            #show the variable seleced by the computer
            print("Computer selected: ", computer)
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("-----------------------------------")
                #show the variable seleced by the computer
                print("Computer selected: ", computer)
                print("You lose!", computer, "covers", player)
            else:
                print("-----------------------------------")
                #show the variable seleced by the computer
                print("Computer selected: ", computer)
                print("You win!", player, "smashes", computer)
                win += 1
        elif player == "Paper":
            if computer == "Scissors":
                print("-----------------------------------")
                #show the variable seleced by the computer
                print("Computer selected: ", computer)
                print("You lose!", computer, "cut", player)
            else:
                print("-----------------------------------")
                #show the variable seleced by the computer
                print("Computer selected: ", computer)
                print("You win!", player, "covers", computer)
                win += 1
        elif player == "Scissors":
            if computer == "Rock":
                print("-----------------------------------")
                #show the variable seleced by the computer
                print("Computer selected: ", computer)
                print("You lose...", computer, "smashes", player)
            else:
                print("-----------------------------------")
                print("Computer selected: ", computer)
                print("You win!", player, "cut", computer)
                win += 1
        else:
            print("That's not a valid play. Check your spelling!")
        #player was set to True, but we want it to be False so the loop continues
        #player = False
        computer = t[random.randint(0,2)]
    #ask the user if they want to play again
    play_again = input("Do you want to play again? (Y/N)")
    if play_again.upper() != "Y":
        #show the count of games winned by the user
        print("Games played: ", games)
        print("You win", win, "games!")
        break


