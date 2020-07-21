# Bohan Lin
#
# Description: This program will play the Rock Paper Scissor game with the user

SENTINEL = 'quit'
import random

def main():
	response = input ("Please choose a strategy that the computer will use to play the game.\nrandom: The comoputer will randomly choose among rock, paper, or scissor,\nestimate: The computer will estimate your choice and counter your choice to play.\nquit: quit the game.")
	strategy(response)

def strategy(response): # use different strategies to play
	user = input("Please choose among r (rock), p (paper), s (scissor). ")
	if response == "random":
		randomOutput(user)
	if response == "estimate":
		estimate(user)

def randomOutput(user): # use random number
	while user != SENTINEL:
		computer = random.randint(1, 3)
		# 1 is rock, 2 is paper, 3 is scissor
		game(user, computer)
		user = input("Please choose among r (rock), p (paper), s (scissor).\nquit (to quit the game)")

def estimate(user): # according to what the user has chosen, the computer will choose at least will make the game a tie
	count_r=0
	count_p=0
	count_s=0

	while user != SENTINEL:
		if count_r > count_p and count_r > count_s:
			computer = 2
		elif count_p > count_r and count_p > count_s:
			computer = 3
		elif count_s > count_r and count_s > count_p:
			computer = 1
		elif count_r == count_p and count_r > count_s:
			computer = 2
		elif count_s == count_r and count_s > count_p:
			computer = 1
		elif count_p == count_s and count_p > count_r:
			computer = 3
		else:
			computer = random.randint(1, 3)
		game(user, computer)
		print()
		user = input("Please choose among r (rock), p (paper), s (scissor).\nquit (to quit the game)")
		# count the time that the user has chosen among rock, paper, or scissor
		if user == "r":
			count_r +=1
		elif user == "p":
			count_p +=1
		else:
			count_s +=1

def game(user, computer): # basically how the game works
	if user == "r":
		if computer == 1:
			print("The game is a tie.")
		elif computer == 2:
			print("You lose!")
		else:
			print("You win!")
	elif user == "p":
		if computer == 1:
			print("You win!")
		elif computer == 2:
			print("The game is a tie.")
		else:
			print("You lose!")
	elif user == "s":
		if computer == 1:
			print("You lose!")
		elif computer == 2:
			print("You win!")
		else:
			print("The game is a tie.")
	else:
		print("Wrong input. Please enter r (rock), p (paper), or s (scissor).")

main()
