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
l1l1111_Krypto_ (u"ࠤࠥࠦࡕࡿࡴࡩࡱࡱࠤࡈࡸࡹࡱࡶࡲ࡫ࡷࡧࡰࡩࡻࠣࡘࡴࡵ࡬࡬࡫ࡷࠎࠏࡇࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡱࡱࠤࡴ࡬ࠠࡤࡴࡼࡴࡹࡵࡧࡳࡣࡳ࡬࡮ࡩࠠ࡮ࡱࡧࡹࡱ࡫ࡳࠡ࡫ࡰࡴࡱ࡫࡭ࡦࡰࡷ࡭ࡳ࡭ࠠࡷࡣࡵ࡭ࡴࡻࡳࠡࡣ࡯࡫ࡴࡸࡩࡵࡪࡰࡷࠏࡧ࡮ࡥࠢࡳࡶࡴࡺ࡯ࡤࡱ࡯ࡷ࠳ࠐࠊࡔࡷࡥࡴࡦࡩ࡫ࡢࡩࡨࡷ࠿ࠐࠊࡄࡴࡼࡴࡹࡵ࠮ࡄ࡫ࡳ࡬ࡪࡸࠊࠡࡕࡨࡧࡷ࡫ࡴ࠮࡭ࡨࡽࠥ࠮ࡁࡆࡕ࠯ࠤࡉࡋࡓ࠭ࠢࡄࡖࡈ࠺ࠩࠡࡣࡱࡨࠥࡶࡵࡣ࡮࡬ࡧ࠲ࡱࡥࡺࠢࡨࡲࡨࡸࡹࡱࡶ࡬ࡳࡳࠦࠨࡓࡕࡄࠤࡕࡑࡃࡔࠌࡆࡶࡾࡶࡴࡰ࠰ࡋࡥࡸ࡮ࠊࠡࡊࡤࡷ࡭࡯࡮ࡨࠢࡤࡰ࡬ࡵࡲࡪࡶ࡫ࡱࡸࠦࠨࡎࡆ࠸࠰࡙ࠥࡈࡂ࠮ࠣࡌࡒࡇࡃࠪࠌࡆࡶࡾࡶࡴࡰ࠰ࡓࡶࡴࡺ࡯ࡤࡱ࡯ࠎࠥࡉࡲࡺࡲࡷࡳ࡬ࡸࡡࡱࡪ࡬ࡧࠥࡶࡲࡰࡶࡲࡧࡴࡲࡳࠡࠪࡆ࡬ࡦ࡬ࡦࡪࡰࡪ࠰ࠥࡧ࡬࡭࠯ࡲࡶ࠲ࡴ࡯ࡵࡪ࡬ࡲ࡬ࠦࡴࡳࡣࡱࡷ࡫ࡵࡲ࡮࠮ࠣ࡯ࡪࡿࠠࡥࡧࡵ࡭ࡻࡧࡴࡪࡱࡱࠎࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࡳࠪ࠰ࠣࡘ࡭࡯ࡳࠡࡲࡤࡧࡰࡧࡧࡦࠢࡧࡳࡪࡹࠠ࡯ࡱࡷࠤࡨࡵ࡮ࡵࡣ࡬ࡲࠥࡧ࡮ࡺࠢࡱࡩࡹࡽ࡯ࡳ࡭ࠣࡴࡷࡵࡴࡰࡥࡲࡰࡸ࠴ࠊࡄࡴࡼࡴࡹࡵ࠮ࡑࡷࡥࡰ࡮ࡩࡋࡦࡻࠍࠤࡕࡻࡢ࡭࡫ࡦ࠱ࡰ࡫ࡹࠡࡧࡱࡧࡷࡿࡰࡵ࡫ࡲࡲࠥࡧ࡮ࡥࠢࡶ࡭࡬ࡴࡡࡵࡷࡵࡩࠥࡧ࡬ࡨࡱࡵ࡭ࡹ࡮࡭ࡴࠢࠫࡖࡘࡇࠬࠡࡆࡖࡅ࠮ࠐࡃࡳࡻࡳࡸࡴ࠴ࡓࡪࡩࡱࡥࡹࡻࡲࡦࠌࠣࡔࡺࡨ࡬ࡪࡥ࠰࡯ࡪࡿࠠࡴ࡫ࡪࡲࡦࡺࡵࡳࡧࠣࡥࡱ࡭࡯ࡳ࡫ࡷ࡬ࡲࡹࠠࠩࡔࡖࡅࠥࡖࡋࡄࡕࠍࡇࡷࡿࡰࡵࡱ࠱࡙ࡹ࡯࡬ࠋ࡙ࠢࡥࡷ࡯࡯ࡶࡵࠣࡹࡸ࡫ࡦࡶ࡮ࠣࡱࡴࡪࡵ࡭ࡧࡶࠤࡦࡴࡤࠡࡨࡸࡲࡨࡺࡩࡰࡰࡶࠤ࠭ࡲ࡯࡯ࡩ࠰ࡸࡴ࠳ࡳࡵࡴ࡬ࡲ࡬ࠦࡣࡰࡰࡹࡩࡷࡹࡩࡰࡰ࠯ࠤࡷࡧ࡮ࡥࡱࡰࠤࡳࡻ࡭ࡣࡧࡵࠎࠥ࡭ࡥ࡯ࡧࡵࡥࡹ࡯࡯࡯࠮ࠣࡲࡺࡳࡢࡦࡴࠣࡸ࡭࡫࡯ࡳࡧࡷ࡭ࡨࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡴࠫࠍࠦࠧࠨࠨ")
__all__ = [l1l1111_Krypto_ (u"ࠪࡇ࡮ࡶࡨࡦࡴࠪࠩ"), l1l1111_Krypto_ (u"ࠫࡍࡧࡳࡩࠩࠪ"), l1l1111_Krypto_ (u"ࠬࡖࡲࡰࡶࡲࡧࡴࡲࠧࠫ"), l1l1111_Krypto_ (u"࠭ࡐࡶࡤ࡯࡭ࡨࡑࡥࡺࠩࠬ"), l1l1111_Krypto_ (u"ࠧࡖࡶ࡬ࡰࠬ࠭"), l1l1111_Krypto_ (u"ࠨࡕ࡬࡫ࡳࡧࡴࡶࡴࡨࠫ࠮")]
__version__ = l1l1111_Krypto_ (u"ࠩ࠵࠲࠻࠴࠱ࠨ࠯")
__revision__ = l1l1111_Krypto_ (u"ࠥࠨࡎࡪࠤࠣ࠰")
version_info = (2, 6, 1, l1l1111_Krypto_ (u"ࠫ࡫࡯࡮ࡢ࡮ࠪ࠱"), 0)