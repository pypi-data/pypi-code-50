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
__revision__ = l1l1111_Krypto_ (u"ࠣࠦࡌࡨࠩࠨᗓ")
import unittest as l1lll111111_Krypto_
import sys as l1l11l11_Krypto_
from l111ll1_Krypto_.l11l11l1_Krypto_ import l1l11lll1_Krypto_
from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l1ll1lllll1_Krypto_ import l1lll1111l1_Krypto_, a2b_hex, b2a_hex
from l111ll1_Krypto_ import l1ll1l11l1_Krypto_
from l111ll1_Krypto_.l11111l_Krypto_ import l11ll1l11_Krypto_ as l1l111l11_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
def l1l1l111111_Krypto_(t):
    l1l1111_Krypto_ (u"ࠤࠥࠦࡗ࡫࡭ࡰࡸࡨࠤࡼ࡮ࡩࡵࡧࠣࡷࡵࡧࡣࡦࡵ࠯ࠤࡹࡧࡢࡴ࠮ࠣࡥࡳࡪࠠ࡯ࡧࡺࠤࡱ࡯࡮ࡦࡵࠣࡪࡷࡵ࡭ࠡࡣࠣࡷࡹࡸࡩ࡯ࡩࠥࠦࠧᗔ")
    for c in [l1l1111_Krypto_ (u"ࠪࡠࡳ࠭ᗕ"), l1l1111_Krypto_ (u"ࠫࡡࡺࠧᗖ"), l1l1111_Krypto_ (u"ࠬࠦࠧᗗ")]:
        t = t.replace(c,l1l1111_Krypto_ (u"࠭ࠧᗘ"))
    return t
def l1l1l111lll_Krypto_(t):
    l1l1111_Krypto_ (u"ࠢࠣࠤࡆࡳࡳࡼࡥࡳࡶࠣࡥࠥࡺࡥࡹࡶࠣࡷࡹࡸࡩ࡯ࡩࠣࡻ࡮ࡺࡨࠡࡤࡼࡸࡪࡹࠠࡪࡰࠣ࡬ࡪࡾࠠࡧࡱࡵࡱࠥࡺ࡯ࠡࡣࠣࡦࡾࡺࡥࠡࡵࡷࡶ࡮ࡴࡧࠣࠤࠥᗙ")
    l1l1l111l11_Krypto_ = b(l1l1l111111_Krypto_(t))
    if len(l1l1l111l11_Krypto_)%2 == 1:
        print(l1l1l111l11_Krypto_)
        raise ValueError(l1l1111_Krypto_ (u"ࠣࡇࡹࡩࡳࠦ࡮ࡶ࡯ࡥࡩࡷࠦ࡯ࡧࠢࡦ࡬ࡦࡸࡡࡤࡶࡨࡶࡸࠦࡥࡹࡲࡨࡧࡹ࡫ࡤࠣᗚ"))
    return a2b_hex(l1l1l111l11_Krypto_)
