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
l1l1111_Krypto_ (u"ࠨࠢࠣࡕࡋࡅ࠲࠻࠱࠳ࠢࡦࡶࡾࡶࡴࡰࡩࡵࡥࡵ࡮ࡩࡤࠢ࡫ࡥࡸ࡮ࠠࡢ࡮ࡪࡳࡷ࡯ࡴࡩ࡯࠱ࠎࠏ࡙ࡈࡂ࠯࠸࠵࠷ࠦࡢࡦ࡮ࡲࡲ࡬ࡹࠠࡵࡱࠣࡸ࡭࡫ࠠࡔࡊࡄ࠱࠷ࡥࠠࡧࡣࡰ࡭ࡱࡿࠠࡰࡨࠣࡧࡷࡿࡰࡵࡱࡪࡶࡦࡶࡨࡪࡥࠣ࡬ࡦࡹࡨࡦࡵ࠱ࠎࡎࡺࠠࡱࡴࡲࡨࡺࡩࡥࡴࠢࡷ࡬ࡪࠦ࠵࠲࠴ࠣࡦ࡮ࡺࠠࡥ࡫ࡪࡩࡸࡺࠠࡰࡨࠣࡥࠥࡳࡥࡴࡵࡤ࡫ࡪ࠴ࠊࠋࠢࠣࠤࠥࡄ࠾࠿ࠢࡩࡶࡴࡳࠠࡄࡴࡼࡴࡹࡵ࠮ࡉࡣࡶ࡬ࠥ࡯࡭ࡱࡱࡵࡸ࡙ࠥࡈࡂ࠷࠴࠶ࠏࠦࠠࠡࠢࡁࡂࡃࠐࠠࠡࠢࠣࡂࡃࡄࠠࡩࠢࡀࠤࡘࡎࡁ࠶࠳࠵࠲ࡳ࡫ࡷࠩࠫࠍࠤࠥࠦࠠ࠿ࡀࡁࠤ࡭࠴ࡵࡱࡦࡤࡸࡪ࠮ࡢࠨࡊࡨࡰࡱࡵࠧࠪࠌࠣࠤࠥࠦ࠾࠿ࡀࠣࡴࡷ࡯࡮ࡵࠢ࡫࠲࡭࡫ࡸࡥ࡫ࡪࡩࡸࡺࠨࠪࠌࠍ࠮ࡘࡎࡁࠫࠢࡶࡸࡦࡴࡤࡴࠢࡩࡳࡷࠦࡓࡦࡥࡸࡶࡪࠦࡈࡢࡵ࡫ࠤࡆࡲࡧࡰࡴ࡬ࡸ࡭ࡳ࠮ࠋࠌ࠱࠲ࠥࡥࡓࡉࡃ࠰࠶࠿ࠦࡨࡵࡶࡳ࠾࠴࠵ࡣࡴࡴࡦ࠲ࡳ࡯ࡳࡵ࠰ࡪࡳࡻ࠵ࡰࡶࡤ࡯࡭ࡨࡧࡴࡪࡱࡱࡷ࠴࡬ࡩࡱࡵ࠲ࡪ࡮ࡶࡳ࠲࠺࠳࠱࠷࠵ࡦࡪࡲࡶ࠵࠽࠶࠭࠳࠰ࡳࡨ࡫ࠐࠢࠣࠤࣩ")
_revision__ = l1l1111_Krypto_ (u"ࠢࠥࡋࡧࠨࠧ࣪")
__all__ = [l1l1111_Krypto_ (u"ࠨࡰࡨࡻࠬ࣫"), l1l1111_Krypto_ (u"ࠩࡧ࡭࡬࡫ࡳࡵࡡࡶ࡭ࡿ࡫ࠧ࣬"), l1l1111_Krypto_ (u"ࠪࡗࡍࡇ࠵࠲࠴ࡋࡥࡸ࡮࣭ࠧ") ]
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
from l111ll1_Krypto_.l1lll1ll1_Krypto_.l11111lll_Krypto_ import l1111l11l_Krypto_
try:
    import hashlib as l1llll1l1l_Krypto_
    l1111l1l1_Krypto_ = l1llll1l1l_Krypto_.sha512
