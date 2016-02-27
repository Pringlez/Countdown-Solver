# John Walsh
## G00299626

## Countdown Letters Game Solver
### Goal
The game countdown requires a word of nine random letters which must contain at least three vowels and four consonants.
The countdown solver must find the longest possible word from a dictionary file loaded into the program. It must be an anagram of some or all of the letters in the generated word.
### Background
A number of countdown solvers already exist on the internet. To be filled later...

## Words Lists
I've compiled a number of different word lists from different sites and web applications. Here is the most up-to date references to these word lists.

* The following word lists are used by spell checkers and other programs, seems to contain quite extensive lists. May not be the best as some words are names of cities, towns and other locations. The link to the resource [here.](http://wordlist.aspell.net/dicts)
* Another site that contains lists of words with their frequencies, mainly for use in spell checker programs. The link to the resource [here.](http://www.kilgarriff.co.uk/bnc-readme.html)

## Python Script
The solver script located in the 'solver' directory. The script is quite basic really, it uses the hash function to map words to a directory structure. This allows the the particular conundrum to be checked against the word map in quick succession.

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
That didn't check for anagrams lower then nine letter, this is why I changed it.

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
Here's some stuff about how efficient my code is, including an analysis of how many calculations my algorithm requires.

## Results
My script runs very quickly, and certainly within the 30 seconds allowed in the countdown letters game.

## References
Below are references to algorithms, word lists and other research sources found online.

* The following link [here](http://stackoverflow.com/questions/8286554/find-anagrams-for-a-list-of-words) contains usful information when I first starting search for ideas on how to approach this countdown conundrum problem.
