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
l1l1111_Krypto_ (u"ࠣࠤࠥࡗࡪࡲࡦ࠮ࡶࡨࡷࡹࠦࡦࡰࡴࠣࡴࡺࡨ࡬ࡪࡥ࠰࡯ࡪࡿࠠࡤࡴࡼࡴࡹࡵࠢࠣࠤᢏ")
__revision__ = l1l1111_Krypto_ (u"ࠤࠧࡍࡩࠪࠢᢐ")
import os as l1111111l1_Krypto_
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    tests = []
    from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l11l11l1_Krypto_ import l11lll1llll_Krypto_;       tests += l11lll1llll_Krypto_.l1ll1llll11_Krypto_(l1ll1lll111_Krypto_=l1ll1lll111_Krypto_)
    from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l11l11l1_Krypto_ import l11l11llll1_Krypto_;       tests += l11l11llll1_Krypto_.l1ll1llll11_Krypto_(l1ll1lll111_Krypto_=l1ll1lll111_Krypto_)
    from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l11l11l1_Krypto_ import l11l1l1ll11_Krypto_; tests += l11l1l1ll11_Krypto_.l1ll1llll11_Krypto_(l1ll1lll111_Krypto_=l1ll1lll111_Krypto_)
    from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l11l11l1_Krypto_ import l11ll1l1l11_Krypto_;   tests += l11ll1l1l11_Krypto_.l1ll1llll11_Krypto_(l1ll1lll111_Krypto_=l1ll1lll111_Krypto_)
    return tests
if __name__ == l1l1111_Krypto_ (u"ࠪࡣࡤࡳࡡࡪࡰࡢࡣࠬᢑ"):
    import unittest as l1lll111111_Krypto_
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"ࠫࡸࡻࡩࡵࡧࠪᢒ"))