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
l1l1111_Krypto_ (u"࡙ࠥࠦࠧࡈࡂ࠯࠵࠶࠹ࠦࡣࡳࡻࡳࡸࡴ࡭ࡲࡢࡲ࡫࡭ࡨࠦࡨࡢࡵ࡫ࠤࡦࡲࡧࡰࡴ࡬ࡸ࡭ࡳ࠮ࠋࠌࡖࡌࡆ࠳࠲࠳࠶ࠣࡦࡪࡲ࡯࡯ࡩࡶࠤࡹࡵࠠࡵࡪࡨࠤࡘࡎࡁ࠮࠴ࡢࠤ࡫ࡧ࡭ࡪ࡮ࡼࠤࡴ࡬ࠠࡤࡴࡼࡴࡹࡵࡧࡳࡣࡳ࡬࡮ࡩࠠࡩࡣࡶ࡬ࡪࡹ࠮ࠋࡋࡷࠤࡵࡸ࡯ࡥࡷࡦࡩࡸࠦࡴࡩࡧࠣ࠶࠷࠺ࠠࡣ࡫ࡷࠤࡩ࡯ࡧࡦࡵࡷࠤࡴ࡬ࠠࡢࠢࡰࡩࡸࡹࡡࡨࡧ࠱ࠎࠏࠦࠠࠡࠢࡁࡂࡃࠦࡦࡳࡱࡰࠤࡈࡸࡹࡱࡶࡲ࠲ࡍࡧࡳࡩࠢ࡬ࡱࡵࡵࡲࡵࠢࡖࡌࡆ࠸࠲࠵ࠌࠣࠤࠥࠦ࠾࠿ࡀࠍࠤࠥࠦࠠ࠿ࡀࡁࠤ࡭ࠦ࠽ࠡࡕࡋࡅ࠷࠸࠴࠯ࡰࡨࡻ࠭࠯ࠊࠡࠢࠣࠤࡃࡄ࠾ࠡࡪ࠱ࡹࡵࡪࡡࡵࡧࠫࡦࠬࡎࡥ࡭࡮ࡲࠫ࠮ࠐࠠࠡࠢࠣࡂࡃࡄࠠࡱࡴ࡬ࡲࡹࠦࡨ࠯ࡪࡨࡼࡩ࡯ࡧࡦࡵࡷࠬ࠮ࠐࠊࠫࡕࡋࡅ࠯ࠦࡳࡵࡣࡱࡨࡸࠦࡦࡰࡴࠣࡗࡪࡩࡵࡳࡧࠣࡌࡦࡹࡨࠡࡃ࡯࡫ࡴࡸࡩࡵࡪࡰ࠲ࠏࠐ࠮࠯ࠢࡢࡗࡍࡇ࠭࠳࠼ࠣ࡬ࡹࡺࡰ࠻࠱࠲ࡧࡸࡸࡣ࠯ࡰ࡬ࡷࡹ࠴ࡧࡰࡸ࠲ࡴࡺࡨ࡬ࡪࡥࡤࡸ࡮ࡵ࡮ࡴ࠱ࡩ࡭ࡵࡹ࠯ࡧ࡫ࡳࡷ࠶࠾࠰࠮࠴࠲ࡪ࡮ࡶࡳ࠲࠺࠳࠱࠷࠴ࡰࡥࡨࠍࠦࠧࠨ࣑")
_revision__ = l1l1111_Krypto_ (u"ࠦࠩࡏࡤࠥࠤ࣒")
__all__ = [l1l1111_Krypto_ (u"ࠬࡴࡥࡸ࣓ࠩ"), l1l1111_Krypto_ (u"࠭ࡤࡪࡩࡨࡷࡹࡥࡳࡪࡼࡨࠫࣔ"), l1l1111_Krypto_ (u"ࠧࡔࡊࡄ࠶࠷࠺ࡈࡢࡵ࡫ࠫࣕ") ]
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
from l111ll1_Krypto_.l1lll1ll1_Krypto_.l11111lll_Krypto_ import l1111l11l_Krypto_
try:
    import hashlib as l1llll1l1l_Krypto_
    l1111l1l1_Krypto_ = l1llll1l1l_Krypto_.sha224
