# -*- coding: utf-8 -*-

import pytest
from snakespace import SnakeSpace

__author__ = "cmrfrd"
__copyright__ = "cmrfrd"
__license__ = "mit"

def test_simple_snakespace():
    S = SnakeSpace()
    assert (S == "")
    assert (str(S) == "")
    assert (str(S) != " ")

def test_init_snakespace():
    S = SnakeSpace('yo.what.up')
    assert (str(S) != " ")
    assert (S == "yo.what.up")
    assert (str(S) == "yo.what.up")
    assert (S[0] == "yo")
    assert (S[1] == "what")
    assert (S[2] == "up")

def test_attrchain_snakespace():
    S = SnakeSpace()
    assert (S.a  == "a")
    assert (S.b.c  == "b.c")
    assert (S.b.c.d  == "b.c.d")

def test_s_snakespace():
    S = SnakeSpace()
    assert (S.c.de.s(1)  == "c.de.1")
    assert (S.c.de.s(1)  != "c.de")
    assert (S.a.b.s('c').d  == "a.b.c.d")
    assert (S.s('a.b.c.d').e.f  == "a.b.c.d.e.f")
    assert (S.a.b.c.d.s().e.f  == "a.b.c.d.e.f")
    assert (S.e.f.g.s(a=3).h  == "e.f.g.3.h")
    assert (S.metrics.score.s(5).yay  == "metrics.score.5.yay")
    assert (S.yay == "yay")
    assert (S.s().a == "a")
    assert (S.s().a.b.s() == "a.b")
    assert (S.s().a.b.s().c.d == "a.b.c.d")
    assert (S.s().a.b.s().c.d.s() == "a.b.c.d")
    assert (S.s(1,False) == "1.False")
    assert (S.s(1,a=2) == "1.2")
    assert (S.s(1,a=2).a.b.s(3) == "1.2.a.b.3")
    assert (S.a.s(1,a=2).a.b.s(3) == "a.1.2.a.b.3")

def test_s_name_collision():
    S = SnakeSpace()
    from random import randint as s
    assert (S.a.s(s(0,0)) == "a.0")

def test_inter_snakespace():
    S = SnakeSpace()
    assert (S.a.s(S.a, S.b) == "a.a.b")
    assert (S.a.s(S.a) == "a.a")
    assert (S.a.s(asdf=S.a) == "a.a")
    assert (S.a.s(asdf=S.a).qwer == "a.a.qwer")

def test_separator_snakespace_access():
    S = SnakeSpace()
    S.separator = "_"
    assert (S.separator == "_")
    S.separator = "."
    assert (S.separator == ".")

def test_sep_snakespace():
    S = SnakeSpace()
    S.separator = "_"
    assert (S == "")
    assert (str(S) == "")
    assert (S.a == "a")
    assert (S.a.b == "a_b")
    assert (S.a.b.c == "a_b_c")
    assert (S.a.s().c == "a_c")
    S.separator = "."

def test_prefix_snakespace():
    S = SnakeSpace(prefix="@")
    assert (S == "@")
    assert (str(S) == "@")
    assert (S.a == "@a")
    assert (S.a.b == "@a.b")
    assert (S.a.b.c == "@a.b.c")
    assert (S.a.s().c == "@a.c")
    assert (S.a.s(1,2).c == "@a.1.2.c")

def test_suffix_snakespace():
    S = SnakeSpace(suffix="@")
    assert (S == "@")
    assert (str(S) == "@")
    assert (S.a == "a@")
    assert (S.a.b == "a.b@")
    assert (S.a.b.c == "a.b.c@")
    assert (S.a.s().c == "a.c@")
    assert (S.a.s(1,2).c == "a.1.2.c@")

