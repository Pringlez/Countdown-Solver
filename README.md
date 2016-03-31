# John Walsh
## G00299626

## Countdown Letters Game Solver
### Goal
The game countdown requires a word of nine random letters which must contain at least three vowels and four consonants.
The countdown solver must find the longest possible word from a dictionary file loaded into the program. It must be an anagram of some or all of the letters in the generated word.
### Background
A number of countdown solvers already exist on the internet. To be filled later...

## Words Lists
I've compiled a two different word lists from different sites and web applications. 

#### Version 1
Version 1 of the word list has been compiled from a number different sources, MIT, kali linux and the nine letter word list from 'www.bestwordlist.com'. I've also included the script written to combine these word lists.

#### Version 2
Version 2 of the word list is entirely made up of word lists from the site 'www.bestwordlist.com', every word of length four to nine letter long. I've included the script used to compile these word lists together.

#### References
Here is the most up-to date references to these word lists.
* The following word lists are used by spell checkers and other programs, seems to contain quite extensive lists. May not be the best as some words are names of cities, towns and other locations. The link to the resource [here.](http://wordlist.aspell.net/dicts)
* Another site that contains lists of words with their frequencies, mainly for use in spell checker programs. The link to the resource [here.](http://www.kilgarriff.co.uk/bnc-readme.html)
* The following site features the ability to filter the length of words wanted, very useful site. The link is [here.](http://www.bestwordlist.com/)

## Python Script
The solver script located in the 'solver' directory. The script is quite basic really, it uses the hash function to map words to a directory structure. This allows the particular conundrum to be checked against the word map in quick succession.

Maybe an interesting section to review. A recursive function that allows the script to check for anagrams from nine to four letter words. It still needs to be modified significantly to check for every single anagram in the conundrum.
```python
    def get_anagram(conundrum, length):
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
```

Previously this function looked like this:
```python
    def get_anagram(conundrum):
        # Sorting the conundrum & hashing key to search the wordmap
        print("\nConundrum: " + conundrum)
        conundrum = ''.join(sorted(conundrum))
        anagram_list = wordmap.get(hash(conundrum))
        # If not null / none then display best anagram(s)
        if anagram_list is not None:
            print("Anagram(s): " + ', '.join(anagram_list))
        else:
            print("Anagram(s): None")
```
That didn't check for anagrams lower than nine letter, this is why I changed it.

The latest python 'get_anagram' function as of 2/3/2016. The function has developed considerably over the last couple of days. The function know attempts look for all anagrams lower than the length of the conundrum. The function can be further optimized I believe. Its current time complexity with worst case scenario conundrum, will run in about seven seconds. I'm unsure of the space complexity.

> Note: The function name 'get_anagram' has been changed to 'get_anagram_1' as of 11/3/2016, version 1c of the script.

```python
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
```
I've added another implementation to search for anagrams called 'get_anagram_2' which doesn't use the brute force approach of using permutations to find every anagram in the conundrum like in first version 'get_anagram_1'.

This version basically swaps letters from the beginning to the end of the string when searching for anagrams lower than nine characters. It also reverses the string and checks the dictionary for any anagrams. Because the words are hashed then compared to the dictionary wordmap, the script fairly quick in searching for anagrams.
```python
    def get_anagram_2(conundrum, length):
    
        anagramFound = False

        while(length > 3 and anagramFound == False):

            print("Looking for Anagram(s) of Length: %d" % length)

            # Looking for anagrams of length nine, much faster to check for them here than going into for loop below
            if(length > 8):
                anagramsList = check_dictionary(conundrum)
                length -= 1
                if anagramsList is not None:
                    print("\nAnagram(s): " + ', '.join(anagramsList) + "\n")
                    anagramFound = True
                    break

            # Loop through length of conundrum to switch up / swap characters to loop for anagrams
            # Loop break outs after anagram(s) have been found, faster then getting full permutations of conundrum
            for i in range(0, len(conundrum)):

                # Swaping two letter from the front to the back
                # Then checking the conundrum against the dictionary
                anagramTemp = conundrum[i:len(conundrum)] + conundrum[0:i]
                anagramsCheckListA = check_dictionary(anagramTemp[0:len(conundrum)][0:length])
                # Also checking the conundrum in reverse using the [::-1] string operation
                # Sometimes it yields better results, this is why I use both approaches
                anagramsCheckListB = check_dictionary((anagramTemp[0:len(conundrum)][::-1][0:length]))

                # If both anagram(s) check lists are not null then append them to 'anagrams' list
                if anagramsCheckListA and anagramsCheckListB is not None:
                    anagrams = ', '.join(anagramsCheckListA)
                    # Checking if anagram is already in list
                    for anagram in anagramsCheckListB:
                        # If not already in list append anagram
                        if(anagram not in anagrams):
                            anagrams.append(anagram)
                    anagramFound = True
                    break
                elif anagramsCheckListA is not None:
                    # If the returned 'anagramsCheckListA' list wasn't null then add any anagram(s) to 'anagrams' list
                    anagrams = ', '.join(anagramsCheckListA)
                    # Breaking out of the loop
                    anagramFound = True
                    break
                elif anagramsCheckListB is not None:
                    # If the returned 'anagramsCheckListB' list wasn't null then add any anagram(s) to 'anagrams' list
                    anagrams = ', '.join(anagramsCheckListB)
                    # Breaking out of the loop
                    anagramFound = True
                    break
            # If anagrams were found then print & break loop
            if(anagramFound):
                print("\nAnagram(s): " + anagrams + "\n")
                break
            # Decrement conundrum length variable, loop again
            length -= 1
            # If no anagrams found then print & exit break while loop
            # Limited search of anagrams to four characters in length 
            if(length < 4):
                print("\nAnagram(s): None Found!\n")
                break
```
This version of the solver function basically loops and shuffles the letters into a mix that’s then checked against the dictionary.
Surprisingly this performs the best from the other version of the solver function, there really isn't any need to loop more than 1000 times to find most anagrams from the conundrum.
```python
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
```

## Preprocessing
The solver script performs some preprocessing initially to build the lists for the random conundrum generator. The letter frequencies of the lists of vowels and consonants were taken from [here.](http://www.thecountdownpage.com/letters.htm)

The function 'preprocess' handles the dictionary & lists generation. You can move the function call to the timing 'run_app' function to see how long it takes to build.
```python
    def preprocess():
        print("\nPreprocessing...")
        build_dictionary(word_list)
        build_letter_lists()
```

## Efficiency
The solver script has a number of different approaches to improve the overall speed of the algorithm. It first takes a random conundrum and sorts the letters which is then passed into a hashing function that will compute a key integer. The key is then passed into the wordmap to be checked against the stored hash keys. Normally words conflict when this hash table is generated, to counteract this words are place on lists much like how conflictions in a [HashMap](https://docs.oracle.com/javase/8/docs/api/java/util/HashMap.html) are handled in the programming language Java.

The word hashing approach is fairly quick, version 3 of the 'get_anagram_X' function performs relatively well in run time speed. It currently computes the result at about 0.2 of a second, version 1 sits at about 2 to 7 seconds in runtime.

There are number of problems that still exist in the solver script:
* Anagrams of length eight or lower are not generated efficiently enough I believe in certain instances
* The pre-processing required takes longer than expected, at about 1.5 seconds
* Hashing words to the dictionary can be quite slow, needs to be cleaned up

## Results
The different versions of the solver function 'get_anagram_X', version 1, 2 and 3. Their weaknesses and strengths listed below:

#### Version 1
* Current implementation of this function is recursive, if a nine letter anagram is not found
* Also uses the more brute force approach of permutations to find all anagrams
* It's about 7 seconds worst case scenario

#### Version 2
* Current implementation of this function will not find every anagram possible but is superior in speed compared to version 1
* It compares the modified ordering of the conundrum to the dictionary to find anagrams, similar to version 3
* It's about 0.1 to 2 seconds worst case scenario

#### Version 3
* Current implementation of this function is slightly better than version 2, but will not find every anagram possible but it’s just as fast and I believe slightly more efficient
* Note: It's an implementation that deals in chance. Every time your run it could display different results
* It's about 0.1 to 0.4 of a second worst case scenario

I've found that version 3 of the solver function performs the best in terms of performance, it finds most of the anagrams in split seconds compared to 2 to 7 seconds in version 1. Version 2 implementation still needs work to perform as good as version 2 I believe, it still finds anagrams but will not currently find as many as version 2 of the solver function.

## References
Below are references to algorithms, word lists and other research sources found online:

* The following link [here](http://stackoverflow.com/questions/8286554/find-anagrams-for-a-list-of-words) contains useful information when I first starting search for ideas on how to approach this countdown conundrum problem.
* Another blog site I found interesting was Jeremy Boyd blog found [here.](http://www.jeremy-boyd.com/2010/10/18/compute-all-permutations-of-a-string-in-python/) There were two solutions to the permutations problem, one had a duplicates issue the other had not any such issues. Both worked fairly well. I'm currently using a slightly modified version of his solutions.
* The site [here](http://www.tutorialspoint.com/python/) contains some great resources and tips about using python. I found it extremely helpful.
* This post in Stackoverflow [here](http://stackoverflow.com/questions/931092/reverse-a-string-in-python) was quite useful in reversing a string.
* Another helpful resource on anagrams searching [here](http://python-for-analysts.pythonblogs.com/211_python-for-analysts/archive/1258_python_for_newbies_a_simple_anagram_finder.html)
