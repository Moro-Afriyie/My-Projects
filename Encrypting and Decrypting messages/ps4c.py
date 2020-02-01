# Problem Set 4C
# Name: MORO AFRIYIE
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    # print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    #  print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    #>>> is_word(word_list, 'bat') returns
    True
    #>>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object

        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()

    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)

        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled
        according to vowels_permutation. The first letter in vowels_permutation
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''

        alphabets = {}  # dictionary of alphabets
        i = 1
        j = 1
        mapping_dict = {}
        m = vowels_permutation
        # A DICTIONARY THAT HOLDS ALL THE ALPHABETS( BOTH LOWERCASE AND UPPERCASE) WITH THEIR RESPECTIVE
        # NUMBERS IN ASCENDING ORDER
        for words in string.ascii_uppercase:
            alphabets[words] = i  # stores the upper case letters in the dictionary
            i += 1
        for words in string.ascii_lowercase:
            alphabets[words] = j  # stores the lower case letters in the dictionary
            j += 1

        for i in range(len(self.message_text)):
            if self.message_text[i] in alphabets.keys():
                for a, b in alphabets.items():
                    if self.message_text[i] == a:
                        if a in string.ascii_lowercase and self.message_text[i] in string.ascii_lowercase:
                            if self.message_text[i] in VOWELS_LOWER and self.message_text[i] == 'a':
                                mapping_dict[self.message_text[i]] = m[0]
                            elif self.message_text[i] in VOWELS_LOWER and self.message_text[i] == 'e':
                                mapping_dict[self.message_text[i]] = m[1]
                            elif self.message_text[i] in VOWELS_LOWER and self.message_text[i] == 'i':
                                mapping_dict[self.message_text[i]] = m[2]
                            elif self.message_text[i] in VOWELS_LOWER and self.message_text[i] == 'o':
                                mapping_dict[self.message_text[i]] = m[3]
                            elif self.message_text[i] in VOWELS_LOWER and self.message_text[i] == 'u':
                                mapping_dict[self.message_text[i]] = m[4]
                            else:
                                mapping_dict[self.message_text[i]] = a
                        elif a in string.ascii_uppercase and self.message_text[i] in string.ascii_uppercase:
                            if self.message_text[i] in VOWELS_UPPER and self.message_text[i] == 'A':
                                mapping_dict[self.message_text[i]] = m[0]
                            elif self.message_text[i] in VOWELS_UPPER and self.message_text[i] == 'E':
                                mapping_dict[self.message_text[i]] = m[1]
                            elif self.message_text[i] in VOWELS_UPPER and self.message_text[i] == 'I':
                                mapping_dict[self.message_text[i]] = m[2]
                            elif self.message_text[i] in VOWELS_UPPER and self.message_text[i] == 'O':
                                mapping_dict[self.message_text[i]] = m[3]
                            elif self.message_text[i] in VOWELS_UPPER and self.message_text[i] == 'U':
                                mapping_dict[self.message_text[i]] = m[4]
                            else:
                                mapping_dict[self.message_text[i]] = a
            else:
                mapping_dict[self.message_text[i]] = self.message_text[i]
        return mapping_dict


    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary

        Returns: an encrypted version of the message text, based
        on the dictionary
        '''

        cipher = []
        encrypted = transpose_dict
        for i in range(len(self.message_text)):
            for a, b in encrypted.items():
                if self.message_text[i] == a:  # compares the letters in the dictionary and stores it in a list
                    # in a list
                    cipher.append(b)
        return ''.join(cipher)

        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)
        self.message_text = text
        self.valid_words = SubMessage.get_valid_words(self)
    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        decrypt_dict = {}
        permutation = get_permutations(VOWELS_LOWER)
        best_match = []
        for i in permutation:
            self.message_text = SubMessage.apply_transpose(self, SubMessage.build_transpose_dict(self, i))
            # print(self.message_text)
            matched_vowels = []
            for words in self.message_text:
                if words in VOWELS_LOWER:
                    # matches the vowel to its corresponding position in the VOWELS LOWER variable
                    if words == 'a':
                        matched_vowels.append(VOWELS_LOWER[0])
                    elif words == 'e':
                        matched_vowels.append(VOWELS_LOWER[1])
                    elif words == 'i':
                        matched_vowels.append(VOWELS_LOWER[2])
                    elif words == 'o':
                        matched_vowels.append(VOWELS_LOWER[3])
                    elif words == 'u':
                        matched_vowels.append(VOWELS_LOWER[4])
                    # matches the vowel to its corresponding position in the VOWELS LOWER variable
                elif words in VOWELS_UPPER:
                    if words == 'A':
                        matched_vowels.append(VOWELS_UPPER[0])
                    elif words == 'E':
                        matched_vowels.append(VOWELS_UPPER[1])
                    elif words == 'I':
                        matched_vowels.append(VOWELS_UPPER[2])
                    elif words == 'O':
                        matched_vowels.append(VOWELS_UPPER[3])
                    elif words == 'U':
                        matched_vowels.append(VOWELS_UPPER[4])
                else:
                    matched_vowels.append(words)
            # print('----------------------')
            # print(l)
            valid_words = []
            for j in ''.join(matched_vowels).split():
                if is_word(self.valid_words, j) is True:
                    valid_words.append(j)
            decrypt_dict[i] = ' '.join(valid_words)  # stores all the words and the permutation  in a dictionary
        # print(decrypt_dict)
        for a, b in decrypt_dict.items():
            best_match.append(len(b))  # stores the length of the words so as to determine the permutation
            # that produced many valid words
        for a, b in decrypt_dict.items():
            if len(b) == max(best_match):
                break  # breaks out of the loop immediately a match is found in case there are words of the same
                # length
        return b


if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
