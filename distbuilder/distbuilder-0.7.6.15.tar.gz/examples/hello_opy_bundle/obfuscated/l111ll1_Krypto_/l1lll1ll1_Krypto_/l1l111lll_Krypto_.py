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
l1l1111_Krypto_ (u"ࠤࠥࠦࡘࡎࡁ࠮࠳ࠣࡧࡷࡿࡰࡵࡱࡪࡶࡦࡶࡨࡪࡥࠣ࡬ࡦࡹࡨࠡࡣ࡯࡫ࡴࡸࡩࡵࡪࡰ࠲ࠏࠐࡓࡉࡃ࠰࠵ࡤࠦࡰࡳࡱࡧࡹࡨ࡫ࡳࠡࡶ࡫ࡩࠥ࠷࠶࠱ࠢࡥ࡭ࡹࠦࡤࡪࡩࡨࡷࡹࠦ࡯ࡧࠢࡤࠤࡲ࡫ࡳࡴࡣࡪࡩ࠳ࠐࠊࠡࠢࠣࠤࡃࡄ࠾ࠡࡨࡵࡳࡲࠦࡃࡳࡻࡳࡸࡴ࠴ࡈࡢࡵ࡫ࠤ࡮ࡳࡰࡰࡴࡷࠤࡘࡎࡁࠋࠢࠣࠤࠥࡄ࠾࠿ࠌࠣࠤࠥࠦ࠾࠿ࡀࠣ࡬ࠥࡃࠠࡔࡊࡄ࠲ࡳ࡫ࡷࠩࠫࠍࠤࠥࠦࠠ࠿ࡀࡁࠤ࡭࠴ࡵࡱࡦࡤࡸࡪ࠮ࡢࠨࡊࡨࡰࡱࡵࠧࠪࠌࠣࠤࠥࠦ࠾࠿ࡀࠣࡴࡷ࡯࡮ࡵࠢ࡫࠲࡭࡫ࡸࡥ࡫ࡪࡩࡸࡺࠨࠪࠌࠍ࠮ࡘࡎࡁࠫࠢࡶࡸࡦࡴࡤࡴࠢࡩࡳࡷࠦࡓࡦࡥࡸࡶࡪࠦࡈࡢࡵ࡫ࠤࡆࡲࡧࡰࡴ࡬ࡸ࡭ࡳ࠮ࠋࠌࡗ࡬࡮ࡹࠠࡢ࡮ࡪࡳࡷ࡯ࡴࡩ࡯ࠣ࡭ࡸࠦ࡮ࡰࡶࠣࡧࡴࡴࡳࡪࡦࡨࡶࡪࡪࠠࡴࡧࡦࡹࡷ࡫࠮ࠡࡆࡲࠤࡳࡵࡴࠡࡷࡶࡩࠥ࡯ࡴࠡࡨࡲࡶࠥࡴࡥࡸࠢࡧࡩࡸ࡯ࡧ࡯ࡵ࠱ࠎࠏ࠴࠮ࠡࡡࡖࡌࡆ࠳࠱࠻ࠢ࡫ࡸࡹࡶ࠺࠰࠱ࡦࡷࡷࡩ࠮࡯࡫ࡶࡸ࠳࡭࡯ࡷ࠱ࡳࡹࡧࡲࡩࡤࡣࡷ࡭ࡴࡴࡳ࠰ࡨ࡬ࡴࡸ࠵ࡦࡪࡲࡶ࠵࠽࠶࠭࠳࠱ࡩ࡭ࡵࡹ࠱࠹࠲࠰࠶࠳ࡶࡤࡧࠌࠥࠦࠧࣉ")
_revision__ = l1l1111_Krypto_ (u"ࠥࠨࡎࡪࠤࠣ࣊")
__all__ = [l1l1111_Krypto_ (u"ࠫࡳ࡫ࡷࠨ࣋"), l1l1111_Krypto_ (u"ࠬࡪࡩࡨࡧࡶࡸࡤࡹࡩࡻࡧࠪ࣌"), l1l1111_Krypto_ (u"࠭ࡓࡉࡃ࠴ࡌࡦࡹࡨࠨ࣍") ]
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
from l111ll1_Krypto_.l1lll1ll1_Krypto_.l11111lll_Krypto_ import l1111l11l_Krypto_
try:
    import hashlib as l1llll1l1l_Krypto_
    l1111l1l1_Krypto_ = l1llll1l1l_Krypto_.sha1
