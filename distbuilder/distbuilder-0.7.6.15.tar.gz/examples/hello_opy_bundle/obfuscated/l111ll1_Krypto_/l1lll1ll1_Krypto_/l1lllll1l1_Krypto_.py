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
l1l1111_Krypto_ (u"ࠧࠨࠢࡎࡆ࠵ࠤࡨࡸࡹࡱࡶࡲ࡫ࡷࡧࡰࡩ࡫ࡦࠤ࡭ࡧࡳࡩࠢࡤࡰ࡬ࡵࡲࡪࡶ࡫ࡱ࠳ࠐࠊࡎࡆ࠵ࠤ࡮ࡹࠠࡴࡲࡨࡧ࡮࡬ࡩࡦࡦࠣ࡭ࡳࠦࡒࡇࡅ࠴࠷࠶࠿࡟ࠡࡣࡱࡨࠥ࡯ࡴࠡࡲࡵࡳࡩࡻࡣࡦࡵࠣࡸ࡭࡫ࠠ࠲࠴࠻ࠤࡧ࡯ࡴࠡࡦ࡬࡫ࡪࡹࡴࠡࡱࡩࠤࡦࠦ࡭ࡦࡵࡶࡥ࡬࡫࠮ࠋࠌࠣࠤࠥࠦ࠾࠿ࡀࠣࡪࡷࡵ࡭ࠡࡅࡵࡽࡵࡺ࡯࠯ࡊࡤࡷ࡭ࠦࡩ࡮ࡲࡲࡶࡹࠦࡍࡅ࠴ࠍࠤࠥࠦࠠ࠿ࡀࡁࠎࠥࠦࠠࠡࡀࡁࡂࠥ࡮ࠠ࠾ࠢࡐࡈ࠷࠴࡮ࡦࡹࠫ࠭ࠏࠦࠠࠡࠢࡁࡂࡃࠦࡨ࠯ࡷࡳࡨࡦࡺࡥࠩࡤࠪࡌࡪࡲ࡬ࡰࠩࠬࠎࠥࠦࠠࠡࡀࡁࡂࠥࡶࡲࡪࡰࡷࠤ࡭࠴ࡨࡦࡺࡧ࡭࡬࡫ࡳࡵࠪࠬࠎࠏࡓࡄ࠳ࠢࡶࡸࡦࡴࡤࠡࡨࡲࡶࠥࡓࡥࡴࡵࡤ࡫ࡪࠦࡄࡪࡩࡨࡷࡹࠦࡶࡦࡴࡶ࡭ࡴࡴࠠ࠳࠮ࠣࡥࡳࡪࠠࡪࡶࠣࡻࡦࡹࠠࡪࡰࡹࡩࡳࡺࡥࡥࠢࡥࡽࠥࡘࡩࡷࡧࡶࡸࠥ࡯࡮ࠡ࠳࠼࠼࠾࠴ࠊࠋࡖ࡫࡭ࡸࠦࡡ࡭ࡩࡲࡶ࡮ࡺࡨ࡮ࠢ࡬ࡷࠥࡨ࡯ࡵࡪࠣࡷࡱࡵࡷࠡࡣࡱࡨࠥ࡯࡮ࡴࡧࡦࡹࡷ࡫࠮ࠡࡆࡲࠤࡳࡵࡴࠡࡷࡶࡩࠥ࡯ࡴࠡࡨࡲࡶࠥࡴࡥࡸࠢࡧࡩࡸ࡯ࡧ࡯ࡵ࠱ࠎࠏ࠴࠮ࠡࡡࡕࡊࡈ࠷࠳࠲࠻࠽ࠤ࡭ࡺࡴࡱ࠼࠲࠳ࡹࡵ࡯࡭ࡵ࠱࡭ࡪࡺࡦ࠯ࡱࡵ࡫࠴࡮ࡴ࡮࡮࠲ࡶ࡫ࡩ࠱࠴࠳࠼ࠎࠧࠨࠢࢩ")
_revision__ = l1l1111_Krypto_ (u"ࠨࠤࡊࡦࠧࠦࢪ")
__all__ = [l1l1111_Krypto_ (u"ࠧ࡯ࡧࡺࠫࢫ"), l1l1111_Krypto_ (u"ࠨࡦ࡬࡫ࡪࡹࡴࡠࡵ࡬ࡾࡪ࠭ࢬ"), l1l1111_Krypto_ (u"ࠩࡐࡈ࠷ࡎࡡࡴࡪࠪࢭ") ]
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
from l111ll1_Krypto_.l1lll1ll1_Krypto_.l11111lll_Krypto_ import l1111l11l_Krypto_
import l111ll1_Krypto_.l1lll1ll1_Krypto_._1lllll1ll_Krypto_ as _1lllll1ll_Krypto_
l1111l1l1_Krypto_ = _1lllll1ll_Krypto_
class l1llllll1l_Krypto_(l1111l11l_Krypto_):
    l1l1111_Krypto_ (u"ࠥࠦࠧࡉ࡬ࡢࡵࡶࠤࡹ࡮ࡡࡵࠢ࡬ࡱࡵࡲࡥ࡮ࡧࡱࡸࡸࠦࡡ࡯ࠢࡐࡈ࠷ࠦࡨࡢࡵ࡫ࠎࠥࠦࠠࠡࠌࠣࠤࠥࠦ࠺ࡶࡰࡧࡳࡨࡻ࡭ࡦࡰࡷࡩࡩࡀࠠࡣ࡮ࡲࡧࡰࡥࡳࡪࡼࡨࠎࠥࠦࠠࠡࠤࠥࠦࢮ")
    l1llllll11_Krypto_ = b(l1l1111_Krypto_ (u"ࠫࡡࡾ࠰࠷࡞ࡻ࠴࠽ࡢࡸ࠳ࡣ࡟ࡼ࠽࠼࡜ࡹ࠶࠻ࡠࡽ࠾࠶࡝ࡺࡩ࠻ࡡࡾ࠰ࡥ࡞ࡻ࠴࠷ࡢࡸ࠱࠴ࠪࢯ"))
    digest_size = 16
    block_size = 16
    def __init__(self, data=None):
        l1111l11l_Krypto_.__init__(self, l1111l1l1_Krypto_, data)
    def new(self, data=None):
        return l1llllll1l_Krypto_(data)
