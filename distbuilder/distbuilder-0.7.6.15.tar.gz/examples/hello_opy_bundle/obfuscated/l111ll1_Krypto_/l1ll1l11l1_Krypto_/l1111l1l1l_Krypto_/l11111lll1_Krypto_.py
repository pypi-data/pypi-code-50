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
__revision__ = l1l1111_Krypto_ (u"ࠨࠤࡊࡦࠧࠦਲ")
import sys as l1l11l11_Krypto_
if l1l11l11_Krypto_.version_info[0] == 2 and l1l11l11_Krypto_.version_info[1] == 1:
    from l111ll1_Krypto_.l1l111ll_Krypto_.l1l1ll1l_Krypto_ import *
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
from binascii import b2a_hex as l1llll1l1l1_Krypto_
import time as l11111l111_Krypto_
import warnings as l11ll1ll11_Krypto_
from l111ll1_Krypto_.l11lll1_Krypto_ import l11llll_Krypto_
from . import l1llllll1l1_Krypto_
from . import l1llllll1ll_Krypto_
class l1lllll1l11_Krypto_(object):
    l1l1111_Krypto_ (u"ࠢࠣࠤࡉࡳࡷࡺࡵ࡯ࡣࠣࡴࡴࡵ࡬ࠡࡶࡼࡴࡪࠐࠊࠡࠢࠣࠤ࡙࡮ࡩࡴࠢࡲࡦ࡯࡫ࡣࡵࠢࡤࡧࡹࡹࠠ࡭࡫࡮ࡩࠥࡧࠠࡩࡣࡶ࡬ࠥࡵࡢ࡫ࡧࡦࡸ࠱ࠦࡷࡪࡶ࡫ࠤࡹ࡮ࡥࠡࡨࡲࡰࡱࡵࡷࡪࡰࡪࠤࡩ࡯ࡦࡧࡧࡵࡩࡳࡩࡥࡴ࠼ࠍࠎࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡊࡶࠣ࡯ࡪ࡫ࡰࡴࠢࡤࠤࡨࡵࡵ࡯ࡶࠣࠬࡹ࡮ࡥࠡ࠰࡯ࡩࡳ࡭ࡴࡩࠢࡤࡸࡹࡸࡩࡣࡷࡷࡩ࠮ࠦ࡯ࡧࠢࡷ࡬ࡪࠦ࡮ࡶ࡯ࡥࡩࡷࠦ࡯ࡧࠢࡥࡽࡹ࡫ࡳࠡࡶ࡫ࡥࡹࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࡫ࡥࡻ࡫ࠠࡣࡧࡨࡲࠥࡧࡤࡥࡧࡧࠤࡹࡵࠠࡵࡪࡨࠤࡵࡵ࡯࡭ࠌࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡏࡴࠡࡵࡸࡴࡵࡵࡲࡵࡵࠣࡥࠥ࠴ࡲࡦࡵࡨࡸ࠭࠯ࠠ࡮ࡧࡷ࡬ࡴࡪࠠࡧࡱࡵࠤ࡮ࡴ࠭ࡱ࡮ࡤࡧࡪࠦࡲࡦ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡥࡹ࡯࡯࡯ࠌࠣࠤࠥࠦࠠࠡࠢࠣ࠱࡚ࠥࡨࡦࠢࡰࡩࡹ࡮࡯ࡥࠢࡷࡳࠥࡧࡤࡥࠢࡥࡽࡹ࡫ࡳࠡࡶࡲࠤࡹ࡮ࡥࠡࡲࡲࡳࡱࠦࡩࡴࠢ࠱ࡥࡵࡶࡥ࡯ࡦࠫ࠭࠱ࠦ࡮ࡰࡶࠣ࠲ࡺࡶࡤࡢࡶࡨࠬ࠮࠴ࠊࠡࠢࠣࠤࠧࠨࠢਲ਼")
    digest_size = l1llllll1l1_Krypto_.digest_size
    def __init__(self):
        self.reset()
    def append(self, data):
        self._1llll1ll1l_Krypto_.update(data)
        self.length += len(data)
    def digest(self):
        return self._1llll1ll1l_Krypto_.digest()
    def hexdigest(self):
        if l1l11l11_Krypto_.version_info[0] == 2:
            return l1llll1l1l1_Krypto_(self.digest())
        else:
            return l1llll1l1l1_Krypto_(self.digest()).decode()
    def reset(self):
        self._1llll1ll1l_Krypto_ = l1llllll1l1_Krypto_.new()
        self.length = 0
