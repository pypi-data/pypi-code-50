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
l1l1111_Krypto_ (u"ࠧࠨࠢࡔࡊࡄ࠱࠸࠾࠴ࠡࡥࡵࡽࡵࡺ࡯ࡨࡴࡤࡴ࡭࡯ࡣࠡࡪࡤࡷ࡭ࠦࡡ࡭ࡩࡲࡶ࡮ࡺࡨ࡮࠰ࠍࠎࡘࡎࡁ࠮࠵࠻࠸ࠥࡨࡥ࡭ࡱࡱ࡫ࡸࠦࡴࡰࠢࡷ࡬ࡪࠦࡓࡉࡃ࠰࠶ࡤࠦࡦࡢ࡯࡬ࡰࡾࠦ࡯ࡧࠢࡦࡶࡾࡶࡴࡰࡩࡵࡥࡵ࡮ࡩࡤࠢ࡫ࡥࡸ࡮ࡥࡴ࠰ࠍࡍࡹࠦࡰࡳࡱࡧࡹࡨ࡫ࡳࠡࡶ࡫ࡩࠥ࠹࠸࠵ࠢࡥ࡭ࡹࠦࡤࡪࡩࡨࡷࡹࠦ࡯ࡧࠢࡤࠤࡲ࡫ࡳࡴࡣࡪࡩ࠳ࠐࠊࠡࠢࠣࠤࡃࡄ࠾ࠡࡨࡵࡳࡲࠦࡃࡳࡻࡳࡸࡴ࠴ࡈࡢࡵ࡫ࠤ࡮ࡳࡰࡰࡴࡷࠤࡘࡎࡁ࠴࠺࠷ࠎࠥࠦࠠࠡࡀࡁࡂࠏࠦࠠࠡࠢࡁࡂࡃࠦࡨࠡ࠿ࠣࡗࡍࡇ࠳࠹࠶࠱ࡲࡪࡽࠨࠪࠌࠣࠤࠥࠦ࠾࠿ࡀࠣ࡬࠳ࡻࡰࡥࡣࡷࡩ࠭ࡨࠧࡉࡧ࡯ࡰࡴ࠭ࠩࠋࠢࠣࠤࠥࡄ࠾࠿ࠢࡳࡶ࡮ࡴࡴࠡࡪ࠱࡬ࡪࡾࡤࡪࡩࡨࡷࡹ࠮ࠩࠋࠌ࠭ࡗࡍࡇࠪࠡࡵࡷࡥࡳࡪࡳࠡࡨࡲࡶ࡙ࠥࡥࡤࡷࡵࡩࠥࡎࡡࡴࡪࠣࡅࡱ࡭࡯ࡳ࡫ࡷ࡬ࡲ࠴ࠊࠋ࠰࠱ࠤࡤ࡙ࡈࡂ࠯࠵࠾ࠥ࡮ࡴࡵࡲ࠽࠳࠴ࡩࡳࡳࡥ࠱ࡲ࡮ࡹࡴ࠯ࡩࡲࡺ࠴ࡶࡵࡣ࡮࡬ࡧࡦࡺࡩࡰࡰࡶ࠳࡫࡯ࡰࡴ࠱ࡩ࡭ࡵࡹ࠱࠹࠲࠰࠶࠴࡬ࡩࡱࡵ࠴࠼࠵࠳࠲࠯ࡲࡧࡪࠏࠨࠢࠣ࣡")
_revision__ = l1l1111_Krypto_ (u"ࠨࠤࡊࡦࠧࠦ࣢")
__all__ = [l1l1111_Krypto_ (u"ࠧ࡯ࡧࡺࣣࠫ"), l1l1111_Krypto_ (u"ࠨࡦ࡬࡫ࡪࡹࡴࡠࡵ࡬ࡾࡪ࠭ࣤ"), l1l1111_Krypto_ (u"ࠩࡖࡌࡆ࠹࠸࠵ࡊࡤࡷ࡭࠭ࣥ") ]
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
from l111ll1_Krypto_.l1lll1ll1_Krypto_.l11111lll_Krypto_ import l1111l11l_Krypto_
try:
    import hashlib as l1llll1l1l_Krypto_
    l1111l1l1_Krypto_ = l1llll1l1l_Krypto_.sha384
