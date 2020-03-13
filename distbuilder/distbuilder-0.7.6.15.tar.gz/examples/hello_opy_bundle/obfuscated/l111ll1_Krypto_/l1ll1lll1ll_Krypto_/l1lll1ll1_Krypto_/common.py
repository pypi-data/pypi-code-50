# -*- coding: utf-8 -*-
from sys import version_info as __1l111l_Krypto_
l1lll_Krypto_ = __1l111l_Krypto_[0] == 2
l1l11ll_Krypto_ = 2048
l1l11_Krypto_ = 7
def l1l1111_Krypto_ (l1ll1l1_Krypto_):
    global l1l1l11_Krypto_
    l1111_Krypto_ = ord (l1ll1l1_Krypto_ [-1])
    l11l_Krypto_ = l1ll1l1_Krypto_ [:-1]
    l1l1lll_Krypto_ = l1111_Krypto_ % len (l11l_Krypto_)
    l11ll1_Krypto_ = l11l_Krypto_ [:l1l1lll_Krypto_] + l11l_Krypto_ [l1l1lll_Krypto_:]
    if l1lll_Krypto_:
        l1l_Krypto_ = unicode () .join ([unichr (ord (char) - l1l11ll_Krypto_ - (l11l1_Krypto_ + l1111_Krypto_) % l1l11_Krypto_) for l11l1_Krypto_, char in enumerate (l11ll1_Krypto_)])
    else:
        l1l_Krypto_ = str () .join ([chr (ord (char) - l1l11ll_Krypto_ - (l11l1_Krypto_ + l1111_Krypto_) % l1l11_Krypto_) for l11l1_Krypto_, char in enumerate (l11ll1_Krypto_)])
    return eval (l1l_Krypto_)
l1l1111_Krypto_ (u"࡙ࠥࠦࠧࡥ࡭ࡨ࠰ࡸࡪࡹࡴࡪࡰࡪࠤ࡫ࡵࡲࠡࡒࡼࡇࡷࡿࡰࡵࡱࠣ࡬ࡦࡹࡨࠡ࡯ࡲࡨࡺࡲࡥࡴࠤࠥࠦᘾ")
__revision__ = l1l1111_Krypto_ (u"ࠦࠩࡏࡤࠥࠤᘿ")
import sys as l1l11l11_Krypto_
import unittest as l1lll111111_Krypto_
import binascii as l11l111lll_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
if l1l11l11_Krypto_.hexversion < 0x02030000:
    def dict(**kwargs):
        return kwargs.copy()
else:
    dict = dict
class l1l111llll1_Krypto_(l1lll111111_Krypto_.TestCase):
    def __init__(self, l1l11ll1111_Krypto_, description, expected):
        l1lll111111_Krypto_.TestCase.__init__(self)
        self.l1l11ll1111_Krypto_ = l1l11ll1111_Krypto_
        self.expected = expected
        self.description = description
    def shortDescription(self):
        return self.description
    def runTest(self):
        self.assertTrue(hasattr(self.l1l11ll1111_Krypto_, l1l1111_Krypto_ (u"ࠧࡪࡩࡨࡧࡶࡸࡤࡹࡩࡻࡧࠥᙀ")))
        self.assertEqual(self.l1l11ll1111_Krypto_.digest_size, self.expected)
        h = self.l1l11ll1111_Krypto_.new()
        self.assertTrue(hasattr(h, l1l1111_Krypto_ (u"ࠨࡤࡪࡩࡨࡷࡹࡥࡳࡪࡼࡨࠦᙁ")))
        self.assertEqual(h.digest_size, self.expected)
class l1l111lll1l_Krypto_(l1lll111111_Krypto_.TestCase):
    def __init__(self, l1l11ll1111_Krypto_, description, expected, input):
        l1lll111111_Krypto_.TestCase.__init__(self)
        self.l1l11ll1111_Krypto_ = l1l11ll1111_Krypto_
        self.expected = expected
        self.input = input
        self.description = description
    def shortDescription(self):
        return self.description
    def runTest(self):
        h = self.l1l11ll1111_Krypto_.new()
        h.update(self.input)
        l1l111lllll_Krypto_ = l11l111lll_Krypto_.b2a_hex(h.digest())
        l1l111ll1ll_Krypto_ = h.hexdigest()
        h = self.l1l11ll1111_Krypto_.new(self.input)
        l1l11l1l1l1_Krypto_ = h.hexdigest()
        l1l111lll11_Krypto_ = l11l111lll_Krypto_.b2a_hex(h.digest())
        self.assertEqual(self.expected, l1l111lllll_Krypto_)
        if l1l11l11_Krypto_.version_info[0] == 2:
            self.assertEqual(self.expected, l1l111ll1ll_Krypto_)
            self.assertEqual(self.expected, l1l11l1l1l1_Krypto_)
        else:
            self.assertEqual(self.expected.decode(), l1l111ll1ll_Krypto_)
            self.assertEqual(self.expected.decode(), l1l11l1l1l1_Krypto_)
        self.assertEqual(self.expected, l1l111lll11_Krypto_)
        l1l11l11ll1_Krypto_ = h.new()
        l1l11l11ll1_Krypto_.update(self.input)
        l1l11l1111l_Krypto_ = l11l111lll_Krypto_.b2a_hex(l1l11l11ll1_Krypto_.digest())
        self.assertEqual(self.expected, l1l11l1111l_Krypto_)
