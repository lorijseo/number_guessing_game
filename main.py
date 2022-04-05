import random

# create a pool of numbers between 1 and 100
number_list = []
for number in range(1,101):
    number_list.append(number)
# computer chooses random number from the list
chosen_number = random.choice(number_list)
# TEST CASE- reference number that I need to guess
print(f"Here is the number: {chosen_number}")

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
# dependent on difficult level, number of attempts (global variable)
if difficulty_level == "easy":
    attempt = 10
elif difficulty_level == "hard":
    attempt = 5
else:
    print("Did not understand. Goodbye")
# since attempt is a global variable, i can use it in my while loop
while attempt != 0:
    print("Guess again.")
    print(f"You have {attempt} attempts remaining to guess the number")
    attempt -= 1
    guess = int(input("Make a guess: "))
    if guess < chosen_number:
        print("Too low!")
    elif guess > chosen_number:
        print("Too high!")
    else:
        print(f"You got it! The answer was {chosen_number} ")
        break
# while loop can end based on either one of two conditions:
# condition #1 when attempts reach zero
# condition #2 when user guesses number
# created two different output dependent on condition met
if attempt == 0:
    print("You are out of attempts! You lose.")


