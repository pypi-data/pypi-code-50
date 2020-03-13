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
l1l1111_Krypto_ (u"ࠦࠧࠨࡓࡉࡃ࠰࠶࠺࠼ࠠࡤࡴࡼࡴࡹࡵࡧࡳࡣࡳ࡬࡮ࡩࠠࡩࡣࡶ࡬ࠥࡧ࡬ࡨࡱࡵ࡭ࡹ࡮࡭࠯ࠌࠍࡗࡍࡇ࠭࠳࠷࠹ࠤࡧ࡫࡬ࡰࡰࡪࡷࠥࡺ࡯ࠡࡶ࡫ࡩ࡙ࠥࡈࡂ࠯࠵ࡣࠥ࡬ࡡ࡮࡫࡯ࡽࠥࡵࡦࠡࡥࡵࡽࡵࡺ࡯ࡨࡴࡤࡴ࡭࡯ࡣࠡࡪࡤࡷ࡭࡫ࡳ࠯ࠌࡌࡸࠥࡶࡲࡰࡦࡸࡧࡪࡹࠠࡵࡪࡨࠤ࠷࠻࠶ࠡࡤ࡬ࡸࠥࡪࡩࡨࡧࡶࡸࠥࡵࡦࠡࡣࠣࡱࡪࡹࡳࡢࡩࡨ࠲ࠏࠐࠠࠡࠢࠣࡂࡃࡄࠠࡧࡴࡲࡱࠥࡉࡲࡺࡲࡷࡳ࠳ࡎࡡࡴࡪࠣ࡭ࡲࡶ࡯ࡳࡶࠣࡗࡍࡇ࠲࠶࠸ࠍࠤࠥࠦࠠ࠿ࡀࡁࠎࠥࠦࠠࠡࡀࡁࡂࠥ࡮ࠠ࠾ࠢࡖࡌࡆ࠸࠵࠷࠰ࡱࡩࡼ࠮ࠩࠋࠢࠣࠤࠥࡄ࠾࠿ࠢ࡫࠲ࡺࡶࡤࡢࡶࡨࠬࡧ࠭ࡈࡦ࡮࡯ࡳࠬ࠯ࠊࠡࠢࠣࠤࡃࡄ࠾ࠡࡲࡵ࡭ࡳࡺࠠࡩ࠰࡫ࡩࡽࡪࡩࡨࡧࡶࡸ࠭࠯ࠊࠋࠬࡖࡌࡆ࠰ࠠࡴࡶࡤࡲࡩࡹࠠࡧࡱࡵࠤࡘ࡫ࡣࡶࡴࡨࠤࡍࡧࡳࡩࠢࡄࡰ࡬ࡵࡲࡪࡶ࡫ࡱ࠳ࠐࠊ࠯࠰ࠣࡣࡘࡎࡁ࠮࠴࠽ࠤ࡭ࡺࡴࡱ࠼࠲࠳ࡨࡹࡲࡤ࠰ࡱ࡭ࡸࡺ࠮ࡨࡱࡹ࠳ࡵࡻࡢ࡭࡫ࡦࡥࡹ࡯࡯࡯ࡵ࠲ࡪ࡮ࡶࡳ࠰ࡨ࡬ࡴࡸ࠷࠸࠱࠯࠵࠳࡫࡯ࡰࡴ࠳࠻࠴࠲࠸࠮ࡱࡦࡩࠎࠧࠨࠢࣙ")
_revision__ = l1l1111_Krypto_ (u"ࠧࠪࡉࡥࠦࠥࣚ")
__all__ = [l1l1111_Krypto_ (u"࠭࡮ࡦࡹࠪࣛ"), l1l1111_Krypto_ (u"ࠧࡥ࡫ࡪࡩࡸࡺ࡟ࡴ࡫ࡽࡩࠬࣜ"), l1l1111_Krypto_ (u"ࠨࡕࡋࡅ࠷࠻࠶ࡉࡣࡶ࡬ࠬࣝ") ]
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
from l111ll1_Krypto_.l1lll1ll1_Krypto_.l11111lll_Krypto_ import l1111l11l_Krypto_
try:
    import hashlib as l1llll1l1l_Krypto_
    l1111l1l1_Krypto_ = l1llll1l1l_Krypto_.sha256
