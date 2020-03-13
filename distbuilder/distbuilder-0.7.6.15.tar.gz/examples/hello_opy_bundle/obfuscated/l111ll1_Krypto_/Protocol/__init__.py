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
l1l1111_Krypto_ (u"ࠧࠨࠢࡄࡴࡼࡴࡹࡵࡧࡳࡣࡳ࡬࡮ࡩࠠࡱࡴࡲࡸࡴࡩ࡯࡭ࡵࠍࠎࡎࡳࡰ࡭ࡧࡰࡩࡳࡺࡳࠡࡸࡤࡶ࡮ࡵࡵࡴࠢࡦࡶࡾࡶࡴࡰࡩࡵࡥࡵ࡮ࡩࡤࠢࡳࡶࡴࡺ࡯ࡤࡱ࡯ࡷ࠳ࠦࠠࠩࡆࡲࡲࠬࡺࠠࡦࡺࡳࡩࡨࡺࠠࡵࡱࠣࡪ࡮ࡴࡤࠋࡰࡨࡸࡼࡵࡲ࡬ࠢࡳࡶࡴࡺ࡯ࡤࡱ࡯ࡷࠥ࡮ࡥࡳࡧ࠱࠭ࠏࠐࡃࡳࡻࡳࡸࡴ࠴ࡐࡳࡱࡷࡳࡨࡵ࡬࠯ࡃ࡯ࡰࡔࡸࡎࡰࡶ࡫࡭ࡳ࡭ࠊࠡࡖࡵࡥࡳࡹࡦࡰࡴࡰࡷࠥࡧࠠ࡮ࡧࡶࡷࡦ࡭ࡥࠡ࡫ࡱࡸࡴࠦࡡࠡࡵࡨࡸࠥࡵࡦࠡ࡯ࡨࡷࡸࡧࡧࡦࠢࡥࡰࡴࡩ࡫ࡴ࠮ࠣࡷࡺࡩࡨࠡࡶ࡫ࡥࡹࠦࡴࡩࡧࠣࡦࡱࡵࡣ࡬ࡵࠍࠤࡨࡧ࡮ࠡࡤࡨࠤࡷ࡫ࡣࡰ࡯ࡥ࡭ࡳ࡫ࡤࠡࡶࡲࠤ࡬࡫ࡴࠡࡶ࡫ࡩࠥࡳࡥࡴࡵࡤ࡫ࡪࠦࡢࡢࡥ࡮࠲ࠏࠐࡃࡳࡻࡳࡸࡴ࠴ࡐࡳࡱࡷࡳࡨࡵ࡬࠯ࡅ࡫ࡥ࡫࡬ࡩ࡯ࡩࠍࠤ࡙ࡧ࡫ࡦࡵࠣࡥࠥࡹࡥࡵࠢࡲࡪࠥࡧࡵࡵࡪࡨࡲࡹ࡯ࡣࡢࡶࡨࡨࠥࡳࡥࡴࡵࡤ࡫ࡪࠦࡢ࡭ࡱࡦ࡯ࡸࠦࠨࡵࡪࡨࠤࡼ࡮ࡥࡢࡶࠬࠤࡦࡴࡤࠡࡣࡧࡨࡸࠦࡡࠡࡰࡸࡱࡧ࡫ࡲࠋࠢࡲࡪࠥࡸࡡ࡯ࡦࡲࡱࡱࡿࠠࡨࡧࡱࡩࡷࡧࡴࡦࡦࠣࡦࡱࡵࡣ࡬ࡵࠣࠬࡹ࡮ࡥࠡࡥ࡫ࡥ࡫࡬ࠩ࠯ࠌࠍࡇࡷࡿࡰࡵࡱ࠱ࡔࡷࡵࡴࡰࡥࡲࡰ࠳ࡑࡄࡇࠌࠣࡅࠥࡩ࡯࡭࡮ࡨࡧࡹ࡯࡯࡯ࠢࡲࡪࠥࡹࡴࡢࡰࡧࡥࡷࡪࠠ࡬ࡧࡼࠤࡩ࡫ࡲࡪࡸࡤࡸ࡮ࡵ࡮ࠡࡨࡸࡲࡨࡺࡩࡰࡰࡶ࠲ࠏࠐ࠺ࡶࡰࡧࡳࡨࡻ࡭ࡦࡰࡷࡩࡩࡀࠠࡠࡡࡵࡩࡻ࡯ࡳࡪࡱࡱࡣࡤࠐࠢࠣࠤ़")
__all__ = [l1l1111_Krypto_ (u"࠭ࡁ࡭࡮ࡒࡶࡓࡵࡴࡩ࡫ࡱ࡫ࠬऽ"), l1l1111_Krypto_ (u"ࠧࡄࡪࡤࡪ࡫࡯࡮ࡨࠩा"), l1l1111_Krypto_ (u"ࠨࡍࡇࡊࠬि")]
__revision__ = l1l1111_Krypto_ (u"ࠤࠧࡍࡩࠪࠢी")