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
__revision__ = l1l1111_Krypto_ (u"ࠣࠦࡌࡨࠩࠨᝩ")
import unittest as l1lll111111_Krypto_
from binascii import unhexlify as l1l1111111l_Krypto_
from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l1ll1lllll1_Krypto_ import l1lll1111l1_Krypto_
from l111ll1_Krypto_.l1lll1ll1_Krypto_ import l1l111lll_Krypto_ as l1l1l1l1ll_Krypto_,l11111ll1_Krypto_
from l111ll1_Krypto_.l11l1l1lll_Krypto_.l1l1l1l1l1_Krypto_ import *
def l1l1l111lll_Krypto_(t): return l1l1111111l_Krypto_(b(t))
class l1l111111l1_Krypto_(l1lll111111_Krypto_.TestCase):
    _1l1l1111ll_Krypto_ = (
            (l1l1111_Krypto_ (u"ࠤࡳࡥࡸࡹࡷࡰࡴࡧࠦᝪ"),l1l1111_Krypto_ (u"ࠥ࠻࠽࠻࠷࠹ࡇ࠸ࡅ࠺ࡊ࠶࠴ࡅࡅ࠴࠻ࠨᝫ"),16,1000,l1l1111_Krypto_ (u"ࠦࡉࡉ࠱࠺࠺࠷࠻ࡊ࠶࠵ࡄ࠸࠷ࡈ࠷ࡌࡁࡇ࠳࠳ࡉࡇࡌࡂ࠵ࡃ࠶ࡈ࠷ࡇ࠲࠱ࠤᝬ")),
    )
    def l11lllllll1_Krypto_(self):
        v = self._1l1l1111ll_Krypto_[0]
        res = l1l1l1l11l_Krypto_(v[0], l1l1l111lll_Krypto_(v[1]), v[2], v[3], l1l1l1l1ll_Krypto_)
        self.assertEqual(res, l1l1l111lll_Krypto_(v[4]))