except ImportError:
    from l111ll1_Krypto_.l1lll1ll1_Krypto_ import _1lll1l1ll_Krypto_
    l1111l1l1_Krypto_ = _1lll1l1ll_Krypto_
class l1lll1l1l1_Krypto_(l1111l11l_Krypto_):
    l1l1111_Krypto_ (u"ࠤࠥࠦࡈࡲࡡࡴࡵࠣࡸ࡭ࡧࡴࠡ࡫ࡰࡴࡱ࡫࡭ࡦࡰࡷࡷࠥࡧࠠࡔࡊࡄ࠱࠷࠻࠶ࠡࡪࡤࡷ࡭ࠐࠠࠡࠢࠣࠎࠥࠦࠠࠡ࠼ࡸࡲࡩࡵࡣࡶ࡯ࡨࡲࡹ࡫ࡤ࠻ࠢࡥࡰࡴࡩ࡫ࡠࡵ࡬ࡾࡪࠐࠠࠡࠢࠣࠦࠧࠨࣞ")
    l1llllll11_Krypto_ = b(l1l1111_Krypto_ (u"ࠪࡠࡽ࠶࠶࡝ࡺ࠳࠽ࡡࡾ࠶࠱࡞ࡻ࠼࠻ࡢࡸ࠵࠺࡟ࡼ࠵࠷࡜ࡹ࠸࠸ࡠࡽ࠶࠳࡝ࡺ࠳࠸ࡡࡾ࠰࠳࡞ࡻ࠴࠶࠭ࣟ"))
    digest_size = 32
    block_size = 64
    def __init__(self, data=None):
        l1111l11l_Krypto_.__init__(self, l1111l1l1_Krypto_, data)
    def new(self, data=None):
        return l1lll1l1l1_Krypto_(data)
def new(data=None):
    l1l1111_Krypto_ (u"ࠦࠧࠨࡒࡦࡶࡸࡶࡳࠦࡡࠡࡨࡵࡩࡸ࡮ࠠࡪࡰࡶࡸࡦࡴࡣࡦࠢࡲࡪࠥࡺࡨࡦࠢ࡫ࡥࡸ࡮ࠠࡰࡤ࡭ࡩࡨࡺ࠮ࠋࠌࠣࠤࠥࠦ࠺ࡑࡣࡵࡥࡲ࡫ࡴࡦࡴࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࡪࡡࡵࡣࠣ࠾ࠥࡨࡹࡵࡧࠣࡷࡹࡸࡩ࡯ࡩࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡙࡮ࡥࠡࡸࡨࡶࡾࠦࡦࡪࡴࡶࡸࠥࡩࡨࡶࡰ࡮ࠤࡴ࡬ࠠࡵࡪࡨࠤࡲ࡫ࡳࡴࡣࡪࡩࠥࡺ࡯ࠡࡪࡤࡷ࡭࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡋࡷࠤ࡮ࡹࠠࡦࡳࡸ࡭ࡻࡧ࡬ࡦࡰࡷࠤࡹࡵࠠࡢࡰࠣࡩࡦࡸ࡬ࡺࠢࡦࡥࡱࡲࠠࡵࡱࠣࡤࡘࡎࡁ࠳࠷࠹ࡌࡦࡹࡨ࠯ࡷࡳࡨࡦࡺࡥࠩࠫࡣ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡏࡱࡶ࡬ࡳࡳࡧ࡬࠯ࠌࠍࠤࠥࠦࠠ࠻ࡔࡨࡸࡺࡸ࡮࠻ࠢࡄࠤࡥ࡙ࡈࡂ࠴࠸࠺ࡍࡧࡳࡩࡢࠣࡳࡧࡰࡥࡤࡶࠍࠤࠥࠦࠠࠣࠤࠥ࣠")
    return l1lll1l1l1_Krypto_().new(data)
digest_size = l1lll1l1l1_Krypto_.digest_size
block_size = l1lll1l1l1_Krypto_.block_size