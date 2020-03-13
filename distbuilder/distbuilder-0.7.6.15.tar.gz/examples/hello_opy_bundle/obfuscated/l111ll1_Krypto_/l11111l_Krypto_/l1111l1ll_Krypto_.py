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
l1l1111_Krypto_ (u"ࠧࠨ࡙ࠢࡑࡕࠤࡹࡵࡹࠡࡥ࡬ࡴ࡭࡫ࡲࠋࠌ࡛ࡓࡗࠦࡩࡴࠢࡲࡲࡪࠦࡴࡩࡧࠣࡷ࡮ࡳࡰ࡭ࡧࡶࡸࠥࡹࡴࡳࡧࡤࡱࠥࡩࡩࡱࡪࡨࡶࡸ࠴ࠠࡆࡰࡦࡶࡾࡶࡴࡪࡱࡱࠤࡦࡴࡤࠡࡦࡨࡧࡷࡿࡰࡵ࡫ࡲࡲࠥࡧࡲࡦࠌࡳࡩࡷ࡬࡯ࡳ࡯ࡨࡨࠥࡨࡹ࡚ࠡࡒࡖ࠲࡯࡮ࡨࠢࡧࡥࡹࡧࠠࡸ࡫ࡷ࡬ࠥࡧࠠ࡬ࡧࡼࡷࡹࡸࡥࡢ࡯ࠣࡱࡦࡪࡥࠡࡤࡼࠤࡨࡵ࡮ࡵࡣࡷࡩࡳࡧࡴࡪࡰࡪࠎࡹ࡮ࡥࠡ࡭ࡨࡽ࠳ࠐࠊࡅࡱࠣࡲࡴࡺࠠࡶࡵࡨࠤ࡮ࡺࠠࡧࡱࡵࠤࡷ࡫ࡡ࡭ࠢࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴࡳࠢࠌࠍ࠾ࡺࡴࡤࡰࡥࡸࡱࡪࡴࡴࡦࡦ࠽ࠤࡤࡥࡲࡦࡸ࡬ࡷ࡮ࡵ࡮ࡠࡡ࠯ࠤࡤࡥࡰࡢࡥ࡮ࡥ࡬࡫࡟ࡠࠌࠥࠦࠧࡿ")
__revision__ = l1l1111_Krypto_ (u"ࠨࠤࡊࡦࠧࠦࢀ")
from l111ll1_Krypto_.l11111l_Krypto_ import _1111ll11_Krypto_
class l1111ll1l_Krypto_:
    l1l1111_Krypto_ (u"ࠢࠣࠤ࡛ࡓࡗࠦࡣࡪࡲ࡫ࡩࡷࠦ࡯ࡣ࡬ࡨࡧࡹࠨࠢࠣࢁ")
    def __init__(self, key, *args, **kwargs):
        l1l1111_Krypto_ (u"ࠣࠤࠥࡍࡳ࡯ࡴࡪࡣ࡯࡭ࡿ࡫ࠠࡢ࡛ࠢࡓࡗࠦࡣࡪࡲ࡫ࡩࡷࠦ࡯ࡣ࡬ࡨࡧࡹࠐࠠࠡࠢࠣࠤࠥࠦࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢࡖࡩࡪࠦࡡ࡭ࡵࡲࠤࡥࡴࡥࡸࠪࠬࡤࠥࡧࡴࠡࡶ࡫ࡩࠥࡳ࡯ࡥࡷ࡯ࡩࠥࡲࡥࡷࡧ࡯࠲ࠧࠨࠢࢂ")
        self._1ll1111_Krypto_ = _1111ll11_Krypto_.new(key, *args, **kwargs)
        self.block_size = self._1ll1111_Krypto_.block_size
        self.l111l1l_Krypto_ = self._1ll1111_Krypto_.l111l1l_Krypto_
    def l1_Krypto_(self, l1ll11l1_Krypto_):
        l1l1111_Krypto_ (u"ࠤࠥࠦࡊࡴࡣࡳࡻࡳࡸࠥࡧࠠࡱ࡫ࡨࡧࡪࠦ࡯ࡧࠢࡧࡥࡹࡧ࠮ࠋࠌࠣࠤࠥࠦࠠࠡࠢࠣ࠾ࡕࡧࡲࡢ࡯ࡨࡸࡪࡸࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡶ࡬ࡢ࡫ࡱࡸࡪࡾࡴࠡ࠼ࠣࡦࡾࡺࡥࠡࡵࡷࡶ࡮ࡴࡧࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡔࡩࡧࠣࡴ࡮࡫ࡣࡦࠢࡲࡪࠥࡪࡡࡵࡣࠣࡸࡴࠦࡥ࡯ࡥࡵࡽࡵࡺ࠮ࠡࡋࡷࠤࡨࡧ࡮ࠡࡤࡨࠤࡴ࡬ࠠࡢࡰࡼࠤࡸ࡯ࡺࡦ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࠿ࡘࡥࡵࡷࡵࡲ࠿ࠦࡴࡩࡧࠣࡩࡳࡩࡲࡺࡲࡷࡩࡩࠦࡤࡢࡶࡤࠤ࠭ࡨࡹࡵࡧࠣࡷࡹࡸࡩ࡯ࡩ࠯ࠤࡦࡹࠠ࡭ࡱࡱ࡫ࠥࡧࡳࠡࡶ࡫ࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡲ࡯ࡥ࡮ࡴࡴࡦࡺࡷ࠭࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥࢃ")
        return self._1ll1111_Krypto_.l1_Krypto_(l1ll11l1_Krypto_)
    def l1lllll_Krypto_(self, l1ll111l_Krypto_):
        l1l1111_Krypto_ (u"ࠥࠦࠧࡊࡥࡤࡴࡼࡴࡹࠦࡡࠡࡲ࡬ࡩࡨ࡫ࠠࡰࡨࠣࡨࡦࡺࡡ࠯ࠌࠍࠤࠥࠦࠠࠡࠢࠣࠤ࠿ࡖࡡࡳࡣࡰࡩࡹ࡫ࡲࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡣࡪࡲ࡫ࡩࡷࡺࡥࡹࡶࠣ࠾ࠥࡨࡹࡵࡧࠣࡷࡹࡸࡩ࡯ࡩࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡖ࡫ࡩࠥࡶࡩࡦࡥࡨࠤࡴ࡬ࠠࡥࡣࡷࡥࠥࡺ࡯ࠡࡦࡨࡧࡷࡿࡰࡵ࠰ࠣࡍࡹࠦࡣࡢࡰࠣࡦࡪࠦ࡯ࡧࠢࡤࡲࡾࠦࡳࡪࡼࡨ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠺ࡓࡧࡷࡹࡷࡴ࠺ࠡࡶ࡫ࡩࠥࡪࡥࡤࡴࡼࡴࡹ࡫ࡤࠡࡦࡤࡸࡦࠦࠨࡣࡻࡷࡩࠥࡹࡴࡳ࡫ࡱ࡫࠱ࠦࡡࡴࠢ࡯ࡳࡳ࡭ࠠࡢࡵࠣࡸ࡭࡫ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡧ࡮ࡶࡨࡦࡴࡷࡩࡽࡺࠩ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨࢄ")
        return self._1ll1111_Krypto_.l1lllll_Krypto_(l1ll111l_Krypto_)
