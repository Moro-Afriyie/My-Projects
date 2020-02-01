# Problem Set 4B
# Name:  MORO OWUSU AFRIYIE
# Collaborators: no one
# Time Spent:

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    # >>> is_word(word_list, 'bat') returns
    True
    # >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'


class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
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
k        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        alphabets = {}  # dictionary of alphabets
        i = 1
        j = 1
        mapping_dict = {}
        # A DICTIONARY THAT HOLDS ALL THE ALPHABETS( BOTH LOWERCASE AND UPPERCASE) WITH THEIR RESPECTIVE
        # NUMBERS IN ASCENDING ORDER
        for words in string.ascii_uppercase:
            alphabets[words] = i  # stores the upper case letters in the dictionary
            i += 1
        for words in string.ascii_lowercase:
            alphabets[words] = j  # stores the lower case letters in the dictionary
            j += 1

        for i in range(len(self.message_text)):
            if self.message_text[i] in alphabets.keys():  # this takes care of the alphabets
                for a, b in alphabets.items():
                    if self.message_text[i] == a:
                        m = b + shift  # does the shifting
                        if m <= 26:
                            for c, d in alphabets.items():
                                if alphabets[c] == m:  # replace the old letter with the shifted value
                                    """
                                    This will treat uppercase and lowercase letters individually, so that uppercase letters
                                    are always mapped to an uppercase letter, and lowercase letters are always
                                    mapped to a lowercase letter and creates a dictionary mapping a letter (string) 
                                    to another letter (string).
                                    """
                                    if c in string.ascii_lowercase and self.message_text[i] in string.ascii_lowercase:
                                        mapping_dict[a] = c
                                    elif c in string.ascii_uppercase and self.message_text[i] in string.ascii_uppercase:
                                        mapping_dict[a] = c
                        elif m > 26:
                            m = m - 26
                            for c, d in alphabets.items():
                                if alphabets[c] == m:
                                    if c in string.ascii_lowercase and self.message_text[i] in string.ascii_lowercase:
                                        mapping_dict[a] = c
                                    elif c in string.ascii_uppercase and self.message_text[i] in string.ascii_uppercase:
                                        mapping_dict[a] = c
            else:  # this takes care of the spaces, commas and any special character
                mapping_dict[self.message_text[i]] = self.message_text[i]
        return mapping_dict  # Returns: a dictionary mapping a letter (string) to another letter (string).

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        cipher = []
        encrypted = Message.build_shift_dict(self, shift)
        for i in range(len(self.message_text)):
            for a, b in encrypted.items():
                if self.message_text[i] == a:  # compares the letters in the dictionary and stores the shifted value
                    # in a list
                    cipher.append(b)
        return ''.join(cipher)

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text) # calls the parent class constructor
        # since it inherits from the Message class it can access its attributes and functions
        self.shift = shift
        self.message_text = Message.get_message_text(self)
        self.encryption_dict = Message.build_shift_dict(self, self.shift)
        self.message_text_encrypted = Message.apply_shift(self, self.shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        PlaintextMessage(self.message_text, self.shift)
        self.encryption_dict = Message.build_shift_dict(self, self.shift)
        self.message_text_encrypted = Message.apply_shift(self, self.shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        self.message_text = text
        self.valid_words = Message.get_valid_words(self)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''

        best_shift = []
        decrypt_dict = {}
        for s in range(27):
            k = Message.apply_shift(self, 26 - s).split()  # gets rid of the spaces
            valid_words = []
            for i in k:
                if is_word(Message.get_valid_words(self), i) is True:
                    valid_words.append(i)
            decrypt_dict[26 - s] = ' '.join(valid_words)  # stores all the words and the shift value in a dictionary
        # print(decrypt_dict)
        for a, b in decrypt_dict.items():
            best_shift.append(len(b))  # stores the length of the words so as to determine the shift value
            # that produced many valid words
        for a, b in decrypt_dict.items():
            if len(b) == max(best_shift):
                break  # breaks out of the loop immediately a match is found in case there are words of the same
                # length
                # print('(', a, ',', b, ')')
        return a, b  # returns a tuple of the best shift and it's decrypted message


if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE

    #TODO: best shift value and unencrypted story

    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())