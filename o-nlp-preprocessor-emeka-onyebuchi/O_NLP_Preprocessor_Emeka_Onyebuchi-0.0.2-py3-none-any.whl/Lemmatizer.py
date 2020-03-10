from nltk.stem import WordNetLemmatizer

class Lemmatizer:

    def lemm_text(self,stemmed_text):
        # #lemmatizing
        lemm_text = []

        print("*"*20)
        print("Lemmatizing Word")
        print("*"*20)

        lemmatizer = WordNetLemmatizer()

        for line in stemmed_text:
            lemm_line = []
            for word in line:
                lemm_word = lemmatizer.lemmatize(word)
                lemm_line.append(lemm_word)
            lemm_text.append(lemm_line)
        # print(lemm_text)
        return lemm_text