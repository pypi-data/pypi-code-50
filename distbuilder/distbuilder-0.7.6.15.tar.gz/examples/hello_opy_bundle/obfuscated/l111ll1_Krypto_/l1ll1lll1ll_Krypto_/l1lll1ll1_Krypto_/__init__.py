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
l1l1111_Krypto_ (u"ࠧࠨࠢࡔࡧ࡯ࡪ࠲ࡺࡥࡴࡶࠣࡪࡴࡸࠠࡩࡣࡶ࡬ࠥࡳ࡯ࡥࡷ࡯ࡩࡸࠨࠢࠣ᝘")
__revision__ = l1l1111_Krypto_ (u"ࠨࠤࡊࡦࠧࠦ᝙")
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    tests = []
    from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l1lll1ll1_Krypto_ import l1l111l1lll_Krypto_;   tests += l1l111l1lll_Krypto_.l1ll1llll11_Krypto_(l1ll1lll111_Krypto_=l1ll1lll111_Krypto_)
    from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l1lll1ll1_Krypto_ import l1l111l11l1_Krypto_;    tests += l1l111l11l1_Krypto_.l1ll1llll11_Krypto_(l1ll1lll111_Krypto_=l1ll1lll111_Krypto_)
    from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l1lll1ll1_Krypto_ import l1l111l111l_Krypto_;    tests += l1l111l111l_Krypto_.l1ll1llll11_Krypto_(l1ll1lll111_Krypto_=l1ll1lll111_Krypto_)
    from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l1lll1ll1_Krypto_ import l1l111l1111_Krypto_;    tests += l1l111l1111_Krypto_.l1ll1llll11_Krypto_(l1ll1lll111_Krypto_=l1ll1lll111_Krypto_)
    from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l1lll1ll1_Krypto_ import l1l1111llll_Krypto_; tests += l1l1111llll_Krypto_.l1ll1llll11_Krypto_(l1ll1lll111_Krypto_=l1ll1lll111_Krypto_)
    from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l1lll1ll1_Krypto_ import l1l1111lll1_Krypto_;    tests += l1l1111lll1_Krypto_.l1ll1llll11_Krypto_(l1ll1lll111_Krypto_=l1ll1lll111_Krypto_)
    from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l1lll1ll1_Krypto_ import l1l1111l1ll_Krypto_; tests += l1l1111l1ll_Krypto_.l1ll1llll11_Krypto_(l1ll1lll111_Krypto_=l1ll1lll111_Krypto_)
    try:
        from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l1lll1ll1_Krypto_ import l1l1111ll1l_Krypto_; tests += l1l1111ll1l_Krypto_.l1ll1llll11_Krypto_(l1ll1lll111_Krypto_=l1ll1lll111_Krypto_)
        from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l1lll1ll1_Krypto_ import l1l1111l11l_Krypto_; tests += l1l1111l11l_Krypto_.l1ll1llll11_Krypto_(l1ll1lll111_Krypto_=l1ll1lll111_Krypto_)
        from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l1lll1ll1_Krypto_ import l1l1111l111_Krypto_; tests += l1l1111l111_Krypto_.l1ll1llll11_Krypto_(l1ll1lll111_Krypto_=l1ll1lll111_Krypto_)
    except ImportError:
        import sys as l1l11l11_Krypto_
        l1l11l11_Krypto_.stderr.write(l1l1111_Krypto_ (u"ࠢࡔࡧ࡯ࡪ࡙࡫ࡳࡵ࠼ࠣࡻࡦࡸ࡮ࡪࡰࡪ࠾ࠥࡴ࡯ࡵࠢࡷࡩࡸࡺࡩ࡯ࡩࠣࡗࡍࡇ࠲࠳࠶࠲ࡗࡍࡇ࠳࠹࠶࠲ࡗࡍࡇ࠵࠲࠴ࠣࡱࡴࡪࡵ࡭ࡧࡶࠤ࠭ࡴ࡯ࡵࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩ࠮ࡢ࡮ࠣ᝚"))
    return tests
if __name__ == l1l1111_Krypto_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪ᝛"):
    import unittest as l1lll111111_Krypto_
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"ࠩࡶࡹ࡮ࡺࡥࠨ᝜"))