def test_snakespace_casting_and_operators():
    S = SnakeSpace()

    # casting
    assert (int(S.s(1)) == 1)
    with pytest.raises(ValueError):
        int(S.a)

    assert (float(S.s(1.0)) == 1.0)
    with pytest.raises(ValueError):
        float(S.a)

    assert (complex(S.s(1.0)) == 1.0+0j)
    with pytest.raises(ValueError):
        complex(S.a)

    assert (hash(S.s(1.0)) == hash('1.0'))

    # gt and lt
    assert (S.a.b.c > S.a)
    assert (S.a.b.c > "a")
    assert (S.a < S.a.b.c)
    assert (S.a < "a.b.c")
    assert (S.a.b.c < S.b)
    assert (S.a.b.c > S.a.s(1))
    assert (S.a.b.c >= S.a.s(1))
    assert ("a.b.c" >= S.a.s(1))
    assert (S.a.b.c >= S.a.b.c)
    assert ("a.b.c" >= S.a.b.c)
    assert (S.a.b.c <= S.a.b.c)
    assert ("a.b.c" <= S.a.b.c)
    assert (S.a.b.c <= S.a.c)
    assert ("a.b.c" <= S.a.c)


    # length
    assert (len(S) == 0)
    assert (len(S.a.b.c) == 3)
    assert (len(S.a.s(1,2,3).c) == 5)
    assert (len(S.apple.bannana.cherry) == 3)

    # contains
    assert ((S.a.b in S.a) == True)
    assert ((S.a not in S.a.b) == True)
    assert (('a' in S.a) == True)
    assert (('b' not in S.a) == True)
    assert ((S.a.b.c in S.a.b) == True)

    # getargs
    assert (S.a.b.c[0] == 'a')
    assert (S.a.b.c[1] == 'b')
    assert (S.a.b.c[2] == 'c')
    assert (S.a.s(1,2,3).c.d[1] == '1')
    assert (S.a.s(1,2,3).c.d[2] == '2')
    assert (S.a.s(1,2,3).c.d[3] == '3')
    assert (S.a.s(1,2,3).c.d[4] == 'c')
    assert (S.a.s(1,2,3).c.d[5] == 'd')

    # addition
    assert (S.a + S.b == S.a.b)
    assert (S.b + S.a == S.b.a)
    assert (S.a + 'a' == "aa")
    assert ('a' + S.a.b.c == "aa.b.c")
    assert (S.a.b.c.__radd__(S.a) == "a.a.b.c")

    # modulo
    assert (S.a % S.b == False)
    assert (S.b % S.a == False)
    assert (S.a % S.a == True)
    assert (S.a.b % S.a == False)
    assert (S.a % S.a.b == True)
    assert (S.a.b.c % S.a == False)
    assert (S.a % S.a.b.c == True)
    assert (S.a.b.c % "a.b.c" == True)
    assert (S.a % "a" == True)
    assert (S.a.b.c % "a.b.c" == True)
    print(S.a.b.c, "a.b.c")
    assert (("a.b.c" % S.a.b) == "a.b.c") # edge case str formatting
    Q = SnakeSpace(separator="/")
    assert (S.a % Q.a.b.c == True)
    assert (Q.a.b.c % "a/b/c" == True)

