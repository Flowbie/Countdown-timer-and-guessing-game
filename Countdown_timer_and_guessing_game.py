# Dolan, Austin
# ICS 110P Assignment 07.2
# November 21 2022
# Program uses functions to roll dice, a small guessing game, countdown from a given number in seconds

import time
import math
import random

# Greet user and ask which of my programs they would like to run
def main():
	try:
		# Variables
		user_name = input("Hello and welcome to my program.\n\nWhat is your name? ").capitalize()
		play = input(f"\n{user_name}, my program can perform 3 operations:\n\n  1. Roll some dice\n  2. Play a HiLo guessing game\n  3. Countdown timer\n\nAre you ready to play?(yes or no) ").lower()
		response = ""
		t = 0
		while play != 'no':
			if play == 'yes':
				command = int(input("Do you want to play game 1, 2, or 3?(enter the #) "))
				if command == 1:
					roll_num = 0
					# Ask user how many dice they want to roll, if they don't enter a real number ask again
					roll_num = int(input("\nHow many dice do you want to roll? "))
					if roll_num > 0:
						dice_roll(roll_num)
						play = input("Play again?(yes or no) ")
					else:
						roll_num = int(input("\nHow many dice do you want to roll? "))
				elif command == 2:
					# HI-LOW guessing game user gets 5 chances to find a random number between 1-100 inclusively
					print("\nYou choose the Hi-Low Guessing Game.\nI'll give you 5 chances to guess a number between 1-100.\nI will tell you if the number you guessed is higher or lower then my number.")
					guess = int(input("\nWhat's your guess? "))
					hi_lo_guess(guess, random_num = random.randint(1,100))
					print(response)
					play = input("Play again?(yes or no) ")
				elif command == 3:
					# Ask user how many seconds to count down from 
					t = int(input("This game is a countdown timer.  How many seconds should I count down from? "))
					print(countdown_timer(t))
					# Rest for 1 seconds and ask to play again
					time.sleep(1)
					play = input("Play again?(yes or no) ")
				else:
					# If user doesn't respond with 1, 2, or 3 ask if they want to keep playing
					print("That's not one of my options.")
					play = input("Do you want to keep playing?(yes or no) ")
			else:
				# If user doesn't respond with yes or no ask if they want to play
				print(f"\n{play} is not a valid response.")
				play = input("Are you ready to play?(yes or no) ")
	except ValueError as e:
		# Value error exception to keep playing the game
		print()
		print("That is not a valid number. Please try again.")
		print("Error:", end = " ")
		print(e)
		print()
	

	print("Thank's for playing. Goodbye")
	
def dice_roll(roll_num):
	# Loop for every dice rolled print a value between 1-6
	for i in range(roll_num):
		rolls = random.randint(1, 6)
		print(rolls)


def hi_lo_guess(guess, random_num = random.randint(1,100)):
	# Hi Lo guessing game creates random value between 1-100 and compares with user's guess if guess count reaches 5 they lose
	guess_count = 0
	guess_limit = 4

	while guess != random_num and guess_count < guess_limit:
		if guess < 0 or guess > 100:
			guess = int(input("\nWhat's your guess? (1-100) "))
		else:
			# Run guessing game until number is guessed or guess_limit is reached
			if guess > random_num:
				print("Your guess is higher then my number.")
				guess = int(input("\nWhat's your guess? "))
				guess_count+=1
			else:
				print("Your guess is lower then my number.")
				guess = int(input("\nWhat's your guess? "))
				guess_count+=1

	if guess == random_num:
		# Tell user they won if they guess the right number and return number of guesses
		print("That's my number! Can you read minds??")
		guess_count+=1
		response = print("You guessed my number in " + str(guess_count) + " guess(es)!")
	else:
		# Else return that they ran out of guesses
		response = print("You are out of guesses. My number was " + str(random_num) + ", try again next time.")
	return response
def countdown_timer(t):
	# Take input from user divmod by 60 to get minutes and seconds and count down from there until 0
	while t:
		mins, secs = divmod(t, 60)
		timer = f"{mins:02d}:{secs:02d}"
		print(timer, end = "\n")
		time.sleep(1)
		t-=1
		if t == 0:
			return "Time's up!"

main()