except ImportError:
    from . import l1llll111l_Krypto_
    l1111l1l1_Krypto_ = l1llll111l_Krypto_
class l1llll1111_Krypto_(l1111l11l_Krypto_):
    l1l1111_Krypto_ (u"ࠢࠣࠤࡆࡰࡦࡹࡳࠡࡶ࡫ࡥࡹࠦࡩ࡮ࡲ࡯ࡩࡲ࡫࡮ࡵࡵࠣࡥ࡙ࠥࡈࡂ࠯࠴ࠤ࡭ࡧࡳࡩࠌࠣࠤࠥࠦࠊࠡࠢࠣࠤ࠿ࡻ࡮ࡥࡱࡦࡹࡲ࡫࡮ࡵࡧࡧ࠾ࠥࡨ࡬ࡰࡥ࡮ࡣࡸ࡯ࡺࡦࠌࠣࠤࠥࠦࠢࠣࠤ࣎")
    l1llllll11_Krypto_ = b(l1l1111_Krypto_ (u"ࠨ࡞ࡻ࠴࠻ࡢࡸ࠱࠷࡟ࡼ࠷ࡨ࡜ࡹ࠲ࡨࡠࡽ࠶࠳࡝ࡺ࠳࠶ࡡࡾ࠱ࡢ࣏ࠩ"))
    digest_size = 20
    block_size = 64
    def __init__(self, data=None):
        l1111l11l_Krypto_.__init__(self, l1111l1l1_Krypto_, data)
    def new(self, data=None):
        return l1llll1111_Krypto_(data)
def new(data=None):
    l1l1111_Krypto_ (u"ࠤࠥࠦࡗ࡫ࡴࡶࡴࡱࠤࡦࠦࡦࡳࡧࡶ࡬ࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࠠࡰࡨࠣࡸ࡭࡫ࠠࡩࡣࡶ࡬ࠥࡵࡢ࡫ࡧࡦࡸ࠳ࠐࠊࠡࠢࠣࠤ࠿ࡖࡡࡳࡣࡰࡩࡹ࡫ࡲࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࡨࡦࡺࡡࠡ࠼ࠣࡦࡾࡺࡥࠡࡵࡷࡶ࡮ࡴࡧࠋࠢࠣࠤࠥࠦࠠࠡࠢࡗ࡬ࡪࠦࡶࡦࡴࡼࠤ࡫࡯ࡲࡴࡶࠣࡧ࡭ࡻ࡮࡬ࠢࡲࡪࠥࡺࡨࡦࠢࡰࡩࡸࡹࡡࡨࡧࠣࡸࡴࠦࡨࡢࡵ࡫࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡉࡵࠢ࡬ࡷࠥ࡫ࡱࡶ࡫ࡹࡥࡱ࡫࡮ࡵࠢࡷࡳࠥࡧ࡮ࠡࡧࡤࡶࡱࡿࠠࡤࡣ࡯ࡰࠥࡺ࡯ࠡࡢࡖࡌࡆ࠷ࡈࡢࡵ࡫࠲ࡺࡶࡤࡢࡶࡨࠬ࠮ࡦ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡒࡴࡹ࡯࡯࡯ࡣ࡯࠲ࠏࠐࠠࠡࠢࠣ࠾ࡗ࡫ࡴࡶࡴࡱ࠾ࠥࡇࠠࡡࡕࡋࡅ࠶ࡎࡡࡴࡪࡣࠤࡴࡨࡪࡦࡥࡷࠎࠥࠦࠠࠡࠤ࣐ࠥࠦ")
    return l1llll1111_Krypto_().new(data)
digest_size = l1llll1111_Krypto_.digest_size
block_size = l1llll1111_Krypto_.block_size