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
__revision__ = l1l1111_Krypto_ (u"ࠤࠧࡍࡩࠪࠢ᠙")
import unittest as l1lll111111_Krypto_
from l111ll1_Krypto_.l11l11l1_Krypto_ import l1l11lll1_Krypto_
from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l1ll1lllll1_Krypto_ import *
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
from l111ll1_Krypto_.l1l111ll_Krypto_.l111l1ll_Krypto_ import l11llll1ll_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_ import l11l1lll1l_Krypto_
def l11l1l11lll_Krypto_(l11l1l111l_Krypto_, text=l1l1111_Krypto_ (u"ࠪࡔ࡚ࡈࡌࡊࡅࠪ᠚")):
    import binascii as l11l111lll_Krypto_
    chunks = [ l11l111lll_Krypto_.b2a_base64(l11l1l111l_Krypto_[i:i+48]) for i in range(0, len(l11l1l111l_Krypto_), 48) ]
    l11l11ll11_Krypto_  = b(l1l1111_Krypto_ (u"ࠫ࠲࠳࠭࠮࠯ࡅࡉࡌࡏࡎࠡࠧࡶࠤࡐࡋ࡙࠮࠯࠰࠱࠲ࡢ࡮ࠨ᠛") % text)
    l11l11ll11_Krypto_ += b(l1l1111_Krypto_ (u"ࠬ࠭᠜")).join(chunks)
    l11l11ll11_Krypto_ += b(l1l1111_Krypto_ (u"࠭࠭࠮࠯࠰࠱ࡊࡔࡄࠡࠧࡶࠤࡐࡋ࡙࠮࠯࠰࠱࠲࠭᠝") % text)
    return l11l11ll11_Krypto_
