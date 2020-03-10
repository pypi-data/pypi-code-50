import os
import re
import json
import emoji

# ideia poder passar frase ou frases
# ser extremamente performático
# adicionar acento na palavra
# fazer os regex das palavras
# tokenizar as palavras

class SentenceTokenizer:
    
    def __init__(self):
        self.LAUGH_REGEX = re.compile(r'^((kk+)|(haha(ha)*h?)+|(rs(rs)*r?)|(hehe(he)*h?)|(hihi(hi)*h?))$')
        self.DATE_REGEX = re.compile(r'^(\d{1,2}[-//]\d{1,2})([-//]\d{2,4})?$')
        self.TIME_REGEX = re.compile(r'^\d{1,2}(:|h(rs)?)(\d{1,2}(min)?)?$')
        self.DDD_REGEX = re.compile(r'^(\(0?\d{2}\))$')
        self.MEASURE_REGEX = re.compile(r'^\d+[a-z]{1,2}$')
        self.CODE_REGEX = re.compile(r'^((\d[a-z])|([a-z]\d))\w*$') 
        self.PHONE_REGEX = re.compile(r'^(\(0?\d{2}\))?\d{4,5}-?\d{4}$')
        self.CNPJ_REGEX = re.compile(r'^\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}$') 
        self.CPF_REGEX = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$') 
        self.EMAIL_REGEX = re.compile(r'^\S+@[^\s]+$')
        self.MONEY_REGEX = re.compile(r'^((rR]?[S$])|([rR][S$]?))\d+([\.,]\d+)*$')
        self.URL_REGEX = re.compile(r'^(https?://)|(www\.)[^\s]+$')
        self.NUMBER_REGEX =  re.compile(r'^[-+]?\d+([\.,-]\d+)*$')
        self.SIMPLE_NUMBER_REGEX = re.compile(r'^\d+-*\d*$')
        self.ORDINAL_NUMBER_REGEX = re.compile(r'^\d+[ºª]$')
        self.PUNCTUATION_REGEX = re.compile(r"[^.?!,.;:\s]+|[?!,.;:]")
        self.FIRST_PUNCTUATION_REGEX = re.compile(r'[!,.;?]\s')
        self.EMOJI_REGEX = re.compile('['
                                  u'\U0001f600-\U0001f64f'  # emoticons
                                  u'\U0001f300-\U0001f5ff'  # symbols & pictographs
                                  u'\U0001f680-\U0001f6ff'  # transport & map symbols
                                  u'\U0001f1e0-\U0001f1ff'  # flags (iOS)
                                                     ']+', flags=re.UNICODE)
        self.__set_word_vocab_dicts()
    
    def __set_word_vocab_dicts(self):
        dir_path = os.path.dirname(__file__)
        full_path_correction = os.path.join(dir_path, 'dictionaries', 'correction_dict.json')
        full_path_accentuation = os.path.join(dir_path, 'dictionaries', 'Titan_v2_dict_without_accentuation.json')
        full_path_pt_words = os.path.join(dir_path, 'dictionaries', 'all_portuguese_words.txt')
        self.__correction_dict = self.__read_json(full_path_correction)
        self.__dict_without_accentuation = self.__read_json(full_path_accentuation)
        self.__set_pt_words = set(self.__read_txt_file(full_path_pt_words))
        
    def process_message(self, message: str):
        message_lst = message.split()
        message_lst = self.to_lowercase(message_lst)
        message_lst = self.add_space_punctuation(message_lst)
        message_lst = self.replace_words_in_sentence(message_lst)
        message_lst = self.replace_words_with_dicts(message_lst)
        message = self.remove_symbol(' '.join(message_lst))
        message = self.normalize_message(message)
        return message
        
    def __read_txt_file(self, txt_path: str):
        with open(txt_path, 'rb') as f:
            lines = [line.rstrip().decode('utf-8') for line in f]
            return lines
        
    def __read_json(self, dict_path: str):
        with open(dict_path, encoding='utf-8') as handle:
            return json.loads(handle.read())

    def replace_words_with_dicts(self, message_lst: list):
        for ind, word in enumerate(message_lst):
            if (word in self.__dict_without_accentuation and word not in self.__set_pt_words):
                message_lst[ind] = self.__dict_without_accentuation[word]
            else:
                if word in self.correction_dict:
                    message_lst[ind] = self.correction_dict[word]
        return message_lst
    
    def to_lowercase(self, message_lst: list):
        processed_message_lst = [message_lst[0].lower()]
        if len(message_lst) != 1:
            processed_message_lst += message_lst[1:]
        return processed_message_lst
    
    def add_space_punctuation(self, message_lst: list):
        return [word[:-1] + ' ' + word[-1] if word[-1] in {'!', ',', '.', ';', '?'} else word for word in message_lst] 
    
    def replace_words_in_sentence(self, message_lst: list):
        return [self.__replace_symbol(self.__tag_word(word)) for word in message_lst]
    
    def normalize_message(self, message: str):
        message = re.findall(self.PUNCTUATION_REGEX, message)
        return ' '.join(message)
    
    def remove_symbol(self, message: str):
        return message.translate(str.maketrans('', '', '(){}[]$/\@|_*^~+"/%'))
    
    def remove_whatsapp_emoji(self, message: str):
        new_message = [word for word in message if word not in emoji.EMOJI_UNICODE.values()]
        return ' '.join(new_message)
    
    def __tag_word(self, word: str):
        word = self.LAUGH_REGEX.sub('LAUGH', word)
        word = self.EMOJI_REGEX.sub('', word)
        word = self.DATE_REGEX.sub('DATE', word)
        word = self.TIME_REGEX.sub('TIME', word)
        word = self.DDD_REGEX.sub('DDD', word)
        word = self.PHONE_REGEX.sub('PHONE', word)
        word = self.CNPJ_REGEX.sub('CNPJ', word)
        word = self.CPF_REGEX.sub('CPF', word)
        word = self.EMAIL_REGEX.sub('EMAIL', word)
        word = self.MONEY_REGEX.sub('MONEY', word)
        word = self.URL_REGEX.sub('URL', word)
        word = self.MEASURE_REGEX.sub('MEASURE', word)
        word = self.ORDINAL_NUMBER_REGEX.sub('NUMBER', word)
        word = self.SIMPLE_NUMBER_REGEX.sub('NUMBER', word)
        word = self.NUMBER_REGEX.sub('NUMBER', word)
        word = self.CODE_REGEX.sub('CODE', word)
        return word
    
    def __replace_symbol(self, word: str):
        word = word.replace(';', ',')
        word = word.replace('=', 'igual')
        word = word.replace('&', 'e')
        return word