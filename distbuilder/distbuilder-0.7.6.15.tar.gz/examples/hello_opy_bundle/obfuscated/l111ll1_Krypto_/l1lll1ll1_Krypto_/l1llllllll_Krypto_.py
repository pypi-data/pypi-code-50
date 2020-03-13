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
l1l1111_Krypto_ (u"ࠢࠣࠤࡐࡈ࠺ࠦࡣࡳࡻࡳࡸࡴ࡭ࡲࡢࡲ࡫࡭ࡨࠦࡨࡢࡵ࡫ࠤࡦࡲࡧࡰࡴ࡬ࡸ࡭ࡳ࠮ࠋࠌࡐࡈ࠺ࠦࡩࡴࠢࡶࡴࡪࡩࡩࡧ࡫ࡨࡨࠥ࡯࡮ࠡࡔࡉࡇ࠶࠹࠲࠲ࡡࠣࡥࡳࡪࠠࡱࡴࡲࡨࡺࡩࡥࡴࠢࡷ࡬ࡪࠦ࠱࠳࠺ࠣࡦ࡮ࡺࠠࡥ࡫ࡪࡩࡸࡺࠠࡰࡨࠣࡥࠥࡳࡥࡴࡵࡤ࡫ࡪ࠴ࠊࠋࠢࠣࠤࠥࡄ࠾࠿ࠢࡩࡶࡴࡳࠠࡄࡴࡼࡴࡹࡵ࠮ࡉࡣࡶ࡬ࠥ࡯࡭ࡱࡱࡵࡸࠥࡓࡄ࠶ࠌࠣࠤࠥࠦ࠾࠿ࡀࠍࠤࠥࠦࠠ࠿ࡀࡁࠤ࡭ࠦ࠽ࠡࡏࡇ࠹࠳ࡴࡥࡸࠪࠬࠎࠥࠦࠠࠡࡀࡁࡂࠥ࡮࠮ࡶࡲࡧࡥࡹ࡫ࠨࡣࠩࡋࡩࡱࡲ࡯ࠨࠫࠍࠤࠥࠦࠠ࠿ࡀࡁࠤࡵࡸࡩ࡯ࡶࠣ࡬࠳࡮ࡥࡹࡦ࡬࡫ࡪࡹࡴࠩࠫࠍࠎࡒࡊ࠵ࠡࡵࡷࡥࡳࡪࠠࡧࡱࡵࠤࡒ࡫ࡳࡴࡣࡪࡩࠥࡊࡩࡨࡧࡶࡸࠥࡼࡥࡳࡵ࡬ࡳࡳࠦ࠵࠭ࠢࡤࡲࡩࠦࡩࡵࠢࡺࡥࡸࠦࡩ࡯ࡸࡨࡲࡹ࡫ࡤࠡࡤࡼࠤࡗ࡯ࡶࡦࡵࡷࠤ࡮ࡴࠠ࠲࠻࠼࠵࠳ࠐࠊࡕࡪ࡬ࡷࠥࡧ࡬ࡨࡱࡵ࡭ࡹ࡮࡭ࠡ࡫ࡶࠤ࡮ࡴࡳࡦࡥࡸࡶࡪ࠴ࠠࡅࡱࠣࡲࡴࡺࠠࡶࡵࡨࠤ࡮ࡺࠠࡧࡱࡵࠤࡳ࡫ࡷࠡࡦࡨࡷ࡮࡭࡮ࡴ࠰ࠍࠎ࠳࠴ࠠࡠࡔࡉࡇ࠶࠹࠲࠲࠼ࠣ࡬ࡹࡺࡰ࠻࠱࠲ࡸࡴࡵ࡬ࡴ࠰࡬ࡩࡹ࡬࠮ࡰࡴࡪ࠳࡭ࡺ࡭࡭࠱ࡵࡪࡨ࠷࠳࠳࠳ࠣࠎࠧࠨࠢࢹ")
_revision__ = l1l1111_Krypto_ (u"ࠣࠦࡌࡨࠩࠨࢺ")
__all__ = [l1l1111_Krypto_ (u"ࠩࡱࡩࡼ࠭ࢻ"), l1l1111_Krypto_ (u"ࠪࡨ࡮࡭ࡥࡴࡶࡢࡷ࡮ࢀࡥࠨࢼ"), l1l1111_Krypto_ (u"ࠫࡒࡊ࠵ࡉࡣࡶ࡬ࠬࢽ") ]
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
from l111ll1_Krypto_.l1lll1ll1_Krypto_.l11111lll_Krypto_ import l1111l11l_Krypto_
try:
    import hashlib as l1llll1l1l_Krypto_
    l1111l1l1_Krypto_ = l1llll1l1l_Krypto_.md5
