import ps3


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
    words = ps3.load_words()
    if new_word in words:  # checks if the word is in the word list
        for a, b in hand2.items():
            if a == '*':
                for i in range(len(ps3.VOWELS)):
                    if ps3.VOWELS[i] in k:
                        continue
                    elif ps3.VOWELS[i] in new_word and ps3.VOWELS[i] not in k:
                        a = a.replace(a, ps3.VOWELS[i])
                        break
            if b > 0 and b != 1:
                m = a * new_word.count(a, 0, len(new_word))  # assigns how may times a letter repeats itself in a
                # word and loops through it
                for i in range(len(m)):  # stores the letters in the same way as the word in a list no matter how
                    k.append(m[i])  # many same number of letter a user has
            elif b == 1 and a in new_word:
                k.append(a)
        print(k)
        if len(new_word) == len(k):  # compares to see if the word the user entered is valid
            return True
        else:
            return False
    elif new_word.find('*') == 1:  # checks if the word has asterisk
        for i in range(len(ps3.VOWELS)):  # assigns a vowel to the asterisks and checks if the word is in the word list
            replaced_word = str.lower(new_word).replace('*', ps3.VOWELS[i])  # replaces the asterisk with a vowel
            c = ps3.VOWELS[i]  # stores the vowel that gave us the word
            if replaced_word in word_list:  # breaks immediately a word has been found
                break
            else:
                continue
        #print(c)
        if replaced_word not in word_list:  # it returns false if the word is not in the word list after all the
            return False  # vowels have been tried
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
            print(k)
            if len(replaced_word) == len(k):  # compares to see if the word the user entered is valid
                return True
            else:
                return False
    else:  # returns false if the word is not in the word list
        return False


# print(is_valid_word('p*b', {'u': 2, '*': 1, 'b': 1, 'p': 1, 'c': 1, 't': 1}, ps3.load_words()))
#hand2 = {'g': 1, 'e': 1, '*': 1, 'n': 1, 'x': 1}
#new_word = '0xen'
#word_list = ps3.load_words()
k = []
# play_hand({'g': 1, 'e': 1, '*': 1, 'n': 1, 'x': 1}, ps3.load_words())
# {{'u': 2, '*': 1, 'b': 1, 'p': 1, 'c': 1, 't': 1}
#if 'oval' in word_list:
    # print('True'

moro = 'abc'
def permutation(sequence):
    if len(sequence) == 1:
        print(sequence)
    else:
        for i in range(len(sequence)):
            m = sequence[i:] + sequence[i+1:]
            print(m)


# permutation(moro)

def permute(prefix, suffix):
 '''
 Recursively shifts all the elements in suffix into
 prefix producing all the permutations of suffix.
 Prints all permutations in lexicographical order.
 '''
 suffix_size = len(suffix)
 if suffix_size == 0: # Have we considered all the elements?
    print(prefix)
 else:
     for i in range(0, suffix_size):
         new_pre = prefix + [suffix[i]]
         print('new_pre: ', new_pre)
         print('---------')
         new_suff = suffix[:i] + suffix[i + 1:]
         print('new_suff: ', new_suff)
         print('---------')
         permute(new_pre, new_suff)

def print_permutations(lst):

    permute([], lst)

def main():
 a = list(moro)
 print_permutations(a)

main()