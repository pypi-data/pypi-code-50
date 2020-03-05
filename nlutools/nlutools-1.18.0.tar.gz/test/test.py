import sys

sys.path.append(".")
from nlutools import tools as nlu
from nlutools.config import env

# 分句
res = nlu.split(['我喜欢在春天去观赏桃花。在夏天去欣赏荷花 在秋天去观赏红叶。但更喜欢在冬天去欣赏雪景。', "可是啊。对的"])
assert len(res[0]) == 3
assert len(res[1]) == 2
print("nlu.split OK")

if env != "dev":
    # 分词
    line1 = "这是一个能够输出名词短语的分词器，欢迎试用！"
    line2 = "这是一个能够输出名词短语的分词器，欢迎试用，这里有神经网络，自然语言处理，和很多机器学习,tensorflow, pytorch"
    line3 = ""
    line4 = "欢迎"
    # line5 = "擅长红白案和本帮菜的厨师优先考虑"
    res = nlu.cut(line1)
    assert len(res['items']) == 12
    assert len(res['pos']) == 12
    assert res['np'][0] == '分词器'
    assert res['entity'][0] == '名词短语'
    res = nlu.cut(line1, pos=False)
    assert 'pos' not in res
    res = nlu.cut(line2)
    assert len(res['entity']) == 4
    res = nlu.cut(line3)
    assert res["items"] == []
    res = nlu.cut(line4)
    assert res["items"][0] == "欢迎"
    # res = nlu.cut("add", words=[["红白案", 100, "np"], ["本帮菜", 100, "np"]], user="test")
    # res = nlu.cut(line5)
    # assert "红白案" in res["items"] and "本帮菜" in res["items"]
    # res = nlu.cut("del", user="test")
    # res = nlu.cut(line5)
    # assert "红白案" not in res["items"] and "本帮菜" not in res["items"]
    print("nlu.cut OK")

    # 词向量
    res = nlu.w2v('深度学习')
    assert len(res) == 1
    assert len(res[0]) == 300
    res = nlu.w2v('深度学习', type='tencent')
    assert len(res) == 1
    assert len(res[0]) == 200
    res = nlu.w2v(['深度学习', '机器学习'])
    assert len(res) == 2
    assert len(res[0]) == 300
    res = nlu.w2v(['深度学习','机器学习'], type='tencent')
    assert len(res) == 2
    assert len(res[0]) == 200
    res = nlu.sim_words('深度学习', 10)
    assert len(res) == 10
    assert len(res[0]) == 2
    res = nlu.sim_words('深度学习', 10, type='tencent')
    assert len(res) == 10
    assert len(res[0]) == 2
    res = nlu.sim_words(['深度学习', '机器学习'], 10)
    assert len(res) == 2
    assert len(res[0]) == 10
    assert len(res[0][0]) == 2
    res = nlu.sim_words(['深度学习', '机器学习'], 10, type='tencent')
    assert len(res) == 2
    assert len(res[0]) == 10
    assert len(res[0][0]) == 2
    res = nlu.sim_score('深度学习', '机器学习', type='tencent')
    assert res > 0.5
    res = nlu.sim_score('深度学习', '机器学习')
    assert res > 0.5
    print("nlu.w2v OK")

    # 普通句向量
    res = nlu.s2v(['主要负责机器学习算法的研究', '训练模型、编写代码、以及其他一些工作', "", "我"])
    assert res['dimention'] == 300
    assert len(res['veclist']) == 4
    assert len(res['veclist'][0]) == 300
    assert sum(res['veclist'][2]) == 0.
    assert sum(res['veclist'][3]) != 0.

    res = nlu.s2v(['主要负责机器学习算法的研究', '训练模型、编写代码、以及其他一些工作', "", "我"], type='tencent')
    assert res['dimention'] == 200
    assert len(res['veclist']) == 4
    assert len(res['veclist'][0]) == 200

    # bert句向量 from bert-as-service
    res = nlu.bert_vec(['主要负责机器学习算法的研究', '训练模型、编写代码、以及其他一些工作'])
    assert res.shape == (2, 768)
    res = nlu.bert_vec(['主要负责机器学习算法的研究', '训练模型、编写代码、以及其他一些工作'], mode='cv')
    assert res.shape == (2, 768)
    print("nlu.bert_vec OK")

# sentence bert句向量及相似度
res = nlu.bert_encode(['主要负责机器学习算法的研究', '训练模型、编写代码、以及其他一些工作'])
assert len(res['vec']) == 2
assert len(res['vec'][0]) == 512
print("nlu.bert_encode OK")
res = nlu.bert_sim("句子通用向量表征", "自然语言处理是人工智能的明珠")
assert res["sim"] < 0.18
res = nlu.bert_sim("句子通用向量表征", ["自然语言处理是人工智能的明珠", "句子表征哪个模型厉害？"])
assert res["sim"][0][0] == "句子表征哪个模型厉害？"
res = nlu.bert_sim(["句子通用向量表征", "自然语言处理这几年发展很快"], ["自然语言处理是人工智能的明珠", "句子表征哪个模型厉害？"])
assert res["sim"][1][0] > 0.6
print("nlu.bert_sim OK")


# 5
# nlu.bertmodels('wwm_ext', './bert_models')

# AI5组 实体服务
res = nlu.ner(["我毕业于北京大学"], 'ner')
assert res[0][0]['text'] == "北京大学"
print("nlu.entity OK")

# 情感分析
res = nlu.emotion(['这家公司很棒','这家公司很糟糕'])
assert res['labels'][0] == 'pos'
assert res['labels'][1] == 'neg'
res = nlu.emotion(['这家公司很棒','这家公司很糟糕'], prob=True)
assert res['labels'][0][0] == 'pos'
assert res['labels'][1][0] == 'neg'
assert res['labels'][0][1] == 0.88
assert res['labels'][1][1] == 0.82
print("nlu.emotion OK")

if env != "dev":
    # 关键词
    res = nlu.keywords('主要负责机器学习算法的研究以及搭建神经网络，训练模型，编写代码，以及其他的一些工作', 4, True)
    assert len(res['keywords']) == 4
    assert len(res['weights']) == 4
    res = nlu.keywords('主要负责机器学习算法的研究以及搭建神经网络，训练模型，编写代码，以及其他的一些工作', 4)
    assert len(res['keywords']) == 4
    assert len(res['weights']) == 0
    res = nlu.keywords('主要负责机器学习算法的研究以及搭建神经网络，训练模型，编写代码，以及其他的一些工作')
    assert len(res['keywords']) == 3
    assert len(res['weights']) == 0
    print("nlu.keywords OK")

    # 句子相似度
    res = nlu.sent_sim('你家的地址是多少', '你住哪里', 1000)
    assert res['result'] > 500
    res = nlu.sent_sim('你家的地址是多少', '', 1000, type="tencent")
    assert res['result'] == 0
    print("nlu.sent_sim OK")

    # 动宾提取
    res = nlu.vob('要负责机器学习算法的研究以及搭建神经网络，训练模型，编写代码，以及其他的一些工作')
    assert len(res) > 0
    print("nlu.vob OK")

# 句子合理性
res = nlu.rationality(['床前明月光，疑是地上霜', '床前星星光，疑是地上霜', '床前白月光，疑是地上霜'])
assert len(res['ppl']) == 3
print("nlu.rationality OK")

# AI2组 姓名识别
res = nlu.name_ner("刘德华的⽼老老婆叫叶丽倩")
assert len(res) == 2
print("nlu.name_ner OK")
