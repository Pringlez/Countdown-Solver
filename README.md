# John Walsh
## G00299626

## Countdown Letters Game Solver
### Goal
The game countdown requires a word of nine random letters which must contain at least three vowels and four consonants.
The countdown solver must find the longest possible word from a dictionary file loaded into the program. It must be an anagram of some or all of the letters in the generated word.
### Background
A number of countdown solvers already exist on the internet. Naming just a few sites like
The first task I completed as part of this project was to Google "countdown letters game solver".
Google gave me two relevant results on the first page, these are [Cool Project name][2] and [Cool Solver][3].

## Words Lists
* The following word lists are used by spell checkers and other programs, seems to contain quite extensive lists. May not be the best as some words are names of cities, towns and other locations. The link to resource is [here.](http://wordlist.aspell.net/dicts)
* Links and lists of words with frequencies, mainly for use in spell checker programs. The link to resource is [here.](http://www.kilgarriff.co.uk/bnc-readme.html)

## Python Scripts
My script is in the files [solver.py](solver.py) in this repository and it works as follows.
The most important section is:

```python
import random
print(random.shuffle("My code is cool."))
```

Previously it looks like this:
```python
# Note that the following snippet of code was adapted from
# the Stack Overflow post available here: http://www.so.com/post/123
import nothing
```
That didn't work too well, so I changed it.

## Preprocessing
My script does a lot of preprocessing, which only needs to be run once.
Once the preprocessing is done we can run the game solver again and again without that overhead.

## Efficiency
Here's some stuff about how efficient my code is, including an analysis of how many calculations my algorithm requires.

## Results
My script runs very quickly, and certainly within the 30 seconds allowed in the Coutdown letters game.

## References
Below are references to algorithms, word lists and other research sources found online.
