# coding: utf-8
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
__revision__ = l1l1111_Krypto_ (u"ࠥࠨࡎࡪࠤࠣੋ")
__all__ = [l1l1111_Krypto_ (u"ࠫࡕࡿࡴࡩࡱࡱࡓࡘ࡛ࡒࡢࡰࡧࡳࡲࡘࡎࡈࠩੌ")]
import os as l1111111l1_Krypto_
from .rng_base import l1lll1l11ll_Krypto_
class l1lll1l11l1_Krypto_(l1lll1l11ll_Krypto_):
    name = l1l1111_Krypto_ (u"ࠧࡂ࡯ࡴ࠰ࡸࡶࡦࡴࡤࡰ࡯ࡁ੍ࠦ")
    def __init__(self):
        self._read = l1111111l1_Krypto_.urandom
        l1lll1l11ll_Krypto_.__init__(self)
    def _1lll1l111l_Krypto_(self):
        self._read = None
def new(*args, **kwargs):
    return l1lll1l11l1_Krypto_(*args, **kwargs)