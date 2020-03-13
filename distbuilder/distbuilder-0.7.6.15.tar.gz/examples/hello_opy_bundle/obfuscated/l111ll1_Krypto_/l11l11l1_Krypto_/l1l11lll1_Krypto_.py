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
l1l1111_Krypto_ (u"ࠣࠤࠥࡖࡘࡇࠠࡱࡷࡥࡰ࡮ࡩ࠭࡬ࡧࡼࠤࡨࡸࡹࡱࡶࡲ࡫ࡷࡧࡰࡩࡻࠣࡥࡱ࡭࡯ࡳ࡫ࡷ࡬ࡲࠦࠨࡴ࡫ࡪࡲࡦࡺࡵࡳࡧࠣࡥࡳࡪࠠࡦࡰࡦࡶࡾࡶࡴࡪࡱࡱ࠭࠳ࠐࠊࡓࡕࡄࡣࠥ࡯ࡳࠡࡶ࡫ࡩࠥࡳ࡯ࡴࡶࠣࡻ࡮ࡪࡥࡴࡲࡵࡩࡦࡪࠠࡢࡰࡧࠤࡺࡹࡥࡥࠢࡳࡹࡧࡲࡩࡤࠢ࡮ࡩࡾࠦࡡ࡭ࡩࡲࡶ࡮ࡺࡨ࡮࠰ࠣࡍࡹࡹࠠࡴࡧࡦࡹࡷ࡯ࡴࡺࠢ࡬ࡷࠏࡨࡡࡴࡧࡧࠤࡴࡴࠠࡵࡪࡨࠤࡩ࡯ࡦࡧ࡫ࡦࡹࡱࡺࡹࠡࡱࡩࠤ࡫ࡧࡣࡵࡱࡵ࡭ࡳ࡭ࠠ࡭ࡣࡵ࡫ࡪࠦࡩ࡯ࡶࡨ࡫ࡪࡸࡳ࠯ࠢࡗ࡬ࡪࠦࡡ࡭ࡩࡲࡶ࡮ࡺࡨ࡮ࠢ࡫ࡥࡸࠐࡷࡪࡶ࡫ࡷࡹࡵ࡯ࡥࠢࡤࡸࡹࡧࡣ࡬ࡵࠣࡪࡴࡸࠠ࠴࠲ࠣࡽࡪࡧࡲࡴ࠮ࠣࡥࡳࡪࠠࡪࡶࠣ࡭ࡸࠦࡴࡩࡧࡵࡩ࡫ࡵࡲࡦࠢࡦࡳࡳࡹࡩࡥࡧࡵࡩࡩࠦࡲࡦࡣࡶࡳࡳࡧࡢ࡭ࡻࠍࡷࡪࡩࡵࡳࡧࠣࡪࡴࡸࠠ࡯ࡧࡺࠤࡩ࡫ࡳࡪࡩࡱࡷ࠳ࠐࠊࡕࡪࡨࠤࡦࡲࡧࡰࡴ࡬ࡸ࡭ࡳࠠࡤࡣࡱࠤࡧ࡫ࠠࡶࡵࡨࡨࠥ࡬࡯ࡳࠢࡥࡳࡹ࡮ࠠࡤࡱࡱࡪ࡮ࡪࡥ࡯ࡶ࡬ࡥࡱ࡯ࡴࡺࠢࠫࡩࡳࡩࡲࡺࡲࡷ࡭ࡴࡴࠩࠡࡣࡱࡨࠏࡧࡵࡵࡪࡨࡲࡹ࡯ࡣࡢࡶ࡬ࡳࡳࠦࠨࡥ࡫ࡪ࡭ࡹࡧ࡬ࠡࡵ࡬࡫ࡳࡧࡴࡶࡴࡨ࠭࠳ࠦࡉࡵࠢ࡬ࡷࠥࡽ࡯ࡳࡶ࡫ࠤࡳࡵࡴࡪࡰࡪࠤࡹ࡮ࡡࡵࠢࡶ࡭࡬ࡴࡩ࡯ࡩࠣࡥࡳࡪࠊࡥࡧࡦࡶࡾࡶࡴࡪࡱࡱࠤࡦࡸࡥࠡࡵ࡬࡫ࡳ࡯ࡦࡪࡥࡤࡲࡹࡲࡹࠡࡵ࡯ࡳࡼ࡫ࡲࠡࡶ࡫ࡥࡳࠦࡶࡦࡴ࡬ࡪ࡮ࡩࡡࡵ࡫ࡲࡲࠥࡧ࡮ࡥࠢࡨࡲࡨࡸࡹࡱࡶ࡬ࡳࡳ࠴ࠊࡕࡪࡨࠤࡨࡸࡹࡱࡶࡲ࡫ࡷࡧࡨࡪࡥࠣࡷࡹࡸࡥ࡯ࡩࡷ࡬ࠥ࡯ࡳࠡࡲࡵ࡭ࡲࡧࡲࡪ࡮ࡼࠤࡱ࡯࡮࡬ࡧࡧࠤࡹࡵࠠࡵࡪࡨࠤࡱ࡫࡮ࡨࡶ࡫ࠤࡴ࡬ࠠࡵࡪࡨࠤࡲࡵࡤࡶ࡮ࡸࡷࠥ࠰࡮ࠫ࠰ࠍࡍࡳࠦ࠲࠱࠳࠵࠰ࠥࡧࠠࡴࡷࡩࡪ࡮ࡩࡩࡦࡰࡷࠤࡱ࡫࡮ࡨࡶ࡫ࠤ࡮ࡹࠠࡥࡧࡨࡱࡪࡪࠠࡵࡱࠣࡦࡪࠦ࠲࠱࠶࠻ࠤࡧ࡯ࡴࡴ࠰ࠣࡊࡴࡸࠠ࡮ࡱࡵࡩࠥ࡯࡮ࡧࡱࡵࡱࡦࡺࡩࡰࡰ࠯ࠎࡸ࡫ࡥࠡࡶ࡫ࡩࠥࡳ࡯ࡴࡶࠣࡶࡪࡩࡥ࡯ࡶࠣࡉࡈࡘ࡙ࡑࡖࡢࠤࡷ࡫ࡰࡰࡴࡷ࠲ࠏࠐࡂࡰࡶ࡫ࠤࡗ࡙ࡁࠡࡥ࡬ࡴ࡭࡫ࡲࡵࡧࡻࡸࠥࡧ࡮ࡥࠢࡕࡗࡆࠦࡳࡪࡩࡱࡥࡹࡻࡲࡦࠢࡤࡶࡪࠦࡡࡴࠢࡥ࡭࡬ࠦࡡࡴࠢࡷ࡬ࡪࠦ࡭ࡰࡦࡸࡰࡺࡹࠠࠫࡰ࠭ࠤ࠭࠸࠵࠷ࠌࡥࡽࡹ࡫ࡳࠡ࡫ࡩࠤ࠯ࡴࠪࠡ࡫ࡶࠤ࠷࠶࠴࠹ࠢࡥ࡭ࡹࠦ࡬ࡰࡰࡪ࠭࠳ࠐࠊࡕࡪ࡬ࡷࠥࡳ࡯ࡥࡷ࡯ࡩࠥࡶࡲࡰࡸ࡬ࡨࡪࡹࠠࡧࡣࡦ࡭ࡱ࡯ࡴࡪࡧࡶࠤ࡫ࡵࡲࠡࡩࡨࡲࡪࡸࡡࡵ࡫ࡱ࡫ࠥ࡬ࡲࡦࡵ࡫࠰ࠥࡴࡥࡸࠢࡕࡗࡆࠦ࡫ࡦࡻࡶ࠰ࠥࡩ࡯࡯ࡵࡷࡶࡺࡩࡴࡪࡰࡪࠎࡹ࡮ࡥ࡮ࠢࡩࡶࡴࡳࠠ࡬ࡰࡲࡻࡳࠦࡣࡰ࡯ࡳࡳࡳ࡫࡮ࡵࡵ࠯ࠤࡪࡾࡰࡰࡴࡷ࡭ࡳ࡭ࠠࡵࡪࡨࡱ࠱ࠦࡡ࡯ࡦࠣ࡭ࡲࡶ࡯ࡳࡶ࡬ࡲ࡬ࠦࡴࡩࡧࡰ࠲ࠏࠐࠠࠡࠢࠣࡂࡃࡄࠠࡧࡴࡲࡱࠥࡉࡲࡺࡲࡷࡳ࠳ࡖࡵࡣ࡮࡬ࡧࡐ࡫ࡹࠡ࡫ࡰࡴࡴࡸࡴࠡࡔࡖࡅࠏࠦࠠࠡࠢࡁࡂࡃࠐࠠࠡࠢࠣࡂࡃࡄࠠ࡬ࡧࡼࠤࡂࠦࡒࡔࡃ࠱࡫ࡪࡴࡥࡳࡣࡷࡩ࠭࠸࠰࠵࠺ࠬࠎࠥࠦࠠࠡࡀࡁࡂࠥ࡬ࠠ࠾ࠢࡲࡴࡪࡴࠨࠨ࡯ࡼ࡯ࡪࡿ࠮ࡱࡧࡰࠫ࠱࠭ࡷࠨࠫࠍࠤࠥࠦࠠ࠿ࡀࡁࠤ࡫࠴ࡷࡳ࡫ࡷࡩ࠭ࡘࡓࡂ࠰ࡨࡼࡵࡵࡲࡵࡍࡨࡽ࠭࠭ࡐࡆࡏࠪ࠭࠮ࠐࠠࠡࠢࠣࡂࡃࡄࠠࡧ࠰ࡦࡰࡴࡹࡥࠩࠫࠍࠤࠥࠦࠠ࠯࠰࠱ࠎࠥࠦࠠࠡࡀࡁࡂࠥ࡬ࠠ࠾ࠢࡲࡴࡪࡴࠨࠨ࡯ࡼ࡯ࡪࡿ࠮ࡱࡧࡰࠫ࠱࠭ࡲࠨࠫࠍࠤࠥࠦࠠ࠿ࡀࡁࠤࡰ࡫ࡹࠡ࠿ࠣࡖࡘࡇ࠮ࡪ࡯ࡳࡳࡷࡺࡋࡦࡻࠫࡪ࠳ࡸࡥࡢࡦࠫ࠭࠮ࠐࠊࡆࡸࡨࡲࠥࡺࡨࡰࡷࡪ࡬ࠥࡿ࡯ࡶࠢࡰࡥࡾࠦࡣࡩࡱࡲࡷࡪࠦࡴࡰࠢࠣࡨ࡮ࡸࡥࡤࡶ࡯ࡽࠥࡻࡳࡦࠢࡷ࡬ࡪࠦ࡭ࡦࡶ࡫ࡳࡩࡹࠠࡰࡨࠣࡥࡳࠦࡒࡔࡃࠣ࡯ࡪࡿࠠࡰࡤ࡭ࡩࡨࡺࠊࡵࡱࠣࡴࡪࡸࡦࡰࡴࡰࠤࡹ࡮ࡥࠡࡲࡵ࡭ࡲ࡯ࡴࡪࡸࡨࠤࡨࡸࡹࡱࡶࡲ࡫ࡷࡧࡰࡩ࡫ࡦࠤࡴࡶࡥࡳࡣࡷ࡭ࡴࡴࡳࠡࠪࡨ࠲࡬࠴ࠠࡡࡡࡕࡗࡆࡵࡢ࡫࠰ࡨࡲࡨࡸࡹࡱࡶࡣ࠭࠱ࠐࡩࡵࠢ࡬ࡷࠥࡸࡥࡤࡱࡰࡱࡪࡴࡤࡦࡦࠣࡸࡴࠦࡵࡴࡧࠣࡳࡳ࡫ࠠࡰࡨࠣࡸ࡭࡫ࠠࡴࡶࡤࡲࡩࡧࡲࡥ࡫ࡽࡩࡩࠦࡳࡤࡪࡨࡱࡪࡹࠠࡪࡰࡶࡸࡪࡧࡤࠡࠪ࡯࡭ࡰ࡫ࠊࡡࡅࡵࡽࡵࡺ࡯࠯ࡅ࡬ࡴ࡭࡫ࡲ࠯ࡒࡎࡇࡘ࠷࡟ࡷ࠳ࡢ࠹ࡥࠦ࡯ࡳࠢࡣࡇࡷࡿࡰࡵࡱ࠱ࡗ࡮࡭࡮ࡢࡶࡸࡶࡪ࠴ࡐࡌࡅࡖ࠵ࡤࡼ࠱ࡠ࠷ࡣ࠭࠳ࠐࠊ࠯࠰ࠣࡣࡗ࡙ࡁ࠻ࠢ࡫ࡸࡹࡶ࠺࠰࠱ࡨࡲ࠳ࡽࡩ࡬࡫ࡳࡩࡩ࡯ࡡ࠯ࡱࡵ࡫࠴ࡽࡩ࡬࡫࠲ࡖࡘࡇ࡟ࠦ࠴࠻ࡥࡱ࡭࡯ࡳ࡫ࡷ࡬ࡲࠫ࠲࠺ࠌ࠱࠲ࠥࡥࡅࡄࡔ࡜ࡔ࡙ࡀࠠࡩࡶࡷࡴ࠿࠵࠯ࡸࡹࡺ࠲ࡪࡩࡲࡺࡲࡷ࠲ࡪࡻ࠮ࡰࡴࡪ࠳ࡩࡵࡣࡶ࡯ࡨࡲࡹࡹ࠯ࡅ࠰ࡖࡔࡆ࠴࠱࠸࠰ࡳࡨ࡫ࠐࠊ࠻ࡵࡲࡶࡹࡀࠠࡨࡧࡱࡩࡷࡧࡴࡦ࠮ࡦࡳࡳࡹࡴࡳࡷࡦࡸ࠱࡯࡭ࡱࡱࡵࡸࡐ࡫ࡹ࠭ࡧࡵࡶࡴࡸࠊࠣࠤࠥও")
__revision__ = l1l1111_Krypto_ (u"ࠤࠧࡍࡩࠪࠢঔ")
__all__ = [l1l1111_Krypto_ (u"ࠪ࡫ࡪࡴࡥࡳࡣࡷࡩࠬক"), l1l1111_Krypto_ (u"ࠫࡨࡵ࡮ࡴࡶࡵࡹࡨࡺࠧখ"), l1l1111_Krypto_ (u"ࠬ࡫ࡲࡳࡱࡵࠫগ"), l1l1111_Krypto_ (u"࠭ࡩ࡮ࡲࡲࡶࡹࡑࡥࡺࠩঘ"), l1l1111_Krypto_ (u"ࠧࡓࡕࡄࡍࡲࡶ࡬ࡦ࡯ࡨࡲࡹࡧࡴࡪࡱࡱࠫঙ"), l1l1111_Krypto_ (u"ࠨࡡࡕࡗࡆࡵࡢ࡫ࠩচ")]
import sys as l1l11l11_Krypto_
if l1l11l11_Krypto_.version_info[0] == 2 and l1l11l11_Krypto_.version_info[1] == 1:
    from l111ll1_Krypto_.l1l111ll_Krypto_.l1l1ll1l_Krypto_ import *
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
from l111ll1_Krypto_.l1l111ll_Krypto_.l111l1ll_Krypto_ import l11lllll1l_Krypto_, l1ll111ll1_Krypto_, l1ll1lllll_Krypto_
from l111ll1_Krypto_.l11l11l1_Krypto_ import _11l1l1111_Krypto_, _1l11llll1_Krypto_, l1l111lll1_Krypto_
from l111ll1_Krypto_ import l1ll1l11l1_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l11l1lll1l_Krypto_ import l11l1ll1ll_Krypto_, l11l11llll_Krypto_, l11l1ll1l1_Krypto_
import binascii as l11l111lll_Krypto_
import struct as l1l1l1ll11_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l111l1ll_Krypto_ import l11llll1ll_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l111l1ll_Krypto_ import l11llll1ll_Krypto_
try:
    from l111ll1_Krypto_.l11l11l1_Krypto_ import _1l11ll111_Krypto_
