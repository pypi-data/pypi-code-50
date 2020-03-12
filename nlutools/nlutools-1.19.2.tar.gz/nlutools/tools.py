import os
import subprocess

from nlutools.config import mapConf, supportConf, bertModelConf
from nlutools.config import getEnvLabel, getLocalIp
from nlutools.online_bert_client import bert_vector
from nlutools.rpc_client import doTask, doCustomTask, doNameEntity
from nlutools.utils import raiseException


class NLU(object):
    def __init__(self, env=""):
        host_ip = getLocalIp()
        if host_ip.startswith("172"):
            if not env:
                print("请设置环境参数：dev=开发环境，online=线上环境，test=测试环境")
                print("参考示例：nlu = NLU('dev')")
        else:
            env = getEnvLabel(host_ip)
        self.env = env
        print("您目前处在%s环境" % self.env)

    def raise_exception(self, e, server_name):
        raiseException('%s exception \nplease contact supporter %s for this exception ! \n%s' % (server_name, supportConf[server_name], e))

    def cut(self, sentence, pos=True, cut_all=False, mode='fast'):
        """名词短语分词"""
        server_name = 'segmentor'
        try:
            if mode in ['fast', 'accurate']:
                if isinstance(pos, bool) and isinstance(cut_all, bool):
                    if sentence == "":
                        res = {"text":"", "items":[], "pos":[], "np":[], "entity":[]}
                    else:
                        data = {'text':sentence, 'mode':mode, 'pos':pos, 'cut_all':cut_all}
                        res = doTask(self.env, server_name, data)
                    return res
                else:
                    return "Please assign boolean value for variables `pos` and `cut_all`"
            else:
                raiseException('Advise: check parameters, make sure value of mode is fast or default, value of pos is true, false or default as well')
        except Exception as e:
            self.raise_exception(server_name, e)

    def getKeywords(self, content, topk, with_weight):
        """关键词抽取"""
        server_name = 'keywords'
        try:
            data = {'content':content, 'topk':topk, 'with_weight':with_weight}
            return doTask(self.env, server_name, data)
        except Exception as e:
            self.raise_exception(server_name, e)

    def keywords(self, content, topk=3, with_weight=False):
        return self.getKeywords(content, topk, with_weight)

    def getSubSentences(self, sentence):
        """规则切句"""
        server_name = 'sentence_spliter'
        try:
            data = {'sentence':sentence, 'mode': 0}
            return doTask(self.env, server_name, data)
        except Exception as e:
            self.raise_exception(server_name, e)

    def split(self, sentence):
        return self.getSubSentences(sentence)

    def getW2VFile(self, version_key, localpath):
        """获取词向量文件"""
        server_name = 'w2v'
        try:
            assert self.env == "online"
        except AssertionError as e:
            raise Exception("only support for online env")
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
                    self.raise_exception(server_name, e)
        except Exception as e:
            raise Exception('Advise: please install hadoop client before use getW2VFile')
    
    def getWordVec(self, word, type_='ifchange'):
        """获取词向量表征"""
        server_name = 'w2v'
        try:
            if isinstance(word, str):
                word = [word]
            data = {'words':word, 'type':type_}
            return doTask(self.env, server_name, data)
        except Exception as e:
            self.raise_exception(e, server_name)
    
    def getCharacterVec(self, char):
        raise NotImplementedError

    def w2v(self, word, type='ifchange'):
        return self.getWordVec(word, type)

    def getWordSimScore(self, word1, word2, type_='ifchange'):
        """词向量相似度计算"""
        server_name = 'w2v'
        try:
            data = {'word1':word1, 'word2':word2, 'type':type_}
            return float(doTask(self.env, server_name, data))
        except Exception as e:
            self.raise_exception(e, server_name)

    def word_sim(self, word1, word2, type='ifchange'):
        return self.getWordSimScore(word1, word2, type)

    def getMostSimWords(self, word, topn=10, type_='ifchange'):
        """相似词"""
        server_name='w2v'
        try:
            data = {'words':word,'topn':topn,'type':type_}
            return doTask(self.env, server_name, data)
        except Exception as e:
            self.raise_exception(e, server_name)

    def sim_words(self, word, topn=10, type='ifchange'):
        return self.getMostSimWords(word, topn, type)

    def getSentenceVec(self, sentences, type_='ifchange'):
        """基于TF—IDF的句向量表征"""
        server_name = 'sentencevec'
        try:
            if isinstance(sentences, str):
                sentences = [sentences]
            data = {'senlist':sentences, 'type':type_}
            return doTask(self.env, server_name, data)
        except Exception as e:
            self.raise_exception(e, server_name)

    def s2v(self, sentences, type='ifchange'):
        return self.getSentenceVec(sentences, type)

    def getSentenceSim(self, text1, text2, precision=100, type_='ifchange'):
        """句子相似度计算"""
        server_name = 'sentencesim'
        try:
            data = {'text1':text1, 'text2':text2, 'precision':precision, 'type':type_}
            return doTask(self.env, server_name, data)
        except Exception as e:
            self.raise_exception(e, server_name)

    def sent_sim(self, text1, text2, precision=100, type='ifchange'):
        return self.getSentenceSim(text1, text2, precision, type)

    def getBertSentenceVec(self, texts, mode='wwm_ext'):
        """基于bert-as-service的bert句向量服务"""
        server_name = 'bert_service'
        try:
            bertVector = bert_vector()
            result = bertVector.parse(texts, mode)
            bertVector.close(mode)
            return result
        except Exception as e:
            self.raise_exception(e, server_name)

    def bert_vec(self, texts, mode='wwm_ext'):
        return self.getBertSentenceVec(texts, mode)

    def getSentenceBertVec(self, text_a, text_b=[], metric="cosine"):
        """Sentence-BERT句向量及相似度计算"""
        server_name = 'sentence_bert'
        try:
            data = {"text_a": text_a, "text_b": text_b, "metric": metric}
            return doTask(self.env, server_name, data)
        except Exception as e:
            self.raise_exception(e, server_name)

    def bert_encode(self, text_a):
        return self.getSentenceBertVec(text_a)

    def bert_sim(self, text_a, text_b, metric="cosine"):
        return self.getSentenceBertVec(text_a, text_b, metric)

    def predictEmotion(self, sentences, prob=False):
        """BERT情感模型"""
        server_name = 'sentiment'
        try:
            if sentences:
                data = {'text':sentences, 'prob':prob}
                res = doTask(self.env, server_name, data)
                if prob:
                    newlabel = []
                    for l in res['labels']:
                        label, score = l.split('_')
                        score = round(float(int(score[:-1]) / 100), 2)
                        newlabel.append((label, score))
                    res['labels'] = newlabel
                    return res
                else:
                    return res
            return None
        except Exception as e:
            self.raise_exception(e, server_name)

    def emotion(self, sentences, prob=False):
        return self.predictEmotion(sentences, prob)

    def getBertModels(self, model_name, output_dir=None):
        """下载BERT模型"""
        server_name = "bert_service"
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
            self.raise_exception(e, server_name)

    def bert_models(self, model_name, output_dir=None):
        self.getBertModels(model_name, output_dir)

    def getVOB(self, content, mode='fast'):
        """动宾提取"""
        server_name = 'verbobject'
        try:
            data = {'content':content, 'mode':mode}
            return doTask(self.env, server_name, data)
        except Exception as e:
            self.raise_exception(e, server_name)
    def vob(self, content, mode='fast'):
        return self.getVOB(content, mode)

    def getSentenceRationality(self, text, with_word_prob=False):
        server_name = 'rationality'
        """BERT句子合理性"""
        try:
            data = {'text':text, 'word_prob':with_word_prob}
            return doTask(self.env, server_name, data)
        except Exception as e:
            self.raise_exception(e, server_name)

    def rationality(self, text, with_word_prob=False):
        return self.getSentenceRationality(text, with_word_prob)

    def doEntityTask(self, text, m):
        """AI5组实体服务"""
        server_name = 'entity'
        try:
            return doCustomTask(self.env, server_name, text, m)
        except Exception as e:
            self.raise_exception(e, server_name)

    def ner(self, text, m):
        return self.doEntityTask(text, m)

    def name_ner(self, text):
        """AI2组姓名识别服务"""
        return doNameEntity(self.env, text)
