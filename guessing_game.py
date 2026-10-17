# Name: Makhari Russom
# Date: October 14th
# Description: Guessing Game Project


secret_num = input("Enter target number: ").strip()

if not secret_num.isdigit():
    print("Invalid Input.")
else:
    secret_num = int(secret_num)
    max_guess = input("Enter max number of guesses: ")

    if not max_guess.isdigit() or int(max_guess) < 1:
        print("Invalid input. Ending game.")
    else:
        max_guess = int(max_guess) 
        guess_count = 0
        total = 0
        won = False
        invalid = False

        while guess_count < max_guess and not won and not invalid:
            guess_num = input(f"Guess {guess_count + 1} of {max_guess}: ").strip()

            if not guess_num.isdigit():
                print("Invalid Input. Ending game.")
                invalid = True
            else:
                guess = int(guess_num)
                guess_count += 1
                total += guess

                if guess > secret_num:
                    print("Too high.")
                elif guess < secret_num:
                    print("Too low.")
                else: 
                    print(f"You got it! Guesses used: {guess_count}")
                    won = True
        if not won and not invalid:
            print(f"Out of guesses. The number was {secret_num}")