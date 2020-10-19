import random
word_list = ["palarie", "deget", "picior", "abecedar"]

def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Sa jucam Spanzuratoarea")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Ghiceste o litera sau cuvantul: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Ai mai incercat aceasta litera", guess, "!")
            elif guess not in word:
                print(guess, "Nu face parte din cuvant :(")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Foarte bine,", guess, "face parte din cuvant!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Ai mai incercat aceasta litera ", guess, "!")
            elif guess != word:
                print(guess, " Nu acesta este cuvantul :(")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Nu exista")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Foarte bine, ai ghicit cuvantul!")
    else:
        print("Imi pare rau, ai ramas fara incercari. Cuvantul era " + word + ". Poate data viitoare!")




def display_hangman(tries):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    return stages[tries]

def main():
    word = get_word(word_list)
    play(word)
    while input("Incerci din nou? (Y/N) ").upper() == "Y":
        word = get_word(word_list)
        play(word)

if __name__ == "__main__":
    main()