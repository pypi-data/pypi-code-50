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
__revision__ = l1l1111_Krypto_ (u"ࠣࠦࡌࡨࠩࠨᤔ")
import unittest as l1lll111111_Krypto_
from l111ll1_Krypto_.l11l11l1_Krypto_ import l1l11lll1_Krypto_
from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l1ll1lllll1_Krypto_ import l1lll1111l1_Krypto_, a2b_hex, b2a_hex
from l111ll1_Krypto_.l1lll1ll1_Krypto_ import *
from l111ll1_Krypto_ import l1ll1l11l1_Krypto_
from l111ll1_Krypto_.Signature import l11ll1l11_Krypto_ as l1l111l11_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
def l111l1l11l1_Krypto_(s):
        t = l1l1111_Krypto_ (u"ࠩࠪᤕ")
        try:
                t += s
        except TypeError:
                return 0
        return 1
def l1l1l111111_Krypto_(t):
    l1l1111_Krypto_ (u"ࠥࠦࠧࡘࡥ࡮ࡱࡹࡩࠥࡽࡨࡪࡶࡨࠤࡸࡶࡡࡤࡧࡶ࠰ࠥࡺࡡࡣࡵ࠯ࠤࡦࡴࡤࠡࡰࡨࡻࠥࡲࡩ࡯ࡧࡶࠤ࡫ࡸ࡯࡮ࠢࡤࠤࡸࡺࡲࡪࡰࡪࠦࠧࠨᤖ")
    for c in [l1l1111_Krypto_ (u"ࠫࡡࡴࠧᤗ"), l1l1111_Krypto_ (u"ࠬࡢࡴࠨᤘ"), l1l1111_Krypto_ (u"࠭ࠠࠨᤙ")]:
        t = t.replace(c,l1l1111_Krypto_ (u"ࠧࠨᤚ"))
    return t
def l1l1l111lll_Krypto_(t):
    l1l1111_Krypto_ (u"ࠣࠤࠥࡇࡴࡴࡶࡦࡴࡷࠤࡦࠦࡴࡦࡺࡷࠤࡸࡺࡲࡪࡰࡪࠤࡼ࡯ࡴࡩࠢࡥࡽࡹ࡫ࡳࠡ࡫ࡱࠤ࡭࡫ࡸࠡࡨࡲࡶࡲࠦࡴࡰࠢࡤࠤࡧࡿࡴࡦࠢࡶࡸࡷ࡯࡮ࡨࠤࠥࠦᤛ")
    l1l1l111l11_Krypto_ = b(l1l1l111111_Krypto_(t))
    if len(l1l1l111l11_Krypto_)%2 == 1:
        raise ValueError(l1l1111_Krypto_ (u"ࠤࡈࡺࡪࡴࠠ࡯ࡷࡰࡦࡪࡸࠠࡰࡨࠣࡧ࡭ࡧࡲࡢࡥࡷࡩࡷࡹࠠࡦࡺࡳࡩࡨࡺࡥࡥࠤᤜ"))
    return a2b_hex(l1l1l111l11_Krypto_)
