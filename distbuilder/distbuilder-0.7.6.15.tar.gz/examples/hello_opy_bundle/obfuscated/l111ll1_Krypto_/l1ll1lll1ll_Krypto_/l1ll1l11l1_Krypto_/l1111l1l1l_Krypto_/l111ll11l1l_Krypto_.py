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
l1l1111_Krypto_ (u"ࠣࠤࠥࡗࡪࡲࡦ࠮ࡶࡨࡷࡹࡹࠠࡧࡱࡵࠤࡈࡸࡹࡱࡶࡲ࠲ࡗࡧ࡮ࡥࡱࡰ࠲ࡋࡵࡲࡵࡷࡱࡥ࠳ࡌ࡯ࡳࡶࡸࡲࡦࡇࡣࡤࡷࡰࡹࡱࡧࡴࡰࡴࠥࠦࠧᣀ")
__revision__ = l1l1111_Krypto_ (u"ࠤࠧࡍࡩࠪࠢᣁ")
import sys as l1l11l11_Krypto_
if l1l11l11_Krypto_.version_info[0] == 2 and l1l11l11_Krypto_.version_info[1] == 1:
    from l111ll1_Krypto_.l1l111ll_Krypto_.l1l1ll1l_Krypto_ import *
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
import unittest as l1lll111111_Krypto_
from binascii import b2a_hex as l1llll1l1l1_Krypto_
class l111ll11ll1_Krypto_(l1lll111111_Krypto_.TestCase):
    def setUp(self):
        global l11111lll1_Krypto_
        from l111ll1_Krypto_.l1ll1l11l1_Krypto_.l1111l1l1l_Krypto_ import l11111lll1_Krypto_
    def l111ll111ll_Krypto_(self):
        l1l1111_Krypto_ (u"ࠥࠦࠧࡌ࡯ࡳࡶࡸࡲࡦࡇࡣࡤࡷࡰࡹࡱࡧࡴࡰࡴ࠱ࡊࡴࡸࡴࡶࡰࡤࡔࡴࡵ࡬ࠣࠤࠥᣂ")
        l111ll1ll1l_Krypto_ = l11111lll1_Krypto_.l1lllll1l11_Krypto_()
        self.assertEqual(0, l111ll1ll1l_Krypto_.length)
        self.assertEqual(l1l1111_Krypto_ (u"ࠦ࠺ࡪࡦ࠷ࡧ࠳ࡩ࠷࠽࠶࠲࠵࠸࠽ࡩ࠹࠰ࡢ࠺࠵࠻࠺࠶࠵࠹ࡧ࠵࠽࠾࡬ࡣࡤ࠲࠶࠼࠶࠻࠳࠵࠷࠷࠹࡫࠻࠵ࡤࡨ࠷࠷ࡪ࠺࠱࠺࠺࠶ࡪ࠺ࡪ࠴ࡤ࠻࠷࠹࠻ࠨᣃ"), l111ll1ll1l_Krypto_.hexdigest())
        l111ll1ll1l_Krypto_.append(b(l1l1111_Krypto_ (u"ࠬࡧࡢࡤࠩᣄ")))
        self.assertEqual(3, l111ll1ll1l_Krypto_.length)
        self.assertEqual(l1l1111_Krypto_ (u"ࠨ࠴ࡧ࠺ࡥ࠸࠷ࡩ࠲࠳ࡦࡧ࠷࠼࠸࠹ࡣ࠷࠴࠽ࡧࡧ࠶ࡧ࠸࠻ࡨ࠷ࡪࡡ࠸ࡥࡦ࠹ࡧ࠸ࡤ࠷࠲࠹ࡨ࠵࠻ࡤࡢࡧࡧ࠹ࡦࡪ࠵࠲࠴࠻ࡧࡨ࠶࠳ࡦ࠸ࡦ࠺࠸࠻࠸ࠣᣅ"), l111ll1ll1l_Krypto_.hexdigest())
        l111ll1ll1l_Krypto_.append(b(l1l1111_Krypto_ (u"ࠢࡥࡤࡦࡨࡪࡩࡤࡦࡨࡧࡩ࡫࡭ࡥࡧࡩ࡫ࡪ࡬࡮ࡩࡨࡪ࡬࡮࡭࡯ࡪ࡬࡫࡭࡯ࡱࡰ࡫࡭࡯࡮ࡰࡲࡴ࡬࡮ࡰࡲࡱࡳࡵࡰ࡯ࡱࡳࡵࠧᣆ")))
        self.assertEqual(56, l111ll1ll1l_Krypto_.length)
        self.assertEqual(b(l1l1111_Krypto_ (u"ࠨ࠲ࡦࡪ࡫࡫࠱࠸ࡨ࠹࠼࠾࠻࠴ࡥࡣࡦ࠷ࡦ࠾࠴ࡧࡤ࠴࠸࠺࠾ࡢࡥ࠷ࡨࡧ࠾࠿࠲࠱࠻࠷࠸࠾࠽࠴࠺ࡤ࠵ࡦ࠸࠶࠸ࡣ࠹ࡦࡦ࠺࠻࠸࠲࠴ࡩ࠽࠺࠼࠳ࡢࡨࠪᣇ")), l1llll1l1l1_Krypto_(l111ll1ll1l_Krypto_.digest()))
        l111ll1ll1l_Krypto_.reset()
        self.assertEqual(0, l111ll1ll1l_Krypto_.length)
        l111ll1ll1l_Krypto_.append(b(l1l1111_Krypto_ (u"ࠩࡤࠫᣈ")) * 10**6)
        self.assertEqual(10**6, l111ll1ll1l_Krypto_.length)
        self.assertEqual(b(l1l1111_Krypto_ (u"ࠪ࠼࠵ࡪ࠱࠲࠺࠼࠸࠼࠽࠵࠷࠵ࡨ࠵ࡧ࠻࠲࠱࠸ࡥ࠶࠼࠺࠹ࡧ࠳ࡤࡪࡪ࠺࠸࠱࠹ࡨ࠹࠼࠶࠵ࡦ࠺ࡥࡨ࠼࠽࠸࠹࠹ࡤ࠺࠵࠷࠸࠸ࡣ࠺࠵࠷࠷࠵࠷࠸࠻࠼ࠬᣉ")), l1llll1l1l1_Krypto_(l111ll1ll1l_Krypto_.digest()))
    def l111ll1l111_Krypto_(self):
        l1l1111_Krypto_ (u"ࠦࠧࠨࡆࡰࡴࡷࡹࡳࡧࡁࡤࡥࡸࡱࡺࡲࡡࡵࡱࡵ࠲ࡼ࡮ࡩࡤࡪࡢࡴࡴࡵ࡬ࡴࠤࠥࠦᣊ")
        self.assertRaises(AssertionError, l11111lll1_Krypto_.l1llll1l1ll_Krypto_, 0)
        self.assertEqual(l11111lll1_Krypto_.l1llll1l1ll_Krypto_(1), [0])
        self.assertEqual(l11111lll1_Krypto_.l1llll1l1ll_Krypto_(2), [0, 1])
        self.assertEqual(l11111lll1_Krypto_.l1llll1l1ll_Krypto_(3), [0])
        self.assertEqual(l11111lll1_Krypto_.l1llll1l1ll_Krypto_(4), [0, 1, 2])
        self.assertEqual(l11111lll1_Krypto_.l1llll1l1ll_Krypto_(5), [0])
        self.assertEqual(l11111lll1_Krypto_.l1llll1l1ll_Krypto_(6), [0, 1])
        self.assertEqual(l11111lll1_Krypto_.l1llll1l1ll_Krypto_(7), [0])
        self.assertEqual(l11111lll1_Krypto_.l1llll1l1ll_Krypto_(8), [0, 1, 2, 3])
        for i in range(1, 32):
            self.assertEqual(l11111lll1_Krypto_.l1llll1l1ll_Krypto_(2**i-1), [0])
            self.assertEqual(l11111lll1_Krypto_.l1llll1l1ll_Krypto_(2**i), list(range(i+1)))
            self.assertEqual(l11111lll1_Krypto_.l1llll1l1ll_Krypto_(2**i+1), [0])
        self.assertEqual(l11111lll1_Krypto_.l1llll1l1ll_Krypto_(2**31), list(range(32)))
        self.assertEqual(l11111lll1_Krypto_.l1llll1l1ll_Krypto_(2**32), list(range(32)))
        self.assertEqual(l11111lll1_Krypto_.l1llll1l1ll_Krypto_(2**33), list(range(32)))
        self.assertEqual(l11111lll1_Krypto_.l1llll1l1ll_Krypto_(2**34), list(range(32)))
        self.assertEqual(l11111lll1_Krypto_.l1llll1l1ll_Krypto_(2**35), list(range(32)))
        self.assertEqual(l11111lll1_Krypto_.l1llll1l1ll_Krypto_(2**36), list(range(32)))
        self.assertEqual(l11111lll1_Krypto_.l1llll1l1ll_Krypto_(2**64), list(range(32)))
        self.assertEqual(l11111lll1_Krypto_.l1llll1l1ll_Krypto_(2**128), list(range(32)))
    def l111ll111l1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠧࠨࠢࡇࡱࡵࡸࡺࡴࡡࡂࡥࡦࡹࡲࡻ࡬ࡢࡶࡲࡶ࠳ࡌ࡯ࡳࡶࡸࡲࡦࡇࡣࡤࡷࡰࡹࡱࡧࡴࡰࡴࠥࠦࠧᣋ")
        l111ll11lll_Krypto_ = l11111lll1_Krypto_.l11111lll1_Krypto_()
        self.assertRaises(AssertionError, l111ll11lll_Krypto_.l111111ll1_Krypto_, 1)
        for p in range(32):
            l111ll11lll_Krypto_.l1111l1lll_Krypto_(42, p, b(l1l1111_Krypto_ (u"ࠨࡘࠣᣌ")) * 32)
            self.assertEqual(32+2, l111ll11lll_Krypto_.l1llllll11l_Krypto_[p].length)
        self.assertRaises(AssertionError, l111ll11lll_Krypto_.l111111ll1_Krypto_, 1)
        for p in range(32):
            l111ll11lll_Krypto_.l1111l1lll_Krypto_(42, p, b(l1l1111_Krypto_ (u"࡙ࠢࠤᣍ")) * 32)
            self.assertEqual((32+2)*2, l111ll11lll_Krypto_.l1llllll11l_Krypto_[p].length)
        self.assertEqual(l1l1111_Krypto_ (u"ࠣࡣࡨࡪ࠹࠸ࡡ࠶ࡦࡦࡦࡩࡪࡡࡣ࠸࠺ࡩ࠽࡫ࡦࡢ࠳࠴࠼ࡪ࠷ࡢ࠵࠹ࡩࡨࡪ࠻ࡤ࠷࠻࠺ࡪ࠽࠿ࡢࡦࡤ࠼࠻࠶ࡨ࠹࠺ࡧ࠹ࡩ࠽࡫࠵ࡦ࠺࠼ࡪࡧ࡬࠰࠷࠶ࠥᣎ"),
            l111ll11lll_Krypto_.l1llllll11l_Krypto_[0].hexdigest())
        self.assertEqual(None, l111ll11lll_Krypto_.generator.key)
        self.assertEqual(0, l111ll11lll_Krypto_.generator.l1lll1llll1_Krypto_.l111ll1111l_Krypto_())
        result = l111ll11lll_Krypto_.l111111ll1_Krypto_(32)
        self.assertEqual(b(l1l1111_Krypto_ (u"ࠤࡥ࠻ࡧ࠾࠶ࡣࡦ࠼ࡥ࠷࠽ࡤ࠺࠸ࡧ࠻ࡧࡨ࠴ࡢࡦࡧ࠵ࡧ࠼ࡢ࠲࠲ࡧ࠵࠺࠽ࠢᣏ") l1l1111_Krypto_ (u"ࠥ࠶࠸࠻࠰ࡣ࠳ࡦ࠺࠶࠸࠵࠴ࡦࡥ࠶࡫࠾ࡤࡢ࠴࠶࠷ࡧ࡫࠷࠳࠸ࡧࡧ࠶࠻ࡦࠣᣐ")), l1llll1l1l1_Krypto_(result))
        self.assertEqual(b(l1l1111_Krypto_ (u"ࠦ࡫࠸࠳ࡢࡦ࠺࠸࠾࡬࠳࠴࠲࠹࠺࡫࡬࠵࠴ࡦ࠶࠴࠼࠿࠱࠵ࡨࡥࡪ࠺ࡨ࠲࠲ࡦࡤ࠽࠻࠼࠷ࡤ࠹ࡨ࠼࠻ࡨࡡ࠳࠶࠺࠺࠺࠻ࡣ࠺࠶࠼࠴ࡪ࠿ࡤ࠺࠶ࡤ࠻ࡨࠨᣑ")), l1llll1l1l1_Krypto_(l111ll11lll_Krypto_.generator.key))
        self.assertEqual(5, l111ll11lll_Krypto_.generator.l1lll1llll1_Krypto_.l111ll1111l_Krypto_())
    def l111ll11l11_Krypto_(self):
        l1l1111_Krypto_ (u"ࠧࠨࠢࡇࡱࡵࡸࡺࡴࡡࡂࡥࡦࡹࡲࡻ࡬ࡢࡶࡲࡶ࠳ࡌ࡯ࡳࡶࡸࡲࡦࡇࡣࡤࡷࡰࡹࡱࡧࡴࡰࡴࠣࡱ࡮ࡴࡩ࡮ࡷࡰࠤࡵࡵ࡯࡭ࠢ࡯ࡩࡳ࡭ࡴࡩࠤࠥࠦᣒ")
        l111ll11lll_Krypto_ = l11111lll1_Krypto_.l11111lll1_Krypto_()
        self.assertEqual(l111ll11lll_Krypto_.l1llll1lll1_Krypto_, 64)
        self.assertRaises(AssertionError, l111ll11lll_Krypto_.l111111ll1_Krypto_, 1)
        for i in range(15):
            for p in range(32):
                l111ll11lll_Krypto_.l1111l1lll_Krypto_(2, p, b(l1l1111_Krypto_ (u"ࠨࡘ࡙ࠤᣓ")))
                self.assertRaises(AssertionError, l111ll11lll_Krypto_.l111111ll1_Krypto_, 1)
        l111ll11lll_Krypto_.l1111l1lll_Krypto_(2, 0, b(l1l1111_Krypto_ (u"࡙࡚ࠢࠥᣔ")))
        l111ll11lll_Krypto_.l111111ll1_Krypto_(1)
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l1ll1lllll1_Krypto_ import l1lll1111l1_Krypto_
    return l1lll1111l1_Krypto_(l111ll11ll1_Krypto_)
if __name__ == l1l1111_Krypto_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪᣕ"):
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"ࠩࡶࡹ࡮ࡺࡥࠨᣖ"))