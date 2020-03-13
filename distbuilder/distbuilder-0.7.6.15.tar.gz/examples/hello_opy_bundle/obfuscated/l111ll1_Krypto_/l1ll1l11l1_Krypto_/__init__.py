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
__revision__ = l1l1111_Krypto_ (u"ࠣࠦࡌࡨࠩࠨਭ")
__all__ = [l1l1111_Krypto_ (u"ࠩࡱࡩࡼ࠭ਮ")]
from l111ll1_Krypto_.l1ll1l11l1_Krypto_ import l111111111_Krypto_
from l111ll1_Krypto_.l1ll1l11l1_Krypto_ import _1111lll11_Krypto_
def new(*args, **kwargs):
    l1l1111_Krypto_ (u"ࠥࠦࠧࡘࡥࡵࡷࡵࡲࠥࡧࠠࡧ࡫࡯ࡩ࠲ࡲࡩ࡬ࡧࠣࡳࡧࡰࡥࡤࡶࠣࡸ࡭ࡧࡴࠡࡱࡸࡸࡵࡻࡴࡴࠢࡦࡶࡾࡶࡴࡰࡩࡵࡥࡵ࡮ࡩࡤࡣ࡯ࡰࡾࠦࡲࡢࡰࡧࡳࡲࠦࡢࡺࡶࡨࡷ࠳ࠨࠢࠣਯ")
    return _1111lll11_Krypto_.new(*args, **kwargs)
def l1lllllll11_Krypto_():
    l1l1111_Krypto_ (u"ࠦࠧࠨࡃࡢ࡮࡯ࠤࡹ࡮ࡩࡴࠢࡺ࡬ࡪࡴࡥࡷࡧࡵࠤࡾࡵࡵࠡࡥࡤࡰࡱࠦ࡯ࡴ࠰ࡩࡳࡷࡱࠨࠪࠤࠥࠦਰ")
    _1111lll11_Krypto_.l1111ll11l_Krypto_()
def l1111l11l1_Krypto_(n):
    l1l1111_Krypto_ (u"ࠧࠨࠢࡓࡧࡷࡹࡷࡴࠠࡵࡪࡨࠤࡸࡶࡥࡤ࡫ࡩ࡭ࡪࡪࠠ࡯ࡷࡰࡦࡪࡸࠠࡰࡨࠣࡧࡷࡿࡰࡵࡱࡪࡶࡦࡶࡨࡪࡥࡤࡰࡱࡿ࠭ࡴࡶࡵࡳࡳ࡭ࠠࡳࡣࡱࡨࡴࡳࠠࡣࡻࡷࡩࡸ࠴ࠢࠣࠤ਱")
    return _1111lll11_Krypto_.l1111l11l1_Krypto_(n)