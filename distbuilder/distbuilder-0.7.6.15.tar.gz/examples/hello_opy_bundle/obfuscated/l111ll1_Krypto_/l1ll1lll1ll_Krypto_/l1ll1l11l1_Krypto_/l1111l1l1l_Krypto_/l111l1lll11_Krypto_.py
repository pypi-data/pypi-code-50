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
l1l1111_Krypto_ (u"ࠤࠥࠦࡘ࡫࡬ࡧ࠯ࡷࡩࡸࡺࠠࡴࡷ࡬ࡸࡪࠦࡦࡰࡴࠣࡇࡷࡿࡰࡵࡱ࠱ࡖࡦࡴࡤࡰ࡯࠱ࡊࡴࡸࡴࡶࡰࡤ࠲ࡘࡎࡁࡥ࠴࠸࠺ࠧࠨࠢᣤ")
__revision__ = l1l1111_Krypto_ (u"ࠥࠨࡎࡪࠤࠣᣥ")
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
l1ll11lllll_Krypto_ = [
    (l1l1111_Krypto_ (u"ࠫ࠺ࡪࡦ࠷ࡧ࠳ࡩ࠷࠽࠶࠲࠵࠸࠽ࡩ࠹࠰ࡢ࠺࠵࠻࠺࠶࠵࠹ࡧ࠵࠽࠾࡬ࡣࡤ࠲࠶࠼࠶࠻࠳࠵࠷࠷࠹࡫࠻࠵ࡤࡨ࠷࠷ࡪ࠺࠱࠺࠺࠶ࡪ࠺ࡪ࠴ࡤ࠻࠷࠹࠻࠭ᣦ"),
        l1l1111_Krypto_ (u"ࠬ࠭ᣧ"), l1l1111_Krypto_ (u"ࠨࠧࠨࠢࠫࡩࡲࡶࡴࡺࠢࡶࡸࡷ࡯࡮ࡨࠫࠥᣨ")),
    (l1l1111_Krypto_ (u"ࠧ࠵ࡨ࠻ࡦ࠹࠸ࡣ࠳࠴ࡧࡨ࠸࠽࠲࠺ࡤ࠸࠵࠾ࡨࡡ࠷ࡨ࠹࠼ࡩ࠸ࡤࡢ࠹ࡦࡧ࠺ࡨ࠲ࡥ࠸࠳࠺ࡩ࠶࠵ࡥࡣࡨࡨ࠺ࡧࡤ࠶࠳࠵࠼ࡨࡩ࠰࠴ࡧ࠹ࡧ࠻࠹࠵࠹ࠩᣩ"),
        l1l1111_Krypto_ (u"ࠨࡣࡥࡧࠬᣪ")),
    (l1l1111_Krypto_ (u"ࠩ࠳ࡧ࡫࡬ࡥ࠲࠹ࡩ࠺࠽࠿࠵࠵ࡦࡤࡧ࠸ࡧ࠸࠵ࡨࡥ࠵࠹࠻࠸ࡣࡦ࠸ࡩࡨ࠿࠹࠳࠲࠼࠸࠹࠿࠷࠵࠻ࡥ࠶ࡧ࠹࠰࠹ࡤ࠺ࡧࡧ࠻࠵࠹࠳࠵ࡪ࠾࠻࠶࠴ࡣࡩࠫᣫ"),
        l1l1111_Krypto_ (u"ࠪࡥࡧࡩࡤࡣࡥࡧࡩࡨࡪࡥࡧࡦࡨࡪ࡬࡫ࡦࡨࡪࡩ࡫࡭࡯ࡧࡩ࡫࡭࡬࡮ࡰ࡫ࡪ࡬࡮ࡰ࡯ࡱ࡬࡮࡭࡯ࡱࡳࡲ࡭࡯ࡱࡰࡲࡴࡶ࡮ࡰࡲࡴࠫᣬ"))
]
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    from l111ll1_Krypto_.l1ll1l11l1_Krypto_.l1111l1l1l_Krypto_ import l1llllll1l1_Krypto_
    from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l1lll1ll1_Krypto_.common import l1l11l1l11l_Krypto_
    return l1l11l1l11l_Krypto_(l1llllll1l1_Krypto_, l1l1111_Krypto_ (u"ࠦࡘࡎࡁࡥ࠴࠸࠺ࠧᣭ"), l1ll11lllll_Krypto_, 32)
if __name__ == l1l1111_Krypto_ (u"ࠬࡥ࡟࡮ࡣ࡬ࡲࡤࡥࠧᣮ"):
    import unittest as l1lll111111_Krypto_
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"࠭ࡳࡶ࡫ࡷࡩࠬᣯ"))