class l1l1l111l1l_Krypto_(l1lll111111_Krypto_.TestCase):
        def setUp(self):
                self.rng = l1ll1l11l1_Krypto_.new().read
                self.l1l1l11l11l_Krypto_ = l1l11lll1_Krypto_.l1llllll1_Krypto_(1024, self.rng)
        _1l1l1111ll_Krypto_ = (
                (
                l1l1111_Krypto_ (u"ࠩࠪࠫ࠲࠳࠭࠮࠯ࡅࡉࡌࡏࡎࠡࡔࡖࡅࠥࡖࡒࡊࡘࡄࡘࡊࠦࡋࡆ࡛࠰࠱࠲࠳࠭ࠋࡏࡌࡍࡈ࡞ࡁࡊࡄࡄࡅࡐࡈࡧࡒࡆࡄ࡭ࡆࡴࡶࡊࡃࡒࡺࡶ࡜ࡷࡋࡖࡤ࡝ࡿࡹࡋ࡯ࡧࡩ࡞࡫ࡺࡧࡵ࡚ࡊࡉ࠷࡮ࡐࡋࡲࡳࡋࡸ࡝࡬࠸࠺ࡼࡾ࠾ࡰࡥ࡙࡛ࠍ࡛࠴ࡌࡸ࡙࠱ࡪࡘࡕ࡛ࡒࡂࡴࡑ࡬ࡩࡴࡨࡑ࠸ࡱ࠷ࡵ࠸࡚ࡢࡆࡌࡆࡷࡕ࠲ࡻ࡫ࡽࡦ࡬ࡏࡘࡴ࠲ࡌࡷࡱࡰࡔࡕࡥࡵ࠸ࡻࡴࡉ࠹ࡨࡐ࡜ࡿࡿࡎࡖࡑ࡭ࡅࠏࢀࡐ࠴ࡰࡽࡑࡶࡠࡄ࡛ࡍ࠹࠻࠺࠽ࡘࡒࡃࡲࡦࡔࡹࡳࡎ࡭ࡅࡊࡶࡘࡗࡸ࡫࡯ࡘ࠴࠹ࡄࡴࡄ࡫ࡖࡵࡲ࠳ࡪࡏࡘ࡬ࡋ࠱ࡷࡷࡲࡗࡗࡍ࡫ࡷࡊࡆࡄࡕࡆࡈࠊࡂࡱࡊࡅࡈ࠺ࡈࡗ࠱࡬ࡲࡔࡸࡰࡨࡖࡹࡗࡦࡨ࠸ࡘ࡬࠳ࡶ࡮ࡿ࡚ࡨࡓࡒ࡞࠸࡛࠳࡛ࡲࡖࡰࡸ࡬ࡒ࠹ࡴࡤ࠽ࡎࡨ࠹ࡖࡧࡨ࠷࡯ࡉ࡙࡯ࡍࡶࡧࡺ࠼ࡇ࡬ࠌࡼ࠺ࡿࡏ࠯ࡤࡦࡷ࠼ࡊࡖࡊ࠵ࡒࡸࡻࡆ࡝ࡓࡏࡌࡽࡦࡵࡨࡖࡢࡆࡹ࡙ࡶ࠸࠵ࡐࡆ࠮ࡇ࡝࠾࠯ࡶࡔࡗ࠴࠽ࡿࡂࡔ࠶ࡍ࠼࡙ࢀࡂࡪࡶ࡝ࡎ࡙ࡊ࠴࡭ࡕ࠺ࠎࡦࡺࡤࡕࡰࡎࡘ࠵࡝࡭ࡸ࡭࠮ࡹ࠽ࡺࡄࡣࡪࡹࡑࡐࡽ࡮ࡖࡊࡧࡎࡑࡩࡵࡊࡵࡼࡧࡹࡹ࠹ࡳࡹࡍ࡚ࡦࡶࡕࡵ࡭ࡆࡕࡖࡊࡶࡅࡲࡻ࠶ࡏࡓࡵ࡯࠲࡜ࡏࡌࠐࡵࡖࡶࡷ࡮ࡲࡒ࠸ࡰࡌ࠶࡙࠵ࡳ࠳࡛ࡸࡐࡨ࡛ࡽࡂࡦࡥࡄ࠴ࡪ࡫ࡢ࡛ࡤ࠴ࡰ࠷ࡐ࠵ࡑࡸࡌ࠷ࡊࡐࡄ࠺࠹ࡨࡏࡪ࠿࠱ࡏࡵࡺ࠼࡙࠹࡬ࡸࡲࡲࡒ࠹࠶࡫ࠋࡋࡲࡧࡘ࡜ࡄ࡬࡮ࡄ࡯ࡊࡇࡺࡪ࠳ࡋࡐࡍࡋ࠶ࡆࡼ࡙ࡔࡔ࡫࠵࡛ࠬ࠳࡯ࡌࡼࡲࡊ࡛ࡕࡖ࡭ࡴࡣࡐࡤ࠺࠶ࡻࡉࡶࡃ࡜ࡹࡈ࠻ࡽࡌ࡛ࡲࡔ࡫ࡶࡵ࠶ࡤ࠶ࠍࡨ࠸࡞ࡈࡇࡄࡅࡕ࡜ࡇ࠶ࡹࡥࡹࡕࡧ࠻ࡷࠬࡘ࡙ࡉࡏࡠࡺࡸ࠸࠷ࡽ࠷࠻ࡳࡉࡹࡍࡆࡆࡓ࡙ࡓࡧࡕࡰ࠻࡙ࡺࡍ࠲ࡴࡅ࠵ࡽࡉ࡚ࡴ࡜࡛ࡷࡕࡴ࠹ࡌࡨࡕࠏ࠾࡭ࡵࡪࡸࡰࡨ࡝ࡈ࡙࡯ࡴࡘ࡬ࡉ࠶ࡇࡇ࡛ࡔ࠾ࡋࡳ࠶ࡉࡇ࠻࠴࡬ࡵࡌ࡮࠷ࡻࡶࡒࡋ࡛ࡩࡌࡦࡍ࠺࡮ࡲࡸࡹࡋࡦࡿ࠷ࡹ࡚ࡏࡇ࡝ࡊ࠯ࡆࡅࡔࡌ࠾ࡧࠊ࠲ࡌ࡜ࡒࡒࡺࡒࡦࡰ࠸ࡹࡳ࡙ࡁࡣࡋࡒࡼࡗࡩࡋ࡬࡙ࡽ࠽࠷ࡌ࠰ࡍࡍࡳࡱ࠾ࡠࡗ࠰ࡕ࠼ࡺࡋࡎࡏࠬ࡯ࡅࡧࡈࡲࡍࡈࡱࡎࡎࡍ࡯ࡵࡒࡺࡏࡆࡸࡒࡢࡕࠌࡑࡸࡊࡠࡦࡔࡌ࡝ࡅࡪ࡙࠲ࡴࡗࡷࡲ࠸࠵࠰ࡄࡓࡇࡦ࠷ࡓ࠲ࡻࡐࡅࡘࡋ࠾ࡌ࡭ࡏ࠳ࡲࡽࡳࡨ࠱࡭࠼࡚ࡌࡳ࠵ࡕࡘࡌࡽࡇࡋࡍࡤ࡫ࡳࡱࡻࡕࡧࡲࡋࡶࠎࡍࡑࡵ࡬࡙ࡅࡧࡶ࠿ࡦ࠰ࡗࡒࡱࡘ࠶࡯ࡆࡪࡤ࡭࠴࠼ࡧࠬࡗࡩ࠻࡛ࡎࡊࡥ࡙ࡤࡩࡔ࠻ࡌࡻࡷࡹࡻ࡚ࡃࠊ࠮࠯࠰࠱࠲ࡋࡎࡅࠢࡕࡗࡆࠦࡐࡓࡋ࡙ࡅ࡙ࡋࠠࡌࡇ࡜࠱࠲࠳࠭࠮ࠩࠪࠫᗛ"),
                l1l1111_Krypto_ (u"࡚ࠪࠫࠬࡈࡊࡕࠣࡍࡘࠦࡐࡍࡃࡌࡒ࡙ࡋࡘࡕ࡞ࡻ࠴ࡆ࠭ࠧࠨᗜ"),
                l1l1111_Krypto_ (u"ࠫࠬ࠭࠳ࡧࠢࡧࡧࠥ࡬ࡤࠡ࠵ࡦࠤࡨࡪࠠ࠶ࡥࠣ࠽ࡧࠦ࠱࠳ࠢࠣࡥ࡫ࠦ࠶࠶ࠢ࠶࠶ࠥ࡫࠳ࠡࡨ࠺ࠤࡩ࠶ࠠࡥࡣࠣ࠷࠻ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠺ࡩࠤ࠽࡬ࠠࡥ࠻ࠣࡩ࠸ࠦ࠱࠴ࠢ࠴ࡧࠥ࠽ࡦࠡࡥ࠻ࠤࠥࡨ࠳ࠡࡨ࠼ࠤࡨ࠷ࠠ࠱࠺ࠣࡩ࠹ࠦࡥࡣࠢ࠺࠽ࠥ࠿ࡣࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠽࠶ࠦ࠸࠺ࠢ࠴ࡪࠥ࠿࠶ࠡ࠵ࡥࠤ࠾࠺ࠠ࠸࠹ࠣ࠺࠶ࠦࠠ࠺࠻ࠣࡥ࠹ࠦࡢ࠲ࠢࡨࡩࠥ࠻ࡤࠡࡧ࠹ࠤ࠶࠽ࠠࡤ࠻ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠻ࡤࠡ࠲ࡤࠤࡧ࠻ࠠ࠷࠵ࠣ࠹࠷ࠦ࠰ࡢࠢࡨࡦࠥ࠶࠰ࠡࠢ࠷࠹ࠥ࠹࠸ࠡ࠴ࡤࠤ࡫ࡨࠠࡣ࠲ࠣ࠻࠶ࠦ࠳ࡥࠢ࠴࠵ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡧ࠹ࠣࡥ࠶ࠦ࠹ࡦࠢࡤ࠻ࠥ࠼࠹ࠡࡤ࠶ࠤࡦ࡬ࠠ࠷࠳ࠣࠤࡨ࠶ࠠࡣࡤࠣ࠴࠹ࠦ࠵ࡣࠢ࠸ࡨࠥ࠺ࡢࠡ࠴࠺ࠤ࠹࠺ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠴ࡪࠥ࠻ࡢࠡ࠻࠺ࠤ࠽࠿ࠠࡣࡣࠣ࠺ࡦࠦ࠰࠹ࠢ࠼࠹ࠥࠦࡥࡦࠢ࠷ࡪࠥࡧ࠲ࠡࡧࡥࠤ࠺࠼ࠠ࠷࠶ࠣࡩ࠺ࠦ࠰ࡧࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡩࡧࠠ࠸ࡥࠣࡪ࠾ࠦ࠹ࡢࠢ࠹࠵ࠥ࠼࠱ࠡ࠲࠹ࠤ࠻࠸ࠠࠡࡧࡧࠤࡦ࠶ࠠࡣࡥࠣ࠹࡫ࠦࡡࡢࠢ࠹ࡧࠥ࠹࠱ࠡ࠹࠻ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠷࠱ࠢ࠵࠼ࠥ࠷ࡡࠡࡤࡥࠤ࠾࠾ࠠ࠴ࡥࠣࡩ࠸ࠦ࠶ࡢࠢࠣ࠺࠵ࠦ࠳ࡤࠢࡧ࠵ࠥ࠶ࡢࠡ࠲ࡩࠤ࠺ࡧࠠࡧ࠶ࠣ࠻࠺࠭ࠧࠨᗝ"),
                l1l1111_Krypto_ (u"ࠬ࠭ࠧࡦࡤࠣࡨ࠼ࠦ࠷ࡥࠢ࠻࠺ࠥࡧ࠴ࠡ࠵࠸ࠤ࠷࠹ࠠࡢ࠵ࠣ࠹࠹ࠦ࠷ࡦࠢ࠳࠶ࠥ࠶ࡢࠡ࠶࠵ࠤ࠶ࡪࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠹࠵ࠥ࠼ࡣࠡࡣࡩࠤ࠻࠽ࠠࡣ࠺ࠣ࠸ࡪࠦ࠱࠸ࠢ࠸࠺ࠥ࠾࠰ࠡ࠸࠹ࠤ࠸࠼ࠠ࠱࠶ࠣ࠺࠹ࠦ࠳࠵ࠢ࠵࠺ࠥ࠾ࡡࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠸࠼ࠦࡤࡥࠢ࠷࠸ࠥࡨ࠳ࠡ࠳ࡤࠤࡧ࠸ࠠ࠲࠹ࠣ࠺࠵ࠦࡦ࠵ࠢ࠼࠵ࠥ࠸ࡥࠡࡧ࠵ࠤࡧ࠻ࠠ࠺࠷ࠣ࠺࠹ࠦࡣࡤࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡫࠿ࠠࡥࡣࠣࡧ࠽ࠦ࠷࠱ࠢ࠼࠸ࠥ࠻࠴ࠡ࠺࠹ࠤ࠹ࡩࠠࡦࡨࠣ࠹ࡧࠦ࠰࠹ࠢ࠺ࡨࠥ࠷࠸ࠡࡥ࠷ࠤࡦࡨࠠ࠹ࡦࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠶࠴ࠡ࠲࠹ࠤ࠸࠹ࠠ࠹ࡨࠣࡧࡦࠦ࠱࠶ࠢ࠸ࡪࠥ࠻࠲ࠡ࠸࠳ࠤ࠽ࡧࠠࡢ࠳ࠣ࠴ࡨࠦࡦ࠶ࠢ࠳࠼ࠥࡨ࠵ࠡ࠶ࡦࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡢࡣࠢ࠼࠽ࠥࡨ࠸ࠡ࠻࠷ࠤ࠷࠻ࠠ࠱࠶ࠣ࠽ࡨࠦࡥ࠷ࠢ࠳࠵ࠥ࠽࠵ࠡࡧ࠹ࠤ࡫࠿ࠠ࠷࠵ࠣ࠻ࡦࠦ࠶࠶ࠢ࠹࠵ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠲࠵ࠣ࠼ࡦࠦࡡ࠸ࠢ࠷࠻ࠥ࠽࠷ࠡ࠺࠴ࠤࡦ࡫ࠠ࠱ࡦࠣࡦ࠽ࠦ࠲ࡤࠢ࠷ࡨࠥ࠻࠰ࠡࡣ࠸ࠫࠬ࠭ᗞ")
                ),
        )
        def l1l11lllll1_Krypto_(self):
                for test in self._1l1l1111ll_Krypto_:
                        key = l1l11lll1_Krypto_.l11ll1111l_Krypto_(test[0])
                        class l1l11llll11_Krypto_:
                            def __init__(self, data):
                                self.data = data
                                self.idx = 0
                            def __call__(self, l11l1111l1_Krypto_):
                                r = self.data[self.idx:l11l1111l1_Krypto_]
                                self.idx += l11l1111l1_Krypto_
                                return r
                        key._11l1lll11_Krypto_ = l1l11llll11_Krypto_(l1l1l111lll_Krypto_(test[3]))
                        l1llll11l_Krypto_ = l1l111l11_Krypto_.new(key)
                        ct = l1llll11l_Krypto_.l1_Krypto_(b(test[1]))
                        self.assertEqual(ct, l1l1l111lll_Krypto_(test[2]))
        def l1l1l11l1l1_Krypto_(self):
                l1l11llll1l_Krypto_ = l1l1111_Krypto_ (u"࠭࡜ࡹ࠲࠳ࠫᗟ")*(128-11+1)
                l1llll11l_Krypto_ = l1l111l11_Krypto_.new(self.l1l1l11l11l_Krypto_)
                self.assertRaises(ValueError, l1llll11l_Krypto_.l1_Krypto_, l1l11llll1l_Krypto_)
        def l1l11llllll_Krypto_(self):
                for test in self._1l1l1111ll_Krypto_:
                        key = l1l11lll1_Krypto_.l11ll1111l_Krypto_(test[0])
                        l1llll11l_Krypto_ = l1l111l11_Krypto_.new(key)
                        l1l11llll1l_Krypto_ = l1llll11l_Krypto_.l1lllll_Krypto_(l1l1l111lll_Krypto_(test[2]), l1l1111_Krypto_ (u"ࠢ࠮࠯࠰ࠦᗠ"))
                        self.assertEqual(l1l11llll1l_Krypto_, b(test[1]))
        def l1l1l1111l1_Krypto_(self):
                l1llll11l_Krypto_ = l1l111l11_Krypto_.new(self.l1l1l11l11l_Krypto_)
                self.assertRaises(ValueError, l1llll11l_Krypto_.l1lllll_Krypto_, l1l1111_Krypto_ (u"ࠨ࡞ࡻ࠴࠵࠭ᗡ")*127, l1l1111_Krypto_ (u"ࠤ࠰࠱࠲ࠨᗢ"))
                self.assertRaises(ValueError, l1llll11l_Krypto_.l1lllll_Krypto_, l1l1111_Krypto_ (u"ࠪࡠࡽ࠶࠰ࠨᗣ")*129, l1l1111_Krypto_ (u"ࠦ࠲࠳࠭ࠣᗤ"))
                l1l11llll1l_Krypto_ = b(l1l1111_Krypto_ (u"ࠬࡢࡸ࠱࠲࡟ࡼ࠵࠸ࠧᗥ") + l1l1111_Krypto_ (u"࠭࡜ࡹࡈࡉࠫᗦ")*7 + l1l1111_Krypto_ (u"ࠧ࡝ࡺ࠳࠴ࠬᗧ") + l1l1111_Krypto_ (u"ࠨ࡞ࡻ࠸࠺࠭ᗨ")*118)
                ct = self.l1l1l11l11l_Krypto_.l1_Krypto_(l1l11llll1l_Krypto_, 0)[0]
                ct = b(l1l1111_Krypto_ (u"ࠩ࡟ࡼ࠵࠶ࠧᗩ")*(128-len(ct))) + ct
                self.assertEqual(l1l1111_Krypto_ (u"ࠥ࠱࠲࠳ࠢᗪ"), l1llll11l_Krypto_.l1lllll_Krypto_(ct, l1l1111_Krypto_ (u"ࠦ࠲࠳࠭ࠣᗫ")))
        def l1l1l111ll1_Krypto_(self):
                for l1l1l11l111_Krypto_ in range(0,128-11+1):
                    l1l11llll1l_Krypto_ = self.rng(l1l1l11l111_Krypto_)
                    l1llll11l_Krypto_ = l1l111l11_Krypto_.new(self.l1l1l11l11l_Krypto_)
                    ct = l1llll11l_Krypto_.l1_Krypto_(l1l11llll1l_Krypto_)
                    l1ll11lll11_Krypto_ = l1llll11l_Krypto_.l1lllll_Krypto_(ct, l1l1111_Krypto_ (u"ࠧ࠳࠭࠮ࠤᗬ"))
                    self.assertEqual(l1l11llll1l_Krypto_,l1ll11lll11_Krypto_)
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    tests = []
    tests += l1lll1111l1_Krypto_(l1l1l111l1l_Krypto_)
    return tests
if __name__ == l1l1111_Krypto_ (u"࠭࡟ࡠ࡯ࡤ࡭ࡳࡥ࡟ࠨᗭ"):
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭ᗮ"))