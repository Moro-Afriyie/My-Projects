import ps3

'''
def subs(substitute, hand2, word_list):
    if substitute == 'yes':
        letter = str(input('Which letter would you like to replace: '))
        hand2 = ps3.substitute_hand(hand2, letter)
        total = ps3.play_hand(hand2, word_list)
        # print(hand2)
    elif substitute == 'no':
        total = ps3.play_hand(hand2, word_list)
        # print(hand2)
'''

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
    while True:
        try:
            ps3.HAND_SIZE = int(input('Enter the total number of hands( Number of letters you want): '))
            break
        except ValueError:
            print('Input should be a number !! ')
    hand = ps3.deal_hand(ps3.HAND_SIZE)
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
    ps3.display_hand(hand2)
    substitute = str.lower(input('Would you like to substitute a letter?(yes/no) : '))

    if substitute == 'yes':
        letter = str(input('Which letter would you like to replace: '))
        hand2 = ps3.substitute_hand(hand2, letter)
        total += ps3.play_hand(hand2, word_list)
        replay = input('Would you like to replay the hand? yes/no: ')
        if replay == 'yes':
            total1 += ps3.play_hand(hand2, word_list)
            if total <= total1:
                total = total1
            print('Total score : ', total)

        if replay == 'no':
                hand = ps3.deal_hand(ps3.HAND_SIZE)
                # print(hand)
                print('Current Hand: ', end=' ')
                ps3.display_hand(hand)
                substitute = str.lower(input('Would you like to substitute a letter?(yes/no) : '))
                if substitute == 'yes':
                    letter = str(input('Which letter would you like to replace: '))
                    hand = ps3.substitute_hand(hand, letter)
                    total += ps3.play_hand(hand, word_list)
                    replay = input('Would you like to replay the hand? yes/no: ')
                    if replay == 'yes':
                        total1 += ps3.play_hand(hand, word_list)
                        if total <= total1:
                            total = total1
                        print('Total score over all hands: ', total+total1)
                    elif replay == 'no':
                        print('total score  : ', total)
                elif substitute == 'no':
                    total3 += ps3.play_hand(hand, word_list)
                    replay = input('Would you like to replay the hand? yes/no: ')
                    if replay == 'yes':
                        # total1 += ps3.play_hand(hand, word_list)
                        total1 += ps3.play_hand(hand, word_list)
                        if total <= total1:
                            total = total1
                            print('Total score over all hands: ', total+total1)
                    elif replay == 'no':
                        print('Total score over all hands: ', total+total1)

    elif substitute == 'no':
        result += ps3.play_hand(hand2, word_list)
        replay = input('Would you like to replay the hand? yes/no: ')
        if replay == 'yes':
            total1 += ps3.play_hand(hand2, word_list)
            if result <= total1:
                result = total1
            print('total score  : ', result)

        if replay == 'no':
            # while replay == 'no':
                hand = ps3.deal_hand(ps3.HAND_SIZE)
                # print(hand)
                print('Current Hand: ', end=' ')
                ps3.display_hand(hand)
                substitute = str.lower(input('Would you like to substitute a letter?(yes/no) : '))
                if substitute == 'yes':
                    letter = str(input('Which letter would you like to replace: '))
                    hand = ps3.substitute_hand(hand, letter)
                    total2 += ps3.play_hand(hand, word_list)
                    replay = input('Would you like to replay the hand? yes/no: ')
                    if replay == 'yes':
                        total3 += ps3.play_hand(hand, word_list)
                        if total2 <= total3:
                            total2 = total3
                        print('Total score over all hands: ', result+total2)
                    elif replay == 'no':
                        print('total score  : ', total2)
                elif substitute == 'no':
                    total4 += ps3.play_hand(hand, word_list)
                    replay = input('Would you like to replay the hand? yes/no: ')
                    if replay == 'yes':
                        total1 += ps3.play_hand(hand, word_list)
                        if total4 <= total1:
                            total4 = total1
                            print('Total score over all hands: ', result+total4)
                    elif replay == 'no':
                        print('Total score over all hands: ', result+total4)


'''
    if total <= total:
        print('total : ', total+total2)
    else:
        print('total : ', total+total2)
'''
#word = 'honey'
#hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}
#word = 'c*ws'
#hand = {'c': 1, 'o': 1, '*': 1, 'w': 1, 's': 1, 'z': 1, 'y': 2}
#word_list = ps3.load_words()
# print(is_valid_word(word, hand, word_list))
# new_word.count(i, 0, len(new_word))
# ps3.display_hand({'c': 1, 'o': 1, '*': 1, 'w': 1, 's': 1, 'z': 1, 'y': 2})
#  and hand: {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}
# Expected True, but got False for word: 'EVIL' and hand: {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}
# Expected False, but got True for word: 'Even' and hand: {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}
# 'h*ney' and hand: {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2
# Expected False, but got True for word: 'honey' and hand: {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}
# 	Expected False, but got True for word: 'c*wz' and hand: {'c': 1, 'o': 1, '*': 1, 'w': 1, 's': 1, 'z': 1, 'y': 2}
# print(ps3.load_words())
# {'i': 1, 'u': 1, '*': 1, 'h': 1, 't': 1, 'd': 1}, di*
v = []

play_game(ps3.load_words())


