Ans="""


def gcd(a,b):
if b>a:
return gcd(b,a)
if a%b==0:
return gcd(b,a%b)

"""
