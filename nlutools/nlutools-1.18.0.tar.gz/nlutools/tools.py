import os
import subprocess

from nlutools.config import mapConf, supportConf, bertModelConf
from nlutools.online_bert_client import bert_vector
from nlutools.rpc_client import doTask, doCustomTask, doNameEntity
from nlutools.utils import raiseException


# Segment
def cut(sentence, pos=True, cut_all=False, mode='fast', words=[], user=""):
    serverName = 'segmentor'
    try:
        # if mode == "del":
        #     if not user:
        #         return "Please assign a value to the variable `user`"
        #     data = {"del": True, "user": user}
        #     res = doTask(serverName, data)
        #     return res
        # elif mode == "add":
        #     if not words:
        #         return "Please assign a list of words to the variable `words`"
        #     if not user:
        #         return "Please assign a value to the variable `user`"
        #     data = {"add": True, "user": user, "words": words}
        #     res = doTask(serverName, data)
        #     check_data = {"check_add": True, "user": user, "words": words}
        #     return res
        if mode in ['fast', 'accurate']:
            if isinstance(pos, bool) and isinstance(cut_all, bool):
                if sentence == "":
                    res = {"text":"", "items":[], "pos":[], "np":[], "entity":[]}
                else:
                    data = {'text':sentence, 'mode':mode, 'pos':pos, 'cut_all':cut_all}
                    res = doTask(serverName, data)
                return res
            else:
                return "Please assign boolean value for variables `pos` and `cut_all`"
        else:
            raiseException('Advise: check parameters, make sure value of mode is fast or default, value of pos is true, false or default as well')
    except Exception as e:
        raiseException('%s exception \nplease contact supporter %s for this exception ! \n%s' % (serverName, supportConf[serverName], e))

# w2v file
def getW2VFile(version_key, localpath):
    try:
        if not version_key or not version_key.strip():
            cat = subprocess.Popen(['hadoop', 'fs', '-cat', mapConf['w2v_hdfs_version_file']], stdout=subprocess.PIPE)
            for line in cat.stdout:
                version_key = bytes.decode(line).strip()
                break
        if version_key and version_key.strip():
            try:
                subprocess.call(['hadoop','fs','-get', mapConf['w2v_hdfs_dir'] + version_key.lower(), localpath])
            except Exception as e:
                raiseException('%s exception \nplease contact supporter %s for this exception ! \n%s' % ('w2v', supportConf['w2v'], e))
    except Exception as e:
        raise Exception('Advise: please install hadoop client before use getW2VFile')

# word similarity
def getSimScore(word1, word2, type_='ifchange'):
    try:
        data = {'type':type_, 'word1':word1, 'word2':word2}
        serverName = 'w2v'
        return float(doTask(serverName, data))
    except Exception as e:
        raiseException('%s exception \nplease contact supporter %s for this exception ! \n%s' % (serverName, supportConf[serverName], e))
# alias
def sim_score(word1, word2, type='ifchange'):
    return getSimScore(word1, word2, type)

# word vector
def getWordVec(word, type_='ifchange'):
    try:
        if isinstance(word, str):
            word = [word]
        data = {'words':word, 'type':type_}
        serverName = 'w2v'
        return doTask(serverName, data)
    except Exception as e:
        raiseException('%s exception \nplease contact supporter %s for this exception ! \n%s' % (serverName, supportConf[serverName], e))
# alias
def w2v(word, type='ifchange'):
    return getWordVec(word, type)

def getCharacterVec(character):
    raise NotImplementedError

def getMostSimWords(word, topn=10, type_='ifchange'):
    try:
        data = {'words':word,'topn':topn,'type':type_}
        serverName='w2v'
        return doTask(serverName,data)
    except Exception as e:
        raiseException('%s exception \nplease contact supporter %s for this exception ! \n%s' % (serverName, supportConf[serverName], e))
# alias
def sim_words(word, topn=10, type='ifchange'):
    return getMostSimWords(word, topn, type)

# sent2vec
def getSentenceVec(sentences, type_='ifchange'):
    try:
        if isinstance(sentences, list):
            data = {'senlist':sentences, 'type':type_}
            serverName = 'sentencevec'
            return doTask(serverName,data)
        return None
    except Exception as e:
        raiseException('%s exception \nplease contact supporter %s for this exception ! \n%s' % (serverName, supportConf[serverName], e))
# alias
def s2v(sentences, type='ifchange'):
    return getSentenceVec(sentences, type)

# EmotionParser
def predictEmotion(sentences, prob=False):
    try:
        if sentences:
            data = {'text':sentences, 'prob':prob}
            serverName = 'sentiment'
            res = doTask(serverName, data)
            if prob:
                newlabel = []
                for l in res['labels']:
                    newlabel.append((l.split('_')[0], float(int(l.split('_')[1][:-1]) / 100)))
                res['labels'] = newlabel
                return res
            else:
                return res
        return None
    except Exception as e:
        raiseException('%s exception \nplease contact supporter %s for this exception ! \n%s' % (serverName, supportConf[serverName], e))
