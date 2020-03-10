Ans="""

from math import *
pf=[]
n=int(input('enter no'))
x=n
while n%2==0:
pf.append(2)
n=n/2
i=3
while i<=sqrt(n):
while n%i==0:
pf.append(i)
n=n/i
i=i+2
if n>2:
pf.append(n)
print('prime factors of',x,'are',pf)
pf1=set(pf)
nf=1
for f in pf1:
cnt=0
for f1 in pf:
if f==f1:
cnt+=1
nf*=cnt+1
print('no of fators of',x,'=',nf)
print('no of positive integral solutions=',nf/2)

"""