except ImportError:
    _1l11ll111_Krypto_ = None
class _11ll111ll_Krypto_(l1l111lll1_Krypto_.l1l111lll1_Krypto_):
    l1l1111_Krypto_ (u"ࠤࠥࠦࡈࡲࡡࡴࡵࠣࡨࡪ࡬ࡩ࡯࡫ࡱ࡫ࠥࡧ࡮ࠡࡣࡦࡸࡺࡧ࡬ࠡࡔࡖࡅࠥࡱࡥࡺ࠰ࠍࠎࠥࠦࠠࠡ࠼ࡸࡲࡩࡵࡣࡶ࡯ࡨࡲࡹ࡫ࡤ࠻ࠢࡢࡣ࡬࡫ࡴࡴࡶࡤࡸࡪࡥ࡟࠭ࠢࡢࡣࡸ࡫ࡴࡴࡶࡤࡸࡪࡥ࡟࠭ࠢࡢࡣࡷ࡫ࡰࡳࡡࡢ࠰ࠥࡥ࡟ࡨࡧࡷࡥࡹࡺࡲࡠࡡࠍࠤࠥࠦࠠࠣࠤࠥছ")
    l1l1l11111_Krypto_ = [l1l1111_Krypto_ (u"ࠪࡲࠬজ"), l1l1111_Krypto_ (u"ࠫࡪ࠭ঝ"), l1l1111_Krypto_ (u"ࠬࡪࠧঞ"), l1l1111_Krypto_ (u"࠭ࡰࠨট"), l1l1111_Krypto_ (u"ࠧࡲࠩঠ"), l1l1111_Krypto_ (u"ࠨࡷࠪড")]
    def __init__(self, implementation, key, l1l11ll1ll_Krypto_=None):
        self.implementation = implementation
        self.key = key
        if l1l11ll1ll_Krypto_ is None:
            l1l11ll1ll_Krypto_ = l1ll1l11l1_Krypto_.new().read
        self._11l1lll11_Krypto_ = l1l11ll1ll_Krypto_
    def __getattr__(self, l1l111llll_Krypto_):
        if l1l111llll_Krypto_ in self.l1l1l11111_Krypto_:
            return getattr(self.key, l1l111llll_Krypto_)
        else:
            raise AttributeError(l1l1111_Krypto_ (u"ࠤࠨࡷࠥࡵࡢ࡫ࡧࡦࡸࠥ࡮ࡡࡴࠢࡱࡳࠥࠫࡲࠡࡣࡷࡸࡷ࡯ࡢࡶࡶࡨࠦঢ") % (self.__class__.__name__, l1l111llll_Krypto_,))
    def l1_Krypto_(self, l1ll11l1_Krypto_, l1l111ll1l_Krypto_):
        l1l1111_Krypto_ (u"ࠥࠦࠧࡋ࡮ࡤࡴࡼࡴࡹࠦࡡࠡࡲ࡬ࡩࡨ࡫ࠠࡰࡨࠣࡨࡦࡺࡡࠡࡹ࡬ࡸ࡭ࠦࡒࡔࡃ࠱ࠎࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠺ࡑࡣࡵࡥࡲ࡫ࡴࡦࡴࠣࡴࡱࡧࡩ࡯ࡶࡨࡼࡹࡀࠠࡕࡪࡨࠤࡵ࡯ࡥࡤࡧࠣࡳ࡫ࠦࡤࡢࡶࡤࠤࡹࡵࠠࡦࡰࡦࡶࡾࡶࡴࠡࡹ࡬ࡸ࡭ࠦࡒࡔࡃ࠱ࠤࡎࡺࠠ࡮ࡣࡼࠤࡳࡵࡴࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࡦࡪࠦ࡮ࡶ࡯ࡨࡶ࡮ࡩࡡ࡭࡮ࡼࠤࡱࡧࡲࡨࡧࡵࠤࡹ࡮ࡡ࡯ࠢࡷ࡬ࡪࠦࡒࡔࡃࠣࡱࡴࡪࡵ࡭ࡧࠣࠬ࠯࠰࡮ࠫࠬࠬ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠺ࡕࡻࡳࡩࠥࡶ࡬ࡢ࡫ࡱࡸࡪࡾࡴ࠻ࠢࡥࡽࡹ࡫ࠠࡴࡶࡵ࡭ࡳ࡭ࠠࡰࡴࠣࡰࡴࡴࡧࠋࠌࠣࠤࠥࠦࠠࠡࠢࠣ࠾ࡕࡧࡲࡢ࡯ࡨࡸࡪࡸࠠࡌ࠼ࠣࡅࠥࡸࡡ࡯ࡦࡲࡱࠥࡶࡡࡳࡣࡰࡩࡹ࡫ࡲࠡࠪ࠭ࡪࡴࡸࠠࡤࡱࡰࡴࡦࡺࡩࡣ࡫࡯࡭ࡹࡿࠠࡰࡰ࡯ࡽ࠳ࠦࡔࡩ࡫ࡶࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࡶࡢ࡮ࡸࡩࠥࡽࡩ࡭࡮ࠣࡦࡪࠦࡩࡨࡰࡲࡶࡪࡪࠪࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣ࠾࡙ࡿࡰࡦࠢࡎ࠾ࠥࡨࡹࡵࡧࠣࡷࡹࡸࡩ࡯ࡩࠣࡳࡷࠦ࡬ࡰࡰࡪࠎࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠺ࡢࡶࡷࡩࡳࡺࡩࡰࡰ࠽ࠤࡹ࡮ࡩࡴࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࡵ࡫ࡲࡧࡱࡵࡱࡸࠦࡴࡩࡧࠣࡴࡱࡧࡩ࡯࠮ࠣࡴࡷ࡯࡭ࡪࡶ࡬ࡺࡪࠦࡒࡔࡃࠣࡩࡳࡩࡲࡺࡲࡷ࡭ࡴࡴࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠫ࠮ࡹ࡫ࡸࡵࡤࡲࡳࡰ࠰ࠩ࠯ࠢࡌࡲࠥࡸࡥࡢ࡮ࠣࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮ࡴ࠮ࠣࡽࡴࡻࠠࡢ࡮ࡺࡥࡾࡹࠠ࡯ࡧࡨࡨࠥࡺ࡯ࠡࡷࡶࡩࠥࡶࡲࡰࡲࡨࡶࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࡤࡴࡼࡴࡹࡵࡧࡳࡣࡳ࡬࡮ࡩࠠࡱࡣࡧࡨ࡮ࡴࡧ࠭ࠢࡤࡲࡩࠦࡹࡰࡷࠣࡷ࡭ࡵࡵ࡭ࡦࠣࡲࡴࡺࠠࡥ࡫ࡵࡩࡨࡺ࡬ࡺࠢࡨࡲࡨࡸࡹࡱࡶࠣࡨࡦࡺࡡࠡࡹ࡬ࡸ࡭ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࡶ࡫࡭ࡸࠦ࡭ࡦࡶ࡫ࡳࡩ࠴ࠠࡇࡣ࡬ࡰࡺࡸࡥࠡࡶࡲࠤࡩࡵࠠࡴࡱࠣࡱࡦࡿࠠ࡭ࡧࡤࡨࠥࡺ࡯ࠡࡵࡨࡧࡺࡸࡩࡵࡻࠣࡺࡺࡲ࡮ࡦࡴࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࡋࡷࠤ࡮ࡹࠠࡳࡧࡦࡳࡲࡳࡥ࡯ࡦࡨࡨࠥࡺ࡯ࠡࡷࡶࡩࠥࡳ࡯ࡥࡷ࡯ࡩࡸࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࡢࡆࡶࡾࡶࡴࡰ࠰ࡆ࡭ࡵ࡮ࡥࡳ࠰ࡓࡏࡈ࡙࠱ࡠࡑࡄࡉࡕࡦࠠࡰࡴࠣࡤࡈࡸࡹࡱࡶࡲ࠲ࡈ࡯ࡰࡩࡧࡵ࠲ࡕࡑࡃࡔ࠳ࡢࡺ࠶ࡥ࠵ࡡࠢ࡬ࡲࡸࡺࡥࡢࡦ࠱ࠎࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠺ࡓࡧࡷࡹࡷࡴ࠺ࠡࡃࠣࡸࡺࡶ࡬ࡦࠢࡺ࡭ࡹ࡮ࠠࡵࡹࡲࠤ࡮ࡺࡥ࡮ࡵ࠱ࠤ࡙࡮ࡥࠡࡨ࡬ࡶࡸࡺࠠࡪࡶࡨࡱࠥ࡯ࡳࠡࡶ࡫ࡩࠥࡩࡩࡱࡪࡨࡶࡹ࡫ࡸࡵࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࡴ࡬ࠠࡵࡪࡨࠤࡸࡧ࡭ࡦࠢࡷࡽࡵ࡫ࠠࡢࡵࠣࡸ࡭࡫ࠠࡱ࡮ࡤ࡭ࡳࡺࡥࡹࡶࠣࠬࡸࡺࡲࡪࡰࡪࠤࡴࡸࠠ࡭ࡱࡱ࡫࠮࠴ࠠࡕࡪࡨࠤࡸ࡫ࡣࡰࡰࡧࠤ࡮ࡺࡥ࡮ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡮ࡹࠠࡢ࡮ࡺࡥࡾࡹࠠࡏࡱࡱࡩ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥণ")
        return l1l111lll1_Krypto_.l1l111lll1_Krypto_.l1_Krypto_(self, l1ll11l1_Krypto_, l1l111ll1l_Krypto_)
    def l1lllll_Krypto_(self, l1ll111l_Krypto_):
        l1l1111_Krypto_ (u"ࠦࠧࠨࡄࡦࡥࡵࡽࡵࡺࠠࡢࠢࡳ࡭ࡪࡩࡥࠡࡱࡩࠤࡩࡧࡴࡢࠢࡺ࡭ࡹ࡮ࠠࡓࡕࡄ࠲ࠏࠐࠠࠡࠢࠣࠤࠥࠦࠠࡅࡧࡦࡶࡾࡶࡴࡪࡱࡱࠤࡦࡲࡷࡢࡻࡶࠤࡹࡧ࡫ࡦࡵࠣࡴࡱࡧࡣࡦࠢࡺ࡭ࡹ࡮ࠠࡣ࡮࡬ࡲࡩ࡯࡮ࡨ࠰ࠍࠎࠥࠦࠠࠡࠢࠣࠤࠥࡀࡡࡵࡶࡨࡲࡹ࡯࡯࡯࠼ࠣࡸ࡭࡯ࡳࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࡴࡪࡸࡦࡰࡴࡰࡷࠥࡺࡨࡦࠢࡳࡰࡦ࡯࡮࠭ࠢࡳࡶ࡮ࡳࡩࡵ࡫ࡹࡩࠥࡘࡓࡂࠢࡧࡩࡨࡸࡹࡱࡶ࡬ࡳࡳࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠪ࠭ࡸࡪࡾࡴࡣࡱࡲ࡯࠯࠯࠮ࠡࡋࡱࠤࡷ࡫ࡡ࡭ࠢࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴࡳ࠭ࠢࡼࡳࡺࠦࡡ࡭ࡹࡤࡽࡸࠦ࡮ࡦࡧࡧࠤࡹࡵࠠࡶࡵࡨࠤࡵࡸ࡯ࡱࡧࡵࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࡣࡳࡻࡳࡸࡴ࡭ࡲࡢࡲ࡫࡭ࡨࠦࡰࡢࡦࡧ࡭ࡳ࡭ࠬࠡࡣࡱࡨࠥࡿ࡯ࡶࠢࡶ࡬ࡴࡻ࡬ࡥࠢࡱࡳࡹࠦࡤࡪࡴࡨࡧࡹࡲࡹࠡࡦࡨࡧࡷࡿࡰࡵࠢࡧࡥࡹࡧࠠࡸ࡫ࡷ࡬ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࡵࡪ࡬ࡷࠥࡳࡥࡵࡪࡲࡨ࠳ࠦࡆࡢ࡫࡯ࡹࡷ࡫ࠠࡵࡱࠣࡨࡴࠦࡳࡰࠢࡰࡥࡾࠦ࡬ࡦࡣࡧࠤࡹࡵࠠࡴࡧࡦࡹࡷ࡯ࡴࡺࠢࡹࡹࡱࡴࡥࡳࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࡊࡶࠣ࡭ࡸࠦࡲࡦࡥࡲࡱࡲ࡫࡮ࡥࡧࡧࠤࡹࡵࠠࡶࡵࡨࠤࡲࡵࡤࡶ࡮ࡨࡷࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࡡࡅࡵࡽࡵࡺ࡯࠯ࡅ࡬ࡴ࡭࡫ࡲ࠯ࡒࡎࡇࡘ࠷࡟ࡐࡃࡈࡔࡥࠦ࡯ࡳࠢࡣࡇࡷࡿࡰࡵࡱ࠱ࡇ࡮ࡶࡨࡦࡴ࠱ࡔࡐࡉࡓ࠲ࡡࡹ࠵ࡤ࠻ࡠࠡ࡫ࡱࡷࡹ࡫ࡡࡥ࠰ࠍࠎࠥࠦࠠࠡࠢࠣࠤࠥࡀࡐࡢࡴࡤࡱࡪࡺࡥࡳࠢࡦ࡭ࡵ࡮ࡥࡳࡶࡨࡼࡹࡀࠠࡕࡪࡨࠤࡵ࡯ࡥࡤࡧࠣࡳ࡫ࠦࡤࡢࡶࡤࠤࡹࡵࠠࡥࡧࡦࡶࡾࡶࡴࠡࡹ࡬ࡸ࡭ࠦࡒࡔࡃ࠱ࠤࡎࡺࠠ࡮ࡣࡼࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦ࡮ࡰࡶࠣࡦࡪࠦ࡮ࡶ࡯ࡨࡶ࡮ࡩࡡ࡭࡮ࡼࠤࡱࡧࡲࡨࡧࡵࠤࡹ࡮ࡡ࡯ࠢࡷ࡬ࡪࠦࡒࡔࡃࠣࡱࡴࡪࡵ࡭ࡧࠣࠬ࠯࠰࡮ࠫࠬࠬ࠲ࠥࡏࡦࠡࡣࠣࡸࡺࡶ࡬ࡦ࠮ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࡺࡨࡦࠢࡩ࡭ࡷࡹࡴࠡ࡫ࡷࡩࡲࠦࡩࡴࠢࡷ࡬ࡪࠦࡡࡤࡶࡸࡥࡱࠦࡣࡪࡲ࡫ࡩࡷࡺࡥࡹࡶ࠾ࠤࡹ࡮ࡥࠡࡵࡨࡧࡴࡴࡤࠡ࡫ࡷࡩࡲࠦࡩࡴࠢ࡬࡫ࡳࡵࡲࡦࡦ࠱ࠎࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠺ࡕࡻࡳࡩࠥࡩࡩࡱࡪࡨࡶࡹ࡫ࡸࡵ࠼ࠣࡦࡾࡺࡥࠡࡵࡷࡶ࡮ࡴࡧ࠭ࠢ࡯ࡳࡳ࡭ࠠࡰࡴࠣࡥࠥ࠸࠭ࡪࡶࡨࡱࠥࡺࡵࡱ࡮ࡨࠤࡦࡹࠠࡳࡧࡷࡹࡷࡴࡥࡥࠢࡥࡽࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࡡࡧࡱࡧࡷࡿࡰࡵࡢࠍࠎࠥࠦࠠࠡࠢࠣࠤࠥࡀࡒࡦࡶࡸࡶࡳࡀࠠࡂࠢࡥࡽࡹ࡫ࠠࡴࡶࡵ࡭ࡳ࡭ࠠࡪࡨࠣࡧ࡮ࡶࡨࡦࡴࡷࡩࡽࡺࠠࡸࡣࡶࠤࡦࠦࡢࡺࡶࡨࠤࡸࡺࡲࡪࡰࡪࠤࡴࡸࠠࡢࠢࡷࡹࡵࡲࡥࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࡳ࡫ࠦࡢࡺࡶࡨࠤࡸࡺࡲࡪࡰࡪࡷ࠳ࠦࡁࠡ࡮ࡲࡲ࡬ࠦ࡯ࡵࡪࡨࡶࡼ࡯ࡳࡦ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢত")
        return l1l111lll1_Krypto_.l1l111lll1_Krypto_.l1lllll_Krypto_(self, l1ll111l_Krypto_)
    def l1l11lll11_Krypto_(self, M, l1l111ll1l_Krypto_):
        l1l1111_Krypto_ (u"ࠧࠨࠢࡔ࡫ࡪࡲࠥࡧࠠࡱ࡫ࡨࡧࡪࠦ࡯ࡧࠢࡧࡥࡹࡧࠠࡸ࡫ࡷ࡬ࠥࡘࡓࡂ࠰ࠍࠎࠥࠦࠠࠡࠢࠣࠤ࡙ࠥࡩࡨࡰ࡬ࡲ࡬ࠦࡡ࡭ࡹࡤࡽࡸࠦࡴࡢ࡭ࡨࡷࠥࡶ࡬ࡢࡥࡨࠤࡼ࡯ࡴࡩࠢࡥࡰ࡮ࡴࡤࡪࡰࡪ࠲ࠏࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠻ࡣࡷࡸࡪࡴࡴࡪࡱࡱ࠾ࠥࡺࡨࡪࡵࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥࡶࡥࡳࡨࡲࡶࡲࡹࠠࡵࡪࡨࠤࡵࡲࡡࡪࡰ࠯ࠤࡵࡸࡩ࡮࡫ࡷ࡭ࡻ࡫ࠠࡓࡕࡄࠤࡩ࡫ࡣࡳࡻࡳࡸ࡮ࡵ࡮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠬ࠯ࡺࡥࡹࡶࡥࡳࡴࡱࠪࠪ࠰ࠣࡍࡳࠦࡲࡦࡣ࡯ࠤࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯ࡵ࠯ࠤࡾࡵࡵࠡࡣ࡯ࡻࡦࡿࡳࠡࡰࡨࡩࡩࠦࡴࡰࠢࡸࡷࡪࠦࡰࡳࡱࡳࡩࡷࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࡥࡵࡽࡵࡺ࡯ࡨࡴࡤࡴ࡭࡯ࡣࠡࡲࡤࡨࡩ࡯࡮ࡨ࠮ࠣࡥࡳࡪࠠࡺࡱࡸࠤࡸ࡮࡯ࡶ࡮ࡧࠤࡳࡵࡴࠡࡦ࡬ࡶࡪࡩࡴ࡭ࡻࠣࡷ࡮࡭࡮ࠡࡦࡤࡸࡦࠦࡷࡪࡶ࡫ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࡴࡩ࡫ࡶࠤࡲ࡫ࡴࡩࡱࡧ࠲ࠥࡌࡡࡪ࡮ࡸࡶࡪࠦࡴࡰࠢࡧࡳࠥࡹ࡯ࠡ࡯ࡤࡽࠥࡲࡥࡢࡦࠣࡸࡴࠦࡳࡦࡥࡸࡶ࡮ࡺࡹࠡࡸࡸࡰࡳ࡫ࡲࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࡉࡵࠢ࡬ࡷࠥࡸࡥࡤࡱࡰࡱࡪࡴࡤࡦࡦࠣࡸࡴࠦࡵࡴࡧࠣࡱࡴࡪࡵ࡭ࡧࡶࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࡠࡄࡴࡼࡴࡹࡵ࠮ࡔ࡫ࡪࡲࡦࡺࡵࡳࡧ࠱ࡔࡐࡉࡓ࠲ࡡࡓࡗࡘࡦࠠࡰࡴࠣࡤࡈࡸࡹࡱࡶࡲ࠲ࡘ࡯ࡧ࡯ࡣࡷࡹࡷ࡫࠮ࡑࡍࡆࡗ࠶ࡥࡶ࠲ࡡ࠸ࡤࠥ࡯࡮ࡴࡶࡨࡥࡩ࠴ࠊࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠽ࡔࡦࡸࡡ࡮ࡧࡷࡩࡷࠦࡍ࠻ࠢࡗ࡬ࡪࠦࡰࡪࡧࡦࡩࠥࡵࡦࠡࡦࡤࡸࡦࠦࡴࡰࠢࡶ࡭࡬ࡴࠠࡸ࡫ࡷ࡬ࠥࡘࡓࡂ࠰ࠣࡍࡹࠦ࡭ࡢࡻࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࡴ࡯ࡵࠢࡥࡩࠥࡴࡵ࡮ࡧࡵ࡭ࡨࡧ࡬࡭ࡻࠣࡰࡦࡸࡧࡦࡴࠣࡸ࡭ࡧ࡮ࠡࡶ࡫ࡩࠥࡘࡓࡂࠢࡰࡳࡩࡻ࡬ࡦࠢࠫ࠮࠯ࡴࠪࠫࠫ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡀࡔࡺࡲࡨࠤࡒࡀࠠࡣࡻࡷࡩࠥࡹࡴࡳ࡫ࡱ࡫ࠥࡵࡲࠡ࡮ࡲࡲ࡬ࠐࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠼ࡓࡥࡷࡧ࡭ࡦࡶࡨࡶࠥࡑ࠺ࠡࡃࠣࡶࡦࡴࡤࡰ࡯ࠣࡴࡦࡸࡡ࡮ࡧࡷࡩࡷࠦࠨࠫࡨࡲࡶࠥࡩ࡯࡮ࡲࡤࡸ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡵ࡮࡭ࡻ࠱ࠤ࡙࡮ࡩࡴࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࡻࡧ࡬ࡶࡧࠣࡻ࡮ࡲ࡬ࠡࡤࡨࠤ࡮࡭࡮ࡰࡴࡨࡨ࠯࠯ࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠼ࡗࡽࡵ࡫ࠠࡌ࠼ࠣࡦࡾࡺࡥࠡࡵࡷࡶ࡮ࡴࡧࠡࡱࡵࠤࡱࡵ࡮ࡨࠌࠍࠤࠥࠦࠠࠡࠢࠣࠤ࠿ࡘࡥࡵࡷࡵࡲ࠿ࠦࡁࠡ࠴࠰࡭ࡹ࡫࡭ࠡࡶࡸࡴࡱ࡫࠮ࠡࡖ࡫ࡩࠥ࡬ࡩࡳࡵࡷࠤ࡮ࡺࡥ࡮ࠢ࡬ࡷࠥࡺࡨࡦࠢࡤࡧࡹࡻࡡ࡭ࠢࡶ࡭࡬ࡴࡡࡵࡷࡵࡩࠥ࠮ࡡࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࡰࡴࡴࡧࠪ࠰ࠣࡘ࡭࡫ࠠࡴࡧࡦࡳࡳࡪࠠࡪࡶࡨࡱࠥ࡯ࡳࠡࡣ࡯ࡻࡦࡿࡳࠡࡐࡲࡲࡪ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦথ")
        return l1l111lll1_Krypto_.l1l111lll1_Krypto_.l1l11lll11_Krypto_(self, M, l1l111ll1l_Krypto_)
    def l1l11l1l11_Krypto_(self, M, signature):
        l1l1111_Krypto_ (u"ࠨࠢࠣࡘࡨࡶ࡮࡬ࡹࠡࡶ࡫ࡩࠥࡼࡡ࡭࡫ࡧ࡭ࡹࡿࠠࡰࡨࠣࡥࡳࠦࡒࡔࡃࠣࡷ࡮࡭࡮ࡢࡶࡸࡶࡪ࠴ࠊࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠽ࡥࡹࡺࡥ࡯ࡶ࡬ࡳࡳࡀࠠࡵࡪ࡬ࡷࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡱࡧࡵࡪࡴࡸ࡭ࡴࠢࡷ࡬ࡪࠦࡰ࡭ࡣ࡬ࡲ࠱ࠦࡰࡳ࡫ࡰ࡭ࡹ࡯ࡶࡦࠢࡕࡗࡆࠦࡥ࡯ࡥࡵࡽࡵࡺࡩࡰࡰࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠮ࠪࡵࡧࡻࡸࡧࡵ࡯࡬ࠬࠬ࠲ࠥࡏ࡮ࠡࡴࡨࡥࡱࠦࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱࡷ࠱ࠦࡹࡰࡷࠣࡥࡱࡽࡡࡺࡵࠣࡲࡪ࡫ࡤࠡࡶࡲࠤࡺࡹࡥࠡࡲࡵࡳࡵ࡫ࡲࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࡧࡷࡿࡰࡵࡱࡪࡶࡦࡶࡨࡪࡥࠣࡴࡦࡪࡤࡪࡰࡪ࠰ࠥࡧ࡮ࡥࠢࡼࡳࡺࠦࡳࡩࡱࡸࡰࡩࠦ࡮ࡰࡶࠣࡨ࡮ࡸࡥࡤࡶ࡯ࡽࠥࡼࡥࡳ࡫ࡩࡽࠥࡪࡡࡵࡣࠣࡻ࡮ࡺࡨࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࡸ࡭࡯ࡳࠡ࡯ࡨࡸ࡭ࡵࡤ࠯ࠢࡉࡥ࡮ࡲࡵࡳࡧࠣࡸࡴࠦࡤࡰࠢࡶࡳࠥࡳࡡࡺࠢ࡯ࡩࡦࡪࠠࡵࡱࠣࡷࡪࡩࡵࡳ࡫ࡷࡽࠥࡼࡵ࡭ࡰࡨࡶࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࡍࡹࠦࡩࡴࠢࡵࡩࡨࡵ࡭࡮ࡧࡱࡨࡪࡪࠠࡵࡱࠣࡹࡸ࡫ࠠ࡮ࡱࡧࡹࡱ࡫ࡳࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࡤࡈࡸࡹࡱࡶࡲ࠲ࡘ࡯ࡧ࡯ࡣࡷࡹࡷ࡫࠮ࡑࡍࡆࡗ࠶ࡥࡐࡔࡕࡣࠤࡴࡸࠠࡡࡅࡵࡽࡵࡺ࡯࠯ࡕ࡬࡫ࡳࡧࡴࡶࡴࡨ࠲ࡕࡑࡃࡔ࠳ࡢࡺ࠶ࡥ࠵ࡡࠢ࡬ࡲࡸࡺࡥࡢࡦ࠱ࠎࠥࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠻ࡒࡤࡶࡦࡳࡥࡵࡧࡵࠤࡒࡀࠠࡕࡪࡨࠤࡪࡾࡰࡦࡥࡷࡩࡩࠦ࡭ࡦࡵࡶࡥ࡬࡫࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠽ࡘࡾࡶࡥࠡࡏ࠽ࠤࡧࡿࡴࡦࠢࡶࡸࡷ࡯࡮ࡨࠢࡲࡶࠥࡲ࡯࡯ࡩࠍࠎࠥࠦࠠࠡࠢࠣࠤࠥࡀࡐࡢࡴࡤࡱࡪࡺࡥࡳࠢࡶ࡭࡬ࡴࡡࡵࡷࡵࡩ࠿ࠦࡔࡩࡧࠣࡖࡘࡇࠠࡴ࡫ࡪࡲࡦࡺࡵࡳࡧࠣࡸࡴࠦࡶࡦࡴ࡬ࡪࡾ࠴ࠠࡕࡪࡨࠤ࡫࡯ࡲࡴࡶࠣ࡭ࡹ࡫࡭ࠡࡱࡩࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࡴࡩࡧࠣࡸࡺࡶ࡬ࡦࠢ࡬ࡷࠥࡺࡨࡦࠢࡤࡧࡹࡻࡡ࡭ࠢࡶ࡭࡬ࡴࡡࡵࡷࡵࡩࠥ࠮ࡡࠡ࡮ࡲࡲ࡬ࠦ࡮ࡰࡶࠣࡰࡦࡸࡧࡦࡴࠣࡸ࡭ࡧ࡮ࠡࡶ࡫ࡩࠥࡳ࡯ࡥࡷ࡯ࡹࡸࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠬ࠭ࡲ࠯࠰ࠩ࠭ࠢࡺ࡬ࡪࡸࡥࡢࡵࠣࡸ࡭࡫ࠠࡴࡧࡦࡳࡳࡪࠠࡪࡶࡨࡱࠥ࡯ࡳࠡࡣ࡯ࡻࡦࡿࡳࠡ࡫ࡪࡲࡴࡸࡥࡥ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࠿࡚ࡹࡱࡧࠣࡷ࡮࡭࡮ࡢࡶࡸࡶࡪࡀࠠࡂࠢ࠵࠱࡮ࡺࡥ࡮ࠢࡷࡹࡵࡲࡥࠡࡣࡶࠤࡷ࡫ࡴࡶࡴࡱࠤࡧࡿࠠࡡࡵ࡬࡫ࡳࡦࠊࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠽ࡖࡪࡺࡵࡳࡰ࠽ࠤ࡙ࡸࡵࡦࠢ࡬ࡪࠥࡺࡨࡦࠢࡶ࡭࡬ࡴࡡࡵࡷࡵࡩࠥ࡯ࡳࠡࡥࡲࡶࡷ࡫ࡣࡵ࠮ࠣࡊࡦࡲࡳࡦࠢࡲࡸ࡭࡫ࡲࡸ࡫ࡶࡩ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥদ")
        return l1l111lll1_Krypto_.l1l111lll1_Krypto_.l1l11l1l11_Krypto_(self, M, signature)
    def _1l11l1lll_Krypto_(self, c, l1l111ll1l_Krypto_):
        return (self.key._1l11l1lll_Krypto_(c),)
    def _1l111l111_Krypto_(self, c):
        (l1ll111l_Krypto_,) = c[:1]
        r = l11lllll1l_Krypto_(1, self.key.n-1, l1l11ll1ll_Krypto_=self._11l1lll11_Krypto_)
        l11l1ll111_Krypto_ = self.key._1l1111111_Krypto_(l1ll111l_Krypto_, r)
        mp = self.key._1l111l111_Krypto_(l11l1ll111_Krypto_)
        return self.key._1l11lll1l_Krypto_(mp, r)
    def _1l1111111_Krypto_(self, m, r):
        return self.key._1l1111111_Krypto_(m, r)
    def _1l11lll1l_Krypto_(self, m, r):
        return self.key._1l11lll1l_Krypto_(m, r)
    def _1l11l1l1l_Krypto_(self, m, l1l111ll1l_Krypto_=None):
        return (self.key._1l11l1l1l_Krypto_(m),)
    def _1l11111l1_Krypto_(self, m, sig):
        (s,) = sig[:1]
        return self.key._1l11111l1_Krypto_(m, s)
    def l1l1111l1l_Krypto_(self):
        return self.key.l1l1111l1l_Krypto_()
    def size(self):
        return self.key.size()
    def l1l1111ll1_Krypto_(self):
        return True
    def l1l1111l11_Krypto_(self):
        return True
    def l1l11ll1l1_Krypto_(self):
        return True
    def l1l11l111l_Krypto_(self):
        return self.implementation.l1l1l1111l_Krypto_((self.key.n, self.key.e))
    def __getstate__(self):
        d = {}
        for k in self.l1l1l11111_Krypto_:
            try:
                d[k] = getattr(self.key, k)
            except AttributeError:
                pass
        return d
    def __setstate__(self, d):
        if not hasattr(self, l1l1111_Krypto_ (u"ࠧࡪ࡯ࡳࡰࡪࡳࡥ࡯ࡶࡤࡸ࡮ࡵ࡮ࠨধ")):
            self.implementation = l11l111ll1_Krypto_()
        t = []
        for k in self.l1l1l11111_Krypto_:
            if k not in d:
                break
            t.append(d[k])
        self.key = self.implementation._1l111111l_Krypto_.l11l11lll1_Krypto_(*tuple(t))
    def __repr__(self):
        attrs = []
        for k in self.l1l1l11111_Krypto_:
            if k == l1l1111_Krypto_ (u"ࠨࡰࠪন"):
                attrs.append(l1l1111_Krypto_ (u"ࠤࡱࠬࠪࡪࠩࠣ঩") % (self.size()+1,))
            elif hasattr(self.key, k):
                attrs.append(k)
        if self.l1l1111l1l_Krypto_():
            attrs.append(l1l1111_Krypto_ (u"ࠥࡴࡷ࡯ࡶࡢࡶࡨࠦপ"))
        return l1l1111_Krypto_ (u"ࠦࡁࠫࡳࠡࡂ࠳ࡼࠪࡾࠠࠦࡵࡁࠦফ") % (self.__class__.__name__, id(self), l1l1111_Krypto_ (u"ࠧ࠲ࠢব").join(attrs))
    def l11l11ll1l_Krypto_(self, format=l1l1111_Krypto_ (u"࠭ࡐࡆࡏࠪভ"), l11l1ll11l_Krypto_=None, l11l1l11l1_Krypto_=1):
        l1l1111_Krypto_ (u"ࠢࠣࠤࡈࡼࡵࡵࡲࡵࠢࡷ࡬࡮ࡹࠠࡓࡕࡄࠤࡰ࡫ࡹ࠯ࠌࠍࠤࠥࠦࠠࠡࠢࠣࠤ࠿ࡖࡡࡳࡣࡰࡩࡹ࡫ࡲࠡࡨࡲࡶࡲࡧࡴ࠻ࠢࡗ࡬ࡪࠦࡦࡰࡴࡰࡥࡹࠦࡴࡰࠢࡸࡷࡪࠦࡦࡰࡴࠣࡻࡷࡧࡰࡱ࡫ࡱ࡫ࠥࡺࡨࡦࠢ࡮ࡩࡾ࠴ࠊࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࠬࠪࡈࡊࡘࠧࠫ࠰ࠣࡆ࡮ࡴࡡࡳࡻࠣࡩࡳࡩ࡯ࡥ࡫ࡱ࡫࠱ࠦࡡ࡭ࡹࡤࡽࡸࠦࡵ࡯ࡧࡱࡧࡷࡿࡰࡵࡧࡧ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥ࠰ࠧࡑࡇࡐࠫ࠯࠴ࠠࡕࡧࡻࡸࡺࡧ࡬ࠡࡧࡱࡧࡴࡪࡩ࡯ࡩ࠯ࠤࡩࡵ࡮ࡦࠢࡤࡧࡨࡵࡲࡥ࡫ࡱ࡫ࠥࡺ࡯ࠡࡢࡕࡊࡈ࠷࠴࠳࠳ࡣࡣ࠴ࡦࡒࡇࡅ࠴࠸࠷࠹ࡠࡠ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡙ࠥࠦࠠࠡࠢࠣࡳ࡫࡮ࡤࡴࡼࡴࡹ࡫ࡤࠡࠪࡧࡩ࡫ࡧࡵ࡭ࡶࠬࠤࡴࡸࠠࡦࡰࡦࡶࡾࡶࡴࡦࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤ࠯࠭ࡏࡱࡧࡱࡗࡘࡎࠧࠫ࠰ࠣࡘࡪࡾࡴࡶࡣ࡯ࠤࡪࡴࡣࡰࡦ࡬ࡲ࡬࠲ࠠࡥࡱࡱࡩࠥࡧࡣࡤࡱࡵࡨ࡮ࡴࡧࠡࡶࡲࠤࡔࡶࡥ࡯ࡕࡖࡌࠥࡹࡰࡦࡥ࡬ࡪ࡮ࡩࡡࡵ࡫ࡲࡲ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡏ࡯࡮ࡼࠤࡸࡻࡩࡵࡣࡥࡰࡪࠦࡦࡰࡴࠣࡴࡺࡨ࡬ࡪࡥࠣ࡯ࡪࡿࡳࠡࠪࡱࡳࡹࠦࡰࡳ࡫ࡹࡥࡹ࡫ࠠ࡬ࡧࡼࡷ࠮࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠼ࡗࡽࡵ࡫ࠠࡧࡱࡵࡱࡦࡺ࠺ࠡࡵࡷࡶ࡮ࡴࡧࠋࠌࠣࠤࠥࠦࠠࠡࠢࠣ࠾ࡕࡧࡲࡢ࡯ࡨࡸࡪࡸࠠࡱࡣࡶࡷࡵ࡮ࡲࡢࡵࡨ࠾ࠥࡏ࡮ࠡࡥࡤࡷࡪࠦ࡯ࡧࠢࡓࡉࡒ࠲ࠠࡵࡪࡨࠤࡵࡧࡳࡴࠢࡳ࡬ࡷࡧࡳࡦࠢࡷࡳࠥࡪࡥࡳ࡫ࡹࡩࠥࡺࡨࡦࠢࡨࡲࡨࡸࡹࡱࡶ࡬ࡳࡳࠦ࡫ࡦࡻࠣࡪࡷࡵ࡭࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣ࠾࡙ࡿࡰࡦࠢࡳࡥࡸࡹࡰࡩࡴࡤࡷࡪࡀࠠࡴࡶࡵ࡭ࡳ࡭ࠠࠋࠌࠣࠤࠥࠦࠠࠡࠢࠣ࠾ࡕࡧࡲࡢ࡯ࡨࡸࡪࡸࠠࡱ࡭ࡦࡷ࠿ࠦࡔࡩࡧࠣࡔࡐࡉࡓࠡࡵࡷࡥࡳࡪࡡࡳࡦࠣࡸࡴࠦࡦࡰ࡮࡯ࡳࡼࠦࡦࡰࡴࠣࡥࡸࡹࡥ࡮ࡤ࡯࡭ࡳ࡭ࠠࡵࡪࡨࠤࡰ࡫ࡹ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡞ࡵࡵࠡࡪࡤࡺࡪࠦࡴࡸࡱࠣࡧ࡭ࡵࡩࡤࡧࡶ࠾ࠏࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡼ࡯ࡴࡩࠢ࠭࠮࠶࠰ࠪ࠭ࠢࡷ࡬ࡪࠦࡰࡶࡤ࡯࡭ࡨࠦ࡫ࡦࡻࠣ࡭ࡸࠦࡥ࡮ࡤࡨࡨࡩ࡫ࡤࠡ࡫ࡱࡸࡴࠦࡡ࡯࡛ࠢ࠲࠺࠶࠹ࠡࡢࡖࡹࡧࡰࡥࡤࡶࡓࡹࡧࡲࡩࡤࡍࡨࡽࡎࡴࡦࡰࡢࠣࡈࡊࡘࠠࡔࡇࡔ࡙ࡊࡔࡃࡆ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡖ࡫ࡩࠥࡶࡲࡪࡸࡤࡸࡪࠦ࡫ࡦࡻࠣ࡭ࡸࠦࡥ࡮ࡤࡨࡨࡩ࡫ࡤࠡ࡫ࡱࡸࡴࠦࡡࠡࡢࡓࡏࡈ࡙ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࡨࡪࡵࠣࡱࡴࡪࡥࠡ࡫ࡶࠤࡹ࡮ࡥࠡࡦࡨࡪࡦࡻ࡬ࡵ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡹ࡬ࡸ࡭ࠦࠪࠫ࠺࠭࠮࠱ࠦࡴࡩࡧࠣࡴࡷ࡯ࡶࡢࡶࡨࠤࡰ࡫ࡹࠡ࡫ࡶࠤࡪࡳࡢࡦࡦࡧࡩࡩࠦࡩ࡯ࡶࡲࠤࡦࠦࡠࡑࡍࡆࡗࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡘ࡭࡯ࡳࠡ࡯ࡲࡨࡪࠦࡩࡴࠢࡱࡳࡹࠦࡡࡷࡣ࡬ࡰࡦࡨ࡬ࡦࠢࡩࡳࡷࠦࡰࡶࡤ࡯࡭ࡨࠦ࡫ࡦࡻࡶ࠲ࠏࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࡒࡎࡇࡘࠦࡳࡵࡣࡱࡨࡦࡸࡤࡴࠢࡤࡶࡪࠦ࡮ࡰࡶࠣࡶࡪࡲࡥࡷࡣࡱࡸࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦࠪࡐࡲࡨࡲࡘ࡙ࡈࠫࠢࡩࡳࡷࡳࡡࡵ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࠿࡚ࡹࡱࡧࠣࡴࡰࡩࡳ࠻ࠢ࡬ࡲࡹ࡫ࡧࡦࡴࠍࠎࠥࠦࠠࠡࠢࠣࠤࠥࡀࡒࡦࡶࡸࡶࡳࡀࠠࡂࠢࡥࡽࡹ࡫ࠠࡴࡶࡵ࡭ࡳ࡭ࠠࡸ࡫ࡷ࡬ࠥࡺࡨࡦࠢࡨࡲࡨࡵࡤࡦࡦࠣࡴࡺࡨ࡬ࡪࡥࠣࡳࡷࠦࡰࡳ࡫ࡹࡥࡹ࡫ࠠࡩࡣ࡯ࡪ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠻ࡔࡤ࡭ࡸ࡫ࠠࡗࡣ࡯ࡹࡪࡋࡲࡳࡱࡵ࠾ࠏࠦࠠࠡࠢࠣࠤ࡛ࠥࠦࠠࠡࠢࠣ࡭࡫࡮ࠡࡶ࡫ࡩࠥ࡬࡯ࡳ࡯ࡤࡸࠥ࡯ࡳࠡࡷࡱ࡯ࡳࡵࡷ࡯࠰ࠍࠎࠥࠦࠠࠡࠢࠣࠤࠥ࠴࠮ࠡࡡࡕࡊࡈ࠷࠴࠳࠳࠽ࠤࠥࠦࠠࡩࡶࡷࡴ࠿࠵࠯ࡸࡹࡺ࠲࡮࡫ࡴࡧ࠰ࡲࡶ࡬࠵ࡲࡧࡥ࠲ࡶ࡫ࡩ࠱࠵࠴࠴࠲ࡹࡾࡴࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠱࠲ࠥࡥࡒࡇࡅ࠴࠸࠷࠹࠺ࠡࠢࠣࠤ࡭ࡺࡴࡱ࠼࠲࠳ࡼࡽࡷ࠯࡫ࡨࡸ࡫࠴࡯ࡳࡩ࠲ࡶ࡫ࡩ࠯ࡳࡨࡦ࠵࠹࠸࠳࠯ࡶࡻࡸࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠮࠯ࠢࡢࡤࡕࡑࡃࡔࠌࠣࠤࠥࠦࠠࠡࠢࠣ࠲࠳ࠦ࡟ࡡࡒࡎࡇࡘࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥম")
        if l11l1ll11l_Krypto_ is not None:
            l11l1ll11l_Krypto_ = tobytes(l11l1ll11l_Krypto_)
        if format==l1l1111_Krypto_ (u"ࠨࡑࡳࡩࡳ࡙ࡓࡉࠩয"):
               l11ll111l1_Krypto_ = l1ll1lllll_Krypto_(self.e)
               l11l1lllll_Krypto_ = l1ll1lllll_Krypto_(self.n)
               if l1lllllll1_Krypto_(l11ll111l1_Krypto_[0]) & 0x80: l11ll111l1_Krypto_=l11111l11_Krypto_(0x00)+l11ll111l1_Krypto_
               if l1lllllll1_Krypto_(l11l1lllll_Krypto_[0]) & 0x80: l11l1lllll_Krypto_=l11111l11_Krypto_(0x00)+l11l1lllll_Krypto_
               l11ll11l11_Krypto_ = [ l1l1111_Krypto_ (u"ࠩࡶࡷ࡭࠳ࡲࡴࡣࠪর"), l11ll111l1_Krypto_, l11l1lllll_Krypto_ ]
               l11l1l11ll_Krypto_ = l1l1111_Krypto_ (u"ࠪࠫ঱").join([ l1l1l1ll11_Krypto_.pack(l1l1111_Krypto_ (u"ࠦࡃࡏࠢল"),len(l11l11l1l1_Krypto_))+l11l11l1l1_Krypto_ for l11l11l1l1_Krypto_ in l11ll11l11_Krypto_])
               return l1l1111_Krypto_ (u"ࠬࡹࡳࡩ࠯ࡵࡷࡦࠦࠧ঳")+l11l111lll_Krypto_.b2a_base64(l11l1l11ll_Krypto_)[:-1]
        l11l1l111l_Krypto_ = l11l11llll_Krypto_()
        if self.l1l1111l1l_Krypto_():
                l11l11l1ll_Krypto_= { 1: l1l1111_Krypto_ (u"࠭ࡒࡔࡃࠣࡔࡗࡏࡖࡂࡖࡈࠫ঴"), 8: l1l1111_Krypto_ (u"ࠧࡑࡔࡌ࡚ࡆ࡚ࡅࠨ঵") }[l11l1l11l1_Krypto_]
                l11l1l111l_Krypto_[:] = [ 0, self.n, self.e, self.d, self.p, self.q,
                           self.d % (self.p-1), self.d % (self.q-1),
                           l11llll1ll_Krypto_(self.q, self.p) ]
                if l11l1l11l1_Krypto_==8:
                    l11ll11lll_Krypto_ = l11l1l111l_Krypto_.encode()
                    l11l1l111l_Krypto_ = l11l11llll_Krypto_([0])
                    l11l1l111l_Krypto_.append(l11ll11ll1_Krypto_)
                    l11l1l111l_Krypto_.append(l11l1ll1ll_Krypto_(l1l1111_Krypto_ (u"ࠨࡑࡆࡘࡊ࡚ࠠࡔࡖࡕࡍࡓࡍࠧশ"), l11ll11lll_Krypto_).encode())
        else:
                l11l11l1ll_Krypto_ = l1l1111_Krypto_ (u"ࠤࡓ࡙ࡇࡒࡉࡄࠤষ")
                l11l1l111l_Krypto_.append(l11ll11ll1_Krypto_)
                l11ll1l11l_Krypto_ = l11l1ll1ll_Krypto_(l1l1111_Krypto_ (u"ࠪࡆࡎ࡚ࠠࡔࡖࡕࡍࡓࡍࠧস"))
                l11l111l1l_Krypto_ = l11l11llll_Krypto_( [ self.n, self.e ] )
                l11ll1l11l_Krypto_.payload = l11111l11_Krypto_(0x00) + l11l111l1l_Krypto_.encode()
                l11l1l111l_Krypto_.append(l11ll1l11l_Krypto_.encode())
        if format==l1l1111_Krypto_ (u"ࠫࡉࡋࡒࠨহ"):
                return l11l1l111l_Krypto_.encode()
        if format==l1l1111_Krypto_ (u"ࠬࡖࡅࡎࠩ঺"):
                l11l11ll11_Krypto_ = b(l1l1111_Krypto_ (u"ࠨ࠭࠮࠯࠰࠱ࡇࡋࡇࡊࡐࠣࠦ঻") + l11l11l1ll_Krypto_ + l1l1111_Krypto_ (u"ࠢࠡࡍࡈ࡝࠲࠳࠭࠮࠯࡟ࡲ়ࠧ"))
                l11l1l1l11_Krypto_ = None
                if l11l1ll11l_Krypto_ and l11l11l1ll_Krypto_.endswith(l1l1111_Krypto_ (u"ࠨࡒࡕࡍ࡛ࡇࡔࡆࠩঽ")):
                    import l111ll1_Krypto_.l1lll1ll1_Krypto_.l1llllllll_Krypto_
                    from l111ll1_Krypto_.l11111l_Krypto_ import l11l1lll_Krypto_
                    from l111ll1_Krypto_.l11l1l1lll_Krypto_.l1l1l1l1l1_Krypto_ import l1l1l1l11l_Krypto_
                    l1l1l111ll_Krypto_ = self._11l1lll11_Krypto_(8)
                    key =  l1l1l1l11l_Krypto_(l11l1ll11l_Krypto_, l1l1l111ll_Krypto_, 16, 1, l111ll1_Krypto_.l1lll1ll1_Krypto_.l1llllllll_Krypto_)
                    key += l1l1l1l11l_Krypto_(key+l11l1ll11l_Krypto_, l1l1l111ll_Krypto_, 8, 1, l111ll1_Krypto_.l1lll1ll1_Krypto_.l1llllllll_Krypto_)
                    l11l1l1l11_Krypto_ = l11l1lll_Krypto_.new(key, l111ll1_Krypto_.l11111l_Krypto_.l11l1lll_Krypto_.l1lllll1_Krypto_, l1l1l111ll_Krypto_)
                    l11l11ll11_Krypto_ += b(l1l1111_Krypto_ (u"ࠩࡓࡶࡴࡩ࠭ࡕࡻࡳࡩ࠿ࠦ࠴࠭ࡇࡑࡇࡗ࡟ࡐࡕࡇࡇࡠࡳ࠭া"))
                    l11l11ll11_Krypto_ += b(l1l1111_Krypto_ (u"ࠪࡈࡊࡑ࠭ࡊࡰࡩࡳ࠿ࠦࡄࡆࡕ࠰ࡉࡉࡋ࠳࠮ࡅࡅࡇ࠱࠭ি")) + l11l111lll_Krypto_.b2a_hex(l1l1l111ll_Krypto_).upper() + b(l1l1111_Krypto_ (u"ࠫࡡࡴ࡜࡯ࠩী"))
                l11ll11l1l_Krypto_ = l11l1l111l_Krypto_.encode()
                if l11l1l1l11_Krypto_:
                    padding = l11l1l1l11_Krypto_.block_size-len(l11ll11l1l_Krypto_)%l11l1l1l11_Krypto_.block_size
                    l11ll11l1l_Krypto_ = l11l1l1l11_Krypto_.l1_Krypto_(l11ll11l1l_Krypto_+l11111l11_Krypto_(padding)*padding)
                chunks = [ l11l111lll_Krypto_.b2a_base64(l11ll11l1l_Krypto_[i:i+48]) for i in range(0, len(l11ll11l1l_Krypto_), 48) ]
                l11l11ll11_Krypto_ += b(l1l1111_Krypto_ (u"ࠬ࠭ু")).join(chunks)
                l11l11ll11_Krypto_ += b(l1l1111_Krypto_ (u"ࠨ࠭࠮࠯࠰࠱ࡊࡔࡄࠡࠤূ") + l11l11l1ll_Krypto_ + l1l1111_Krypto_ (u"ࠢࠡࡍࡈ࡝࠲࠳࠭࠮࠯ࠥৃ"))
                return l11l11ll11_Krypto_
        return ValueError(l1l1111_Krypto_ (u"ࠣࡗࡱ࡯ࡳࡵࡷ࡯ࠢ࡮ࡩࡾࠦࡦࡰࡴࡰࡥࡹࠦࠧࠦࡵࠪ࠲ࠥࡉࡡ࡯ࡰࡲࡸࠥ࡫ࡸࡱࡱࡵࡸࠥࡺࡨࡦࠢࡕࡗࡆࠦ࡫ࡦࡻ࠱ࠦৄ") % format)