class l11llllllll_Krypto_(l1lll111111_Krypto_.TestCase):
    _1l1l1111ll_Krypto_ = (
            (l1l1111_Krypto_ (u"ࠧࡶࡡࡴࡵࡺࡳࡷࡪࠢ᝭"),l1l1111_Krypto_ (u"ࠨ࠷࠹࠷࠺࠼ࡊ࠻ࡁ࠶ࡆ࠹࠷ࡈࡈ࠰࠷ࠤᝮ"),24,2048,l1l1111_Krypto_ (u"ࠢࡃࡈࡇࡉ࠻ࡈࡅ࠺࠶ࡇࡊ࠼ࡋ࠱࠲ࡆࡇ࠸࠵࠿ࡂࡄࡇ࠵࠴ࡆ࠶࠲࠶࠷ࡈࡇ࠸࠸࠷ࡄࡄ࠼࠷࠻ࡌࡆࡆ࠻࠶࠺࠹࠹ࠢᝯ")),
            (l1l1111_Krypto_ (u"ࠣࡲࡤࡷࡸࡽ࡯ࡳࡦࠥᝰ"),l1l1111_Krypto_ (u"ࠤ࠺࠷࠻࠷࠶ࡤ࠹࠷ࠦ᝱"), 20, 1,          l1l1111_Krypto_ (u"ࠥ࠴ࡨ࠼࠰ࡤ࠺࠳ࡪ࠾࠼࠱ࡧ࠲ࡨ࠻࠶࡬࠳ࡢ࠻ࡥ࠹࠷࠺ࡡࡧ࠸࠳࠵࠷࠶࠶࠳ࡨࡨ࠴࠸࠽ࡡ࠷ࠤᝲ")),
            (l1l1111_Krypto_ (u"ࠦࡵࡧࡳࡴࡹࡲࡶࡩࠨᝳ"),l1l1111_Krypto_ (u"ࠧ࠽࠳࠷࠳࠹ࡧ࠼࠺ࠢ᝴"), 20, 2,          l1l1111_Krypto_ (u"ࠨࡥࡢ࠸ࡦ࠴࠶࠺ࡤࡤ࠹࠵ࡨ࠻࡬࠸ࡤࡥࡧ࠵ࡪࡪ࠹࠳ࡣࡦࡩ࠶ࡪ࠴࠲ࡨ࠳ࡨ࠽ࡪࡥ࠹࠻࠸࠻ࠧ᝵")),
            (l1l1111_Krypto_ (u"ࠢࡱࡣࡶࡷࡼࡵࡲࡥࠤ᝶"),l1l1111_Krypto_ (u"ࠣ࠹࠶࠺࠶࠼ࡣ࠸࠶ࠥ᝷"), 20, 4096,       l1l1111_Krypto_ (u"ࠤ࠷ࡦ࠵࠶࠷࠺࠲࠴ࡦ࠼࠼࠵࠵࠺࠼ࡥࡧ࡫ࡡࡥ࠶࠼ࡨ࠾࠸࠶ࡧ࠹࠵࠵ࡩ࠶࠶࠶ࡣ࠷࠶࠾ࡩ࠱ࠣ᝸")),
            (l1l1111_Krypto_ (u"ࠥࡴࡦࡹࡳࡸࡱࡵࡨࡕࡇࡓࡔ࡙ࡒࡖࡉࡶࡡࡴࡵࡺࡳࡷࡪࠢ᝹"),l1l1111_Krypto_ (u"ࠦ࠼࠹࠶࠲࠸ࡦ࠻࠹࠻࠳࠵࠳࠷ࡧ࠺࠺࠷࠴࠸࠴࠺ࡨ࠽࠴࠶࠵࠷࠵࠹ࡩ࠵࠵࠹࠶࠺࠶࠼ࡣ࠸࠶࠸࠷࠹࠷࠴ࡤ࠷࠷࠻࠸࠼࠱࠷ࡥ࠺࠸࠺࠹࠴࠲࠶ࡦ࠹࠹࠽࠳࠷࠳࠹ࡧ࠼࠺ࠢ᝺"),
                                    25, 4096,       l1l1111_Krypto_ (u"ࠧ࠹ࡤ࠳ࡧࡨࡧ࠹࡬ࡥ࠵࠳ࡦ࠼࠹࠿ࡢ࠹࠲ࡦ࠼ࡩ࠾࠳࠷࠸࠵ࡧ࠵࡫࠴࠵ࡣ࠻ࡦ࠷࠿࠱ࡢ࠻࠹࠸ࡨ࡬࠲ࡧ࠲࠺࠴࠸࠾ࠢ᝻")),
            ( l1l1111_Krypto_ (u"࠭ࡰࡢࡵࡶࡠࡽ࠶࠰ࡸࡱࡵࡨࠬ᝼"),l1l1111_Krypto_ (u"ࠢ࠸࠵࠹࠵࠵࠶࠶ࡤ࠹࠷ࠦ᝽"),16,4096,  l1l1111_Krypto_ (u"ࠣ࠷࠹ࡪࡦ࠼ࡡࡢ࠹࠸࠹࠹࠾࠰࠺࠻ࡧࡧࡨ࠹࠷ࡥ࠹ࡩ࠴࠸࠺࠲࠶ࡧ࠳ࡧ࠸ࠨ᝾")),
    )
    def l11lllllll1_Krypto_(self):
        def l1l1l11ll1_Krypto_(p,s):
            return l11111ll1_Krypto_.new(p,s,l1l1l1l1ll_Krypto_).digest()
        for i in range(len(self._1l1l1111ll_Krypto_)):
            v = self._1l1l1111ll_Krypto_[i]
            res  = l1l1l11l11_Krypto_(v[0], l1l1l111lll_Krypto_(v[1]), v[2], v[3])
            l11llllll1l_Krypto_ = l1l1l11l11_Krypto_(v[0], l1l1l111lll_Krypto_(v[1]), v[2], v[3], l1l1l11ll1_Krypto_)
            self.assertEqual(res, l1l1l111lll_Krypto_(v[4]))
            self.assertEqual(res, l11llllll1l_Krypto_)
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    tests = []
    tests += l1lll1111l1_Krypto_(l1l111111l1_Krypto_)
    tests += l1lll1111l1_Krypto_(l11llllllll_Krypto_)
    return tests
if __name__ == l1l1111_Krypto_ (u"ࠩࡢࡣࡲࡧࡩ࡯ࡡࡢࠫ᝿"):
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"ࠪࡷࡺ࡯ࡴࡦࠩក"))