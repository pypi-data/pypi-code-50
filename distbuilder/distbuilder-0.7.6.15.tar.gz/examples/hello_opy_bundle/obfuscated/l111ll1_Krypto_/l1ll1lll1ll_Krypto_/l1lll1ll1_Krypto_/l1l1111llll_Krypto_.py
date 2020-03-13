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
__revision__ = l1l1111_Krypto_ (u"ࠧࠪࡉࡥࠦࠥᛡ")
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
l1ll11lllll_Krypto_ = [
    (l1l1111_Krypto_ (u"࠭࠹ࡤ࠳࠴࠼࠺ࡧ࠵ࡤ࠷ࡨ࠽࡫ࡩ࠵࠵࠸࠴࠶࠽࠶࠸࠺࠹࠺ࡩࡪ࠾ࡦ࠶࠶࠻ࡦ࠷࠸࠵࠹ࡦ࠶࠵ࠬᛢ"), l1l1111_Krypto_ (u"ࠧࠨᛣ"), l1l1111_Krypto_ (u"ࠣࠩࠪࠤ࠭࡫࡭ࡱࡶࡼࠤࡸࡺࡲࡪࡰࡪ࠭ࠧᛤ")),
    (l1l1111_Krypto_ (u"ࠩ࠳ࡦࡩࡩ࠹ࡥ࠴ࡧ࠶࠺࠼ࡢ࠴ࡧࡨ࠽ࡩࡧࡡࡦ࠵࠷࠻ࡧ࡫࠶ࡧ࠶ࡧࡧ࠽࠹࠵ࡢ࠶࠹࠻࡫࡬ࡥࠨᛥ"), l1l1111_Krypto_ (u"ࠪࡥࠬᛦ")),
    (l1l1111_Krypto_ (u"ࠫ࠽࡫ࡢ࠳࠲࠻ࡪ࠼࡫࠰࠶ࡦ࠼࠼࠼ࡧ࠹ࡣ࠲࠷࠸ࡦ࠾ࡥ࠺࠺ࡦ࠺ࡧ࠶࠸࠸ࡨ࠴࠹ࡦ࠶ࡢࡧࡥࠪᛧ"), l1l1111_Krypto_ (u"ࠬࡧࡢࡤࠩᛨ")),
    (l1l1111_Krypto_ (u"࠭࠵ࡥ࠲࠹࠼࠾࡫ࡦ࠵࠻ࡧ࠶࡫ࡧࡥ࠶࠹࠵ࡦ࠽࠾࠱ࡣ࠳࠵࠷ࡦ࠾࠵ࡧࡨࡤ࠶࠶࠻࠹࠶ࡨ࠶࠺ࠬᛩ"), l1l1111_Krypto_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠡࡦ࡬࡫ࡪࡹࡴࠨᛪ")),
    (l1l1111_Krypto_ (u"ࠨࡨ࠺࠵ࡨ࠸࠷࠲࠲࠼ࡧ࠻࠿࠲ࡤ࠳ࡥ࠹࠻ࡨࡢࡥࡥࡨࡦ࠺ࡨ࠹ࡥ࠴࠻࠺࠺ࡨ࠳࠸࠲࠻ࡨࡧࡩࠧ᛫"),
        l1l1111_Krypto_ (u"ࠩࡤࡦࡨࡪࡥࡧࡩ࡫࡭࡯ࡱ࡬࡮ࡰࡲࡴࡶࡸࡳࡵࡷࡹࡻࡽࡿࡺࠨ᛬"),
        l1l1111_Krypto_ (u"ࠪࡥ࠲ࢀࠧ᛭")),
    (l1l1111_Krypto_ (u"ࠫ࠶࠸ࡡ࠱࠷࠶࠷࠽࠺ࡡ࠺ࡥ࠳ࡧ࠽࠾ࡥ࠵࠲࠸ࡥ࠵࠼ࡣ࠳࠹ࡧࡧ࡫࠺࠹ࡢࡦࡤ࠺࠷࡫ࡢ࠳ࡤࠪᛮ"),
        l1l1111_Krypto_ (u"ࠬࡧࡢࡤࡦࡥࡧࡩ࡫ࡣࡥࡧࡩࡨࡪ࡬ࡧࡦࡨࡪ࡬࡫࡭ࡨࡪࡩ࡫࡭࡯࡮ࡩ࡫࡭࡬࡮ࡰࡲࡪ࡬࡮ࡰ࡯ࡱࡳ࡮࡭࡯ࡱࡳࡲࡴ࡯ࡱࡰࡲࡴࡶ࠭ᛯ"),
        l1l1111_Krypto_ (u"࠭ࡡࡣࡥࡧࡦࡨࡪ࠮࠯࠰ࡳࡲࡴࡶࡱࠨᛰ")),
    (l1l1111_Krypto_ (u"ࠧࡣ࠲ࡨ࠶࠵ࡨ࠶ࡦ࠵࠴࠵࠻࠼࠴࠱࠴࠻࠺ࡪࡪ࠳ࡢ࠺࠺ࡥ࠺࠽࠱࠴࠲࠺࠽ࡧ࠸࠱ࡧ࠷࠴࠼࠾࠭ᛱ"),
        l1l1111_Krypto_ (u"ࠨࡃࡅࡇࡉࡋࡆࡈࡊࡌࡎࡐࡒࡍࡏࡑࡓࡕࡗ࡙ࡔࡖࡘ࡚࡜࡞ࡠࡡࡣࡥࡧࡩ࡫࡭ࡨࡪ࡬࡮ࡰࡲࡴ࡯ࡱࡳࡵࡷࡹࡻࡶࡸࡺࡼࡾ࠵࠷࠲࠴࠶࠸࠺࠼࠾࠹ࠨᛲ"),
        l1l1111_Krypto_ (u"ࠩࡄ࠱࡟࠲ࠠࡢ࠯ࡽ࠰ࠥ࠶࠭࠺ࠩᛳ")),
    (l1l1111_Krypto_ (u"ࠪ࠽ࡧ࠽࠵࠳ࡧ࠷࠹࠺࠽࠳ࡥ࠶ࡥ࠷࠾࡬࠴ࡥࡤࡧ࠷࠸࠸࠳ࡤࡣࡥ࠼࠷ࡨࡦ࠷࠵࠶࠶࠻ࡨࡦࡣࠩᛴ"),
        l1l1111_Krypto_ (u"ࠫ࠶࠸࠳࠵࠷࠹࠻࠽࠿࠰ࠨᛵ") * 8,
        l1l1111_Krypto_ (u"ࠧ࠭࠱࠳࠵࠷࠹࠻࠽࠸࠺࠲ࠪࠤ࠯ࠦ࠸ࠣᛶ")),
    (l1l1111_Krypto_ (u"࠭࠵࠳࠹࠻࠷࠷࠺࠳ࡤ࠳࠹࠽࠼ࡨࡤࡣࡧ࠴࠺ࡩ࠹࠷ࡧ࠻࠺ࡪ࠻࠾ࡦ࠱࠺࠶࠶࠺ࡪࡣ࠲࠷࠵࠼ࠬᛷ"),
        l1l1111_Krypto_ (u"ࠧࡢࠩᛸ") * 10**6,
        l1l1111_Krypto_ (u"ࠨࠤࡤࠦࠥ࠰ࠠ࠲࠲࠭࠮࠻࠭᛹")),
]
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    from l111ll1_Krypto_.l1lll1ll1_Krypto_ import l1llll11l1_Krypto_
    from .common import l1l11l1l11l_Krypto_
    return l1l11l1l11l_Krypto_(l1llll11l1_Krypto_, l1l1111_Krypto_ (u"ࠤࡕࡍࡕࡋࡍࡅࠤ᛺"), l1ll11lllll_Krypto_,
        digest_size=20,
        l1llllll11_Krypto_=l1l1111_Krypto_ (u"ࠥࡠࡽ࠶࠶࡝ࡺ࠳࠹ࡡࡾ࠲ࡣ࡞ࡻ࠶࠹ࡢࡸ࠱࠵࡟࠴࠷ࡢࡸ࠱࠳ࠥ᛻"))
if __name__ == l1l1111_Krypto_ (u"ࠫࡤࡥ࡭ࡢ࡫ࡱࡣࡤ࠭᛼"):
    import unittest as l1lll111111_Krypto_
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"ࠬࡹࡵࡪࡶࡨࠫ᛽"))