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
l1l1111_Krypto_ (u"ࠣࠤࠥࡖࡎࡖࡅࡎࡆ࠰࠵࠻࠶ࠠࡤࡴࡼࡴࡹࡵࡧࡳࡣࡳ࡬࡮ࡩࠠࡩࡣࡶ࡬ࠥࡧ࡬ࡨࡱࡵ࡭ࡹ࡮࡭࠯ࠌࠍࡖࡎࡖࡅࡎࡆ࠰࠵࠻࠶࡟ࠡࡲࡵࡳࡩࡻࡣࡦࡵࠣࡸ࡭࡫ࠠ࠲࠸࠳ࠤࡧ࡯ࡴࠡࡦ࡬࡫ࡪࡹࡴࠡࡱࡩࠤࡦࠦ࡭ࡦࡵࡶࡥ࡬࡫࠮ࠋࠌࠣࠤࠥࠦ࠾࠿ࡀࠣࡪࡷࡵ࡭ࠡࡅࡵࡽࡵࡺ࡯࠯ࡊࡤࡷ࡭ࠦࡩ࡮ࡲࡲࡶࡹࠦࡒࡊࡒࡈࡑࡉࠐࠠࠡࠢࠣࡂࡃࡄࠊࠡࠢࠣࠤࡃࡄ࠾ࠡࡪࠣࡁࠥࡘࡉࡑࡇࡐࡈ࠳ࡴࡥࡸࠪࠬࠎࠥࠦࠠࠡࡀࡁࡂࠥ࡮࠮ࡶࡲࡧࡥࡹ࡫ࠨࡣࠩࡋࡩࡱࡲ࡯ࠨࠫࠍࠤࠥࠦࠠ࠿ࡀࡁࠤࡵࡸࡩ࡯ࡶࠣ࡬࠳࡮ࡥࡹࡦ࡬࡫ࡪࡹࡴࠩࠫࠍࠎࡗࡏࡐࡆࡏࡇ࠱࠶࠼࠰ࠡࡵࡷࡥࡳࡪࡳࠡࡨࡲࡶࠥࡘࡁࡄࡇࠣࡍࡳࡺࡥࡨࡴ࡬ࡸࡾࠦࡐࡳ࡫ࡰ࡭ࡹ࡯ࡶࡦࡵࠣࡉࡻࡧ࡬ࡶࡣࡷ࡭ࡴࡴࠠࡎࡧࡶࡷࡦ࡭ࡥࠡࡆ࡬࡫ࡪࡹࡴࠋࡹ࡬ࡸ࡭ࠦࡡࠡ࠳࠹࠴ࠥࡨࡩࡵࠢࡧ࡭࡬࡫ࡳࡵ࠰ࠣࡍࡹࠦࡷࡢࡵࠣ࡭ࡳࡼࡥ࡯ࡶࡨࡨࠥࡨࡹࠡࡆࡲࡦࡧ࡫ࡲࡵ࡫ࡱ࠰ࠥࡈ࡯ࡴࡵࡨࡰࡦ࡫ࡲࡴ࠮ࠣࡥࡳࡪࠠࡑࡴࡨࡲࡪ࡫࡬࠯ࠌࠍࡘ࡭࡯ࡳࠡࡣ࡯࡫ࡴࡸࡩࡵࡪࡰࠤ࡮ࡹࠠࡤࡱࡱࡷ࡮ࡪࡥࡳࡧࡧࠤࡸ࡫ࡣࡶࡴࡨ࠰ࠥࡧ࡬ࡵࡪࡲࡹ࡬࡮ࠠࡪࡶࠣ࡬ࡦࡹࠠ࡯ࡱࡷࠤࡧ࡫ࡥ࡯ࠢࡶࡧࡷࡻࡴࡪࡰ࡬ࡾࡪࡪࠠࡢࡵࠍࡩࡽࡺࡥ࡯ࡵ࡬ࡺࡪࡲࡹࠡࡣࡶࠤࡘࡎࡁ࠮࠳࠱ࠤࡒࡵࡲࡦࡱࡹࡩࡷ࠲ࠠࡪࡶࠣࡴࡷࡵࡶࡪࡦࡨࡷࠥࡧ࡮ࠡ࡫ࡱࡪࡴࡸ࡭ࡢ࡮ࠣࡷࡪࡩࡵࡳ࡫ࡷࡽࠥࡲࡥࡷࡧ࡯ࠤࡴ࡬ࠠ࡫ࡷࡶࡸࠏ࠾࠰ࡣ࡫ࡷࡷ࠳ࠐࠊ࠯࠰ࠣࡣࡗࡏࡐࡆࡏࡇ࠱࠶࠼࠰࠻ࠢ࡫ࡸࡹࡶ࠺࠰࠱࡫ࡳࡲ࡫ࡳ࠯ࡧࡶࡥࡹ࠴࡫ࡶ࡮ࡨࡹࡻ࡫࡮࠯ࡤࡨ࠳ࢃࡨ࡯ࡴࡵࡨࡰࡦ࡫࠯ࡳ࡫ࡳࡩࡲࡪ࠱࠷࠲࠱࡬ࡹࡳ࡬ࠋࠤࠥࠦࣁ")
_revision__ = l1l1111_Krypto_ (u"ࠤࠧࡍࡩࠪࠢࣂ")
__all__ = [l1l1111_Krypto_ (u"ࠪࡲࡪࡽࠧࣃ"), l1l1111_Krypto_ (u"ࠫࡩ࡯ࡧࡦࡵࡷࡣࡸ࡯ࡺࡦࠩࣄ"), l1l1111_Krypto_ (u"ࠬࡘࡉࡑࡇࡐࡈ࠶࠼࠰ࡉࡣࡶ࡬ࠬࣅ") ]
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
from l111ll1_Krypto_.l1lll1ll1_Krypto_.l11111lll_Krypto_ import l1111l11l_Krypto_
import l111ll1_Krypto_.l1lll1ll1_Krypto_._1llll11ll_Krypto_ as _1llll11ll_Krypto_
l1111l1l1_Krypto_ = _1llll11ll_Krypto_
class l1llll1l11_Krypto_(l1111l11l_Krypto_):
    l1l1111_Krypto_ (u"ࠨࠢࠣࡅ࡯ࡥࡸࡹࠠࡵࡪࡤࡸࠥ࡯࡭ࡱ࡮ࡨࡱࡪࡴࡴࡴࠢࡤࠤࡗࡏࡐࡎࡆ࠰࠵࠻࠶ࠠࡩࡣࡶ࡬ࠏࠦࠠࠡࠢࠍࠤࠥࠦࠠ࠻ࡷࡱࡨࡴࡩࡵ࡮ࡧࡱࡸࡪࡪ࠺ࠡࡤ࡯ࡳࡨࡱ࡟ࡴ࡫ࡽࡩࠏࠦࠠࠡࠢࠥࠦࠧࣆ")
    l1llllll11_Krypto_ = b(l1l1111_Krypto_ (u"ࠢ࡝ࡺ࠳࠺ࡡࡾ࠰࠶࡞ࡻ࠶ࡧࡢࡸ࠳࠶࡟ࡼ࠵࠹࡜ࡹ࠲࠵ࡠࡽ࠶࠱ࠣࣇ"))
    digest_size = 20
    block_size = 64
    def __init__(self, data=None):
        l1111l11l_Krypto_.__init__(self, l1111l1l1_Krypto_, data)
    def new(self, data=None):
        return l1llll1l11_Krypto_(data)
