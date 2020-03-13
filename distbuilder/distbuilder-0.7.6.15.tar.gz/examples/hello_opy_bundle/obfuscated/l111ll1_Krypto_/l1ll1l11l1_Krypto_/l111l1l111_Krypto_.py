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
l1l1111_Krypto_ (u"ࠨࠢࠣࡃࠣࡧࡷࡿࡰࡵࡱࡪࡶࡦࡶࡨࡪࡥࡤࡰࡱࡿࠠࡴࡶࡵࡳࡳ࡭ࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡱࡩࠤࡕࡿࡴࡩࡱࡱࠫࡸࠦࡳࡵࡣࡱࡨࡦࡸࡤࠡࠤࡵࡥࡳࡪ࡯࡮ࠤࠣࡱࡴࡪࡵ࡭ࡧ࠱ࠦࠧࠨਈ")
__revision__ = l1l1111_Krypto_ (u"ࠢࠥࡋࡧࠨࠧਉ")
__all__ = [l1l1111_Krypto_ (u"ࠨࡕࡷࡶࡴࡴࡧࡓࡣࡱࡨࡴࡳࠧਊ"), l1l1111_Krypto_ (u"ࠩࡪࡩࡹࡸࡡ࡯ࡦࡥ࡭ࡹࡹࠧ਋"), l1l1111_Krypto_ (u"ࠪࡶࡦࡴࡤࡳࡣࡱ࡫ࡪ࠭਌"), l1l1111_Krypto_ (u"ࠫࡷࡧ࡮ࡥ࡫ࡱࡸࠬ਍"), l1l1111_Krypto_ (u"ࠬࡩࡨࡰ࡫ࡦࡩࠬ਎"), l1l1111_Krypto_ (u"࠭ࡳࡩࡷࡩࡪࡱ࡫ࠧਏ"), l1l1111_Krypto_ (u"ࠧࡴࡣࡰࡴࡱ࡫ࠧਐ")]
from l111ll1_Krypto_ import l1ll1l11l1_Krypto_
import sys as l1l11l11_Krypto_
if l1l11l11_Krypto_.version_info[0] == 2 and l1l11l11_Krypto_.version_info[1] == 1:
    from l111ll1_Krypto_.l1l111ll_Krypto_.l1l1ll1l_Krypto_ import *
