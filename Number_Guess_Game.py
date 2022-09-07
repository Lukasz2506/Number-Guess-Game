#100 Days of Code, Dr Angela Yu
#Student Łukasz Świątek Brzeziński
#Number Guessing Game Project, try to use global variable in some function


from logo import logo
import random

print(logo) # creates a logo
print("Welcome to the Number Guessing Game!")


numbers = [element for element in range(1,101)] #created a list from 1 to 100
number = random.choice(numbers) # choose one number from the list
number_of_lives = 0 #there will be added the number of attempts related to game difficulty

def lives_no(): #just print the current attempts no
    print(f"You have {number_of_lives} attempts remaining to guess the number.")

def level(): # allows user to choose how many attempts he/she would like to get 
    global number_of_lives
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
    if difficulty == 'easy':
        number_of_lives += 10
    elif difficulty == 'hard':
        number_of_lives = 5
    else:
        print('There is no that option. Type again')
    return number_of_lives

move = True

while move: #protected from wrong difficulty level name
  choose_level = level()
  if choose_level != 0:
    move = False
    
lives_no() #call the level function

while number_of_lives > 0 : #loop for the game

    guess = int(input("Make a guess: ")) #for guess the number by user
    #conditions is user wins/loose, inform where the user is (too high / too low)
    if guess not in numbers:
        print("Out of the range 1-100")
        number_of_lives -= 1
        lives_no()
    elif guess > number:
        print("Too high.")
        number_of_lives -= 1
        lives_no()
    elif guess < number:
        print("Too low.")
        number_of_lives -= 1
        lives_no()
    else: #win statement (if no from upper statements were true
        print(f"{guess} is the number!!! You win!!!")

    if number_of_lives == 0: #loose statement (each wrong answer take one attempt point
        print("Game over. You loose :(")

