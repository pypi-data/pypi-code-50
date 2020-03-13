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
l1l1111_Krypto_ (u"ࠧࠨࠢ࡝ࠌࡖࡌࡆࡥࡤ࠮࠴࠸࠺ࠥ࡮ࡡࡴࡪࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥ࡯࡭ࡱ࡮ࡨࡱࡪࡴࡴࡢࡶ࡬ࡳࡳ࠴ࠊࠋࡖ࡫࡭ࡸࠦ࡭ࡰࡦࡸࡰࡪࠦࡳࡩࡱࡸࡰࡩࠦࡣࡰ࡯ࡳࡰࡾࠦࡷࡪࡶ࡫ࠤࡕࡋࡐࠡ࠴࠷࠻࠳ࠐࠢࠣࠤਿ")
__revision__ = l1l1111_Krypto_ (u"ࠨࠤࡊࡦࠧࠦੀ")
__all__ = [l1l1111_Krypto_ (u"ࠧ࡯ࡧࡺࠫੁ"), l1l1111_Krypto_ (u"ࠨࡦ࡬࡫ࡪࡹࡴࡠࡵ࡬ࡾࡪ࠭ੂ")]
import sys as l1l11l11_Krypto_
if l1l11l11_Krypto_.version_info[0] == 2 and l1l11l11_Krypto_.version_info[1] == 1:
    from l111ll1_Krypto_.l1l111ll_Krypto_.l1l1ll1l_Krypto_ import *
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
from binascii import b2a_hex as l1llll1l1l1_Krypto_
from l111ll1_Krypto_.l1lll1ll1_Krypto_ import l1lll1ll11_Krypto_
assert l1lll1ll11_Krypto_.digest_size == 32
class _1lll1l1ll1_Krypto_(object):
    l1l1111_Krypto_ (u"ࠤࠥࠦࡘࡎࡁ࠮࠴࠸࠺࠱ࠦࡤࡰࡷࡥࡰࡪࡪ࠮ࠋࠌࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹࠠࡔࡊࡄ࠱࠷࠻࠶ࠩࡕࡋࡅ࠲࠸࠵࠷ࠪࡧࡥࡹࡧࠩࠪ࠰ࠍࠤࠥࠦࠠࠣࠤࠥ੃")
    digest_size = l1lll1ll11_Krypto_.digest_size
    _1lll1l1lll_Krypto_ = object()
    def __init__(self, l1lll1l1l1l_Krypto_, l1lll1l1l11_Krypto_):
        if l1lll1l1l1l_Krypto_ is not self._1lll1l1lll_Krypto_:
            raise AssertionError(l1l1111_Krypto_ (u"ࠥࡈࡴࠦ࡮ࡰࡶࠣ࡭ࡳࡹࡴࡢࡰࡷ࡭ࡦࡺࡥࠡࡶ࡫࡭ࡸࠦࡣ࡭ࡣࡶࡷࠥࡪࡩࡳࡧࡦࡸࡱࡿ࠮ࠡࠢࡘࡷࡪࠦࠥࡴ࠰ࡱࡩࡼ࠮ࠩࠣ੄") % (__name__,))
        self._1llll1ll1l_Krypto_ = l1lll1l1l11_Krypto_
    def copy(self):
        l1l1111_Krypto_ (u"ࠦࠧࠨࡒࡦࡶࡸࡶࡳࠦࡡࠡࡥࡲࡴࡾࠦ࡯ࡧࠢࡷ࡬࡮ࡹࠠࡩࡣࡶ࡬࡮ࡴࡧࠡࡱࡥ࡮ࡪࡩࡴࠣࠤࠥ੅")
        return _1lll1l1ll1_Krypto_(l1llllll1l1_Krypto_._1lll1l1lll_Krypto_, self._1llll1ll1l_Krypto_.copy())
    def digest(self):
        l1l1111_Krypto_ (u"ࠧࠨࠢࡓࡧࡷࡹࡷࡴࠠࡵࡪࡨࠤ࡭ࡧࡳࡩࠢࡹࡥࡱࡻࡥࠡࡱࡩࠤࡹ࡮ࡩࡴࠢࡲࡦ࡯࡫ࡣࡵࠢࡤࡷࠥࡧࠠࡣ࡫ࡱࡥࡷࡿࠠࡴࡶࡵ࡭ࡳ࡭ࠢࠣࠤ੆")
        l111l111ll_Krypto_ = l1lll1ll11_Krypto_.new(self._1llll1ll1l_Krypto_.digest()).digest()
        assert len(l111l111ll_Krypto_) == 32
        return l111l111ll_Krypto_
    def hexdigest(self):
        l1l1111_Krypto_ (u"ࠨࠢࠣࡔࡨࡸࡺࡸ࡮ࠡࡶ࡫ࡩࠥ࡮ࡡࡴࡪࠣࡺࡦࡲࡵࡦࠢࡲࡪࠥࡺࡨࡪࡵࠣࡳࡧࡰࡥࡤࡶࠣࡥࡸࠦࡡࠡࠪ࡯ࡳࡼ࡫ࡲࡤࡣࡶࡩ࠮ࠦࡨࡦࡺࡤࡨࡪࡩࡩ࡮ࡣ࡯ࠤࡸࡺࡲࡪࡰࡪࠦࠧࠨੇ")
        l111l111ll_Krypto_ = l1llll1l1l1_Krypto_(self.digest())
        assert len(l111l111ll_Krypto_) == 64
        if l1l11l11_Krypto_.version_info[0] == 2:
            return l111l111ll_Krypto_
        else:
            return l111l111ll_Krypto_.decode()
    def update(self, data):
        self._1llll1ll1l_Krypto_.update(data)
digest_size = _1lll1l1ll1_Krypto_.digest_size
def new(data=None):
    l1l1111_Krypto_ (u"ࠢࠣࠤࡕࡩࡹࡻࡲ࡯ࠢࡤࠤࡳ࡫ࡷࠡࡕࡋࡅࡩ࠸࠵࠷ࠢ࡫ࡥࡸ࡮ࡩ࡯ࡩࠣࡳࡧࡰࡥࡤࡶࠥࠦࠧੈ")
    if not data:
        data=b(l1l1111_Krypto_ (u"ࠣࠤ੉"))
    l1llll111l_Krypto_ = _1lll1l1ll1_Krypto_(_1lll1l1ll1_Krypto_._1lll1l1lll_Krypto_, l1lll1ll11_Krypto_.new(data))
    l1llll111l_Krypto_.new = globals()[l1l1111_Krypto_ (u"ࠩࡱࡩࡼ࠭੊")]
    return l1llll111l_Krypto_