class l111l1l11l_Krypto_(object):
    def __init__(self, rng=None, l1l11ll1ll_Krypto_=None):
        if l1l11ll1ll_Krypto_ is None and rng is None:
            self._11l1lll11_Krypto_ = None
        elif l1l11ll1ll_Krypto_ is not None and rng is None:
            self._11l1lll11_Krypto_ = l1l11ll1ll_Krypto_
        elif l1l11ll1ll_Krypto_ is None and rng is not None:
            self._11l1lll11_Krypto_ = rng.read
        else:
            raise ValueError(l1l1111_Krypto_ (u"ࠣࡅࡤࡲࡳࡵࡴࠡࡵࡳࡩࡨ࡯ࡦࡺࠢࡥࡳࡹ࡮ࠠࠨࡴࡱ࡫ࠬࠦࡡ࡯ࡦࠣࠫࡷࡧ࡮ࡥࡨࡸࡲࡨ࠭ࠢ਑"))
    def l111l1111l_Krypto_(self, k):
        l1l1111_Krypto_ (u"ࠤࠥࠦࡗ࡫ࡴࡶࡴࡱࠤࡦࠦࡰࡺࡶ࡫ࡳࡳࠦ࡬ࡰࡰࡪࠤ࡮ࡴࡴࡦࡩࡨࡶࠥࡽࡩࡵࡪࠣ࡯ࠥࡸࡡ࡯ࡦࡲࡱࠥࡨࡩࡵࡵ࠱ࠦࠧࠨ਒")
        if self._11l1lll11_Krypto_ is None:
            self._11l1lll11_Krypto_ = l1ll1l11l1_Krypto_.new().read
        mask = (1 << k) - 1
        return mask & l1ll111ll1_Krypto_(self._11l1lll11_Krypto_(l1ll11111_Krypto_(k, 8)))
    def l111l1ll11_Krypto_(self, *args):
        l1l1111_Krypto_ (u"ࠥࠦࠧࡸࡡ࡯ࡦࡵࡥࡳ࡭ࡥࠩ࡝ࡶࡸࡦࡸࡴ࠭࡟ࠣࡷࡹࡵࡰ࡜࠮ࠣࡷࡹ࡫ࡰ࡞ࠫ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࠥࡧࠠࡳࡣࡱࡨࡴࡳ࡬ࡺ࠯ࡶࡩࡱ࡫ࡣࡵࡧࡧࠤࡪࡲࡥ࡮ࡧࡱࡸࠥ࡬ࡲࡰ࡯ࠣࡶࡦࡴࡧࡦࠪࡶࡸࡦࡸࡴ࠭ࠢࡶࡸࡴࡶࠬࠡࡵࡷࡩࡵ࠯࠮ࠣࠤࠥਓ")
        if len(args) == 3:
            (start, stop, step) = args
        elif len(args) == 2:
            (start, stop) = args
            step = 1
        elif len(args) == 1:
            (stop,) = args
            start = 0
            step = 1
        else:
            raise TypeError(l1l1111_Krypto_ (u"ࠦࡷࡧ࡮ࡥࡴࡤࡲ࡬࡫ࠠࡦࡺࡳࡩࡨࡺࡥࡥࠢࡤࡸࠥࡳ࡯ࡴࡶࠣ࠷ࠥࡧࡲࡨࡷࡰࡩࡳࡺࡳ࠭ࠢࡪࡳࡹࠦࠥࡥࠤਔ") % (len(args),))
        if (not isinstance(start, int)
                or not isinstance(stop, int)
                or not isinstance(step, int)):
            raise TypeError(l1l1111_Krypto_ (u"ࠧࡸࡡ࡯ࡦࡵࡥࡳ࡭ࡥࠡࡴࡨࡵࡺ࡯ࡲࡦࡵࠣ࡭ࡳࡺࡥࡨࡧࡵࠤࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢਕ"))
        if step == 0:
            raise ValueError(l1l1111_Krypto_ (u"ࠨࡲࡢࡰࡧࡶࡦࡴࡧࡦࠢࡶࡸࡪࡶࠠࡢࡴࡪࡹࡲ࡫࡮ࡵࠢࡰࡹࡸࡺࠠ࡯ࡱࡷࠤࡧ࡫ࠠࡻࡧࡵࡳࠧਖ"))
        l111l1l1l1_Krypto_ = l1ll11111_Krypto_(stop - start, step)
        if l111l1l1l1_Krypto_ < 0:
            l111l1l1l1_Krypto_ = 0
        if l111l1l1l1_Krypto_ < 1:
            raise ValueError(l1l1111_Krypto_ (u"ࠢࡦ࡯ࡳࡸࡾࠦࡲࡢࡰࡪࡩࠥ࡬࡯ࡳࠢࡵࡥࡳࡪࡲࡢࡰࡪࡩ࠭ࠫࡲ࠭ࠢࠨࡶ࠱ࠦࠥࡳࠫࠥਗ") % (start, stop, step))
        r = l111l1l1l1_Krypto_
        while r >= l111l1l1l1_Krypto_:
            r = self.l111l1111l_Krypto_(size(l111l1l1l1_Krypto_))
        return start + (step * r)
    def l111l111l1_Krypto_(self, a, b):
        l1l1111_Krypto_ (u"ࠣࠤࠥࡖࡪࡺࡵࡳࡰࠣࡥࠥࡸࡡ࡯ࡦࡲࡱࠥ࡯࡮ࡵࡧࡪࡩࡷࠦࡎࠡࡵࡸࡧ࡭ࠦࡴࡩࡣࡷࠤࡦࠦ࠼࠾ࠢࡑࠤࡁࡃࠠࡣ࠰ࠥࠦࠧਘ")
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError(l1l1111_Krypto_ (u"ࠤࡵࡥࡳࡪࡩ࡯ࡶࠣࡶࡪࡷࡵࡪࡴࡨࡷࠥ࡯࡮ࡵࡧࡪࡩࡷࠦࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤਙ"))
        l11l1111l1_Krypto_ = self.l111l1ll11_Krypto_(a, b+1)
        assert a <= l11l1111l1_Krypto_ <= b
        return l11l1111l1_Krypto_
    def l1l1111ll_Krypto_(self, seq):
        l1l1111_Krypto_ (u"ࠥࠦࠧࡘࡥࡵࡷࡵࡲࠥࡧࠠࡳࡣࡱࡨࡴࡳࠠࡦ࡮ࡨࡱࡪࡴࡴࠡࡨࡵࡳࡲࠦࡡࠡࠪࡱࡳࡳ࠳ࡥ࡮ࡲࡷࡽ࠮ࠦࡳࡦࡳࡸࡩࡳࡩࡥ࠯ࠌࠍࠤࠥࠦࠠࠡࠢࠣࠤࡎ࡬ࠠࡵࡪࡨࠤࡸ࡫ࡱࡦࡰࡦࡩࠥ࡯ࡳࠡࡧࡰࡴࡹࡿࠬࠡࡴࡤ࡭ࡸ࡫ࡳࠡࡋࡱࡨࡪࡾࡅࡳࡴࡲࡶ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥਚ")
        if len(seq) == 0:
            raise IndexError(l1l1111_Krypto_ (u"ࠦࡪࡳࡰࡵࡻࠣࡷࡪࡷࡵࡦࡰࡦࡩࠧਛ"))
        return seq[self.l111l1ll11_Krypto_(len(seq))]
    def l111l1l1ll_Krypto_(self, x):
        l1l1111_Krypto_ (u"ࠧࠨࠢࡔࡪࡸࡪ࡫ࡲࡥࠡࡶ࡫ࡩࠥࡹࡥࡲࡷࡨࡲࡨ࡫ࠠࡪࡰࠣࡴࡱࡧࡣࡦ࠰ࠥࠦࠧਜ")
        items = list(x)
        for i in range(len(x)):
            x[i] = items.pop(self.l111l1ll11_Krypto_(len(items)))
    def l111l11lll_Krypto_(self, l111l11ll1_Krypto_, k):
        l1l1111_Krypto_ (u"ࠨࠢࠣࡔࡨࡸࡺࡸ࡮ࠡࡣࠣ࡯࠲ࡲࡥ࡯ࡩࡷ࡬ࠥࡲࡩࡴࡶࠣࡳ࡫ࠦࡵ࡯࡫ࡴࡹࡪࠦࡥ࡭ࡧࡰࡩࡳࡺࡳࠡࡥ࡫ࡳࡸ࡫࡮ࠡࡨࡵࡳࡲࠦࡴࡩࡧࠣࡴࡴࡶࡵ࡭ࡣࡷ࡭ࡴࡴࠠࡴࡧࡴࡹࡪࡴࡣࡦ࠰ࠥࠦࠧਝ")
        l111l1l1l1_Krypto_ = len(l111l11ll1_Krypto_)
        if k > l111l1l1l1_Krypto_:
            raise ValueError(l1l1111_Krypto_ (u"ࠢࡴࡣࡰࡴࡱ࡫ࠠ࡭ࡣࡵ࡫ࡪࡸࠠࡵࡪࡤࡲࠥࡶ࡯ࡱࡷ࡯ࡥࡹ࡯࡯࡯ࠤਞ"))
        l111l111ll_Krypto_ = []
        l111l11l1l_Krypto_ = {}
        for i in range(k):
            r = None
            while r is None or r in l111l11l1l_Krypto_:
                r = self.l111l1ll11_Krypto_(l111l1l1l1_Krypto_)
            l111l111ll_Krypto_.append(l111l11ll1_Krypto_[r])
            l111l11l1l_Krypto_[r] = 1
        return l111l111ll_Krypto_
_111l11l11_Krypto_ = l111l1l11l_Krypto_()
l111l1111l_Krypto_ = _111l11l11_Krypto_.l111l1111l_Krypto_
l111l1ll11_Krypto_ = _111l11l11_Krypto_.l111l1ll11_Krypto_
l111l111l1_Krypto_ = _111l11l11_Krypto_.l111l111l1_Krypto_
l1l1111ll_Krypto_ = _111l11l11_Krypto_.l1l1111ll_Krypto_
l111l1l1ll_Krypto_ = _111l11l11_Krypto_.l111l1l1ll_Krypto_
l111l11lll_Krypto_ = _111l11l11_Krypto_.l111l11lll_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l111l1ll_Krypto_ import l1ll11111_Krypto_, l1ll111ll1_Krypto_, l1ll1lllll_Krypto_, size