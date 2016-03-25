# Anagram Solver - John Walsh
# G00299626
# Version 1d

import random
import timeit

from itertools import permutations

wordlListFile = 'final.wordlist-2.txt'

vowelsList = list()
consonantsList = list()
wordmap = dict()
userOptions = False

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
    # Continue looping until end of file is encountered
    for word in f:
        word = word.rstrip()
        hash_key = ''.join(sorted(word))
        if hash_key in wordmap:
            wordmap.get(hash_key).append(word)
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
    print("\nMust be at least four consonants, three vowels & nine letters max!")
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

# Gets the longest anagram from the passed string of characters - Version 1
# Current implementation of this function is recursive, if a nine letter anagram is not found
# Also uses the more brute force approach of permutations to find all anagrams
# It's about 7 seconds worst case scenario
def get_anagram_1(conundrum, length):
    
    print("Looking for Anagram(s) of Length: %d" % length)
    
    # If length equals conundrum length then check conundrum against wordmap
    # Basically its checking if its the first time this function has been executed
    if(length > 8):
        anagramsList = check_dictionary(conundrum)
        # If not null / none then display best anagram(s)
        if(anagramsList is not None):
            print("\nAnagram(s): " + ', '.join(anagramsList) + "\n")
        else:
            # Start a recursive call to this function to check for anagrams of varying length
            # Continue to call until conundrum length is lower then four
            length -= 1
            get_anagram_1(conundrum, length)
    # Else, continue to look for anagram(s) of length lower then conundrum
    else:
        anagramsDict = dict()
        anagramsList = list()
        # Looping through the permutations & checking against dictionary
        # If ana anagram is found store it in a dict structure
        # This is currently the slowest part of the algorithm
        for perm in get_perms(conundrum):
            anagramsTempList = check_dictionary(perm[:length])
            if anagramsTempList is not None:
                anagram = ''.join(anagramsTempList)
                if(anagram not in anagramsDict):
                    anagramsDict[''.join(anagramsTempList)] = ""
                    
        # If anagramsDict contains anagrams then loop through them & add them to list to print
        if anagramsDict:
            for anagram, value in anagramsDict.items():
                anagramsList.append(anagram)
            print("\nAnagram(s): " + ', '.join(anagramsList) + "\n")
        else:
            # Keep looping through until length of four letters
            length -= 1
            if(length > 3):
                get_anagram_1(conundrum, length)
            else:
                print("\nAnagram(s): None Found!\n")
                
# Gets the longest anagram from the passed string of characters - Version 2
# Current implementation of this function will not find every anagram possible but is superior in speed compared to version 1
# It compares the modified ordering of the conundrum to the dictionary to find anagrams, similar to version 3
# It's about 0.1 to 2 seconds worst case scenario
def get_anagram_2(conundrum, length):
    
    anagramFound = False
    # Looping until an anagram is found or length is lower then four
    while(length > 3 and anagramFound == False):
        
        print("Looking for Anagram(s) of Length: %d" % length)
        
        # Looking for anagrams of length nine, theres no need to loop through and swap letters 
        # around to find nine letter anagrams because of the hashing 
        if(length > 8):
            anagrams = check_dictionary(conundrum)
            if anagrams is not None:
                print("\nAnagram(s): " + ', '.join(anagrams) + "\n")
                anagramFound = True
                break
        
        # Defining a list to store anagrams
        anagrams = list()
        
        # Loop through length of conundrum to switch up / swap characters to loop for anagrams
        # Loop break outs after anagram(s) have been found, faster then getting full permutations of conundrum
        for i in range(0, len(conundrum)):
            
            # Swaping two letter from the front to the back
            # Then checking the conundrum against the dictionary
            stringTemp = conundrum[i:len(conundrum)] + conundrum[0:i]
            anagramsA = check_dictionary(stringTemp[0:len(conundrum)][0:length])
            # Also checking the conundrum in reverse using the [::-1] string operation
            # Sometimes it yields better results, this is why I use both approaches
            anagramsB = check_dictionary((stringTemp[0:len(conundrum)][::-1][0:length]))
            
            # If both anagram(s) check lists are not null then append them to 'anagrams' list
            if anagramsA and anagramsB is not None:
                anagrams = anagramsA + list(set(anagramsB) - set(anagramsA))
                anagramFound = True
            elif anagramsA is not None:
                anagrams = anagramsA
                anagramFound = True
            elif anagramsB is not None:
                anagrams = anagramsB
                anagramFound = True
            
        # If anagrams were found then print & break loop
        if anagrams:
            print("\nAnagram(s): " + ', '.join(anagrams) + "\n")
            anagramFound = True
            break
        # Decrement conundrum length variable, loop again
        length -= 1
        # If no anagrams found then print & exit break while loop
        # Limited search of anagrams to four characters in length 
        if(length < 4):
            print("\nAnagram(s): None Found!\n")
            break

