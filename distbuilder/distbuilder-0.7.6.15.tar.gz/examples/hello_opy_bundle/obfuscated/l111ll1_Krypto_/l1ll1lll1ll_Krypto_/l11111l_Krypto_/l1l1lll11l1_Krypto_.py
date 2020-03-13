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
l1l1111_Krypto_ (u"ࠣࠤࠥࡗࡪࡲࡦ࠮ࡶࡨࡷࡹࠦࡳࡶ࡫ࡷࡩࠥ࡬࡯ࡳࠢࡆࡶࡾࡶࡴࡰ࠰ࡆ࡭ࡵ࡮ࡥࡳ࠰ࡆࡅࡘ࡚ࠢࠣࠤፁ")
__revision__ = l1l1111_Krypto_ (u"ࠤࠧࡍࡩࠪࠢፂ")
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
l1ll11lllll_Krypto_ = [
    (l1l1111_Krypto_ (u"ࠪ࠴࠶࠸࠳࠵࠷࠹࠻࠽࠿ࡡࡣࡥࡧࡩ࡫࠭ፃ"), l1l1111_Krypto_ (u"ࠫ࠷࠹࠸ࡣ࠶ࡩࡩ࠺࠾࠴࠸ࡧ࠷࠸ࡧ࠸ࠧፄ"),
        l1l1111_Krypto_ (u"ࠬ࠶࠱࠳࠵࠷࠹࠻࠽࠱࠳࠵࠷࠹࠻࠽࠸࠳࠵࠷࠹࠻࠽࠸࠺࠵࠷࠹࠻࠽࠸࠺ࡣࠪፅ"),
        l1l1111_Krypto_ (u"࠭࠱࠳࠺࠰ࡦ࡮ࡺࠠ࡬ࡧࡼࠫፆ")),
    (l1l1111_Krypto_ (u"ࠧ࠱࠳࠵࠷࠹࠻࠶࠸࠺࠼ࡥࡧࡩࡤࡦࡨࠪፇ"), l1l1111_Krypto_ (u"ࠨࡧࡥ࠺ࡦ࠽࠱࠲ࡣ࠵ࡧ࠵࠸࠲࠸࠳ࡥࠫፈ"),
        l1l1111_Krypto_ (u"ࠩ࠳࠵࠷࠹࠴࠶࠸࠺࠵࠷࠹࠴࠶࠸࠺࠼࠷࠹࠴࠶ࠩፉ"),
        l1l1111_Krypto_ (u"ࠪ࠼࠵࠳ࡢࡪࡶࠣ࡯ࡪࡿࠧፊ")),
    (l1l1111_Krypto_ (u"ࠫ࠵࠷࠲࠴࠶࠸࠺࠼࠾࠹ࡢࡤࡦࡨࡪ࡬ࠧፋ"), l1l1111_Krypto_ (u"ࠬ࠽ࡡࡤ࠺࠴࠺ࡩ࠷࠶ࡦ࠻ࡥ࠷࠵࠸ࡥࠨፌ"),
        l1l1111_Krypto_ (u"࠭࠰࠲࠴࠶࠸࠺࠼࠷࠲࠴ࠪፍ"),
        l1l1111_Krypto_ (u"ࠧ࠵࠲࠰ࡦ࡮ࡺࠠ࡬ࡧࡼࠫፎ")),
]
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    from l111ll1_Krypto_.l11111l_Krypto_ import l11lllll_Krypto_
    from .common import l1ll1ll11l1_Krypto_
    return l1ll1ll11l1_Krypto_(l11lllll_Krypto_, l1l1111_Krypto_ (u"ࠣࡅࡄࡗ࡙ࠨፏ"), l1ll11lllll_Krypto_)
if __name__ == l1l1111_Krypto_ (u"ࠩࡢࡣࡲࡧࡩ࡯ࡡࡢࠫፐ"):
    import unittest as l1lll111111_Krypto_
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"ࠪࡷࡺ࡯ࡴࡦࠩፑ"))