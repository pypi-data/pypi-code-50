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
__revision__ = l1l1111_Krypto_ (u"ࠦࠩࡏࡤࠥࠤ੓")
__all__ = [l1l1111_Krypto_ (u"ࠬࡊࡥࡷࡗࡕࡥࡳࡪ࡯࡮ࡔࡑࡋࠬ੔")]
import errno as l1lll11l111_Krypto_
import os as l1111111l1_Krypto_
import stat as l1lll11l1l1_Krypto_
from .rng_base import l1lll1l11ll_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import b
class l1lll111ll1_Krypto_(l1lll1l11ll_Krypto_):
    def __init__(self, l1lll111lll_Krypto_=None):
        if l1lll111lll_Krypto_ is None:
            self.name = l1l1111_Krypto_ (u"ࠨ࠯ࡥࡧࡹ࠳ࡺࡸࡡ࡯ࡦࡲࡱࠧ੕")
        else:
            self.name = l1lll111lll_Krypto_
        f = open(self.name, l1l1111_Krypto_ (u"ࠢࡳࡤࠥ੖"), 0)
        l1lll11l11l_Krypto_ = l1111111l1_Krypto_.fstat(f.fileno())[l1lll11l1l1_Krypto_.ST_MODE]
        if not l1lll11l1l1_Krypto_.S_ISCHR(l1lll11l11l_Krypto_):
            f.close()
            raise TypeError(l1l1111_Krypto_ (u"ࠣࠧࡵࠤ࡮ࡹࠠ࡯ࡱࡷࠤࡦࠦࡣࡩࡣࡵࡥࡨࡺࡥࡳࠢࡶࡴࡪࡩࡩࡢ࡮ࠣࡨࡪࡼࡩࡤࡧࠥ੗") % (self.name,))
        self.__1lll111l1l_Krypto_ = f
        l1lll1l11ll_Krypto_.__init__(self)
    def _1lll1l111l_Krypto_(self):
        self.__1lll111l1l_Krypto_.close()
    def _read(self, l11l1111l1_Krypto_):
        data = b(l1l1111_Krypto_ (u"ࠤࠥ੘"))
        while len(data) < l11l1111l1_Krypto_:
            try:
                d = self.__1lll111l1l_Krypto_.read(l11l1111l1_Krypto_ - len(data))
            except IOError as e:
                if e.l1lll11l111_Krypto_ == l1lll11l111_Krypto_.EINTR:
                    continue
                raise
            if d is None:
                return data
            if len(d) == 0:
                return data
            data += d
        return data
def new(*args, **kwargs):
    return l1lll111ll1_Krypto_(*args, **kwargs)