except ImportError:
    from l111ll1_Krypto_.l1lll1ll1_Krypto_ import _1lll11lll_Krypto_
    l1111l1l1_Krypto_ = _1lll11lll_Krypto_
class l1lll1l11l_Krypto_(l1111l11l_Krypto_):
    l1l1111_Krypto_ (u"ࠥࠦࠧࡉ࡬ࡢࡵࡶࠤࡹ࡮ࡡࡵࠢ࡬ࡱࡵࡲࡥ࡮ࡧࡱࡸࡸࠦࡡࠡࡕࡋࡅ࠲࠹࠸࠵ࠢ࡫ࡥࡸ࡮ࠊࠡࠢࠣࠤࠏࠦࠠࠡࠢ࠽ࡹࡳࡪ࡯ࡤࡷࡰࡩࡳࡺࡥࡥ࠼ࠣࡦࡱࡵࡣ࡬ࡡࡶ࡭ࡿ࡫ࠊࠡࠢࠣࠤࠧࠨࣦࠢ")
    l1llllll11_Krypto_ = b(l1l1111_Krypto_ (u"ࠫࡡࡾ࠰࠷࡞ࡻ࠴࠾ࡢࡸ࠷࠲࡟ࡼ࠽࠼࡜ࡹ࠶࠻ࡠࡽ࠶࠱࡝ࡺ࠹࠹ࡡࡾ࠰࠴࡞ࡻ࠴࠹ࡢࡸ࠱࠴࡟ࡼ࠵࠸ࠧࣧ"))
    digest_size = 48
    block_size = 128
    def __init__(self, data=None):
        l1111l11l_Krypto_.__init__(self, l1111l1l1_Krypto_, data)
    def new(self, data=None):
        return l1lll1l11l_Krypto_(data)
def new(data=None):
    l1l1111_Krypto_ (u"ࠧࠨࠢࡓࡧࡷࡹࡷࡴࠠࡢࠢࡩࡶࡪࡹࡨࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠣࡳ࡫ࠦࡴࡩࡧࠣ࡬ࡦࡹࡨࠡࡱࡥ࡮ࡪࡩࡴ࠯ࠌࠍࠤࠥࠦࠠ࠻ࡒࡤࡶࡦࡳࡥࡵࡧࡵࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࡤࡢࡶࡤࠤ࠿ࠦࡢࡺࡶࡨࠤࡸࡺࡲࡪࡰࡪࠎࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࡨࡦࠢࡹࡩࡷࡿࠠࡧ࡫ࡵࡷࡹࠦࡣࡩࡷࡱ࡯ࠥࡵࡦࠡࡶ࡫ࡩࠥࡳࡥࡴࡵࡤ࡫ࡪࠦࡴࡰࠢ࡫ࡥࡸ࡮࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡌࡸࠥ࡯ࡳࠡࡧࡴࡹ࡮ࡼࡡ࡭ࡧࡱࡸࠥࡺ࡯ࠡࡣࡱࠤࡪࡧࡲ࡭ࡻࠣࡧࡦࡲ࡬ࠡࡶࡲࠤࡥ࡙ࡈࡂ࠵࠻࠸ࡍࡧࡳࡩ࠰ࡸࡴࡩࡧࡴࡦࠪࠬࡤ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡐࡲࡷ࡭ࡴࡴࡡ࡭࠰ࠍࠎࠥࠦࠠࠡ࠼ࡕࡩࡹࡻࡲ࡯࠼ࠣࡅࠥࡦࡓࡉࡃ࠶࠼࠹ࡎࡡࡴࡪࡣࠤࡴࡨࡪࡦࡥࡷࠎࠥࠦࠠࠡࠤࠥࠦࣨ")
    return l1lll1l11l_Krypto_().new(data)
digest_size = l1lll1l11l_Krypto_.digest_size
block_size = l1lll1l11l_Krypto_.block_size