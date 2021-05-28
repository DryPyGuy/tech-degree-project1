import random

username = input("Hi, what should we call you? ")
print(f"Alright, {username}, welcome to DryPy's Guessing Game!")

def start_game():
    number_to_guess = random.randrange(1, 11)
    guess_count = 1
    guess = None
    
    while guess != number_to_guess:
        try:
            guess = int(input("I am thinking of a number between 1-10, what's your guess? "))
            if guess < number_to_guess:
                print("Your guess was lower then the secret number")
                guess_count += 1
            elif guess > number_to_guess:
                print("Your guess was higher then the secret number")
                guess_count += 1
            else: 
                print(f"Whoa, {username}! You got it right!")
                print(f"It took you {guess_count} trys to get the right answer.")
                print("See you next ime!")
                break
        except ValueError:
            print("Hmm, that doesn't look like a number between 1-10")
            
start_game()