# alias
def emotion(sentences, prob=False):
    return predictEmotion(sentences, prob)

# SentenceSpliter
def getSubSentences(sentence, mode=0):
    try:
        if mode == 0 or mode == 1:
            data = {'sentence':sentence, 'mode':mode}
            serverName = 'sentence_spliter'
            return doTask(serverName, data)
        else:
            raiseException('Advise: make sure value of mode is 0 or 1')
    except Exception as e:
        raiseException('%s exception \nplease contact supporter %s for this exception ! \n%s' % (serverName, supportConf[serverName], e))
# alias
def split(sentence, mode=0):
    return getSubSentences(sentence, mode)

def getBertSentenceVec(texts, mode='wwm_ext'):
    try:
        bertVector = bert_vector()
        result = bertVector.parse(texts, mode)
        bertVector.close(mode)
        return result
    except Exception as e:
        raiseException('%s exception \nplease contact supporter %s for this exception ! \n%s' % ('bert sentence vector', supportConf['bert_service'], e))
# alias
def bert_vec(texts, mode='wwm_ext'):
    return getBertSentenceVec(texts, mode)

def getSentenceBertVec(text_a, text_b=[]):
    try:
        data = {"text_a": text_a, "text_b": text_b}
        serverName = 'sentence_bert'
        return doTask(serverName, data)
    except Exception as e:
        raiseException('%s exception \nplease contact supporter %s for this exception ! \n%s' % ('sentence bert vector', supportConf['sentence_bert'], e))
# alias
def bert_encode(text_a):
    return getSentenceBertVec(text_a)
def bert_sim(text_a, text_b):
    return getSentenceBertVec(text_a, text_b)

def getBertModels(model_name, output_dir=None):
    try:
        model_dir = bertModelConf.get(model_name)
        if not model_dir:
            print('Please check pass in valid model_name')
            print('Following models are available:')
            print('base_cn, wwm, wwm_ext, ernie_cv')
        else:
            print('Model Dir: ', model_dir)
            if output_dir:
                os.system('mkdir -p %s' % output_dir)
                ret = os.system('hadoop fs -get %s %s' % (model_dir, output_dir))
                if ret:
                    print('Download succeed!')
                else:
                    print('Please check whether model exists and concat %s' % supportConf['bert_service'])
    except Exception as e:
        raiseException('%s exception \nplease contact supporter %s for this exception ! \n%s' % ('sentence vector', supportConf['bert_service'], e))
# alias
def bertmodels(model_name, output_dir=None):
    getBertModels(model_name, output_dir)

def getKeywords(content, topk, with_weight):
    try:
        data = {'content':content, 'topk':topk, 'with_weight':with_weight}
        serverName = 'keywords'
        return doTask(serverName, data)
    except Exception as e:
        raiseException('%s exception \nplease contact supporter %s for this exception ! \n%s' % (serverName, supportConf[serverName], e))
# alias
def keywords(content, topk=3, with_weight=False):
    return getKeywords(content, topk, with_weight)

def getSentenceSim(text1, text2, precision=100, type_='ifchange'):
    try:
        data = {'text1':text1, 'text2':text2, 'precision':precision, 'type':type_}
        serverName = 'sentencesim'
        return doTask(serverName, data)
    except Exception as e:
        raiseException('%s exception \nplease contact supporter %s for this exception ! \n%s' % (serverName, supportConf[serverName], e))
# alias
def sent_sim(text1, text2, precision=100, type='ifchange'):
    return getSentenceSim(text1, text2, precision, type)

def getVOB(content, mode='fast'):
    try:
        data = {'content':content, 'mode':mode}
        serverName = 'verbobject'
        return doTask(serverName, data)
    except Exception as e:
        raiseException('%s exception \nplease contact supporter %s for this exception ! \n%s' % (serverName, supportConf[serverName], e))
# alias
def vob(content, mode='fast'):
    return getVOB(content, mode)

def getSentenceRationality(text, with_word_prob=False):
    try:
        data = {'text':text, 'word_prob':with_word_prob}
        serverName = 'rationality'
        return doTask(serverName, data)
    except Exception as e:
        raiseException('%s exception \nplease contact supporter %s for this exception ! \n%s'%(serverName, supportConf[serverName], e))
# alias
def rationality(text, with_word_prob=False):
    return getSentenceRationality(text, with_word_prob)

def doEntityTask(text, m):
    try:
        serverName = 'entity'
        return doCustomTask(serverName, text, m)
    except Exception as e:
        raiseException('%s exception \nplease contact supporter %s for this exception ! \n%s' % (serverName, supportConf[serverName], e))
# alias
def ner(text, m):
    return doEntityTask(text, m)

def name_ner(text):
    return doNameEntity(text)