def new(key, *args, **kwargs):
    l1l1111_Krypto_ (u"ࠦࠧࠨࡃࡳࡧࡤࡸࡪࠦࡡࠡࡰࡨࡻࠥ࡞ࡏࡓࠢࡦ࡭ࡵ࡮ࡥࡳࠌࠍࠤࠥࠦࠠ࠻ࡒࡤࡶࡦࡳࡥࡵࡧࡵࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࡱࡥࡺࠢ࠽ࠤࡧࡿࡴࡦࠢࡶࡸࡷ࡯࡮ࡨࠌࠣࠤࠥࠦࠠࠡࠢࠣࡘ࡭࡫ࠠࡴࡧࡦࡶࡪࡺࠠ࡬ࡧࡼࠤࡹࡵࠠࡶࡵࡨࠤ࡮ࡴࠠࡵࡪࡨࠤࡸࡿ࡭࡮ࡧࡷࡶ࡮ࡩࠠࡤ࡫ࡳ࡬ࡪࡸ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡌࡸࡸࠦ࡬ࡦࡰࡪࡸ࡭ࠦ࡭ࡢࡻࠣࡺࡦࡸࡹࠡࡨࡵࡳࡲࠦ࠱ࠡࡶࡲࠤ࠸࠸ࠠࡣࡻࡷࡩࡸ࠴ࠊࠋࠢࠣࠤࠥࡀࡒࡦࡶࡸࡶࡳࡀࠠࡢࡰࠣࡤ࡝ࡕࡒࡄ࡫ࡳ࡬ࡪࡸࡠࠡࡱࡥ࡮ࡪࡩࡴࠋࠢࠣࠤࠥࠨࠢࠣࢅ")
    return l1111ll1l_Krypto_(key, *args, **kwargs)
block_size = 1
l111l1l_Krypto_ = range(1,32+1)