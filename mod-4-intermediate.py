'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    while True:
        def shift_letter(letter, shift):

            ciper = ''
            for string in letter:

                if string == '':
                    ciper = ciper
                    
                        
                elif string.isupper():
                    ciper = ciper+chr((ord(letter)+shift-65)%26+65)
                    
                elif len(text)>1:
                    print('Invalid please enter one letter only')
                    ciper = 'N/A'

                elif string.islower():
                    print('Invalid please enter a capital letter')
                    ciper = 'N/A'

                else:
                    print('error')
                    ciper = 'Invalid please enter one capital letter only'
                

            return ciper

        text = input('enter your letter: ')
        shift = int(input('enter the shift: '))
        print('\n'+shift_letter(text, shift)+'\n') 

def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    while True:
        def caesar_shift(message, shift):
            ciper = ''
            for string in message:
                if string == '':
                    ciper = ciper

                elif string.isupper():
                    ciper = ciper+chr((ord(string)+shift-65)%26+65)

                elif string.islower():
                    ciper = ciper+chr((ord(string)+shift-97)%26+97)

                else:
                    ciper = 'please enter letters only'

            return ciper      

        text = input("enter your message: ")
        shift = input('enter your shift key letter: ')
        print('\n'+caesar_shift(text, shift)+'\n')
    
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

def shift_by_letter(letter, letter_shift):

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    while True:
        def vigenere_cypher(letter, letter_shift):
            ciper = ''
            for string in letter:
                if string == '':
                    ciper = ciper

                elif letter_shift == 30:
                    ciper = 'Invalid please enter letters only'

                elif letter_shift == 31:
                    ciper = 'Invalid please enter one letter only'

                elif letter_shift == 32:
                    ciper = 'Invalid please use capital letters only'
                    
                elif string.isupper():
                    ciper = ciper+chr((ord(string)+letter_shift-65)%26+65)

                elif string.islower():
                    ciper = 'Invalid please use capital letters only'

                else:
                    ciper = 'Invalid please enter one letter only'

            return ciper      

            
        text = input("enter a letter: ")
        letter_shift = input('enter your shift key letter: ')

        if len(letter_shift)>1:
            letter_shift = 31
        elif letter_shift.islower():
            letter_shift = 32
        elif letter_shift.isupper():
            letter_shift = (ord(letter_shift)-65)
        elif letter_shift == '':
            letter_shift = ''
        else:
            letter_shift = 30

        print('\n'+vigenere_cypher(text, letter_shift)'\n')

def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def vigenere_cipher(message, key):
        encrypted_text = ""
        key_length = len(key)
        
        for i, char in enumerate(message):
            if char.isalpha():
                
                key_char = key[i % key_length]
                key_shift = ord(key_char.upper()) - ord('A')

                if char.isupper():
                    shifted_char = chr(((ord(char) - ord('A') + key_shift) % 26) + ord('A'))
                else:
                    shifted_char = chr(((ord(char) - ord('a') + key_shift) % 26) + ord('a'))
                
                encrypted_text += shifted_char
            else:
                encrypted_text += char

        return encrypted_text


    message = input('Enter your text: ')
    key = input('Enter your shift key: ')

    encrypted_text = vigenere_cipher(message, key)
    print("Encrypted text:", encrypted_text)