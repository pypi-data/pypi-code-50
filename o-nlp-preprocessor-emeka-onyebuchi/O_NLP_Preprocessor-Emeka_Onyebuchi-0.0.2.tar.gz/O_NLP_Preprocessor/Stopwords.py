from nltk.corpus import stopwords



stop_words = set(stopwords.words('english'))


class Stopwords:
    
    def remove_stopwords(self,text):
        filtered_text = []
        print("*"*20)
        print("Removing Stopwords")
        print("*"*20)
        for line in text:
            #print(line)
            filtered_line = []
            for word in line:
                #print(word)
                
                if word not in stop_words:
                    filtered_line.append(word)
            filtered_text.append(filtered_line)
        return filtered_text