except ImportError:
    from . import md5
    l1111l1l1_Krypto_ = md5
class l1llll1ll1_Krypto_(l1111l11l_Krypto_):
    l1l1111_Krypto_ (u"ࠧࠨࠢࡄ࡮ࡤࡷࡸࠦࡴࡩࡣࡷࠤ࡮ࡳࡰ࡭ࡧࡰࡩࡳࡺࡳࠡࡣࡱࠤࡒࡊ࠵ࠡࡪࡤࡷ࡭ࠐࠠࠡࠢࠣࠎࠥࠦࠠࠡ࠼ࡸࡲࡩࡵࡣࡶ࡯ࡨࡲࡹ࡫ࡤ࠻ࠢࡥࡰࡴࡩ࡫ࡠࡵ࡬ࡾࡪࠐࠠࠡࠢࠣࠦࠧࠨࢾ")
    l1llllll11_Krypto_ = b(l1l1111_Krypto_ (u"࠭࡜ࡹ࠲࠹ࡠࡽ࠶࠸࡝ࡺ࠵ࡥࡡࡾ࠸࠷࡞ࡻ࠸࠽ࡢࡸ࠹࠸࡟ࡼ࡫࠽࡜ࡹ࠲ࡧࡠࡽ࠶࠲࡝ࡺ࠳࠹ࠬࢿ"))
    digest_size = 16
    block_size = 64
    def __init__(self, data=None):
        l1111l11l_Krypto_.__init__(self, l1111l1l1_Krypto_, data)
    def new(self, data=None):
        return l1llll1ll1_Krypto_(data)
def new(data=None):
    l1l1111_Krypto_ (u"ࠢࠣࠤࡕࡩࡹࡻࡲ࡯ࠢࡤࠤ࡫ࡸࡥࡴࡪࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࠥࡵࡦࠡࡶ࡫ࡩࠥ࡮ࡡࡴࡪࠣࡳࡧࡰࡥࡤࡶ࠱ࠎࠏࠦࠠࠡࠢ࠽ࡔࡦࡸࡡ࡮ࡧࡷࡩࡷࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࡦࡤࡸࡦࠦ࠺ࠡࡤࡼࡸࡪࠦࡳࡵࡴ࡬ࡲ࡬ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡕࡪࡨࠤࡻ࡫ࡲࡺࠢࡩ࡭ࡷࡹࡴࠡࡥ࡫ࡹࡳࡱࠠࡰࡨࠣࡸ࡭࡫ࠠ࡮ࡧࡶࡷࡦ࡭ࡥࠡࡶࡲࠤ࡭ࡧࡳࡩ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡎࡺࠠࡪࡵࠣࡩࡶࡻࡩࡷࡣ࡯ࡩࡳࡺࠠࡵࡱࠣࡥࡳࠦࡥࡢࡴ࡯ࡽࠥࡩࡡ࡭࡮ࠣࡸࡴࠦࡠࡎࡆ࠸ࡌࡦࡹࡨ࠯ࡷࡳࡨࡦࡺࡥࠩࠫࡣ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡏࡱࡶ࡬ࡳࡳࡧ࡬࠯ࠌࠍࠤࠥࠦࠠ࠻ࡔࡨࡸࡺࡸ࡮࠻ࠢࡄࠤࡥࡓࡄ࠶ࡊࡤࡷ࡭ࡦࠠࡰࡤ࡭ࡩࡨࡺࠊࠡࠢࠣࠤࠧࠨࠢࣀ")
    return l1llll1ll1_Krypto_().new(data)
digest_size = l1llll1ll1_Krypto_.digest_size
block_size = l1llll1ll1_Krypto_.block_size