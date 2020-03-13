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
__revision__ = l1l1111_Krypto_ (u"ࠥࠨࡎࡪࠤࠣਖ਼")
import sys as l1l11l11_Krypto_
if l1l11l11_Krypto_.version_info[0] == 2 and l1l11l11_Krypto_.version_info[1] == 1:
    from l111ll1_Krypto_.l1l111ll_Krypto_.l1l1ll1l_Krypto_ import *
class l1lll1l11ll_Krypto_(object):
    def __init__(self):
        self.closed = False
        self._1lll111l11_Krypto_()
    def __del__(self):
        self.close()
    def _1lll111l11_Krypto_(self):
        data = self.read(16)
        if len(data) != 16:
            raise AssertionError(l1l1111_Krypto_ (u"ࠦࡷ࡫ࡡࡥࠢࡷࡶࡺࡴࡣࡢࡶࡨࡨࠧਗ਼"))
        l1lll1111ll_Krypto_ = self.read(16)
        if data == l1lll1111ll_Krypto_:
            raise AssertionError(l1l1111_Krypto_ (u"ࠧࡕࡓࠡࡔࡑࡋࠥࡸࡥࡵࡷࡵࡲࡪࡪࠠࡥࡷࡳࡰ࡮ࡩࡡࡵࡧࠣࡨࡦࡺࡡࠣਜ਼"))
    def __enter__(self):
        pass
    def __exit__(self):
        l1l1111_Krypto_ (u"ࠨࠢࠣࡒࡈࡔࠥ࠹࠴࠴ࠢࡶࡹࡵࡶ࡯ࡳࡶࠥࠦࠧੜ")
        self.close()
    def close(self):
        if not self.closed:
            self._1lll1l111l_Krypto_()
        self.closed = True
    def flush(self):
        pass
    def read(self, l11l1111l1_Krypto_=-1):
        l1l1111_Krypto_ (u"ࠢࠣࠤࡕࡩࡹࡻࡲ࡯ࠢࡑࠤࡧࡿࡴࡦࡵࠣࡪࡷࡵ࡭ࠡࡶ࡫ࡩࠥࡘࡎࡈ࠰ࠥࠦࠧ੝")
        if self.closed:
            raise ValueError(l1l1111_Krypto_ (u"ࠣࡋ࠲ࡓࠥࡵࡰࡦࡴࡤࡸ࡮ࡵ࡮ࠡࡱࡱࠤࡨࡲ࡯ࡴࡧࡧࠤ࡫࡯࡬ࡦࠤਫ਼"))
        if not isinstance(l11l1111l1_Krypto_, int):
            raise TypeError(l1l1111_Krypto_ (u"ࠤࡤࡲࠥ࡯࡮ࡵࡧࡪࡩࡷࠦࡩࡴࠢࡵࡩࡶࡻࡩࡳࡧࡧࠦ੟"))
        if l11l1111l1_Krypto_ < 0:
            raise ValueError(l1l1111_Krypto_ (u"ࠥࡧࡦࡴ࡮ࡰࡶࠣࡶࡪࡧࡤࠡࡶࡲࠤࡪࡴࡤࠡࡱࡩࠤ࡮ࡴࡦࡪࡰ࡬ࡸࡪࠦࡳࡵࡴࡨࡥࡲࠨ੠"))
        elif l11l1111l1_Krypto_ == 0:
            return l1l1111_Krypto_ (u"ࠦࠧ੡")
        data = self._read(l11l1111l1_Krypto_)
        if len(data) != l11l1111l1_Krypto_:
            raise AssertionError(l1l1111_Krypto_ (u"ࠧࠫࡳࠡࡲࡵࡳࡩࡻࡣࡦࡦࠣࡸࡷࡻ࡮ࡤࡣࡷࡩࡩࠦ࡯ࡶࡶࡳࡹࡹࠦࠨࡳࡧࡴࡹࡪࡹࡴࡦࡦࠣࠩࡩ࠲ࠠࡨࡱࡷࠤࠪࡪࠩࠣ੢") % (self.name, l11l1111l1_Krypto_, len(data)))
        return data
    def _1lll1l111l_Krypto_(self):
        raise NotImplementedError(l1l1111_Krypto_ (u"ࠨࡣࡩ࡫࡯ࡨࠥࡩ࡬ࡢࡵࡶࠤࡲࡻࡳࡵࠢ࡬ࡱࡵࡲࡥ࡮ࡧࡱࡸࠥࡺࡨࡪࡵࠥ੣"))
    def _read(self, l11l1111l1_Krypto_):
        raise NotImplementedError(l1l1111_Krypto_ (u"ࠢࡤࡪ࡬ࡰࡩࠦࡣ࡭ࡣࡶࡷࠥࡳࡵࡴࡶࠣ࡭ࡲࡶ࡬ࡦ࡯ࡨࡲࡹࠦࡴࡩ࡫ࡶࠦ੤"))