class l11l1llllll_Krypto_(l1lll111111_Krypto_.TestCase):
    l11l1l1ll1l_Krypto_ = l1l1111_Krypto_ (u"ࠧࠨࠩ࠰࠱࠲࠳࠭ࡃࡇࡊࡍࡓࠦࡒࡔࡃࠣࡔࡗࡏࡖࡂࡖࡈࠤࡐࡋ࡙࠮࠯࠰࠱࠲ࠐࡍࡊࡋࡅࡓࡼࡏࡂࡂࡃࡍࡆࡆࡒ࠸ࡦࡌ࠸ࡅࡐࡵࡉࡴ࡬ࡘࡖࡵࡩࡅࡰࡉࡸࡦ࡟ࡓࡸࡍࡆ࠺࠯ࡰ࡚ࠫࡕࡎࡵ࠻࡚ࡱࡶࡆࡶࡉࡶࡗ࡮ࡄࡅࡍࡐࡸࡺࡏࡉࠋࡳ࠴࠽ࡋࡸࡌ࠵ࡲࡘࡍࡒࡿ࡭ࡑࡏࡖࡐࡇࡴ࠳ࡩࡌࡏࡩ࠸࠶ࡄࡸ࠶࠻ࡋࡖࡓ࠴ࡖࡅࡄࡻࡊࡇࡁࡒࡌࡄࡇ࡚࡙ࡄࡆࡲ࠻ࡖ࡙࡫࠳࠳ࡨࡷࡵ࠽ࡏࡷࡈ࠺ࠍ࡛ࡴࡰ࡬࠶࡯ࡄࡨ࠶ࡽࡆࡪࡋࡒࡶ࡟࠵ࡕࡷ࠺ࡥ࠽࠻࠹ࡗࡋࡑࡍ࡭ࡺࡗࡣࡗࡐ࠵࠽ࡻࡾࡕ࠶࠭ࡐࡽ࠾ࡍࡐ࡛࠹ࡕࡅ࠸࡮ࡲࡅࡄࡈࡅࡴࡎࡕࡅࡒࡵࡍࠏࡕࡑࡊࡪࡄࡔࡎࡖࡌࡻ࠶ࡧࡴ࡭࡯ࡄ࠺࡫ࡰࡅࡰ࡯ࡶ࡚࠵࠴ࡖࡨ࠻ࡁࡧࡊࡍ࡭ࡖࡘࡁ࠸࡚࡬ࡼ࡙ࡩࡪࡆ࡭ࡲ࡮ࡆ࡯ࡅࡂࡻ࡫࠳ࡵࡐࡈ࡬ࡵ࠲ࡑࡱࡸࠊࠬࡴࡧࡔࡓࡋࡰࡰࡶࡅ࡮࡫࡜࠴ࡎ࠶ࡅ࡯࡬ࡍࡁࡂ࠱࡬ࡴࡨࡳࡡࡂ࡬ࡦࡇࡎࡗࡃࡉࡸ࡫ࡻࡼࡑࡖࡃࡎࡽࡾ࡙ࡹࡣࡕ࠴ࡋࡩ࡚ࡪࡅࡦࡄࡐࡳ࡮࡞ࡘࡌࠌࡍࡅࡈࡇࡲ࠴ࡵࡍࡕࡏࡍࡸࡊࡓࡌ࡫ࡦࡸࡒࡱ࠭ࡰ࠵࡜࡙ࡋࡗ࠳ࡐࡧ࡮ࡽࡍࡢࡖࡒࡲࡧ࡛࠷ࡸࡺࡉࡷ࠾ࡊࡐ࠲ࡲࡹࡥ࠼࠼࡬࡚ࡄࡽ࡫࡚ࡉࡉࡒࡅ࠼ࠎࡳ࠶ࡃ࡯࡜ࡆࡎ࠻ࡏ࡚࡚ࡳࡖࡸ࠵ࡎ࠵ࡏ࠹࠮ࡕ࠰࠸ࡒࡰ࠸࠷ࡲࡺࡽࡖ࠰ࡑࡖࡕ࡫ࡓ࠶ࡴࡄࡺࡕࡂࡃࠊ࠮࠯࠰࠱࠲ࡋࡎࡅࠢࡕࡗࡆࠦࡐࡓࡋ࡙ࡅ࡙ࡋࠠࡌࡇ࡜࠱࠲࠳࠭࠮ࠩࠪࠫ᠞")
    l11l1l11l1l_Krypto_ = l1l1111_Krypto_ (u"ࠨࠩࠪ࠱࠲࠳࠭࠮ࡄࡈࡋࡎࡔࠠࡑࡔࡌ࡚ࡆ࡚ࡅࠡࡍࡈ࡝࠲࠳࠭࠮࠯ࠍࡑࡎࡏࡂࡗࡓࡌࡆࡆࡊࡁࡏࡄࡪ࡯ࡶ࡮࡫ࡪࡉ࠼ࡻ࠵ࡈࡁࡒࡇࡉࡅࡆ࡙ࡃࡂࡖ࠻ࡻ࡬࡭ࡅ࠸ࡃࡪࡉࡆࡇ࡫ࡆࡃࡹࡼ࠹ࡴ࡫ࡂࡳࡪ࡭ࡾࡔࡒࡈ࡮ࡺࡗࠏ࡭ࡡ࠶ࡶ࡮ࡾࡊࡹࡐࡷ࠸ࡕࡔ࠺ࡓࡵࡷࡶࡖࡗ࠽࡙࠰ࡘࡶࡊࡉࡒࡓ࡯ࡺ࠴࠷࡫࡮ࡸࡘ࠱࡙ࡶࡺ࡮ࡲࡑࡨࡼࡎ࡝࠽ࡾࡉࡴࡉࡩࡩࡊࡱࡴ࠸ࡨࡔࡔࡉࡰࠊࡸ࡜ࡄࡾ࡭ࡗࡉࡅࡃࡔࡅࡇࡇ࡫ࡂࡌࡕࡍࡒ࡙࡮ࡹࡈࡑ࠻࡫ࡠࠫ࠳ࡴࡺ࡮ࡆࡨࡸࡢ࡫ࡒ࡜ࡲ࡟ࡂ࠴࡚ࡄ࡛ࡎ࡭࠶ࡵࡰ࠼ࡗ࠴ࡾࡶ࠴ࡴࡧ࡝ࡰ࠺࡭ࡌࠌ࠸ࡆࡽ࡛࠳ࡣ࠴࠲ࡊ࡙ࡴ࠴ࡻࡎ࠳࡝࠾ࡴࡴࡆࡆࡨࡋࡸࡓࡅࡒࡅࡪࡨࡖࡓࠫࡴࡩ࠸ࡅ࡮ࡋࡁ࠹ࡩ࠻ࡺࡕ࡮࠲࡮ࡉࡌࡔ࠷ࡑ࡙ࡄࡕࡎ࠽࡯࡬ࡖࡇࡼ࡮ࠎࡇ࠾ࡣ࡮ࡌࡅࡉࡉࡺࡥࡍࡈࡑࡽࡒ࡙ࡓࡪࡏࡆࡍࡖࡊࡋࡉ࠭࡮࡯ࡪ࡙ࡺ࠹ࡻ࡚ࡺ࠻ࡺ࠰࠹࠲ࡖࡱ࡮࠶ࡇࡏ࠻࡛࡫ࡿ࡭ࡇࡔࡃ࡜ࡅࡉ࠱ࡋ࡭ࡻ࡝ࡳࡈࠐࡎࡸࡋ࡫ࡅࡎ࡫ࠫࡉࡆࡄࡴ࡚ࡋࡶࡑࡐࡒࡼࡽࡖ࡙ࡥ࠷ࡕ࠴ࡗ࠺ࡅࡺ࡫ࡍࡨࡨࡵ࡫ࡂࡋࡆࡺࡪࡽ࡬ࡂ࡭ࡥࡉ࡭ࡇࡩࡃࡳࡷࡋࡳ࠼ࡢࡗ࡜ࡌࡴ࡝࡛ࡸࠋࡻࡏࡅࡽࡶࡍ࠷ࡦࡷࡘࡻࡊࡅࡘࡼ࠳ࡑ࠴࡝࡭࠺ࡴࡹࡵ࡛࡭ࡈࡐࡄࡔࡍ࡭ࡇࡌ࠳ࡨࡔࡏࡩࡱࡉ࡯ࡱ࡫ࡰ࡮ࡶࡋ࠴ࡓࡩ࡯࠸ࡼ࠵ࡅ࠹࡝ࡋ࡯ࡸࡩࡦ࠹ࠍࡆ࡝࠾࠵ࡋࡄ࠻ࡾࡶࡽࡈࡃࠌ࠰࠱࠲࠳࠭ࡆࡐࡇࠤࡕࡘࡉࡗࡃࡗࡉࠥࡑࡅ࡚࠯࠰࠱࠲࠳ࠧࠨࠩ᠟")
    l11l1lll11l_Krypto_=(
        (l1l1111_Krypto_ (u"ࠩࡷࡩࡸࡺࠧᠠ"), l1l1111_Krypto_ (u"ࠪࠫࠬ࠳࠭࠮࠯࠰ࡆࡊࡍࡉࡏࠢࡕࡗࡆࠦࡐࡓࡋ࡙ࡅ࡙ࡋࠠࡌࡇ࡜࠱࠲࠳࠭࠮ࠌࡓࡶࡴࡩ࠭ࡕࡻࡳࡩ࠿ࠦ࠴࠭ࡇࡑࡇࡗ࡟ࡐࡕࡇࡇࠎࡉࡋࡋ࠮ࡋࡱࡪࡴࡀࠠࡅࡇࡖ࠱ࡈࡈࡃ࠭ࡃࡉ࠼ࡋ࠿ࡁ࠵࠲ࡅࡈ࠷ࡌࡁ࠳ࡈࡆࠎࠏࡉ࡫࡭࠻ࡨࡼ࠶ࡱࡡࡗࡇ࡚࡬࡞ࡉ࠲ࡒࡄࡰࡪࡦࡌ࡚ࠫࡒ࡬ࡖ࠹ࡔࡆ࡬ࡔ࡛ࡅ࠼ࡴࡪ࠴ࡦࡦࡲࡺࡌࡅࡻࡄࡱ࡝࠺࡞ࡕࡍࡷࡳࡵࡖࡶࡑࡊ࠵ࡴࡦ࡫ࡇࠊࡶ࠺ࡊ࡝ࡘ࠽ࠫࡣ࠵ࡷࡳ࡜࡝ࡩࡉ࡜࡬ࡺࡍࡨࡁࡂࡗࡅࡔࡉࡏ࡚ࡈ࠻࡫ࡏࡉࡿࡂ࠺ࡕࡴ࠶࡛ࡓࡁࡓࡉࡶ࡜࠶ࡿࡗ࠲ࡼ࡫ࡒࡻࡠࡌࡊ࡫࡙ࡎࡿ࡛ࡈࡴࠌࡆ࠺ࡓࡾࡑ࠲ࡋࡍ࡛ࡔ࡞ࡺࡕࡧࡺ࠳ࡽࡓ࠲ࡊ࠴࠹࡯ࡕࡽࡈࡊࡸࡤࡨࡶ࠱࠯ࡗࡣࡗ࠼࡬ࡒࡑࡥ࡬ࡧࡌ࠵ࡰࡏࡪࡘࡑࡥࡪࡼࡪࡘࡰࡏ࡫ࡷࡴ࠱࡮ࡎࡓࠎࡇࡉࡎࡓࡏࡧࡧࡪࡾ࡯ࡻ࡙ࡷࡅࡋࡔࡎࡲࡕࡽࡪ࡜࠻࠸ࡎࡌࡏ࠶ࡔࡪࡍࡪ࠴࠴ࡉࡉ࠷࠸࠵ࡇࡉࡽࡹࡏࡣ࠲ࡄ࡯ࡆ࠰ࡌ࡚ࡪࡉ࡝ࡨࡺࡽࡋࡈࡷࡤࡏࡾࠐ࠹ࡣࡏࡥࡨࡧ࠵࠱ࡑࡕࡹࡷࡘࢀࡐࡴࡳ࡚࠻ࡐ࡙ࡓࡳࡖࡺ࠺ࡒ࡭ࡊࡂࡈࡍ࡫࠻ࡲࡺࡊ࡛ࡹࡖ࠺ࡌ࠴ࡱࡱࡗ࡚ࡇࡾࡷࡃ࡚࠶࠯ࡊࡿࡅ࡮ࡕ࡫࡭ࡦࡔ࡙ࠋࡋࡕ࡜࠸࡚ࡧࡒࡋ࠳ࡍ࡯ࡸࡖࡶࡎࡰࡺࡱࡠࡋࡣࡉ࡚ࡔ࠶࠾ࡆ࡙࡬࠺ࡍ࠼ࡱ࠹ࡵࡕࡶࡒࡔࡕࡺ࡭࡮ࡗࡘࡩࡷ࠳࡯ࡻ࠸ࡺ࡬ࡓ࠳ࡂ࠭ࡼࡲ࡫ࡇࡡࡹࡲࠍࡨࡾࡹࡋࡻࡰࡔ࠺ࡕ࠱ࡉࡰࡳࡐࡐ࠶࡝ࡸࡂࡋࡇ࠸ࡦࡍࡒࡎ࡙࡮ࡥ࠰ࡻࡁࡳࡑࡍ࠵࠹࠾ࡒࡣ࡬࠼ࡷࡂࠐ࠭࠮࠯࠰࠱ࡊࡔࡄࠡࡔࡖࡅࠥࡖࡒࡊࡘࡄࡘࡊࠦࡋࡆ࡛࠰࠱࠲࠳࠭ࠨࠩࠪᠡ"),
        l1l1111_Krypto_ (u"ࠦࡡࡾࡁࡇ࡞ࡻ࠼ࡋࡢࡸ࠺ࡃ࡟ࡼ࠹࠶࡜ࡹࡄࡇࡠࡽ࠸ࡆ࡝ࡺࡄ࠶ࡡࡾࡆࡄࠤᠢ")),
        (l1l1111_Krypto_ (u"ࠬࡸ࡯ࡤ࡭࡬ࡲ࡬࠭ᠣ"), l1l1111_Krypto_ (u"࠭ࠧࠨ࠯࠰࠱࠲࠳ࡂࡆࡉࡌࡒࠥࡘࡓࡂࠢࡓࡖࡎ࡜ࡁࡕࡇࠣࡏࡊ࡟࠭࠮࠯࠰࠱ࠏࡖࡲࡰࡥ࠰ࡘࡾࡶࡥ࠻ࠢ࠷࠰ࡊࡔࡃࡓ࡛ࡓࡘࡊࡊࠊࡅࡇࡎ࠱ࡎࡴࡦࡰ࠼ࠣࡈࡊ࡙࠭ࡆࡆࡈ࠷࠲ࡉࡂࡄ࠮ࡆ࠴࠺ࡊ࠶ࡄ࠲࠺ࡊ࠼ࡌࡃ࠱࠴ࡉ࠺ࠏࠐࡷ࠵࡮ࡺࡕࡷ࡞ࡡࡗࡱࡗࡘࡏ࠶ࡇࡨࡹ࡜࠹࠻࠼ࡨࡵࡖࡄ࠶࠴ࡺ࠱࡚࡮࡬ࡱ࡭ࡾ࡫ࡹ࡛ࡷ࠽ࡆࡋࡥࡄࡥ࡬ࡨࡘ࠻ࡍ࠱࡙ࡴ࠽ࡈࡲࡐࡪࡒࡽ࠽ࡔ࠽ࡆࠋ࡯࠹ࡏ࠺ࡗࡰࡎ࠳ࡵࡼࡴ࠷ࡒࡖࡇ࠲࡞ࡾࡏ࠸࠶ࡩࡪࡰࡗࡔࡐࡥࡐࡺ࡯ࡪ࡚ࡏࡲ࡫ࡷ࠯ࡰࡻ࡭࠸ࡰࡑ࠻࠸ࡇࡔࡰ࡚࠴࠻࠰࡯ࡲࡗ࡯ࡒࡅ࠹ࡠ࠹ࡆ࠭ࠍ࠸ࡔ࠶࠷ࡵ࠻࠴ࡋࡽࡍࡍࡤ࡬ࡘࡗࡎࡌ࡫࠱ࡷࡦࡻࡊ࡛࠴࡫ࡩࡻࡖࡻ࡟ࡳࡤࡤࡹࡓࡒࡼࡎࡣࡷ࡝ࡷࡿࡍࡤࡗࡐࡽࡆ࡙࡜ࡤࡥࡰࡖ࡬ࡐࡉࡳࡺ࠻࡬࠻ࠏࡴࡊࡣࡒ࡯࡜ࡪࡋࡋ࡚࡫࠲ࡓࡰࡘࡧࡐ࠶ࡓࡸ࡫ࡷࡱࡘࡓࡸ࠹ࡌࡏࡅࡇࡘࡘࡪ࠾࡫ࡶ࠲ࡓ࡙࠻ࡆࡼࡃࠬ࡭ࡼ࡛࡙ࡘ࠱ࡸ࡙࡜ࡲࡍ࡞࠲࠷࠷࡭࡙࠺ࡩࠊࡴࡱࡳࡼࡖࡗࡴࡑ࠺࡛ࡉࡍࡏࡊࡆࡦࡧ࠹࠴ࡶ࠱ࡰ࡫ࡨࡖࡨ࡝ࡔࡄࡐࡼ࡝࠽ࡋ࡫ࡴ࡮ࡻࡈࡘࡹࡲࡧ࠲ࡒࡸ࡟ࡶ࠶࡮࡜ࡋ࠽ࡓ࠱ࡋࡖ࠶࠺ࡧ࡬ࡗࡴࡵࠌ࠼ࡵࡌࡕࡒ࡮࡮࡚ࡲࡸࡏ࡯ࡇࡈࡎࡧࡉࡵࡨࡣࡶࡒࡥ࡜ࡈࡔࡌࡪ࡮࡮࠺࡮࠶ࡐ࡭ࡏ࡮ࡋࡰࡦࡖ࠱ࡶࡆࡪ࡜࠱ࡤ࠭࠺ࡻࡉ࡚࠳ࡥࡃࡼ࠹ࡹࡧࡷ࡙࡬ࡊࠎ࡞࡙ࡸࡄ࠹ࡴࡈࡖࡏࡔ࠰ࡔࡈࡇࡻ࡜࠳ࠬࡱࡔࡏࡊࡩ࡭ࡱࡇࡸ࡮ࡳ࠺࠵ࡸࡃࡱ࡯࡙࡯࠱࠳ࡄࡋ࠷࠵ࡃࠊ࠮࠯࠰࠱࠲ࡋࡎࡅࠢࡕࡗࡆࠦࡐࡓࡋ࡙ࡅ࡙ࡋࠠࡌࡇ࡜࠱࠲࠳࠭࠮ࠩࠪࠫᠤ"),
        l1l1111_Krypto_ (u"ࠢ࡝ࡺࡆ࠴ࡡࡾ࠵ࡅ࡞ࡻ࠺ࡈࡢࡸ࠱࠹࡟ࡼࡋ࠽࡜ࡹࡈࡆࡠࡽ࠶࠲࡝ࡺࡉ࠺ࠧᠥ")),
    )
    l11l1l111l1_Krypto_ = l1l1111_Krypto_ (u"ࠨࠩࠪ࠱࠲࠳࠭࠮ࡄࡈࡋࡎࡔࠠࡑࡗࡅࡐࡎࡉࠠࡌࡇ࡜࠱࠲࠳࠭࠮ࠌࡐࡊࡼࡽࡄࡒ࡛ࡍࡏࡴࡠࡉࡩࡸࡦࡒࡆࡗࡅࡃࡄࡔࡅࡉ࡙ࡷࡂࡹࡖࡅࡏࡈࡁࡍ࠺ࡨࡎ࠺ࡇࡋࡰࡋࡶ࡮࡚ࡘࡰࡤࡇࡲࡋࡺࡨ࡚ࡎࡺࡏࡈ࠼࠱࡫ࡕ࠭ࡗࠎࡑࡸ࠷ࡖ࡭ࡹࡉࡹࡌࡲࡓࡪࡇࡈࡐࡓࡴࡶࡋࡌࡵ࠶࠿ࡆࡳࡎ࠷ࡴ࡚ࡏࡍࡺ࡯ࡓࡑࡘࡒࡂ࡯࠵࡫ࡎࡑ࡫࠳࠱ࡆࡺ࠸࠽ࡍࡑࡎ࠶ࡘࡇࡆࡽࡅࡂࡃࡔࡁࡂࠐ࠭࠮࠯࠰࠱ࡊࡔࡄࠡࡒࡘࡆࡑࡏࡃࠡࡍࡈ࡝࠲࠳࠭࠮࠯ࠪࠫࠬᠦ")
    l11l1l1l1l1_Krypto_ = l1l1111_Krypto_ (u"ࠩࠪࠫࡸࡹࡨ࠮ࡴࡶࡥࠥࡇࡁࡂࡃࡅ࠷ࡓࢀࡡࡄ࠳ࡼࡧ࠷ࡋࡁࡂࡃࡄࡈࡆࡗࡁࡃࡃࡄࡅࡆࡗࡑࡄ࠱ࡋ࡭ࡪࡗࡃࡲࡅࡏࡍ࠶ࡋࡡ࡙ࡄࡎࡆࡷࡳ࠲ࡕࡏࡖࡻ࠰࠵ࡰࡆ࠱࡮ࡽ࠻࠱࠱ࡋࡎࡻࡐࡗࡧ࠰࡚ࡓࡺࡽ࡯ࡒࡢࡪࡅࡎࡸ࡫ࡘࡡࡺ࠭ࡎ࡚ࡈࡊࡍࡱ࡬ࡽࡉ࡮ࡽ࡚࠺࠶ࡖࡗ࠸ࡺ࠹ࡂ࠺ࡒࡔࡇࡱࡄࡐࡈࠣࡧࡴࡳ࡭ࡦࡰࡷࡠࡳ࠭ࠧࠨᠧ")
    l11ll1111l1_Krypto_ = a2b_hex(
    l1l1111_Krypto_ (u"ࠪࠫࠬ࠹࠰࠹࠴࠳࠵࠸ࡨ࠰࠳࠲࠴࠴࠵࠶࠲࠵࠳࠳࠴ࡧ࡬࠱ࡦ࠴࠺࠽࠵࠶ࡡࡢ࠲࠻ࡦ࠷࠹࠵࠲࠳ࡤ࠹ࡨ࠷࠲࠹࠳ࡤࡩ࠻ࡪ࠹࠴࠵࠴࠶ࡨ࠹ࡥࡧࡧࠍࠤࠥࠦࠠ࠺࠳࠶ࡪ࠾࠹࠲ࡦࡤࡨࡨ࠹࠿࠲ࡧ࠳࠵ࡨ࠶࠼ࡢ࠵࠸࠴࠴ࡨ࠹࠲࠹ࡥࡥ࠺ࡪ࠸࠰࠹ࡣࡥ࠹࡫࠺࠵ࡢࡥࡥࡩ࠷࠿࠵࠱࠺࠶࠷࠷࠿࠸ࡧ࠵࠴࠶ࠏࠦࠠࠡࠢ࠵ࡧ࠶࠿ࡦ࠸࠺࠷࠽࠷ࡪࡥࡥࡨ࠷࠴࡫࠶ࡥ࠴ࡥ࠴࠽࠵࠹࠳࠹࠷࠳࠶࠵࠹࠰࠲࠲࠳࠴࠶࠶࠲࠵࠲࠳࠽࠹࠺࠸࠴࠳࠵࠽࡫࠷࠱࠵ࡦࡨࡨ࡫࠼ࠊࠡࠢࠣࠤ࠼࡫ࡤࡢࡤࡦ࠶࠸࠶࠱ࡣࡥ࠸ࡥ࠽࠾ࡥ࠶ࡧ࠹࠺࠵࠷ࡤࡥ࠹࠳࠵࠻࠸࠲࠱ࡧࡤࡨ࠾࡬ࡤ࠵ࡤࡩࡧ࠻࡬ࡤࡦࡤ࠺࠹࠽࠿࠳࠹࠻࠻ࡥࡪ࠺࠱ࡤࠌࠣࠤࠥࠦ࠵࠵ࡦࡧࡦࡩࡨࡦ࠲࠷࠶࠽࡫࠾ࡣࡤࡤࡧ࠵࠽࡬࠶࠸ࡤ࠷࠸࠵ࡪࡥ࠲ࡣࡦ࠷࠵࠺࠴࠱࠴࠻࠵ࡩ࠺࠰ࡤࡨࡤࡧ࠽࠹࠹࠱࠴࠵࠵࠵࠶ࡦ࠳࠲ࡩࠎࠥࠦࠠࠡ࠴ࡩ࠷ࡪ࠷ࡤࡢ࠸࠴࠼࠽࠹ࡦ࠷࠴࠼࠼࠵࠿࠲࠳ࡤࡧ࠼ࡩ࡬࠵࠵࠷ࡦࡩ࠹࠶࠷ࡤ࠹࠵࠺࠷࠺࠱࠲࠲࠶ࡦ࠺࡫࠲ࡤ࠷࠶࠻࠷࠹࠱࠳࠶ࡤ࠶࠸ࠐࠠࠡࠢࠣ࠴࠷࠸࠱࠱࠲ࡦࡥ࠶࡬ࡥ࠺࠴࠷࠻࠾࠸ࡣࡧࡥࡦ࠽࠻ࡨࡦࡢࡤ࠺࠸࡫࠹࠴࠵ࡣ࠹࠼ࡧ࠺࠱࠹ࡦࡩ࠹࠼࠾࠳࠴࠺࠳࠺࠹࠾࠰࠷࠲࠳࠴࡫࡫࠲ࠋࠢࠣࠤࠥࡧ࠵ࡤ࠻࠼ࡥ࠵࠸࠳࠸࠲࠵࠶࠶࠶࠰࠹࠹ࡥࡩ࠶ࡩ࠳࠱࠴࠼࠹࠵࠺ࡢࡤࡨ࠶࠸ࡪࡩ࠷࠲࠵ࡧ࠼࠼࠽࠹࠵࠹࠷࠸࠼࠾࠱࠴࠴࠻࠼࠾࠽࠵ࡤࡣࠍࠤࠥࠦࠠ࠳࠶࠳࠴࠽࠶ࡡࡧ࠹ࡥ࠴࠾࠺࠰࠺࠳ࡥ࠵࠷࠷࠰࠳࠴࠳࠺ࡦࡨ࠴࠷࠻ࡩࡥ࠻ࡪ࠵࠷࠶࠻ࡥ࠺࠽࠵࠴࠳ࡦ࠼ࡧ࠶࠳࠲ࡣ࠷ࡧࡪ࠿ࡤࡣ࠷࠶ࡦࠏࠦࠠࠡࠢࡦ࠷࠶࠷࠶ࡤࡨ࠷࠷࠸࡬࠵ࡢ࠸ࡩ࠺ࡧࡨࡥࡢ࠷࠹࠴࠶ࡩࡥ࠱࠷࠳࠶࠷࠷࠰࠱ࡤࡧ࠽࡫࠺࠰ࡢ࠹࠹࠸࠷࠸࠷ࡢ࠴࠴࠽࠻࠸ࡡ࠵ࡣࡧࡨ࠵࠽ࠊࠡࠢࠣࠤࡪ࠺ࡤࡦࡨࡨ࠸࠸࡫ࡤ࠺࠳ࡤ࠷ࡦ࡫࠲࠸ࡤࡥ࠴࠺࠽ࡦ࠴࠻࠵࠸࠶࡬࠳࠴ࡣࡥ࠴࠶ࡩ࠱ࠋࠢࠣࠤࠥ࠭ࠧࠨᠨ").replace(l1l1111_Krypto_ (u"ࠦࠥࠨᠩ"),l1l1111_Krypto_ (u"ࠧࠨᠪ")))
    l11ll111111_Krypto_ = a2b_hex(
    l1l1111_Krypto_ (u"࠭ࠧࠨ࠵࠳࠼࠷࠶࠱࠶࠷࠳࠶࠵࠷࠰࠱࠵࠳࠴ࡩ࠶࠶࠱࠻࠵ࡥ࠽࠼࠴࠹࠺࠹ࡪ࠼࠶ࡤ࠱࠳࠳࠵࠵࠷࠰࠶࠲࠳࠴࠹࠾࠲࠱࠳࠶ࡪ࠸࠶࠸࠳࠲࠴࠷ࠏࠦࠠࠡࠢࡥ࠴࠷࠶࠱࠱࠲࠳࠶࠹࠷࠰࠱ࡤࡩ࠵ࡪ࠸࠷࠺࠲࠳ࡥࡦ࠶࠸ࡣ࠴࠶࠹࠶࠷ࡡ࠶ࡥ࠴࠶࠽࠷ࡡࡦ࠸ࡧ࠽࠸࠹࠱࠳ࡥ࠶ࡩ࡫࡫࠹࠲࠵ࡩ࠽࠸࠸ࠊࠡࠢࠣࠤࡪࡨࡥࡥ࠶࠼࠶࡫࠷࠲ࡥ࠳࠹ࡦ࠹࠼࠱࠱ࡥ࠶࠶࠽ࡩࡢ࠷ࡧ࠵࠴࠽ࡧࡢ࠶ࡨ࠷࠹ࡦࡩࡢࡦ࠴࠼࠹࠵࠾࠳࠴࠴࠼࠼࡫࠹࠱࠳࠴ࡦ࠵࠾࡬࠷࠹ࠌࠣࠤࠥࠦ࠴࠺࠴ࡧࡩࡩ࡬࠴࠱ࡨ࠳ࡩ࠸ࡩ࠱࠺࠲࠶࠷࠽࠻࠰࠳࠲࠶࠴࠶࠶࠰࠱࠳࠳࠶࠹࠶࠰࠺࠶࠷࠼࠸࠷࠲࠺ࡨ࠴࠵࠹ࡪࡥࡥࡨ࠹࠻ࡪࡪࡡࡣࡥ࠵ࠎࠥࠦࠠࠡ࠵࠳࠵ࡧࡩ࠵ࡢ࠺࠻ࡩ࠺࡫࠶࠷࠲࠴ࡨࡩ࠽࠰࠲࠸࠵࠶࠵࡫ࡡࡥ࠻ࡩࡨ࠹ࡨࡦࡤ࠸ࡩࡨࡪࡨ࠷࠶࠺࠼࠷࠽࠿࠸ࡢࡧ࠷࠵ࡨ࠻࠴ࡥࡦࡥࡨࡧࠐࠠࠡࠢࠣࡪ࠶࠻࠳࠺ࡨ࠻ࡧࡨࡨࡤ࠲࠺ࡩ࠺࠼ࡨ࠴࠵࠲ࡧࡩ࠶ࡧࡣ࠴࠲࠷࠸࠵࠸࠸࠲ࡦ࠷࠴ࡨ࡬ࡡࡤ࠺࠶࠽࠵࠸࠲࠲࠲࠳ࡪ࠷࠶ࡦ࠳ࡨ࠶ࡩ࠶ࡪࡡࠋࠢࠣࠤࠥ࠼࠱࠹࠺࠶ࡪ࠻࠸࠹࠹࠲࠼࠶࠷ࡨࡤ࠹ࡦࡩ࠹࠹࠻ࡣࡦ࠶࠳࠻ࡨ࠽࠲࠷࠴࠷࠵࠶࠶࠳ࡣ࠷ࡨ࠶ࡨ࠻࠳࠸࠴࠶࠵࠷࠺ࡡ࠳࠵࠳࠶࠷࠷࠰࠱ࡥࠍࠤࠥࠦࠠࡢ࠳ࡩࡩ࠾࠸࠴࠸࠻࠵ࡧ࡫ࡩࡣ࠺࠸ࡥࡪࡦࡨ࠷࠵ࡨ࠶࠸࠹ࡧ࠶࠹ࡤ࠷࠵࠽ࡪࡦ࠶࠹࠻࠷࠸࠾࠰࠷࠶࠻࠴࠻࠶࠰࠱ࡨࡨ࠶ࡦ࠻ࡣ࠺࠻ࡤ࠴ࠏࠦࠠࠡࠢ࠵࠷࠼࠶࠲࠳࠳࠳࠴࠽࠽ࡢࡦ࠳ࡦ࠷࠵࠸࠹࠶࠲࠷ࡦࡨ࡬࠳࠵ࡧࡦ࠻࠶࠹ࡤ࠹࠹࠺࠽࠹࠽࠴࠵࠹࠻࠵࠸࠸࠸࠹࠻࠺࠹ࡨࡧ࠲࠵࠲࠳࠼࠵ࡧࠊࠡࠢࠣࠤ࡫࠽ࡢ࠱࠻࠷࠴࠾࠷ࡢ࠲࠴࠴࠴࠷࠸࠰࠷ࡣࡥ࠸࠻࠿ࡦࡢ࠸ࡧ࠹࠻࠺࠸ࡢ࠷࠺࠹࠸࠷ࡣ࠹ࡤ࠳࠷࠶ࡧ࠴ࡤࡧ࠼ࡨࡧ࠻࠳ࡣࡥ࠶࠵࠶࠼ࡣࡧࠌࠣࠤࠥࠦ࠴࠴࠵ࡩ࠹ࡦ࠼ࡦ࠷ࡤࡥࡩࡦ࠻࠶࠱࠳ࡦࡩ࠵࠻࠰࠳࠴࠴࠴࠵ࡨࡤ࠺ࡨ࠷࠴ࡦ࠽࠶࠵࠴࠵࠻ࡦ࠸࠱࠺࠸࠵ࡥ࠹ࡧࡤࡥ࠲࠺ࡩ࠹ࡪࡥࡧࡧ࠷ࠎࠥࠦࠠࠡ࠵ࡨࡨ࠾࠷ࡡ࠴ࡣࡨ࠶࠼ࡨࡢ࠱࠷࠺ࡪ࠸࠿࠲࠵࠳ࡩ࠷࠸ࡧࡢ࠱࠳ࡦ࠵ࠏࠦࠠࠡࠢࠪࠫࠬᠫ").replace(l1l1111_Krypto_ (u"ࠢࠡࠤᠬ"),l1l1111_Krypto_ (u"ࠣࠤᠭ")))
    l11ll11111l_Krypto_ = a2b_hex(
    l1l1111_Krypto_ (u"ࠩࠪࠫ࠸࠶࠵ࡤ࠵࠳࠴ࡩ࠶࠶࠱࠻࠵ࡥ࠽࠼࠴࠹࠺࠹ࡪ࠼࠶ࡤ࠱࠳࠳࠵࠵࠷࠰࠶࠲࠳࠴࠸࠺ࡢ࠱࠲࠶࠴࠹࠾࠰࠳࠶࠴࠴࠵ࡨࡦ࠲ࡧ࠵࠻࠾࠶࠰ࡢࠌࠣࠤࠥࠦࡡ࠱࠺ࡥ࠶࠸࠻࠱࠲ࡣ࠸ࡧ࠶࠸࠸࠲ࡣࡨ࠺ࡩ࠿࠳࠴࠳࠵ࡧ࠸࡫ࡦࡦ࠻࠴࠷࡫࠿࠳࠳ࡧࡥࡩࡩ࠺࠹࠳ࡨ࠴࠶ࡩ࠷࠶ࡣ࠶࠹࠵࠵ࡩ࠳࠳࠺ࡦࠎࠥࠦࠠࠡࡤ࠹ࡩ࠷࠶࠸ࡢࡤ࠸ࡪ࠹࠻ࡡࡤࡤࡨ࠶࠾࠻࠰࠹࠵࠶࠶࠾࠾ࡦ࠴࠳࠵࠶ࡨ࠷࠹ࡧ࠹࠻࠸࠾࠸ࡤࡦࡦࡩ࠸࠵࡬࠰ࡦ࠵ࡦ࠵࠾࠶࠳࠴࠺࠸࠴࠷ࠐࠠࠡࠢࠣ࠴࠸࠶࠱࠱࠲࠳࠵ࠏࠦࠠࠡࠢࠪࠫࠬᠮ").replace(l1l1111_Krypto_ (u"ࠥࠤࠧᠯ"),l1l1111_Krypto_ (u"ࠦࠧᠰ")))
    n = int(l1l1111_Krypto_ (u"ࠬࡈࡆࠡ࠳ࡈࠤ࠷࠽ࠠ࠺࠲ࠣ࠴ࡆࠦࡁ࠱ࠢ࠻ࡆࠥ࠸࠳ࠡ࠷࠴ࠤ࠶ࡇࠠ࠶ࡅࠣ࠵࠷ࠦ࠸࠲ࠢࡄࡉࠥ࠼ࡄࠡ࠻࠶ࠤ࠸࠷ࠠ࠳ࡅࠣ࠷ࡊࠦࡆࡆࠢ࠼࠵ࠥ࠹ࡆࠡ࠻࠶ࠤ࠷ࡋࠠࡃࡇࠣࡈ࠹ࠦ࠹࠳ࠢࡉ࠵ࠥ࠸ࡄࠡ࠳࠹ࠤࡇ࠺ࠠ࠷࠳ࠣ࠴ࡈࠦ࠳࠳ࠢ࠻ࡇࠥࡈ࠶ࠡࡇ࠵ࠤ࠵࠾ࠠࡂࡄࠣ࠹ࡋࠦ࠴࠶ࠢࡄࡇࠥࡈࡅࠡ࠴࠼ࠤ࠺࠶ࠠ࠹࠵ࠣ࠷࠷ࠦ࠹࠹ࠢࡉ࠷ࠥ࠷࠲ࠡ࠴ࡆࠤ࠶࠿ࠠࡇ࠹ࠣ࠼࠹ࠦ࠹࠳ࠢࡇࡉࠥࡊࡆࠡ࠶࠳ࠤࡋ࠶ࠠࡆ࠵ࠣࡇ࠶ࠦ࠹࠱ࠢ࠶࠷ࠥ࠾࠵ࠨᠱ").replace(l1l1111_Krypto_ (u"ࠨࠠࠣᠲ"),l1l1111_Krypto_ (u"ࠢࠣᠳ")),16)
    e = 65537
    d = int(l1l1111_Krypto_ (u"ࠨ࠲࠼ࠤ࠹࠺ࠠ࠹࠵ࠣ࠵࠷ࠦ࠹ࡇࠢ࠴࠵ࠥ࠺ࡄࠡࡇࡇࠤࡋ࠼ࠠ࠸ࡇࠣࡈࡆࠦࡂࡄࠢ࠵࠷ࠥ࠶࠱ࠡࡄࡆࠤ࠺ࡇࠠ࠹࠺ࠣࡉ࠺ࠦࡅ࠷ࠢ࠹࠴ࠥ࠷ࡄࠡࡆ࠺ࠤ࠵࠷ࠠ࠷࠴ࠣ࠶࠵ࠦࡅࡂࠢࡇ࠽ࠥࡌࡄࠡ࠶ࡅࠤࡋࡉࠠ࠷ࡈࠣࡈࡊࠦࡂ࠸ࠢ࠸࠼ࠥ࠿࠳ࠡ࠺࠼ࠤ࠽ࡇࠠࡆ࠶ࠣ࠵ࡈࠦ࠵࠵ࠢࡇࡈࠥࡈࡄࠡࡄࡉࠤ࠶࠻ࠠ࠴࠻ࠣࡊ࠽ࠦࡃࡄࠢࡅࡈࠥ࠷࠸ࠡࡈ࠹ࠤ࠼ࡈࠠ࠵࠶ࠣ࠴ࡉࠦࡅ࠲ࠢࡄࡇࠥ࠹࠰ࠡ࠶࠷ࠤ࠵࠸ࠠ࠹࠳ࠣࡈ࠹ࠦ࠰ࡄࠢࡉࡅࠥࡉ࠸ࠡ࠵࠼ࠫᠴ").replace(l1l1111_Krypto_ (u"ࠤࠣࠦᠵ"),l1l1111_Krypto_ (u"ࠥࠦᠶ")),16)
    p = int(l1l1111_Krypto_ (u"ࠫ࠵࠶ࠠࡇ࠴ࠣ࠴ࡋࠦ࠲ࡇࠢ࠶ࡉࠥ࠷ࡄࠡࡃ࠹ࠤ࠶࠾ࠠ࠹࠵ࠣࡊ࠻ࠦ࠲࠺ࠢ࠻࠴ࠥ࠿࠲ࠡ࠴ࡅࠤࡉ࠾ࠠࡅࡈࠣ࠹࠹ࠦ࠵ࡄࠢࡈ࠸ࠥ࠶࠷ࠡࡅ࠺ࠤ࠷࠼ࠠ࠳࠶ࠣ࠵࠶ࠦ࠰࠴ࠢࡅ࠹ࠥࡋ࠲ࠡࡅ࠸ࠤ࠸࠽ࠠ࠳࠵ࠣ࠵࠷ࠦ࠴ࡂࠢ࠵࠷ࠬᠷ").replace(l1l1111_Krypto_ (u"ࠧࠦࠢᠸ"),l1l1111_Krypto_ (u"ࠨࠢᠹ")),16)
    q = int(l1l1111_Krypto_ (u"ࠧ࠱࠲ࠣࡇࡆࠦ࠱ࡇࠢࡈ࠽ࠥ࠸࠴ࠡ࠹࠼ࠤ࠷ࡉࠠࡇࡅࠣࡇ࠾ࠦ࠶ࡃࠢࡉࡅࠥࡈ࠷ࠡ࠶ࡉࠤ࠸࠺ࠠ࠵ࡃࠣ࠺࠽ࠦࡂ࠵ࠢ࠴࠼ࠥࡊࡆࠡ࠷࠺ࠤ࠽࠹ࠠ࠴࠺ࠣ࠴࠻ࠦ࠴࠹ࠢ࠳࠺ࠥ࠶࠰ࠡ࠲ࡉࠤࡊ࠸ࠠࡂ࠷ࠣࡇ࠾ࠦ࠹ࡂࠢ࠳࠶ࠥ࠹࠷ࠨᠺ").replace(l1l1111_Krypto_ (u"ࠣࠢࠥᠻ"),l1l1111_Krypto_ (u"ࠤࠥᠼ")),16)
    l11l1l1l11l_Krypto_ = int(l1l1111_Krypto_ (u"ࠪ࠴࠵ࠦࡂࡅࠢ࠼ࡊࠥ࠺࠰ࠡࡃ࠺ࠤ࠻࠺ࠠ࠳࠴ࠣ࠻ࡆࠦ࠲࠲ࠢ࠼࠺ࠥ࠸ࡁࠡ࠶ࡄࠤࡉࡊࠠ࠱࠹ࠣࡉ࠹ࠦࡄࡆࠢࡉࡉࠥ࠺࠳ࠡࡇࡇࠤ࠾࠷ࠠࡂ࠵ࠣࡅࡊࠦ࠲࠸ࠢࡅࡆࠥ࠶࠵ࠡ࠹ࡉࠤ࠸࠿ࠠ࠳࠶ࠣ࠵ࡋࠦ࠳࠴ࠢࡄࡆࠥ࠶࠱ࠡࡅ࠴ࠫᠽ").replace(l1l1111_Krypto_ (u"ࠦࠥࠨᠾ"),l1l1111_Krypto_ (u"ࠧࠨᠿ")),16)
    l11ll11l111_Krypto_ = l11llll1ll_Krypto_(p,q)
    def l11l1ll1ll1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠨࠢࠣࡘࡨࡶ࡮࡬ࡹࠡ࡫ࡰࡴࡴࡸࡴࠡࡱࡩࠤࡗ࡙ࡁࡑࡴ࡬ࡺࡦࡺࡥࡌࡧࡼࠤࡉࡋࡒࠡࡕࡈࡕ࡚ࡋࡎࡄࡇࠥࠦࠧᡀ")
        key = self.l11l1llll11_Krypto_.l11ll1111l_Krypto_(self.l11ll1111l1_Krypto_)
        self.assertTrue(key.l1l1111l1l_Krypto_())
        self.assertEqual(key.n, self.n)
        self.assertEqual(key.e, self.e)
        self.assertEqual(key.d, self.d)
        self.assertEqual(key.p, self.p)
        self.assertEqual(key.q, self.q)
    def l11ll111lll_Krypto_(self):
        l1l1111_Krypto_ (u"ࠢࠣࠤ࡙ࡩࡷ࡯ࡦࡺࠢ࡬ࡱࡵࡵࡲࡵࠢࡲࡪ࡙ࠥࡵࡣ࡬ࡨࡧࡹࡖࡵࡣ࡮࡬ࡧࡐ࡫ࡹࡊࡰࡩࡳࠥࡊࡅࡓࠢࡖࡉࡖ࡛ࡅࡏࡅࡈࠦࠧࠨᡁ")
        key = self.l11l1llll11_Krypto_.l11ll1111l_Krypto_(self.l11ll11111l_Krypto_)
        self.assertFalse(key.l1l1111l1l_Krypto_())
        self.assertEqual(key.n, self.n)
        self.assertEqual(key.e, self.e)
    def l11l1llll1l_Krypto_(self):
        l1l1111_Krypto_ (u"ࠣࠤ࡚ࠥࡪࡸࡩࡧࡻࠣ࡭ࡲࡶ࡯ࡳࡶࠣࡳ࡫ࠦࡒࡔࡃࡓࡶ࡮ࡼࡡࡵࡧࡎࡩࡾࠦࡄࡆࡔࠣࡗࡊࡗࡕࡆࡐࡆࡉ࠱ࠦࡥ࡯ࡥࡲࡨࡪࡪࠠࡸ࡫ࡷ࡬ࠥࡖࡅࡎࠢࡤࡷࠥࡻ࡮ࡪࡥࡲࡨࡪࠨࠢࠣᡂ")
        key = l1l11lll1_Krypto_.l11ll1111l_Krypto_(self.l11l1l1ll1l_Krypto_)
        self.assertEqual(key.l1l1111l1l_Krypto_(),True)
        self.assertEqual(key.n, self.n)
        self.assertEqual(key.e, self.e)
        self.assertEqual(key.d, self.d)
        self.assertEqual(key.p, self.p)
        self.assertEqual(key.q, self.q)
    def l11l1ll1l1l_Krypto_(self):
        l1l1111_Krypto_ (u"ࠤ࡛ࠥࠦ࡫ࡲࡪࡨࡼࠤ࡮ࡳࡰࡰࡴࡷࠤࡴ࡬ࠠࡓࡕࡄࡔࡷ࡯ࡶࡢࡶࡨࡏࡪࡿࠠࡅࡇࡕࠤࡘࡋࡑࡖࡇࡑࡇࡊ࠲ࠠࡦࡰࡦࡳࡩ࡫ࡤࠡࡹ࡬ࡸ࡭ࠦࡐࡆࡏࠣࡥࡸࠦࡢࡺࡶࡨࠤࡸࡺࡲࡪࡰࡪࠦࠧࠨᡃ")
        key = l1l11lll1_Krypto_.l11ll1111l_Krypto_(b(self.l11l1l1ll1l_Krypto_))
        self.assertEqual(key.l1l1111l1l_Krypto_(),True)
        self.assertEqual(key.n, self.n)
        self.assertEqual(key.e, self.e)
        self.assertEqual(key.d, self.d)
        self.assertEqual(key.p, self.p)
        self.assertEqual(key.q, self.q)
    def l11ll111ll1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠥࠦࠧ࡜ࡥࡳ࡫ࡩࡽࠥ࡯࡭ࡱࡱࡵࡸࠥࡵࡦࠡࡔࡖࡅࡕࡸࡩࡷࡣࡷࡩࡐ࡫ࡹࠡࡆࡈࡖ࡙ࠥࡅࡒࡗࡈࡒࡈࡋࠬࠡࡧࡱࡧࡴࡪࡥࡥࠢࡺ࡭ࡹ࡮ࠠࡑࡇࡐࠤࡦࡹࠠࡶࡰ࡬ࡧࡴࡪࡥࠣࠤࠥᡄ")
        key = l1l11lll1_Krypto_.l11ll1111l_Krypto_(self.l11l1l111l1_Krypto_)
        self.assertEqual(key.l1l1111l1l_Krypto_(),False)
        self.assertEqual(key.n, self.n)
        self.assertEqual(key.e, self.e)
    def l11l1ll1l11_Krypto_(self):
        l1l1111_Krypto_ (u"ࠦࠧࠨࡖࡦࡴ࡬ࡪࡾࠦࡩ࡮ࡲࡲࡶࡹࠦ࡯ࡧࠢࡖࡹࡧࡰࡥࡤࡶࡓࡹࡧࡲࡩࡤࡍࡨࡽࡎࡴࡦࡰࠢࡇࡉࡗࠦࡓࡆࡓࡘࡉࡓࡉࡅ࠭ࠢࡨࡲࡨࡵࡤࡦࡦࠣࡻ࡮ࡺࡨࠡࡒࡈࡑࠥࡧࡳࠡࡤࡼࡸࡪࠦࡳࡵࡴ࡬ࡲ࡬ࠨࠢࠣᡅ")
        key = l1l11lll1_Krypto_.l11ll1111l_Krypto_(b(self.l11l1l111l1_Krypto_))
        self.assertEqual(key.l1l1111l1l_Krypto_(),False)
        self.assertEqual(key.n, self.n)
        self.assertEqual(key.e, self.e)
    def l11l1ll111l_Krypto_(self):
        l1l1111_Krypto_ (u"ࠧࠨࠢࡗࡧࡵ࡭࡫࡯ࡥࡴࠢࡷ࡬ࡦࡺࠠࡵࡪࡨࠤ࡮ࡳࡰࡰࡴࡷࡩࡩࠦ࡫ࡦࡻࠣ࡭ࡸࠦࡳࡵ࡫࡯ࡰࠥࡧࠠࡷࡣ࡯࡭ࡩࠦࡒࡔࡃࠣࡴࡦ࡯ࡲࠣࠤࠥᡆ")
        key = l1l11lll1_Krypto_.l11ll1111l_Krypto_(self.l11l1l1ll1l_Krypto_)
        l11l1ll11ll_Krypto_ = key.l1_Krypto_(key.l1lllll_Krypto_(b(l1l1111_Krypto_ (u"ࠨࡔࡦࡵࡷࠦᡇ"))),0)
        self.assertEqual(l11l1ll11ll_Krypto_[0],b(l1l1111_Krypto_ (u"ࠢࡕࡧࡶࡸࠧᡈ")))
    def l11l1l1lll1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠣࠤ࡚ࠥࡪࡸࡩࡧ࡫ࡨࡷࠥࡺࡨࡢࡶࠣࡸ࡭࡫ࠠࡪ࡯ࡳࡳࡷࡺࡥࡥࠢ࡮ࡩࡾࠦࡩࡴࠢࡶࡸ࡮ࡲ࡬ࠡࡣࠣࡺࡦࡲࡩࡥࠢࡕࡗࡆࠦࡰࡢ࡫ࡵࠦࠧࠨᡉ")
        key = l1l11lll1_Krypto_.l11ll1111l_Krypto_(self.l11ll1111l1_Krypto_)
        l11l1ll11ll_Krypto_ = key.l1_Krypto_(key.l1lllll_Krypto_(b(l1l1111_Krypto_ (u"ࠤࡗࡩࡸࡺࠢᡊ"))),0)
        self.assertEqual(l11l1ll11ll_Krypto_[0],b(l1l1111_Krypto_ (u"ࠥࡘࡪࡹࡴࠣᡋ")))
    def l11l1lllll1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠦࠧࠨࡖࡦࡴ࡬ࡪࡾࠦࡩ࡮ࡲࡲࡶࡹࠦ࡯ࡧࠢࡒࡴࡪࡴࡓࡔࡊࠣࡴࡺࡨ࡬ࡪࡥࠣ࡯ࡪࡿࠢࠣࠤᡌ")
        key = self.l11l1llll11_Krypto_.l11ll1111l_Krypto_(self.l11l1l1l1l1_Krypto_)
        self.assertEqual(key.n, self.n)
        self.assertEqual(key.e, self.e)
    def l11ll1111ll_Krypto_(self):
        l1l1111_Krypto_ (u"ࠧࠨࠢࡗࡧࡵ࡭࡫ࡿࠠࡪ࡯ࡳࡳࡷࡺࠠࡰࡨࠣࡩࡳࡩࡲࡺࡲࡷࡩࡩࠦࡐࡳ࡫ࡹࡥࡹ࡫ࡋࡦࡻࡌࡲ࡫ࡵࠠࡅࡇࡕࠤࡘࡋࡑࡖࡇࡑࡇࡊࠨࠢࠣᡍ")
        for t in self.l11l1lll11l_Krypto_:
            key = self.l11l1llll11_Krypto_.l11ll1111l_Krypto_(t[1], t[0])
            self.assertTrue(key.l1l1111l1l_Krypto_())
            self.assertEqual(key.n, self.n)
            self.assertEqual(key.e, self.e)
            self.assertEqual(key.d, self.d)
            self.assertEqual(key.p, self.p)
            self.assertEqual(key.q, self.q)
    def l11l1lll1l1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠨࠢࠣࡘࡨࡶ࡮࡬ࡹࠡ࡫ࡰࡴࡴࡸࡴࠡࡱࡩࠤࡺࡴࡥ࡯ࡥࡵࡽࡵࡺࡥࡥࠢࡓࡶ࡮ࡼࡡࡵࡧࡎࡩࡾࡏ࡮ࡧࡱࠣࡈࡊࡘࠠࡔࡇࡔ࡙ࡊࡔࡃࡆࠤࠥࠦᡎ")
        key = self.l11l1llll11_Krypto_.l11ll1111l_Krypto_(self.l11ll111111_Krypto_)
        self.assertTrue(key.l1l1111l1l_Krypto_())
        self.assertEqual(key.n, self.n)
        self.assertEqual(key.e, self.e)
        self.assertEqual(key.d, self.d)
        self.assertEqual(key.p, self.p)
        self.assertEqual(key.q, self.q)
    def l11ll11l11l_Krypto_(self):
        l1l1111_Krypto_ (u"ࠢࠣࠤ࡙ࡩࡷ࡯ࡦࡺࠢ࡬ࡱࡵࡵࡲࡵࠢࡲࡪࠥࡻ࡮ࡦࡰࡦࡶࡾࡶࡴࡦࡦࠣࡔࡷ࡯ࡶࡢࡶࡨࡏࡪࡿࡉ࡯ࡨࡲࠤࡉࡋࡒࠡࡕࡈࡕ࡚ࡋࡎࡄࡇ࠯ࠤࡪࡴࡣࡰࡦࡨࡨࠥࡽࡩࡵࡪࠣࡔࡊࡓࠢࠣࠤᡏ")
        key = self.l11l1llll11_Krypto_.l11ll1111l_Krypto_(self.l11l1l11l1l_Krypto_)
        self.assertTrue(key.l1l1111l1l_Krypto_())
        self.assertEqual(key.n, self.n)
        self.assertEqual(key.e, self.e)
        self.assertEqual(key.d, self.d)
        self.assertEqual(key.p, self.p)
        self.assertEqual(key.q, self.q)
    def l11l1l1l1ll_Krypto_(self):
        l1l1111_Krypto_ (u"ࠣࠤ࡚ࠥࡪࡸࡩࡧࡻࠣ࡭ࡲࡶ࡯ࡳࡶࠣࡳ࡫ࠦࡒࡔࡃࡓࡹࡧࡲࡩࡤࡍࡨࡽࠥࡊࡅࡓࠢࡖࡉࡖ࡛ࡅࡏࡅࡈࠦࠧࠨᡐ")
        l11l1l111l_Krypto_ = l11l1lll1l_Krypto_.l11l11llll_Krypto_([17, 3]).encode()
        key = self.l11l1llll11_Krypto_.l11ll1111l_Krypto_(l11l1l111l_Krypto_)
        self.assertEqual(key.n, 17)
        self.assertEqual(key.e, 3)
    def l11l1ll11l1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠤ࡛ࠥࠦ࡫ࡲࡪࡨࡼࠤ࡮ࡳࡰࡰࡴࡷࠤࡴ࡬ࠠࡓࡕࡄࡔࡺࡨ࡬ࡪࡥࡎࡩࡾࠦࡄࡆࡔࠣࡗࡊࡗࡕࡆࡐࡆࡉ࠱ࠦࡥ࡯ࡥࡲࡨࡪࡪࠠࡸ࡫ࡷ࡬ࠥࡖࡅࡎࠤࠥࠦᡑ")
        l11l1l111l_Krypto_ = l11l1lll1l_Krypto_.l11l11llll_Krypto_([17, 3]).encode()
        l11l11ll11_Krypto_ = l11l1l11lll_Krypto_(l11l1l111l_Krypto_)
        key = self.l11l1llll11_Krypto_.l11ll1111l_Krypto_(l11l11ll11_Krypto_)
        self.assertEqual(key.n, 17)
        self.assertEqual(key.e, 3)
    def l11l1l11l11_Krypto_(self):
        key = self.l11l1llll11_Krypto_.l1l1l1111l_Krypto_([self.n, self.e, self.d, self.p, self.q, self.l11ll11l111_Krypto_])
        l11l1l1l111_Krypto_ = key.l11l11ll1l_Krypto_(l1l1111_Krypto_ (u"ࠥࡈࡊࡘࠢᡒ"))
        self.assertEqual(l11l1l1l111_Krypto_, self.l11ll1111l1_Krypto_)
    def l11l1l11ll1_Krypto_(self):
        key = self.l11l1llll11_Krypto_.l1l1l1111l_Krypto_([self.n, self.e])
        l11l1l1l111_Krypto_ = key.l11l11ll1l_Krypto_(l1l1111_Krypto_ (u"ࠦࡉࡋࡒࠣᡓ"))
        self.assertEqual(l11l1l1l111_Krypto_, self.l11ll11111l_Krypto_)
    def l11l1ll1111_Krypto_(self):
        key = self.l11l1llll11_Krypto_.l1l1l1111l_Krypto_([self.n, self.e, self.d, self.p, self.q, self.l11ll11l111_Krypto_])
        l11l1l111ll_Krypto_ = key.l11l11ll1l_Krypto_(l1l1111_Krypto_ (u"ࠧࡖࡅࡎࠤᡔ"))
        self.assertEqual(l11l1l111ll_Krypto_, b(self.l11l1l1ll1l_Krypto_))
    def l11l1l1111l_Krypto_(self):
        key = self.l11l1llll11_Krypto_.l1l1l1111l_Krypto_([self.n, self.e])
        l11l1l111ll_Krypto_ = key.l11l11ll1l_Krypto_(l1l1111_Krypto_ (u"ࠨࡐࡆࡏࠥᡕ"))
        self.assertEqual(l11l1l111ll_Krypto_, b(self.l11l1l111l1_Krypto_))
    def l11ll111l1l_Krypto_(self):
        key = self.l11l1llll11_Krypto_.l1l1l1111l_Krypto_([self.n, self.e])
        l11l1l1llll_Krypto_ = key.l11l11ll1l_Krypto_(l1l1111_Krypto_ (u"ࠢࡐࡲࡨࡲࡘ࡙ࡈࠣᡖ")).split()
        l11l1lll1ll_Krypto_ = self.l11l1l1l1l1_Krypto_.split()
        self.assertEqual(l11l1l1llll_Krypto_[0], l11l1lll1ll_Krypto_[0])
        self.assertEqual(l11l1l1llll_Krypto_[1], l11l1lll1ll_Krypto_[1])
    def l11l1l1111l_Krypto_(self):
        key = self.l11l1llll11_Krypto_.l1l1l1111l_Krypto_([self.n, self.e, self.d, self.p, self.q, self.l11ll11l111_Krypto_])
        t = list(map(b,self.l11l1lll11l_Krypto_[1]))
        key._11l1lll11_Krypto_ = lambda l11l1111l1_Krypto_: (t[2]*divmod(l11l1111l1_Krypto_+len(t[2]),len(t[2]))[0])[:l11l1111l1_Krypto_]
        l11l1l111ll_Krypto_ = key.l11l11ll1l_Krypto_(l1l1111_Krypto_ (u"ࠣࡒࡈࡑࠧᡗ"), t[0])
        self.assertEqual(l11l1l111ll_Krypto_, t[1])
    def l11ll111l1l_Krypto_(self):
        key = self.l11l1llll11_Krypto_.l1l1l1111l_Krypto_([self.n, self.e, self.d, self.p, self.q, self.l11ll11l111_Krypto_])
        l11l1l1l111_Krypto_ = key.l11l11ll1l_Krypto_(l1l1111_Krypto_ (u"ࠤࡇࡉࡗࠨᡘ"), l11l1l11l1_Krypto_=8)
        self.assertEqual(l11l1l1l111_Krypto_, self.l11ll111111_Krypto_)
    def l11l1lll111_Krypto_(self):
        key = self.l11l1llll11_Krypto_.l1l1l1111l_Krypto_([self.n, self.e, self.d, self.p, self.q, self.l11ll11l111_Krypto_])
        l11l1l111ll_Krypto_ = key.l11l11ll1l_Krypto_(l1l1111_Krypto_ (u"ࠥࡔࡊࡓࠢᡙ"), l11l1l11l1_Krypto_=8)
        self.assertEqual(l11l1l111ll_Krypto_, b(self.l11l1l11l1l_Krypto_))
