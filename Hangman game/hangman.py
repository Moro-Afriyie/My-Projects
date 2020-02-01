# Problem Set 2, hangman.py
# Name: AFRIYIE MORO OWUSU
# Collaborators: none
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if secret_word == ''.join(letters_guessed):  # Can also be written as if list(secret_word) == letters_guessed
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters = []
    for word in list(secret_word):
        if word in letters_guessed:
            letters.append(word)
        else:
            letters.append('_')
    if ''.join(letters) == secret_word:
        return secret_word
    else:
        return ' '.join(letters)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import string
    available_letters = []
    for words in string.ascii_lowercase:
        if words in letters_guessed:
            continue
        else:
            available_letters.append(words)
    return ''.join(available_letters)
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''

    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import string
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), ' letters long.')
    print('You have 3 warnings left.')
    print('------------------------------------------------')
    print('You have 6 guesses left.')
    print('Available letters: ', string.ascii_lowercase)
    guesses = 6
    letter = []  # stores the rightly guessed letters
    letter2 = []  # stores all the letters the user try to guess
    warnings = 3
    vowels = ['a', 'e', 'i', 'o', 'u']
    while guesses > 0:
        guess_letter1 = input('Please guess a letter: ​')

        if guess_letter1.isalpha() or guess_letter1.islower():  # checks if input is an alphabet or lower case
            guess_letter = str.lower(guess_letter1)  # converts any upper case letter to lower case
            if guess_letter in letter2:  # checks to see if the letter has already been entered
                if warnings == 0:
                    guesses -= 1
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:",
                          get_guessed_word(secret_word, letter))
                    print('-----------------------------------')
                    print('You have ', guesses, 'guesses left')
                    print('Available letters: ', get_available_letters(letter2))
                else:
                    warnings -= 1  # and subtracts one from warning
                    print("Oops! You've already guessed that letter. You now have", warnings, ' warnings left: ',
                          get_guessed_word(secret_word, letter))
                    print('-----------------------------------')
                    print('You have ', guesses, 'guesses left')
                    print('Available letters: ', get_available_letters(letter2))
            elif guess_letter in secret_word:
                letter.append(guess_letter)
                letter2.append(guess_letter)
                if get_guessed_word(secret_word, letter) == secret_word:
                    #  prints a congratulations message when the user gets the word right
                    print('Good guess: ', get_guessed_word(secret_word, letter))
                    print('-----------------------------------')
                    print('Congratulations. You won!!')
                    print('Your total score for this game is: ', guesses * len(letter))
                    break
                else:
                    print('Good guess: ', get_guessed_word(secret_word, letter))
                    print('-----------------------------------')
                    print('You have', guesses, ' guesses left.')
                    print('Available letters: ', get_available_letters(letter2))
            else:
                letter2.append(guess_letter)
                print('Oops! That letter is not in my word: ', get_guessed_word(secret_word, letter))
                # print(final_letter)
                if guess_letter in vowels:
                    guesses -= 2
                else:
                    guesses -= 1
                if guesses <= 0:
                    print('-----------------------------------')
                    break
                print('-----------------------------------')
                print('You have', guesses, ' guesses left.')
                print('Available letters: ', get_available_letters(letter2))
        elif warnings == 0:  # if the input is invalid and warnings is 0, subtract 1 from guess
            guesses -= 1
            print('Oops! That is not a valid letter!!!. You have', guesses, ' guesses left: ')
            print('-----------------------------------')
            print('You have ', guesses, 'guesses left')
            print('Available letters: ', get_available_letters(letter2))
        else:
            warnings -= 1  # if the input is invalid, subtract 1 from warnings
            print('Oops! That is not a valid letter!!!. You have', warnings, ' warnings left: ',
                  get_guessed_word(secret_word, letter))
            print('-----------------------------------')
            print('You have ', guesses, 'guesses left')
            print('Available letters: ', get_available_letters(letter2))
    if guesses <= 0:
        print('Sorry, you ran out of guesses. The word was : ', secret_word)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    space = my_word.replace(' ', '')  # removes the spaces
    underscore = space.replace('_', '')  # removes the underscores
    if len(space) == len(other_word):  # checks for the length of the guessed word is equal to the length of the words
        # in the text file
        for a, b in zip(space, other_word):  # zip is used to compare and join two different list together
            # instead of a for loop
            if (a != '_' and a != b) or (a == '_' and b in underscore):  # it compares the letter in the first list
                # to the second one to see if they are different and returns false else returns true
                return False
        return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    words_in_text_file = wordlist  # loads all the words in the text file into a list
    for i in words_in_text_file:  # loops through the list and see the one that matches the incomplete word  and
        if match_with_gaps(my_word, i) is True:
            print(i, end=' ')   # and prints the list of words that matches the incomplete words(hints)


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    import string
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ', len(secret_word), 'letters long.')
    print('You have 3 warnings left.')
    print("You can press '*' for hints.")
    print('------------------------------------------------')
    print('You have 6 guesses left.')
    print('Available letters: ', string.ascii_lowercase)
    guesses = 6
    letter = []  # stores the rightly guessed letters
    letter2 = []  # stores all the letters the user try to guess
    warnings = 3
    vowels = ['a', 'e', 'i', 'o', 'u']
    while guesses > 0:
        guess_letter1 = input('Please guess a letter: ​')

        if guess_letter1.isalpha() or guess_letter1.islower():  # checks if input is an alphabet or lower case
            guess_letter = str.lower(guess_letter1)  # converts any upper case letter to lower case
            if guess_letter in letter2:  # checks to see if the letter has already been entered
                if warnings == 0:
                    guesses -= 1
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:",
                          get_guessed_word(secret_word, letter))
                    print('-----------------------------------')
                    print('You have ', guesses, 'guesses left')
                    print('Available letters: ', get_available_letters(letter2))
                else:
                    warnings -= 1           # and subtracts one from warning
                    print("Oops! You've already guessed that letter. You now have", warnings, ' warnings left: ',
                          get_guessed_word(secret_word, letter))
                    print('-----------------------------------')
                    print('You have ', guesses, 'guesses left')
                    print('Available letters: ', get_available_letters(letter2))
            elif guess_letter in secret_word:
                letter.append(guess_letter)
                letter2.append(guess_letter)
                if get_guessed_word(secret_word,  letter) == secret_word:
                    #  prints a congratulations message when the user gets the word right
                    print('Good guess: ', get_guessed_word(secret_word, letter))
                    print('-----------------------------------')
                    print('Congratulations. You won!!')
                    print('Your total score for this game is: ', guesses*len(letter))
                    break
                else:
                    print('Good guess: ', get_guessed_word(secret_word,  letter))  # prints the word in the _ _ _ _ form
                    print('-----------------------------------')
                    print('You have', guesses, ' guesses left.')
                    print('Available letters: ', get_available_letters(letter2))  # prints the letters that has not been
                    # entered
            else:
                letter2.append(guess_letter)
                print('Oops! That letter is not in my word: ', get_guessed_word(secret_word,  letter))
                if guess_letter in vowels:
                    guesses -= 2
                else:
                    guesses -= 1
                if guesses <= 0:
                    print('-----------------------------------')
                    break
                print('-----------------------------------')
                print('You have', guesses, ' guesses left.')
                print('Available letters: ', get_available_letters(letter2))
        elif guess_letter1 == '*':  # inputs that key to get the hints of words
            print('Possible word matches are: ', get_guessed_word(secret_word, letter))
            show_possible_matches(get_guessed_word(secret_word, letter))
            print('\n-----------------------------------')
            print('You have ', guesses, 'guesses left')
            print('Available letters: ', get_available_letters(letter2))

        elif warnings == 0:  # if the input is invalid and warnings is 0, subtract 1 from guess
            guesses -= 1
            print('Oops! That is not a valid letter!!!. You have', guesses, ' guesses left: ')
            print('-----------------------------------')
            print('You have ', guesses, 'guesses left')
            print('Available letters: ', get_available_letters(letter2))
        else:
            warnings -= 1  # if the input is invalid, subtract 1 from warnings
            print('Oops! That is not a valid letter!!!. You have',  warnings, ' warnings left: ',
                  get_guessed_word(secret_word,  letter))
            print('-----------------------------------')
            print('You have ', guesses, 'guesses left')
            print('Available letters: ', get_available_letters(letter2))
    if guesses <= 0:
        print('Sorry, you ran out of guesses. The word was : ', secret_word)




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
     #pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
      secret_word = choose_word(wordlist)
      hangman_with_hints(secret_word)
