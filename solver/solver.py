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
    vowelsList.clear()
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
    consonantsList.clear()
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
    counter = 0
    # Continue looping until end of file is encountered
    for word in f:
        word = word.rstrip()
        hash_key = hash(''.join(sorted(word)))
        if hash_key in wordmap:
            wordmap.get(hash_key).append(word)
            counter += 1
        else:
            wordmap.update({hash_key:[word]})
        
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
    print("\nMust be at least four consonants, three vowels & nine letters max")
    return input('Enter String: ')

# Create a random conundrum, depending on random number generated 
def create_conundrum():
    # Generating a random number & calling function to generate conundrum
    randomNumber = random.randint(0,2)
    if(randomNumber is 0):
        conundrum = generate_conundrum(3, 6)
    elif(randomNumber is 1):
        conundrum = generate_conundrum(4, 5)
    else:
        conundrum = generate_conundrum(5, 4)
    return ''.join(conundrum)

# Function used to pick a random amount of vowels & consonants
def generate_conundrum(vowelAmount, consonantAmount):
    # Store characters in a list & return list
    randomListChars = list()
    for i in range(0, vowelAmount):
        random.shuffle(vowelsList)
        randomListChars.append(vowelsList.pop())
    for i in range(0, consonantAmount):
        random.shuffle(consonantsList)
        randomListChars.append(consonantsList.pop())
    # Rebuild the lists after conundrum generation
    build_letter_lists()
    return randomListChars
    
# Process the user's option
def process_option(option):
    # Exit program
    if(option == "3"):
        exit()
    else:
        # Generate a random conundrum
        if(option == "1"):
            return create_conundrum()
        # Else get a user's conundrum
        elif(option == "2"):
            return get_userstring()
        else:
            print("\nPlease enter a valid option!")

# Gets the longest anagram in a string of characters
def get_best_anagram(conundrum, length):
    # Sorting the conundrum & hashing key to search the wordmap
    anagram_list = check_dictionary(conundrum)
    # If not null / none then display best anagram(s)
    if anagram_list is not None:
        print("Anagram(s): " + ', '.join(anagram_list))
    else:
        # Recursively call this function to check for anagrams of varying length
        # Continue to call until conundrum length is lower then four
        if(len(conundrum) > 3):
            length -= 1
            get_best_anagram(conundrum[:length], length)
        else:
            print("Anagram(s): None Found!")
        
# Checks wordmap dictionary if word exists for conundrum
def check_dictionary(conundrum):
    conundrum = ''.join(sorted(conundrum))
    return wordmap.get(hash(conundrum))

# Preprocess the dictionary & letter lists
def preprocess():
    print("\nPreprocessing...")
    build_dictionary(word_list)
    build_letter_lists()

# Runs the application
def run_app():
    #conundrum = "decuionat"
    #conundrum = "decuienag"
    conundrum = "infish"
    
    if(userOptions == True):
        while 1:
            conundrum = process_option(get_option())
            print("\nConundrum: " + conundrum)
            if(conundrum is not None):
                get_best_anagram(conundrum, len(conundrum))
    else:
        print("\nConundrum: " + conundrum)
        get_best_anagram(conundrum, len(conundrum))

# Timing the algorithm
if(userOptions != True):
    from solver import run_app
    preprocess()
    print(timeit.timeit('run_app()', setup='from solver import run_app', number=1))
else:
    preprocess()
    run_app()
