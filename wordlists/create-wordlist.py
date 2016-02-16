import re

input_file1 = 'mit.10000.words.txt'
input_file2 = 'large.wordlist.txt'
output_file = open('final.wordlist.txt', 'w')

wordmap = dict()
wordCount = 0

def parseFile(filename):
    
    global wordCount
    f = open(filename, 'r')
    
    while 1:
        word = f.readline().rstrip().lower()
        
        if not word:
            print("End of '%s' found!" % filename)
            break
            
        if(word[len(word)-2:-1]) != "'":
            if len(word) == 9:
                if word in wordmap:
                    wordCount += 1
                else:
                    wordmap[word] = ""
                    output_file.write(word + "\n")
                    print("Written")
        #else:
            #print("Fucked")

parseFile(input_file1)
parseFile(input_file2)

print("\nWord Collisions", wordCount)
print("Wordlist Generation Complete!")
