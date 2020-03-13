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
l1l1111_Krypto_ (u"࡙ࠥࠦࠧࡥ࡭ࡨ࠰ࡸࡪࡹࡴࡴࠢࡩࡳࡷࠦࡃࡳࡻࡳࡸࡴ࠴ࡒࡢࡰࡧࡳࡲ࠴ࡆࡰࡴࡷࡹࡳࡧ࠮ࡇࡱࡵࡸࡺࡴࡡࡈࡧࡱࡩࡷࡧࡴࡰࡴࠥࠦࠧᣗ")
__revision__ = l1l1111_Krypto_ (u"ࠦࠩࡏࡤࠥࠤᣘ")
import sys as l1l11l11_Krypto_
if l1l11l11_Krypto_.version_info[0] == 2 and l1l11l11_Krypto_.version_info[1] == 1:
    from l111ll1_Krypto_.l1l111ll_Krypto_.l1l1ll1l_Krypto_ import *
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
import unittest as l1lll111111_Krypto_
from binascii import b2a_hex as l1llll1l1l1_Krypto_
class l111l1llll1_Krypto_(l1lll111111_Krypto_.TestCase):
    def setUp(self):
        global l1llllll1ll_Krypto_
        from l111ll1_Krypto_.l1ll1l11l1_Krypto_.l1111l1l1l_Krypto_ import l1llllll1ll_Krypto_
    def l111l1lll1l_Krypto_(self):
        l1l1111_Krypto_ (u"ࠧࠨࠢࡇࡱࡵࡸࡺࡴࡡࡈࡧࡱࡩࡷࡧࡴࡰࡴ࠱ࡅࡊ࡙ࡇࡦࡰࡨࡶࡦࡺ࡯ࡳࠤࠥࠦᣙ")
        l111l1lllll_Krypto_ = l1llllll1ll_Krypto_.l1llll1ll11_Krypto_()
        self.assertRaises(Exception, l111l1lllll_Krypto_.l1llll1llll_Krypto_, 1)
        self.assertEqual(0, l111l1lllll_Krypto_.l1lll1llll1_Krypto_.l111ll1111l_Krypto_())
        l111l1lllll_Krypto_.l1lllll111l_Krypto_(b(l1l1111_Krypto_ (u"ࠨࡈࡦ࡮࡯ࡳࠧᣚ")))
        self.assertEqual(b(l1l1111_Krypto_ (u"ࠢ࠱ࡧࡤ࠺࠾࠷࠹ࡥ࠶࠶࠺࠶࠻࠵࠲࠵࠹࠸࠷࠺࠲ࡢ࠶ࡥࡥ࠽࠿࠰ࡧ࠺ࡩ࠴࠼࠹࠶࠸࠸ࡨ࠼࠷ࡩࡦ࠲ࡣ࠸࠶ࡧࡨ࠸࠹࠲ࡩ࠻ࡪ࠺࠹࠷࠸࠷࠼ࡧ࠻࠶࠶ࠤᣛ")), l1llll1l1l1_Krypto_(l111l1lllll_Krypto_.key))
        self.assertEqual(1, l111l1lllll_Krypto_.l1lll1llll1_Krypto_.l111ll1111l_Krypto_())
        self.assertEqual(b(l1l1111_Krypto_ (u"ࠣ࠹ࡦࡦࡪ࠸ࡣ࠲࠹࠹࠼࠹ࡧࡣ࠳࠴࠶ࡨ࠵࠾࠹࠷࠻ࡨࡩ࠽ࡨ࠵࠷࠷࠹࠵࠻ࠨᣜ")) +
                         b(l1l1111_Krypto_ (u"ࠤ࠺࠵࠼࠼࠶࠲ࡥ࠳ࡨ࠷࡬࠴࠸࠷࠻ࡦࡩ࠼ࡢࡢ࠳࠷࠴ࡧ࡬࠳࠸࠻࠴ࡥࡧࡪࠢᣝ")),
            l1llll1l1l1_Krypto_(l111l1lllll_Krypto_.l1llll1llll_Krypto_(32)))
        self.assertEqual(b(l1l1111_Krypto_ (u"ࠥ࠷࠸ࡧ࠱ࡣࡤ࠵࠵࠾࠾࠷࠹࠷࠼ࡧࡦ࡬࠲ࡣࡤࡩࡧ࠺࠼࠱࠶ࡤࡨࡪ࠺࠼ࡤࠣᣞ")) +
                         b(l1l1111_Krypto_ (u"ࠦࡪ࠼ࡢ࠸࠳ࡩࡪ࠾࡬࠳࠸࠳࠴࠶ࡩ࠶ࡣ࠲࠻࠶ࡥ࠶࠹࠵࠲࠸࠳࠼࠻࠸ࡢ࠸ࠤᣟ")),
            l1llll1l1l1_Krypto_(l111l1lllll_Krypto_.key))
        self.assertEqual(5, l111l1lllll_Krypto_.l1lll1llll1_Krypto_.l111ll1111l_Krypto_())
        self.assertEqual(b(l1l1111_Krypto_ (u"ࠧ࡬ࡤ࠷࠸࠷࠼ࡧࡧ࠳࠱࠺࠹ࡩ࠾࠷࠹ࡤࡧࡨ࠷࠹࠿࠰࠵ࡧࡩ࠴࠾ࡧ࠷ࡧࡨࠥᣠ")) +
                         b(l1l1111_Krypto_ (u"ࠨ࠰࠳࠳ࡩ࠻࠼࠻࠸࠱࠷࠸࠼ࡧ࠾ࡣ࠴ࡧ࠼࠶࠹࠾࠲࠸࠷ࡩ࠶࠸࠶࠴࠳ࡤࡩࠦᣡ")),
            l1llll1l1l1_Krypto_(l111l1lllll_Krypto_.l1llll1llll_Krypto_(32)))
        self.assertRaises(AssertionError, l111l1lllll_Krypto_._1lll1ll1l1_Krypto_, 2**20+1)
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l1ll1lllll1_Krypto_ import l1lll1111l1_Krypto_
    return l1lll1111l1_Krypto_(l111l1llll1_Krypto_)
if __name__ == l1l1111_Krypto_ (u"ࠧࡠࡡࡰࡥ࡮ࡴ࡟ࡠࠩᣢ"):
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧᣣ"))