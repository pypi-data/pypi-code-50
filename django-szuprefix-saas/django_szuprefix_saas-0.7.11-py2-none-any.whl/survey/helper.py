# -*- coding:utf-8 -*- 
__author__ = 'denishuang'
import re,logging
from django.utils.datastructures import OrderedDict

log = logging.getLogger("django")

def stat_answer(survey,extattr_filter=None):
    from allapps.company.helper import condition_match
    r = {}
    for answer in survey.answers.all():
        if extattr_filter and not condition_match(answer.worker.extattrs,extattr_filter):
            continue
        try:
            als = answer.content_json
        except Exception,e:
            log.warning(u"survey stat_answer error: %s:%s",e,answer.content)
            continue
        for a in als:
            q=a['name']
            if '_t' in q:
                if not a['value']:
                    continue
                n=q.split("_t")[0]
                r.setdefault(n,{})
                d = r.get(n)
                d.setdefault(q,"")
                d[q]+= "\n--------\n"+a['value']
            else:
                r.setdefault(q,{})
                d = r.get(q)
                d.setdefault(a['value'],0)
                d[a['value']]+=1
    return r

def stat_detail(survey,extattr_filter=None):
    cd = survey.content_json
    sd = stat_answer(survey,extattr_filter)
    cc = qc = 0
    for category in cd["categories"]:
        for question in category["questions"]:
            code = "c%s_q%s" % (cc,qc)
            question["code"] = code
            stat = OrderedDict()
            for s in question.get("S")+question.get("M"):
                stat[clear_text_input_under_line(s)]=0
            stat.update(sd.get(code,{}))
            question["stat"] = stat
            qc += 1
        qc = 0
        cc += 1
    return cd

def clear_text_input_under_line(s):
    return RE_TEXT_INPUT.sub("",s)

def replace_text_input(s,prefix):
    gs = re_group_split(RE_TEXT_INPUT,s)
    r = [gs[0][1]]
    i=0
    for g in gs[1:] :
        n= "%s_t%d" % (prefix,i)
        r.append("<input type='text' name='%s' class='answer_other_input answer_other_input_%d'>" % (n,i))
        r.append(g[1])
        i += 1
    return "".join(r)


def replace_textarea(s,prefix):
    gs = re_group_split(RE_TEXT_INPUT,s)
    r = [gs[0][1]]
    i=0
    for g in gs[1:] :
        n= "%s_t%d" % (prefix,i)
        r.append("<p><textarea name='%s'></textarea></p>" % (n))
        r.append(g[1])
        i += 1
    return "".join(r)
