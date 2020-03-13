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
l1l1111_Krypto_ (u"ࠨࠢࠣࡕࡨࡰ࡫࠳ࡴࡦࡵࡷࠤࡸࡻࡩࡵࡧࠣࡪࡴࡸࠠࡄࡴࡼࡴࡹࡵ࠮ࡄ࡫ࡳ࡬ࡪࡸ࠮ࡂࡔࡆ࠸ࠧࠨࠢቦ")
__revision__ = l1l1111_Krypto_ (u"ࠢࠥࡋࡧࠨࠧቧ")
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
l1ll11lllll_Krypto_ = [
    (l1l1111_Krypto_ (u"ࠨ࠲࠴࠶࠸࠺࠵࠷࠹࠻࠽ࡦࡨࡣࡥࡧࡩࠫቨ"), l1l1111_Krypto_ (u"ࠩ࠺࠹ࡧ࠽࠸࠸࠺࠳࠽࠾࡫࠰ࡤ࠷࠼࠺ࠬቩ"), l1l1111_Krypto_ (u"ࠪ࠴࠶࠸࠳࠵࠷࠹࠻࠽࠿ࡡࡣࡥࡧࡩ࡫࠭ቪ"),
        l1l1111_Krypto_ (u"࡙ࠫ࡫ࡳࡵࠢࡹࡩࡨࡺ࡯ࡳࠢ࠳ࠫቫ")),
    (l1l1111_Krypto_ (u"ࠬ࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰ࠨቬ"), l1l1111_Krypto_ (u"࠭࠷࠵࠻࠷ࡧ࠷࡫࠷࠲࠲࠷ࡦ࠵࠾࠷࠺ࠩቭ"), l1l1111_Krypto_ (u"ࠧ࠱࠳࠵࠷࠹࠻࠶࠸࠺࠼ࡥࡧࡩࡤࡦࡨࠪቮ"),
        l1l1111_Krypto_ (u"ࠨࡖࡨࡷࡹࠦࡶࡦࡥࡷࡳࡷࠦ࠱ࠨቯ")),
    (l1l1111_Krypto_ (u"ࠩ࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴ࠬተ"), l1l1111_Krypto_ (u"ࠪࡨࡪ࠷࠸࠹࠻࠷࠵ࡦ࠹࠳࠸࠷ࡧ࠷ࡦ࠭ቱ"), l1l1111_Krypto_ (u"ࠫ࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶ࠧቲ"),
        l1l1111_Krypto_ (u"࡚ࠬࡥࡴࡶࠣࡺࡪࡩࡴࡰࡴࠣ࠶ࠬታ")),
    (l1l1111_Krypto_ (u"࠭࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠭ቴ"), l1l1111_Krypto_ (u"ࠧࡥ࠸ࡤ࠵࠹࠷ࡡ࠸ࡧࡦ࠷ࡨ࠹࠸ࡥࡨࡥࡨ࠻࠷ࠧት"), l1l1111_Krypto_ (u"ࠨࡧࡩ࠴࠶࠸࠳࠵࠷ࠪቶ"),
        l1l1111_Krypto_ (u"ࠩࡗࡩࡸࡺࠠࡷࡧࡦࡸࡴࡸࠠ࠴ࠩቷ")),
    (l1l1111_Krypto_ (u"ࠪ࠴࠶࠭ቸ") * 512,
        l1l1111_Krypto_ (u"ࠫ࠼࠻࠹࠶ࡥ࠶ࡩ࠻࠷࠱࠵ࡣ࠳࠽࠼࠾࠰ࡤ࠶ࡤࡨ࠹࠻࠲࠴࠵࠻ࡩ࠶࡬ࡦࡥ࠻ࡤ࠵ࡧ࡫࠹࠵࠻࠻ࡪ࠽࠷࠳ࡥ࠹࠹࠹࠸࠹࠴࠵࠻ࡥ࠺࠼࠽࠸ࡥࡥࡤࡨ࠽࠭ቹ")
        + l1l1111_Krypto_ (u"ࠬࡩ࠷࠹ࡣ࠻ࡨ࠷ࡨࡡ࠺ࡣࡦ࠺࠻࠶࠸࠶ࡦ࠳ࡩ࠺࠹ࡤ࠶࠻ࡦ࠶࠻ࡩ࠲ࡥ࠳ࡦ࠸࠾࠶ࡣ࠲ࡧࡥࡦࡪ࠶ࡣࡦ࠸࠹ࡨ࠶ࡨ࠶ࡣ࠳ࡥ࠵࠸ࡨ࠶ࡣ࠻࠴࠽ࡧ࠾ࠧቺ")
        + l1l1111_Krypto_ (u"࠭࠴࠸ࡥ࠵࠹ࡦ࠿࠱࠵࠶࠺ࡥ࠾࠻ࡥ࠸࠷ࡨ࠸ࡪ࡬࠱࠷࠹࠺࠽ࡨࡪࡥ࠹ࡤࡩ࠴ࡦ࠿࠵࠹࠷࠳ࡩ࠸࠸ࡡࡧ࠻࠹࠼࠾࠺࠴࠵ࡨࡧ࠷࠼࠽࠱࠱࠺ࡩ࠽࠽࡬ࡤࠨቻ")
        + l1l1111_Krypto_ (u"ࠧࡤࡤࡧ࠸ࡪ࠽࠲࠷࠷࠹࠻࠺࠶࠰࠺࠻࠳ࡦࡨࡩ࠷ࡦ࠲ࡦࡥ࠸ࡩ࠴ࡢࡣࡤ࠷࠵࠺ࡡ࠴࠺࠺ࡨ࠷࠶ࡦ࠴ࡤ࠻ࡪࡧࡨࡣࡥ࠶࠵ࡥ࠶ࡨࡤ࠴࠳࠴ࡨ࠼ࡧ࠴࠴ࠩቼ")
        + l1l1111_Krypto_ (u"ࠨ࠲࠶ࡨࡩࡧ࠵ࡢࡤ࠳࠻࠽࠾࠹࠷ࡣࡨ࠼࠵ࡩ࠱࠹ࡤ࠳ࡥ࡫࠼࠶ࡥࡨࡩ࠷࠶࠿࠶࠲࠸ࡨࡦ࠼࠾࠴ࡦ࠶࠼࠹ࡦࡪ࠲ࡤࡧ࠼࠴ࡩ࠽ࡦ࠸࠹࠵ࡥ࠽࠷࠷࠵࠹ࠪች")
        + l1l1111_Krypto_ (u"ࠩࡥ࠺࠺࡬࠶࠳࠲࠼࠷ࡧ࠷ࡥ࠱ࡦࡥ࠽ࡪ࠻ࡢࡢ࠷࠶࠶࡫ࡧࡦࡦࡥ࠷࠻࠺࠶࠸࠴࠴࠶ࡩ࠻࠽࠱࠴࠴࠺ࡨ࡫࠿࠴࠵࠶࠷࠷࠷ࡩࡢ࠸࠵࠹࠻ࡨ࡫ࡣ࠹࠴ࡩࠫቾ")
        + l1l1111_Krypto_ (u"ࠪ࠹ࡩ࠺࠴ࡤ࠲ࡧ࠴࠵ࡨ࠶࠸ࡦ࠹࠹࠵ࡧ࠰࠸࠷ࡦࡨ࠹ࡨ࠷࠱ࡦࡨࡨࡩ࠽࠷ࡦࡤ࠼ࡦ࠶࠶࠲࠴࠳ࡥ࠺ࡧ࠻ࡢ࠸࠶࠴࠷࠹࠽࠳࠺࠸ࡧ࠺࠷࠾࠹࠸࠶࠵࠵ࠬቿ")
        + l1l1111_Krypto_ (u"ࠫࡩ࠺࠳ࡥࡨ࠼ࡦ࠹࠸ࡥ࠵࠶࠹ࡩ࠸࠻࠸ࡦ࠻ࡦ࠵࠶ࡧ࠹ࡣ࠴࠴࠼࠹࡫ࡣࡣࡧࡩ࠴ࡨࡪ࠸ࡦ࠹ࡤ࠼࠼࠽ࡥࡧ࠻࠹࠼࡫࠷࠳࠺࠲ࡨࡧ࠾ࡨ࠳ࡥ࠵࠸ࡥ࠺࠭ኀ")
        + l1l1111_Krypto_ (u"ࠬ࠻࠸࠶ࡥࡥ࠴࠵࠿࠲࠺࠲ࡨ࠶࡫ࡩࡤࡦ࠹ࡥ࠹ࡪࡩ࠶࠷ࡦ࠼࠴࠽࠺ࡢࡦ࠶࠷࠴࠺࠻ࡡ࠷࠳࠼ࡨ࠾ࡪࡤ࠸ࡨࡦ࠷࠶࠼࠶ࡧ࠻࠷࠼࠼࡬࠷ࡤࡤ࠵࠻࠷࠿ࠧኁ")
        + l1l1111_Krypto_ (u"࠭࠱࠳࠶࠵࠺࠹࠺࠵࠺࠻࠻࠹࠶࠺ࡣ࠲࠷ࡧ࠹࠸ࡧ࠱࠹ࡥ࠻࠺࠹ࡩࡥ࠴ࡣ࠵ࡦ࠼࠻࠵࠶࠹࠼࠷࠾࠾࠸࠲࠴࠹࠹࠷࠶ࡥࡢࡥࡩ࠶ࡪ࠹࠰࠷࠸ࡨ࠶࠸࠶ࡣࠨኂ")
        + l1l1111_Krypto_ (u"ࠧ࠺࠳ࡥࡩࡪ࠺ࡤࡥ࠷࠶࠴࠹࡬࠵ࡧࡦ࠳࠸࠵࠻ࡢ࠴࠷ࡥࡨ࠾࠿ࡣ࠸࠵࠴࠷࠺ࡪ࠳ࡥ࠻ࡥࡧ࠸࠹࠵ࡦࡧ࠳࠸࠾࡫ࡦ࠷࠻ࡥ࠷࠽࠼࠷ࡣࡨ࠵ࡨ࠼ࡨࡤ࠲ࠩኃ")
        + l1l1111_Krypto_ (u"ࠨࡧࡤࡥ࠺࠿࠵ࡥ࠺ࡥࡪࡨ࠶࠰࠷࠸ࡩࡪ࠽ࡪ࠳࠲࠷࠳࠽ࡪࡨ࠰ࡤ࠸ࡦࡥࡦ࠶࠰࠷ࡥ࠻࠴࠼ࡧ࠶࠳࠵ࡨࡪ࠽࠺ࡣ࠴ࡦ࠶࠷ࡨ࠷࠹࠶ࡦ࠵࠷ࡪ࡫࠳࠳࠲ࠪኄ")
        + l1l1111_Krypto_ (u"ࠩࡦ࠸࠵ࡪࡥ࠱࠷࠸࠼࠶࠻࠷ࡤ࠺࠵࠶ࡩ࠺ࡢ࠹ࡥ࠸࠺࠾ࡪ࠸࠵࠻ࡤࡩࡩ࠻࠹ࡥ࠶ࡨ࠴࡫ࡪ࠷ࡧ࠵࠺࠽࠺࠾࠶ࡣ࠶ࡥ࠻࡫࡬࠶࠹࠶ࡨࡨ࠻ࡧ࠱࠹࠻ࡩࠫኅ")
        + l1l1111_Krypto_ (u"ࠪ࠻࠹࠾࠶ࡥ࠶࠼ࡦ࠾ࡩ࠴ࡣࡣࡧ࠽ࡧࡧ࠲࠵ࡤ࠼࠺ࡦࡨࡦ࠺࠴࠷࠷࠼࠸ࡣ࠹ࡣ࠻ࡪ࡫࡬ࡢ࠲࠲ࡧ࠹࠺࠹࠵࠵࠻࠳࠴ࡦ࠽࠷ࡢ࠵ࡧࡦ࠺࡬࠲࠱࠷ࡨ࠵ࠬኆ")
        + l1l1111_Krypto_ (u"ࠫࡧ࠿࠹ࡧࡥࡧ࠼࠻࠼࠰࠹࠸࠶ࡥ࠶࠻࠹ࡢࡦ࠷ࡥࡧ࡫࠴࠱ࡨࡤ࠸࠽࠿࠳࠵࠳࠹࠷ࡩࡪࡤࡦ࠷࠷࠶ࡦ࠼࠵࠹࠷࠸࠸࠵࡬ࡤ࠷࠺࠶ࡧࡧ࡬ࡤ࠹ࡥ࠳࠴࡫࠭ኇ")
        + l1l1111_Krypto_ (u"ࠬ࠷࠲࠲࠴࠼ࡥ࠷࠾࠴ࡥࡧࡤࡧࡨ࠺ࡣࡥࡧࡩࡩ࠺࠾ࡢࡦ࠹࠴࠷࠼࠻࠴࠲ࡥ࠳࠸࠼࠷࠲࠷ࡥ࠻ࡨ࠹࠿ࡥ࠳࠹࠸࠹ࡦࡨ࠱࠹࠳ࡤࡦ࠼࡫࠹࠵࠲ࡥ࠴ࡨ࠶ࠧኈ"),
        l1l1111_Krypto_ (u"࠭࠰࠲࠴࠶࠸࠺࠼࠷࠹࠻ࡤࡦࡨࡪࡥࡧࠩ኉"),
        l1l1111_Krypto_ (u"ࠢࡕࡧࡶࡸࠥࡼࡥࡤࡶࡲࡶࠥ࠺ࠢኊ")),
]
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    from l111ll1_Krypto_.l11111l_Krypto_ import l1ll1l1l_Krypto_
    from .common import l1l1lll1l11_Krypto_
    return l1l1lll1l11_Krypto_(l1ll1l1l_Krypto_, l1l1111_Krypto_ (u"ࠣࡃࡕࡇ࠹ࠨኋ"), l1ll11lllll_Krypto_)
if __name__ == l1l1111_Krypto_ (u"ࠩࡢࡣࡲࡧࡩ࡯ࡡࡢࠫኌ"):
    import unittest as l1lll111111_Krypto_
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"ࠪࡷࡺ࡯ࡴࡦࠩኍ"))