except ImportError:
    from l111ll1_Krypto_.l1lll1ll1_Krypto_ import _1lll11l11_Krypto_
    l1111l1l1_Krypto_ = _1lll11l11_Krypto_
class l1lll11l1l_Krypto_(l1111l11l_Krypto_):
    l1l1111_Krypto_ (u"ࠦࠧࠨࡃ࡭ࡣࡶࡷࠥࡺࡨࡢࡶࠣ࡭ࡲࡶ࡬ࡦ࡯ࡨࡲࡹࡹࠠࡢࠢࡖࡌࡆ࠳࠵࠲࠴ࠣ࡬ࡦࡹࡨࠋࠢࠣࠤࠥࠐࠠࠡࠢࠣ࠾ࡺࡴࡤࡰࡥࡸࡱࡪࡴࡴࡦࡦ࠽ࠤࡧࡲ࡯ࡤ࡭ࡢࡷ࡮ࢀࡥࠋࠢࠣࠤࠥࠨ࣮ࠢࠣ")
    l1llllll11_Krypto_ = b(l1l1111_Krypto_ (u"ࠬࡢࡸ࠱࠸࡟ࡼ࠵࠿࡜ࡹ࠸࠳ࡠࡽ࠾࠶࡝ࡺ࠷࠼ࡡࡾ࠰࠲࡞ࡻ࠺࠺ࡢࡸ࠱࠵࡟ࡼ࠵࠺࡜ࡹ࠲࠵ࡠࡽ࠶࠳ࠨ࣯"))
    digest_size = 64
    block_size = 128
    def __init__(self, data=None):
        l1111l11l_Krypto_.__init__(self, l1111l1l1_Krypto_, data)
    def new(self, data=None):
        return l1lll11l1l_Krypto_(data)
def new(data=None):
    l1l1111_Krypto_ (u"ࠨࠢࠣࡔࡨࡸࡺࡸ࡮ࠡࡣࠣࡪࡷ࡫ࡳࡩࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠤࡴ࡬ࠠࡵࡪࡨࠤ࡭ࡧࡳࡩࠢࡲࡦ࡯࡫ࡣࡵ࠰ࠍࠎࠥࠦࠠࠡ࠼ࡓࡥࡷࡧ࡭ࡦࡶࡨࡶࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࡥࡣࡷࡥࠥࡀࠠࡣࡻࡷࡩࠥࡹࡴࡳ࡫ࡱ࡫ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡔࡩࡧࠣࡺࡪࡸࡹࠡࡨ࡬ࡶࡸࡺࠠࡤࡪࡸࡲࡰࠦ࡯ࡧࠢࡷ࡬ࡪࠦ࡭ࡦࡵࡶࡥ࡬࡫ࠠࡵࡱࠣ࡬ࡦࡹࡨ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡍࡹࠦࡩࡴࠢࡨࡵࡺ࡯ࡶࡢ࡮ࡨࡲࡹࠦࡴࡰࠢࡤࡲࠥ࡫ࡡࡳ࡮ࡼࠤࡨࡧ࡬࡭ࠢࡷࡳࠥࡦࡓࡉࡃ࠸࠵࠷ࡎࡡࡴࡪ࠱ࡹࡵࡪࡡࡵࡧࠫ࠭ࡥ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡑࡳࡸ࡮ࡵ࡮ࡢ࡮࠱ࠎࠏࠦࠠࠡࠢ࠽ࡖࡪࡺࡵࡳࡰ࠽ࠤࡆࠦࡠࡔࡊࡄ࠹࠶࠸ࡈࡢࡵ࡫ࡤࠥࡵࡢ࡫ࡧࡦࡸࠏࣰࠦࠠࠡࠢࠥࠦࠧ")
    return l1lll11l1l_Krypto_().new(data)
digest_size = l1lll11l1l_Krypto_.digest_size
block_size = l1lll11l1l_Krypto_.block_size