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
l1l1111_Krypto_ (u"ࠣࠤࠥࡗࡪࡲࡦ࠮ࡶࡨࡷࡹࠦࡳࡶ࡫ࡷࡩࠥ࡬࡯ࡳࠢࡆࡶࡾࡶࡴࡰ࠰ࡋࡥࡸ࡮࠮ࡎࡆ࠸ࠦࠧࠨᛈ")
__revision__ = l1l1111_Krypto_ (u"ࠤࠧࡍࡩࠪࠢᛉ")
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
l1ll11lllll_Krypto_ = [
    (l1l1111_Krypto_ (u"ࠪࡨ࠹࠷ࡤ࠹ࡥࡧ࠽࠽࡬࠰࠱ࡤ࠵࠴࠹࡫࠹࠹࠲࠳࠽࠾࠾ࡥࡤࡨ࠻࠸࠷࠽ࡥࠨᛊ"), l1l1111_Krypto_ (u"ࠫࠬᛋ"), l1l1111_Krypto_ (u"ࠧ࠭ࠧࠡࠪࡨࡱࡵࡺࡹࠡࡵࡷࡶ࡮ࡴࡧࠪࠤᛌ")),
    (l1l1111_Krypto_ (u"࠭࠰ࡤࡥ࠴࠻࠺ࡨ࠹ࡤ࠲ࡩ࠵ࡧ࠼ࡡ࠹࠵࠴ࡧ࠸࠿࠹ࡦ࠴࠹࠽࠼࠽࠲࠷࠸࠴ࠫᛍ"), l1l1111_Krypto_ (u"ࠧࡢࠩᛎ")),
    (l1l1111_Krypto_ (u"ࠨ࠻࠳࠴࠶࠻࠰࠺࠺࠶ࡧࡩ࠸࠴ࡧࡤ࠳ࡨ࠻࠿࠶࠴ࡨ࠺ࡨ࠷࠾ࡥ࠲࠹ࡩ࠻࠷࠭ᛏ"), l1l1111_Krypto_ (u"ࠩࡤࡦࡨ࠭ᛐ")),
    (l1l1111_Krypto_ (u"ࠪࡪ࠾࠼ࡢ࠷࠻࠺ࡨ࠼ࡩࡢ࠸࠻࠶࠼ࡩ࠻࠲࠶ࡣ࠵ࡪ࠸࠷ࡡࡢࡨ࠴࠺࠶ࡪ࠰ࠨᛑ"), l1l1111_Krypto_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠥࡪࡩࡨࡧࡶࡸࠬᛒ")),
    (l1l1111_Krypto_ (u"ࠬࡩ࠳ࡧࡥࡧ࠷ࡩ࠽࠶࠲࠻࠵ࡩ࠹࠶࠰࠸ࡦࡩࡦ࠹࠿࠶ࡤࡥࡤ࠺࠼࡫࠱࠴ࡤࠪᛓ"), l1l1111_Krypto_ (u"࠭ࡡࡣࡥࡧࡩ࡫࡭ࡨࡪ࡬࡮ࡰࡲࡴ࡯ࡱࡳࡵࡷࡹࡻࡶࡸࡺࡼࡾࠬᛔ"),
        l1l1111_Krypto_ (u"ࠧࡢ࠯ࡽࠫᛕ")),
    (l1l1111_Krypto_ (u"ࠨࡦ࠴࠻࠹ࡧࡢ࠺࠺ࡧ࠶࠼࠽ࡤ࠺ࡨ࠸ࡥ࠺࠼࠱࠲ࡥ࠵ࡧ࠾࡬࠴࠲࠻ࡧ࠽࡫࠭ᛖ"),
        l1l1111_Krypto_ (u"ࠩࡄࡆࡈࡊࡅࡇࡉࡋࡍࡏࡑࡌࡎࡐࡒࡔࡖࡘࡓࡕࡗ࡙࡛࡝࡟࡚ࡢࡤࡦࡨࡪ࡬ࡧࡩ࡫࡭࡯ࡱࡳ࡮ࡰࡲࡴࡶࡸࡺࡵࡷࡹࡻࡽࡿ࠶࠱࠳࠵࠷࠹࠻࠽࠸࠺ࠩᛗ"),
        l1l1111_Krypto_ (u"ࠪࡅ࠲ࡠࠬࠡࡣ࠰ࡾ࠱ࠦ࠰࠮࠻ࠪᛘ")),
    (l1l1111_Krypto_ (u"ࠫ࠺࠽ࡥࡥࡨ࠷ࡥ࠷࠸ࡢࡦ࠵ࡦ࠽࠺࠻ࡡࡤ࠶࠼ࡨࡦ࠸ࡥ࠳࠳࠳࠻ࡧ࠼࠷ࡢࠩᛙ"),
        l1l1111_Krypto_ (u"ࠬ࠷࠲࠴࠶࠸࠺࠼࠾࠹࠱࠳࠵࠷࠹࠻࠶࠸࠺࠼࠴࠶࠸࠳࠵࠷࠹࠻࠽࠿࠰࠲࠴࠶࠸࠺࠼࠷࠹࠻࠳࠵࠷࠹࠴࠶࠸ࠪᛚ")
        + l1l1111_Krypto_ (u"࠭࠷࠹࠻࠳࠵࠷࠹࠴࠶࠸࠺࠼࠾࠶࠱࠳࠵࠷࠹࠻࠽࠸࠺࠲࠴࠶࠸࠺࠵࠷࠹࠻࠽࠵࠭ᛛ"),
        l1l1111_Krypto_ (u"ࠢࠨ࠳࠵࠷࠹࠻࠶࠸࠺࠼࠴ࠬࠦࠪࠡ࠺ࠥᛜ")),
]
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    from l111ll1_Krypto_.l1lll1ll1_Krypto_ import l1llllllll_Krypto_
    from .common import l1l11l1l11l_Krypto_
    return l1l11l1l11l_Krypto_(l1llllllll_Krypto_, l1l1111_Krypto_ (u"ࠣࡏࡇ࠹ࠧᛝ"), l1ll11lllll_Krypto_,
        digest_size=16,
        l1llllll11_Krypto_=l1l1111_Krypto_ (u"ࠤ࡟ࡼ࠵࠼࡜ࡹ࠲࠻ࡠࡽ࠸ࡡ࡝ࡺ࠻࠺ࡡࡾ࠴࠹࡞ࡻ࠼࠻ࡢࡸࡧ࠹࡟ࡼ࠵ࡪ࡜ࡹ࠲࠵ࡠࡽ࠶࠵ࠣᛞ"))
if __name__ == l1l1111_Krypto_ (u"ࠪࡣࡤࡳࡡࡪࡰࡢࡣࠬᛟ"):
    import unittest as l1lll111111_Krypto_
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"ࠫࡸࡻࡩࡵࡧࠪᛠ"))