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
l1l1111_Krypto_ (u"ࠦࠧࠨࡓࡦ࡮ࡩ࠱ࡹ࡫ࡳࡵࠢࡶࡹ࡮ࡺࡥࠡࡨࡲࡶࠥࡉࡲࡺࡲࡷࡳ࠳ࡎࡡࡴࡪ࠱ࡌࡒࡇࡃࠣࠤࠥᙆ")
__revision__ = l1l1111_Krypto_ (u"ࠧࠪࡉࡥࠦࠥᙇ")
from .common import dict
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
l1ll11lllll_Krypto_ = [
    (l1l1111_Krypto_ (u"࠭࠰ࡣࠩᙈ") * 16,
        l1l1111_Krypto_ (u"ࠧ࠵࠺࠹࠽࠷࠶࠵࠵࠸࠻࠺࠺࠽࠲࠷࠷ࠪᙉ"),
        dict(default=l1l1111_Krypto_ (u"ࠨ࠻࠵࠽࠹࠽࠲࠸ࡣ࠶࠺࠸࠾ࡢࡣ࠳ࡦ࠵࠸࡬࠴࠹ࡧࡩ࠼࠶࠻࠸ࡣࡨࡦ࠽ࡩ࠭ᙊ")),
        l1l1111_Krypto_ (u"ࠩࡧࡩ࡫ࡧࡵ࡭ࡶ࠰࡭ࡸ࠳ࡍࡅ࠷ࠪᙋ")),
    (l1l1111_Krypto_ (u"ࠪ࠴ࡧ࠭ᙌ") * 16,
        l1l1111_Krypto_ (u"ࠫ࠹࠾࠶࠺࠴࠳࠹࠹࠼࠸࠷࠷࠺࠶࠻࠻ࠧᙍ"),
        dict(l1llllllll_Krypto_=l1l1111_Krypto_ (u"ࠬ࠿࠲࠺࠶࠺࠶࠼ࡧ࠳࠷࠵࠻ࡦࡧ࠷ࡣ࠲࠵ࡩ࠸࠽࡫ࡦ࠹࠳࠸࠼ࡧ࡬ࡣ࠺ࡦࠪᙎ")),
        l1l1111_Krypto_ (u"࠭ࡒࡇࡅࠣ࠶࠷࠶࠲ࠡࠌࠍࠤࠥࠦࠠࠋࠢࠣࠤࠥ࠮ࠧᙏ")0unScramble_opy_ (u"ࡢࠨࠢ࠭ࠤ࠷࠶ࠬࠋࠢࠣࠤࠥࠦࠠࠡࠢࠪᙐ")4869205468657265unScramble_opy_ (u"ࠨ࠮ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡩ࡯ࡣࡵࠪࡖࡌࡆ࠷࠽ࠨᙑ")l1l111ll1l1_Krypto_ (u"ࠩࠬ࠰ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠧᙒ")l1ll1111ll1_Krypto_ 2202
    (l1l1111_Krypto_ (u"ࠪ࠸ࡦ࠼࠵࠷࠸࠹࠹ࠬᙓ"),
        l1l1111_Krypto_ (u"ࠫ࠼࠽࠶࠹࠸࠴࠻࠹࠸࠰࠷࠶࠹ࡪ࠷࠶࠷࠺࠸࠴࠶࠵࠽࠷࠷࠳࠹ࡩ࠼࠺࠲࠱࠸࠹࠺࡫࠽࠲࠳࠲࠹ࡩ࠻࡬࠷࠵࠸࠻࠺࠾࠼ࡥ࠷࠹࠶ࡪࠬᙔ"),
        dict(l1llllllll_Krypto_=l1l1111_Krypto_ (u"ࠬ࠽࠵࠱ࡥ࠺࠼࠸࡫࠶ࡢࡤ࠳ࡦ࠺࠶࠳ࡦࡣࡤ࠼࠻࡫࠳࠲࠲ࡤ࠹ࡩࡨ࠷࠴࠺ࠪᙕ"),
            l1l1l1l1ll_Krypto_=l1l1111_Krypto_ (u"࠭ࡥࡧࡨࡦࡨ࡫࠼ࡡࡦ࠷ࡨࡦ࠷࡬ࡡ࠳ࡦ࠵࠻࠹࠷࠶ࡥ࠷ࡩ࠵࠽࠺ࡤࡧ࠻ࡦ࠶࠺࠿ࡡ࠸ࡥ࠺࠽ࠬᙖ")),
        l1l1111_Krypto_ (u"ࠧࡓࡈࡆࠤ࠷࠸࠰࠳ࠢࠍࠎࠥࠦࠠࠡࠌࠣࠤࠥࠦࠨࠨᙗ")l1l111l1l1l_Krypto_ (u"ࠨࠢ࠭ࠤ࠶࠼ࠬࠋࠢࠣࠤࠥࠦࠠࠡࠢࠪᙘ")l1l111l11ll_Krypto_ (u"ࠩࠣ࠮ࠥ࠻࠰࠭ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡨ࡮ࡩࡴࠩࡏࡇ࠹ࡂ࠭ᙙ")56be34521d144c88dbb8c733f0e8b3f6unScramble_opy_ (u"ࠪ࠭࠱ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠨᙚ")l1ll1111ll1_Krypto_ 2202
    (l1l1111_Krypto_ (u"ࠫࡦࡧࠧᙛ") * 20,
        l1l1111_Krypto_ (u"ࠬࡪࡤࠨᙜ") * 50,
        dict(l1l1l1l1ll_Krypto_=l1l1111_Krypto_ (u"࠭࠱࠳࠷ࡧ࠻࠸࠺࠲ࡣ࠻ࡤࡧ࠶࠷ࡣࡥ࠻࠴ࡥ࠸࠿ࡡࡧ࠶࠻ࡥࡦ࠷࠷ࡣ࠶ࡩ࠺࠸࡬࠱࠸࠷ࡧ࠷ࠬᙝ")),
        l1l1111_Krypto_ (u"ࠧࡓࡈࡆࠤ࠷࠸࠰࠳ࠢࠍࠎࠥࠦࠠࠡࠌࠣࠤࠥࠦࠨࠨᙞ")0102030405060708090a0b0c0d0e0f10111213141516171819unScramble_opy_ (u"ࠨ࠮ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠬᙟ")l1l111l1ll1_Krypto_ (u"ࠩࠣ࠮ࠥ࠻࠰࠭ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡨ࡮ࡩࡴࠩࡏࡇ࠹ࡂ࠭ᙠ")697eaf0aca3a3aea3a75164746ffaa79unScramble_opy_ (u"ࠪ࠰ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡗࡍࡇ࠱࠾ࠩᙡ")4c9007f4026250c6bc8414f9bf50c86c2d7235daunScramble_opy_ (u"ࠫ࠮࠲ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠩᙢ")l1ll1111ll1_Krypto_ 2202
    (l1l1111_Krypto_ (u"ࠬ࠶ࡣࠨᙣ") * 16,
        l1l1111_Krypto_ (u"࠭࠵࠵࠸࠸࠻࠸࠽࠴࠳࠲࠸࠻࠻࠿࠷࠵࠸࠻࠶࠵࠻࠴࠸࠴࠺࠹࠻࡫࠶࠴࠸࠴࠻࠹࠼࠹࠷ࡨ࠹ࡩࠬᙤ"),
        dict(l1llllllll_Krypto_=l1l1111_Krypto_ (u"ࠧ࠶࠸࠷࠺࠶࡫ࡦ࠳࠵࠷࠶ࡪࡪࡣ࠱࠲ࡩ࠽ࡧࡧࡢ࠺࠻࠸࠺࠾࠶ࡥࡧࡦ࠷ࡧࠬᙥ")),
        l1l1111_Krypto_ (u"ࠨࡔࡉࡇࠥ࠸࠲࠱࠴ࠣࠎࠏࠦࠠࠡࠢࠍࠤࠥࠦࠠࠋࠢࠣࠤࠥ࠮ࠧᙦ")0cunScramble_opy_ (u"ࠩࠣ࠮ࠥ࠸࠰࠭ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠫᙧ")546573742057697468205472756e636174696f6eunScramble_opy_ (u"ࠪ࠰ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡤࡪࡥࡷࠬࡘࡎࡁ࠲࠿ࠪᙨ")4c1a03424b55e07fe7f27be1d58bb9324a9a5a04unScramble_opy_ (u"ࠫ࠮࠲ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠩᙩ")l1ll1111ll1_Krypto_ 2202
    (l1l1111_Krypto_ (u"ࠬࡧࡡࠨᙪ") * 80,
        l1l1111_Krypto_ (u"࠭࠵࠵࠸࠸࠻࠸࠽࠴࠳࠲࠸࠹࠼࠹࠶࠺࠸ࡨ࠺࠼࠸࠰࠵ࡥ࠹࠵࠼࠸࠶࠸࠸࠸࠻࠷࠸࠰࠶࠶࠹࠼࠻࠷࠶ࡦ࠴࠳࠸࠷࠼ࡣ࠷ࡨ࠹࠷࠻ࡨ࠲ࡥ࠷࠶࠺࠾࠽ࡡࠨᙫ")
        + l1l1111_Krypto_ (u"ࠧ࠷࠷࠵࠴࠹ࡨ࠶࠶࠹࠼࠶࠵࠸ࡤ࠳࠲࠷࠼࠻࠷࠷࠴࠸࠻࠶࠵࠺ࡢ࠷࠷࠺࠽࠷࠶࠴࠷࠸࠼࠻࠷࠽࠳࠸࠶ࠪᙬ"),
        dict(l1llllllll_Krypto_=l1l1111_Krypto_ (u"ࠨ࠸ࡥ࠵ࡦࡨ࠷ࡧࡧ࠷ࡦࡩ࠽ࡢࡧ࠺ࡩ࠴ࡧ࠼࠲ࡦ࠸ࡦࡩ࠻࠷ࡢ࠺ࡦ࠳ࡧࡩ࠭᙭"),
            l1l1l1l1ll_Krypto_=l1l1111_Krypto_ (u"ࠩࡤࡥ࠹ࡧࡥ࠶ࡧ࠴࠹࠷࠽࠲ࡥ࠲࠳ࡩ࠾࠻࠷࠱࠷࠹࠷࠼ࡩࡥ࠹ࡣ࠶ࡦ࠺࠻ࡥࡥ࠶࠳࠶࠶࠷࠲ࠨ᙮")),
        l1l1111_Krypto_ (u"ࠪࡖࡋࡉࠠ࠳࠴࠳࠶ࠥࠐࠊࠡࠢࠣࠤࠏࠦࠠࠡࠢࠫࠫᙯ")l1l111l1l1l_Krypto_ (u"ࠫࠥ࠰ࠠ࠹࠲࠯ࠎࠥࠦࠠࠡࠢࠣࠤࠥ࠭ᙰ")54657374205573696e67204c6172676572205468616e20426c6f636b2d53697aunScramble_opy_ (u"ࠬࠐࠠࠡࠢࠣࠤࠥࠦࠠࠬࠢࠪᙱ")65204b657920616e64204c6172676572205468616e204f6e6520426c6f636b2dunScramble_opy_ (u"࠭ࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠭ࠣࠫᙲ")53697a652044617461unScramble_opy_ (u"ࠧ࠭ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡨ࡮ࡩࡴࠩࡏࡇ࠹ࡂ࠭ᙳ")6f630fad67cda0ee1fb1f562db3aa53eunScramble_opy_ (u"ࠨ࠮ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡕࡋࡅ࠶ࡃࠧᙴ")l1l111ll11l_Krypto_ (u"ࠩࠬ࠰ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠧᙵ")l1ll1111ll1_Krypto_ 2202
    (l1l1111_Krypto_ (u"ࠪ࠴ࡧ࠶ࡢ࠱ࡤ࠳ࡦ࠵ࡨ࠰ࡣ࠲ࡥ࠴ࡧ࠶ࡢ࠱ࡤ࠳ࡦ࠵ࡨ࠰ࡣ࠲ࡥ࠴ࡧ࠶ࡢ࠱ࡤ࠳ࡦ࠵ࡨ࠰ࡣࠩᙶ"),
        l1l1111_Krypto_ (u"ࠫ࠹࠾࠶࠺࠴࠳࠹࠹࠼࠸࠷࠷࠺࠶࠻࠻ࠧᙷ"),
        dict(l1lll1ll11_Krypto_=l1l1111_Krypto_ (u"ࠬ࠭ࠧࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡢ࠱࠵࠷࠸ࡨ࠼࠱ࡥ࠺ࡧࡦ࠸࠾࠵࠴࠷ࡦࡥ࠽ࡧࡦࡤࡧࡤࡪ࠵ࡨࡦ࠲࠴ࡥࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠻࠼࠶ࡪࡣ࠳࠲࠳ࡧ࠾࠾࠳࠴ࡦࡤ࠻࠷࠼ࡥ࠺࠵࠺࠺ࡨ࠸ࡥ࠴࠴ࡦࡪ࡫࠽ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠩࠪࠫᙸ")),
        l1l1111_Krypto_ (u"࠭ࡒࡇࡅࠣ࠸࠷࠹࠱ࠡࠌࠍࠤࠥࠦࠠࠋࠢࠣࠤࠥࠐࠠࠡࠢࠣࠬࠬᙹ")4a656665unScramble_opy_ (u"ࠧ࠭ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠫᙺ")7768617420646f2079612077616e7420666f72206e6f7468696e673funScramble_opy_ (u"ࠨ࠮ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡩ࡯ࡣࡵࠪࡖࡌࡆ࠸࠵࠷࠿ࠪᙻ")l1l1111_Krypto_ (u"ࠩࠪᙼ")
            5bdcc146bf60754e6a042426089575c7
            5a003f089d2739839dec58b964ec3843
        l1l1111_Krypto_ (u"ࠪࠫࠬ࠯ࠬࠋࠢࠣࠤࠥࠦࠠࠡࠢࠪࡖࡋࡉࠠ࠵࠴࠶࠵ࠥࠐࠊࠡࠢࠣࠤࠏࠦࠠࠡࠢࠍࠤࠥࠦࠠࠩࠩࡤࡥࠬࠦࠪࠡ࠴࠳࠰ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠧࡥࡦࠪࠤ࠯ࠦ࠵࠱࠮ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡩ࡯ࡣࡵࠪࡖࡌࡆ࠸࠵࠷࠿ࠪࠫࠬᙽ")
            773ea91e36800e46854db8ebd09181a7
            2959098b3ef8c122d9635514ced565fe
        l1l1111_Krypto_ (u"ࠫࠬ࠭ࠩ࠭ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠫࡗࡌࡃࠡ࠶࠵࠷࠶ࠦࠊࠋࠢࠣࠤࠥࠐࠠࠡࠢࠣࠎࠥࠦࠠࠡࠪࠪ࠴࠶࠶࠲࠱࠵࠳࠸࠵࠻࠰࠷࠲࠺࠴࠽࠶࠹࠱ࡣ࠳ࡦ࠵ࡩ࠰ࡥ࠲ࡨ࠴࡫࠷࠰࠲࠳࠴࠶࠶࠹࠱࠵࠳࠸࠵࠻࠷࠷࠲࠺࠴࠽ࠬ࠲ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠩࡦࡨࠬࠦࠪࠡ࠷࠳࠰ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡤࡪࡥࡷࠬࡘࡎࡁ࠳࠷࠹ࡁࠬ࠭ࠧᙾ")
            82558a389a443c0ea4cc819899f2083a
            85f0faa3e578f8077a2e3ff46729665b
        l1l1111_Krypto_ (u"ࠬ࠭ࠧࠪ࠮ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠬࡘࡆࡄࠢ࠷࠶࠸࠷ࠠࠋࠌࠣࠤࠥࠦࠊࠡࠢࠣࠤࠏࠦࠠࠡࠢࠍࠤࠥࠦࠠࠋࠌࠣࠤࠥࠦࠊࠡࠢࠣࠤࠏࠦࠠࠡࠢࠫࠫࡦࡧࠧࠡࠬࠣ࠵࠸࠷ࠬࠋࠢࠣࠤࠥࠦࠠࠡࠢࠪ࠹࠹࠼࠵࠸࠵࠺࠸࠷࠶࠵࠶࠹࠶࠺࠾࠼ࡥ࠷࠹࠵࠴࠹ࡩ࠶࠲࠹࠵࠺࠼࠼࠵࠸࠴࠵࠴࠺࠺࠶࠹࠸࠴࠺ࡪ࠸࠰࠵࠴࠹ࡧ࠻࡬࠶࠴࠸ࡥ࠶ࡩ࠻࠳࠷࠻࠺ࡥࠬࠐࠠࠡࠢࠣࠤࠥࠦࠠࠬࠢࠪ࠺࠺࠸࠰࠵ࡤ࠹࠹࠼࠿࠲࠱࠴ࡧ࠶࠵࠺࠸࠷࠳࠺࠷࠻࠾࠲࠱࠶ࡥ࠺࠺࠽࠹࠳࠲࠷࠺࠻࠿࠷࠳࠹࠶࠻࠹࠭ࠬࠋࠢࠣࠤࠥࠦࠠࠡࠢࡧ࡭ࡨࡺࠨࡔࡊࡄ࠶࠺࠼࠽ࠨࠩࠪᙿ")
            60e431591ee0b67f0d8a26aacbf5b77f
            8e0bc6213728c5140546040f0ee37f54
        l1l1111_Krypto_ (u"࠭ࠧࠨࠫ࠯ࠎࠥࠦࠠࠡࠢࠣࠤࠥ࠭ࡒࡇࡅࠣ࠸࠷࠹࠱ࠡࠌࠍࠤࠥࠦࠠࠋࠢࠣࠤࠥࠐࠠࠡࠢࠣࠬࠬࡧࡡࠨࠢ࠭ࠤ࠶࠹࠱࠭ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠫ࠺࠺࠶࠹࠸࠼࠻࠸࠸࠰࠷࠻࠺࠷࠷࠶࠶࠲࠴࠳࠻࠹࠼࠵࠸࠵࠺࠸࠷࠶࠷࠶࠹࠶࠺࠾࠼ࡥ࠷࠹࠵࠴࠻࠷࠲࠱࠸ࡦ࠺࠶࠽࠲࠷࠹࠹࠹࠼࠸࠲࠱࠹࠷࠺࠽࠭ࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠭ࠣࠫ࠻࠷࠶ࡦ࠴࠳࠺࠷࠼ࡣ࠷ࡨ࠹࠷࠻ࡨ࠲ࡥ࠹࠶࠺࠾࠽ࡡ࠷࠷࠵࠴࠻ࡨ࠶࠶࠹࠼࠶࠵࠼࠱࠷ࡧ࠹࠸࠷࠶࠶࠲࠴࠳࠺ࡨ࠼࠱࠸࠴࠹࠻࠻࠻࠷࠳࠴࠳࠻࠹࠭ࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠭ࠣࠫ࠻࠾࠶࠲࠸ࡨ࠶࠵࠼࠲࠷ࡥ࠹ࡪ࠻࠹࠶ࡣ࠴ࡧ࠻࠸࠼࠹࠸ࡣ࠹࠹࠷࠶࠶࠵࠸࠴࠻࠹࠼࠱࠳ࡧ࠵࠴࠺࠺࠶࠹࠸࠸࠶࠵࠼ࡢ࠷࠷࠺࠽࠷࠶࠶ࡦ࠸࠸࠺࠺࠭ࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠭ࠣࠫ࠻࠺࠷࠴࠴࠳࠻࠹࠼ࡦ࠳࠲࠹࠶࠻࠻࠲࠱࠸࠻࠺࠶࠽࠳࠷࠺࠹࠹࠻࠺࠲࠱࠸࠵࠺࠺࠼࠶࠷ࡨ࠺࠶࠻࠻࠲࠱࠸࠵࠺࠺࠼࠹࠷ࡧ࠹࠻࠷࠶࠷࠶࠹࠶࠺࠺࠭ࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠭ࠣࠫ࠻࠺࠲࠱࠸࠵࠻࠾࠸࠰࠸࠶࠹࠼࠻࠻࠲࠱࠶࠻࠸ࡩ࠺࠱࠵࠵࠵࠴࠻࠷࠶ࡤ࠸࠺࠺࡫࠽࠲࠷࠻࠺࠸࠻࠾࠶ࡥ࠴ࡨࠫ࠱ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡥ࡫ࡦࡸ࡙࠭ࡈࡂ࠴࠸࠺ࡂ࠭ࠧࠨ ")
            9b09ffa71b942fcb27635fbcd5b0e944
            l1l111l1l11_Krypto_
        l1l1111_Krypto_ (u"ࠧࠨᚁ")l1l1111_Krypto_ (u"ࠨࠫ࠯ࠎࠥࠦࠠࠡࠢࠣࠤࠥ࠭ᚂ")l1ll1111ll1_Krypto_ 4231
]
l1l111ll111_Krypto_ = [
    (l1l1111_Krypto_ (u"ࠩ࠷ࡥ࠻࠻࠶࠷࠸࠸ࠫᚃ"),
        l1l1111_Krypto_ (u"ࠪ࠻࠼࠼࠸࠷࠳࠺࠸࠷࠶࠶࠵࠸ࡩ࠶࠵࠽࠹࠷࠳࠵࠴࠼࠽࠶࠲࠸ࡨ࠻࠹࠭ᚄ")
        + l1l1111_Krypto_ (u"ࠫ࠷࠶࠶࠷࠸ࡩ࠻࠷࠸࠰࠷ࡧ࠹ࡪ࠼࠺࠶࠹࠸࠼࠺ࡪ࠼࠷࠴ࡨࠪᚅ"),
        dict(l1lll1lll1_Krypto_=l1l1111_Krypto_ (u"ࠬࡧ࠳࠱ࡧ࠳࠵࠵࠿࠸ࡣࡥ࠹ࡨࡧࡨࡦ࠵࠷࠹࠽࠵࡬࠳ࡢ࠹ࡨ࠽ࡪ࠼ࡤ࠱ࡨ࠻ࡦࡧ࡫ࡡ࠳ࡣ࠶࠽ࡪ࠼࠱࠵࠺࠳࠴࠽࡬ࡤ࠱࠷ࡨ࠸࠹࠭ᚆ")),
        l1l1111_Krypto_ (u"࠭ࡒࡇࡅࠣ࠸࠻࠹࠴ࠡ࠺࠱࠸࡙ࠥࡈࡂ࠴࠵࠸ࠥ࠮ࡈࡎࡃࡆ࠱ࡘࡎࡁ࠳࠴࠷࠭ࠬᚇ")),
    (l1l1111_Krypto_ (u"ࠧ࠵ࡣ࠹࠹࠻࠼࠶࠶ࠩᚈ"),
        l1l1111_Krypto_ (u"ࠨ࠹࠺࠺࠽࠼࠱࠸࠶࠵࠴࠻࠺࠶ࡧ࠴࠳࠻࠾࠼࠱࠳࠲࠺࠻࠻࠷࠶ࡦ࠹࠷ࠫᚉ")
        + l1l1111_Krypto_ (u"ࠩ࠵࠴࠻࠼࠶ࡧ࠹࠵࠶࠵࠼ࡥ࠷ࡨ࠺࠸࠻࠾࠶࠺࠸ࡨ࠺࠼࠹ࡦࠨᚊ"),
        dict(l1lll1l111_Krypto_=l1l1111_Krypto_ (u"ࠪࡥ࡫࠺࠵ࡥ࠴ࡨ࠷࠼࠼࠴࠹࠶࠳࠷࠶࠼࠱࠸ࡨ࠺࠼ࡩ࠸ࡢ࠶࠺ࡤ࠺ࡧ࠷ࡢ࠺ࡥ࠺ࡩ࡫࠺࠶࠵ࡨ࠸ࡥ࠵࠷ࡢ࠵࠹ࡨ࠸࠷࡫ࡣ࠴࠹࠶࠺࠸࠸࠲࠵࠶࠸ࡩ࠽࡫࠲࠳࠶࠳ࡧࡦ࠻ࡥ࠷࠻ࡨ࠶ࡨ࠽࠸ࡣ࠵࠵࠷࠾࡫ࡣࡧࡣࡥ࠶࠶࠼࠴࠺ࠩᚋ")),
        l1l1111_Krypto_ (u"ࠫࡗࡌࡃࠡ࠶࠹࠷࠹ࠦ࠸࠯࠶ࠣࡗࡍࡇ࠳࠹࠶ࠣࠬࡍࡓࡁࡄ࠯ࡖࡌࡆ࠹࠸࠵ࠫࠪᚌ")),
    (l1l1111_Krypto_ (u"ࠬ࠺ࡡ࠷࠷࠹࠺࠻࠻ࠧᚍ"),
        l1l1111_Krypto_ (u"࠭࠷࠸࠸࠻࠺࠶࠽࠴࠳࠲࠹࠸࠻࡬࠲࠱࠹࠼࠺࠶࠸࠰࠸࠹࠹࠵࠻࡫࠷࠵ࠩᚎ")
        + l1l1111_Krypto_ (u"ࠧ࠳࠲࠹࠺࠻࡬࠷࠳࠴࠳࠺ࡪ࠼ࡦ࠸࠶࠹࠼࠻࠿࠶ࡦ࠸࠺࠷࡫࠭ᚏ"),
        dict(l1lll11ll1_Krypto_=l1l1111_Krypto_ (u"ࠨ࠳࠹࠸ࡧ࠽ࡡ࠸ࡤࡩࡧ࡫࠾࠱࠺ࡧ࠵ࡩ࠸࠿࠵ࡧࡤࡨ࠻࠸ࡨ࠵࠷ࡧ࠳ࡥ࠸࠾࠷ࡣࡦ࠹࠸࠷࠸࠲ࡦ࠺࠶࠵࡫ࡪ࠶࠲࠲࠵࠻࠵ࡩࡤ࠸ࡧࡤ࠶࠺࠶࠵࠶࠶࠼࠻࠺࠾ࡢࡧ࠹࠸ࡧ࠵࠻ࡡ࠺࠻࠷ࡥ࠻ࡪ࠰࠴࠶ࡩ࠺࠺࡬࠸ࡧ࠲ࡨ࠺࡫ࡪࡣࡢࡧࡤࡦ࠶ࡧ࠳࠵ࡦ࠷ࡥ࠻ࡨ࠴ࡣ࠸࠶࠺ࡪ࠶࠷࠱ࡣ࠶࠼ࡧࡩࡥ࠸࠵࠺ࠫᚐ")),
        l1l1111_Krypto_ (u"ࠩࡕࡊࡈࠦ࠴࠷࠵࠷ࠤ࠽࠴࠴ࠡࡕࡋࡅ࠺࠷࠲ࠡࠪࡋࡑࡆࡉ࠭ࡔࡊࡄ࠹࠶࠸ࠩࠨᚑ")),
]
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    global l1ll11lllll_Krypto_
    from l111ll1_Krypto_.l1lll1ll1_Krypto_ import l11111ll1_Krypto_, l1llllllll_Krypto_, l1l111lll_Krypto_ as l1l1l1l1ll_Krypto_, l1lll1ll11_Krypto_
    from .common import l1l11l11lll_Krypto_
    l1l11l111l1_Krypto_ = dict(l1llllllll_Krypto_=l1llllllll_Krypto_, l1l1l1l1ll_Krypto_=l1l1l1l1ll_Krypto_, l1lll1ll11_Krypto_=l1lll1ll11_Krypto_, default=None)
    try:
        from l111ll1_Krypto_.l1lll1ll1_Krypto_ import l1lll1lll1_Krypto_, l1lll1l111_Krypto_, l1lll11ll1_Krypto_
        l1l11l111l1_Krypto_.update(dict(l1lll1lll1_Krypto_=l1lll1lll1_Krypto_, l1lll1l111_Krypto_=l1lll1l111_Krypto_, l1lll11ll1_Krypto_=l1lll11ll1_Krypto_))
        l1ll11lllll_Krypto_ += l1l111ll111_Krypto_
    except ImportError:
        import sys as l1l11l11_Krypto_
        l1l11l11_Krypto_.stderr.write(l1l1111_Krypto_ (u"ࠥࡗࡪࡲࡦࡕࡧࡶࡸ࠿ࠦࡷࡢࡴࡱ࡭ࡳ࡭࠺ࠡࡰࡲࡸࠥࡺࡥࡴࡶ࡬ࡲ࡬ࠦࡈࡎࡃࡆ࠱ࡘࡎࡁ࠳࠴࠷࠳࠸࠾࠴࠰࠷࠴࠶ࠥ࠮࡮ࡰࡶࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪ࠯࡜࡯ࠤᚒ"))
    return l1l11l11lll_Krypto_(l11111ll1_Krypto_, l1l1111_Krypto_ (u"ࠦࡍࡓࡁࡄࠤᚓ"), l1ll11lllll_Krypto_, l1l11l111l1_Krypto_)
if __name__ == l1l1111_Krypto_ (u"ࠬࡥ࡟࡮ࡣ࡬ࡲࡤࡥࠧᚔ"):
    import unittest as l1lll111111_Krypto_
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"࠭ࡳࡶ࡫ࡷࡩࠬᚕ"))