# Word list generator - John Walsh - Version 2
# Used to process multiple words on one line in a file
# This script can process words separated by one white space

input_file1 = '9.letter.words.txt'
output_file = open('9.letter.words.final.txt', 'w')

wordmap = dict()

def parseFile(filename):
    
    f = open(filename, 'r')
    
    # Loop until end of file, force lowercase to output file
    for word in f.read().split():
        output_file.write(word.lower() + "\n")

# Files to be processed
parseFile(input_file1)

print("Wordlist Generation Complete!")
