# -*- coding: ascii -*-
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
class l11l11l_Krypto_(Warning):
    l1l1111_Krypto_ (u"ࠣࠤࠥࡆࡦࡹࡥࠡࡥ࡯ࡥࡸࡹࠠࡧࡱࡵࠤࡕࡿࡃࡳࡻࡳࡸࡴࠦࡷࡢࡴࡱ࡭ࡳ࡭ࡳࠣࠤࠥࠠ")
class l11ll1l_Krypto_(DeprecationWarning, l11l11l_Krypto_):
    l1l1111_Krypto_ (u"ࠤࠥࠦࡇࡧࡳࡦࠢࡓࡽࡈࡸࡹࡱࡶࡲࠤࡉ࡫ࡰࡳࡧࡦࡥࡹ࡯࡯࡯࡙ࡤࡶࡳ࡯࡮ࡨࠢࡦࡰࡦࡹࡳࠣࠤࠥࠡ")
class l11l1l1_Krypto_(RuntimeWarning, l11l11l_Krypto_):
    l1l1111_Krypto_ (u"ࠥࠦࠧࡈࡡࡴࡧࠣࡔࡾࡉࡲࡺࡲࡷࡳࠥࡘࡵ࡯ࡶ࡬ࡱࡪ࡝ࡡࡳࡰ࡬ࡲ࡬ࠦࡣ࡭ࡣࡶࡷࠧࠨࠢࠢ")
class l11ll11_Krypto_(l11ll1l_Krypto_):
    l1l1111_Krypto_ (u"ࠦࠧࠨࡉࡴࡵࡸࡩࡩࠦࡷࡩࡧࡱࠤࡈࡸࡹࡱࡶࡲ࠲࡚ࡺࡩ࡭࠰ࡵࡥࡳࡪࡰࡰࡱ࡯࠲ࡗࡧ࡮ࡥࡱࡰࡔࡴࡵ࡬ࠡ࡫ࡶࠤ࡮ࡴࡳࡵࡣࡱࡸ࡮ࡧࡴࡦࡦ࠱ࠦࠧࠨࠣ")
class l11llll_Krypto_(l11l1l1_Krypto_):
    l1l1111_Krypto_ (u"ࠧࠨࠢࡘࡣࡵࡲ࡮ࡴࡧࠡࡨࡲࡶࠥࡽࡨࡦࡰࠣࡸ࡭࡫ࠠࡴࡻࡶࡸࡪࡳࠠࡤ࡮ࡲࡧࡰࠦ࡭ࡰࡸࡨࡷࠥࡨࡡࡤ࡭ࡺࡥࡷࡪࡳ࠯ࠤࠥࠦࠤ")
class l11l111_Krypto_(l11ll1l_Krypto_):
    l1l1111_Krypto_ (u"ࠨࠢࠣࡋࡶࡷࡺ࡫ࡤࠡࡹ࡫ࡩࡳࠦࡃࡳࡻࡳࡸࡴ࠴ࡕࡵ࡫࡯࠲ࡳࡻ࡭ࡣࡧࡵ࠲࡬࡫ࡴࡓࡣࡱࡨࡴࡳࡎࡶ࡯ࡥࡩࡷࠦࡩࡴࠢ࡬ࡲࡻࡵ࡫ࡦࡦ࠱ࠦࠧࠨࠥ")
class l11l1ll_Krypto_(l11l1l1_Krypto_):
    l1l1111_Krypto_ (u"ࠢࠣࠤ࡚ࡥࡷࡴࡩ࡯ࡩࠣࡪࡴࡸࠠࡸࡪࡨࡲࠥࡥࡦࡢࡵࡷࡱࡦࡺࡨࠡ࡫ࡶࠤࡧࡻࡩ࡭ࡶࠣࡻ࡮ࡺࡨࡰࡷࡷࠤࡲࡶࡺࡠࡲࡲࡻࡲࡥࡳࡦࡥࠥࠦࠧࠦ")
import warnings as _warnings
_warnings.filterwarnings(l1l1111_Krypto_ (u"ࠨࡣ࡯ࡻࡦࡿࡳࠨࠧ"), category=l11llll_Krypto_, append=1)