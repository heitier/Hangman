import random

word_list = ["aardvark", "baboon", "camel", "cattle", "dog", "elephant", "fish", "goat", "kangaroo", "hamster"]
lives = 6
tracked_lives = 0

random_word = random.choice(word_list)
# print (random_word)

placeholder = ""
prev_g = []

for letter in random_word:
    placeholder += "_"
print(placeholder)

game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in prev_g:
        print("You already guessed that letter!")
        tracked_lives += 1

    else:
        prev_g.append(guess)
        display = []

        for letter in random_word:
            if letter in prev_g:
                display.append(letter)
            else:
                display.append("_")

        if guess not in random_word :
            tracked_lives += 1


    display_str = "".join(display)
    print(display_str)
    print(f"Lives remaining: {lives - tracked_lives}")


    #print(display)
    if "_" not in display:
        game_over = True
        print("You win!")
    elif lives - tracked_lives == 0:
        game_over = True
        print("You lose!")




if __name__ == "__main__":
    # Code to be executed only if this module is run as the main script
    pass
