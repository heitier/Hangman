import random

word_list = ["aardvark", "baboon", "camel", "cattle", "dog", "elephant", "fish", "goat", "kangaroo", "hamster"]

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
    prev_g.append(guess)
    display = []
    for letter in random_word:
        if letter in prev_g:
            display.append(letter)
        else:
            display.append("_")
    display_str = "".join(display)
    print(display_str)

    #print(display)
    if "_" not in display:
        game_over = True
        print("You win!")






if __name__ == "__main__":
    # Code to be executed only if this module is run as the main script
    pass
