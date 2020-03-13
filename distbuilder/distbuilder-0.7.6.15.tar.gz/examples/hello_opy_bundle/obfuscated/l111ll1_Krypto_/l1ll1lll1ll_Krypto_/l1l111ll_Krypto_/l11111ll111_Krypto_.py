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
l1l1111_Krypto_ (u"ࠢࠣࠤࡖࡩࡱ࡬࠭ࡵࡧࡶࡸࡸࠦࡦࡰࡴࠣࠬࡸࡵ࡭ࡦࠢࡲࡪ࠮ࠦࡃࡳࡻࡳࡸࡴ࠴ࡕࡵ࡫࡯࠲ࡳࡻ࡭ࡣࡧࡵࠦࠧࠨ᧺")
__revision__ = l1l1111_Krypto_ (u"ࠣࠦࡌࡨࠩࠨ᧻")
import sys as l1l11l11_Krypto_
if l1l11l11_Krypto_.version_info[0] == 2 and l1l11l11_Krypto_.version_info[1] == 1:
    from l111ll1_Krypto_.l1l111ll_Krypto_.l1l1ll1l_Krypto_ import *
import unittest as l1lll111111_Krypto_
class l11111l111l_Krypto_(l1lll111111_Krypto_.TestCase):
    def setUp(self):
        global l111l1ll_Krypto_, l1l1l1ll1l_Krypto_
        from l111ll1_Krypto_.l1l111ll_Krypto_ import l111l1ll_Krypto_
        import math as l1l1l1ll1l_Krypto_
    def l11111l1l11_Krypto_(self):
        l1l1111_Krypto_ (u"ࠤ࡚ࠥࠦࡺࡩ࡭࠰ࡱࡹࡲࡨࡥࡳ࠰ࡦࡩ࡮ࡲ࡟ࡴࡪ࡬ࡪࡹࠨࠢࠣ᧼")
        self.assertRaises(AssertionError, l111l1ll_Krypto_.l1llll11lll_Krypto_, -1, 1)
        self.assertRaises(AssertionError, l111l1ll_Krypto_.l1llll11lll_Krypto_, 1, -1)
        self.assertEqual(0, l111l1ll_Krypto_.l1llll11lll_Krypto_(0, 0))
        self.assertEqual(1, l111l1ll_Krypto_.l1llll11lll_Krypto_(1, 0))
        self.assertEqual(2, l111l1ll_Krypto_.l1llll11lll_Krypto_(2, 0))
        self.assertEqual(3, l111l1ll_Krypto_.l1llll11lll_Krypto_(3, 0))
        self.assertEqual(0, l111l1ll_Krypto_.l1llll11lll_Krypto_(0, 1))
        self.assertEqual(1, l111l1ll_Krypto_.l1llll11lll_Krypto_(1, 1))
        self.assertEqual(1, l111l1ll_Krypto_.l1llll11lll_Krypto_(2, 1))
        self.assertEqual(2, l111l1ll_Krypto_.l1llll11lll_Krypto_(3, 1))
        self.assertEqual(0, l111l1ll_Krypto_.l1llll11lll_Krypto_(0, 2))
        self.assertEqual(1, l111l1ll_Krypto_.l1llll11lll_Krypto_(1, 2))
        self.assertEqual(1, l111l1ll_Krypto_.l1llll11lll_Krypto_(2, 2))
        self.assertEqual(1, l111l1ll_Krypto_.l1llll11lll_Krypto_(3, 2))
        self.assertEqual(1, l111l1ll_Krypto_.l1llll11lll_Krypto_(4, 2))
        self.assertEqual(2, l111l1ll_Krypto_.l1llll11lll_Krypto_(5, 2))
        self.assertEqual(2, l111l1ll_Krypto_.l1llll11lll_Krypto_(6, 2))
        self.assertEqual(2, l111l1ll_Krypto_.l1llll11lll_Krypto_(7, 2))
        self.assertEqual(2, l111l1ll_Krypto_.l1llll11lll_Krypto_(8, 2))
        self.assertEqual(3, l111l1ll_Krypto_.l1llll11lll_Krypto_(9, 2))
        for b in range(3, 1+129, 3):
            self.assertEqual(0, l111l1ll_Krypto_.l1llll11lll_Krypto_(0, b))
            n = 1
            while n <= 2**(b+2):
                (q, r) = divmod(n-1, 2**b)
                expected = q + int(not not r)
                self.assertEqual((n-1, b, expected),
                                 (n-1, b, l111l1ll_Krypto_.l1llll11lll_Krypto_(n-1, b)))
                (q, r) = divmod(n, 2**b)
                expected = q + int(not not r)
                self.assertEqual((n, b, expected),
                                 (n, b, l111l1ll_Krypto_.l1llll11lll_Krypto_(n, b)))
                (q, r) = divmod(n+1, 2**b)
                expected = q + int(not not r)
                self.assertEqual((n+1, b, expected),
                                 (n+1, b, l111l1ll_Krypto_.l1llll11lll_Krypto_(n+1, b)))
                n *= 2
    def l11111l1lll_Krypto_(self):
        l1l1111_Krypto_ (u"࡛ࠥࠦࠧࡴࡪ࡮࠱ࡲࡺࡳࡢࡦࡴ࠱ࡧࡪ࡯࡬ࡠࡦ࡬ࡺࠧࠨࠢ᧽")
        self.assertRaises(TypeError, l111l1ll_Krypto_.l1ll11111_Krypto_, l1l1111_Krypto_ (u"ࠦ࠶ࠨ᧾"), 1)
        self.assertRaises(ZeroDivisionError, l111l1ll_Krypto_.l1ll11111_Krypto_, 1, 0)
        self.assertRaises(ZeroDivisionError, l111l1ll_Krypto_.l1ll11111_Krypto_, -1, 0)
        self.assertEqual(0, l111l1ll_Krypto_.l1ll11111_Krypto_(0, -1))
        self.assertEqual(-1, l111l1ll_Krypto_.l1ll11111_Krypto_(1, -1))
        self.assertEqual(-2, l111l1ll_Krypto_.l1ll11111_Krypto_(2, -1))
        self.assertEqual(-3, l111l1ll_Krypto_.l1ll11111_Krypto_(3, -1))
        self.assertEqual(0, l111l1ll_Krypto_.l1ll11111_Krypto_(0, 1))
        self.assertEqual(1, l111l1ll_Krypto_.l1ll11111_Krypto_(1, 1))
        self.assertEqual(2, l111l1ll_Krypto_.l1ll11111_Krypto_(2, 1))
        self.assertEqual(3, l111l1ll_Krypto_.l1ll11111_Krypto_(3, 1))
        self.assertEqual(0, l111l1ll_Krypto_.l1ll11111_Krypto_(0, 2))
        self.assertEqual(1, l111l1ll_Krypto_.l1ll11111_Krypto_(1, 2))
        self.assertEqual(1, l111l1ll_Krypto_.l1ll11111_Krypto_(2, 2))
        self.assertEqual(2, l111l1ll_Krypto_.l1ll11111_Krypto_(3, 2))
        self.assertEqual(2, l111l1ll_Krypto_.l1ll11111_Krypto_(4, 2))
        self.assertEqual(3, l111l1ll_Krypto_.l1ll11111_Krypto_(5, 2))
        self.assertEqual(0, l111l1ll_Krypto_.l1ll11111_Krypto_(0, 3))
        self.assertEqual(1, l111l1ll_Krypto_.l1ll11111_Krypto_(1, 3))
        self.assertEqual(1, l111l1ll_Krypto_.l1ll11111_Krypto_(2, 3))
        self.assertEqual(1, l111l1ll_Krypto_.l1ll11111_Krypto_(3, 3))
        self.assertEqual(2, l111l1ll_Krypto_.l1ll11111_Krypto_(4, 3))
        self.assertEqual(2, l111l1ll_Krypto_.l1ll11111_Krypto_(5, 3))
        self.assertEqual(2, l111l1ll_Krypto_.l1ll11111_Krypto_(6, 3))
        self.assertEqual(3, l111l1ll_Krypto_.l1ll11111_Krypto_(7, 3))
        self.assertEqual(0, l111l1ll_Krypto_.l1ll11111_Krypto_(0, 4))
        self.assertEqual(1, l111l1ll_Krypto_.l1ll11111_Krypto_(1, 4))
        self.assertEqual(1, l111l1ll_Krypto_.l1ll11111_Krypto_(2, 4))
        self.assertEqual(1, l111l1ll_Krypto_.l1ll11111_Krypto_(3, 4))
        self.assertEqual(1, l111l1ll_Krypto_.l1ll11111_Krypto_(4, 4))
        self.assertEqual(2, l111l1ll_Krypto_.l1ll11111_Krypto_(5, 4))
        self.assertEqual(2, l111l1ll_Krypto_.l1ll11111_Krypto_(6, 4))
        self.assertEqual(2, l111l1ll_Krypto_.l1ll11111_Krypto_(7, 4))
        self.assertEqual(2, l111l1ll_Krypto_.l1ll11111_Krypto_(8, 4))
        self.assertEqual(3, l111l1ll_Krypto_.l1ll11111_Krypto_(9, 4))
        self.assertEqual(3, l111l1ll_Krypto_.l1ll11111_Krypto_(-9, -4))
        self.assertEqual(2, l111l1ll_Krypto_.l1ll11111_Krypto_(-8, -4))
        self.assertEqual(2, l111l1ll_Krypto_.l1ll11111_Krypto_(-7, -4))
        self.assertEqual(2, l111l1ll_Krypto_.l1ll11111_Krypto_(-6, -4))
        self.assertEqual(2, l111l1ll_Krypto_.l1ll11111_Krypto_(-5, -4))
        self.assertEqual(1, l111l1ll_Krypto_.l1ll11111_Krypto_(-4, -4))
        self.assertEqual(1, l111l1ll_Krypto_.l1ll11111_Krypto_(-3, -4))
        self.assertEqual(1, l111l1ll_Krypto_.l1ll11111_Krypto_(-2, -4))
        self.assertEqual(1, l111l1ll_Krypto_.l1ll11111_Krypto_(-1, -4))
        self.assertEqual(0, l111l1ll_Krypto_.l1ll11111_Krypto_(0, -4))
        self.assertEqual(0, l111l1ll_Krypto_.l1ll11111_Krypto_(1, -4))
        self.assertEqual(0, l111l1ll_Krypto_.l1ll11111_Krypto_(2, -4))
        self.assertEqual(0, l111l1ll_Krypto_.l1ll11111_Krypto_(3, -4))
        self.assertEqual(-1, l111l1ll_Krypto_.l1ll11111_Krypto_(4, -4))
        self.assertEqual(-1, l111l1ll_Krypto_.l1ll11111_Krypto_(5, -4))
        self.assertEqual(-1, l111l1ll_Krypto_.l1ll11111_Krypto_(6, -4))
        self.assertEqual(-1, l111l1ll_Krypto_.l1ll11111_Krypto_(7, -4))
        self.assertEqual(-2, l111l1ll_Krypto_.l1ll11111_Krypto_(8, -4))
        self.assertEqual(-2, l111l1ll_Krypto_.l1ll11111_Krypto_(9, -4))
    def l11111ll11l_Krypto_(self):
        l1l1111_Krypto_ (u"ࠧࠨࠢࡖࡶ࡬ࡰ࠳ࡴࡵ࡮ࡤࡨࡶ࠳࡫ࡸࡢࡥࡷࡣࡱࡵࡧ࠳ࠤࠥࠦ᧿")
        self.assertRaises(TypeError, l111l1ll_Krypto_.l1llll11l1l_Krypto_, l1l1111_Krypto_ (u"ࠨ࠰ࠣᨀ"))
        self.assertRaises(ValueError, l111l1ll_Krypto_.l1llll11l1l_Krypto_, -1)
        self.assertRaises(ValueError, l111l1ll_Krypto_.l1llll11l1l_Krypto_, 0)
        self.assertEqual(0, l111l1ll_Krypto_.l1llll11l1l_Krypto_(1))
        self.assertEqual(1, l111l1ll_Krypto_.l1llll11l1l_Krypto_(2))
        self.assertRaises(ValueError, l111l1ll_Krypto_.l1llll11l1l_Krypto_, 3)
        self.assertEqual(2, l111l1ll_Krypto_.l1llll11l1l_Krypto_(4))
        self.assertRaises(ValueError, l111l1ll_Krypto_.l1llll11l1l_Krypto_, 5)
        self.assertRaises(ValueError, l111l1ll_Krypto_.l1llll11l1l_Krypto_, 6)
        self.assertRaises(ValueError, l111l1ll_Krypto_.l1llll11l1l_Krypto_, 7)
        e = 3
        n = 8
        while e < 16:
            if n == 2**e:
                self.assertEqual(e, l111l1ll_Krypto_.l1llll11l1l_Krypto_(n), l1l1111_Krypto_ (u"ࠢࡦࡺࡳࡩࡨࡺࡥࡥ࠿࠵࠮࠯ࠫࡤ࠭ࠢࡱࡁࠪࡪࠢᨁ") % (e, n))
                e += 1
            else:
                self.assertRaises(ValueError, l111l1ll_Krypto_.l1llll11l1l_Krypto_, n)
            n += 1
        for e in range(16, 1+64, 2):
            self.assertRaises(ValueError, l111l1ll_Krypto_.l1llll11l1l_Krypto_, 2**e-1)
            self.assertEqual(e, l111l1ll_Krypto_.l1llll11l1l_Krypto_(2**e))
            self.assertRaises(ValueError, l111l1ll_Krypto_.l1llll11l1l_Krypto_, 2**e+1)
    def l11111l1l1l_Krypto_(self):
        l1l1111_Krypto_ (u"ࠣࠤ࡙ࠥࡹ࡯࡬࠯ࡰࡸࡱࡧ࡫ࡲ࠯ࡧࡻࡥࡨࡺ࡟ࡥ࡫ࡹࠦࠧࠨᨂ")
        self.assertEqual(1, l111l1ll_Krypto_.l1llll1l11l_Krypto_(1, 1))
        self.assertRaises(ValueError, l111l1ll_Krypto_.l1llll1l11l_Krypto_, 1, 2)
        self.assertEqual(1, l111l1ll_Krypto_.l1llll1l11l_Krypto_(2, 2))
        self.assertRaises(ValueError, l111l1ll_Krypto_.l1llll1l11l_Krypto_, 3, 2)
        self.assertEqual(2, l111l1ll_Krypto_.l1llll1l11l_Krypto_(4, 2))
        self.assertEqual(-1, l111l1ll_Krypto_.l1llll1l11l_Krypto_(-1, 1))
        self.assertEqual(-1, l111l1ll_Krypto_.l1llll1l11l_Krypto_(1, -1))
        self.assertRaises(ValueError, l111l1ll_Krypto_.l1llll1l11l_Krypto_, -1, 2)
        self.assertEqual(1, l111l1ll_Krypto_.l1llll1l11l_Krypto_(-2, -2))
        self.assertEqual(-2, l111l1ll_Krypto_.l1llll1l11l_Krypto_(-4, 2))
        self.assertEqual(0, l111l1ll_Krypto_.l1llll1l11l_Krypto_(0, 1))
        self.assertEqual(0, l111l1ll_Krypto_.l1llll1l11l_Krypto_(0, 2))
        self.assertRaises(ZeroDivisionError, l111l1ll_Krypto_.l1llll1l11l_Krypto_, 0, 0)
        self.assertRaises(ZeroDivisionError, l111l1ll_Krypto_.l1llll1l11l_Krypto_, 1, 0)
        self.assertEqual(0, l111l1ll_Krypto_.l1llll1l11l_Krypto_(0, 0, l11111ll1ll_Krypto_=True))
        self.assertRaises(ValueError, l111l1ll_Krypto_.l1llll1l11l_Krypto_, 1, 0, l11111ll1ll_Krypto_=True)
    def l11111lll1l_Krypto_(self):
        l1l1111_Krypto_ (u"ࠤ࡚ࠥࠦࡺࡩ࡭࠰ࡱࡹࡲࡨࡥࡳ࠰ࡩࡰࡴࡵࡲࡠࡦ࡬ࡺࠧࠨࠢᨃ")
        self.assertRaises(TypeError, l111l1ll_Krypto_.l11111l11ll_Krypto_, l1l1111_Krypto_ (u"ࠥ࠵ࠧᨄ"), 1)
        for a in range(-10, 10):
            for b in range(-10, 10):
                if b == 0:
                    self.assertRaises(ZeroDivisionError, l111l1ll_Krypto_.l11111l11ll_Krypto_, a, b)
                else:
                    self.assertEqual((a, b, int(l1l1l1ll1l_Krypto_.floor(float(a) / b))),
                                     (a, b, l111l1ll_Krypto_.l11111l11ll_Krypto_(a, b)))
    def l11111llll1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠦࠧࠨࡕࡵ࡫࡯࠲ࡳࡻ࡭ࡣࡧࡵ࠲࡬࡫ࡴࡔࡶࡵࡳࡳ࡭ࡐࡳ࡫ࡰࡩࠧࠨࠢᨅ")
        self.assertRaises(ValueError, l111l1ll_Krypto_.l111ll1lll_Krypto_, 256)
        self.assertRaises(ValueError, l111l1ll_Krypto_.l111ll1lll_Krypto_, 513)
        bits = 512
        x = l111l1ll_Krypto_.l111ll1lll_Krypto_(bits)
        self.assertNotEqual(x % 2, 0)
        self.assertEqual(x > (1 << bits-1)-1, 1)
        self.assertEqual(x < (1 << bits), 1)
        e = 2**16+1
        x = l111l1ll_Krypto_.l111ll1lll_Krypto_(bits, e)
        self.assertEqual(l111l1ll_Krypto_.l11llllll1_Krypto_(x-1, e), 1)
        self.assertNotEqual(x % 2, 0)
        self.assertEqual(x > (1 << bits-1)-1, 1)
        self.assertEqual(x < (1 << bits), 1)
        e = 2**16+2
        x = l111l1ll_Krypto_.l111ll1lll_Krypto_(bits, e)
        self.assertEqual(l111l1ll_Krypto_.l11llllll1_Krypto_((x-1)>>1, e), 1)
        self.assertNotEqual(x % 2, 0)
        self.assertEqual(x > (1 << bits-1)-1, 1)
        self.assertEqual(x < (1 << bits), 1)
    def l11111l1ll1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠧࠨࠢࡖࡶ࡬ࡰ࠳ࡴࡵ࡮ࡤࡨࡶ࠳࡯ࡳࡑࡴ࡬ࡱࡪࠨࠢࠣᨆ")
        self.assertEqual(l111l1ll_Krypto_.l11lll1l1l_Krypto_(-3), False)
        self.assertEqual(l111l1ll_Krypto_.l11lll1l1l_Krypto_(-2), False)
        self.assertEqual(l111l1ll_Krypto_.l11lll1l1l_Krypto_(1), False)
        self.assertEqual(l111l1ll_Krypto_.l11lll1l1l_Krypto_(2), True)
        self.assertEqual(l111l1ll_Krypto_.l11lll1l1l_Krypto_(3), True)
        self.assertEqual(l111l1ll_Krypto_.l11lll1l1l_Krypto_(4), False)
        self.assertEqual(l111l1ll_Krypto_.l11lll1l1l_Krypto_(2**1279-1), True)
        self.assertEqual(l111l1ll_Krypto_.l11lll1l1l_Krypto_(-(2**1279-1)), False)
        for l11111ll1l1_Krypto_ in (43 * 127 * 211, 61 * 151 * 211, 15259 * 30517,
                          346141 * 692281, 1007119 * 2014237, 3589477 * 7178953,
                          4859419 * 9718837, 2730439 * 5460877,
                          245127919 * 490255837, 963939391 * 1927878781,
                          4186358431 * 8372716861, 1576820467 * 3153640933):
            self.assertEqual(l111l1ll_Krypto_.l11lll1l1l_Krypto_(int(l11111ll1l1_Krypto_)), False)
    def l11111l11l1_Krypto_(self):
        self.assertEqual(l111l1ll_Krypto_.size(2),2)
        self.assertEqual(l111l1ll_Krypto_.size(3),2)
        self.assertEqual(l111l1ll_Krypto_.size(0xa2),8)
        self.assertEqual(l111l1ll_Krypto_.size(0xa2ba40),8*3)
        self.assertEqual(l111l1ll_Krypto_.size(0xa2ba40ee07e3b2bd2f02ce227f36a195024486e49c19cb41bbbdfbba98b22b0e577c2eeaffa20d883a76e65e394c69d4b3c05a1e8fadda27edb2a42bc000fe888b9b32c22d15add0cd76b3e7936e19955b220dd17d4ea904b1ec102b2e4de7751222aa99151024c7cb41cc5ea21d00eeb41f7c800834d2c6e06bce3bce7ea9a5), 1024)
    def l11111lll11_Krypto_(self):
        l1l1111_Krypto_ (u"ࠨࠢࠣࡖࡨࡷࡹࠦࡴࡩࡣࡷࠤࡲࡶࡺࡕࡱࡏࡳࡳ࡭ࡏࡣ࡬ࠣࡥࡳࡪࠠ࡭ࡱࡱ࡫ࡔࡨࡪࡕࡱࡐࡔ࡟ࠦࠨࡪࡰࡷࡩࡷࡴࡡ࡭ࠢࡩࡹࡳࡩࡴࡪࡱࡱࡷ࠮ࠦࡲࡰࡷࡱࡨࡹࡸࡩࡱࠢࡱࡩ࡬ࡧࡴࡪࡸࡨࠤࡳࡻ࡭ࡣࡧࡵࡷࠥࡩ࡯ࡳࡴࡨࡧࡹࡲࡹ࠯ࠤࠥࠦᨇ")
        n = -100000000000000000000000000000000000
        e = 2
        k = l111l1ll_Krypto_._1l11ll111_Krypto_.l11l11lll1_Krypto_(n, e)
        self.assertEqual(n, k.n)
        self.assertEqual(e, k.e)
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l1ll1lllll1_Krypto_ import l1lll1111l1_Krypto_
    return l1lll1111l1_Krypto_(l11111l111l_Krypto_)
if __name__ == l1l1111_Krypto_ (u"ࠧࡠࡡࡰࡥ࡮ࡴ࡟ࡠࠩᨈ"):
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧᨉ"))