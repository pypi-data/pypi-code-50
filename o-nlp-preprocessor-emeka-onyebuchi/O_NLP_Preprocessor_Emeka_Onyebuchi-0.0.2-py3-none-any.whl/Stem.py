from nltk.stem import PorterStemmer 

class Stem:
    def stem_word(self,filtered_text):
        ##stem
        stemmed_text = []

        print("*"*20)
        print("Stemming Word")
        print("*"*20)

        stemmer = PorterStemmer()
        for line in filtered_text:
            stemmed_line = []
            for word in line:
                stemmed_word = stemmer.stem(word)
                stemmed_line.append(stemmed_word)
            stemmed_text.append(stemmed_line)
        
        return stemmed_text