class l1l1l111l1l_Krypto_(l1lll111111_Krypto_.TestCase):
        _1l1l1111ll_Krypto_ = (
                (
                {
                l1l1111_Krypto_ (u"ࠪࡲࠬᤝ"):l1l1111_Krypto_ (u"ࠫࠬ࠭࠰ࡢࠢ࠹࠺ࠥ࠽࠹ࠡ࠳ࡧࠤࡨ࠼ࠠ࠺࠺ࠣ࠼࠶ࠦ࠶࠹ࠢࡧࡩࠥ࠽ࡡࠡࡤ࠺ࠤ࠼࠺ࠠ࠲࠻ࠣࡦࡧࠦ࠷ࡧࠢࡥ࠴ࠥࡩ࠰ࠡ࠲࠴ࠤࡨ࠼ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠲࠸ࠢ࠴࠴ࠥ࠸࠷ࠡ࠲࠳ࠤ࠼࠻ࠠ࠲࠶ࠣ࠶࠾ࠦ࠴࠳ࠢࡨ࠵ࠥ࠿ࡡࠡ࠺ࡧࠤ࠽ࡩࠠ࠶࠳ࠣࡨ࠵ࠦ࠵࠴ࠢࡥ࠷ࠥ࡫࠳ࠡ࠹࠻ࠤ࠷ࡧࠠ࠲ࡦࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡨ࠹ࠥࡪࡣࠡ࠷ࡤࠤ࡫࠺ࠠࡦࡤࠣࡩ࠾ࠦ࠹࠵ࠢ࠹࠼ࠥ࠷࠷ࠡ࠲࠴ࠤ࠶࠺ࠠࡢ࠳ࠣࡨ࡫ࠦࡥ࠷ࠢ࠺ࡧࠥࡪࡣࠡ࠻ࡤࠤ࠾ࡧࠠࡧ࠷ࠣ࠹ࡩࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠼࠵ࠡ࠷࠹ࠤ࠷࠶ࠠࡣࡤࠣࡥࡧ࠭ࠧࠨᤞ"),
                l1l1111_Krypto_ (u"ࠬ࡫ࠧ᤟"):l1l1111_Krypto_ (u"࠭ࠧࠨ࠲࠴ࠤ࠵࠶ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠰࠲ࠩࠪࠫᤠ"),
                l1l1111_Krypto_ (u"ࠧࡥࠩᤡ"):l1l1111_Krypto_ (u"ࠨࠩࠪ࠴࠶ࠦ࠲࠴ࠢࡦ࠹ࠥࡨ࠶ࠡ࠳ࡥࠤࡦ࠹ࠠ࠷ࡧࠣࡨࡧࠦ࠱ࡥࠢ࠶࠺ࠥ࠽࠹ࠡ࠻࠳ࠤ࠹࠷ࠠ࠺࠻ࠣࡥ࠽ࠦ࠹ࡦࠢࡤ࠼ࠥ࠶ࡣࠡ࠲࠼ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡦ࠾ࠦ࠱࠳ࠢ࠵ࡩࠥ࠷࠴ࠡ࠲࠳ࠤࡨ࠶ࠠ࠺ࡣࠣࡨࡨࠦࡦ࠸ࠢ࠺࠼ࠥ࠺࠶ࠡ࠹࠹ࠤࡩ࠶ࠠ࠲ࡦࠣ࠶࠸ࠦ࠳࠶ࠢ࠹ࡥࠥ࠽ࡤࠡ࠶࠷ࠤࡩ࠼ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡢࡥࠢ࠻ࡦࠥࡪ࠵ࠡ࠲ࡨࠤ࠾࠺ࠠࡣࡨࠣࡧ࠼ࠦ࠲࠴ࠢࡩࡥࠥ࠾࠷ࠡࡦ࠻ࠤ࠽࠼ࠠ࠳ࡤࠣ࠻࠺ࠦ࠱࠸ࠢ࠺࠺ࠥ࠿࠱ࠡࡥ࠴ࠤ࠶ࡪࠠ࠸࠷ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠺࠺ࠥ࠿࠲ࠡࡦࡩࠤ࠽࠾ࠠ࠹࠳ࠪࠫࠬᤢ")
                },
                l1l1111_Krypto_ (u"ࠩࠪࠫ࠸࠶ࠠ࠹࠳ࠣࡥ࠹ࠦ࠰࠳ࠢ࠳࠵ࠥ࠶࠰ࠡ࠵࠳ࠤ࠹࠸ࠠ࠴࠳ࠣ࠴ࡧࠦ࠳࠱ࠢ࠳࠽ࠥ࠶࠶ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠴࠸ࠦ࠵࠶ࠢ࠳࠸ࠥ࠶࠶ࠡ࠳࠶ࠤ࠵࠸ࠠ࠶࠷ࠣ࠹࠸ࠦ࠳࠲ࠢ࠴ࡨࠥ࠹࠰ࠡ࠳ࡥࠤ࠵࠼ࠠ࠱࠵ࠣ࠹࠺ࠦ࠰࠵ࠢ࠳ࡥࠥ࠷࠳ࠡ࠳࠷ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠴࠶ࠢ࠺࠼ࠥ࠼࠱ࠡ࠸ࡧࠤ࠼࠶ࠠ࠷ࡥࠣ࠺࠺ࠦ࠲࠱ࠢ࠷ࡪࠥ࠽࠲ࠡ࠸࠺ࠤ࠻࠷ࠠ࠷ࡧࠣ࠺࠾ࠦ࠷ࡢࠢ࠹࠵ࠥ࠽࠴ࠡ࠸࠼ࠤ࠻࡬ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠹ࡩࠥ࠹࠱ࠡ࠳࠷ࠤ࠸࠶ࠠ࠲࠴ࠣ࠴࠻ࠦ࠰࠴ࠢ࠸࠹ࠥ࠶࠴ࠡ࠲࠶ࠤ࠶࠹ࠠ࠱ࡤࠣ࠹࠹ࠦ࠶࠶ࠢ࠺࠷ࠥ࠽࠴ࠡ࠴࠳ࠤ࠺࠻ࠠ࠸࠵ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠼࠵ࠡ࠹࠵ࠤ࠷࠶ࠠ࠴࠳ࠣ࠷࠵ࠦ࠵ࡣࠢ࠶࠴ࠥ࠶ࡤࠡ࠲࠹ࠤ࠵࠿ࠠ࠳ࡣࠣ࠼࠻ࠦ࠴࠹ࠢ࠻࠺ࠥ࡬࠷ࠡ࠲ࡧࠤ࠵࠷ࠠ࠱࠳ࠣ࠴࠶ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠲࠸ࠤ࠵࠶ࠠ࠱࠵ࠣ࠸ࡦࠦ࠰࠱ࠢ࠶࠴ࠥ࠺࠷ࠡ࠲࠵ࠤ࠹࠶ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠳ࡥࠥ࠼࠶ࠡ࠹࠼ࠤ࠶ࡪࠠࡤ࠸ࠣ࠽࠽ࠦ࠸࠲ࠢ࠹࠼ࠥࡪࡥࠡ࠹ࡤࠤࡧ࠽ࠠ࠸࠶ࠣ࠵࠾ࠦࡢࡣࠢ࠺ࡪࠥࡨ࠰ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡧ࠵ࠦ࠰࠲ࠢࡦ࠺ࠥ࠸࠷ࠡ࠳࠳ࠤ࠷࠽ࠠ࠱࠲ࠣ࠻࠺ࠦ࠱࠵ࠢ࠵࠽ࠥ࠺࠲ࠡࡧ࠴ࠤ࠾ࡧࠠ࠹ࡦࠣ࠼ࡨࠦ࠵࠲ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡩ࠶ࠠ࠶࠵ࠣࡦ࠸ࠦࡥ࠴ࠢ࠺࠼ࠥ࠸ࡡࠡ࠳ࡧࠤࡪ࠻ࠠࡥࡥࠣ࠹ࡦࠦࡦ࠵ࠢࡨࡦࠥ࡫࠹ࠡ࠻࠷ࠤ࠻࠾ࠠ࠲࠹ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠶࠱ࠡ࠳࠷ࠤࡦ࠷ࠠࡥࡨࠣࡩ࠻ࠦ࠷ࡤࠢࡧࡧࠥ࠿ࡡࠡ࠻ࡤࠤ࡫࠻ࠠ࠶ࡦࠣ࠺࠺ࠦ࠵࠷ࠢ࠵࠴ࠥࡨࡢࠡࡣࡥࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠰࠳ࠢ࠳࠷ࠥ࠶࠱ࠡ࠲࠳ࠤ࠵࠷ࠧࠨࠩᤣ"),
                l1l1111_Krypto_ (u"ࠪࠫࠬ࠶࠶ࠡࡦࡥࠤ࠸࠼ࠠࡤࡤࠣ࠵࠽ࠦࡤ࠴ࠢ࠷࠻ࠥ࠻ࡢࠡ࠻ࡦࠤ࠵࠷ࠠࡥࡤࠣ࠷ࡨࠦ࠷࠹ࠢ࠼࠹ࠥ࠸࠸ࠡ࠲࠻ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠰࠳ࠢ࠺࠽ࠥࡨࡢࠡࡣࡨࠤ࡫࡬ࠠ࠳ࡤࠣ࠻ࡩࠦ࠵࠶ࠢ࠻ࡩࠥࡪ࠶ࠡ࠸࠴ࠤ࠺࠿ࠠ࠹࠹ࠣࡧ࠽ࠦ࠵࠲ࠢ࠻࠺ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠴ࡨࠣ࠼ࡦࠦ࠶ࡤࠢ࠵ࡧࠥ࡬ࡦࠡࡤࡦࠤ࠽࠿ࠠࡤ࠵ࠣࡪ࠼ࠦ࠵ࡢࠢ࠴࠼ࠥࡪ࠹ࠡ࠸ࡥࠤ࠶࠸ࠠ࠸ࡥࠣ࠻࠶ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠹ࡧࠤ࠺࠺ࠠࡥ࠲ࠣࡨ࠽ࠦ࠰࠵ࠢ࠻ࡨࠥࡧ࠸ࠡࡣ࠳ࠤ࠺࠺ࠠ࠵࠸ࠣ࠶࠻ࠦࡤ࠲ࠢ࠺ࡥࠥ࠸ࡡࠡ࠺ࡩࠤࡧ࡫ࠧࠨࠩᤤ"),
                l1lllll1l1_Krypto_
                ),
                (
                l1l1111_Krypto_ (u"ࠦࠧࠨ࠭࠮࠯࠰࠱ࡇࡋࡇࡊࡐࠣࡖࡘࡇࠠࡑࡔࡌ࡚ࡆ࡚ࡅࠡࡍࡈ࡝࠲࠳࠭࠮࠯ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡓࡉࡊࡄࡒࡻࡎࡈࡁࡂࡌࡅࡅࡑ࠾ࡥࡋ࠷ࡄࡏࡴࡏࡳ࡫ࡗࡕࡴࡨࡋ࡯ࡈࡷࡥ࡞ࡒࡾࡌࡅ࠹࠮࡯࡙࠱ࡔࡍࡴ࠺࡙ࡰࡼࡅࡵࡈࡵࡖ࡭ࡊࡄࡌࡏࡷࡹࡎࡏࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡴ࠵࠾ࡌࡲࡍ࠶ࡳ࡙ࡎࡓࡹ࡮ࡒࡐࡗࡑࡈ࡮࠴ࡪࡍࡐࡪ࠹࠰ࡅࡹ࠷࠼ࡌࡗࡍ࠵ࡗࡆࡅࡼࡋࡁࡂࡓࡍࡅࡈ࡛ࡓࡅࡇࡳ࠼ࡗ࡚ࡥ࠴࠴ࡩࡸࡶ࠾ࡉࡸࡉ࠻ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡗࡰ࡬࡯࠹ࡲࡇࡤ࠲ࡹࡉ࡭ࡎࡕࡲ࡛࠱ࡘࡺ࠽ࡨ࠹࠷࠵࡚ࡎࡔࡐࡩࡶࡓࡦ࡚ࡓ࠸࠹ࡷࡺࡘ࠹࠰ࡓࡹ࠺ࡉࡓ࡞࠼ࡘࡁ࠴ࡪࡵࡈࡇࡋࡁࡰࡊࡘࡈࡕࡸࡉࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡓࡖࡏࡨࡂࡒࡌࡔࡑࢀ࠴ࡥࡲ࡫࡭ࡉ࠿ࡩ࡮ࡃ࡮࡭ࡻ࡟࠳࠲ࡔࡦ࠹ࡆ࡬ࡈࡋ࡫ࡔࡖࡆ࠽ࡘࡪࡺࡗࡧ࡯ࡋ࡫ࡰ࡬ࡄ࡭ࡊࡇࡹࡩ࠱ࡳࡎࡍࡱࡳ࠰ࡏ࡯ࡶࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠬࡴࡧࡔࡓࡋࡰࡰࡶࡅ࡮࡫࡜࠴ࡎ࠶ࡅ࡯࡬ࡍࡁࡂ࠱࡬ࡴࡨࡳࡡࡂ࡬ࡦࡇࡎࡗࡃࡉࡸ࡫ࡻࡼࡑࡖࡃࡎࡽࡾ࡙ࡹࡣࡕ࠴ࡋࡩ࡚ࡪࡅࡦࡄࡐࡳ࡮࡞ࡘࡌࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡏࡇࡃࡂࡴ࠶ࡷࡏࡗࡊࡈࡺࡌࡕࡎ࡭ࡡࡳࡔࡳ࠯ࡲ࠷ࡗࡔࡍ࡙࠵ࡒࡩࡩࡸࡏࡤࡘࡔࡴࡢࡖ࠹ࡺࡼࡋࡹ࠹ࡅࡒ࠴ࡴࡻࡧ࠷࠷࡮࡜ࡆࡿ࡭ࡕࡄࡋࡔࡇ࠾ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡰ࠳ࡇࡳࡠࡃࡋ࠸ࡌ࡞࡞ࡷࡓࡵ࠲ࡋ࠹ࡓ࠽ࠫࡒ࠭࠵ࡖࡴ࠼࠴࡯ࡷࡺ࡚࠴ࡕࡓࡒࡨࡐ࠺ࡸࡈࡷࡒ࠿ࡀࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭࠮࠯࠰࠱ࡊࡔࡄࠡࡔࡖࡅࠥࡖࡒࡊࡘࡄࡘࡊࠦࡋࡆ࡛࠰࠱࠲࠳࠭ࠣࠤࠥᤥ"),
                l1l1111_Krypto_ (u"࡚ࠧࡨࡪࡵࠣ࡭ࡸࠦࡡࠡࡶࡨࡷࡹࡢࡸ࠱ࡣࠥᤦ"),
                l1l1111_Krypto_ (u"࠭ࠧࠨ࠶ࡤ࠻࠵࠶ࡡ࠲࠸࠷࠷࠷ࡧ࠲࠺࠳ࡤ࠷࠶࠿࠴࠷࠶࠹࠽࠺࠸࠶࠹࠹ࡧ࠹࠸࠷࠶࠵࠷࠻ࡦ࠽ࡨ࠸࠷ࡨࡥ࠴ࡦ࠸࠵ࡢࡣ࠶࠴ࡪ࠶ࡤࡤࡧࡦࡨࡧࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠶࠷࠶࠻࠽࠶࠸࠷࠼ࡥࡨ࠼࠳ࡥ࠷࠹ࡩࡨ࠷࠴࠺࠻ࡦ࠷ࡦ࡫࠴ࡤ࠲࠳࠵࠸ࡩ࠲࠱࠷࠶ࡧࡦࡨࡤ࠶ࡤ࠸࠼࠵࠺࠸࠵࠺࠼࠽࠹࠻࠴࠲ࡣࡦ࠵࠻ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡨࡤ࠶࠹࠹ࡡ࠵ࡦࠪࠫࠬᤧ"),
                l1l111lll_Krypto_
                ),
                (
                {
                    l1l1111_Krypto_ (u"ࠧ࡯ࠩᤨ"):l1l1111_Krypto_ (u"ࠨࠩࠪࡉ࠵࠾࠹࠸࠵࠶࠽࠽ࡊࡄ࠹ࡈ࠸ࡊ࠺ࡋ࠸࠹࠹࠺࠺࠸࠿࠷ࡇ࠶ࡈࡆ࠵࠶࠵ࡃࡄ࠸࠷࠽࠹ࡄࡆ࠲ࡉࡆ࠼ࡇࡂࡅࡅ࠺ࡈࡈ࠽࠷࠶࠴࠼࠴ࡉ࠶࠵࠳ࡇ࠹ࡈࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠶࠸ࡄࡇࡃ࠹࠼࠻࠸࠶ࡅ࠶ࡇ࠶࠻ࡌࡁࡂ࠷࠻࠶࠾ࡌࡃ࠺࠹ࡈࡇࡋࡇ࠸࠳࠷࠴࠴ࡋ࠹࠰࠹࠲ࡅࡉࡇ࠷࠵࠱࠻ࡈ࠸࠻࠺࠴ࡇ࠳࠵ࡇࡇࡈࡄ࠹࠵࠵ࡇࡋࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡉ࠶࠷࠺࠹ࡊ࠵࠽ࡄ࠺ࡄ࠳࠺࠵ࡇࡃࡃࡇࡈࡉ࠸࠺࠰࠺࠸ࡄ࠵࠸ࡌ࠵ࡇ࠹࠳࠹࠵࠻࠹࠴ࡆࡉ࠹ࡊࡈࡁ࠴࠷࠸࠺ࡉ࠿࠶࠲ࡈࡉ࠵࠾࠽ࡆࡄ࠻࠻࠵ࡊ࠼ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡆ࠹࠸ࡆࡉࡆ࠾࠷࠵࠲࠺࠴ࡊࡌࡁࡄ࠸ࡇ࠶ࡈ࠽࠴࠺ࡈ࠵ࡈࡋࡇ࠵࠶࠵ࡄࡆ࠾࠿࠹࠸࠹࠳࠶ࡆ࠼࠴࠹࠷࠵࠼ࡈ࠺ࡅࡇ࠵࠸࠻࠸࠾࠵࠸࠹࠷࠹࠼࠻ࡆࠨࠩࠪᤩ"),
                    l1l1111_Krypto_ (u"ࠩࡨࠫᤪ"):l1l1111_Krypto_ (u"ࠪࠫࠬ࠶࠱࠱࠲࠳࠵ࠬ࠭ࠧᤫ"),
                    l1l1111_Krypto_ (u"ࠫࡩ࠭᤬"):l1l1111_Krypto_ (u"ࠬ࠭ࠧ࠱࠲ࡄ࠸࠵࠹ࡃ࠴࠴࠺࠸࠼࠽࠶࠴࠶࠶࠸࠻ࡉࡁ࠷࠺࠹ࡆ࠺࠽࠹࠵࠻࠳࠵࠹ࡈ࠲ࡆ࠺ࡄࡈ࠷ࡉ࠸࠷࠴ࡅ࠶ࡈ࠽ࡄ࠸࠶࠻࠴࠾࠼ࡁ࠹ࡄ࠼࠵ࡋ࠽࠳࠷ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡈ࠵࠻࠺ࡊ࠶ࡆ࠺ࡆࡈ࠶࠻࠹࠱࠸࠳࠶࠼࠹࠱࠵࠹࠶࠹࠻࠺࠴ࡅ࠻࠸ࡇࡉ࠼࠷࠷࠵ࡆࡉࡇ࠺࠹ࡇ࠷࠹ࡅࡈ࠸ࡆ࠴࠹࠹ࡉ࠶ࡉࡅࡆ࠲ࡈࡆࡋ࠸࠸࠳ࡆࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡉ࠸࠸࠿࠹࠱࠸ࡉ࠷࠹ࡊ࠸࠷ࡇ࠳࠼࠺ࡈࡄ࠶࠸࠸࠺ࡆࡊ࠸࠵࠳ࡉ࠷࠶࠹ࡄ࠸࠴ࡇ࠷࠾࠻ࡅࡇࡇ࠶࠷ࡈࡈࡆࡇ࠴࠼ࡉ࠹࠶࠳࠱ࡄ࠶ࡈ࠵࠻ࡁ࠳࠺ࡉࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡆ࠼ࡌ࠱࠹ࡇࡄ࠶࠼࠼࠳࠸ࡄ࠳࠻࠾࠻࠷ࡅ࠵࠵ࡊ࠷ࡈࡄࡆ࠺࠺࠴࠻࠸࠲࠸ࡆ࠳࠸࠻࠼࠵ࡆࡅ࠼࠵ࡇࡇࡆ࠹ࡄ࠴ࡅࡈ࠹ࡅࡄ࠻࠴࠸࠹ࡇࡂ࠸ࡈ࠵࠵ࠬ࠭ࠧ᤭")
                },
                l1l1111_Krypto_ (u"ࠨࡡࡣࡥࠥ᤮"),
                l1l1111_Krypto_ (u"ࠧࠨࠩ࠹࠴ࡆࡊ࠵ࡂ࠹࠻ࡊࡇ࠺ࡁ࠵࠲࠶࠴ࡊࡉ࠵࠵࠴ࡆ࠼࠾࠽࠴ࡄࡆ࠴࠹ࡋ࠻࠵࠴࠺࠷ࡉ࠽࠹࠶࠶࠷࠷ࡇࡊࡊࡄ࠺ࡃ࠶࠶࠷ࡊ࠵ࡇ࠶࠴࠷࠺ࡉ࠶࠳࠸࠺ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡁ࠺ࡆ࠵࠴࠾࠽࠰ࡄ࠷࠷ࡉ࠻࠼࠵࠲࠲࠺࠴ࡇ࠶࠱࠵࠶ࡇ࠸࠸࠾࠴࠵ࡅ࠻࠽࠾࠹࠲࠱ࡆࡇ࠼ࡋࡇ࠷࠹࠳࠼ࡊ࠼ࡋࡂࡄ࠸ࡄ࠻࠼࠷࠵࠳࠺࠺࠷࠸࠸ࡅࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡇ࠽࠼࠷࠶ࡅ࠴࠷࠻࠷࠸࠴ࡄ࠶ࡊ࠽ࡇ࠱ࡇ࠺࠴ࡉࡋ࠿࠶࠺࠶࠴࠼࠷࠼࠷࠲࠵࠳ࡅ࠼࠻࠶ࡇࡆࡅࡆ࠷ࡉ࠷࠲ࡆ࠼ࡅ࠻࠼࠷࠵࠶࠹ࡉ࠸࠺ࡅ࠱ࡇࡄࡈࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠺ࡅࡉ࠷࠶ࡈࡆࡃ࠸࠹ࡊ࠽࠷࠶ࡇ࠵࠴࠽ࡉ࠶ࡂ࠸ࡇ࠷࠷࠵ࡇ࠵ࡇ࠴࠻࠽࠶࠻࠵࠴࠻࠻࠺ࡊ࠶࠰࠴࠹࠵࠴࠷࠼࠱ࡄ࠹ࡈ࠽࠵࠸࠲ࡄ࠲ࡇ࠽ࡋ࠷࠱ࡇࠩࠪࠫ᤯"),
                l1l111lll_Krypto_
                )
        )
        def l111l1l11ll_Krypto_(self):
                for i in range(len(self._1l1l1111ll_Krypto_)):
                        row = self._1l1l1111ll_Krypto_[i]
                        if l111l1l11l1_Krypto_(row[0]):
                                key = l1l11lll1_Krypto_.l11ll1111l_Krypto_(row[0])
                        else:
                                comps = [ int(l1l1l111111_Krypto_(row[0][x]),16) for x in (l1l1111_Krypto_ (u"ࠨࡰࠪᤰ"),l1l1111_Krypto_ (u"ࠩࡨࠫᤱ"),l1l1111_Krypto_ (u"ࠪࡨࠬᤲ")) ]
                                key = l1l11lll1_Krypto_.l1l1l1111l_Krypto_(comps)
                        h = row[3].new()
                        try:
                            h.update(l1l1l111lll_Krypto_(row[1]))
                        except:
                            h.update(b(row[1]))
                        l111l1l1l11_Krypto_ = l1l111l11_Krypto_.new(key)
                        self.assertTrue(l111l1l1l11_Krypto_.l1l11ll1l1_Krypto_())
                        s = l111l1l1l11_Krypto_.l1l11lll11_Krypto_(h)
                        self.assertEqual(s, l1l1l111lll_Krypto_(row[2]))
        def l1l11llllll_Krypto_(self):
                for i in range(len(self._1l1l1111ll_Krypto_)):
                        row = self._1l1l1111ll_Krypto_[i]
                        if l111l1l11l1_Krypto_(row[0]):
                                key = l1l11lll1_Krypto_.l11ll1111l_Krypto_(row[0]).l1l11l111l_Krypto_()
                        else:
                                comps = [ int(l1l1l111111_Krypto_(row[0][x]),16) for x in (l1l1111_Krypto_ (u"ࠫࡳ࠭ᤳ"),l1l1111_Krypto_ (u"ࠬ࡫ࠧᤴ")) ]
                                key = l1l11lll1_Krypto_.l1l1l1111l_Krypto_(comps)
                        h = row[3].new()
                        try:
                            h.update(l1l1l111lll_Krypto_(row[1]))
                        except:
                            h.update(b(row[1]))
                        l111l1l1l1l_Krypto_ = l1l111l11_Krypto_.new(key)
                        self.assertFalse(l111l1l1l1l_Krypto_.l1l11ll1l1_Krypto_())
                        result = l111l1l1l1l_Krypto_.l1l11l1l11_Krypto_(h, l1l1l111lll_Krypto_(row[2]))
                        self.assertTrue(result)
        def l111l1l1ll1_Krypto_(self):
                        rng = l1ll1l11l1_Krypto_.new().read
                        key = l1l11lll1_Krypto_.l1llllll1_Krypto_(1024, rng)
                        for l1l11ll1111_Krypto_ in (l1lllll1l1_Krypto_,l1llllllll_Krypto_,l1l111lll_Krypto_,l1lll1lll1_Krypto_,l1lll1ll11_Krypto_,l1lll1l111_Krypto_,l1lll11ll1_Krypto_,l1llll11l1_Krypto_):
                            h = l1l11ll1111_Krypto_.new()
                            h.update(b(l1l1111_Krypto_ (u"࠭ࡢ࡭ࡣ࡫ࠤࡧࡲࡡࡩࠢࡥࡰࡦ࡮ࠧᤵ")))
                            l111l1l1l11_Krypto_ = l1l111l11_Krypto_.new(key)
                            s = l111l1l1l11_Krypto_.l1l11lll11_Krypto_(h)
                            result = l111l1l1l11_Krypto_.l1l11l1l11_Krypto_(h, s)
                            self.assertTrue(result)
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    tests = []
    tests += l1lll1111l1_Krypto_(l1l1l111l1l_Krypto_)
    return tests
if __name__ == l1l1111_Krypto_ (u"ࠧࡠࡡࡰࡥ࡮ࡴ࡟ࡠࠩᤶ"):
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧᤷ"))