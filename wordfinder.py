"""Word Finder: finds random words from a dictionary."""

from random import choice

class WordFinder:
    """ the class will find random words from a dictionary
    first it will read the file word.txt, 
    next find random text in it 
    """
    
    def __init__(self,my_file):
        fle = open(f"{my_file}", "r")
        lines =  (line.rstrip() for line in fle) 
        self.line = list(line for line in lines if line)
        
    def __repr__(self):
        return f"WordFinder takes a file {self.my_file} as input and return random word in it"
    def findWord(self):
        return [choice(self.line)]
       

l = "words.txt"
m = WordFinder(l)

print(m.findWord())
print(m.findWord())
    
