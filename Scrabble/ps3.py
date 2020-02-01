# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : MORO OWUSU AFRIYIE
# Collaborators : none
# Time spent    : one fuckin week :)

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    # print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    # print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """

    new_word = str.lower(word)
    sum2 = 0
    for a, b in SCRABBLE_LETTER_VALUES.items():  # loops through the dictionary and compares the letters
        for i in new_word:   # in the word to the letters in the dictionary to get their corresponding numbers or marks
            if i in a:       # in order to add them and print the scores
                sum2 += b    # test the code in the test_ps3 to see if it was right
                # print(i, "==", b)
    result = sum2 * (7 * len(new_word) - 3 * (n - len(new_word)))  # calculation of the scores
    if (7 * len(new_word) - 3 * (n - len(new_word))) > 0:
        return result
    else:
        return sum2 * 1

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    hand = {}
    num_vowels = int(math.ceil(n / 3))
     ##### ORIGINAL FUNCTION THAT PRINTS ONLY LETTERS WITHOUT A WILDCARD ("*")
    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    return hand
    """
    # FUNCTION THAT PRINTS  LETTERS WITH A WILDCARD ("*")
    hand = {}
    num_vowels = int(math.ceil(n / 4))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    hand['*'] = 1
    for i in range(num_vowels + 1, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    return hand


#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    new_word = str.lower(word)
    new_hand = {}
    hand2 = hand.copy()
    for i in hand2.keys():
        if i in new_word:   # checks for the letter that repeats itself in the word and reduces its value by the
            hand2[i] -= new_word.count(i, 0, len(new_word))  # number of times it repeats in the word
    for a, b in hand2.items():     # this loop prints only the letters remaining or the letters
        if a in new_word and b <= 0:  # available to the user after forming the word
            continue
        elif a in new_word or b > 0:
            new_hand[a] = b
    return new_hand


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    new_word = str.lower(word)
    hand2 = hand.copy()
    k = []
    words = load_words()
    if new_word in words:  # checks if the word is in the word list
        for a, b in hand2.items():
            if b > 0 and b != 1:
                m = a * new_word.count(a, 0, len(new_word))  # assigns how may times a letter repeats itself in a
                # word and loops through it
                for i in range(len(m)):  # stores the letters in the same way as the word in a list no matter how
                    k.append(m[i])  # many same number of letter a user has
            elif b == 1 and a in new_word:
                k.append(a)
        if len(new_word) == len(k):  # compares to see if the word the user entered is valid
            return True
        else:
            return False
    elif new_word.find('*') == 1:  # checks if the word has asterisk
        for i in range(len(VOWELS)):  # assigns a vowel to the asterisks and checks if the word is in the word list
            replaced_word = str.lower(new_word).replace('*', VOWELS[i])  # replaces the asterisk with a vowel
            c = VOWELS[i]                              # stores the vowel that gave us the word
            if replaced_word in word_list:       # breaks immediately a word has been found
                break
            else:
                continue
        if replaced_word not in word_list:  # it returns false if the word is not in the word list after all the
            return False   # vowels have been tried
        else:
            for a, b in hand2.items():
                if a == '*':
                    k.append(a.replace(a, c))  # replaces asterisk the vowel that when inserted, matched a word
                if b > 0 and b != 1:
                    m = a * replaced_word.count(a, 0, len(replaced_word))  # assigns how may times a letter
                    # repeats itself in a word and loops through it t
                    for i in range(len(m)):  # stores the letters in the same way as the word in a list no matter
                        k.append(m[i])  # how many same number of letter a user has
                elif b == 1 and a in replaced_word:
                    k.append(a)
            if len(replaced_word) == len(k):  # compares to see if the word the user entered is valid
                return True
            else:
                return False
    else:  # returns false if the word is not in the word list
        return False



#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    sum1 = 0
    hand2 = hand.copy()
    for i in hand2.values():
        sum1 += i
    return sum1

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    hand2 = hand.copy()
    total = 0
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score

    # As long as there are still letters left in the hand:

    # Display the hand
    print('Current Hand: ', end=' ')
    display_hand(hand2)

    word = input('Enter word, or "!!" to indicate that you are finished: ')  # Ask user for input
    while word != '!!':  # If the input is two exclamation points. End the game (break out of the loop)
        # Otherwise (the input is not two exclamation points):
        if is_valid_word(word, hand2, word_list) is True:  # If the word is valid:
            score = get_word_score(word, calculate_handlen(hand2))
            total += score  # Keep track of the total score
            # Tell the user how many points the word earned, and the updated total score
            print('"' + word + '"', 'earned', score, 'points.  Total: ', total, 'points')
            hand2 = update_hand(hand2, word)  # update the user's hand by removing the letters of their
            # inputted word
            if calculate_handlen(hand2) == 0:
                print('\nRan out of letters.')
                break
            print('\nCurrent Hand: ', end=' ')
            display_hand(hand2)
        elif is_valid_word(word, hand2, word_list) is False:  # Otherwise (the word is not valid):
            print('That is not a valid word. ', end='')  # Reject invalid word (print a message)
            hand2 = update_hand(hand2, word)
            if calculate_handlen(hand2) == 0:
                print('Ran out of letters.')
                break
            print('Please choose another word.')
            print('\nCurrent Hand: ', end=' ')
            display_hand(hand2)
        word = input('Enter word, or "!!" to indicate that you are finished: ')
    print('Total score for this hand: ', total)
    print('------------------------------------')  # Game is over (user entered '!!' or ran out of letters),
    return total
    # so tell user the total score
    # return total  # Return the total score as result of function



#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    k = []
    # This one tries to return a random letter from the alphabets
    for i in VOWELS + CONSONANTS:  # ensures that the new letter is not part of the letters in the hand or the
        if i in hand.keys() or i == letter:  # to be substituted
            continue
        else:
            k.append(i)
    # print(random.choice(''.join(k)))
    q = {}
    # This code replaces the letter to be substituted with the random letter generated
    for a, b in hand.items():
        if a == letter:  # if the letter in the dictionary matches the letter to be substituted,
            q[a.replace(a, random.choice(''.join(k)))] = b  # creates a new dictionary to store the old hand a replace
            # the letter to be substituted
        else:
            q[a] = b
    # print(q)
    return q
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    while True:  # This loop handles exceptions thus, making sure the input is always an integer
        try:
            HAND_SIZE = int(input('Enter the total number of hands( Number of letters you want): '))
            break
        except ValueError:
            print('Input should be a number !! ')
    hand = deal_hand(HAND_SIZE)
    hand2 = hand.copy()
    result = 0
    total = 0
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0
    # WROTE THIS FUNCTION ACCORDING TO THE STATEMENTS  AT THE TOP
    # print(hand2)
    print('Current Hand: ', end=' ')
    display_hand(hand2)
    # allows for substitution of a letter
    substitute = str.lower(input('Would you like to substitute a letter?(yes/no) : '))

    if substitute == 'yes':
        letter = str(input('Which letter would you like to replace: '))
        hand2 = substitute_hand(hand2, letter)  # function for substituting hand
        total += play_hand(hand2, word_list)
        replay = input('Would you like to replay the hand? yes/no: ')
        if replay == 'yes':
            total1 += play_hand(hand2, word_list)
            if total <= total1:
                total = total1
            print('Total score : ', total)

        if replay == 'no':
            hand = deal_hand(HAND_SIZE)
            # print(hand)
            print('Current Hand: ', end=' ')
            display_hand(hand)
            substitute = str.lower(input('Would you like to substitute a letter?(yes/no) : '))
            if substitute == 'yes':
                letter = str(input('Which letter would you like to replace: '))
                hand = substitute_hand(hand, letter)
                total += play_hand(hand, word_list)
                replay = input('Would you like to replay the hand? yes/no: ')
                if replay == 'yes':
                    total1 += play_hand(hand, word_list)
                    if total <= total1:
                        total = total1
                    print('Total score over all hands: ', total + total1)
                elif replay == 'no':
                    print('total score  : ', total)
            elif substitute == 'no':
                total3 += play_hand(hand, word_list)
                replay = input('Would you like to replay the hand? yes/no: ')
                if replay == 'yes':
                    total1 += play_hand(hand, word_list)
                    if total <= total1:
                        total = total1
                        print('Total score over all hands: ', total + total1)
                elif replay == 'no':
                    print('Total score over all hands: ', total + total1)

    elif substitute == 'no':
        result += play_hand(hand2, word_list)
        replay = input('Would you like to replay the hand? yes/no: ')
        if replay == 'yes':
            total1 += play_hand(hand2, word_list)
            if result <= total1:
                result = total1
            print('total score  : ', result)

        if replay == 'no':
            hand = deal_hand(HAND_SIZE)
            # print(hand)
            print('Current Hand: ', end=' ')
            display_hand(hand)
            substitute = str.lower(input('Would you like to substitute a letter?(yes/no) : '))
            if substitute == 'yes':
                letter = str(input('Which letter would you like to replace: '))
                hand = substitute_hand(hand, letter)
                total2 += play_hand(hand, word_list)
                replay = input('Would you like to replay the hand? yes/no: ')
                if replay == 'yes':
                    total3 += play_hand(hand, word_list)
                    if total2 <= total3:
                        total2 = total3
                    print('Total score over all hands: ', result + total2)
                elif replay == 'no':
                    print('total score  : ', total2)
            elif substitute == 'no':
                total4 += play_hand(hand, word_list)
                replay = input('Would you like to replay the hand? yes/no: ')
                if replay == 'yes':
                    total1 += play_hand(hand, word_list)
                    if total4 <= total1:
                        total4 = total1
                        print('Total score over all hands: ', result + total4)
                elif replay == 'no':
                    print('Total score over all hands: ', result + total4)


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