class l1l11l11l11_Krypto_(l1lll111111_Krypto_.TestCase):
    def __init__(self, l1l11ll1111_Krypto_, l1llllll11_Krypto_):
        l1lll111111_Krypto_.TestCase.__init__(self)
        self.l1l11ll1111_Krypto_ = l1l11ll1111_Krypto_
        self.l1llllll11_Krypto_ = l1llllll11_Krypto_
    def runTest(self):
        h = self.l1l11ll1111_Krypto_.new()
        if self.l1llllll11_Krypto_==None:
            try:
                l1l11l1l111_Krypto_ = 0
                a = h.l1llllll11_Krypto_
            except AttributeError:
                l1l11l1l111_Krypto_ = 1
            self.assertEqual(l1l11l1l111_Krypto_,1)
        else:
            self.assertEqual(h.l1llllll11_Krypto_, self.l1llllll11_Krypto_)
class l1l11l11l1l_Krypto_(l1lll111111_Krypto_.TestCase):
    def __init__(self, l1l11ll1111_Krypto_, description, l1l11l11111_Krypto_, input, key, l1l11l111l1_Krypto_):
        l1lll111111_Krypto_.TestCase.__init__(self)
        self.l1l11ll1111_Krypto_ = l1l11ll1111_Krypto_
        self.l1l11l11111_Krypto_ = l1l11l11111_Krypto_
        self.input = input
        self.key = key
        self.l1l11l111l1_Krypto_ = l1l11l111l1_Krypto_
        self.description = description
    def shortDescription(self):
        return self.description
    def runTest(self):
        for l1l11l111ll_Krypto_ in list(self.l1l11l11111_Krypto_.keys()):
            l1l11ll1111_Krypto_ = self.l1l11l111l1_Krypto_[l1l11l111ll_Krypto_]
            key = l11l111lll_Krypto_.a2b_hex(b(self.key))
            data = l11l111lll_Krypto_.a2b_hex(b(self.input))
            expected = b(l1l1111_Krypto_ (u"ࠢࠣᙂ").join(self.l1l11l11111_Krypto_[l1l11l111ll_Krypto_].split()))
            h = self.l1l11ll1111_Krypto_.new(key, l1111111l_Krypto_=l1l11ll1111_Krypto_)
            h.update(data)
            l1l111lllll_Krypto_ = l11l111lll_Krypto_.b2a_hex(h.digest())
            l1l111ll1ll_Krypto_ = h.hexdigest()
            h = self.l1l11ll1111_Krypto_.new(key, data, l1l11ll1111_Krypto_)
            l1l11l1l1l1_Krypto_ = h.hexdigest()
            l1l111lll11_Krypto_ = l11l111lll_Krypto_.b2a_hex(h.digest())
            l1l11l11ll1_Krypto_ = h.copy()
            h.update(b(l1l1111_Krypto_ (u"ࠣࡤ࡯ࡥ࡭ࠦࡢ࡭ࡣ࡫ࠤࡧࡲࡡࡩࠤᙃ")))
            l1l11l1111l_Krypto_ = l11l111lll_Krypto_.b2a_hex(l1l11l11ll1_Krypto_.digest())
            self.assertEqual(expected, l1l111lllll_Krypto_)
            if l1l11l11_Krypto_.version_info[0] == 2:
                self.assertEqual(expected, l1l111ll1ll_Krypto_)
                self.assertEqual(expected, l1l11l1l1l1_Krypto_)
            else:
                self.assertEqual(expected.decode(), l1l111ll1ll_Krypto_)
                self.assertEqual(expected.decode(), l1l11l1l1l1_Krypto_)
            self.assertEqual(expected, l1l111lll11_Krypto_)
            self.assertEqual(expected, l1l11l1111l_Krypto_)
def l1l11l1l11l_Krypto_(module, module_name, l1ll11lllll_Krypto_, digest_size, l1llllll11_Krypto_=None):
    tests = []
    for i in range(len(l1ll11lllll_Krypto_)):
        row = l1ll11lllll_Krypto_[i]
        (expected, input) = list(map(b,row[0:2]))
        if len(row) < 3:
            description = repr(input)
        else:
            description = row[2].encode(l1l1111_Krypto_ (u"ࠩ࡯ࡥࡹ࡯࡮࠮࠳ࠪᙄ"))
        name = l1l1111_Krypto_ (u"ࠥࠩࡸࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࡶࡨࡷࡹࡹ࠮ࡢࡲࡳࡩࡳࡪࠨࡉࡣࡶ࡬ࡘ࡫࡬ࡧࡖࡨࡷࡹ࠮࡭ࡰࡦࡸࡰࡪ࠲ࠠ࡯ࡣࡰࡩ࠱ࠦࡥࡹࡲࡨࡧࡹ࡫ࡤ࠭ࠢ࡬ࡲࡵࡻࡴࠪࠫࠍࠤࠥࠦࠠࡪࡨࠣࡳ࡮ࡪࠠࡪࡵࠣࡲࡴࡺࠠࡏࡱࡱࡩ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡰ࡫ࡧࠤࡂࠦࡢࠩࡱ࡬ࡨ࠮ࠐࠠࠡࠢࠣࡲࡦࡳࡥࠡ࠿ࠣࠦᙅ")%s
    tests.append(l1l111llll1_Krypto_(module, name, digest_size))
    tests.append(l1l11l11l11_Krypto_(module, l1llllll11_Krypto_))
    return tests
def l1l11l11lll_Krypto_(module, module_name, l1ll11lllll_Krypto_, l1l11l111l1_Krypto_):
    tests = []
    for i in range(len(l1ll11lllll_Krypto_)):
        row = l1ll11lllll_Krypto_[i]
        (key, data, results, description) = row
        name = "%s
        tests.append(l1l11l11l1l_Krypto_(module, name, results, data, key, l1l11l111l1_Krypto_))
    return tests