except ImportError:
    from l111ll1_Krypto_.l1lll1ll1_Krypto_ import _1lll1ll1l_Krypto_
    l1111l1l1_Krypto_ = _1lll1ll1l_Krypto_
class l1lll1llll_Krypto_(l1111l11l_Krypto_):
    l1l1111_Krypto_ (u"ࠣࠤࠥࡇࡱࡧࡳࡴࠢࡷ࡬ࡦࡺࠠࡪ࡯ࡳࡰࡪࡳࡥ࡯ࡶࡶࠤࡦࠦࡓࡉࡃ࠰࠶࠷࠺ࠠࡩࡣࡶ࡬ࠏࠦࠠࠡࠢࠍࠤࠥࠦࠠ࠻ࡷࡱࡨࡴࡩࡵ࡮ࡧࡱࡸࡪࡪ࠺ࠡࡤ࡯ࡳࡨࡱ࡟ࡴ࡫ࡽࡩࠏࠦࠠࠡࠢࠥࠦࠧࣖ")
    l1llllll11_Krypto_ = b(l1l1111_Krypto_ (u"ࠩ࡟ࡼ࠵࠼࡜ࡹ࠲࠼ࡠࡽ࠼࠰࡝ࡺ࠻࠺ࡡࡾ࠴࠹࡞ࡻ࠴࠶ࡢࡸ࠷࠷࡟ࡼ࠵࠹࡜ࡹ࠲࠷ࡠࡽ࠶࠲࡝ࡺ࠳࠸ࠬࣗ"))
    digest_size = 28
    block_size = 64
    def __init__(self, data=None):
        l1111l11l_Krypto_.__init__(self, l1111l1l1_Krypto_, data)
    def new(self, data=None):
        return l1lll1llll_Krypto_(data)
def new(data=None):
    l1l1111_Krypto_ (u"ࠥࠦࠧࡘࡥࡵࡷࡵࡲࠥࡧࠠࡧࡴࡨࡷ࡭ࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࠡࡱࡩࠤࡹ࡮ࡥࠡࡪࡤࡷ࡭ࠦ࡯ࡣ࡬ࡨࡧࡹ࠴ࠊࠋࠢࠣࠤࠥࡀࡐࡢࡴࡤࡱࡪࡺࡥࡳࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࡩࡧࡴࡢࠢ࠽ࠤࡧࡿࡴࡦࠢࡶࡸࡷ࡯࡮ࡨࠌࠣࠤࠥࠦࠠࠡࠢࠣࡘ࡭࡫ࠠࡷࡧࡵࡽࠥ࡬ࡩࡳࡵࡷࠤࡨ࡮ࡵ࡯࡭ࠣࡳ࡫ࠦࡴࡩࡧࠣࡱࡪࡹࡳࡢࡩࡨࠤࡹࡵࠠࡩࡣࡶ࡬࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡊࡶࠣ࡭ࡸࠦࡥࡲࡷ࡬ࡺࡦࡲࡥ࡯ࡶࠣࡸࡴࠦࡡ࡯ࠢࡨࡥࡷࡲࡹࠡࡥࡤࡰࡱࠦࡴࡰࠢࡣࡗࡍࡇ࠲࠳࠶ࡋࡥࡸ࡮࠮ࡶࡲࡧࡥࡹ࡫ࠨࠪࡢ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡕࡰࡵ࡫ࡲࡲࡦࡲ࠮ࠋࠌࠣࠤࠥࠦ࠺ࡓࡧࡷࡹࡷࡴ࠺ࠡࡃࠣࡤࡘࡎࡁ࠳࠴࠷ࡌࡦࡹࡨࡡࠢࡲࡦ࡯࡫ࡣࡵࠌࠣࠤࠥࠦࠢࠣࠤࣘ")
    return l1lll1llll_Krypto_().new(data)
digest_size = l1lll1llll_Krypto_.digest_size
block_size = l1lll1llll_Krypto_.block_size