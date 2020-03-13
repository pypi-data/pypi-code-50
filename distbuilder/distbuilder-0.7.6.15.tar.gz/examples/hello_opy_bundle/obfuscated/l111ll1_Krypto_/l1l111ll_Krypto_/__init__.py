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
l1l1111_Krypto_ (u"ࠨࠢࠣࡏ࡬ࡷࡨ࡫࡬࡭ࡣࡱࡩࡴࡻࡳࠡ࡯ࡲࡨࡺࡲࡥࡴࠌࠍࡇࡴࡴࡴࡢ࡫ࡱࡷࠥࡻࡳࡦࡨࡸࡰࠥࡳ࡯ࡥࡷ࡯ࡩࡸࠦࡴࡩࡣࡷࠤࡩࡵ࡮ࠨࡶࠣࡦࡪࡲ࡯࡯ࡩࠣ࡭ࡳࡺ࡯ࠡࡣࡱࡽࠥࡵࡦࠡࡶ࡫ࡩࠏࡵࡴࡩࡧࡵࠤࡈࡸࡹࡱࡶࡲ࠲࠯ࠦࡳࡶࡤࡳࡥࡨࡱࡡࡨࡧࡶ࠲ࠏࠐࡃࡳࡻࡳࡸࡴ࠴ࡕࡵ࡫࡯࠲ࡳࡻ࡭ࡣࡧࡵࠤࠥࠦࠠࠡࠢࠣࠤࡓࡻ࡭ࡣࡧࡵ࠱ࡹ࡮ࡥࡰࡴࡨࡸ࡮ࡩࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࡵࠣࠬࡵࡸࡩ࡮ࡣ࡯࡭ࡹࡿࠠࡵࡧࡶࡸ࡮ࡴࡧ࠭ࠢࡨࡸࡨ࠴ࠩࠋࡅࡵࡽࡵࡺ࡯࠯ࡗࡷ࡭ࡱ࠴ࡲࡢࡰࡧࡴࡴࡵ࡬ࠡࠢࠣࠤࠥࠦࡒࡢࡰࡧࡳࡲࠦ࡮ࡶ࡯ࡥࡩࡷࠦࡧࡦࡰࡨࡶࡦࡺࡩࡰࡰࠍࡇࡷࡿࡰࡵࡱ࠱࡙ࡹ࡯࡬࠯ࡔࡉࡇ࠶࠽࠵࠲ࠢࠣࠤࠥࠦࠠࠡࡅࡲࡲࡻ࡫ࡲࡵࡵࠣࡦࡪࡺࡷࡦࡧࡱࠤ࠶࠸࠸࠮ࡤ࡬ࡸࠥࡱࡥࡺࡵࠣࡥࡳࡪࠠࡩࡷࡰࡥࡳ࠳ࡲࡦࡣࡧࡥࡧࡲࡥࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡳࡵࡴ࡬ࡲ࡬ࡹࠠࡰࡨࠣࡻࡴࡸࡤࡴ࠰ࠍࡇࡷࡿࡰࡵࡱ࠱࡙ࡹ࡯࡬࠯ࡣࡶࡲ࠶ࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡏ࡬ࡲ࡮ࡳࡡ࡭ࠢࡶࡹࡵࡶ࡯ࡳࡶࠣࡪࡴࡸࠠࡂࡕࡑ࠲࠶ࠦࡄࡆࡔࠣࡩࡳࡩ࡯ࡥ࡫ࡱ࡫ࠏࠐࠢࠣࠤ⋜")
__all__ = [l1l1111_Krypto_ (u"ࠧࡳࡣࡱࡨࡵࡵ࡯࡭ࠩ⋝"), l1l1111_Krypto_ (u"ࠨࡔࡉࡇ࠶࠽࠵࠲ࠩ⋞"), l1l1111_Krypto_ (u"ࠩࡱࡹࡲࡨࡥࡳࠩ⋟"), l1l1111_Krypto_ (u"ࠪࡷࡹࡸࡸࡰࡴࠪ⋠"), l1l1111_Krypto_ (u"ࠫࡦࡹ࡮࠲ࠩ⋡") ]
__revision__ = l1l1111_Krypto_ (u"ࠧࠪࡉࡥࠦࠥ⋢")