def l1llll1l1ll_Krypto_(r):
    l1l1111_Krypto_ (u"ࠣࠤࠥࡖࡪࡺࡵࡳࡰࠣࡥࠥࡲࡩࡴࡶࠣࡳ࡫ࠦࡰࡰࡱ࡯ࡷࠥ࡯࡮ࡥࡧࡻࡩࡸࠦࠨࡪࡰࠣࡶࡦࡴࡧࡦࠪ࠶࠶࠮࠯ࠠࡵࡪࡤࡸࠥࡧࡲࡦࠢࡷࡳࠥࡨࡥࠡ࡫ࡱࡧࡱࡻࡤࡦࡦࠣࡨࡺࡸࡩ࡯ࡩࠣࡶࡪࡹࡥࡦࡦࠣࡲࡺࡳࡢࡦࡴࠣࡶ࠳ࠐࠊࠡࠢࠣࠤࡆࡩࡣࡰࡴࡧ࡭ࡳ࡭ࠠࡵࡱࠣࡣࡕࡸࡡࡤࡶ࡬ࡧࡦࡲࠠࡄࡴࡼࡴࡹࡵࡧࡳࡣࡳ࡬ࡾࡥࠬࠡࡥ࡫ࡥࡵࡺࡥࡳࠢ࠴࠴࠳࠻࠮࠳ࠢࠥࡔࡴࡵ࡬ࡴࠤ࠽ࠎࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࡑࡱࡲࡰࠥࡖ࡟ࡪࠢ࡬ࡷࠥ࡯࡮ࡤ࡮ࡸࡨࡪࡪࠠࡪࡨࠣ࠶࠯࠰ࡩࠡ࡫ࡶࠤࡦࠦࡤࡪࡸ࡬ࡷࡴࡸࠠࡰࡨࠣࡶ࠳ࠦࠠࡕࡪࡸࡷࠥࡖ࡟࠱ࠢ࡬ࡷࠥࡻࡳࡦࡦࠍࠤࠥࠦࠠࠡࠢࠣࠤࡪࡼࡥࡳࡻࠣࡶࡪࡹࡥࡦࡦ࠯ࠤࡕࡥ࠱ࠡࡧࡹࡩࡷࡿࠠࡰࡶ࡫ࡩࡷࠦࡲࡦࡵࡨࡩࡩ࠲ࠠࡑࡡ࠵ࠤࡪࡼࡥࡳࡻࠣࡪࡴࡻࡲࡵࡪࠣࡶࡪࡹࡥࡦࡦ࠯ࠤࡪࡺࡣ࠯ࠤࠍࠤࠥࠦࠠࠣࠤࠥ਴")
    assert r >= 1
    l111l111ll_Krypto_ = []
    mask = 0
    for i in range(32):
        if (r & mask) == 0:
            l111l111ll_Krypto_.append(i)
        else:
            break
        mask = (mask << 1) | 1
    return l111l111ll_Krypto_
class l11111lll1_Krypto_(object):
    l1llll1lll1_Krypto_ = 64
    l1lllll11l1_Krypto_ = 0.100
    def __init__(self):
        self.l1lllll1l1l_Krypto_ = 0
        self.generator = l1llllll1ll_Krypto_.l1llll1ll11_Krypto_()
        self.l1lllll11ll_Krypto_ = None
        self.l1llllll11l_Krypto_ = [l1lllll1l11_Krypto_() for i in range(32)]
        assert(self.l1llllll11l_Krypto_[0] is not self.l1llllll11l_Krypto_[1])
    def _11111l1l1_Krypto_(self):
        self.l1lllll11ll_Krypto_ = None
    def l111111ll1_Krypto_(self, bytes):
        l1llllll111_Krypto_ = l11111l111_Krypto_.l11111l111_Krypto_()
        if (self.l1lllll11ll_Krypto_ is not None and self.l1lllll11ll_Krypto_ > l1llllll111_Krypto_):
            l11ll1ll11_Krypto_.warn(l1l1111_Krypto_ (u"ࠤࡆࡰࡴࡩ࡫ࠡࡴࡨࡻ࡮ࡴࡤࠡࡦࡨࡸࡪࡩࡴࡦࡦ࠱ࠤࡗ࡫ࡳࡦࡶࡷ࡭ࡳ࡭ࠠ࡭ࡣࡶࡸࡤࡸࡥࡴࡧࡨࡨ࠳ࠨਵ"), l11llll_Krypto_)
            self.l1lllll11ll_Krypto_ = None
        if (self.l1llllll11l_Krypto_[0].length >= self.l1llll1lll1_Krypto_ and
            (self.l1lllll11ll_Krypto_ is None or
             l1llllll111_Krypto_ > self.l1lllll11ll_Krypto_ + self.l1lllll11l1_Krypto_)):
            self._1lllll1111_Krypto_(l1llllll111_Krypto_)
        return self.generator.l1llll1llll_Krypto_(bytes)
    def _1lllll1111_Krypto_(self, l1llllll111_Krypto_=None):
        if l1llllll111_Krypto_ is None:
            l1llllll111_Krypto_ = l11111l111_Krypto_.l11111l111_Krypto_()
        l1ll1111l_Krypto_ = []
        self.l1lllll1l1l_Krypto_ += 1
        self.l1lllll11ll_Krypto_ = l1llllll111_Krypto_
        for i in l1llll1l1ll_Krypto_(self.l1lllll1l1l_Krypto_):
            l1ll1111l_Krypto_.append(self.l1llllll11l_Krypto_[i].digest())
            self.l1llllll11l_Krypto_[i].reset()
        l1ll1111l_Krypto_ = b(l1l1111_Krypto_ (u"ࠥࠦਸ਼")).join(l1ll1111l_Krypto_)
        self.generator.l1lllll111l_Krypto_(l1ll1111l_Krypto_)
    def l1111l1lll_Krypto_(self, l1lllll1ll1_Krypto_, l1lllll1lll_Krypto_, data):
        assert 1 <= len(data) <= 32
        assert 0 <= l1lllll1ll1_Krypto_ <= 255
        assert 0 <= l1lllll1lll_Krypto_ <= 31
        self.l1llllll11l_Krypto_[l1lllll1lll_Krypto_].append(l11111l11_Krypto_(l1lllll1ll1_Krypto_))
        self.l1llllll11l_Krypto_[l1lllll1lll_Krypto_].append(l11111l11_Krypto_(len(data)))
        self.l1llllll11l_Krypto_[l1lllll1lll_Krypto_].append(data)