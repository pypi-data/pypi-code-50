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
l1l1111_Krypto_ (u"ࠧࠨࠢࡔࡧ࡯ࡪ࠲ࡺࡥࡴࡶࠣࡷࡺ࡯ࡴࡦࠢࡩࡳࡷࠦࡃࡳࡻࡳࡸࡴ࠴ࡒࡢࡰࡧࡳࡲ࠴࡮ࡦࡹࠫ࠭ࠧࠨࠢᢓ")
__revision__ = l1l1111_Krypto_ (u"ࠨࠤࡊࡦࠧࠦᢔ")
import unittest as l1lll111111_Krypto_
import sys as l1l11l11_Krypto_
if l1l11l11_Krypto_.version_info[0] == 2 and l1l11l11_Krypto_.version_info[1] == 1:
    from l111ll1_Krypto_.l1l111ll_Krypto_.l1l1ll1l_Krypto_ import *
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
class l11l111l1l1_Krypto_(l1lll111111_Krypto_.TestCase):
    def runTest(self):
        l1l1111_Krypto_ (u"ࠢࠣࠤࡆࡶࡾࡶࡴࡰ࠰ࡕࡥࡳࡪ࡯࡮࠰ࡱࡩࡼ࠮ࠩࠣࠤࠥᢕ")
        from l111ll1_Krypto_ import l1ll1l11l1_Krypto_
        l11l111l11l_Krypto_ = l1ll1l11l1_Krypto_.new()
        x = l11l111l11l_Krypto_.read(16)
        y = l11l111l11l_Krypto_.read(16)
        self.assertNotEqual(x, y)
        l11l1111lll_Krypto_ = l1ll1l11l1_Krypto_.l1111l11l1_Krypto_(16)
        self.assertNotEqual(x, l11l1111lll_Krypto_)
        self.assertNotEqual(y, l11l1111lll_Krypto_)
        from l111ll1_Krypto_.l1ll1l11l1_Krypto_ import l111l1l111_Krypto_
        x = l111l1l111_Krypto_.l111l1111l_Krypto_(16*8)
        y = l111l1l111_Krypto_.l111l1111l_Krypto_(16*8)
        self.assertNotEqual(x, y)
        if x>y:
            start = y
            stop = x
        else:
            start = x
            stop = y
        for step in range(1,10):
            x = l111l1l111_Krypto_.l111l1ll11_Krypto_(start,stop,step)
            y = l111l1l111_Krypto_.l111l1ll11_Krypto_(start,stop,step)
            self.assertNotEqual(x, y)
            self.assertEqual(start <= x < stop, True)
            self.assertEqual(start <= y < stop, True)
            self.assertEqual((x - start) % step, 0)
            self.assertEqual((y - start) % step, 0)
        for i in range(10):
            self.assertEqual(l111l1l111_Krypto_.l111l1ll11_Krypto_(1,2), 1)
        self.assertRaises(ValueError, l111l1l111_Krypto_.l111l1ll11_Krypto_, start, start)
        self.assertRaises(ValueError, l111l1l111_Krypto_.l111l1ll11_Krypto_, stop, start, step)
        self.assertRaises(TypeError, l111l1l111_Krypto_.l111l1ll11_Krypto_, start, stop, step, step)
        self.assertRaises(TypeError, l111l1l111_Krypto_.l111l1ll11_Krypto_, start, stop, l1l1111_Krypto_ (u"ࠣ࠳ࠥᢖ"))
        self.assertRaises(TypeError, l111l1l111_Krypto_.l111l1ll11_Krypto_, l1l1111_Krypto_ (u"ࠤ࠴ࠦᢗ"), stop, step)
        self.assertRaises(TypeError, l111l1l111_Krypto_.l111l1ll11_Krypto_, 1, l1l1111_Krypto_ (u"ࠥ࠶ࠧᢘ"), step)
        self.assertRaises(ValueError, l111l1l111_Krypto_.l111l1ll11_Krypto_, start, stop, 0)
        x = l111l1l111_Krypto_.l111l111l1_Krypto_(start,stop)
        y = l111l1l111_Krypto_.l111l111l1_Krypto_(start,stop)
        self.assertNotEqual(x, y)
        self.assertEqual(start <= x <= stop, True)
        self.assertEqual(start <= y <= stop, True)
        for i in range(10):
            self.assertEqual(l111l1l111_Krypto_.l111l111l1_Krypto_(1,1), 1)
        self.assertRaises(ValueError, l111l1l111_Krypto_.l111l111l1_Krypto_, stop, start)
        self.assertRaises(TypeError, l111l1l111_Krypto_.l111l111l1_Krypto_, start, stop, step)
        self.assertRaises(TypeError, l111l1l111_Krypto_.l111l111l1_Krypto_, l1l1111_Krypto_ (u"ࠦ࠶ࠨᢙ"), stop)
        self.assertRaises(TypeError, l111l1l111_Krypto_.l111l111l1_Krypto_, 1, l1l1111_Krypto_ (u"ࠧ࠸ࠢᢚ"))
        seq = list(range(10000))
        x = l111l1l111_Krypto_.l1l1111ll_Krypto_(seq)
        y = l111l1l111_Krypto_.l1l1111ll_Krypto_(seq)
        self.assertNotEqual(x, y)
        self.assertEqual(x in seq, True)
        self.assertEqual(y in seq, True)
        for i in range(10):
            self.assertEqual(l111l1l111_Krypto_.l1l1111ll_Krypto_((1,2,3)) in (1,2,3), True)
        self.assertEqual(l111l1l111_Krypto_.l1l1111ll_Krypto_([1,2,3]) in [1,2,3], True)
        if l1l11l11_Krypto_.version_info[0] is 3:
            self.assertEqual(l111l1l111_Krypto_.l1l1111ll_Krypto_(bytearray(b(l1l1111_Krypto_ (u"࠭࠱࠳࠵ࠪᢛ")))) in bytearray(b(l1l1111_Krypto_ (u"ࠧ࠲࠴࠶ࠫᢜ"))), True)
        self.assertEqual(1, l111l1l111_Krypto_.l1l1111ll_Krypto_([1]))
        self.assertRaises(IndexError, l111l1l111_Krypto_.l1l1111ll_Krypto_, [])
        self.assertRaises(TypeError, l111l1l111_Krypto_.l1l1111ll_Krypto_, 1)
        seq = list(range(500))
        x = list(seq)
        y = list(seq)
        l111l1l111_Krypto_.l111l1l1ll_Krypto_(x)
        l111l1l111_Krypto_.l111l1l1ll_Krypto_(y)
        self.assertNotEqual(x, y)
        self.assertEqual(len(seq), len(x))
        self.assertEqual(len(seq), len(y))
        for i in range(len(seq)):
           self.assertEqual(x[i] in seq, True)
           self.assertEqual(y[i] in seq, True)
           self.assertEqual(seq[i] in x, True)
           self.assertEqual(seq[i] in y, True)
        l11l1111lll_Krypto_ = [1]
        l111l1l111_Krypto_.l111l1l1ll_Krypto_(l11l1111lll_Krypto_)
        self.assertEqual(l11l1111lll_Krypto_, [1])
        if l1l11l11_Krypto_.version_info[0] == 3:
            l11l1111lll_Krypto_ = bytearray(b(l1l1111_Krypto_ (u"ࠨ࠳࠵ࠫᢝ")))
            l111l1l111_Krypto_.l111l1l1ll_Krypto_(l11l1111lll_Krypto_)
            self.assertEqual(b(l1l1111_Krypto_ (u"ࠩ࠴ࠫᢞ")) in l11l1111lll_Krypto_, True)
            self.assertRaises(TypeError, l111l1l111_Krypto_.l111l1l1ll_Krypto_, b(l1l1111_Krypto_ (u"ࠪ࠵࠷࠭ᢟ")))
        self.assertRaises(TypeError, l111l1l111_Krypto_.l111l1l1ll_Krypto_, 1)
        self.assertRaises(TypeError, l111l1l111_Krypto_.l111l1l1ll_Krypto_, l1l1111_Krypto_ (u"ࠦ࠶ࠨᢠ"))
        self.assertRaises(TypeError, l111l1l111_Krypto_.l111l1l1ll_Krypto_, (1,2))
        x = l111l1l111_Krypto_.l111l11lll_Krypto_(seq, 20)
        y = l111l1l111_Krypto_.l111l11lll_Krypto_(seq, 20)
        self.assertNotEqual(x, y)
        for i in range(20):
           self.assertEqual(x[i] in seq, True)
           self.assertEqual(y[i] in seq, True)
        l11l1111lll_Krypto_ = l111l1l111_Krypto_.l111l11lll_Krypto_([1], 1)
        self.assertEqual(l11l1111lll_Krypto_, [1])
        l11l1111lll_Krypto_ = l111l1l111_Krypto_.l111l11lll_Krypto_((1,2,3), 1)
        self.assertEqual(l11l1111lll_Krypto_[0] in (1,2,3), True)
        l11l1111lll_Krypto_ = l111l1l111_Krypto_.l111l11lll_Krypto_(l1l1111_Krypto_ (u"ࠧ࠷࠲࠴ࠤᢡ"), 1)
        self.assertEqual(l11l1111lll_Krypto_[0] in l1l1111_Krypto_ (u"ࠨ࠱࠳࠵ࠥᢢ"), True)
        l11l1111lll_Krypto_ = l111l1l111_Krypto_.l111l11lll_Krypto_(list(range(3)), 1)
        self.assertEqual(l11l1111lll_Krypto_[0] in range(3), True)
        if l1l11l11_Krypto_.version_info[0] == 3:
                l11l1111lll_Krypto_ = l111l1l111_Krypto_.l111l11lll_Krypto_(b(l1l1111_Krypto_ (u"ࠢ࠲࠴࠶ࠦᢣ")), 1)
                self.assertEqual(l11l1111lll_Krypto_[0] in b(l1l1111_Krypto_ (u"ࠣ࠳࠵࠷ࠧᢤ")), True)
                l11l1111lll_Krypto_ = l111l1l111_Krypto_.l111l11lll_Krypto_(bytearray(b(l1l1111_Krypto_ (u"ࠤ࠴࠶࠸ࠨᢥ"))), 1)
                self.assertEqual(l11l1111lll_Krypto_[0] in bytearray(b(l1l1111_Krypto_ (u"ࠥ࠵࠷࠹ࠢᢦ"))), True)
        self.assertRaises(TypeError, l111l1l111_Krypto_.l111l11lll_Krypto_, 1)
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    return [l11l111l1l1_Krypto_()]
if __name__ == l1l1111_Krypto_ (u"ࠫࡤࡥ࡭ࡢ࡫ࡱࡣࡤ࠭ᢧ"):
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"ࠬࡹࡵࡪࡶࡨࠫᢨ"))