def new(data=None):
    l1l1111_Krypto_ (u"ࠣࠤࠥࡖࡪࡺࡵࡳࡰࠣࡥࠥ࡬ࡲࡦࡵ࡫ࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࠦ࡯ࡧࠢࡷ࡬ࡪࠦࡨࡢࡵ࡫ࠤࡴࡨࡪࡦࡥࡷ࠲ࠏࠐࠠࠡࠢࠣ࠾ࡕࡧࡲࡢ࡯ࡨࡸࡪࡸࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࡧࡥࡹࡧࠠ࠻ࠢࡥࡽࡹ࡫ࠠࡴࡶࡵ࡭ࡳ࡭ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡖ࡫ࡩࠥࡼࡥࡳࡻࠣࡪ࡮ࡸࡳࡵࠢࡦ࡬ࡺࡴ࡫ࠡࡱࡩࠤࡹ࡮ࡥࠡ࡯ࡨࡷࡸࡧࡧࡦࠢࡷࡳࠥ࡮ࡡࡴࡪ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡏࡴࠡ࡫ࡶࠤࡪࡷࡵࡪࡸࡤࡰࡪࡴࡴࠡࡶࡲࠤࡦࡴࠠࡦࡣࡵࡰࡾࠦࡣࡢ࡮࡯ࠤࡹࡵࠠࡡࡔࡌࡔࡊࡓࡄ࠲࠸࠳ࡌࡦࡹࡨ࠯ࡷࡳࡨࡦࡺࡥࠩࠫࡣ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡏࡱࡶ࡬ࡳࡳࡧ࡬࠯ࠌࠍࠤࠥࠦࠠ࠻ࡔࡨࡸࡺࡸ࡮࠻ࠢࡄࠤࡥࡘࡉࡑࡇࡐࡈ࠶࠼࠰ࡉࡣࡶ࡬ࡥࠦ࡯ࡣ࡬ࡨࡧࡹࠐࠠࠡࠢࠣࠦࠧࠨࣈ")
    return l1llll1l11_Krypto_().new(data)
digest_size = l1llll1l11_Krypto_.digest_size
block_size = l1llll1l11_Krypto_.block_size