class l11l1ll1lll_Krypto_(l11l1llllll_Krypto_):
    def setUp(self):
        self.l11l1llll11_Krypto_ = l1l11lll1_Krypto_.l11l111ll1_Krypto_(l1l11l1ll1_Krypto_=0)
class l11ll111l11_Krypto_(l11l1llllll_Krypto_):
    def setUp(self):
        self.l11l1llll11_Krypto_ = l1l11lll1_Krypto_.l11l111ll1_Krypto_(l1l11l1ll1_Krypto_=1)
if __name__ == l1l1111_Krypto_ (u"ࠫࡤࡥ࡭ࡢ࡫ࡱࡣࡤ࠭ᡚ"):
    l1lll111111_Krypto_.main()
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    tests = []
    try:
        from l111ll1_Krypto_.l11l11l1_Krypto_ import _1l11ll111_Krypto_
        tests += l1lll1111l1_Krypto_(l11ll111l11_Krypto_)
    except ImportError:
        pass
    tests += l1lll1111l1_Krypto_(l11l1ll1lll_Krypto_)
    return tests
if __name__ == l1l1111_Krypto_ (u"ࠬࡥ࡟࡮ࡣ࡬ࡲࡤࡥࠧᡛ"):
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"࠭ࡳࡶ࡫ࡷࡩࠬᡜ"))