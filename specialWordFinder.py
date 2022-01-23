from wordfinder import WordFinder
from random import choice
class SpecialWordFinder(WordFinder):
    """this class import the WordFinder
    to find a random word in the file
    by ignoring the comments or space
    """
    def __init__(self,my_file):
        super().__init__(my_file)
    def findWords(self):
        l = choice(self.line)
        #if not choice(self.line).startswith("#"):
        if not l.startswith("#"): return l

        #return [not choice(self.line).startswith("#")]  
      
m = "file.txt"
x = SpecialWordFinder(m)

print(x.findWords())
