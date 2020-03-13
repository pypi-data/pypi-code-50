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
l1l1111_Krypto_ (u"ࠣࠤࠥࡗࡪࡲࡦ࠮ࡶࡨࡷࡹࠦࡳࡶ࡫ࡷࡩࠥ࡬࡯ࡳࠢࡆࡶࡾࡶࡴࡰ࠰ࡆ࡭ࡵ࡮ࡥࡳ࠰ࡄࡖࡈ࠸ࠢࠣࠤᇿ")
__revision__ = l1l1111_Krypto_ (u"ࠤࠧࡍࡩࠪࠢሀ")
from .common import dict
import unittest as l1lll111111_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
l1ll11lllll_Krypto_ = [
    (l1l1111_Krypto_ (u"ࠪ࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠭ሁ"), l1l1111_Krypto_ (u"ࠫࡪࡨࡢ࠸࠹࠶ࡪ࠾࠿࠳࠳࠹࠻ࡩ࡫࡬ࠧሂ"), l1l1111_Krypto_ (u"ࠬ࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰ࠨሃ"),
        l1l1111_Krypto_ (u"࠭ࡒࡇࡅ࠵࠶࠻࠾࠭࠲ࠩሄ"), dict(l1l1lll1lll_Krypto_=63)),
    (l1l1111_Krypto_ (u"ࠧࡧࡨࡩࡪ࡫࡬ࡦࡧࡨࡩࡪ࡫࡬ࡦࡧࡨࠪህ"), l1l1111_Krypto_ (u"ࠨ࠴࠺࠼ࡧ࠸࠷ࡦ࠶࠵ࡩ࠷࡬࠰ࡥ࠶࠼ࠫሆ"), l1l1111_Krypto_ (u"ࠩࡩࡪ࡫࡬ࡦࡧࡨࡩࡪ࡫࡬ࡦࡧࡨࡩࡪࠬሇ"),
        l1l1111_Krypto_ (u"ࠪࡖࡋࡉ࠲࠳࠸࠻࠱࠷࠭ለ"), dict(l1l1lll1lll_Krypto_=64)),
    (l1l1111_Krypto_ (u"ࠫ࠶࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠷ࠧሉ"), l1l1111_Krypto_ (u"ࠬ࠹࠰࠷࠶࠼ࡩࡩ࡬࠹ࡣࡧ࠺ࡨ࠷ࡩ࠲ࠨሊ"), l1l1111_Krypto_ (u"࠭࠳࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱ࠩላ"),
        l1l1111_Krypto_ (u"ࠧࡓࡈࡆ࠶࠷࠼࠸࠮࠵ࠪሌ"), dict(l1l1lll1lll_Krypto_=64)),
    (l1l1111_Krypto_ (u"ࠨ࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳ࠫል"), l1l1111_Krypto_ (u"ࠩ࠹࠵ࡦ࠾ࡡ࠳࠶࠷ࡥࡩࡧࡣࡤࡥࡩ࠴ࠬሎ"), l1l1111_Krypto_ (u"ࠪ࠼࠽࠭ሏ"),
        l1l1111_Krypto_ (u"ࠫࡗࡌࡃ࠳࠴࠹࠼࠲࠺ࠧሐ"), dict(l1l1lll1lll_Krypto_=64)),
    (l1l1111_Krypto_ (u"ࠬ࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰ࠨሑ"), l1l1111_Krypto_ (u"࠭࠶ࡤࡥࡩ࠸࠸࠶࠸࠺࠹࠷ࡧ࠷࠼࠷ࡧࠩሒ"), l1l1111_Krypto_ (u"ࠧ࠹࠺ࡥࡧࡦ࠿࠰ࡦ࠻࠳࠼࠼࠻ࡡࠨሓ"),
        l1l1111_Krypto_ (u"ࠨࡔࡉࡇ࠷࠸࠶࠹࠯࠸ࠫሔ"), dict(l1l1lll1lll_Krypto_=64)),
    (l1l1111_Krypto_ (u"ࠩ࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴ࠬሕ"), l1l1111_Krypto_ (u"ࠪ࠵ࡦ࠾࠰࠸ࡦ࠵࠻࠷ࡨࡢࡦ࠷ࡧࡦ࠶࠭ሖ"), l1l1111_Krypto_ (u"ࠫ࠽࠾ࡢࡤࡣ࠼࠴ࡪ࠿࠰࠹࠹࠸ࡥ࠼࡬࠰ࡧ࠹࠼ࡧ࠸࠾࠴࠷࠴࠺ࡦࡦ࡬ࡢ࠳ࠩሗ"),
        l1l1111_Krypto_ (u"ࠬࡘࡆࡄ࠴࠵࠺࠽࠳࠶ࠨመ"), dict(l1l1lll1lll_Krypto_=64)),
    (l1l1111_Krypto_ (u"࠭࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱ࠩሙ"), l1l1111_Krypto_ (u"ࠧ࠳࠴࠹࠽࠺࠻࠲ࡢࡤ࠳ࡪ࠽࠻ࡣࡢ࠸ࠪሚ"), l1l1111_Krypto_ (u"ࠨ࠺࠻ࡦࡨࡧ࠹࠱ࡧ࠼࠴࠽࠽࠵ࡢ࠹ࡩ࠴࡫࠽࠹ࡤ࠵࠻࠸࠻࠸࠷ࡣࡣࡩࡦ࠷࠭ማ"),
        l1l1111_Krypto_ (u"ࠤࡕࡊࡈ࠸࠲࠷࠺࠰࠻ࠧሜ"), dict(l1l1lll1lll_Krypto_=128)),
    (l1l1111_Krypto_ (u"ࠪ࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠭ም"), l1l1111_Krypto_ (u"ࠫ࠺ࡨ࠷࠹ࡦ࠶ࡥ࠹࠹ࡤࡧࡨࡩ࠵࡫࠷ࠧሞ"),
        l1l1111_Krypto_ (u"ࠬ࠾࠸ࡣࡥࡤ࠽࠵࡫࠹࠱࠺࠺࠹ࡦ࠽ࡦ࠱ࡨ࠺࠽ࡨ࠹࠸࠵࠸࠵࠻ࡧࡧࡦࡣ࠴࠴࠺࡫࠾࠰ࡢ࠸ࡩ࠼࠺࠿࠲࠱࠷࠻࠸ࡨ࠺࠲ࡧࡥࡨࡦ࠵ࡨࡥ࠳࠷࠸ࡨࡦ࡬࠱ࡦࠩሟ"),
        l1l1111_Krypto_ (u"ࠨࡒࡇࡅ࠵࠶࠻࠾࠭࠹ࠤሠ"), dict(l1l1lll1lll_Krypto_=129)),
    (l1l1111_Krypto_ (u"ࠧ࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲ࠪሡ"), l1l1111_Krypto_ (u"ࠨ࠸࠵࠸࡫ࡨ࠳ࡦ࠺࠻࠻࠹࠷࠹ࡦ࠶࠻ࠫሢ"), l1l1111_Krypto_ (u"ࠩ࠸࠴࠻࠾࠶࠺࠸ࡦ࠺࠾࠽࠰࠵࠹࠹ࡧ࠻࠷࠷࠴࠹࠶ࠫሣ"),
        l1l1111_Krypto_ (u"ࠪࡔࡈ࡚ࡶ࠳࠲࠴࠱࠵࠭ሤ")),
    (l1l1111_Krypto_ (u"ࠫ࡫࡬ࡦࡧࡨࡩࡪ࡫࡬ࡦࡧࡨࡩࡪ࡫࡬ࠧሥ"), l1l1111_Krypto_ (u"ࠬ࠽࠹ࡤࡣࡧࡩ࡫࠺࠴ࡤ࠶ࡤ࠹ࡦ࠾࠵ࠨሦ"), l1l1111_Krypto_ (u"࠭࠵࠱࠸࠻࠺࠾࠼ࡣ࠷࠻࠺࠴࠹࠽࠶ࡤ࠸࠴࠻࠸࠽࠳ࠨሧ"),
        l1l1111_Krypto_ (u"ࠧࡑࡅࡗࡺ࠷࠶࠱࠮࠳ࠪረ")),
    (l1l1111_Krypto_ (u"ࠨ࠲࠳࠴࠶࠶࠲࠱࠵࠳࠸࠵࠻࠰࠷࠲࠺ࠫሩ"), l1l1111_Krypto_ (u"ࠩ࠼࠴࠹࠷࠱࠶࠴࠸ࡦ࠸࠺ࡥ࠵ࡥ࠵ࡧࠬሪ"), l1l1111_Krypto_ (u"ࠪ࠹࠵࠼࠸࠷࠻࠹ࡧ࠻࠿࠷࠱࠶࠺࠺ࡨ࠼࠱࠸࠵࠺࠷ࠬራ"),
        l1l1111_Krypto_ (u"ࠫࡕࡉࡔࡷ࠴࠳࠵࠲࠸ࠧሬ")),
    (l1l1111_Krypto_ (u"ࠬ࠶࠰࠲࠳࠵࠶࠸࠹࠴࠵࠷࠸࠺࠻࠽࠷ࠨር"), l1l1111_Krypto_ (u"࠭࠰࠸࠺࠹࠹࠻ࡧࡡࡣࡣ࠹࠵ࡨࡨࡦࡣࠩሮ"), l1l1111_Krypto_ (u"ࠧ࠶࠲࠹࠼࠻࠿࠶ࡤ࠸࠼࠻࠵࠺࠷࠷ࡥ࠹࠵࠼࠹࠷࠴ࠩሯ"),
        l1l1111_Krypto_ (u"ࠨࡒࡆࡘࡻ࠸࠰࠲࠯࠶ࠫሰ")),
    (l1l1111_Krypto_ (u"ࠩ࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴ࠬሱ"), l1l1111_Krypto_ (u"ࠪࡨ࠼ࡨࡣࡤ࠷ࡧࡦࡧ࠺ࡤ࠷ࡧ࠸࠺ࡦ࠭ሲ"), l1l1111_Krypto_ (u"ࠫ࡫࡬ࡦࡧࡨࡩࡪ࡫࡬ࡦࡧࡨࡩࡪ࡫࡬ࠧሳ"),
        l1l1111_Krypto_ (u"ࠬࡖࡃࡕࡸ࠵࠴࠶࠳࠴ࠨሴ")),
    (l1l1111_Krypto_ (u"࠭ࡦࡧࡨࡩࡪ࡫࡬ࡦࡧࡨࡩࡪ࡫࡬ࡦࡧࠩስ"), l1l1111_Krypto_ (u"ࠧ࠸࠴࠸࠽࠵࠷࠸ࡦࡥ࠸࠹࠼ࡨ࠳࠶࠹ࠪሶ"), l1l1111_Krypto_ (u"ࠨࡨࡩࡪ࡫࡬ࡦࡧࡨࡩࡪ࡫࡬ࡦࡧࡨࡩࠫሷ"),
        l1l1111_Krypto_ (u"ࠩࡓࡇ࡙ࡼ࠲࠱࠳࠰࠹ࠬሸ")),
    (l1l1111_Krypto_ (u"ࠪ࠴࠵࠶࠱࠱࠴࠳࠷࠵࠺࠰࠶࠲࠹࠴࠼࠭ሹ"), l1l1111_Krypto_ (u"ࠫ࠾࠹ࡤ࠳࠲ࡤ࠸࠾࠽ࡦ࠳ࡥࡦࡦ࠻࠸ࠧሺ"), l1l1111_Krypto_ (u"ࠬ࡬ࡦࡧࡨࡩࡪ࡫࡬ࡦࡧࡨࡩࡪ࡫࡬ࡦࠨሻ"),
        l1l1111_Krypto_ (u"࠭ࡐࡄࡖࡹ࠶࠵࠷࠭࠷ࠩሼ")),
    (l1l1111_Krypto_ (u"ࠧ࠱࠲࠴࠵࠷࠸࠳࠴࠶࠷࠹࠺࠼࠶࠸࠹ࠪሽ"), l1l1111_Krypto_ (u"ࠨࡥࡥ࠵࠺ࡧ࠷ࡧ࠺࠴࠽ࡨ࠶࠰࠲࠶ࡧࠫሾ"), l1l1111_Krypto_ (u"ࠩࡩࡪ࡫࡬ࡦࡧࡨࡩࡪ࡫࡬ࡦࡧࡨࡩࡪࠬሿ"),
        l1l1111_Krypto_ (u"ࠪࡔࡈ࡚ࡶ࠳࠲࠴࠱࠼࠭ቀ")),
    (l1l1111_Krypto_ (u"ࠫ࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶ࠧቁ"), l1l1111_Krypto_ (u"ࠬ࠼࠳ࡢࡥ࠼࠼ࡨࡪࡦ࠴࠺࠷࠷ࡦ࠽ࡡࠨቂ"), l1l1111_Krypto_ (u"࠭ࡦࡧࡨࡩࡪ࡫࡬ࡦࡧࡨࡩࡪ࡫࡬ࡦࡧ࠷࠳࠺࠺࠽࠴࠷࠷࠺࠶࠹࠽࠷࠳࠸࠸࠺࠺࠼ࡥ࠷࠳࠺࠻࠻࠷࠷࠺࠷࠶ࡩ࠺࡬ࡦࡦ࠷࠸࠷ࠬቃ"),
        l1l1111_Krypto_ (u"ࠧࡑࡅࡗࡺ࠷࠶࠱࠮࠺ࠪቄ")),
    (l1l1111_Krypto_ (u"ࠨࡨࡩࡪ࡫࡬ࡦࡧࡨࡩࡪ࡫࡬ࡦࡧࡨࡩࠫቅ"), l1l1111_Krypto_ (u"ࠩ࠶ࡪࡧ࠺࠹ࡦ࠴ࡩࡥ࠶࠸࠳࠸࠳ࡧࡨࠬቆ"), l1l1111_Krypto_ (u"ࠪࡪ࡫࡬ࡦࡧࡨࡩࡪ࡫࡬ࡦࡧࡨࡩࡪ࡫࠻࠰࠷࠷࠺࠸࠻࠻࠷࠳࠶࠺࠻࠷࠼࠵࠷࠷࠹ࡩ࠻࠷࠷࠸࠸࠴࠻࠾࠻࠳ࡦ࠷ࡩࡪࡪ࠻࠵࠴ࠩቇ"),
        l1l1111_Krypto_ (u"ࠫࡕࡉࡔࡷ࠴࠳࠵࠲࠿ࠧቈ")),
    (l1l1111_Krypto_ (u"ࠬ࠶࠰࠱࠳࠳࠶࠵࠹࠰࠵࠲࠸࠴࠻࠶࠷ࠨ቉"), l1l1111_Krypto_ (u"࠭࠴࠷࠶࠴࠸࠼࠾࠱ࡢࡤ࠶࠼࠼ࡪ࠵ࡧࠩቊ"), l1l1111_Krypto_ (u"ࠧࡧࡨࡩࡪ࡫࡬ࡦࡧࡨࡩࡪ࡫࡬ࡦࡧࡨ࠸࠴࠻࠻࠷࠵࠸࠸࠻࠷࠺࠷࠸࠴࠹࠹࠻࠻࠶ࡦ࠸࠴࠻࠼࠼࠱࠸࠻࠸࠷ࡪ࠻ࡦࡧࡧ࠸࠹࠸࠭ቋ"),
        l1l1111_Krypto_ (u"ࠨࡒࡆࡘࡻ࠸࠰࠲࠯࠴࠴ࠬቌ")),
    (l1l1111_Krypto_ (u"ࠩ࠳࠴࠶࠷࠲࠳࠵࠶࠸࠹࠻࠵࠷࠸࠺࠻ࠬቍ"), l1l1111_Krypto_ (u"ࠪࡦࡪ࠶࠹ࡥࡥ࠻࠵࡫࡫ࡡࡤࡣ࠵࠻࠶࠭቎"), l1l1111_Krypto_ (u"ࠫ࡫࡬ࡦࡧࡨࡩࡪ࡫࡬ࡦࡧࡨࡩࡪ࡫࡬࠵࠱࠸࠸࠻࠹࠼࠵࠸࠴࠷࠻࠼࠸࠶࠶࠸࠸࠺ࡪ࠼࠱࠸࠹࠹࠵࠼࠿࠵࠴ࡧ࠸ࡪ࡫࡫࠵࠶࠵ࠪ቏"),
        l1l1111_Krypto_ (u"ࠬࡖࡃࡕࡸ࠵࠴࠶࠳࠱࠲ࠩቐ")),
    (l1l1111_Krypto_ (u"࠭࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱ࠩቑ"), l1l1111_Krypto_ (u"ࠧࡦ࠸࠷࠶࠷࠷ࡥ࠷࠲࠻ࡦࡪ࠹࠰ࡢࡤࠪቒ"), l1l1111_Krypto_ (u"ࠨ࠷࠶ࡩ࠺࡬ࡦࡦ࠷࠸࠷ࠬቓ"),
        l1l1111_Krypto_ (u"ࠩࡓࡇ࡙ࡼ࠲࠱࠳࠰࠵࠷࠭ቔ")),
    (l1l1111_Krypto_ (u"ࠪࡪ࡫࡬ࡦࡧࡨࡩࡪ࡫࡬ࡦࡧࡨࡩࡪ࡫࠭ቕ"), l1l1111_Krypto_ (u"ࠫ࠽࠼࠲ࡣࡥ࠹࠴࡫ࡪࡣࡥ࠶ࡧ࠽ࡦ࠿ࠧቖ"), l1l1111_Krypto_ (u"ࠬ࠻࠳ࡦ࠷ࡩࡪࡪ࠻࠵࠴ࠩ቗"),
        l1l1111_Krypto_ (u"࠭ࡐࡄࡖࡹ࠶࠵࠷࠭࠲࠵ࠪቘ")),
    (l1l1111_Krypto_ (u"ࠧ࠱࠲࠳࠵࠵࠸࠰࠴࠲࠷࠴࠺࠶࠶࠱࠹ࠪ቙"), l1l1111_Krypto_ (u"ࠨ࠸ࡤ࠷࠹ࡪࡡ࠶࠲ࡩࡥ࠺࡫࠴࠸ࡦࡨࠫቚ"), l1l1111_Krypto_ (u"ࠩ࠸࠷ࡪ࠻ࡦࡧࡧ࠸࠹࠸࠭ቛ"),
        l1l1111_Krypto_ (u"ࠪࡔࡈ࡚ࡶ࠳࠲࠴࠱࠶࠺ࠧቜ")),
    (l1l1111_Krypto_ (u"ࠫ࠵࠶࠱࠲࠴࠵࠷࠸࠺࠴࠶࠷࠹࠺࠼࠽ࠧቝ"), l1l1111_Krypto_ (u"ࠬ࠻࠸࠵࠸࠷࠸ࡨ࠹࠴࠶࠲࠶࠵࠷࠸ࡣࠨ቞"), l1l1111_Krypto_ (u"࠭࠵࠴ࡧ࠸ࡪ࡫࡫࠵࠶࠵ࠪ቟"),
        l1l1111_Krypto_ (u"ࠧࡑࡅࡗࡺ࠷࠶࠱࠮࠳࠸ࠫበ")),
]
class l1l1llll111_Krypto_(l1lll111111_Krypto_.TestCase):
    def setUp(self):
        global l1lll111_Krypto_
        from l111ll1_Krypto_.l11111l_Krypto_ import l1lll111_Krypto_
    def runTest(self):
        l1l1111_Krypto_ (u"ࠣࠤࠥࡅࡗࡉ࠲ࠡࡹ࡬ࡸ࡭ࠦ࡫ࡦࡻ࡯ࡩࡳ࡭ࡴࡩࠢࡁࠤ࠶࠸࠸ࠣࠤࠥቡ")
        key = l1l1111_Krypto_ (u"ࠤࡻࠦቢ") * 16384
        mode = l1lll111_Krypto_.l1lll1ll_Krypto_
        self.assertRaises(ValueError, l1lll111_Krypto_.new, key, mode)
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    from l111ll1_Krypto_.l11111l_Krypto_ import l1lll111_Krypto_
    from .common import l1ll1ll11l1_Krypto_
    tests = l1ll1ll11l1_Krypto_(l1lll111_Krypto_, l1l1111_Krypto_ (u"ࠥࡅࡗࡉ࠲ࠣባ"), l1ll11lllll_Krypto_)
    tests.append(l1l1llll111_Krypto_())
    return tests
if __name__ == l1l1111_Krypto_ (u"ࠫࡤࡥ࡭ࡢ࡫ࡱࡣࡤ࠭ቤ"):
    import unittest as l1lll111111_Krypto_
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"ࠬࡹࡵࡪࡶࡨࠫብ"))