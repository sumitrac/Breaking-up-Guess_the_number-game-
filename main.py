import random

RANGE_LOW = 0
RANGE_HIGH = 100
# pick a random number
random_number = random.randint(RANGE_LOW, RANGE_HIGH)


#guess_the_number processes the user's guess 
def guess_the_number():

      user_input = get_number_from_user()

      if user_input < RANGE_LOW or user_input > RANGE_HIGH:
          print(f"Your guess is out of bounds.")
          print(f"It must be between {RANGE_LOW} and {RANGE_HIGH}")
      elif user_input == random_number:
          print("You guessed the number!  Good job!")
      elif user_input > random_number:
          print("Your guess is too high")
      elif user_input < random_number:
          print("Your guess is too low")

#get_number_from_user gets input from user
def get_number_from_user():
    user_input_string = input("Guess the number: ")
    user_input = None
    if user_input_string.isnumeric():
        user_input = int(user_input_string)
    else:
        print("You must input a number!")

    return user_input







guess_the_number()