def test_snakespace_str_methods():

    # capitalize
    S = SnakeSpace()
    assert (S.a.b.c.capitalize() == S.A.B.C)
    S.separator = 'a'
    assert (S.a.b.c.capitalize() == "AaBaC")
    S.separator = '.'
    S = SnakeSpace(prefix='a')
    assert (S.a.b.c.capitalize() == "aA.B.C")
    S = SnakeSpace(suffix='a')
    assert (S.a.b.c.capitalize() == "A.B.Ca")

    # casefold
    S = SnakeSpace()
    assert (S.A.B.C.casefold() == S.a.b.c)
    S.separator = 'a'
    assert (S.A.B.C.casefold() == "aabac")
    S.separator = '.'
    S = SnakeSpace(prefix='a')
    assert (S.A.B.C.casefold() == "aa.b.c")
    S = SnakeSpace(suffix='a')
    assert (S.A.B.C.casefold() == "a.b.ca")

    # encode
    S = SnakeSpace()
    assert (S.a.b.c.encode() == b"a.b.c")

    # endswith
    S = SnakeSpace()
    assert (S.a.b.c.endswith("c") == True)
    assert (S.a.b.c.endswith("d") == False)
    assert (S.a.b.c.endswith(S.c) == True)
    assert (S.a.b.c.endswith(S.asdf) == False)
    assert (S.a.b.c.endswith(S.b.c) == True)
    assert (S.a.b.c.endswith(S.b, end=-1) == True)
    assert (S.a.b.c.endswith(S.b, start=1) == False)

    # find
    S = SnakeSpace()
    assert (S.a.b.c.find("c") == 2)
    assert (S.a.b.c.find("asdf") == -1)
    assert (S.aa.bb.cc.find(S.c) == 2)
    assert (S.aa.bb.cc.find(S.bb) == 1)
    assert (S.a.b.c.find(S.asdf) == -1)
    assert (S.apple.potato.radish.find("is") == 2)
    assert (S.apple.potato.radish.find("rad") == 2)
    assert (S.apple.potato.radish.find("tat") == 1)
    assert (S.apple.potato.radish.find(S.rad) == 2)
    assert (S.apple.potato.radish.find(S.rad.ish) == -1)

    # index
    S = SnakeSpace()
    assert (S.a.index(S.a) == 0)
    with pytest.raises(ValueError):
        S.a.index(S.b)
    assert (S.a.b.c.d.index(S.c) == 2)
    with pytest.raises(ValueError):
        S.a.index('asdf')

    # isalpha
    S = SnakeSpace()
    assert (S.a.b.c.isalpha() == True)
    assert (S.a.s(1,2,3).c.isalpha() == False)

    # isalnum
    S = SnakeSpace()
    assert (S.a.b.c.isalnum() == True)
    assert (S.a.s(1,2,3).c.isalnum() == True)
    assert (S.a.s(1,2,3, d="#").c.isalnum() == False)

    # isdecimal
    S = SnakeSpace()
    assert (S.a.b.c.isdecimal() == False)
    assert (S.a.s(1,2,3).c.isdecimal() == False)
    assert (S.s(1,2,3).isdecimal() == True)

    # isdigit
    S = SnakeSpace()
    assert (S.a.b.c.isdigit() == False)
    assert (S.a.s(1,2,3).c.isdigit() == False)
    assert (S.s(1,2,3).isdigit() == True)

    # isidentifier
    S = SnakeSpace()
    assert (S.a.b.c.isidentifier() == True)
    assert (S.a.s(1,2,3).c.isidentifier() == False)
    assert (S.s(1,2,3).isidentifier() == False)

    # islower
    S = SnakeSpace()
    assert (S.a.b.c.islower() == True)
    assert (S.a.s(1,2,3).c.islower() == False)
    assert (S.s(1,2,3).islower() == False)
    assert (S.A.B.islower() == False)

    # isnumeric
    S = SnakeSpace()
    assert (S.a.b.c.isnumeric() == False)
    assert (S.a.s(1,2,3).c.isnumeric() == False)
    assert (S.s(1,2,3).isnumeric() == True)

    # isprintable
    S = SnakeSpace()
    assert (S.a.b.c.isprintable() == True)
    assert (S.a.s(1,2,3).c.isprintable() == True)
    assert (S.s(1,2,3).isprintable() == True)
    assert (S.s('\n').isprintable() == False)

    # isspace
    S = SnakeSpace()
    assert (S.a.b.c.isspace() == False)
    assert (S.a.s(1,2,3).c.isspace() == False)
    assert (S.s(1,2,3).isspace() == False)
    assert (S.s(' ').isspace() == True)
    assert (S.s(' ', ' ').isspace() == True)
    assert (S.s(' ').s(' ').isspace() == True)

    # istitle
    S = SnakeSpace()
    assert (S.a.b.c.istitle() == False)
    assert (S.a.s(1,2,3).c.istitle() == False)
    assert (S.Ay.What.Up.istitle() == True)
    assert (S.Ay.s("What").Up.istitle() == True)

    # isupper
    S = SnakeSpace()
    assert (S.a.b.c.isupper() == False)
    assert (S.a.s(1,2,3).c.isupper() == False)
    assert (S.AY.WHAT.UP.isupper() == True)
    assert (S.AY.s("What").UP.isupper() == False)
    assert (S.AY.s("WHAT").UP.isupper() == True)

    #ljust
    S = SnakeSpace()
    assert (S.a.b.c.ljust(5) == "a    .b    .c    ")
    assert (S.a.s(1,2,3).c.ljust(2,'.') == "a..1..2..3..c.")
    assert (S.a.s(1,2,3).c.ljust(3,'.') == "a...1...2...3...c..")

    # lower
    S = SnakeSpace()
    assert (S.a.b.c.lower() == S.a.b.c)
    assert (S.a.s(1,2,3).c.lower() == S.a.s(1,2,3).c)
    assert (S.AY.WHAT.UP.lower() == S.ay.what.up)
    assert (S.AY.s("What").UP.lower() == S.ay.what.up)
    assert (S.AY.s("WHAT").UP.lower() == S.ay.what.up)

    # lstrip
    S = SnakeSpace()
    assert (S.s(' a').s(' b').s(' c').lstrip() == S.a.b.c)

    # partition
    S = SnakeSpace()
    assert (S.a.b.c.partition() == S.a.b.c)
    assert (S.a.s("ya@ya").c.partition('@') == "a.ya.@.ya.c")
    assert (S.a.s("yaya").c.partition(S.ya) == "a.ya.ya.c")

    # replace
    S = SnakeSpace()
    assert (S.a.b.c.replace(S.asdf, S.asdf) == S.a.b.c)
    assert (S.a.b.c.replace(S.b, S.c) == S.a.c.c)
    assert (S.a.b.c.replace('b', 'c') == S.a.c.c)
    assert (S.yay.s(1,2,3).b.c.replace(1, 2) == S.yay.s(2,2,3).b.c)


    # rfind
    S = SnakeSpace()
    assert (S.a.b.c.b.a.rfind("b") == 3)
    assert (S.a.b.c.rfind("asdf") == -1)
    assert (S.aa.bb.cc.bb.aa.rfind(S.c) == 2)
    assert (S.aa.bb.cc.rfind(S.bb) == 1)
    assert (S.a.b.c.rfind(S.asdf) == -1)
    assert (S.apple.potato.radish.rfind("is") == 2)
    assert (S.apple.potato.radish.rfind("rad") == 2)
    assert (S.apple.potato.radish.rfind("tat") == 1)
    assert (S.apple.potato.radish.rfind(S.rad) == 2)
    assert (S.apple.potato.radish.rfind(S.rad.ish) == -1)

    # rindex
    S = SnakeSpace()
    assert (S.a.rindex(S.a) == 0)
    with pytest.raises(ValueError):
        S.a.rindex(S.b)
    assert (S.a.b.c.d.rindex(S.c) == 2)
    assert (S.a.b.c.d.c.b.a.rindex(S.c) == 4)
    with pytest.raises(ValueError):
        S.a.index('asdf')

    # rjust
    S = SnakeSpace()
    assert (S.a.b.c.rjust(5) == "    a.    b.    c")
    assert (S.a.s(1,2,3).c.rjust(2,'.') == ".a..1..2..3..c")
    assert (S.a.s(1,2,3).c.rjust(3,'.') == "..a...1...2...3...c")

    # rpartition
    S = SnakeSpace()
    assert (S.a.b.c.rpartition() == S.a.b.c)
    assert (S.a.s("ya@ya").c.rpartition('@') == "a.ya.@.ya.c")
    assert (S.a.s("yaya").c.rpartition(S.ya) == "a.ya.ya.c")
    assert (S.aa.bb.cc.bb.aa.rpartition(S.b) == S.aa.b.b.cc.b.b.aa)
    assert (S.aabbaabbcc.rpartition(S.bb) == S.aabbaa.bb.cc)

    # startswith
    S = SnakeSpace()
    assert (S.startswith(S) == True)
    assert (S.a.b.c.startswith(S.a.b.c) == True)
    assert (S.a.b.c.startswith(S.b.c) == False)
    assert (S.a.b.c.startswith("a.b.c") == True)
    assert (S.a.b.c.startswith("b.c") == False)

    # rstrip
    S = SnakeSpace()
    assert (S.s('a ').s('b ').s('c ').rstrip() == S.a.b.c)

    # strip
    S = SnakeSpace()
    assert (S.s(' a ').s(' b ').s(' c ').strip() == S.a.b.c)

    # swapcase
    S = SnakeSpace()
    assert (S.A.b.C.swapcase() == S.a.B.c)
    assert (S.A.s("aPpLe").C.swapcase() == S.a.ApPlE.c)

    # title
    S = SnakeSpace()
    assert (S.A.b.C.title() == S.A.B.C)
    assert (S.A.apple.C.title() == S.A.Apple.C)

    # translate
    S = SnakeSpace()
    assert (S.A.B.C.translate(S.B,S.A,S.C) == S.A.A)

    # upper
    S = SnakeSpace()
    assert (S.a.b.c.upper() == S.A.B.C)
    assert (S.wut.da.ship.upper() == S.WUT.DA.SHIP)

    # zfill
    S = SnakeSpace()
    assert (S.a.b.c.zfill(0) == S.a.b.c)
    assert (S.wut.da.ship.zfill(5) == S.s('00wut').s('000da').s('0ship'))
