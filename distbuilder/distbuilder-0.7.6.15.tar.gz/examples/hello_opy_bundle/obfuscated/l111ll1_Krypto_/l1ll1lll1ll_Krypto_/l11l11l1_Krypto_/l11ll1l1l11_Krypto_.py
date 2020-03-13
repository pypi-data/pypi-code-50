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
l1l1111_Krypto_ (u"ࠢࠣࠤࡖࡩࡱ࡬࠭ࡵࡧࡶࡸࠥࡹࡵࡪࡶࡨࠤ࡫ࡵࡲࠡࡅࡵࡽࡵࡺ࡯࠯ࡒࡸࡦࡱ࡯ࡣࡌࡧࡼ࠲ࡊࡲࡇࡢ࡯ࡤࡰࠧࠨࠢ឵")
__revision__ = l1l1111_Krypto_ (u"ࠣࠦࡌࡨࠩࠨា")
import unittest as l1lll111111_Krypto_
from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l1ll1lllll1_Krypto_ import l1lll1111l1_Krypto_, a2b_hex, b2a_hex
from l111ll1_Krypto_ import l1ll1l11l1_Krypto_
from l111ll1_Krypto_.l11l11l1_Krypto_ import l11lll1lll_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l111l1ll_Krypto_ import *
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
class l11ll1l1ll1_Krypto_(l1lll111111_Krypto_.TestCase):
    l11ll1l1l1l_Krypto_=[
        {
        l1l1111_Krypto_ (u"ࠩࡳࠫិ")  :l1l1111_Krypto_ (u"ࠪࡆࡆ࠺ࡃࡂࡇࡄࡅࡊࡊ࠸ࡄࡄࡈ࠽࠺࠸ࡁࡇࡆ࠵࠵࠷࠼ࡃ࠷࠵ࡈࡆ࠸ࡈ࠳࠵࠷ࡇ࠺࠺ࡉ࠲ࡂ࠲ࡄ࠻࠸ࡊ࠲ࡂ࠵ࡄࡈ࠹࠷࠳࠹ࡄ࠹ࡈ࠵࠿ࡂࡅ࠻࠶࠷ࠬី"),
        l1l1111_Krypto_ (u"ࠫ࡬࠭ឹ")  :l1l1111_Krypto_ (u"ࠬ࠶࠵ࠨឺ"),
        l1l1111_Krypto_ (u"࠭ࡹࠨុ")  :l1l1111_Krypto_ (u"ࠧ࠷࠲ࡇ࠴࠻࠹࠶࠱࠲ࡈࡇࡊࡊ࠷ࡄ࠹ࡆ࠹࠺࠷࠴࠷࠲࠵࠴ࡊ࠽ࡁ࠴࠳ࡆ࠸࠹࠽࠶ࡆ࠻࠺࠽࠸ࡈࡅࡂࡇࡇ࠸࠷࠶ࡆࡆࡅ࠼ࡉ࠼࠽࠶࠱࠶ࡆࡅࡊ࠺ࡅࡇࠩូ"),
        l1l1111_Krypto_ (u"ࠨࡺࠪួ")  :l1l1111_Krypto_ (u"ࠩ࠴ࡈ࠸࠿࠱ࡃࡃ࠵ࡉࡊ࠹ࡃ࠴࠹ࡉࡉ࠶ࡈࡁ࠲࠹࠸ࡅ࠻࠿ࡂ࠳ࡅ࠺࠷ࡆ࠷࠱࠳࠵࠻ࡅࡉ࠽࠷࠷࠹࠸࠽࠸࠸ࠧើ"),
        l1l1111_Krypto_ (u"ࠪ࡯ࠬឿ")  :l1l1111_Krypto_ (u"ࠫࡋ࠻࠸࠺࠵ࡆ࠹ࡇࡇࡂ࠵࠳࠶࠵࠷࠼࠴࠱࠸࠹ࡊ࠺࠽ࡁࡃ࠵ࡇ࠼ࡆࡊ࠸࠺ࡇ࠶࠽࠶ࡇ࠰ࡃ࠸࠻ࡅ࠻࠾ࡁ࠲ࠩៀ"),
        l1l1111_Krypto_ (u"ࠬࡶࡴࠨេ") :l1l1111_Krypto_ (u"࠭࠴࠹࠸࠸࠺ࡈ࠼ࡃ࠷ࡈ࠵࠴࠼࠺࠶࠹࠸࠸࠻࠷࠼࠵ࠨែ"),
        l1l1111_Krypto_ (u"ࠧࡤࡶ࠴ࠫៃ"):l1l1111_Krypto_ (u"ࠨ࠵࠵ࡆࡋࡊ࠵ࡇ࠶࠻࠻࠾࠼࠶ࡄࡇࡄ࠽ࡊ࠿࠳࠶࠸࠺࠵࠺࠽࠸࠹ࡅ࠷࠽࠶ࡋࡃ࠶࠳࠸ࡉ࠹ࡋࡄ࠵࠺ࡅ࠹࠽ࡌ࠰ࡇ࠲࠳࠽࠼࠷ࡅ࠺࠵ࡄࡅࡆ࠻ࡅࡄ࠹ࠪោ"),
        l1l1111_Krypto_ (u"ࠩࡦࡸ࠷࠭ៅ"):l1l1111_Krypto_ (u"ࠪ࠻ࡇࡋ࠸ࡇࡄࡉࡊ࠸࠷࠷ࡄ࠻࠶ࡉ࠽࠸ࡆࡄࡇࡉ࠽ࡇࡊ࠵࠲࠷࠵࠼࠹ࡈࡁ࠶࠲࠹࠺࠵࠹ࡆࡆࡃ࠵࠹ࡉ࠶࠱ࡄ࠲ࡆࡆ࠽࠽࠴ࡂ࠵࠴ࡊ࠸࠷࠵ࡆࡇ࠹࠼ࠬំ")
        },
        {
        l1l1111_Krypto_ (u"ࠫࡵ࠭ះ")  :l1l1111_Krypto_ (u"ࠬࡌ࠱ࡃ࠳࠻ࡅࡊ࠿ࡆ࠸ࡄ࠷ࡉ࠵࠾ࡆࡅࡃ࠼ࡅ࠵࠺࠸࠴࠴ࡉ࠸ࡊ࠿࠱࠺ࡆ࠻࠽࠹࠼࠲ࡇࡆ࠶࠵ࡇࡌ࠱࠳ࡈ࠼࠶࠼࠿࠱ࡂ࠻࠶࠹࠶࠿ࡆ࠸࠷࠳࠻࠻ࡊ࠶ࡄࡇ࠶࠽࠹࠸࠶࠹࠻ࡆࡈࡋࡌ࠲ࡇ࠵࠷࠸ࡈࡇࡆࡇ࠲ࡉ࠼࠷ࡊ࠰࠲࠺࠹࠸ࡋ࠼࠹ࡇ࠵ࡄࡉࡈࡌ࠵࠷࠸ࡆ࠻࠼࠺ࡃࡃࡃࡆࡊ࠼࠸࠸ࡃ࠺࠴ࡅ࠷࠸࠷ࠨៈ"),
        l1l1111_Krypto_ (u"࠭ࡧࠨ៉")  :l1l1111_Krypto_ (u"ࠧ࠱࠹ࠪ៊"),
        l1l1111_Krypto_ (u"ࠨࡻࠪ់")  :l1l1111_Krypto_ (u"ࠩ࠹࠼࠽࠼࠲࠹ࡅ࠹࠻࠻ࡋ࠴ࡇ࠲࠸ࡈ࠻࠹࠰ࡆ࠳ࡅࡉ࠸࠿ࡄ࠱࠲࠹࠺࠶࠽࠸ࡄࡃ࠺ࡅࡆ࠾࠳࠹࠵࠹ࡆ࠻࠺࠵ࡅࡇ࠸ࡅࡉࡊ࠳࠶࠻ࡅ࠸࠽࠸࠵ࡂ࠳࠵ࡆ࠵࠸ࡅࡇ࠶࠵࠹࠷ࡋ࠴ࡆ࠸ࡉࡅ࠾ࡈࡅࡄ࠳ࡇࡆ࠵ࡈࡅ࠺࠲ࡉ࠺ࡉ࠽ࡃ࠹࠸࠵࠽ࡈࡇࡂࡃ࠸ࡈ࠹࠸࠷ࡆ࠵࠹࠵ࡆ࠷࠼࠶࠵࠺࠹࠼࠶࠻࠶ࡆ࠴࠳ࡇࠬ៌"),
        l1l1111_Krypto_ (u"ࠪࡼࠬ៍")  :l1l1111_Krypto_ (u"ࠫ࠶࠺ࡅ࠷࠲ࡅ࠵ࡇࡊࡆࡅ࠵࠶࠸࠸࠼ࡃ࠱ࡆࡄ࠼ࡆ࠸࠲ࡇࡆࡆ࠵࠹ࡇ࠲ࡄࡅࡇࡆࡇࡋࡄ࠱࠸࠵࠻ࡈࡋ࠶࠹ࠩ៎"),
        l1l1111_Krypto_ (u"ࠬࡱࠧ៏")  :l1l1111_Krypto_ (u"࠭࠳࠹ࡆࡅࡊ࠶࠺ࡅ࠲ࡈ࠶࠵࠾ࡈࡄࡂ࠻ࡅࡅࡇ࠹࠳ࡆࡇࡈࡅࡉࡉࡁࡇ࠸ࡅ࠶ࡊࡇ࠵࠳࠷࠳࠹࠼࠽ࡁࡄࡇ࠺ࠫ័"),
        l1l1111_Krypto_ (u"ࠧࡱࡶࠪ៑") :l1l1111_Krypto_ (u"ࠨ࠶࠻࠺࠺࠼ࡃ࠷ࡅ࠹ࡊ࠷࠶࠷࠵࠸࠻࠺࠺࠽࠲࠷࠷្ࠪ"),
        l1l1111_Krypto_ (u"ࠩࡦࡸ࠶࠭៓"):l1l1111_Krypto_ (u"ࠪ࠶࠾࠶ࡆ࠹࠷࠶࠴ࡈ࠸ࡃࡄ࠵࠴࠶ࡊࡉ࠴࠷࠳࠺࠼࠼࠸࠴ࡇ࠳࠼࠺ࡋ࠹࠰࠹ࡃࡇ࠸ࡈ࠻࠲࠴ࡅࡈࡅࡇࡈ࠰࠱࠳ࡉࡅࡈࡈ࠰࠶࠲࠹ࡆࡋࡋࡄ࠷࠹࠹࠴࠽࠹ࡆࡆ࠲ࡉ࠶࠼ࡇࡃ࠷࠺࠻ࡆ࠺ࡉ࠷࠵࠻ࡄࡆ࠸ࡉࡂ࠹ࡃ࠻࠴ࡈࡊ࠶ࡇ࠹࠳࠽࠹ࡊࡂࡂ࠶࠵࠵ࡋࡈ࠱࠺࠶࠷࠶ࡋ࠻ࡁ࠵࠳࠶ࡉ࠵࠼ࡁ࠺࠹࠺࠶ࡇ࠭។"),
        l1l1111_Krypto_ (u"ࠫࡨࡺ࠲ࠨ៕"):l1l1111_Krypto_ (u"ࠬ࠷ࡄ࠷࠻ࡄࡅࡆࡊ࠱ࡅࡅ࠸࠴࠹࠿࠳ࡇࡄ࠴ࡆ࠽ࡋ࠸࠸࠴࠴ࡈ࠻࠸࠱ࡅ࠸࠻࠷ࡋ࠹ࡂࡇ࠳࠶࠶࠶ࡈࡅ࠳࠳ࡅࡇ࠹ࡇ࠴࠴ࡇ࠴࠵ࡇ࠺࠰ࡄ࠻ࡇ࠸ࡉ࠿ࡃ࠹࠲ࡇࡉ࠸ࡇࡁࡄ࠴ࡄࡆ࠻࠶ࡄ࠴࠳࠺࠼࠷ࡈ࠱࠷ࡄ࠹࠵࠶࠷࠲ࡆ࠸࠻࠶࠷࠶࠸࠹࠻ࡇ࠹࠸ࡉ࠴ࡄ࠵࠴࠷࠻ࡋࡅ࠷ࡈ࠹ࡇࡊ࠼࠱ࡇ࠺ࡄ࠶࠸ࡇ࠰ࠨ៖")
        }
    ]
    l11ll1ll11l_Krypto_=[
        {
        l1l1111_Krypto_ (u"࠭ࡰࠨៗ")  :l1l1111_Krypto_ (u"ࠧࡅ࠴ࡉ࠷ࡈ࠺࠱ࡆࡃ࠹࠺࠺࠹࠰࠹࠵࠻ࡅ࠼࠶࠴ࡂ࠶࠻ࡊࡋࡇࡃ࠺࠵࠶࠸ࡋ࠺࠷࠱࠳ࡈࡇࡊ࠹ࡁ࠺࠹ࡆࡉࡊ࠺ࡃ࠷࠻ࡇࡈ࠵࠷ࡁࡆ࠹࠴࠶࠾ࡊࡄ࠸ࠩ៘"),
        l1l1111_Krypto_ (u"ࠨࡩࠪ៙")  :l1l1111_Krypto_ (u"ࠩ࠳࠹ࠬ៚"),
        l1l1111_Krypto_ (u"ࠪࡽࠬ៛")  :l1l1111_Krypto_ (u"ࠫࡈ࠹ࡆ࠺࠶࠴࠻ࡉࡉ࠰ࡅࡃࡉࡉࡆ࠼ࡁ࠱࠷ࡆ࠵ࡉ࠸࠳࠴࠵ࡅ࠻ࡆ࠿࠵ࡆ࠸࠶ࡆ࠸ࡌ࠴ࡇ࠴࠻ࡇࡈ࠿࠶࠳࠴࠸࠸ࡇ࠹࠲࠶࠸࠼࠼࠹ࡊ࠱࠱࠳࠵ࡉ࠼࠭ៜ"),
        l1l1111_Krypto_ (u"ࠬࡾࠧ៝")  :l1l1111_Krypto_ (u"࠭࠱࠷࠷ࡈ࠸ࡆ࠹࠹ࡃࡇ࠷࠸ࡉ࠻ࡁ࠳ࡆ࠻ࡆ࠶࠹࠳࠳ࡆ࠷࠵࠻ࡈࡃ࠶࠷࠼࠺࠶࠼ࡆ࠶࠵࠹ࡆࡈ࠽࠳࠶ࡄࡅࠫ៞"),
        l1l1111_Krypto_ (u"ࠧ࡬ࠩ៟")  :l1l1111_Krypto_ (u"ࠨࡅ࠺ࡊ࠵ࡉ࠷࠺࠶ࡄ࠻ࡊࡇࡄ࠸࠴࠹ࡉ࠷࠻ࡁ࠵࠹ࡉࡊ࠽࠿࠲࠹࠲࠴࠷࠻࠾࠰ࡆ࠹࠶ࡇ࠺࠷ࡄࡅ࠵ࡇ࠻ࡉ࠿࠹ࡃࡈࡇࡅ࠽ࡌ࠴࠺࠴࠸࠼࠺࠿࠲࠹ࡈࠪ០"),
        l1l1111_Krypto_ (u"ࠩ࡫ࠫ១")  :l1l1111_Krypto_ (u"ࠪ࠸࠽࠼࠵࠷ࡅ࠹ࡇ࠻ࡌ࠲࠱࠹࠷࠺࠽࠼࠵࠸࠴࠹࠹ࠬ២"),
        l1l1111_Krypto_ (u"ࠫࡸ࡯ࡧ࠲ࠩ៣"):l1l1111_Krypto_ (u"ࠬ࠹࠵ࡄࡃ࠼࠼࠶࠹࠳࠸࠹࠼ࡉ࠷࠶࠷࠴ࡇࡉ࠷࠶࠷࠶࠶ࡃࡉࡇࡉࡋࡂ࠸࠸࠷ࡈࡉ࠻࠴ࡆ࠻࠹ࡅࡉࡋ࠸࠶࠳࠺࠵࠺࠺࠹࠶ࡈ࠼ࡇ࠻࠹࠵ࡆ࠳ࡈ࠻ࡈ࠸ࠧ៤"),
        l1l1111_Krypto_ (u"࠭ࡳࡪࡩ࠵ࠫ៥"):l1l1111_Krypto_ (u"ࠧ࠱࠳࠶࠹ࡇ࠾࠸ࡃ࠳࠴࠹࠶࠸࠷࠺ࡈࡈ࠹ࡉ࠾࠰࠸࠺ࡇ࠸ࡋࡉ࠶࠹࠷ࡈࡉ࠽࠷࠱࠸࠹ࡈࡉ࠾࠾࠰࠳ࡃࡅ࠵࠷࠹ࡁ࠸࠵࠼࠶࠺ࡌࡃ࠲ࡅࡅ࠴࠺࠿ࡁ࠸ࠩ៦"),
        },
        {
        l1l1111_Krypto_ (u"ࠨࡲࠪ៧")  :l1l1111_Krypto_ (u"ࠩࡈ࠶࠹ࡉࡆ࠴ࡃ࠷ࡆ࠽ࡇ࠶ࡂࡈ࠺࠸࠾ࡊࡃࡂ࠸ࡇ࠻࠶࠺࠲࠹࠴ࡉࡉ࠹ࡇࡁࡃࡇࡈࡉ࠹࠺ࡁ࠶࠵ࡅࡆ࠻ࡋࡄ࠲࠷ࡉࡆࡊ࠹࠲ࡃ࠷ࡇ࠷ࡈ࠹ࡅࡇ࠻ࡆࡇ࠹࠷࠲࠵ࡃ࠵ࡉࡈࡇ࠳࠴࠳ࡉ࠷ࡈ࠷ࡃ࠲ࡄ࠹࠺࠼ࡇࡃࡂ࠵࠺࠺࠻࠾࠲࠶࠴࠴࠻ࡊ࠽ࡂ࠶ࡈ࠼࠼࠺࠼࠶࠵࠺ࡇ࠽࠺ࡌ࠰࠶࠵࠶࠴ࡈ࠼ࡁ࠲࠻ࡆࡊࠬ៨"),
        l1l1111_Krypto_ (u"ࠪ࡫ࠬ៩")  :l1l1111_Krypto_ (u"ࠫ࠵ࡈࠧ៪"),
        l1l1111_Krypto_ (u"ࠬࡿࠧ៫")  :l1l1111_Krypto_ (u"࠭࠲ࡂࡆ࠶ࡅ࠶࠶࠴࠺ࡅࡄ࠹ࡉ࠺ࡅࡅ࠴࠳࠻ࡇ࠸࠴࠴࠳ࡆ࠻࠾ࡇ࠸࠸࠳࠼ࡆࡇ࠺࠰࠸࠵ࡇ࠸ࡆ࠿࠴ࡆ࠶࠸࠴ࡊࡇ࠶ࡄࡇࡈ࠼ࡆ࠽࠶࠱ࡇࡅ࠴࠼ࡇࡄࡃ࠸࠺ࡇ࠵ࡊ࠵࠳ࡅ࠵࠻࠺ࡋࡅ࠹࠷ࡇ࠻ࡇ࠻࠲࠸࠺࠼࠴࠻࠷ࡅࡆ࠶࠸ࡊ࠷ࡌ࠳࠸ࡆ࠼ࡆ࠷ࡇࡅ࠶࠴࠵ࡅ࠺࠷ࡃ࠳࠺࠶࠶࠾࠽࠶࠷ࡄࡉࡉ࠻࠾ࡁࡄࠩ៬"),
        l1l1111_Krypto_ (u"ࠧࡹࠩ៭")  :l1l1111_Krypto_ (u"ࠨ࠳࠹ࡇࡇࡈ࠴ࡇ࠶࠹ࡈ࠾ࡋࡃࡄࡈ࠵࠸ࡋࡌ࠹ࡇ࠹ࡈ࠺࠸ࡉࡁࡂ࠵ࡅࡈ࠽࠿࠳࠷࠵࠷࠵࠺࠻࠵࠱࠸࠵ࡅࡇ࠭៮"),
        l1l1111_Krypto_ (u"ࠩ࡮ࠫ៯")  :l1l1111_Krypto_ (u"ࠪ࠼ࡆ࠹ࡄ࠹࠻ࡄ࠸ࡊ࠺࠲࠺ࡈࡇ࠶࠹࠽࠶ࡅ࠹ࡇ࠻࠶࠽࠲࠶࠳ࡉࡆ࠼࠿ࡂࡇ࠻࠳࠴ࡋࡌࡅ࠸࠹࠷࠸࠹ࡋ࠶ࡃࡄ࠻࠶࠾࠿ࡄࡄ࠵ࡉ࠼࠹ࡊ࠰ࡅࡆ࠸࠻ࡆࡈࡁࡃ࠷࠳࠻࠸࠸ࡁࡆ࠳࠸࠼ࡊࡇ࠵࠳ࡈ࠸ࡆ࠾ࡋ࠷ࡅ࠺࠻࠵࠸ࡋ࠸࠲ࡈࡇ࠽ࡋ࠽࠹࠵࠹࠳ࡅࡊ࠸࠲ࡇ࠺ࡉ࠵ࡈࡌ࠹ࡂࡇࡆ࠼࠷࠶ࡁ࠸࠺ࡆ࠺࠾࠭៰"),
        l1l1111_Krypto_ (u"ࠫ࡭࠭៱")  :l1l1111_Krypto_ (u"ࠬ࠺࠸࠷࠷࠹ࡇ࠻ࡉ࠶ࡇ࠴࠳࠻࠹࠼࠸࠷࠷࠺࠶࠻࠻ࠧ៲"),
        l1l1111_Krypto_ (u"࠭ࡳࡪࡩ࠴ࠫ៳"):l1l1111_Krypto_ (u"ࠧࡃࡇ࠳࠴࠶ࡇࡁࡃࡃࡉࡊࡋ࠿࠷࠷ࡇࡆ࠽࠵࠷࠶࠲࠻࠻ࡊࡇࡌࡅࡂ࠳࠷ࡇࡇࡋࡆ࠺࠸ࡅ࠴࠵࠶ࡃࡄࡅ࠳࠴࠻࠹ࡄ࠴࠵࠵࠸࠵࠷࠶ࡇ࠻ࡈ࠽࠶ࡌࡅ࠹࠲ࡇ࠼ࡋ࠿࠳࠳࠷࠻࠵࠷ࡋࡄ࠳࠶ࡇࡈࡇ࠸ࡂ࠵ࡆ࠷ࡇࡋ࠺࠴࠴࠲ࡅ࠵࠻࠿࠸࠹࠲ࡅ࠷ࡈࡋ࠸࠹࠵࠴࠷ࡇ࠻࠳࠳࠷࠸ࡆࡉ࠺ࡅࡄ࠲࠶࠻࠽࠻࠸࠷ࡈࠪ៴"),
        l1l1111_Krypto_ (u"ࠨࡵ࡬࡫࠷࠭៵"):l1l1111_Krypto_ (u"ࠩ࠸ࡉ࠷࠼࠶ࡇ࠵ࡉ࠼࠸࠽ࡂࡂ࠴࠳࠸ࡊ࠹ࡂࡃࡄ࠹ࡈࡇࡋࡃࡄ࠲࠹࠵࠶࠺࠲࠺ࡆ࠼࠺ࡋ࠾ࡃ࠸ࡅࡈ࠼ࡋ࠺ࡅࡇࡆࡉ࠽ࡉ࠺ࡃࡃ࠸࠻࠵ࡈ࠸ࡁ࠺࠷࠷࠸࠻࠾ࡁ࠴࠷࠺ࡆࡋ࠺࠲࠵࠴ࡆࡉࡈ࠽࠴࠲࠺ࡅ࠹࠶ࡊࡆࡄ࠲࠻࠵ࡇࡉࡄ࠳࠳࠵࠽࠾ࡋࡆ࠶ࡄ࠸ࡅ࠵ࡊࡄࡆࡈ࠶ࡅ࠶࠹࠹ࡂ࠳࠻࠵࠼࠻࠰࠴ࡆࡇࡉࠬ៶"),
        }
    ]
    def l11ll11ll1l_Krypto_(self):
        self._11ll1lll1l_Krypto_(128)
    def l11ll11l1ll_Krypto_(self):
        self._11ll1lll1l_Krypto_(512)
    def l11ll11ll11_Krypto_(self):
        for l11ll1l11l1_Krypto_ in self.l11ll1l1l1l_Krypto_:
            for l11ll1ll111_Krypto_ in (0,1):
                d = self.l11ll1l11ll_Krypto_(l11ll1l11l1_Krypto_, l11ll1ll111_Krypto_)
                key = l11lll1lll_Krypto_.l1l1l1111l_Krypto_(d[l1l1111_Krypto_ (u"ࠪ࡯ࡪࡿࠧ៷")])
                ct = key.l1_Krypto_(d[l1l1111_Krypto_ (u"ࠫࡵࡺࠧ៸")], d[l1l1111_Krypto_ (u"ࠬࡱࠧ៹")])
                self.assertEqual(ct[0], d[l1l1111_Krypto_ (u"࠭ࡣࡵ࠳ࠪ៺")])
                self.assertEqual(ct[1], d[l1l1111_Krypto_ (u"ࠧࡤࡶ࠵ࠫ៻")])
    def l11ll11lll1_Krypto_(self):
        for l11ll1l11l1_Krypto_ in self.l11ll1l1l1l_Krypto_:
            for l11ll1ll111_Krypto_ in (0,1):
                d = self.l11ll1l11ll_Krypto_(l11ll1l11l1_Krypto_, l11ll1ll111_Krypto_)
                key = l11lll1lll_Krypto_.l1l1l1111l_Krypto_(d[l1l1111_Krypto_ (u"ࠨ࡭ࡨࡽࠬ៼")])
                l1l11llll1l_Krypto_ = key.l1lllll_Krypto_((d[l1l1111_Krypto_ (u"ࠩࡦࡸ࠶࠭៽")], d[l1l1111_Krypto_ (u"ࠪࡧࡹ࠸ࠧ៾")]))
                self.assertEqual(l1l11llll1l_Krypto_, d[l1l1111_Krypto_ (u"ࠫࡵࡺࠧ៿")])
    def l11ll1l1111_Krypto_(self):
        for l11ll1l11l1_Krypto_ in self.l11ll1ll11l_Krypto_:
            for l11ll1ll111_Krypto_ in (0,1):
                d = self.l11ll1l11ll_Krypto_(l11ll1l11l1_Krypto_, l11ll1ll111_Krypto_)
                key = l11lll1lll_Krypto_.l1l1l1111l_Krypto_(d[l1l1111_Krypto_ (u"ࠬࡱࡥࡺࠩ᠀")])
                l11ll11llll_Krypto_, l11ll1l111l_Krypto_ = key.l1l11lll11_Krypto_(d[l1l1111_Krypto_ (u"࠭ࡨࠨ᠁")], d[l1l1111_Krypto_ (u"ࠧ࡬ࠩ᠂")])
                self.assertEqual(l11ll11llll_Krypto_, d[l1l1111_Krypto_ (u"ࠨࡵ࡬࡫࠶࠭᠃")])
                self.assertEqual(l11ll1l111l_Krypto_, d[l1l1111_Krypto_ (u"ࠩࡶ࡭࡬࠸ࠧ᠄")])
    def l11ll11l1l1_Krypto_(self):
        for l11ll1l11l1_Krypto_ in self.l11ll1ll11l_Krypto_:
            for l11ll1ll111_Krypto_ in (0,1):
                d = self.l11ll1l11ll_Krypto_(l11ll1l11l1_Krypto_, l11ll1ll111_Krypto_)
                key = l11lll1lll_Krypto_.l1l1l1111l_Krypto_(d[l1l1111_Krypto_ (u"ࠪ࡯ࡪࡿࠧ᠅")])
                res = key.l1l11l1l11_Krypto_( d[l1l1111_Krypto_ (u"ࠫ࡭࠭᠆")], (d[l1l1111_Krypto_ (u"ࠬࡹࡩࡨ࠳ࠪ᠇")],d[l1l1111_Krypto_ (u"࠭ࡳࡪࡩ࠵ࠫ᠈")]) )
                self.assertTrue(res)
                res = key.l1l11l1l11_Krypto_( d[l1l1111_Krypto_ (u"ࠧࡩࠩ᠉")], (d[l1l1111_Krypto_ (u"ࠨࡵ࡬࡫࠶࠭᠊")]+1,d[l1l1111_Krypto_ (u"ࠩࡶ࡭࡬࠸ࠧ᠋")]) )
                self.assertFalse(res)
    def l11ll1l11ll_Krypto_(self, l11ll1l11l1_Krypto_, l11ll1ll111_Krypto_=0):
        l1l1111_Krypto_ (u"ࠥࠦࠧࡉ࡯࡯ࡸࡨࡶࡹࠦࡡࠡࡶࡨࡷࡹࠦࡶࡦࡥࡷࡳࡷࠦࡦࡳࡱࡰࠤࡹ࡫ࡸࡵࡷࡤࡰࠥ࡬࡯ࡳ࡯ࠣࠬ࡭࡫ࡸࡢࡦࡨࡧ࡮ࡳࡡ࡭ࠢࡤࡷࡨ࡯ࡩࠋࠢࠣࠤࠥࠦࠠࠡࠢࡷࡳࠥ࡫ࡩࡵࡪࡨࡶࠥ࡯࡮ࡵࡧࡪࡩࡷࡹࠠࡰࡴࠣࡦࡾࡺࡥࠡࡵࡷࡶ࡮ࡴࡧࡴ࠰ࠥࠦࠧ᠌")
        l11ll1ll1ll_Krypto_ = l1l1111_Krypto_ (u"ࠫࡵ࠭᠍"),l1l1111_Krypto_ (u"ࠬ࡭ࠧ᠎"),l1l1111_Krypto_ (u"࠭ࡹࠨ᠏"),l1l1111_Krypto_ (u"ࠧࡹࠩ᠐")
        l11ll1lllll_Krypto_ = {}
        for c in list(l11ll1l11l1_Krypto_.keys()):
            l11ll1lllll_Krypto_[c] = a2b_hex(l11ll1l11l1_Krypto_[c])
            if l11ll1ll111_Krypto_ or c in l11ll1ll1ll_Krypto_ or c in (l1l1111_Krypto_ (u"ࠨࡵ࡬࡫࠶࠭᠑"),l1l1111_Krypto_ (u"ࠩࡶ࡭࡬࠸ࠧ᠒")):
                l11ll1lllll_Krypto_[c] = l1ll111ll1_Krypto_(l11ll1lllll_Krypto_[c])
        l11ll1lllll_Krypto_[l1l1111_Krypto_ (u"ࠪ࡯ࡪࡿࠧ᠓")]=[]
        for c in l11ll1ll1ll_Krypto_:
            l11ll1lllll_Krypto_[l1l1111_Krypto_ (u"ࠫࡰ࡫ࡹࠨ᠔")] += [l11ll1lllll_Krypto_[c]]
            del l11ll1lllll_Krypto_[c]
        return l11ll1lllll_Krypto_
    def _11ll1lll1l_Krypto_(self, bits):
        l11ll1ll1l1_Krypto_ = l11lll1lll_Krypto_.l1llllll1_Krypto_(bits, l1ll1l11l1_Krypto_.new().read)
        self._11lll11111_Krypto_(l11ll1ll1l1_Krypto_)
        self._11ll1llll1_Krypto_(l11ll1ll1l1_Krypto_)
        l11lll111ll_Krypto_ = l11ll1ll1l1_Krypto_.l1l11l111l_Krypto_()
        self._11lll1lll1_Krypto_(l11lll111ll_Krypto_)
        self._11ll1l1lll_Krypto_(l11ll1ll1l1_Krypto_)
    def _11lll11111_Krypto_(self, l11ll1ll1l1_Krypto_):
        self.assertTrue(l11ll1ll1l1_Krypto_.l1l1111l1l_Krypto_())
        self.assertTrue(l11ll1ll1l1_Krypto_.l1l11ll1l1_Krypto_())
        self.assertTrue(l11ll1ll1l1_Krypto_.l1l1111l11_Krypto_())
        self.assertTrue(1<l11ll1ll1l1_Krypto_.g<(l11ll1ll1l1_Krypto_.p-1))
        self.assertEqual(pow(l11ll1ll1l1_Krypto_.g, l11ll1ll1l1_Krypto_.p-1, l11ll1ll1l1_Krypto_.p), 1)
        self.assertTrue(1<l11ll1ll1l1_Krypto_.x<(l11ll1ll1l1_Krypto_.p-1))
        self.assertEqual(pow(l11ll1ll1l1_Krypto_.g, l11ll1ll1l1_Krypto_.x, l11ll1ll1l1_Krypto_.p), l11ll1ll1l1_Krypto_.y)
    def _11lll1lll1_Krypto_(self, l11ll1ll1l1_Krypto_):
        self.assertFalse(l11ll1ll1l1_Krypto_.l1l1111l1l_Krypto_())
        self.assertTrue(l11ll1ll1l1_Krypto_.l1l11ll1l1_Krypto_())
        self.assertTrue(l11ll1ll1l1_Krypto_.l1l1111l11_Krypto_())
        self.assertTrue(1<l11ll1ll1l1_Krypto_.g<(l11ll1ll1l1_Krypto_.p-1))
        self.assertEqual(pow(l11ll1ll1l1_Krypto_.g, l11ll1ll1l1_Krypto_.p-1, l11ll1ll1l1_Krypto_.p), 1)
    def _11ll1llll1_Krypto_(self, l11ll1ll1l1_Krypto_):
        l1ll11l1_Krypto_ = b(l1l1111_Krypto_ (u"࡚ࠧࡥࡴࡶࠥ᠕"))
        l1ll111l_Krypto_ = l11ll1ll1l1_Krypto_.l1_Krypto_(l1ll11l1_Krypto_, 123456789)
        l11ll1lll11_Krypto_ = l11ll1ll1l1_Krypto_.l1lllll_Krypto_(l1ll111l_Krypto_)
        self.assertEqual(l1ll11l1_Krypto_, l11ll1lll11_Krypto_)
        signature = l11ll1ll1l1_Krypto_.l1l11lll11_Krypto_(l1ll11l1_Krypto_, 987654321)
        l11ll1ll1l1_Krypto_.l1l11l1l11_Krypto_(l1ll11l1_Krypto_, signature)
    def _11ll1l1lll_Krypto_(self, l11ll1ll1l1_Krypto_):
        l1ll11l1_Krypto_ = b(l1l1111_Krypto_ (u"ࠨࡔࡦࡵࡷࠦ᠖"))
        l1ll111l_Krypto_ = l11ll1ll1l1_Krypto_.l1_Krypto_(l1ll11l1_Krypto_, 123456789)
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    tests = []
    tests += l1lll1111l1_Krypto_(l11ll1l1ll1_Krypto_)
    return tests
if __name__ == l1l1111_Krypto_ (u"ࠧࡠࡡࡰࡥ࡮ࡴ࡟ࡠࠩ᠗"):
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧ᠘"))