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
l1l1111_Krypto_ (u"ࠦࠧࠨࡓࡦ࡮ࡩ࠱ࡹ࡫ࡳࡵࠢࡶࡹ࡮ࡺࡥࠡࡨࡲࡶࠥࡉࡲࡺࡲࡷࡳ࠳ࡉࡩࡱࡪࡨࡶ࠳ࡊࡅࡔࠤࠥࠦፒ")
__revision__ = l1l1111_Krypto_ (u"ࠧࠪࡉࡥࠦࠥፓ")
from .common import dict
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
import unittest as l1lll111111_Krypto_
l1l1l1lll1l_Krypto_ = l1l1111_Krypto_ (u"࠭࠰࠲ࠩፔ") * 8
l1l1l1llll1_Krypto_ = l1l1111_Krypto_ (u"ࠧ࠱࠲ࠪፕ") * 8
l1ll11lllll_Krypto_ = [
    (l1l1111_Krypto_ (u"ࠨ࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳ࠫፖ"), l1l1111_Krypto_ (u"ࠩ࠻࠶ࡩࡩࡢࡢࡨࡥࡨࡪࡧࡢ࠷࠸࠳࠶ࠬፗ"), l1l1111_Krypto_ (u"ࠪ࠵࠵࠹࠱࠷ࡧ࠳࠶࠽ࡩ࠸ࡧ࠵ࡥ࠸ࡦ࠭ፘ"),
        l1l1111_Krypto_ (u"ࠦࡓࡏࡓࡕࠢࡖࡔ࠽࠶࠰࠮࠳࠺ࠤࡆࠨፙ")),
    (l1l1111_Krypto_ (u"ࠬ࠾࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰ࠨፚ"), l1l1111_Krypto_ (u"࠭࠹࠶ࡨ࠻ࡥ࠺࡫࠵ࡥࡦ࠶࠵ࡩ࠿࠰࠱ࠩ፛"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠧࡏࡋࡖࡘ࡙ࠥࡐ࠹࠲࠳࠱࠶࠽ࠠࡃ࠰࠴ࠤࠏࠦࠠࠡࠢࠫࠫ፜")4000000000000000unScramble_opy_ (u"ࠨ࠮ࠣࠫ፝")l1l1lll111l_Krypto_ (u"ࠩ࠯ࠤࡘࡖ࠸࠱࠲ࡢ࠵࠼ࡥࡂ࠲ࡡࡎࡉ࡞࠲ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠩ፞")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"ࠪ࠶࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠭፟"), l1l1111_Krypto_ (u"ࠫ࠷࡫࠸࠷࠷࠶࠵࠵࠺ࡦ࠴࠺࠶࠸ࡪࡧࠧ፠"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠬࡔࡉࡔࡖࠣࡗࡕ࠾࠰࠱࠯࠴࠻ࠥࡈ࠮࠲ࠢࠍࠤࠥࠦࠠࠩࠩ፡")1000000000000000unScramble_opy_ (u"࠭ࠬࠡࠩ።")4bd388ff6cd81d4funScramble_opy_ (u"ࠧ࠭ࠢࡖࡔ࠽࠶࠰ࡠ࠳࠺ࡣࡇ࠷࡟ࡌࡇ࡜࠰ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠧ፣")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"ࠨ࠲࠻࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳ࠫ፤"), l1l1111_Krypto_ (u"ࠩ࠵࠴ࡧ࠿ࡥ࠸࠸࠺ࡦ࠷࡬ࡢ࠲࠶࠸࠺ࠬ፥"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠪࡒࡎ࡙ࡔࠡࡕࡓ࠼࠵࠶࠭࠲࠹ࠣࡆ࠳࠷ࠠࠋࠢࠣࠤࠥ࠮ࠧ፦")0400000000000000unScramble_opy_ (u"ࠫ࠱ࠦࠧ፧")55579380d77138efunScramble_opy_ (u"ࠬ࠲ࠠࡔࡒ࠻࠴࠵ࡥ࠱࠸ࡡࡅ࠵ࡤࡑࡅ࡚࠮ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠬ፨")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"࠭࠰࠳࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱ࠩ፩"), l1l1111_Krypto_ (u"ࠧ࠷ࡥࡦ࠹ࡩ࡫ࡦࡢࡣࡩ࠴࠹࠻࠱࠳ࡨࠪ፪"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠨࡐࡌࡗ࡙ࠦࡓࡑ࠺࠳࠴࠲࠷࠷ࠡࡄ࠱࠵ࠥࠐࠠࠡࠢࠣࠬࠬ፫")0100000000000000unScramble_opy_ (u"ࠩ࠯ࠤࠬ፬")0d9f279ba5d87260unScramble_opy_ (u"ࠪ࠰࡙ࠥࡐ࠹࠲࠳ࡣ࠶࠽࡟ࡃ࠳ࡢࡏࡊ࡟ࠬࠋࠢࠣࠤࠥࠦࠠࠡࠢࠪ፭")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"ࠫ࠵࠶࠸࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶ࠧ፮"), l1l1111_Krypto_ (u"ࠬࡪ࠹࠱࠵࠴ࡦ࠵࠸࠷࠲ࡤࡧ࠹ࡦ࠶ࡡࠨ፯"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"࠭ࡎࡊࡕࡗࠤࡘࡖ࠸࠱࠲࠰࠵࠼ࠦࡂ࠯࠳ࠣࠎࠥࠦࠠࠡࠪࠪ፰")0040000000000000unScramble_opy_ (u"ࠧ࠭ࠢࠪ፱")424250b37c3dd951unScramble_opy_ (u"ࠨ࠮ࠣࡗࡕ࠾࠰࠱ࡡ࠴࠻ࡤࡈ࠱ࡠࡍࡈ࡝࠱ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠨ፲")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"ࠩ࠳࠴࠷࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴ࠬ፳"), l1l1111_Krypto_ (u"ࠪࡦ࠽࠶࠶࠲ࡤ࠺ࡩࡨࡪ࠹ࡢ࠴࠴ࡩ࠺࠭፴"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠫࡓࡏࡓࡕࠢࡖࡔ࠽࠶࠰࠮࠳࠺ࠤࡇ࠴࠱ࠡࠌࠣࠤࠥࠦࠨࠨ፵")0010000000000000unScramble_opy_ (u"ࠬ࠲ࠠࠨ፶")l1l1ll111l1_Krypto_ (u"࠭ࠬࠡࡕࡓ࠼࠵࠶࡟࠲࠹ࡢࡆ࠶ࡥࡋࡆ࡛࠯ࠎࠥࠦࠠࠡࠢࠣࠤࠥ࠭፷")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"ࠧ࠱࠲࠳࠼࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲ࠪ፸"), l1l1111_Krypto_ (u"ࠨࡣࡧࡨ࠵ࡩࡣ࠹ࡦ࠹ࡩ࠺ࡪࡥࡣࡣ࠴ࠫ፹"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠩࡑࡍࡘ࡚ࠠࡔࡒ࠻࠴࠵࠳࠱࠸ࠢࡅ࠲࠶ࠦࠊࠡࠢࠣࠤ࠭࠭፺")0004000000000000unScramble_opy_ (u"ࠪ࠰ࠥ࠭፻")l1l1ll11l11_Krypto_ (u"ࠫ࠱ࠦࡓࡑ࠺࠳࠴ࡤ࠷࠷ࡠࡄ࠴ࡣࡐࡋ࡙࠭ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠫ፼")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"ࠬ࠶࠰࠱࠴࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰ࠨ፽"), l1l1111_Krypto_ (u"࠭ࡥࡤࡤࡩࡩ࠸ࡨࡤ࠴ࡨ࠸࠽࠶ࡧ࠵ࡦࠩ፾"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠧࡏࡋࡖࡘ࡙ࠥࡐ࠹࠲࠳࠱࠶࠽ࠠࡃ࠰࠴ࠤࠏࠦࠠࠡࠢࠫࠫ፿")0001000000000000unScramble_opy_ (u"ࠨ࠮ࠣࠫᎀ")l1l1l1l1l11_Krypto_ (u"ࠩ࠯ࠤࡘࡖ࠸࠱࠲ࡢ࠵࠼ࡥࡂ࠲ࡡࡎࡉ࡞࠲ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠩᎁ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"ࠪ࠴࠵࠶࠰࠹࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠭ᎂ"), l1l1111_Krypto_ (u"ࠫ࠷ࡨ࠹ࡧ࠻࠻࠶࡫࠸࠰࠱࠵࠺ࡪࡦ࠿ࠧᎃ"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠬࡔࡉࡔࡖࠣࡗࡕ࠾࠰࠱࠯࠴࠻ࠥࡈ࠮࠲ࠢࠍࠤࠥࠦࠠࠩࠩᎄ")0000400000000000unScramble_opy_ (u"࠭ࠬࠡࠩᎅ")889de068a16f0be6unScramble_opy_ (u"ࠧ࠭ࠢࡖࡔ࠽࠶࠰ࡠ࠳࠺ࡣࡇ࠷࡟ࡌࡇ࡜࠰ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠧᎆ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"ࠨ࠲࠳࠴࠵࠸࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳ࠫᎇ"), l1l1111_Krypto_ (u"ࠩࡨ࠵࠾࡫࠲࠸࠷ࡧ࠼࠹࠼ࡡ࠲࠴࠼࠼ࠬᎈ"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠪࡒࡎ࡙ࡔࠡࡕࡓ࠼࠵࠶࠭࠲࠹ࠣࡆ࠳࠷ࠠࠋࠢࠣࠤࠥ࠮ࠧᎉ")0000100000000000unScramble_opy_ (u"ࠫ࠱ࠦࠧᎊ")329a8ed523d71aecunScramble_opy_ (u"ࠬ࠲ࠠࡔࡒ࠻࠴࠵ࡥ࠱࠸ࡡࡅ࠵ࡤࡑࡅ࡚࠮ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠬᎋ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"࠭࠰࠱࠲࠳࠴࠽࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱ࠩᎌ"), l1l1111_Krypto_ (u"ࠧࡦ࠹ࡩࡧࡪ࠸࠲࠶࠷࠺ࡨ࠷࠹ࡣ࠺࠹ࠪᎍ"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠨࡐࡌࡗ࡙ࠦࡓࡑ࠺࠳࠴࠲࠷࠷ࠡࡄ࠱࠵ࠥࠐࠠࠡࠢࠣࠬࠬᎎ")0000040000000000unScramble_opy_ (u"ࠩ࠯ࠤࠬᎏ")12a9f5817ff2d65dunScramble_opy_ (u"ࠪ࠰࡙ࠥࡐ࠹࠲࠳ࡣ࠶࠽࡟ࡃ࠳ࡢࡏࡊ࡟ࠬࠋࠢࠣࠤࠥࠦࠠࠡࠢࠪ᎐")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"ࠫ࠵࠶࠰࠱࠲࠵࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶ࠧ᎑"), l1l1111_Krypto_ (u"ࠬࡧ࠴࠹࠶ࡦ࠷ࡦࡪ࠳࠹ࡦࡦ࠽ࡨ࠷࠹ࠨ᎒"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"࠭ࡎࡊࡕࡗࠤࡘࡖ࠸࠱࠲࠰࠵࠼ࠦࡂ࠯࠳ࠣࠎࠥࠦࠠࠡࠪࠪ᎓")0000010000000000unScramble_opy_ (u"ࠧ࠭ࠢࠪ᎔")l1l1l1l11ll_Krypto_ (u"ࠨ࠮ࠣࡗࡕ࠾࠰࠱ࡡ࠴࠻ࡤࡈ࠱ࡠࡍࡈ࡝࠱ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠨ᎕")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"ࠩ࠳࠴࠵࠶࠰࠱࠺࠳࠴࠵࠶࠰࠱࠲࠳࠴ࠬ᎖"), l1l1111_Krypto_ (u"ࠪ࠻࠺࠶ࡤ࠱࠹࠼࠸࠵࠽࠵࠳࠳࠶࠺࠸࠭᎗"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠫࡓࡏࡓࡕࠢࡖࡔ࠽࠶࠰࠮࠳࠺ࠤࡇ࠴࠱ࠡࠌࠣࠤࠥࠦࠨࠨ᎘")0000004000000000unScramble_opy_ (u"ࠬ࠲ࠠࠨ᎙")64feed9c724c2fafunScramble_opy_ (u"࠭ࠬࠡࡕࡓ࠼࠵࠶࡟࠲࠹ࡢࡆ࠶ࡥࡋࡆ࡛࠯ࠎࠥࠦࠠࠡࠢࠣࠤࠥ࠭᎚")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"ࠧ࠱࠲࠳࠴࠵࠶࠲࠱࠲࠳࠴࠵࠶࠰࠱࠲ࠪ᎛"), l1l1111_Krypto_ (u"ࠨࡨ࠳࠶ࡧ࠸࠶࠴ࡤ࠶࠶࠽࡫࠲ࡣ࠸࠳ࠫ᎜"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠩࡑࡍࡘ࡚ࠠࡔࡒ࠻࠴࠵࠳࠱࠸ࠢࡅ࠲࠶ࠦࠊࠡࠢࠣࠤ࠭࠭᎝")0000001000000000unScramble_opy_ (u"ࠪ࠰ࠥ࠭᎞")9d64555a9a10b852unScramble_opy_ (u"ࠫ࠱ࠦࡓࡑ࠺࠳࠴ࡤ࠷࠷ࡠࡄ࠴ࡣࡐࡋ࡙࠭ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠫ᎟")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"ࠬ࠶࠰࠱࠲࠳࠴࠵࠾࠰࠱࠲࠳࠴࠵࠶࠰ࠨᎠ"), l1l1111_Krypto_ (u"࠭ࡤ࠲࠲࠹ࡪ࡫࠶ࡢࡦࡦ࠸࠶࠺࠻ࡤ࠸ࠩᎡ"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠧࡏࡋࡖࡘ࡙ࠥࡐ࠹࠲࠳࠱࠶࠽ࠠࡃ࠰࠴ࠤࠏࠦࠠࠡࠢࠫࠫᎢ")0000000400000000unScramble_opy_ (u"ࠨ࠮ࠣࠫᎣ")l1l1l1ll1l1_Krypto_ (u"ࠩ࠯ࠤࡘࡖ࠸࠱࠲ࡢ࠵࠼ࡥࡂ࠲ࡡࡎࡉ࡞࠲ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠩᎤ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"ࠪ࠴࠵࠶࠰࠱࠲࠳࠶࠵࠶࠰࠱࠲࠳࠴࠵࠭Ꭵ"), l1l1111_Krypto_ (u"ࠫࡪ࠺࠲࠹࠷࠻࠵࠶࠾࠶ࡦࡥ࠻ࡪ࠹࠼ࠧᎦ"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠬࡔࡉࡔࡖࠣࡗࡕ࠾࠰࠱࠯࠴࠻ࠥࡈ࠮࠲ࠢࠍࠤࠥࠦࠠࠩࠩᎧ")0000000100000000unScramble_opy_ (u"࠭ࠬࠡࠩᎨ")l1l1lll1111_Krypto_ (u"ࠧ࠭ࠢࡖࡔ࠽࠶࠰ࡠ࠳࠺ࡣࡇ࠷࡟ࡌࡇ࡜࠰ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠧᎩ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"ࠨ࠲࠳࠴࠵࠶࠰࠱࠲࠻࠴࠵࠶࠰࠱࠲࠳ࠫᎪ"), l1l1111_Krypto_ (u"ࠩࡨ࠽࠹࠹ࡤ࠸࠷࠹࠼ࡦ࡫ࡣ࠱ࡥ࠸ࡧࠬᎫ"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠪࡒࡎ࡙ࡔࠡࡕࡓ࠼࠵࠶࠭࠲࠹ࠣࡆ࠳࠷ࠠࠋࠢࠣࠤࠥ࠮ࠧᎬ")0000000040000000unScramble_opy_ (u"ࠫ࠱ࠦࠧᎭ")l1l1ll1l1l1_Krypto_ (u"ࡧ࠭ࠬࠡࡕࡓ࠼࠵࠶࡟࠲࠹ࡢࡆ࠶ࡥࡋࡆ࡛࠯ࠎࠥࠦࠠࠡࠢࠣࠤࠥ࠭Ꭾ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"࠭࠰࠱࠲࠳࠴࠵࠶࠰࠳࠲࠳࠴࠵࠶࠰࠱ࠩᎯ"), l1l1111_Krypto_ (u"ࠧࡣ࠳࠹࠴ࡪ࠺࠶࠹࠲ࡩ࠺ࡨ࠼࠹࠷ࡨࠪᎰ"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠨࡐࡌࡗ࡙ࠦࡓࡑ࠺࠳࠴࠲࠷࠷ࠡࡄ࠱࠵ࠥࠐࠠࠡࠢࠣࠬࠬᎱ")0000000010000000unScramble_opy_ (u"ࠩ࠯ࠤࠬᎲ")l1l1l1l1l1l_Krypto_ (u"ࠪ࠰࡙ࠥࡐ࠹࠲࠳ࡣ࠶࠽࡟ࡃ࠳ࡢࡏࡊ࡟ࠬࠋࠢࠣࠤࠥࠦࠠࠡࠢࠪᎳ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"ࠫ࠵࠶࠰࠱࠲࠳࠴࠵࠶࠸࠱࠲࠳࠴࠵࠶ࠧᎴ"), l1l1111_Krypto_ (u"ࠬࡩࡡ࠴ࡣ࠵ࡦ࠵࠹࠶ࡥࡤࡦ࠼࠺࠶࠲ࠨᎵ"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"࠭ࡎࡊࡕࡗࠤࡘࡖ࠸࠱࠲࠰࠵࠼ࠦࡂ࠯࠳ࠣࠎࠥࠦࠠࠡࠪࠪᎶ")0000000004000000unScramble_opy_ (u"ࠧ࠭ࠢࠪᎷ")5e0905517bb59bcfunScramble_opy_ (u"ࠨ࠮ࠣࡗࡕ࠾࠰࠱ࡡ࠴࠻ࡤࡈ࠱ࡠࡍࡈ࡝࠱ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠨᎸ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"ࠩ࠳࠴࠵࠶࠰࠱࠲࠳࠴࠷࠶࠰࠱࠲࠳࠴ࠬᎹ"), l1l1111_Krypto_ (u"ࠪ࠼࠶࠺ࡥࡦࡤ࠶ࡦ࠾࠷ࡤ࠺࠲࠺࠶࠻࠭Ꮊ"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠫࡓࡏࡓࡕࠢࡖࡔ࠽࠶࠰࠮࠳࠺ࠤࡇ࠴࠱ࠡࠌࠣࠤࠥࠦࠨࠨᎻ")0000000001000000unScramble_opy_ (u"ࠬ࠲ࠠࠨᎼ")4d49db1532919c9funScramble_opy_ (u"࠭ࠬࠡࡕࡓ࠼࠵࠶࡟࠲࠹ࡢࡆ࠶ࡥࡋࡆ࡛࠯ࠎࠥࠦࠠࠡࠢࠣࠤࠥ࠭Ꮍ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"ࠧ࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠼࠵࠶࠰࠱࠲ࠪᎾ"), l1l1111_Krypto_ (u"ࠨ࠴࠸ࡩࡧ࠻ࡦࡤ࠵ࡩ࠼ࡨ࡬࠰࠷࠴࠴ࠫᎿ"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠩࡑࡍࡘ࡚ࠠࡔࡒ࠻࠴࠵࠳࠱࠸ࠢࡅ࠲࠶ࠦࠊࠡࠢࠣࠤ࠭࠭Ꮐ")0000000000400000unScramble_opy_ (u"ࠪ࠰ࠥ࠭Ꮑ")l1l1l1ll11l_Krypto_ (u"ࠫ࠱ࠦࡓࡑ࠺࠳࠴ࡤ࠷࠷ࡠࡄ࠴ࡣࡐࡋ࡙࠭ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠫᏂ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"ࠬ࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱࠴࠳࠴࠵࠶࠰ࠨᏃ"), l1l1111_Krypto_ (u"࠭࠷࠺ࡧ࠼࠴ࡩࡨࡣ࠺࠺ࡩ࠽࠷ࡩࡣࡢࠩᏄ"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠧࡏࡋࡖࡘ࡙ࠥࡐ࠹࠲࠳࠱࠶࠽ࠠࡃ࠰࠴ࠤࠏࠦࠠࠡࠢࠫࠫᏅ")0000000000100000unScramble_opy_ (u"ࠨ࠮ࠣࠫᏆ")866ecedd8072bb0eunScramble_opy_ (u"ࠩ࠯ࠤࡘࡖ࠸࠱࠲ࡢ࠵࠼ࡥࡂ࠲ࡡࡎࡉ࡞࠲ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠩᏇ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"ࠪ࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰࠹࠲࠳࠴࠵࠭Ꮘ"), l1l1111_Krypto_ (u"ࠫ࠽ࡨ࠵࠵࠷࠶࠺࡫࠸ࡦ࠴ࡧ࠹࠸ࡦ࠾ࠧᏉ"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠬࡔࡉࡔࡖࠣࡗࡕ࠾࠰࠱࠯࠴࠻ࠥࡈ࠮࠲ࠢࠍࠤࠥࠦࠠࠩࠩᏊ")0000000000040000unScramble_opy_ (u"࠭ࠬࠡࠩᏋ")l1l1l1ll1ll_Krypto_ (u"ࡢࠨ࠮ࠣࡗࡕ࠾࠰࠱ࡡ࠴࠻ࡤࡈ࠱ࡠࡍࡈ࡝࠱ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠨᏌ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"ࠨ࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠸࠰࠱࠲࠳ࠫᏍ"), l1l1111_Krypto_ (u"ࠩࡦࡥ࡫࡬ࡣ࠷ࡣࡦ࠸࠺࠺࠲ࡥࡧ࠶࠵ࠬᏎ"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠪࡒࡎ࡙ࡔࠡࡕࡓ࠼࠵࠶࠭࠲࠹ࠣࡆ࠳࠷ࠠࠋࠢࠣࠤࠥ࠮ࠧᏏ")0000000000010000unScramble_opy_ (u"ࠫ࠱ࠦࠧᏐ")8dd45a2ddf90796cunScramble_opy_ (u"ࠬ࠲ࠠࡔࡒ࠻࠴࠵ࡥ࠱࠸ࡡࡅ࠵ࡤࡑࡅ࡚࠮ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠬᏑ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"࠭࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠽࠶࠰࠱ࠩᏒ"), l1l1111_Krypto_ (u"ࠧ࠲࠲࠵࠽ࡩ࠻࠵ࡦ࠺࠻࠴ࡪࡩ࠲ࡥ࠲ࠪᏓ"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠨࡐࡌࡗ࡙ࠦࡓࡑ࠺࠳࠴࠲࠷࠷ࠡࡄ࠱࠵ࠥࠐࠠࠡࠢࠣࠬࠬᏔ")0000000000004000unScramble_opy_ (u"ࠩ࠯ࠤࠬᏕ")5d86cb23639dbea9unScramble_opy_ (u"ࠪ࠰࡙ࠥࡐ࠹࠲࠳ࡣ࠶࠽࡟ࡃ࠳ࡢࡏࡊ࡟ࠬࠋࠢࠣࠤࠥࠦࠠࠡࠢࠪᏖ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"ࠫ࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠵࠴࠵࠶ࠧᏗ"), l1l1111_Krypto_ (u"ࠬ࠷ࡤ࠲ࡥࡤ࠼࠺࠹ࡡࡦ࠹ࡦ࠴ࡨ࠻ࡦࠨᏘ"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"࠭ࡎࡊࡕࡗࠤࡘࡖ࠸࠱࠲࠰࠵࠼ࠦࡂ࠯࠳ࠣࠎࠥࠦࠠࠡࠪࠪᏙ")0000000000001000unScramble_opy_ (u"ࠧ࠭ࠢࠪᏚ")l1l1ll1l111_Krypto_ (u"ࠨ࠮ࠣࡗࡕ࠾࠰࠱ࡡ࠴࠻ࡤࡈ࠱ࡠࡍࡈ࡝࠱ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠨᏛ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"ࠩ࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱࠺࠳࠴ࠬᏜ"), l1l1111_Krypto_ (u"ࠪ࠼࠹࠶࠵ࡥ࠳ࡤࡦࡪ࠸࠴ࡧࡤ࠼࠸࠷࠭Ꮭ"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠫࡓࡏࡓࡕࠢࡖࡔ࠽࠶࠰࠮࠳࠺ࠤࡇ࠴࠱ࠡࠌࠣࠤࠥࠦࠨࠨᏞ")0000000000000400unScramble_opy_ (u"ࠬ࠲ࠠࠨᏟ")l1l1ll11l1l_Krypto_ (u"࠭ࠬࠡࡕࡓ࠼࠵࠶࡟࠲࠹ࡢࡆ࠶ࡥࡋࡆ࡛࠯ࠎࠥࠦࠠࠡࠢࠣࠤࠥ࠭Ꮰ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"ࠧ࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶࠲࠱࠲ࠪᏡ"), l1l1111_Krypto_ (u"ࠨ࠶࠻࠶࠷࠷ࡢ࠺࠻࠶࠻࠼࠺࠸ࡢ࠴࠶ࠫᏢ"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠩࡑࡍࡘ࡚ࠠࡔࡒ࠻࠴࠵࠳࠱࠸ࠢࡅ࠲࠶ࠦࠊࠡࠢࠣࠤ࠭࠭Ꮳ")0000000000000100unScramble_opy_ (u"ࠪ࠰ࠥ࠭Ꮴ")l1l1l1lll11_Krypto_ (u"ࠫ࠱ࠦࡓࡑ࠺࠳࠴ࡤ࠷࠷ࡠࡄ࠴ࡣࡐࡋ࡙࠭ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠫᏥ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"ࠬ࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠾࠰ࠨᏦ"), l1l1111_Krypto_ (u"࠭࠲ࡧࡤࡦ࠶࠾࠷ࡡ࠶࠹࠳ࡨࡧ࠻ࡣ࠵ࠩᏧ"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠧࡏࡋࡖࡘ࡙ࠥࡐ࠹࠲࠳࠱࠶࠽ࠠࡃ࠰࠴ࠤࠏࠦࠠࠡࠢࠫࠫᏨ")0000000000000040unScramble_opy_ (u"ࠨ࠮ࠣࠫᏩ")l1l1ll11lll_Krypto_ (u"ࠩ࠯ࠤࡘࡖ࠸࠱࠲ࡢ࠵࠼ࡥࡂ࠲ࡡࡎࡉ࡞࠲ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠩᏪ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"ࠪ࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠶࠵࠭Ꮻ"), l1l1111_Krypto_ (u"ࠫ࠵࠿࠵࠴ࡧ࠵࠶࠺࠾ࡥ࠹ࡧ࠼࠴ࡦ࠷ࠧᏬ"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠬࡔࡉࡔࡖࠣࡗࡕ࠾࠰࠱࠯࠴࠻ࠥࡈ࠮࠲ࠢࠍࠤࠥࠦࠠࠩࠩᏭ")0000000000000010unScramble_opy_ (u"࠭ࠬࠡࠩᏮ")5b711bc4ceebf2eeunScramble_opy_ (u"ࠧ࠭ࠢࡖࡔ࠽࠶࠰ࡠ࠳࠺ࡣࡇ࠷࡟ࡌࡇ࡜࠰ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠧᏯ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"ࠨ࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠻ࠫᏰ"), l1l1111_Krypto_ (u"ࠩࡦࡧ࠵࠾࠳ࡧ࠳ࡨ࠺ࡩ࠿ࡥ࠹࠷ࡩ࠺ࠬᏱ"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠪࡒࡎ࡙ࡔࠡࡕࡓ࠼࠵࠶࠭࠲࠹ࠣࡆ࠳࠷ࠠࠋࠢࠣࠤࠥ࠮ࠧᏲ")0000000000000004unScramble_opy_ (u"ࠫ࠱ࠦࠧᏳ")l1l1l1l1ll1_Krypto_ (u"ࠬ࠲ࠠࡔࡒ࠻࠴࠵ࡥ࠱࠸ࡡࡅ࠵ࡤࡑࡅ࡚࠮ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠬᏴ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1111_Krypto_ (u"࠭࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰࠳ࠩᏵ"), l1l1111_Krypto_ (u"ࠧ࠱࠸ࡨ࠻ࡪࡧ࠲࠳ࡥࡨ࠽࠷࠽࠰࠹ࡨࠪ᏶"), l1l1l1lll1l_Krypto_,
        l1l1111_Krypto_ (u"ࠨࡐࡌࡗ࡙ࠦࡓࡑ࠺࠳࠴࠲࠷࠷ࠡࡄ࠱࠵ࠥࠐࠠࠡࠢࠣࠬࠬ᏷")0000000000000001unScramble_opy_ (u"ࠩ࠯ࠤࠬᏸ")166b40b44aba4bd6unScramble_opy_ (u"ࠪ࠰࡙ࠥࡐ࠹࠲࠳ࡣ࠶࠽࡟ࡃ࠳ࡢࡏࡊ࡟ࠬࠋࠢࠣࠤࠥࠦࠠࠡࠢࠪᏹ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.1
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"ࠫ࠾࠻ࡡ࠹ࡦ࠺࠶࠽࠷࠳ࡥࡣࡤ࠽࠹ࡪࠧᏺ"), l1l1111_Krypto_ (u"ࠬ࠾࠰࠱࠳࠳࠵࠵࠷࠰࠲࠲࠴࠴࠶࠶࠱ࠨᏻ"),
        l1l1111_Krypto_ (u"࠭ࡎࡊࡕࡗࠤࡘࡖ࠸࠱࠲࠰࠵࠼ࠦࡂ࠯࠴ࠣࠎࠥࠦࠠࠡࠪࡖࡔ࠽࠶࠰ࡠ࠳࠺ࡣࡇ࠸࡟ࡑࡖ࠯ࠤࠬᏼ")0eec1487dd8c26d5unScramble_opy_ (u"ࠧ࠭ࠢࠪᏽ")4001010101010101unScramble_opy_ (u"ࠨ࠮ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠬ᏾")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"ࠩ࠺ࡥࡩ࠷࠶ࡧࡨࡥ࠻࠾ࡩ࠴࠶࠻࠵࠺ࠬ᏿"), l1l1111_Krypto_ (u"ࠪ࠶࠵࠶࠱࠱࠳࠳࠵࠵࠷࠰࠲࠲࠴࠴࠶࠭᐀"),
        l1l1111_Krypto_ (u"ࠫࡓࡏࡓࡕࠢࡖࡔ࠽࠶࠰࠮࠳࠺ࠤࡇ࠴࠲ࠡࠌࠣࠤࠥࠦࠨࡔࡒ࠻࠴࠵ࡥ࠱࠸ࡡࡅ࠶ࡤࡖࡔ࠭ࠢࠪᐁ")l1l1ll1l1ll_Krypto_ (u"ࠬ࠲ࠠࠨᐂ")1001010101010101unScramble_opy_ (u"࠭ࠬࠋࠢࠣࠤࠥࠦࠠࠡࠢࠪᐃ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"ࠧ࠹࠲࠼ࡪ࠺࡬࠸࠸࠵ࡦ࠵࡫ࡪ࠷࠷࠳ࠪᐄ"), l1l1111_Krypto_ (u"ࠨ࠲࠻࠴࠶࠶࠱࠱࠳࠳࠵࠵࠷࠰࠲࠲࠴ࠫᐅ"),
        l1l1111_Krypto_ (u"ࠩࡑࡍࡘ࡚ࠠࡔࡒ࠻࠴࠵࠳࠱࠸ࠢࡅ࠲࠷ࠦࠊࠡࠢࠣࠤ࡙࠭ࡐ࠹࠲࠳ࡣ࠶࠽࡟ࡃ࠴ࡢࡔ࡙࠲ࠠࠨᐆ")l1l1ll1lll1_Krypto_ (u"ࠪ࠰ࠥ࠭ᐇ")0401010101010101unScramble_opy_ (u"ࠫ࠱ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠨᐈ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"ࠬ࠺࠶࠲࠷ࡤࡥ࠶ࡪ࠳࠴ࡧ࠺࠶࡫࠷࠰ࠨᐉ"), l1l1111_Krypto_ (u"࠭࠰࠳࠲࠴࠴࠶࠶࠱࠱࠳࠳࠵࠵࠷࠰࠲ࠩᐊ"),
        l1l1111_Krypto_ (u"ࠧࡏࡋࡖࡘ࡙ࠥࡐ࠹࠲࠳࠱࠶࠽ࠠࡃ࠰࠵ࠤࠏࠦࠠࠡࠢࠫࡗࡕ࠾࠰࠱ࡡ࠴࠻ࡤࡈ࠲ࡠࡒࡗ࠰ࠥ࠭ᐋ")2055123350c00858unScramble_opy_ (u"ࠨ࠮ࠣࠫᐌ")0180010101010101unScramble_opy_ (u"ࠩ࠯ࠎࠥࠦࠠࠡࠢࠣࠤࠥ࠭ᐍ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"ࠪࡨ࡫࠹ࡢ࠺࠻ࡧ࠺࠺࠽࠷࠴࠻࠺ࡧ࠽࠭ᐎ"), l1l1111_Krypto_ (u"ࠫ࠵࠷࠴࠱࠲࠴࠴࠶࠶࠱࠱࠳࠳࠵࠵࠷ࠧᐏ"),
        l1l1111_Krypto_ (u"ࠬࡔࡉࡔࡖࠣࡗࡕ࠾࠰࠱࠯࠴࠻ࠥࡈ࠮࠳ࠢࠍࠤࠥࠦࠠࠩࡕࡓ࠼࠵࠶࡟࠲࠹ࡢࡆ࠷ࡥࡐࡕ࠮ࠣࠫᐐ")31fe17369b5288c9unScramble_opy_ (u"࠭ࠬࠡࠩᐑ")0120010101010101unScramble_opy_ (u"ࠧ࠭ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠫᐒ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"ࠨࡦࡩࡨࡩ࠹ࡣࡤ࠸࠷ࡨࡦ࡫࠱࠷࠶࠵ࠫᐓ"), l1l1111_Krypto_ (u"ࠩ࠳࠵࠶࠶࠰࠲࠲࠴࠴࠶࠶࠱࠱࠳࠳࠵ࠬᐔ"),
        l1l1111_Krypto_ (u"ࠪࡒࡎ࡙ࡔࠡࡕࡓ࠼࠵࠶࠭࠲࠹ࠣࡆ࠳࠸ࠠࠋࠢࠣࠤࠥ࠮ࡓࡑ࠺࠳࠴ࡤ࠷࠷ࡠࡄ࠵ࡣࡕ࡚ࠬࠡࠩᐕ")178c83ce2b399d94unScramble_opy_ (u"ࠫ࠱ࠦࠧᐖ")0108010101010101unScramble_opy_ (u"ࠬ࠲ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠩᐗ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"࠭࠵࠱ࡨ࠹࠷࠻࠹࠲࠵ࡣ࠼ࡦ࠼࡬࠸࠱ࠩᐘ"), l1l1111_Krypto_ (u"ࠧ࠱࠳࠳࠸࠵࠷࠰࠲࠲࠴࠴࠶࠶࠱࠱࠳ࠪᐙ"),
        l1l1111_Krypto_ (u"ࠨࡐࡌࡗ࡙ࠦࡓࡑ࠺࠳࠴࠲࠷࠷ࠡࡄ࠱࠶ࠥࠐࠠࠡࠢࠣࠬࡘࡖ࠸࠱࠲ࡢ࠵࠼ࡥࡂ࠳ࡡࡓࡘ࠱ࠦࠧᐚ")l1l1ll1ll1l_Krypto_ (u"ࠩ࠯ࠤࠬᐛ")0102010101010101unScramble_opy_ (u"ࠪ࠰ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠧᐜ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"ࠫࡦ࠸ࡤࡤ࠻ࡨ࠽࠷࡬ࡤ࠴ࡥࡧࡩ࠾࠸ࠧᐝ"), l1l1111_Krypto_ (u"ࠬ࠶࠱࠱࠳࠻࠴࠵࠷࠰࠲࠲࠴࠴࠶࠶࠱ࠨᐞ"),
        l1l1111_Krypto_ (u"࠭ࡎࡊࡕࡗࠤࡘࡖ࠸࠱࠲࠰࠵࠼ࠦࡂ࠯࠴ࠣࠎࠥࠦࠠࠡࠪࡖࡔ࠽࠶࠰ࡠ࠳࠺ࡣࡇ࠸࡟ࡑࡖ࠯ࠤࠬᐟ")l1l1l1lllll_Krypto_ (u"ࠧ࠭ࠢࠪᐠ")0101400101010101unScramble_opy_ (u"ࠨ࠮ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠬᐡ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"ࠩ࠼࠴ࡧࡧ࠶࠹࠲ࡥ࠶࠷ࡧࡥࡣ࠷࠵࠹ࠬᐢ"), l1l1111_Krypto_ (u"ࠪ࠴࠶࠶࠱࠳࠲࠳࠵࠵࠷࠰࠲࠲࠴࠴࠶࠭ᐣ"),
        l1l1111_Krypto_ (u"ࠫࡓࡏࡓࡕࠢࡖࡔ࠽࠶࠰࠮࠳࠺ࠤࡇ࠴࠲ࠡࠌࠣࠤࠥࠦࠨࡔࡒ࠻࠴࠵ࡥ࠱࠸ࡡࡅ࠶ࡤࡖࡔ࠭ࠢࠪᐤ")l1l1l1l11l1_Krypto_ (u"ࠬ࠲ࠠࠨᐥ")0101100101010101unScramble_opy_ (u"࠭ࠬࠋࠢࠣࠤࠥࠦࠠࠡࠢࠪᐦ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"ࠧ࠹࠺࠵ࡦ࡫࡬࠰ࡢࡣ࠳࠵ࡦ࠶ࡢ࠹࠹ࠪᐧ"), l1l1111_Krypto_ (u"ࠨ࠲࠴࠴࠶࠶࠸࠱࠳࠳࠵࠵࠷࠰࠲࠲࠴ࠫᐨ"),
        l1l1111_Krypto_ (u"ࠩࡑࡍࡘ࡚ࠠࡔࡒ࠻࠴࠵࠳࠱࠸ࠢࡅ࠲࠷ࠦࠊࠡࠢࠣࠤ࡙࠭ࡐ࠹࠲࠳ࡣ࠶࠽࡟ࡃ࠴ࡢࡔ࡙࠲ࠠࠨᐩ")25610288924511c2unScramble_opy_ (u"ࠪ࠰ࠥ࠭ᐪ")0101040101010101unScramble_opy_ (u"ࠫ࠱ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠨᐫ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"ࠬࡩ࠷࠲࠷࠴࠺ࡨ࠸࠹ࡤ࠹࠸ࡨ࠶࠽࠰ࠨᐬ"), l1l1111_Krypto_ (u"࠭࠰࠲࠲࠴࠴࠷࠶࠱࠱࠳࠳࠵࠵࠷࠰࠲ࠩᐭ"),
        l1l1111_Krypto_ (u"ࠧࡏࡋࡖࡘ࡙ࠥࡐ࠹࠲࠳࠱࠶࠽ࠠࡃ࠰࠵ࠤࠏࠦࠠࠡࠢࠫࡗࡕ࠾࠰࠱ࡡ࠴࠻ࡤࡈ࠲ࡠࡒࡗ࠰ࠥ࠭ᐮ")5199c29a52c9f059unScramble_opy_ (u"ࠨ࠮ࠣࠫᐯ")0101018001010101unScramble_opy_ (u"ࠩ࠯ࠎࠥࠦࠠࠡࠢࠣࠤࠥ࠭ᐰ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"ࠪࡧ࠷࠸ࡦ࠱ࡣ࠵࠽࠹ࡧ࠷࠲ࡨ࠵࠽࡫࠭ᐱ"), l1l1111_Krypto_ (u"ࠫ࠵࠷࠰࠲࠲࠴࠸࠵࠶࠱࠱࠳࠳࠵࠵࠷ࠧᐲ"),
        l1l1111_Krypto_ (u"ࠬࡔࡉࡔࡖࠣࡗࡕ࠾࠰࠱࠯࠴࠻ࠥࡈ࠮࠳ࠢࠍࠤࠥࠦࠠࠩࡕࡓ࠼࠵࠶࡟࠲࠹ࡢࡆ࠷ࡥࡐࡕ࠮ࠣࠫᐳ")l1l1ll1l11l_Krypto_ (u"࠭ࠬࠡࠩᐴ")0101012001010101unScramble_opy_ (u"ࠧ࠭ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠫᐵ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"ࠨࡣ࠻࠵࡫ࡨࡤ࠵࠶࠻ࡪ࠾࡫࠵࠳࠴ࡩࠫᐶ"), l1l1111_Krypto_ (u"ࠩ࠳࠵࠵࠷࠰࠲࠳࠳࠴࠶࠶࠱࠱࠳࠳࠵ࠬᐷ"),
        l1l1111_Krypto_ (u"ࠪࡒࡎ࡙ࡔࠡࡕࡓ࠼࠵࠶࠭࠲࠹ࠣࡆ࠳࠸ࠠࠋࠢࠣࠤࠥ࠮ࡓࡑ࠺࠳࠴ࡤ࠷࠷ࡠࡄ࠵ࡣࡕ࡚ࠬࠡࠩᐸ")4f644c92e192dfedunScramble_opy_ (u"ࠫ࠱ࠦࠧᐹ")0101010801010101unScramble_opy_ (u"ࠬ࠲ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠩᐺ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"࠭࠱ࡢࡨࡤ࠽ࡦ࠼࠶ࡢ࠸ࡧࡪ࠾࠸ࡡࡦࠩᐻ"), l1l1111_Krypto_ (u"ࠧ࠱࠳࠳࠵࠵࠷࠰࠵࠲࠴࠴࠶࠶࠱࠱࠳ࠪᐼ"),
        l1l1111_Krypto_ (u"ࠨࡐࡌࡗ࡙ࠦࡓࡑ࠺࠳࠴࠲࠷࠷ࠡࡄ࠱࠶ࠥࠐࠠࠡࠢࠣࠬࡘࡖ࠸࠱࠲ࡢ࠵࠼ࡥࡂ࠳ࡡࡓࡘ࠱ࠦࠧᐽ")l1l1l1ll111_Krypto_ (u"ࠩ࠯ࠤࠬᐾ")0101010201010101unScramble_opy_ (u"ࠪ࠰ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠧᐿ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"ࠫ࠶࠿ࡤ࠱࠵࠵ࡩ࠻࠺ࡡࡣ࠲ࡥࡨ࠽ࡨࠧᑀ"), l1l1111_Krypto_ (u"ࠬ࠶࠱࠱࠳࠳࠵࠵࠷࠸࠱࠲࠴࠴࠶࠶࠱ࠨᑁ"),
        l1l1111_Krypto_ (u"࠭ࡎࡊࡕࡗࠤࡘࡖ࠸࠱࠲࠰࠵࠼ࠦࡂ࠯࠴ࠣࠎࠥࠦࠠࠡࠪࡖࡔ࠽࠶࠰ࡠ࠳࠺ࡣࡇ࠸࡟ࡑࡖ࠯ࠤࠬᑂ")3cfaa7a7dc8720dcunScramble_opy_ (u"ࠧ࠭ࠢࠪᑃ")0101010140010101unScramble_opy_ (u"ࠨ࠮ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠬᑄ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"ࠩࡥ࠻࠷࠼࠵ࡧ࠹ࡩ࠸࠹࠽ࡡࡤ࠸ࡩ࠷ࠬᑅ"), l1l1111_Krypto_ (u"ࠪ࠴࠶࠶࠱࠱࠳࠳࠵࠷࠶࠰࠲࠲࠴࠴࠶࠭ᑆ"),
        l1l1111_Krypto_ (u"ࠫࡓࡏࡓࡕࠢࡖࡔ࠽࠶࠰࠮࠳࠺ࠤࡇ࠴࠲ࠡࠌࠣࠤࠥࠦࠨࡔࡒ࠻࠴࠵ࡥ࠱࠸ࡡࡅ࠶ࡤࡖࡔ࠭ࠢࠪᑇ")9db73b3c0d163f54unScramble_opy_ (u"ࠬ࠲ࠠࠨᑈ")0101010110010101unScramble_opy_ (u"࠭ࠬࠋࠢࠣࠤࠥࠦࠠࠡࠢࠪᑉ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"ࠧ࠹࠳࠻࠵ࡧ࠼࠵ࡣࡣࡥࡪ࠹ࡧ࠹࠸࠷ࠪᑊ"), l1l1111_Krypto_ (u"ࠨ࠲࠴࠴࠶࠶࠱࠱࠳࠳࠼࠵࠷࠰࠲࠲࠴ࠫᑋ"),
        l1l1111_Krypto_ (u"ࠩࡑࡍࡘ࡚ࠠࡔࡒ࠻࠴࠵࠳࠱࠸ࠢࡅ࠲࠷ࠦࠊࠡࠢࠣࠤ࡙࠭ࡐ࠹࠲࠳ࡣ࠶࠽࡟ࡃ࠴ࡢࡔ࡙࠲ࠠࠨᑌ")93c9b64042eaa240unScramble_opy_ (u"ࠪ࠰ࠥ࠭ᑍ")0101010104010101unScramble_opy_ (u"ࠫ࠱ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠨᑎ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"ࠬ࠻࠵࠸࠲࠸࠷࠵࠾࠲࠺࠹࠳࠹࠺࠿࠲ࠨᑏ"), l1l1111_Krypto_ (u"࠭࠰࠲࠲࠴࠴࠶࠶࠱࠱࠴࠳࠵࠵࠷࠰࠲ࠩᑐ"),
        l1l1111_Krypto_ (u"ࠧࡏࡋࡖࡘ࡙ࠥࡐ࠹࠲࠳࠱࠶࠽ࠠࡃ࠰࠵ࠤࠏࠦࠠࠡࠢࠫࡗࡕ࠾࠰࠱ࡡ࠴࠻ࡤࡈ࠲ࡠࡒࡗ࠰ࠥ࠭ᑑ")8638809e878787a0unScramble_opy_ (u"ࠨ࠮ࠣࠫᑒ")0101010101800101unScramble_opy_ (u"ࠩ࠯ࠎࠥࠦࠠࠡࠢࠣࠤࠥ࠭ᑓ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"ࠪ࠸࠶ࡨ࠹ࡢ࠹࠼ࡥ࡫࠽࠹ࡢࡥ࠵࠴࠽࠭ᑔ"), l1l1111_Krypto_ (u"ࠫ࠵࠷࠰࠲࠲࠴࠴࠶࠶࠱࠵࠲࠳࠵࠵࠷ࠧᑕ"),
        l1l1111_Krypto_ (u"ࠬࡔࡉࡔࡖࠣࡗࡕ࠾࠰࠱࠯࠴࠻ࠥࡈ࠮࠳ࠢࠍࠤࠥࠦࠠࠩࡕࡓ࠼࠵࠶࡟࠲࠹ࡢࡆ࠷ࡥࡐࡕ࠮ࠣࠫᑖ")7a9be42f2009a892unScramble_opy_ (u"࠭ࠬࠡࠩᑗ")0101010101200101unScramble_opy_ (u"ࠧ࠭ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠫᑘ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"ࠨ࠴࠼࠴࠸࠾ࡤ࠶࠸ࡥࡥ࠻ࡪ࠲࠸࠶࠸ࠫᑙ"), l1l1111_Krypto_ (u"ࠩ࠳࠵࠵࠷࠰࠲࠲࠴࠴࠶࠷࠰࠱࠳࠳࠵ࠬᑚ"),
        l1l1111_Krypto_ (u"ࠪࡒࡎ࡙ࡔࠡࡕࡓ࠼࠵࠶࠭࠲࠹ࠣࡆ࠳࠸ࠠࠋࠢࠣࠤࠥ࠮ࡓࡑ࠺࠳࠴ࡤ࠷࠷ࡠࡄ࠵ࡣࡕ࡚ࠬࠡࠩᑛ")5495c6abf1e5df51unScramble_opy_ (u"ࠫ࠱ࠦࠧᑜ")0101010101080101unScramble_opy_ (u"ࠬ࠲ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠩᑝ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"࠭ࡡࡦ࠳࠶ࡨࡧࡪ࠵࠷࠳࠷࠼࠽࠿࠳࠴ࠩᑞ"), l1l1111_Krypto_ (u"ࠧ࠱࠳࠳࠵࠵࠷࠰࠲࠲࠴࠴࠹࠶࠱࠱࠳ࠪᑟ"),
        l1l1111_Krypto_ (u"ࠨࡐࡌࡗ࡙ࠦࡓࡑ࠺࠳࠴࠲࠷࠷ࠡࡄ࠱࠶ࠥࠐࠠࠡࠢࠣࠬࡘࡖ࠸࠱࠲ࡢ࠵࠼ࡥࡂ࠳ࡡࡓࡘ࠱ࠦࠧᑠ")024d1ffa8904e389unScramble_opy_ (u"ࠩ࠯ࠤࠬᑡ")0101010101020101unScramble_opy_ (u"ࠪ࠰ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠧᑢ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"ࠫࡩ࠷࠳࠺࠻࠺࠵࠷࡬࠹࠺ࡤࡩ࠴࠷࡫ࠧᑣ"), l1l1111_Krypto_ (u"ࠬ࠶࠱࠱࠳࠳࠵࠵࠷࠰࠲࠲࠴࠼࠵࠶࠱ࠨᑤ"),
        l1l1111_Krypto_ (u"࠭ࡎࡊࡕࡗࠤࡘࡖ࠸࠱࠲࠰࠵࠼ࠦࡂ࠯࠴ࠣࠎࠥࠦࠠࠡࠪࡖࡔ࠽࠶࠰ࡠ࠳࠺ࡣࡇ࠸࡟ࡑࡖ࠯ࠤࠬᑥ")14c1d7c1cffec79eunScramble_opy_ (u"ࠧ࠭ࠢࠪᑦ")0101010101014001unScramble_opy_ (u"ࠨ࠮ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠬᑧ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"ࠩ࠴ࡨࡪ࠻࠲࠸࠻ࡧࡥࡪ࠹ࡢࡦࡦ࠹ࡪࠬᑨ"), l1l1111_Krypto_ (u"ࠪ࠴࠶࠶࠱࠱࠳࠳࠵࠵࠷࠰࠲࠴࠳࠴࠶࠭ᑩ"),
        l1l1111_Krypto_ (u"ࠫࡓࡏࡓࡕࠢࡖࡔ࠽࠶࠰࠮࠳࠺ࠤࡇ࠴࠲ࠡࠌࠣࠤࠥࠦࠨࡔࡒ࠻࠴࠵ࡥ࠱࠸ࡡࡅ࠶ࡤࡖࡔ࠭ࠢࠪᑪ")l1l1l1l1lll_Krypto_ (u"ࠬ࠲ࠠࠨᑫ")0101010101011001unScramble_opy_ (u"࠭ࠬࠋࠢࠣࠤࠥࠦࠠࠡࠢࠪᑬ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"ࠧࡥࡣ࠼࠽ࡩࡨࡢࡤ࠻ࡤ࠴࠸࡬࠳࠸࠻ࠪᑭ"), l1l1111_Krypto_ (u"ࠨ࠲࠴࠴࠶࠶࠱࠱࠳࠳࠵࠵࠷࠰࠹࠲࠴ࠫᑮ"),
        l1l1111_Krypto_ (u"ࠩࡑࡍࡘ࡚ࠠࡔࡒ࠻࠴࠵࠳࠱࠸ࠢࡅ࠲࠷ࠦࠊࠡࠢࠣࠤ࡙࠭ࡐ࠹࠲࠳ࡣ࠶࠽࡟ࡃ࠴ࡢࡔ࡙࠲ࠠࠨᑯ")l1l1ll11ll1_Krypto_ (u"ࠪ࠰ࠥ࠭ᑰ")0101010101010401unScramble_opy_ (u"ࠫ࠱ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠨᑱ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"ࠬࡧࡥ࠹ࡧ࠸ࡧࡦࡧ࠳ࡤࡣ࠳࠸ࡪ࠾࠵ࠨᑲ"), l1l1111_Krypto_ (u"࠭࠰࠲࠲࠴࠴࠶࠶࠱࠱࠳࠳࠵࠵࠸࠰࠲ࠩᑳ"),
        l1l1111_Krypto_ (u"ࠧࡏࡋࡖࡘ࡙ࠥࡐ࠹࠲࠳࠱࠶࠽ࠠࡃ࠰࠵ࠤࠏࠦࠠࠡࠢࠫࡗࡕ࠾࠰࠱ࡡ࠴࠻ࡤࡈ࠲ࡠࡒࡗ࠰ࠥ࠭ᑴ")9cc62df43b6eed74unScramble_opy_ (u"ࠨ࠮ࠣࠫᑵ")0101010101010180unScramble_opy_ (u"ࠩ࠯ࠎࠥࠦࠠࠡࠢࠣࠤࠥ࠭ᑶ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"ࠪࡨ࠽࠼࠳ࡥࡤࡥ࠹ࡨ࠻࠹ࡢ࠻࠴ࡥ࠵࠭ᑷ"), l1l1111_Krypto_ (u"ࠫ࠵࠷࠰࠲࠲࠴࠴࠶࠶࠱࠱࠳࠳࠵࠹࠶ࠧᑸ"),
        l1l1111_Krypto_ (u"ࠬࡔࡉࡔࡖࠣࡗࡕ࠾࠰࠱࠯࠴࠻ࠥࡈ࠮࠳ࠢࠍࠤࠥࠦࠠࠩࡕࡓ࠼࠵࠶࡟࠲࠹ࡢࡆ࠷ࡥࡐࡕ࠮ࠣࠫᑹ")l1l1ll1111l_Krypto_ (u"࠭ࠬࠡࠩᑺ")0101010101010120unScramble_opy_ (u"ࠧ࠭ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠫᑻ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"ࠨ࠲࠻࠻࠺࠶࠴࠲ࡧ࠹࠸ࡨ࠻࠷࠱ࡨ࠺ࠫᑼ"), l1l1111_Krypto_ (u"ࠩ࠳࠵࠵࠷࠰࠲࠲࠴࠴࠶࠶࠱࠱࠳࠴࠴ࠬᑽ"),
        l1l1111_Krypto_ (u"ࠪࡒࡎ࡙ࡔࠡࡕࡓ࠼࠵࠶࠭࠲࠹ࠣࡆ࠳࠸ࠠࠋࠢࠣࠤࠥ࠮ࡓࡑ࠺࠳࠴ࡤ࠷࠷ࡠࡄ࠵ࡣࡕ࡚ࠬࠡࠩᑾ")5a594528bebef1ccunScramble_opy_ (u"ࠫ࠱ࠦࠧᑿ")0101010101010108unScramble_opy_ (u"ࠬ࠲ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠩᒀ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
    (l1l1l1llll1_Krypto_, l1l1111_Krypto_ (u"࠭ࡦࡤࡦࡥ࠷࠷࠿࠱ࡥࡧ࠵࠵࡫࠶ࡣ࠱ࠩᒁ"), l1l1111_Krypto_ (u"ࠧ࠱࠳࠳࠵࠵࠷࠰࠲࠲࠴࠴࠶࠶࠱࠱࠶ࠪᒂ"),
        l1l1111_Krypto_ (u"ࠨࡐࡌࡗ࡙ࠦࡓࡑ࠺࠳࠴࠲࠷࠷ࠡࡄ࠱࠶ࠥࠐࠠࠡࠢࠣࠬࡘࡖ࠸࠱࠲ࡢ࠵࠼ࡥࡂ࠳ࡡࡓࡘ࠱ࠦࠧᒃ")869efd7f9f265a09unScramble_opy_ (u"ࠩ࠯ࠤࠬᒄ")0101010101010102unScramble_opy_ (u"ࠪ࠰ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠧᒅ")l1l1ll1llll_Krypto_ l1l1ll111ll_Krypto_-17 B.2
]
class l1l1ll11111_Krypto_(l1lll111111_Krypto_.TestCase):
    l1l1111_Krypto_ (u"ࠦࠧࠨࠠࡓࡱࡱࡥࡱࡪࠠࡍ࠰ࠣࡖ࡮ࡼࡥࡴࡶࠪࡷࠥࡊࡅࡔࠢࡷࡩࡸࡺࠬࠡࡵࡨࡩࠥࠐࠠࠡࠢࠣࠤࠥࠦࠠࡩࡶࡷࡴ࠿࠵࠯ࡱࡧࡲࡴࡱ࡫࠮ࡤࡵࡤ࡭ࡱ࠴࡭ࡪࡶ࠱ࡩࡩࡻ࠯ࡳ࡫ࡹࡩࡸࡺ࠯ࡅࡧࡶࡸࡪࡹࡴ࠯ࡶࡻࡸࠏࠦࠠࠡࠢࡄࡆࡘ࡚ࡒࡂࡅࡗࠎࠥࠦࠠࠡ࠯࠰࠱࠲࠳࠭࠮࠯ࠍࠎ࡙ࠥࠦࠠࠡࡨࠤࡵࡸࡥࡴࡧࡱࡸࠥࡧࠠࡴ࡫ࡰࡴࡱ࡫ࠠࡸࡣࡼࠤࡹࡵࠠࡵࡧࡶࡸࠥࡺࡨࡦࠢࡦࡳࡷࡸࡥࡤࡶࡱࡩࡸࡹࠠࡰࡨࠣࡥࠥࡊࡅࡔࠢ࡬ࡱࡵࡲࡥ࡮ࡧࡱࡸࡦࡺࡩࡰࡰ࠽ࠎࠥࠦࠠࠡࡗࡶࡩࠥࡺࡨࡦࠢࡵࡩࡨࡻࡲࡳࡧࡱࡧࡪࠦࡲࡦ࡮ࡤࡸ࡮ࡵ࡮࠻ࠌࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡝࠶ࠠࠡࠢࠣࠤࠥࡃࠠࠡࠢࠣࠤࠥࠦ࠹࠵࠹࠷ࡆ࠽ࡋ࠸ࡄ࠹࠶ࡆࡈࡇ࠷ࡅࠢࠫ࡬ࡪࡾࡡࡥࡧࡦ࡭ࡲࡧ࡬ࠪࠌࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡝࠮ࡩࠬ࠳ࠬࠤࠥࡃࠠࠡࠢࠣࠤࠥࠦࡉࡇࠢࠣࠬ࡮ࠦࡩࡴࠢࡨࡺࡪࡴࠩࠡࠢࡗࡌࡊࡔࠠࠡࡇࠫ࡜࡮࠲ࡘࡪࠫࠣࠤࡊࡒࡓࡆࠢࠣࡈ࠭࡞ࡩ࡚࠭࡬࠭ࠏࠐࠠࠡࠢࠣࡸࡴࠦࡣࡰ࡯ࡳࡹࡹ࡫ࠠࡢࠢࡶࡩࡶࡻࡥ࡯ࡥࡨࠤࡴ࡬ࠠ࠷࠶࠰ࡦ࡮ࡺࠠࡷࡣ࡯ࡹࡪࡹ࠺࡛ࠡࠢ࠴࠱ࠦࡘ࠲࠮ࠣ࡜࠷࠲ࠠ࠯࠰࠱࠰ࠥ࡞࠱࠷࠰ࠣࠤࡍ࡫ࡲࡦࠌࠣࠤࠥࠦࡅ࡚ࠩ࠯ࡏ࠮ࠦࠠࡥࡧࡱࡳࡹ࡫ࡳࠡࡶ࡫ࡩࠥࡊࡅࡔࠢࡨࡲࡨࡸࡹࡱࡶ࡬ࡳࡳࠦ࡯ࡧࠢࠣ࡜ࠥࠦࡵࡴ࡫ࡱ࡫ࠥࡱࡥࡺࠢࠣࡏ࠱ࠦࡡ࡯ࡦࠣࠤࡉ࠮ࡘ࠭ࡍࠬࠤࠥࡪࡥ࡯ࡱࡷࡩࡸࠐࠠࠡࠢࠣࡸ࡭࡫ࠠࡅࡇࡖࠤࡩ࡫ࡣࡳࡻࡳࡸ࡮ࡵ࡮ࠡࡱࡩࠤࠥ࡞ࠠࠡࡷࡶ࡭ࡳ࡭ࠠ࡬ࡧࡼࠤࠥࡑ࠮ࠡࠢࡌࡪࠥࡿ࡯ࡶࠢࡲࡦࡹࡧࡩ࡯ࠌࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡝࠷࠶ࠡࠢࠣࠤࠥࡃࠠࠡࠢࠣࠤࠥࠦ࠱ࡃ࠳ࡄ࠶ࡉࡊࡂ࠵ࡅ࠹࠸࠷࠺࠳࠹ࠌࠍࠤࠥࠦࠠࡺࡱࡸࡶࠥ࡯࡭ࡱ࡮ࡨࡱࡪࡴࡴࡢࡶ࡬ࡳࡳࠦࡤࡰࡧࡶࠤࡳࡵࡴࠡࡪࡤࡺࡪࠦࡡ࡯ࡻࠣࡳ࡫ࠦࡴࡩࡧࠣ࠷࠻࠲࠵࠷࠺ࠣࡴࡴࡹࡳࡪࡤ࡯ࡩࠥࡹࡩ࡯ࡩ࡯ࡩ࠲࡬ࡡࡶ࡮ࡷࠤࠏࠦࠠࠡࠢࡨࡶࡷࡵࡲࡴࠢࡧࡩࡸࡩࡲࡪࡤࡨࡨࠥ࡮ࡥࡳࡧ࡬ࡲ࠳ࠐࠠࠡࠢࠣࠦࠧࠨᒆ")
    def runTest(self):
        from l111ll1_Krypto_.l11111l_Krypto_ import l11ll1l1_Krypto_
        from binascii import b2a_hex as l1llll1l1l1_Krypto_
        X = []
        X[0:] = [b(l1l1111_Krypto_ (u"ࠬࡢࡸ࠺࠶࡟ࡼ࠼࠺࡜ࡹࡄ࠻ࡠࡽࡋ࠸࡝ࡺࡆ࠻ࡡࡾ࠳ࡃ࡞ࡻࡇࡆࡢࡸ࠸ࡆࠪᒇ"))]
        for i in range(16):
            c = l11ll1l1_Krypto_.new(X[i],l11ll1l1_Krypto_.l1lll1ll_Krypto_)
            if not (i&1):
                X[i+1:] = [c.l1_Krypto_(X[i])]
            else:
                X[i+1:] = [c.l1lllll_Krypto_(X[i])]
        self.assertEqual(l1llll1l1l1_Krypto_(X[16]),
            l1llll1l1l1_Krypto_(b(l1l1111_Krypto_ (u"࠭࡜ࡹ࠳ࡅࡠࡽ࠷ࡁ࡝ࡺ࠵ࡈࡡࡾࡄࡃ࡞ࡻ࠸ࡈࡢࡸ࠷࠶࡟ࡼ࠷࠺࡜ࡹ࠵࠻ࠫᒈ"))))
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    from l111ll1_Krypto_.l11111l_Krypto_ import l11ll1l1_Krypto_
    from .common import l1ll1ll11l1_Krypto_
    return l1ll1ll11l1_Krypto_(l11ll1l1_Krypto_, l1l1111_Krypto_ (u"ࠢࡅࡇࡖࠦᒉ"), l1ll11lllll_Krypto_) + [l1l1ll11111_Krypto_()]
if __name__ == l1l1111_Krypto_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪᒊ"):
    import unittest as l1lll111111_Krypto_
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"ࠩࡶࡹ࡮ࡺࡥࠨᒋ"))