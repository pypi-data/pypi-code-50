import re

s = 'hello MaNa vs. TLO goodbye'

r = re.search('\\w+ +[v,V][s,S]\\. +\\w+', s)
print(re.split('.vs\\..', r.group()))


new = re.search('\\w{1}(?: *$)', 'Group A')
print(new)
