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
l1l1111_Krypto_ (u"ࠢࠣࠤࡖࡩࡱ࡬࠭ࡵࡧࡶࡸࠥࡹࡵࡪࡶࡨࠤ࡫ࡵࡲࠡࡅࡵࡽࡵࡺ࡯࠯ࡊࡤࡷ࡭࠴ࡍࡅ࠴ࠥࠦࠧᚖ")
__revision__ = l1l1111_Krypto_ (u"ࠣࠦࡌࡨࠩࠨᚗ")
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
l1ll11lllll_Krypto_ = [
    (l1l1111_Krypto_ (u"ࠩ࠻࠷࠺࠶ࡥ࠶ࡣ࠶ࡩ࠷࠺ࡣ࠲࠷࠶ࡨ࡫࠸࠲࠸࠷ࡦ࠽࡫࠾࠰࠷࠻࠵࠻࠼࠹ࠧᚘ"), l1l1111_Krypto_ (u"ࠪࠫᚙ"), l1l1111_Krypto_ (u"ࠦࠬ࠭ࠠࠩࡧࡰࡴࡹࡿࠠࡴࡶࡵ࡭ࡳ࡭ࠩࠣᚚ")),
    (l1l1111_Krypto_ (u"ࠬ࠹࠲ࡦࡥ࠳࠵ࡪࡩ࠴ࡢ࠸ࡧࡥࡨ࠽࠲ࡤ࠲ࡤࡦ࠾࠼ࡦࡣ࠵࠷ࡧ࠵ࡨ࠵ࡥ࠳ࠪ᚛"), l1l1111_Krypto_ (u"࠭ࡡࠨ᚜")),
    (l1l1111_Krypto_ (u"ࠧࡥࡣ࠻࠹࠸ࡨ࠰ࡥ࠵ࡩ࠼࠽ࡪ࠹࠺ࡤ࠶࠴࠷࠾࠳ࡢ࠸࠼ࡩ࠻ࡪࡥࡥ࠸ࡥࡦࠬ᚝"), l1l1111_Krypto_ (u"ࠨࡣࡥࡧࠬ᚞")),
    (l1l1111_Krypto_ (u"ࠩࡤࡦ࠹࡬࠴࠺࠸ࡥࡪࡧ࠸ࡡ࠶࠵࠳ࡦ࠷࠷࠹ࡧࡨ࠶࠷࠵࠹࠱ࡧࡧ࠳࠺ࡧ࠶ࠧ᚟"), l1l1111_Krypto_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠤࡩ࡯ࡧࡦࡵࡷࠫᚠ")),
    (l1l1111_Krypto_ (u"ࠫ࠹࡫࠸ࡥࡦࡩࡪ࠸࠼࠵࠱࠴࠼࠶ࡦࡨ࠵ࡢ࠶࠴࠴࠽ࡩ࠳ࡢࡣ࠷࠻࠾࠺࠰ࡣࠩᚡ"), l1l1111_Krypto_ (u"ࠬࡧࡢࡤࡦࡨࡪ࡬࡮ࡩ࡫࡭࡯ࡱࡳࡵࡰࡲࡴࡶࡸࡺࡼࡷࡹࡻࡽࠫᚢ"),
        l1l1111_Krypto_ (u"࠭ࡡ࠮ࡼࠪᚣ")),
    (l1l1111_Krypto_ (u"ࠧࡥࡣ࠶࠷ࡩ࡫ࡦ࠳ࡣ࠷࠶ࡩ࡬࠱࠴࠻࠺࠹࠸࠻࠲࠹࠶࠹ࡧ࠸࠶࠳࠴࠺ࡦࡨࠬᚤ"),
        l1l1111_Krypto_ (u"ࠨࡃࡅࡇࡉࡋࡆࡈࡊࡌࡎࡐࡒࡍࡏࡑࡓࡕࡗ࡙ࡔࡖࡘ࡚࡜࡞ࡠࡡࡣࡥࡧࡩ࡫࡭ࡨࡪ࡬࡮ࡰࡲࡴ࡯ࡱࡳࡵࡷࡹࡻࡶࡸࡺࡼࡾ࠵࠷࠲࠴࠶࠸࠺࠼࠾࠹ࠨᚥ"),
        l1l1111_Krypto_ (u"ࠩࡄ࠱࡟࠲ࠠࡢ࠯ࡽ࠰ࠥ࠶࠭࠺ࠩᚦ")),
    (l1l1111_Krypto_ (u"ࠪࡨ࠺࠿࠷࠷ࡨ࠺࠽ࡩ࠾࠳ࡥ࠵ࡤ࠴ࡩࡩ࠹࠹࠲࠹ࡧ࠸ࡩ࠶࠷ࡨ࠶ࡩ࡫ࡪ࠸ࠨᚧ"),
        l1l1111_Krypto_ (u"ࠫ࠶࠸࠳࠵࠷࠹࠻࠽࠿࠰࠲࠴࠶࠸࠺࠼࠷࠹࠻࠳࠵࠷࠹࠴࠶࠸࠺࠼࠾࠶࠱࠳࠵࠷࠹࠻࠽࠸࠺࠲࠴࠶࠸࠺࠵࠷ࠩᚨ")
        + l1l1111_Krypto_ (u"ࠬ࠽࠸࠺࠲࠴࠶࠸࠺࠵࠷࠹࠻࠽࠵࠷࠲࠴࠶࠸࠺࠼࠾࠹࠱࠳࠵࠷࠹࠻࠶࠸࠺࠼࠴ࠬᚩ"),
        l1l1111_Krypto_ (u"ࠨࠧ࠲࠴࠶࠸࠺࠼࠷࠹࠻࠳ࠫࠥ࠰ࠠ࠹ࠤᚪ")),
]
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    from l111ll1_Krypto_.l1lll1ll1_Krypto_ import l1lllll1l1_Krypto_
    from .common import l1l11l1l11l_Krypto_
    return l1l11l1l11l_Krypto_(l1lllll1l1_Krypto_, l1l1111_Krypto_ (u"ࠢࡎࡆ࠵ࠦᚫ"), l1ll11lllll_Krypto_,
        digest_size=16,
        l1llllll11_Krypto_=l1l1111_Krypto_ (u"ࠣ࡞ࡻ࠴࠻ࡢࡸ࠱࠺࡟ࡼ࠷ࡧ࡜ࡹ࠺࠹ࡠࡽ࠺࠸࡝ࡺ࠻࠺ࡡࡾࡦ࠸࡞ࡻ࠴ࡩࡢࡸ࠱࠴࡟ࡼ࠵࠸ࠢᚬ"))
if __name__ == l1l1111_Krypto_ (u"ࠩࡢࡣࡲࡧࡩ࡯ࡡࡢࠫᚭ"):
    import unittest as l1lll111111_Krypto_
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"ࠪࡷࡺ࡯ࡴࡦࠩᚮ"))