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
l1l1111_Krypto_ (u"ࠧࠨࠢࡔࡧ࡯ࡪ࠲ࡺࡥࡴࡶࠣࡷࡺ࡯ࡴࡦࠢࡩࡳࡷࠦࡃࡳࡻࡳࡸࡴ࠴ࡈࡢࡵ࡫࠲ࡘࡎࡁ࠳࠴࠷ࠦࠧࠨᜋ")
__revision__ = l1l1111_Krypto_ (u"ࠨࠤࡊࡦࠧࠦᜌ")
l1ll11lllll_Krypto_ = [
    (l1l1111_Krypto_ (u"ࠧ࠳࠵࠳࠽࠼ࡪ࠲࠳࠵࠷࠴࠺ࡪ࠸࠳࠴࠻࠺࠹࠸ࡡ࠵࠹࠺ࡦࡩࡧ࠲࠶࠷ࡥ࠷࠷ࡧࡡࡥࡤࡦࡩ࠹ࡨࡤࡢ࠲ࡥ࠷࡫࠽ࡥ࠴࠸ࡦ࠽ࡩࡧ࠷ࠨᜍ"), l1l1111_Krypto_ (u"ࠨࡣࡥࡧࠬᜎ")),
    (l1l1111_Krypto_ (u"ࠩ࠺࠹࠸࠾࠸ࡣ࠳࠹࠹࠶࠸࠷࠸࠸ࡦࡧ࠺ࡪࡢࡢ࠷ࡧࡥ࠶࡬ࡤ࠹࠻࠳࠵࠺࠶ࡢ࠱ࡥ࠹࠸࠺࠻ࡣࡣ࠶ࡩ࠹࠽ࡨ࠱࠺࠷࠵࠹࠷࠸࠵࠳࠷ࠪᜏ"), l1l1111_Krypto_ (u"ࠪࡥࡧࡩࡤࡣࡥࡧࡩࡨࡪࡥࡧࡦࡨࡪ࡬࡫ࡦࡨࡪࡩ࡫࡭࡯ࡧࡩ࡫࡭࡬࡮ࡰ࡫ࡪ࡬࡮ࡰ࡯ࡱ࡬࡮࡭࡯ࡱࡳࡲ࡭࡯ࡱࡰࡲࡴࡶ࡮ࡰࡲࡴࠫᜐ")),
    (l1l1111_Krypto_ (u"ࠫ࠷࠶࠷࠺࠶࠹࠹࠺࠿࠸࠱ࡥ࠼࠵ࡩ࠾ࡢࡣࡤ࠷ࡧ࠶࡫ࡡ࠺࠹࠹࠵࠽ࡧ࠴ࡣࡨ࠳࠷࡫࠺࠲࠶࠺࠴࠽࠹࠾ࡢ࠳ࡧࡨ࠸ࡪ࡫࠷ࡢࡦ࠹࠻ࠬᜑ"), l1l1111_Krypto_ (u"ࠬࡧࠧᜒ") * 10**6, l1l1111_Krypto_ (u"ࠨࠧࡢࠩࠣ࠮ࠥ࠷࠰ࠫࠬ࠹ࠦᜓ")),
    (l1l1111_Krypto_ (u"ࠧࡥ࠳࠷ࡥ࠵࠸࠸ࡤ࠴ࡤ࠷ࡦ࠸ࡢࡤ࠻࠷࠻࠻࠷࠰࠳ࡤࡥ࠶࠽࠾࠲࠴࠶ࡦ࠸࠶࠻ࡡ࠳ࡤ࠳࠵࡫࠾࠲࠹ࡧࡤ࠺࠷ࡧࡣ࠶ࡤ࠶ࡩ࠹࠸ࡦࠨ᜔"), l1l1111_Krypto_ (u"ࠨ᜕ࠩ")),
    (l1l1111_Krypto_ (u"ࠩ࠷࠽ࡧ࠶࠸ࡥࡧࡩࡥ࠻࠻ࡥ࠷࠶࠷ࡧࡧ࡬࠸ࡢ࠴ࡧࡨ࠾࠸࠷࠱ࡤࡧࡩࡩ࡫ࡤࡢࡤࡦ࠻࠹࠷࠹࠺࠹ࡧ࠵ࡩࡧࡤࡥ࠶࠵࠴࠷࠼ࡤ࠸ࡤࠪ᜖"),
     l1l1111_Krypto_ (u"ࠪࡊࡷࡧ࡮ࡻࠢ࡭ࡥ࡬ࡺࠠࡪ࡯ࠣ࡯ࡴࡳࡰ࡭ࡧࡷࡸࠥࡼࡥࡳࡹࡤ࡬ࡷࡲ࡯ࡴࡶࡨࡲ࡚ࠥࡡࡹ࡫ࠣࡵࡺ࡫ࡲࠡࡦࡸࡶࡨ࡮ࠠࡃࡣࡼࡩࡷࡴࠧ᜗")),
    (l1l1111_Krypto_ (u"ࠫ࠺࠾࠹࠲࠳ࡨ࠻࡫ࡩࡣࡧ࠴࠼࠻࠶ࡧ࠷ࡥ࠲࠺ࡪ࠾࠹࠱࠷࠴ࡧ࠼ࡧࡪ࠱࠴࠷࠹࠼ࡪ࠽࠱ࡢࡣ࠻ࡪࡨ࠾࠶ࡧࡥ࠴ࡪࡪ࠿࠰࠵࠵ࡧ࠵ࠬ᜘"),
     l1l1111_Krypto_ (u"ࠬࡌࡲࡢࡰ࡮ࠤ࡯ࡧࡧࡵࠢ࡬ࡱࠥࡱ࡯࡮ࡲ࡯ࡩࡹࡺࠠࡷࡧࡵࡻࡦ࡮ࡲ࡭ࡱࡶࡸࡪࡴࠠࡕࡣࡻ࡭ࠥࡷࡵࡦࡴࠣࡨࡺࡸࡣࡩࠢࡅࡥࡾ࡫ࡲ࡯ࠩ᜙")),
]
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    from l111ll1_Krypto_.l1lll1ll1_Krypto_ import l1lll1lll1_Krypto_
    from .common import l1l11l1l11l_Krypto_
    return l1l11l1l11l_Krypto_(l1lll1lll1_Krypto_, l1l1111_Krypto_ (u"ࠨࡓࡉࡃ࠵࠶࠹ࠨ᜚"), l1ll11lllll_Krypto_,
        digest_size=28,
        l1llllll11_Krypto_=l1l1111_Krypto_ (u"ࠧ࡝ࡺ࠳࠺ࡡࡾ࠰࠺࡞ࡻ࠺࠵ࡢࡸ࠹࠸࡟ࡼ࠹࠾࡜ࡹ࠲࠴ࡠࡽ࠼࠵࡝ࡺ࠳࠷ࡡࡾ࠰࠵࡞ࡻ࠴࠷ࡢࡸ࠱࠶ࠪ᜛"))
if __name__ == l1l1111_Krypto_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪ᜜"):
    import unittest as l1lll111111_Krypto_
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"ࠩࡶࡹ࡮ࡺࡥࠨ᜝"))