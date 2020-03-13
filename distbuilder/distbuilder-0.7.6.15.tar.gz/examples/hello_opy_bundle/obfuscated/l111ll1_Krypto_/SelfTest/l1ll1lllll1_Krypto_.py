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
l1l1111_Krypto_ (u"ࠢࠣࠤࡆࡳࡲࡳ࡯࡯ࠢࡩࡹࡳࡩࡴࡪࡱࡱࡷࠥ࡬࡯ࡳࠢࡖࡩࡱ࡬ࡔࡦࡵࡷࠤࡲࡵࡤࡶ࡮ࡨࡷࠧࠨࠢ੫")
__revision__ = l1l1111_Krypto_ (u"ࠣࠦࡌࡨࠩࠨ੬")
import unittest as l1lll111111_Krypto_
import binascii as l11l111lll_Krypto_
import sys as l1l11l11_Krypto_
if l1l11l11_Krypto_.version_info[0] == 2 and l1l11l11_Krypto_.version_info[1] == 1:
    from l111ll1_Krypto_.l1l111ll_Krypto_.l1l1ll1l_Krypto_ import *
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
class _1ll1llll1l_Krypto_(l1lll111111_Krypto_.TestLoader):
    suiteClass = list
def l1lll1111l1_Krypto_(l1lll11111l_Krypto_):
    l1l1111_Krypto_ (u"ࠤࠥࠦࡗ࡫ࡴࡶࡴࡱࠤࡦࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡕࡧࡶࡸࡈࡧࡳࡦࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷࠥ࡭ࡩࡷࡧࡱࠤࡦࠦࡔࡦࡵࡷࡇࡦࡹࡥࠡࡥ࡯ࡥࡸࡹࠊࠋࠢࠣࠤ࡚ࠥࡨࡪࡵࠣ࡭ࡸࠦࡵࡴࡧࡩࡹࡱࠦࡷࡩࡧࡱࠤࡾࡵࡵࠡࡪࡤࡺࡪࠦࡤࡦࡨ࡬ࡲࡪࡪࠠࡵࡧࡶࡸ࠯ࠦ࡭ࡦࡶ࡫ࡳࡩࡹࠠࡰࡰࠣࡽࡴࡻࡲࠡࡖࡨࡷࡹࡉࡡࡴࡧࠣࡧࡱࡧࡳࡴ࠰ࠍࠤࠥࠦࠠࠣࠤࠥ੭")
    return _1ll1llll1l_Krypto_().loadTestsFromTestCase(l1lll11111l_Krypto_)
def l1ll1llllll_Krypto_(s):
    l1l1111_Krypto_ (u"ࠥࠦࠧࡘࡥ࡮ࡱࡹࡩࠥࡽࡨࡪࡶࡨࡷࡵࡧࡣࡦࠢࡩࡶࡴࡳࠠࡢࠢࡷࡩࡽࡺࠠࡰࡴࠣࡦࡾࡺࡥࠡࡵࡷࡶ࡮ࡴࡧࠣࠤࠥ੮")
    if isinstance(s,str):
        return b(l1l1111_Krypto_ (u"ࠦࠧ੯").join(s.split()))
    else:
        return b(l1l1111_Krypto_ (u"ࠧࠨੰ")).join(s.split())
def a2b_hex(s):
    l1l1111_Krypto_ (u"ࠨࠢࠣࡅࡲࡲࡻ࡫ࡲࡵࠢ࡫ࡩࡽࡧࡤࡦࡥ࡬ࡱࡦࡲࠠࡵࡱࠣࡦ࡮ࡴࡡࡳࡻ࠯ࠤ࡮࡭࡮ࡰࡴ࡬ࡲ࡬ࠦࡷࡩ࡫ࡷࡩࡸࡶࡡࡤࡧࠥࠦࠧੱ")
    return l11l111lll_Krypto_.a2b_hex(l1ll1llllll_Krypto_(s))
def b2a_hex(s):
    l1l1111_Krypto_ (u"ࠢࠣࠤࡆࡳࡳࡼࡥࡳࡶࠣࡦ࡮ࡴࡡࡳࡻࠣࡸࡴࠦࡨࡦࡺࡤࡨࡪࡩࡩ࡮ࡣ࡯ࠦࠧࠨੲ")
    return l11l111lll_Krypto_.b2a_hex(s)