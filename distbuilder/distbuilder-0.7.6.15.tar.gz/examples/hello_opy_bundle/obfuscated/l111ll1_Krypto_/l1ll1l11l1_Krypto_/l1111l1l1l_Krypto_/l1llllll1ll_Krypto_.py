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
__revision__ = l1l1111_Krypto_ (u"ࠦࠩࡏࡤࠥࠤ਷")
import sys as l1l11l11_Krypto_
if l1l11l11_Krypto_.version_info[0] is 2 and  l1l11l11_Krypto_.version_info[1] is 1:
    from l111ll1_Krypto_.l1l111ll_Krypto_.l1l1ll1l_Krypto_ import *
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
import struct as l1l1l1ll11_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l111l1ll_Krypto_ import l1llll11lll_Krypto_, l1llll11l1l_Krypto_, l1llll1l11l_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_ import Counter
from l111ll1_Krypto_.l11111l_Krypto_ import l111lll_Krypto_
from . import l1llllll1l1_Krypto_
class l1llll1ll11_Krypto_(object):
    l1l1111_Krypto_ (u"ࠧࠨࠢࡕࡪࡨࠤࡋࡵࡲࡵࡷࡱࡥࠥࠨࡧࡦࡰࡨࡶࡦࡺ࡯ࡳࠤࠍࠎࠥࠦࠠࠡࡖ࡫࡭ࡸࠦࡩࡴࠢࡸࡷࡪࡪࠠࡪࡰࡷࡩࡷࡴࡡ࡭࡮ࡼࠤࡧࡿࠠࡵࡪࡨࠤࡋࡵࡲࡵࡷࡱࡥࠥࡖࡒࡏࡉࠣࡸࡴࠦࡧࡦࡰࡨࡶࡦࡺࡥࠡࡣࡵࡦ࡮ࡺࡲࡢࡴࡼࠤࡦࡳ࡯ࡶࡰࡷࡷࠏࠦࠠࠡࠢࡲࡪࠥࡶࡳࡦࡷࡧࡳࡷࡧ࡮ࡥࡱࡰࠤࡩࡧࡴࡢࠢࡩࡶࡴࡳࠠࡢࠢࡶࡱࡦࡲ࡬ࡦࡴࠣࡥࡲࡵࡵ࡯ࡶࠣࡳ࡫ࠦࡳࡦࡧࡧࠤࡩࡧࡴࡢ࠰ࠍࠎࠥࠦࠠࠡࡖ࡫ࡩࠥࡵࡵࡵࡲࡸࡸࠥ࡯ࡳࠡࡩࡨࡲࡪࡸࡡࡵࡧࡧࠤࡧࡿࠠࡳࡷࡱࡲ࡮ࡴࡧࠡࡃࡈࡗ࠲࠸࠵࠷ࠢ࡬ࡲࠥࡩ࡯ࡶࡰࡷࡩࡷࠦ࡭ࡰࡦࡨࠤࡦࡴࡤࠡࡴࡨ࠱ࡰ࡫ࡹࡪࡰࡪࠎࠥࠦࠠࠡࡣࡩࡸࡪࡸࠠࡦࡸࡨࡶࡾࠦ࡭ࡦࡤ࡬ࡦࡾࡺࡥࠡࠪ࠵࠮࠯࠷࠶ࠡࡤ࡯ࡳࡨࡱࡳࠪࠢࡲࡪࠥࡵࡵࡵࡲࡸࡸ࠳ࠐࠠࠡࠢࠣࠦࠧࠨਸ")
    block_size = l111lll_Krypto_.block_size
    l111l1l_Krypto_ = 32
    l1llll11l11_Krypto_ = 2**16
    _1llll1111l_Krypto_ = b(l1l1111_Krypto_ (u"ࠨ࡜࠱ࠤਹ")) * block_size * 4096
    def __init__(self):
        self.l1lll1llll1_Krypto_ = Counter.new(l1llll111l1_Krypto_=self.block_size*8, l1llll11111_Krypto_=0, l1lll1ll111_Krypto_=True)
        self.key = None
        self.l1lll1lllll_Krypto_ = l1llll11l1l_Krypto_(self.block_size)
        assert (1 << self.l1lll1lllll_Krypto_) == self.block_size
        self.l1lll1lll1l_Krypto_ = l1llll1l11l_Krypto_(self.l111l1l_Krypto_, self.block_size)
        assert self.l111l1l_Krypto_ == self.l1lll1lll1l_Krypto_ * self.block_size
        self.l1llll1l111_Krypto_ = self.l1llll11l11_Krypto_ * self.block_size
    def l1lllll111l_Krypto_(self, l1ll1111l_Krypto_):
        if self.key is None:
            self.key = b(l1l1111_Krypto_ (u"ࠢ࡝࠲ࠥ਺")) * self.l111l1l_Krypto_
        self._1llll11ll1_Krypto_(l1llllll1l1_Krypto_.new(self.key + l1ll1111l_Krypto_).digest())
        self.l1lll1llll1_Krypto_()
        assert len(self.key) == self.l111l1l_Krypto_
    def l1llll1llll_Krypto_(self, bytes):
        assert bytes >= 0
        l1lll1ll11l_Krypto_ = bytes >> 20
        remainder = bytes & ((1<<20)-1)
        l111l111ll_Krypto_ = []
        for i in range(l1lll1ll11l_Krypto_):
            l111l111ll_Krypto_.append(self._1lll1ll1l1_Krypto_(1<<20))
        l111l111ll_Krypto_.append(self._1lll1ll1l1_Krypto_(remainder))
        return b(l1l1111_Krypto_ (u"ࠣࠤ਻")).join(l111l111ll_Krypto_)
    def _1llll11ll1_Krypto_(self, key):
        self.key = key
        self._1ll1111_Krypto_ = l111lll_Krypto_.new(key, l111lll_Krypto_.l1llllll_Krypto_, l1lll1llll1_Krypto_=self.l1lll1llll1_Krypto_)
    def _1lll1ll1l1_Krypto_(self, bytes):
        if not (0 <= bytes <= self.l1llll1l111_Krypto_):
            raise AssertionError(l1l1111_Krypto_ (u"ࠤ࡜ࡳࡺࠦࡣࡢࡰࡱࡳࡹࠦࡡࡴ࡭ࠣࡪࡴࡸࠠ࡮ࡱࡵࡩࠥࡺࡨࡢࡰࠣ࠵ࠥࡓࡩࡃࠢࡲࡪࠥࡪࡡࡵࡣࠣࡴࡪࡸࠠࡳࡧࡴࡹࡪࡹࡴ਼ࠣ"))
        l1lll1lll11_Krypto_ = l1llll11lll_Krypto_(bytes, self.l1lll1lllll_Krypto_)
        l111l111ll_Krypto_ = self._1llll111ll_Krypto_(l1lll1lll11_Krypto_)[:bytes]
        self._1llll11ll1_Krypto_(self._1llll111ll_Krypto_(self.l1lll1lll1l_Krypto_))
        assert len(l111l111ll_Krypto_) == bytes
        assert len(self.key) == self.l111l1l_Krypto_
        return l111l111ll_Krypto_
    def _1llll111ll_Krypto_(self, l1lll1lll11_Krypto_):
        if self.key is None:
            raise AssertionError(l1l1111_Krypto_ (u"ࠥ࡫ࡪࡴࡥࡳࡣࡷࡳࡷࠦ࡭ࡶࡵࡷࠤࡧ࡫ࠠࡴࡧࡨࡨࡪࡪࠠࡣࡧࡩࡳࡷ࡫ࠠࡶࡵࡨࠦ਽"))
        assert 0 <= l1lll1lll11_Krypto_ <= self.l1llll11l11_Krypto_
        l111l111ll_Krypto_ = []
        for i in range(l1lll1lll11_Krypto_ >> 12):
            l111l111ll_Krypto_.append(self._1ll1111_Krypto_.l1_Krypto_(self._1llll1111l_Krypto_))
        l1lll1ll1ll_Krypto_ = (l1lll1lll11_Krypto_ & 4095) << self.l1lll1lllll_Krypto_
        l111l111ll_Krypto_.append(self._1ll1111_Krypto_.l1_Krypto_(self._1llll1111l_Krypto_[:l1lll1ll1ll_Krypto_]))
        return b(l1l1111_Krypto_ (u"ࠦࠧਾ")).join(l111l111ll_Krypto_)