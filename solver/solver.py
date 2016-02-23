# Anagram Solver - John Walsh

import random

vowelsList = list()
consonantsList = list()

def build_lists():
    # Building Vowels List
    for i in range(0, 5):
        vowelsList.append('u')
    for i in range(0, 13):
        vowelsList.append('i')
        vowelsList.append('o')
    for i in range(0, 15):
        vowelsList.append('a')
    for i in range(0, 21):
        vowelsList.append('e')
    
    # Building Consonants List
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

def print_options():
    print("\nCountdown Solver - Options\n")
    print("1: Generate Random Conundrum")
    print("2: Enter Nine Characters String")
    print("3: Exit")

# Get input from user
def get_option():
    print_options()
    return input('\nEnter Option: ')

# Get input from user
def get_userstring():
    print("\nMust be at least 4 consonants and 3 vowels!")
    return input('Enter String: ')

# Runs the application
def run_app():
    build_lists()
    option = get_option()
    if(option == "3"):
        exit()
    else:
        if(option == "1"):
            randomListChars = list()
            for i in range(0, 4):
                randomListChars.append(random.choice(vowelsList))
            for i in range(0, 5):
                randomListChars.append(random.choice(consonantsList))
            print("\nConundrum: " + ''.join(randomListChars))
        elif(option == "2"):
            user_input = get_userstring()
            print("\nUser Input: " + user_input)
            
# Timing the algorithm
if __name__ == '__main__':
    import timeit
    print(timeit.timeit("run_app()", setup="from __main__ import run_app"))