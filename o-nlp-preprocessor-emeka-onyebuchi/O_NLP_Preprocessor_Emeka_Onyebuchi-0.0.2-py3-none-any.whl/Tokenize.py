import string
from nltk.tokenize import  word_tokenize

class Tokenize:

    def tokenize_document(self,document):
        text  = []
        print("*"*20)
        print("Tokenizing")
        print("*"*20)

        for line in document:
            line = line.translate(str.maketrans("","", string.punctuation)) #remove punctuation
            line = line.strip() #remove whitespace
            line =  word_tokenize(line) #tokenize
            text.append(line)

        return text
