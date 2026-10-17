# Name: Makhari Russom
# Date: October 14th
# Description: Guessing Game Project


secret_num = input("Enter target number: ").strip()

if not secret_num_num.isdigit():
    print("Invalid Input.")
else:
    target = int(secret_num)
    max_guess = input("Enter max number of guesses: ")

    if not max_text.isdigit() or int(max_num) < 1:
        print("Invalid input.")
    else:
        max_num = int(max_num) < 1:
        guess_count = 0
        total = 0
        won = False
        invalid = False

        while guess_count < max_guesses and not won and not invalid:
            guess_num = input(f"Guess {guess_count + 1} of {max_guesses}:").strip()

            if not guess_num.isdigit():
                print("Invalid Input.")
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
                    print(f"Correct! Guesses used: {average:.2f}")
        if not won and not invalid:
            print(f"Out of guesses. The number was {secret_num}")