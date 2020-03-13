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
l1l1111_Krypto_ (u"ࠦࠧࠨࡓࡦ࡮ࡩ࠱ࡹ࡫ࡳࡵࠢࡶࡹ࡮ࡺࡥࠡࡨࡲࡶࠥࡉࡲࡺࡲࡷࡳ࠳ࡉࡩࡱࡪࡨࡶ࠳࡞ࡏࡓࠤࠥࠦᘣ")
import unittest as l1lll111111_Krypto_
__revision__ = l1l1111_Krypto_ (u"ࠧࠪࡉࡥࠦࠥᘤ")
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
l1ll11lllll_Krypto_ = [
    (l1l1111_Krypto_ (u"࠭࠰࠲ࠩᘥ"), l1l1111_Krypto_ (u"ࠧ࠱࠳ࠪᘦ"),
        l1l1111_Krypto_ (u"ࠨ࠲࠳ࠫᘧ"),
        l1l1111_Krypto_ (u"ࠩࡽࡩࡷࡵࠠ࡬ࡧࡼࠫᘨ")),
    (l1l1111_Krypto_ (u"ࠪ࠴࠶࠶࠲࠱࠶࠳࠼࠶࠶࠲࠱࠶࠳࠼࠵࠭ᘩ"), l1l1111_Krypto_ (u"ࠫ࠵࠶࠰࠴࠲࠸࠴࠾࠷࠱࠳࠳࠷࠵࠽࠷ࠧᘪ"),
        l1l1111_Krypto_ (u"ࠬ࠶࠱ࠨᘫ"),
        l1l1111_Krypto_ (u"࠭࠱࠮ࡤࡼࡸࡪࠦ࡫ࡦࡻࠪᘬ")),
    (l1l1111_Krypto_ (u"ࠧ࠱࠳࠳࠶࠵࠺࠰࠹࠳࠳࠶࠵࠺࠰࠹࠲ࠪᘭ"), l1l1111_Krypto_ (u"ࠨࡥࡧࡥ࠽ࡩ࠸ࡢ࠴ࡧࡧ࠽ࡧ࠸ࡤ࠴ࡤࠫᘮ"),
        l1l1111_Krypto_ (u"ࠩࡦࡧࡦࡧࠧᘯ"),
        l1l1111_Krypto_ (u"ࠪ࠶࠲ࡨࡹࡵࡧࠣ࡯ࡪࡿࠧᘰ")),
    (l1l1111_Krypto_ (u"ࠫ࡫࡬ࠧᘱ")*64, l1l1111_Krypto_ (u"ࠬ࡬ࡦࡧࡧࡩࡨ࡫ࡩࡦࡣࡨࡤࡪ࠾࡬࠸ࡧ࠹ࡩ࠺࡫࠻ࡦ࠵ࡨ࠶ࡪ࠷࡬࠱ࡧ࠲ࡨࡪࡪ࡫ࡥࡥࡧࡦࡩࡧ࡫ࡡࡦ࠻ࡨ࠼ࡪ࠽ࡥ࠷ࡧ࠸ࡩ࠹࡫࠳ࡦ࠴ࡨ࠵ࡪ࠶ࠧᘲ")*2,
        l1l1111_Krypto_ (u"࠭࠰࠱࠲࠴࠴࠷࠶࠳࠱࠶࠳࠹࠵࠼࠰࠸࠲࠻࠴࠾࠶ࡡ࠱ࡤ࠳ࡧ࠵ࡪ࠰ࡦ࠲ࡩ࠵࠵࠷࠱࠲࠴࠴࠷࠶࠺࠱࠶࠳࠹࠵࠼࠷࠸࠲࠻࠴ࡥ࠶ࡨ࠱ࡤ࠳ࡧ࠵ࡪ࠷ࡦࠨᘳ"),
        l1l1111_Krypto_ (u"ࠧ࠴࠴࠰ࡦࡾࡺࡥࠡ࡭ࡨࡽࠬᘴ")),
]
class l1l11l1l1ll_Krypto_(l1lll111111_Krypto_.TestCase):
    def runTest(self):
        l1l1111_Krypto_ (u"ࠣࠤࠥ࠷࠸࠳ࡢࡺࡶࡨࠤࡰ࡫ࡹࠡࠪࡶ࡬ࡴࡻ࡬ࡥࠢࡵࡥ࡮ࡹࡥࠡࡘࡤࡰࡺ࡫ࡅࡳࡴࡲࡶࠥࡻ࡮ࡥࡧࡵࠤࡨࡻࡲࡳࡧࡱࡸࠥ࡯࡭ࡱ࡮ࡨࡱࡪࡴࡴࡢࡶ࡬ࡳࡳ࠯ࠢࠣࠤᘵ")
        self.assertRaises(ValueError, l1111l1ll_Krypto_.new, l1l1111_Krypto_ (u"ࠤࡻࠦᘶ")*33)
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    global l1111l1ll_Krypto_
    from l111ll1_Krypto_.l11111l_Krypto_ import l1111l1ll_Krypto_
    from .common import l1l1lll1l11_Krypto_
    return l1l1lll1l11_Krypto_(l1111l1ll_Krypto_, l1l1111_Krypto_ (u"ࠥ࡜ࡔࡘࠢᘷ"), l1ll11lllll_Krypto_) + [l1l11l1l1ll_Krypto_()]
if __name__ == l1l1111_Krypto_ (u"ࠫࡤࡥ࡭ࡢ࡫ࡱࡣࡤ࠭ᘸ"):
    import unittest as l1lll111111_Krypto_
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"ࠬࡹࡵࡪࡶࡨࠫᘹ"))