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
l1l1111_Krypto_ (u"ࠨࠢࠣࡏࡇ࠸ࠥࡩࡲࡺࡲࡷࡳ࡬ࡸࡡࡱࡪ࡬ࡧࠥ࡮ࡡࡴࡪࠣࡥࡱ࡭࡯ࡳ࡫ࡷ࡬ࡲ࠴ࠊࠋࡏࡇ࠸ࠥ࡯ࡳࠡࡵࡳࡩࡨ࡯ࡦࡪࡧࡧࠤ࡮ࡴࠠࡓࡈࡆ࠵࠸࠸࠰ࡠࠢࡤࡲࡩࠦࡰࡳࡱࡧࡹࡨ࡫ࡳࠡࡶ࡫ࡩࠥ࠷࠲࠹ࠢࡥ࡭ࡹࠦࡤࡪࡩࡨࡷࡹࠦ࡯ࡧࠢࡤࠤࡲ࡫ࡳࡴࡣࡪࡩ࠳ࠐࠊࠡࠢࠣࠤࡃࡄ࠾ࠡࡨࡵࡳࡲࠦࡃࡳࡻࡳࡸࡴ࠴ࡈࡢࡵ࡫ࠤ࡮ࡳࡰࡰࡴࡷࠤࡒࡊ࠴ࠋࠢࠣࠤࠥࡄ࠾࠿ࠌࠣࠤࠥࠦ࠾࠿ࡀࠣ࡬ࠥࡃࠠࡎࡆ࠷࠲ࡳ࡫ࡷࠩࠫࠍࠤࠥࠦࠠ࠿ࡀࡁࠤ࡭࠴ࡵࡱࡦࡤࡸࡪ࠮ࡢࠨࡊࡨࡰࡱࡵࠧࠪࠌࠣࠤࠥࠦ࠾࠿ࡀࠣࡴࡷ࡯࡮ࡵࠢ࡫࠲࡭࡫ࡸࡥ࡫ࡪࡩࡸࡺࠨࠪࠌࠍࡑࡉ࠺ࠠࡴࡶࡤࡲࡩࠦࡦࡰࡴࠣࡑࡪࡹࡳࡢࡩࡨࠤࡉ࡯ࡧࡦࡵࡷࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥ࠺ࠬࠡࡣࡱࡨࠥ࡯ࡴࠡࡹࡤࡷࠥ࡯࡮ࡷࡧࡱࡸࡪࡪࠠࡣࡻࠣࡖ࡮ࡼࡥࡴࡶࠣ࡭ࡳࠦ࠱࠺࠻࠳࠲ࠏࠐࡔࡩ࡫ࡶࠤࡦࡲࡧࡰࡴ࡬ࡸ࡭ࡳࠠࡪࡵࠣ࡭ࡳࡹࡥࡤࡷࡵࡩ࠳ࠦࡄࡰࠢࡱࡳࡹࠦࡵࡴࡧࠣ࡭ࡹࠦࡦࡰࡴࠣࡲࡪࡽࠠࡥࡧࡶ࡭࡬ࡴࡳ࠯ࠌࠍ࠲࠳ࠦ࡟ࡓࡈࡆ࠵࠸࠸࠰࠻ࠢ࡫ࡸࡹࡶ࠺࠰࠱ࡷࡳࡴࡲࡳ࠯࡫ࡨࡸ࡫࠴࡯ࡳࡩ࠲࡬ࡹࡳ࡬࠰ࡴࡩࡧ࠶࠹࠲࠱ࠌࠥࠦࠧࢱ")
_revision__ = l1l1111_Krypto_ (u"ࠢࠥࡋࡧࠨࠧࢲ")
__all__ = [l1l1111_Krypto_ (u"ࠨࡰࡨࡻࠬࢳ"), l1l1111_Krypto_ (u"ࠩࡧ࡭࡬࡫ࡳࡵࡡࡶ࡭ࡿ࡫ࠧࢴ"), l1l1111_Krypto_ (u"ࠪࡑࡉ࠺ࡈࡢࡵ࡫ࠫࢵ") ]
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
from l111ll1_Krypto_.l1lll1ll1_Krypto_.l11111lll_Krypto_ import l1111l11l_Krypto_
import l111ll1_Krypto_.l1lll1ll1_Krypto_._1lllll11l_Krypto_ as _1lllll11l_Krypto_
l1111l1l1_Krypto_ = _1lllll11l_Krypto_
class l1lllll111_Krypto_(l1111l11l_Krypto_):
    l1l1111_Krypto_ (u"ࠦࠧࠨࡃ࡭ࡣࡶࡷࠥࡺࡨࡢࡶࠣ࡭ࡲࡶ࡬ࡦ࡯ࡨࡲࡹࡹࠠࡢࡰࠣࡑࡉ࠺ࠠࡩࡣࡶ࡬ࠏࠦࠠࠡࠢࠍࠤࠥࠦࠠ࠻ࡷࡱࡨࡴࡩࡵ࡮ࡧࡱࡸࡪࡪ࠺ࠡࡤ࡯ࡳࡨࡱ࡟ࡴ࡫ࡽࡩࠏࠦࠠࠡࠢࠥࠦࠧࢶ")
    l1llllll11_Krypto_ = b(l1l1111_Krypto_ (u"ࠬࡢࡸ࠱࠸࡟ࡼ࠵࠾࡜ࡹ࠴ࡤࡠࡽ࠾࠶࡝ࡺ࠷࠼ࡡࡾ࠸࠷࡞ࡻࡪ࠼ࡢࡸ࠱ࡦ࡟ࡼ࠵࠸࡜ࡹ࠲࠷ࠫࢷ"))
    digest_size = 16
    block_size = 64
    def __init__(self, data=None):
        l1111l11l_Krypto_.__init__(self, l1111l1l1_Krypto_, data)
    def new(self, data=None):
        return l1lllll111_Krypto_(data)
