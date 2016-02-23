# Word list generator - John Walsh - Version 2
# Used to process multiple words on one line in a file
# This script can process words separated by one white space

input_file1 = '9.letter.words.txt'
input_file2 = '8.letter.words.txt'
input_file3 = '7.letter.words.txt'
input_file4 = '6.letter.words.txt'
input_file5 = '5.letter.words.txt'
input_file6 = '4.letter.words.txt'

output_file = open('final.wordlist-2.txt', 'w')

wordmap = dict()

def parseFile(filename):
    
    f = open(filename, 'r')
    
    # Loop until end of file, force lowercase to output file
    for word in f.read().split():
        output_file.write(word.lower() + "\n")

# Files to be processed
parseFile(input_file1)
parseFile(input_file2)
parseFile(input_file3)
parseFile(input_file4)
parseFile(input_file5)
parseFile(input_file6)

print("Wordlist Generation Complete!")
