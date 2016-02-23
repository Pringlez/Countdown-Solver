# Anagram Solver - John Walsh
# G00299626
# Version 1a

import random
import timeit

word_list = 'final.wordlist-2.txt'

vowelsList = list()
consonantsList = list()
wordmap = dict()
userOptions = True

# Builds the vowels & consonants lists
def build_letter_lists():
    # Building vowels list
    for i in range(0, 5):
        vowelsList.append('u')
    for i in range(0, 13):
        vowelsList.append('i')
        vowelsList.append('o')
    for i in range(0, 15):
        vowelsList.append('a')
    for i in range(0, 21):
        vowelsList.append('e')
    
    # Building consonants list
    for i in range(0, 1):
        consonantsList.append('j')
        consonantsList.append('k')
        consonantsList.append('q')
        consonantsList.append('v')
        consonantsList.append('w')
        consonantsList.append('x')
        consonantsList.append('y')
        consonantsList.append('z')
    for i in range(0, 2):
        consonantsList.append('b')
        consonantsList.append('f')
        consonantsList.append('h')
    for i in range(0, 3):
        consonantsList.append('c')
        consonantsList.append('g')
    for i in range(0, 4):
        consonantsList.append('m')
        consonantsList.append('p')
    for i in range(0, 5):
        consonantsList.append('l')
    for i in range(0, 6):
        consonantsList.append('d')
    for i in range(0, 8):
        consonantsList.append('n')
    for i in range(0, 9):
        consonantsList.append('r')
        consonantsList.append('s')
        consonantsList.append('t')

# Builds the wordmap dictionary
def build_dictionary(filename):
    f = open(filename, 'r')
    
    # Continue looping until end of file is encountered
    for word in f:
        word = word.rstrip()
        word_hash = hash(''.join(sorted(word)))
        
        if not word:
            print("\nEnd of '%s' found!" % filename)
            break
            
        wordmap[hash(word_hash)] = word

# Prints the user's options
def print_options():
    print("\nCountdown Solver - Options\n")
    print("1: Generate Random Conundrum")
    print("2: Enter Nine Characters String")
    print("3: Exit")

# Get user's option
def get_option():
    print_options()
    return input('\nEnter Option: ')

# Get user's conundrum string of letters
def get_userstring():
    print("\nMust be at least 4 consonants and 3 vowels!")
    return input('Enter String: ')

# Processes the user's option
def process_option(option):
    # Exit program
    if(option == "3"):
        exit()
    else:
        # Generate a random conundrum
        if(option == "1"):
            randomListChars = list()
            for i in range(0, 4):
                randomListChars.append(random.choice(vowelsList))
            for i in range(0, 5):
                randomListChars.append(random.choice(consonantsList))
            return ''.join(randomListChars)
        # Else get a user's conundrum
        elif(option == "2"):
            return get_userstring()

# Gets the longest anagram in a string of characters
def get_anagram(conundrum):
    # Sorting the conundrum to search the wordmap
    conundrum = ''.join(sorted(conundrum))
    anagram = wordmap.get(hash(conundrum))
    # If not null / none then compare sorted anagram & conundrum
    if anagram is not None:
        if sorted(anagram) == sorted(conundrum):
            return anagram

def check_conundrum(conundrum):
    print("\nConundrum: " + conundrum)
    anagram = get_anagram(conundrum)
    if anagram is not None:
        print("Anagram: " + get_anagram(conundrum))
    else:
        print("No anagram found!")

# Runs the application
def run_app():
    conundrum = "decuionat"
    
    if(userOptions == True):
        while 1:
            build_letter_lists()
            conundrum = process_option(get_option())
            check_conundrum(conundrum)
    else:
        check_conundrum(conundrum)

# Preprocess the dictionary
build_dictionary(word_list)
        
# Timing the algorithm
if(userOptions != True):
    from solver import run_app
    print(timeit.timeit('run_app()', setup='from solver import run_app', number=1))
else:
    run_app()