class l11l111ll1_Krypto_(object):
    l1l1111_Krypto_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡄࡲࠥࡘࡓࡂࠢ࡮ࡩࡾࠦࡦࡢࡥࡷࡳࡷࡿ࠮ࠋࠌࠣࠤࠥࠦࡔࡩ࡫ࡶࠤࡨࡲࡡࡴࡵࠣ࡭ࡸࠦ࡯࡯࡮ࡼࠤ࡮ࡴࡴࡦࡴࡱࡥࡱࡲࡹࠡࡷࡶࡩࡩࠦࡴࡰࠢ࡬ࡱࡵࡲࡥ࡮ࡧࡱࡸࠥࡺࡨࡦࠢࡰࡩࡹ࡮࡯ࡥࡵࠣࡳ࡫ࠦࡴࡩࡧࠣࡤࡈࡸࡹࡱࡶࡲ࠲ࡕࡻࡢ࡭࡫ࡦࡏࡪࡿ࠮ࡓࡕࡄࡤࠥࡳ࡯ࡥࡷ࡯ࡩ࠳ࠐࠊࠡࠢࠣࠤ࠿ࡹ࡯ࡳࡶ࠽ࠤࡤࡥࡩ࡯࡫ࡷࡣࡤ࠲ࡧࡦࡰࡨࡶࡦࡺࡥ࠭ࡥࡲࡲࡸࡺࡲࡶࡥࡷ࠰࡮ࡳࡰࡰࡴࡷࡏࡪࡿࠊࠡࠢࠣࠤ࠿ࡻ࡮ࡥࡱࡦࡹࡲ࡫࡮ࡵࡧࡧ࠾ࠥࡥࡧࠫ࠮ࠣࡣ࡮࠰ࠊࠡࠢࠣࠤࠧࠨࠢ৅")
    def __init__(self, **kwargs):
        l1l1111_Krypto_ (u"ࠥࠦࠧࡉࡲࡦࡣࡷࡩࠥࡧࠠ࡯ࡧࡺࠤࡗ࡙ࡁࠡ࡭ࡨࡽࠥ࡬ࡡࡤࡶࡲࡶࡾ࠴ࠊࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠽ࡏࡪࡿࡷࡰࡴࡧࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࡷࡶࡩࡤ࡬ࡡࡴࡶࡢࡱࡦࡺࡨࠡ࠼ࠣࡦࡴࡵ࡬ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡙ࠥࡰࡦࡥ࡬ࡪࡾࠦࡷࡩ࡫ࡦ࡬ࠥࡳࡡࡵࡪࡨࡱࡦࡺࡩࡤࠢ࡯࡭ࡧࡸࡡࡳࡻࠣࡸࡴࠦࡵࡴࡧ࠽ࠎࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤ࠯ࡔ࡯࡯ࡧ࠭ࠤ࠭ࡪࡥࡧࡣࡸࡰࡹ࠯࠮ࠡࡗࡶࡩࠥ࡬ࡡࡴࡶࡨࡷࡹࠦ࡭ࡢࡶ࡫ࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࠫࡖࡵࡹࡪ࠰ࠠ࠯ࠢࡘࡷࡪࠦࡦࡢࡵࡷࠤࡲࡧࡴࡩ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢ࠭ࡊࡦࡲࡳࡦࠬࠣ࠲࡛ࠥࡳࡦࠢࡶࡰࡴࡽࠠ࡮ࡣࡷ࡬࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࡦࡨࡪࡦࡻ࡬ࡵࡡࡵࡥࡳࡪࡦࡶࡰࡦࠤ࠿ࠦࡣࡢ࡮࡯ࡥࡧࡲࡥࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡙ࠥࡰࡦࡥ࡬ࡪࡾࠦࡨࡰࡹࠣࡸࡴࠦࡣࡰ࡮࡯ࡩࡨࡺࠠࡳࡣࡱࡨࡴࡳࠠࡥࡣࡷࡥ࠿ࠐࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࠪࡏࡱࡱࡩ࠯ࠦࠨࡥࡧࡩࡥࡺࡲࡴࠪ࠰࡙ࠣࡸ࡫ࠠࡓࡣࡱࡨࡴࡳ࠮࡯ࡧࡺࠬ࠮࠴ࡲࡦࡣࡧࠬ࠮࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦ࡮ࡰࡶࠣ࠮ࡓࡵ࡮ࡦࠬࠣ࠲࡛ࠥࡳࡦࠢࡷ࡬ࡪࠦࡳࡱࡧࡦ࡭࡫࡯ࡥࡥࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࡩ࡯ࡲࡦࡥࡷࡰࡾ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠼ࡕࡥ࡮ࡹࡥࠡࡔࡸࡲࡹ࡯࡭ࡦࡇࡵࡶࡴࡸ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡗࡩࡧࡱࠤ࠯࠰ࡵࡴࡧࡢࡪࡦࡹࡴࡠ࡯ࡤࡸ࡭࠰ࠪࠡ࠿ࡗࡶࡺ࡫ࠠࡣࡷࡷࠤ࡫ࡧࡳࡵࠢࡰࡥࡹ࡮ࠠࡪࡵࠣࡲࡴࡺࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣ৆")
        l1l11l1ll1_Krypto_ = kwargs.get(l1l1111_Krypto_ (u"ࠫࡺࡹࡥࡠࡨࡤࡷࡹࡥ࡭ࡢࡶ࡫ࠫে"), None)
        if l1l11l1ll1_Krypto_ is None:
            if _1l11ll111_Krypto_ is not None:
                self._1l111111l_Krypto_ = _1l11ll111_Krypto_
            else:
                self._1l111111l_Krypto_ = _1l11llll1_Krypto_
        elif l1l11l1ll1_Krypto_:
            if _1l11ll111_Krypto_ is not None:
                self._1l111111l_Krypto_ = _1l11ll111_Krypto_
            else:
                raise RuntimeError(l1l1111_Krypto_ (u"ࠧ࡬ࡡࡴࡶࠣࡱࡦࡺࡨࠡ࡯ࡲࡨࡺࡲࡥࠡࡰࡲࡸࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥࠣৈ"))
        else:
            self._1l111111l_Krypto_ = _1l11llll1_Krypto_
        self.error = self._1l111111l_Krypto_.error
        self._1l111l11l_Krypto_ = kwargs.get(l1l1111_Krypto_ (u"࠭ࡤࡦࡨࡤࡹࡱࡺ࡟ࡳࡣࡱࡨ࡫ࡻ࡮ࡤࠩ৉"), None)
        self._1l11lllll_Krypto_ = None
    def _11lllllll_Krypto_(self, l1l11ll1ll_Krypto_):
        if l1l11ll1ll_Krypto_ is not None:
            return l1l11ll1ll_Krypto_
        elif self._1l11lllll_Krypto_ is None:
            self._1l11lllll_Krypto_ = l1ll1l11l1_Krypto_.new().read
        return self._1l11lllll_Krypto_
    def l1llllll1_Krypto_(self, bits, l1l11ll1ll_Krypto_=None, l1l1111lll_Krypto_=None, e=65537):
        l1l1111_Krypto_ (u"ࠢࠣࠤࡕࡥࡳࡪ࡯࡮࡮ࡼࠤ࡬࡫࡮ࡦࡴࡤࡸࡪࠦࡡࠡࡨࡵࡩࡸ࡮ࠬࠡࡰࡨࡻࠥࡘࡓࡂࠢ࡮ࡩࡾ࠴ࠊࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠽ࡔࡦࡸࡡ࡮ࡧࡷࡩࡷࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࡦ࡮ࡺࡳࠡ࠼ࠣ࡭ࡳࡺࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡌࡧࡼࠤࡱ࡫࡮ࡨࡶ࡫࠰ࠥࡵࡲࠡࡵ࡬ࡾࡪࠦࠨࡪࡰࠣࡦ࡮ࡺࡳࠪࠢࡲࡪࠥࡺࡨࡦࠢࡕࡗࡆࠦ࡭ࡰࡦࡸࡰࡺࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡋࡷࠤࡲࡻࡳࡵࠢࡥࡩࠥࡧࠠ࡮ࡷ࡯ࡸ࡮ࡶ࡬ࡦࠢࡲࡪࠥ࠸࠵࠷࠮ࠣࡥࡳࡪࠠ࡯ࡱࠣࡷࡲࡧ࡬࡭ࡧࡵࠤࡹ࡮ࡡ࡯ࠢ࠴࠴࠷࠺࠮ࠋࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࡷࡧ࡮ࡥࡨࡸࡲࡨࠦ࠺ࠡࡥࡤࡰࡱࡧࡢ࡭ࡧࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡖࡦࡴࡤࡰ࡯ࠣࡲࡺࡳࡢࡦࡴࠣ࡫ࡪࡴࡥࡳࡣࡷ࡭ࡴࡴࠠࡧࡷࡱࡧࡹ࡯࡯࡯࠽ࠣ࡭ࡹࠦࡳࡩࡱࡸࡰࡩࠦࡡࡤࡥࡨࡴࡹࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡡࠡࡵ࡬ࡲ࡬ࡲࡥࠡ࡫ࡱࡸࡪ࡭ࡥࡳࠢࡑࠤࡦࡴࡤࠡࡴࡨࡸࡺࡸ࡮ࠡࡣࠣࡷࡹࡸࡩ࡯ࡩࠣࡳ࡫ࠦࡲࡢࡰࡧࡳࡲࠦࡤࡢࡶࡤࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡓࠦࡢࡺࡶࡨࡷࠥࡲ࡯࡯ࡩ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡎ࡬ࠠ࡯ࡱࡷࠤࡸࡶࡥࡤ࡫ࡩ࡭ࡪࡪࠬࠡࡣࠣࡲࡪࡽࠠࡰࡰࡨࠤࡼ࡯࡬࡭ࠢࡥࡩࠥ࡯࡮ࡴࡶࡤࡲࡹ࡯ࡡࡵࡧࡧࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡫ࡸ࡯࡮ࠢࡣࡤࡈࡸࡹࡱࡶࡲ࠲ࡗࡧ࡮ࡥࡱࡰࡤࡥ࠴ࠊࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࡴࡷࡵࡧࡳࡧࡶࡷࡤ࡬ࡵ࡯ࡥࠣ࠾ࠥࡩࡡ࡭࡮ࡤࡦࡱ࡫ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡐࡲࡷ࡭ࡴࡴࡡ࡭ࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࡹ࡮ࡡࡵࠢࡺ࡭ࡱࡲࠠࡣࡧࠣࡧࡦࡲ࡬ࡦࡦࠣࡻ࡮ࡺࡨࠡࡣࠣࡷ࡭ࡵࡲࡵࠢࡶࡸࡷ࡯࡮ࡨࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡦࡳࡳࡺࡡࡪࡰ࡬ࡲ࡬ࠦࡴࡩࡧࠣ࡯ࡪࡿࠠࡱࡣࡵࡥࡲ࡫ࡴࡦࡴࠣࡧࡺࡸࡲࡦࡰࡷࡰࡾࠦࡢࡦ࡫ࡱ࡫ࠥ࡭ࡥ࡯ࡧࡵࡥࡹ࡫ࡤ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࡬ࡸࠬࡹࠠࡶࡵࡨࡪࡺࡲࠠࡧࡱࡵࠤ࡮ࡴࡴࡦࡴࡤࡧࡹ࡯ࡶࡦࠢࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴࡳࠡࡹ࡫ࡩࡷ࡫ࠠࡢࠢࡸࡷࡪࡸࠠࡪࡵࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡻࡦ࡯ࡴࡪࡰࡪࠤ࡫ࡵࡲࠡࡣࠣ࡯ࡪࡿࠠࡵࡱࠣࡦࡪࠦࡧࡦࡰࡨࡶࡦࡺࡥࡥ࠰ࠍࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࡥࠡ࠼ࠣ࡭ࡳࡺࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡑࡷࡥࡰ࡮ࡩࠠࡓࡕࡄࠤࡪࡾࡰࡰࡰࡨࡲࡹ࠴ࠠࡊࡶࠣࡱࡺࡹࡴࠡࡤࡨࠤࡦࡴࠠࡰࡦࡧࠤࡵࡵࡳࡪࡶ࡬ࡺࡪࠦࡩ࡯ࡶࡨ࡫ࡪࡸ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡋࡷࠤ࡮ࡹࠠࡵࡻࡳ࡭ࡨࡧ࡬࡭ࡻࠣࡥࠥࡹ࡭ࡢ࡮࡯ࠤࡳࡻ࡭ࡣࡧࡵࠤࡼ࡯ࡴࡩࠢࡹࡩࡷࡿࠠࡧࡧࡺࠤࡴࡴࡥࡴࠢ࡬ࡲࠥ࡯ࡴࡴࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡥ࡭ࡳࡧࡲࡺࠢࡵࡩࡵࡸࡥࡴࡧࡱࡸࡦࡺࡩࡰࡰ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡙࡮ࡥࠡࡦࡨࡪࡦࡻ࡬ࡵࠢࡹࡥࡱࡻࡥࠡ࠸࠸࠹࠸࠽ࠠࠩ࠿ࠣࡤࡥ࠶ࡢ࠲࠲࠳࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶࠰࠱࠲࠴ࡤࡥࠦࠩࠡ࡫ࡶࠤࡦࠦࡳࡢࡨࡨࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡨ࡮࡯ࡪࡥࡨ࠾ࠥࡵࡴࡩࡧࡵࠤࡨࡵ࡭࡮ࡱࡱࠤࡻࡧ࡬ࡶࡧࡶࠤࡦࡸࡥࠡ࠷࠯ࠤ࠼࠲ࠠ࠲࠹࠯ࠤࡦࡴࡤࠡ࠴࠸࠻࠳ࠐࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠼ࡤࡸࡹ࡫࡮ࡵ࡫ࡲࡲ࠿࡙ࠦࡰࡷࠣࡷ࡭ࡵࡵ࡭ࡦࠣࡥࡱࡽࡡࡺࡵࠣࡹࡸ࡫ࠠࡢࠢࡦࡶࡾࡶࡴࡰࡩࡵࡥࡵ࡮ࡩࡤࡣ࡯ࡰࡾࠦࡳࡦࡥࡸࡶࡪࠦࡲࡢࡰࡧࡳࡲࠦ࡮ࡶ࡯ࡥࡩࡷࠦࡧࡦࡰࡨࡶࡦࡺ࡯ࡳ࠮ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡵࡸࡧ࡭ࠦࡡࡴࠢࡷ࡬ࡪࠦ࡯࡯ࡧࠣࡨࡪ࡬ࡩ࡯ࡧࡧࠤ࡮ࡴࠠࡵࡪࡨࠤࡥࡦࡃࡳࡻࡳࡸࡴ࠴ࡒࡢࡰࡧࡳࡲࡦࡠࠡ࡯ࡲࡨࡺࡲࡥ࠼ࠢ࠭࠮ࡩࡵ࡮ࠨࡶ࠭࠮ࠥࡰࡵࡴࡶࠣࡹࡸ࡫ࠠࡵࡪࡨࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡦࡹࡷࡸࡥ࡯ࡶࠣࡸ࡮ࡳࡥࠡࡣࡱࡨࠥࡺࡨࡦࠢࡣࡤࡷࡧ࡮ࡥࡱࡰࡤࡥࠦ࡭ࡰࡦࡸࡰࡪ࠴ࠊࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠽ࡥࡹࡺࡥ࡯ࡶ࡬ࡳࡳࡀࠠࡆࡺࡳࡳࡳ࡫࡮ࡵࠢ࠶ࠤ࡮ࡹࠠࡢ࡮ࡶࡳࠥࡽࡩࡥࡧ࡯ࡽࠥࡻࡳࡦࡦ࠯ࠤࡧࡻࡴࠡ࡫ࡷࠤࡷ࡫ࡱࡶ࡫ࡵࡩࡸࠦࡶࡦࡴࡼࠤࡸࡶࡥࡤ࡫ࡤࡰࠥࡩࡡࡳࡧࠣࡻ࡭࡫࡮ࠡࡲࡤࡨࡩ࡯࡮ࡨࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡵࡪࡨࠤࡲ࡫ࡳࡴࡣࡪࡩ࠳ࠐࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠼ࡕࡩࡹࡻࡲ࡯࠼ࠣࡅࡳࠦࡒࡔࡃࠣ࡯ࡪࡿࠠࡰࡤ࡭ࡩࡨࡺࠠࠩࡢࡢࡖࡘࡇ࡯ࡣ࡬ࡣ࠭࠳ࠐࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠼ࡕࡥ࡮ࡹࡥࠡࡘࡤࡰࡺ࡫ࡅࡳࡴࡲࡶ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡜࡮ࡥ࡯ࠢ࠭࠮ࡧ࡯ࡴࡴࠬ࠭ࠤ࡮ࡹࠠࡵࡱࡲࠤࡱ࡯ࡴࡵ࡮ࡨࠤࡴࡸࠠ࡯ࡱࡷࠤࡦࠦ࡭ࡶ࡮ࡷ࡭ࡵࡲࡥࠡࡱࡩࠤ࠷࠻࠶࠭ࠢࡲࡶࠥࡽࡨࡦࡰࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠬ࠭ࡩ࠯࠰ࠠࡪࡵࠣࡲࡴࡺࠠࡰࡦࡧࠤࡴࡸࠠࡴ࡯ࡤࡰࡱ࡫ࡲࠡࡶ࡫ࡥࡳࠦ࠲࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨ৊")
        if bits < 1024 or (bits & 0xff) != 0:
            raise ValueError(l1l1111_Krypto_ (u"ࠣࡔࡖࡅࠥࡳ࡯ࡥࡷ࡯ࡹࡸࠦ࡬ࡦࡰࡪࡸ࡭ࠦ࡭ࡶࡵࡷࠤࡧ࡫ࠠࡢࠢࡰࡹࡱࡺࡩࡱ࡮ࡨࠤࡴ࡬ࠠ࠳࠷࠹ࠤࡦࡴࡤࠡࡀࡀࠤ࠶࠶࠲࠵ࠤো"))
        if e%2==0 or e<3:
            raise ValueError(l1l1111_Krypto_ (u"ࠤࡕࡗࡆࠦࡰࡶࡤ࡯࡭ࡨࠦࡥࡹࡲࡲࡲࡪࡴࡴࠡ࡯ࡸࡷࡹࠦࡢࡦࠢࡤࠤࡵࡵࡳࡪࡶ࡬ࡺࡪ࠲ࠠࡰࡦࡧࠤ࡮ࡴࡴࡦࡩࡨࡶࠥࡲࡡࡳࡩࡨࡶࠥࡺࡨࡢࡰࠣ࠶࠳ࠨৌ"))
        l1l111l1l1_Krypto_ = self._11lllllll_Krypto_(l1l11ll1ll_Krypto_)
        obj = _11l1l1111_Krypto_.l1l11l1111_Krypto_(bits, l1l111l1l1_Krypto_, l1l1111lll_Krypto_, e)
        key = self._1l111111l_Krypto_.l11l11lll1_Krypto_(obj.n, obj.e, obj.d, obj.p, obj.q, obj.u)
        return _11ll111ll_Krypto_(self, key)
    def l1l1l1111l_Krypto_(self, tup):
        l1l1111_Krypto_ (u"ࠥࠦࠧࡉ࡯࡯ࡵࡷࡶࡺࡩࡴࠡࡣࡱࠤࡗ࡙ࡁࠡ࡭ࡨࡽࠥ࡬ࡲࡰ࡯ࠣࡥࠥࡺࡵࡱ࡮ࡨࠤࡴ࡬ࠠࡷࡣ࡯࡭ࡩࠦࡒࡔࡃࠣࡧࡴࡳࡰࡰࡰࡨࡲࡹࡹ࠮ࠋࠌࠣࠤࠥࠦࠠࠡࠢࠣࡘ࡭࡫ࠠ࡮ࡱࡧࡹࡱࡻࡳࠡࠬ࠭ࡲ࠯࠰ࠠ࡮ࡷࡶࡸࠥࡨࡥࠡࡶ࡫ࡩࠥࡶࡲࡰࡦࡸࡧࡹࠦ࡯ࡧࠢࡷࡻࡴࠦࡰࡳ࡫ࡰࡩࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡖ࡫ࡩࠥࡶࡵࡣ࡮࡬ࡧࠥ࡫ࡸࡱࡱࡱࡩࡳࡺࠠࠫࠬࡨ࠮࠯ࠦ࡭ࡶࡵࡷࠤࡧ࡫ࠠࡰࡦࡧࠤࡦࡴࡤࠡ࡮ࡤࡶ࡬࡫ࡲࠡࡶ࡫ࡥࡳࠦ࠱࠯ࠌࠍࠤࠥࠦࠠࠡࠢࠣࠤࡎࡴࠠࡤࡣࡶࡩࠥࡵࡦࠡࡣࠣࡴࡷ࡯ࡶࡢࡶࡨࠤࡰ࡫ࡹ࠭ࠢࡷ࡬ࡪࠦࡦࡰ࡮࡯ࡳࡼ࡯࡮ࡨࠢࡨࡵࡺࡧࡴࡪࡱࡱࡷࠥࡳࡵࡴࡶࠣࡥࡵࡶ࡬ࡺ࠼ࠍࠎࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡦࠢࠤࡁࠥ࠷ࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡴ࠯ࡷࠠ࠾ࠢࡱࠎࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡦࠬࡧࠤࡂࠦ࠱ࠡ࡯ࡲࡨࠥ࠮ࡰ࠮࠳ࠬࠬࡶ࠳࠱ࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡶࠪࡶࠢࡀࠤ࠶ࠦ࡭ࡰࡦࠣࡵࠏࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠻ࡒࡤࡶࡦࡳࡥࡵࡧࡵࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࡶࡸࡴࠥࡀࠠࡵࡷࡳࡰࡪࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡇࠠࡵࡷࡳࡰࡪࠦ࡯ࡧࠢ࡯ࡳࡳ࡭ࠠࡪࡰࡷࡩ࡬࡫ࡲࡴ࠮ࠣࡻ࡮ࡺࡨࠡࡣࡷࠤࡱ࡫ࡡࡴࡶࠣ࠶ࠥࡧ࡮ࡥࠢࡱࡳࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡲࡵࡲࡦࠢࡷ࡬ࡦࡴࠠ࠷ࠢ࡬ࡸࡪࡳࡳ࠯ࠢࡗ࡬ࡪࠦࡩࡵࡧࡰࡷࠥࡩ࡯࡮ࡧࠣ࡭ࡳࠦࡴࡩࡧࠣࡪࡴࡲ࡬ࡰࡹ࡬ࡲ࡬ࠦ࡯ࡳࡦࡨࡶ࠿ࠐࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠱࠯ࠢࡕࡗࡆࠦ࡭ࡰࡦࡸࡰࡺࡹࠠࠩࡰࠬ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠷࠴ࠠࡑࡷࡥࡰ࡮ࡩࠠࡦࡺࡳࡳࡳ࡫࡮ࡵࠢࠫࡩ࠮࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠳࠯ࠢࡓࡶ࡮ࡼࡡࡵࡧࠣࡩࡽࡶ࡯࡯ࡧࡱࡸࠥ࠮ࡤࠪ࠰ࠣࡓࡳࡲࡹࠡࡴࡨࡵࡺ࡯ࡲࡦࡦࠣ࡭࡫ࠦࡴࡩࡧࠣ࡯ࡪࡿࠠࡪࡵࠣࡴࡷ࡯ࡶࡢࡶࡨ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠹࠴ࠠࡇ࡫ࡵࡷࡹࠦࡦࡢࡥࡷࡳࡷࠦ࡯ࡧࠢࡱࠤ࠭ࡶࠩ࠯ࠢࡒࡴࡹ࡯࡯࡯ࡣ࡯࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠺࠴ࠠࡔࡧࡦࡳࡳࡪࠠࡧࡣࡦࡸࡴࡸࠠࡰࡨࠣࡲࠥ࠮ࡱࠪ࠰ࠣࡓࡵࡺࡩࡰࡰࡤࡰ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠼࠮ࠡࡅࡕࡘࠥࡩ࡯ࡦࡨࡩ࡭ࡨ࡯ࡥ࡯ࡶ࠯ࠤ࠭࠷࠯ࡱࠫࠣࡱࡴࡪࠠࡲࠢࠫࡹ࠮࠴ࠠࡐࡲࡷ࡭ࡴࡴࡡ࡭࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠺ࡓࡧࡷࡹࡷࡴ࠺ࠡࡃࡱࠤࡗ࡙ࡁࠡ࡭ࡨࡽࠥࡵࡢ࡫ࡧࡦࡸࠥ࠮ࡠࡠࡔࡖࡅࡴࡨࡪࡡࠫ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨ্ࠢࠣ")
        key = self._1l111111l_Krypto_.l11l11lll1_Krypto_(*tup)
        return _11ll111ll_Krypto_(self, key)
    def _11l111l11_Krypto_(self, l11l1l1l1l_Krypto_):
        l1l1111_Krypto_ (u"ࠦࠧࠨࡉ࡮ࡲࡲࡶࡹࠦࡡ࡯ࠢࡕࡗࡆࠦ࡫ࡦࡻࠣࠬࡵࡻࡢ࡭࡫ࡦࠤࡴࡸࠠࡱࡴ࡬ࡺࡦࡺࡥࠡࡪࡤࡰ࡫࠯ࠬࠡࡧࡱࡧࡴࡪࡥࡥࠢ࡬ࡲࠥࡊࡅࡓࠢࡩࡳࡷࡳ࠮ࠣࠤࠥৎ")
        try:
            l11l1l111l_Krypto_ = l11l11llll_Krypto_()
            l11l1l111l_Krypto_.decode(l11l1l1l1l_Krypto_, True)
            if len(l11l1l111l_Krypto_)==9 and l11l1l111l_Krypto_.l11l11l11l_Krypto_() and l11l1l111l_Krypto_[0]==0:
                del l11l1l111l_Krypto_[6:]
                l11l1l111l_Krypto_.append(l11llll1ll_Krypto_(l11l1l111l_Krypto_[4],l11l1l111l_Krypto_[5]))
                del l11l1l111l_Krypto_[0]
                return self.l1l1l1111l_Krypto_(l11l1l111l_Krypto_[:])
            if len(l11l1l111l_Krypto_)==2:
                if l11l1l111l_Krypto_.l11l11l11l_Krypto_():
                    return self.l1l1l1111l_Krypto_(l11l1l111l_Krypto_[:])
                if l11l1l111l_Krypto_[0]==l11ll11ll1_Krypto_:
                        l11ll1l11l_Krypto_ = l11l1ll1ll_Krypto_()
                        l11ll1l11l_Krypto_.decode(l11l1l111l_Krypto_[1], True)
                        if l11ll1l11l_Krypto_.l11l1l1ll1_Krypto_(l1l1111_Krypto_ (u"ࠬࡈࡉࡕࠢࡖࡘࡗࡏࡎࡈࠩ৏")) and l1lllllll1_Krypto_(l11ll1l11l_Krypto_.payload[0])==0x00:
                                l11l1l111l_Krypto_.decode(l11ll1l11l_Krypto_.payload[1:], True)
                                if len(l11l1l111l_Krypto_)==2 and l11l1l111l_Krypto_.l11l11l11l_Krypto_():
                                        return self.l1l1l1111l_Krypto_(l11l1l111l_Krypto_[:])
            if l11l1l111l_Krypto_[0]==0:
                if l11l1l111l_Krypto_[1]==l11ll11ll1_Krypto_:
                    l11l1llll1_Krypto_ = l11l1ll1ll_Krypto_()
                    l11l1llll1_Krypto_.decode(l11l1l111l_Krypto_[2], True)
                    if l11l1llll1_Krypto_.l11l1l1ll1_Krypto_(l1l1111_Krypto_ (u"࠭ࡏࡄࡖࡈࡘ࡙ࠥࡔࡓࡋࡑࡋࠬ৐")):
                        return self._11l111l11_Krypto_(l11l1llll1_Krypto_.payload)
        except ValueError as IndexError:
            pass
        raise ValueError(l1l1111_Krypto_ (u"ࠢࡓࡕࡄࠤࡰ࡫ࡹࠡࡨࡲࡶࡲࡧࡴࠡ࡫ࡶࠤࡳࡵࡴࠡࡵࡸࡴࡵࡵࡲࡵࡧࡧࠦ৑"))
    def l11ll1111l_Krypto_(self, l11l1l1l1l_Krypto_, l11l1ll11l_Krypto_=None):
        l1l1111_Krypto_ (u"ࠣࠤࠥࡍࡲࡶ࡯ࡳࡶࠣࡥࡳࠦࡒࡔࡃࠣ࡯ࡪࡿࠠࠩࡲࡸࡦࡱ࡯ࡣࠡࡱࡵࠤࡵࡸࡩࡷࡣࡷࡩࠥ࡮ࡡ࡭ࡨࠬ࠰ࠥ࡫࡮ࡤࡱࡧࡩࡩࠦࡩ࡯ࠢࡶࡸࡦࡴࡤࡢࡴࡧࠤ࡫ࡵࡲ࡮࠰ࠍࠎࠥࠦࠠࠡࠢࠣࠤࠥࡀࡐࡢࡴࡤࡱࡪࡺࡥࡳࠢࡨࡼࡹ࡫ࡲ࡯ࡍࡨࡽ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡙࡮ࡥࠡࡔࡖࡅࠥࡱࡥࡺࠢࡷࡳࠥ࡯࡭ࡱࡱࡵࡸ࠱ࠦࡥ࡯ࡥࡲࡨࡪࡪࠠࡢࡵࠣࡥࠥࡹࡴࡳ࡫ࡱ࡫࠳ࠐࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡇ࡮ࠡࡔࡖࡅࠥࡶࡵࡣ࡮࡬ࡧࠥࡱࡥࡺࠢࡦࡥࡳࠦࡢࡦࠢ࡬ࡲࠥࡧ࡮ࡺࠢࡲࡪࠥࡺࡨࡦࠢࡩࡳࡱࡲ࡯ࡸ࡫ࡱ࡫ࠥ࡬࡯ࡳ࡯ࡤࡸࡸࡀࠊࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࠦ࠭ࠡ࠱࠹࠵࠿ࠠࡡࡵࡸࡦ࡯࡫ࡣࡵࡒࡸࡦࡱ࡯ࡣࡌࡧࡼࡍࡳ࡬࡯ࡡࠢࡇࡉࡗࠦࡓࡆࡓࡘࡉࡓࡉࡅࠡࠪࡥ࡭ࡳࡧࡲࡺࠢࡲࡶࠥࡖࡅࡎࠢࡨࡲࡨࡵࡤࡪࡰࡪ࠭ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡦࡐࡌࡅࡖࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡔࡶࡥ࡯ࡕࡖࡌࠥ࠮ࡴࡦࡺࡷࡹࡦࡲࠠࡱࡷࡥࡰ࡮ࡩࠠ࡬ࡧࡼࠤࡴࡴ࡬ࡺࠫࠍࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡄࡲࠥࡘࡓࡂࠢࡳࡶ࡮ࡼࡡࡵࡧࠣ࡯ࡪࡿࠠࡤࡣࡱࠤࡧ࡫ࠠࡪࡰࠣࡥࡳࡿࠠࡰࡨࠣࡸ࡭࡫ࠠࡧࡱ࡯ࡰࡴࡽࡩ࡯ࡩࠣࡪࡴࡸ࡭ࡢࡶࡶ࠾ࠏࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡐࡌࡅࡖࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡥࡖࡋࡄࡕࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡓࡵ࡫࡮ࡔࡕࡋࠤ࠭ࡺࡥࡹࡶࡸࡥࡱࠦࡰࡶࡤ࡯࡭ࡨࠦ࡫ࡦࡻࠣࡳࡳࡲࡹࠪࠌࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡈࡲࡶࠥࡪࡥࡵࡣ࡬ࡰࡸࠦࡡࡣࡱࡸࡸࠥࡺࡨࡦࠢࡓࡉࡒࠦࡥ࡯ࡥࡲࡨ࡮ࡴࡧ࠭ࠢࡶࡩࡪࠦࡠࡓࡈࡆ࠵࠹࠸࠱ࡡࡡ࠲ࡤࡗࡌࡃ࠲࠶࠵࠷ࡥࡥ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡏ࡮ࠡࡥࡤࡷࡪࠦ࡯ࡧࠢࡓࡉࡒࠦࡥ࡯ࡥࡲࡨ࡮ࡴࡧ࠭ࠢࡷ࡬ࡪࠦࡰࡳ࡫ࡹࡥࡹ࡫ࠠ࡬ࡧࡼࠤࡨࡧ࡮ࠡࡤࡨࠤࡪࡴࡣࡳࡻࡳࡸࡪࡪࠠࡸ࡫ࡷ࡬ࠥࡊࡅࡔࠢࡲࡶࠥ࠹ࡔࡅࡇࡖࠤࡦࡩࡣࡰࡴࡧ࡭ࡳ࡭ࠠࡵࡱࠣࡥࠥࡩࡥࡳࡶࡤ࡭ࡳࠦࡠࡡࡲࡤࡷࡸࠦࡰࡩࡴࡤࡷࡪࡦࡠ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡐࡰ࡯ࡽࠥࡕࡰࡦࡰࡖࡗࡑ࠳ࡣࡰ࡯ࡳࡥࡹ࡯ࡢ࡭ࡧࠣࡴࡦࡹࡳࠡࡲ࡫ࡶࡦࡹࡥࡴࠢࡤࡶࡪࠦࡳࡶࡲࡳࡳࡷࡺࡥࡥ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࠿࡚ࡹࡱࡧࠣࡩࡽࡺࡥࡳࡰࡎࡩࡾࡀࠠࡴࡶࡵ࡭ࡳ࡭ࠊࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠽ࡔࡦࡸࡡ࡮ࡧࡷࡩࡷࠦࡰࡢࡵࡶࡴ࡭ࡸࡡࡴࡧ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡌࡲࠥࡩࡡࡴࡧࠣࡳ࡫ࠦࡡ࡯ࠢࡨࡲࡨࡸࡹࡱࡶࡨࡨࠥࡖࡅࡎࠢ࡮ࡩࡾ࠲ࠠࡵࡪ࡬ࡷࠥ࡯ࡳࠡࡶ࡫ࡩࠥࡶࡡࡴࡵࠣࡴ࡭ࡸࡡࡴࡧࠣࡪࡷࡵ࡭ࠡࡹ࡫࡭ࡨ࡮ࠠࡵࡪࡨࠤࡪࡴࡣࡳࡻࡳࡸ࡮ࡵ࡮ࠡ࡭ࡨࡽࠥ࡯ࡳࠡࡦࡨࡶ࡮ࡼࡥࡥ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࠿࡚ࡹࡱࡧࠣࡴࡦࡹࡳࡱࡪࡵࡥࡸ࡫࠺ࠡࡵࡷࡶ࡮ࡴࡧࠋࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤ࠿ࡘࡥࡵࡷࡵࡲ࠿ࠦࡁ࡯ࠢࡕࡗࡆࠦ࡫ࡦࡻࠣࡳࡧࡰࡥࡤࡶࠣࠬࡥࡥࡒࡔࡃࡲࡦ࡯ࡦࠩ࠯ࠌࠍࠤࠥࠦࠠࠡࠢࠣࠤ࠿ࡘࡡࡪࡵࡨࠤ࡛ࡧ࡬ࡶࡧࡈࡶࡷࡵࡲ࠰ࡋࡱࡨࡪࡾࡅࡳࡴࡲࡶ࠴࡚ࡹࡱࡧࡈࡶࡷࡵࡲ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡘࡪࡨࡲࠥࡺࡨࡦࠢࡪ࡭ࡻ࡫࡮ࠡ࡭ࡨࡽࠥࡩࡡ࡯ࡰࡲࡸࠥࡨࡥࠡࡲࡤࡶࡸ࡫ࡤࠡࠪࡳࡳࡸࡹࡩࡣ࡮ࡼࠤࡧ࡫ࡣࡢࡷࡶࡩࠥࡺࡨࡦࠢࡳࡥࡸࡹࠠࡱࡪࡵࡥࡸ࡫ࠠࡪࡵࠣࡻࡷࡵ࡮ࡨࠫ࠱ࠎࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠮࠯ࠢࡢࡖࡋࡉ࠱࠵࠴࠴࠾ࠥ࡮ࡴࡵࡲ࠽࠳࠴ࡽࡷࡸ࠰࡬ࡩࡹ࡬࠮ࡰࡴࡪ࠳ࡷ࡬ࡣ࠰ࡴࡩࡧ࠶࠺࠲࠲࠰ࡷࡼࡹࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠯࠰ࠣࡣࡗࡌࡃ࠲࠶࠵࠷࠿ࠦࡨࡵࡶࡳ࠾࠴࠵ࡷࡸࡹ࠱࡭ࡪࡺࡦ࠯ࡱࡵ࡫࠴ࡸࡦࡤ࠱ࡵࡪࡨ࠷࠴࠳࠵࠱ࡸࡽࡺࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠰࠱ࠤࡤࡦࡐࡌࡅࡖࠎࠥࠦࠠࠡࠢࠣࠤࠥ࠴࠮ࠡࡡࡣࡔࡐࡉࡓࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧ৒")
        l11l1l1l1l_Krypto_ = tobytes(l11l1l1l1l_Krypto_)
        if l11l1ll11l_Krypto_ is not None:
            l11l1ll11l_Krypto_ = tobytes(l11l1ll11l_Krypto_)
        if l11l1l1l1l_Krypto_.startswith(b(l1l1111_Krypto_ (u"ࠩ࠰࠱࠲࠳࠭ࠨ৓"))):
                lines = l11l1l1l1l_Krypto_.replace(b(l1l1111_Krypto_ (u"ࠥࠤࠧ৔")),b(l1l1111_Krypto_ (u"ࠫࠬ৕"))).split()
                l11l11l111_Krypto_ = None
                if lines[1].startswith(b(l1l1111_Krypto_ (u"ࠬࡖࡲࡰࡥ࠰ࡘࡾࡶࡥ࠻࠶࠯ࡉࡓࡉࡒ࡚ࡒࡗࡉࡉ࠭৖"))):
                    l11ll1l111_Krypto_ = lines[2].split(b(l1l1111_Krypto_ (u"࠭࠺ࠨৗ")))
                    if len(l11ll1l111_Krypto_)!=2 or l11ll1l111_Krypto_[0]!=b(l1l1111_Krypto_ (u"ࠧࡅࡇࡎ࠱ࡎࡴࡦࡰࠩ৘")) or not l11l1ll11l_Krypto_:
                        raise ValueError(l1l1111_Krypto_ (u"ࠣࡒࡈࡑࠥ࡫࡮ࡤࡴࡼࡴࡹ࡯࡯࡯ࠢࡩࡳࡷࡳࡡࡵࠢࡱࡳࡹࠦࡳࡶࡲࡳࡳࡷࡺࡥࡥ࠰ࠥ৙"))
                    l11ll11111_Krypto_, l1l1l111ll_Krypto_ = l11ll1l111_Krypto_[1].split(b(l1l1111_Krypto_ (u"ࠩ࠯ࠫ৚")))
                    l1l1l111ll_Krypto_ = l11l111lll_Krypto_.a2b_hex(l1l1l111ll_Krypto_)
                    import l111ll1_Krypto_.l1lll1ll1_Krypto_.l1llllllll_Krypto_
                    from l111ll1_Krypto_.l11111l_Krypto_ import l11ll1l1_Krypto_, l11l1lll_Krypto_
                    from l111ll1_Krypto_.l11l1l1lll_Krypto_.l1l1l1l1l1_Krypto_ import l1l1l1l11l_Krypto_
                    if l11ll11111_Krypto_==b(l1l1111_Krypto_ (u"ࠥࡈࡊ࡙࠭ࡄࡄࡆࠦ৛")):
                        key = l1l1l1l11l_Krypto_(l11l1ll11l_Krypto_, l1l1l111ll_Krypto_, 8, 1, l111ll1_Krypto_.l1lll1ll1_Krypto_.l1llllllll_Krypto_)
                        l11l11l111_Krypto_ = l11ll1l1_Krypto_.new(key, l111ll1_Krypto_.l11111l_Krypto_.l11ll1l1_Krypto_.l1lllll1_Krypto_, l1l1l111ll_Krypto_)
                    elif l11ll11111_Krypto_==b(l1l1111_Krypto_ (u"ࠦࡉࡋࡓ࠮ࡇࡇࡉ࠸࠳ࡃࡃࡅࠥড়")):
                        key =  l1l1l1l11l_Krypto_(l11l1ll11l_Krypto_, l1l1l111ll_Krypto_, 16, 1, l111ll1_Krypto_.l1lll1ll1_Krypto_.l1llllllll_Krypto_)
                        key += l1l1l1l11l_Krypto_(key+l11l1ll11l_Krypto_, l1l1l111ll_Krypto_, 8, 1, l111ll1_Krypto_.l1lll1ll1_Krypto_.l1llllllll_Krypto_)
                        l11l11l111_Krypto_ = l11l1lll_Krypto_.new(key, l111ll1_Krypto_.l11111l_Krypto_.l11l1lll_Krypto_.l1lllll1_Krypto_, l1l1l111ll_Krypto_)
                    else:
                        raise ValueError(l1l1111_Krypto_ (u"࡛ࠧ࡮ࡴࡷࡳࡴࡴࡸࡴࠡࡒࡈࡑࠥ࡫࡮ࡤࡴࡼࡴࡹ࡯࡯࡯ࠢࡤࡰ࡬ࡵࡲࡪࡶ࡫ࡱ࠳ࠨঢ়"))
                    lines = lines[2:]
                l11l1l111l_Krypto_ = l11l111lll_Krypto_.a2b_base64(b(l1l1111_Krypto_ (u"࠭ࠧ৞")).join(lines[1:-1]))
                if l11l11l111_Krypto_:
                    l11l1l111l_Krypto_ = l11l11l111_Krypto_.l1lllll_Krypto_(l11l1l111l_Krypto_)
                    padding = l1lllllll1_Krypto_(l11l1l111l_Krypto_[-1])
                    l11l1l111l_Krypto_ = l11l1l111l_Krypto_[:-padding]
                return self._11l111l11_Krypto_(l11l1l111l_Krypto_)
        if l11l1l1l1l_Krypto_.startswith(b(l1l1111_Krypto_ (u"ࠧࡴࡵ࡫࠱ࡷࡹࡡࠡࠩয়"))):
                l11l1l11ll_Krypto_ = l11l111lll_Krypto_.a2b_base64(l11l1l1l1l_Krypto_.split(b(l1l1111_Krypto_ (u"ࠨࠢࠪৠ")))[1])
                l11ll11l11_Krypto_ = []
                while len(l11l1l11ll_Krypto_)>4:
                    l = l1l1l1ll11_Krypto_.unpack(l1l1111_Krypto_ (u"ࠤࡁࡍࠧৡ"),l11l1l11ll_Krypto_[:4])[0]
                    l11ll11l11_Krypto_.append(l11l1l11ll_Krypto_[4:4+l])
                    l11l1l11ll_Krypto_ = l11l1l11ll_Krypto_[4+l:]
                e = l1ll111ll1_Krypto_(l11ll11l11_Krypto_[1])
                n = l1ll111ll1_Krypto_(l11ll11l11_Krypto_[2])
                return self.l1l1l1111l_Krypto_([n, e])
        if l1lllllll1_Krypto_(l11l1l1l1l_Krypto_[0])==0x30:
                return self._11l111l11_Krypto_(l11l1l1l1l_Krypto_)
        raise ValueError(l1l1111_Krypto_ (u"ࠥࡖࡘࡇࠠ࡬ࡧࡼࠤ࡫ࡵࡲ࡮ࡣࡷࠤ࡮ࡹࠠ࡯ࡱࡷࠤࡸࡻࡰࡱࡱࡵࡸࡪࡪࠢৢ"))
l11ll11ll1_Krypto_ = l11l11llll_Krypto_(
  [ b(l1l1111_Krypto_ (u"ࠫࡡࡾ࠰࠷࡞ࡻ࠴࠾ࡢࡸ࠳ࡃ࡟ࡼ࠽࠼࡜ࡹ࠶࠻ࡠࡽ࠾࠶࡝ࡺࡉ࠻ࡡࡾ࠰ࡅ࡞ࡻ࠴࠶ࡢࡸ࠱࠳࡟ࡼ࠵࠷ࠧৣ")),
  l11l1ll1l1_Krypto_().encode() ]
  ).encode()
_impl = l11l111ll1_Krypto_()
l1llllll1_Krypto_ = _impl.l1llllll1_Krypto_
l1l1l1111l_Krypto_ = _impl.l1l1l1111l_Krypto_
l11ll1111l_Krypto_ = _impl.l11ll1111l_Krypto_
error = _impl.error