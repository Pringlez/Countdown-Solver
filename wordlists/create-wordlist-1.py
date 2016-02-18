# Word list generator - John Walsh - Version 1
# Used to create one single large wordlist by combining other smaller wordlists
# This script can process words separated by a new line character

input_file1 = 'mit.10000.words.txt'
input_file2 = 'large.wordlist.txt'
input_file3 = '9.letter.words.final.txt'
output_file = open('final.wordlist-1.txt', 'w')

wordmap = dict()
wordCount = 0

def parseFile(filename):
    
    # Global var to count word collisions when storing words in wordmap variable
    global wordCount
    f = open(filename, 'r')
    
    # Continue looping until end of file is encountered
    while 1:
        word = f.readline().rstrip().lower()
        
        # If word is null or empty then break out of loop
        if not word:
            print("End of '%s' found!" % filename)
            break
        
        # Checking if word contains punctuation character
        if(word[len(word)-2:-1]) != "'":
            # If word length 9 then continue
            if len(word) == 9:
                # If word is already in map ignore word and increment count
                if word in wordmap:
                    wordCount += 1
                else:
                    # Storing word in map, value is empty
                    wordmap[word] = ""
                    output_file.write(word + "\n")

# Files to be processed
parseFile(input_file1)
parseFile(input_file2)
parseFile(input_file3)

# Final print out
print("\nWord Collisions", wordCount)
print("Wordlist Generation Complete!")