def new(data=None):
    l1l1111_Krypto_ (u"ࠨࠢࠣࡔࡨࡸࡺࡸ࡮ࠡࡣࠣࡪࡷ࡫ࡳࡩࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠤࡴ࡬ࠠࡵࡪࡨࠤ࡭ࡧࡳࡩࠢࡲࡦ࡯࡫ࡣࡵ࠰ࠍࠎࠥࠦࠠࠡ࠼ࡓࡥࡷࡧ࡭ࡦࡶࡨࡶࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࡥࡣࡷࡥࠥࡀࠠࡣࡻࡷࡩࠥࡹࡴࡳ࡫ࡱ࡫ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡔࡩࡧࠣࡺࡪࡸࡹࠡࡨ࡬ࡶࡸࡺࠠࡤࡪࡸࡲࡰࠦ࡯ࡧࠢࡷ࡬ࡪࠦ࡭ࡦࡵࡶࡥ࡬࡫ࠠࡵࡱࠣ࡬ࡦࡹࡨ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡍࡹࠦࡩࡴࠢࡨࡵࡺ࡯ࡶࡢ࡮ࡨࡲࡹࠦࡴࡰࠢࡤࡲࠥ࡫ࡡࡳ࡮ࡼࠤࡨࡧ࡬࡭ࠢࡷࡳࠥࡦࡍࡅ࠶ࡋࡥࡸ࡮࠮ࡶࡲࡧࡥࡹ࡫ࠨࠪࡢ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡕࡰࡵ࡫ࡲࡲࡦࡲ࠮ࠋࠌࠣࠤࠥࠦ࠺ࡓࡧࡷࡹࡷࡴ࠺ࠡࡃࠣࡤࡒࡊ࠴ࡉࡣࡶ࡬ࡥࠦ࡯ࡣ࡬ࡨࡧࡹࠐࠠࠡࠢࠣࠦࠧࠨࢸ")
    return l1lllll111_Krypto_().new(data)
digest_size = l1lllll111_Krypto_.digest_size
block_size = l1lllll111_Krypto_.block_size