def new(data=None):
    l1l1111_Krypto_ (u"ࠧࠨࠢࡓࡧࡷࡹࡷࡴࠠࡢࠢࡩࡶࡪࡹࡨࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠣࡳ࡫ࠦࡴࡩࡧࠣ࡬ࡦࡹࡨࠡࡱࡥ࡮ࡪࡩࡴ࠯ࠌࠍࠤࠥࠦࠠ࠻ࡒࡤࡶࡦࡳࡥࡵࡧࡵࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࡤࡢࡶࡤࠤ࠿ࠦࡢࡺࡶࡨࠤࡸࡺࡲࡪࡰࡪࠎࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࡨࡦࠢࡹࡩࡷࡿࠠࡧ࡫ࡵࡷࡹࠦࡣࡩࡷࡱ࡯ࠥࡵࡦࠡࡶ࡫ࡩࠥࡳࡥࡴࡵࡤ࡫ࡪࠦࡴࡰࠢ࡫ࡥࡸ࡮࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡌࡸࠥ࡯ࡳࠡࡧࡴࡹ࡮ࡼࡡ࡭ࡧࡱࡸࠥࡺ࡯ࠡࡣࡱࠤࡪࡧࡲ࡭ࡻࠣࡧࡦࡲ࡬ࠡࡶࡲࠤࡥࡓࡄ࠳ࡊࡤࡷ࡭࠴ࡵࡱࡦࡤࡸࡪ࠮ࠩࡡ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡔࡶࡴࡪࡱࡱࡥࡱ࠴ࠊࠋࠢࠣࠤࠥࡀࡒࡦࡶࡸࡶࡳࡀࠠࡂࡰࠣࡤࡒࡊ࠲ࡉࡣࡶ࡬ࡥࠦ࡯ࡣ࡬ࡨࡧࡹࠐࠠࠡࠢࠣࠦࠧࠨࢰ")
    return l1llllll1l_Krypto_().new(data)
digest_size = l1llllll1l_Krypto_.digest_size
block_size = l1llllll1l_Krypto_.block_size