# Gets the longest anagram from the passed string of characters - Version 3
# Current implementation of this function is slightly better then verson 2, but will not find
# every anagram possible but its just as fast and I believe slightly more efficient
# Note: It's an implementation that deals in chance. Everytime your run it could display different results
# It's about 0.1 to 0.4 of a second worst case scenario
def get_anagram_3(conundrum, length):
    
    anagramFound = False
    # Looping until an anagram is found or length is lower then four
    while(length > 3 and anagramFound == False):
        
        print("Looking for Anagram(s) of Length: %d" % length)
        
        # Looking for anagrams of length nine, theres no need to loop through and swap letters 
        # around to find nine letter anagrams because of the hashing 
        if(length > 8):
            anagrams = check_dictionary(conundrum)
            if anagrams is not None:
                print("\nAnagram(s): " + ', '.join(anagrams) + "\n")
                anagramFound = True
                break
        
        # Defining a list to store anagrams
        anagrams = list()
            
        # Looping through 'X' amount of times to get anagrams from the dictionary
        # Note: Increase the loop count to get more hits, but this will increase the compute time
        for i in range(0, 750):
            # Randomly check against the dictionary by shuffling the letter in the conundrum
            # Limiting the length by using [0:length]
            anagramsCheck = check_dictionary(''.join(random.sample(conundrum,len(conundrum))[0:length]))
            # If not null then add the anagrams found to a global list variable 'anagrams'
            if anagramsCheck is not None:
                # Removing the duplicates from the list first, then combined both lists
                anagrams = anagrams + list(set(anagramsCheck) - set(anagrams))
            
        # If anagrams were found then print & break loop
        if anagrams:
            print("\nAnagram(s): " + ', '.join(anagrams) + "\n")
            anagramFound = True
            break
        # Decrement conundrum length variable, loop again
        length -= 1
        # If no anagrams found then print & exit break while loop
        # Limited search of anagrams to four characters in length
        if(length < 4):
            print("\nAnagram(s): None Found!\n")
            break

# Get perms of the conundrum & return list
def get_perms(conundrum):
    return [''.join(p) for p in permutations(conundrum)]
        
# Checks wordmap dictionary if word exists for conundrum
def check_dictionary(conundrum):
    return wordmap.get(''.join(sorted(conundrum)))

# Preprocess the dictionary & letter lists
def preprocess():
    print("\nPreprocessing...")
    build_dictionary(wordlListFile)
    build_letter_lists()

# Runs the application
def run_app():
    #preprocess()
    #conundrum = "decuionat"
    conundrum = "decuienag"
    #conundrum = "oaiesdttr"
    #conundrum = "abcdefghi"
    #conundrum = "infish"
    #conundrum = "iiiiiiiii"
    
    print("\nConundrum: " + conundrum + "\n")
    
    if(userOptions == True):
        while 1:
            conundrum = process_option(get_option())
            if(conundrum is not None):
                get_anagram_3(conundrum, len(conundrum))
    else:
        # You can swap the implementation of 'get_anagram_X' for either version 1, 2 and 3
        # 'get_anagram_1', 'get_anagram_2' and 'get_anagram_3'
        # Both implementations use the same hashmap / wordmap to check for anagrams
        get_anagram_3(conundrum, len(conundrum))


# Timing the algorithm
if(userOptions != True):
    from solver import run_app
    preprocess()
    print(timeit.timeit('run_app()', setup='from solver import run_app', number=1))
else:
    preprocess()
    run_app()
