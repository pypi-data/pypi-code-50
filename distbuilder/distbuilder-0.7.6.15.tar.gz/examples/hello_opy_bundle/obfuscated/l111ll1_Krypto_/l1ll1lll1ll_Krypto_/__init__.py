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
l1l1111_Krypto_ (u"ࠣࠤࠥࡗࡪࡲࡦࠡࡶࡨࡷࡹࡹࠊࠋࡖ࡫ࡩࡸ࡫ࠠࡵࡧࡶࡸࡸࠦࡳࡩࡱࡸࡰࡩࠦࡰࡦࡴࡩࡳࡷࡳࠠࡲࡷ࡬ࡧࡰࡲࡹࠡࡣࡱࡨࠥࡩࡡ࡯ࠢ࡬ࡨࡪࡧ࡬࡭ࡻࠣࡦࡪࠦࡵࡴࡧࡧࠤࡪࡼࡥࡳࡻࠣࡸ࡮ࡳࡥࠡࡣࡱࠎࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯ࠢࡵࡹࡳࡹ࠮ࠋࠤࠥࠦੳ")
__revision__ = l1l1111_Krypto_ (u"ࠤࠧࡍࡩࠪࠢੴ")
import sys as l1l11l11_Krypto_
import unittest as l1lll111111_Krypto_
from io import StringIO as l1ll1lll11l_Krypto_
class l1ll1lll1l1_Krypto_(Exception):
    def __init__(self, message, result):
        Exception.__init__(self, message, result)
        self.message = message
        self.result = result
def run(module=None, verbosity=0, stream=None, tests=None, l1ll1lll111_Krypto_=None, **kwargs):
    l1l1111_Krypto_ (u"ࠥࠦࠧࡋࡸࡦࡥࡸࡸࡪࠦࡳࡦ࡮ࡩ࠱ࡹ࡫ࡳࡵࡵ࠱ࠎࠏࠦࠠࠡࠢࡗ࡬࡮ࡹࠠࡳࡣ࡬ࡷࡪࡹࠠࡔࡧ࡯ࡪ࡙࡫ࡳࡵࡇࡵࡶࡴࡸࠠࡪࡨࠣࡥࡳࡿࠠࡵࡧࡶࡸࠥ࡯ࡳࠡࡷࡱࡷࡺࡩࡣࡦࡵࡶࡪࡺࡲ࠮ࠋࠌࠣࠤ࡙ࠥࠦࡰࡷࠣࡱࡦࡿࠠࡰࡲࡷ࡭ࡴࡴࡡ࡭࡮ࡼࠤࡵࡧࡳࡴࠢ࡬ࡲࠥࡧࠠࡴࡷࡥ࠱ࡲࡵࡤࡶ࡮ࡨࠤࡴ࡬ࠠࡔࡧ࡯ࡪ࡙࡫ࡳࡵࠢ࡬ࡪࠥࡿ࡯ࡶࠢࡲࡲࡱࡿࠠࡸࡣࡱࡸࠥࡺ࡯ࠋࠢࠣࠤࠥࡶࡥࡳࡨࡲࡶࡲࠦࡳࡰ࡯ࡨࠤࡴ࡬ࠠࡵࡪࡨࠤࡹ࡫ࡳࡵࡵ࠱ࠤࠥࡌ࡯ࡳࠢࡨࡼࡦࡳࡰ࡭ࡧ࠯ࠤࡹ࡮ࡥࠡࡨࡲࡰࡱࡵࡷࡪࡰࡪࠤࡼࡵࡵ࡭ࡦࠣࡸࡪࡹࡴࠡࡱࡱࡰࡾࠦࡴࡩࡧࠍࠤࠥࠦࠠࡩࡣࡶ࡬ࠥࡳ࡯ࡥࡷ࡯ࡩࡸࡀࠊࠋࠢࠣࠤࠥࠦࠠࠡࠢࡆࡶࡾࡶࡴࡰ࠰ࡖࡩࡱ࡬ࡔࡦࡵࡷ࠲ࡷࡻ࡮ࠩࡅࡵࡽࡵࡺ࡯࠯ࡕࡨࡰ࡫࡚ࡥࡴࡶ࠱ࡌࡦࡹࡨࠪࠌࠍࠤࠥࠦࠠࠣࠤࠥੵ")
    if l1ll1lll111_Krypto_ is None:
        l1ll1lll111_Krypto_ = {}
    suite = l1lll111111_Krypto_.TestSuite()
    if module is None:
        if tests is None:
            tests = l1ll1llll11_Krypto_(l1ll1lll111_Krypto_=l1ll1lll111_Krypto_)
        suite.addTests(tests)
    else:
        if tests is None:
            suite.addTests(module.l1ll1llll11_Krypto_(l1ll1lll111_Krypto_=l1ll1lll111_Krypto_))
        else:
            raise ValueError(l1l1111_Krypto_ (u"ࠦࠬࡳ࡯ࡥࡷ࡯ࡩࠬࠦࡡ࡯ࡦࠣࠫࡹ࡫ࡳࡵࡵࠪࠤࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠠࡢࡴࡨࠤࡲࡻࡴࡶࡣ࡯ࡰࡾࠦࡥࡹࡥ࡯ࡹࡸ࡯ࡶࡦࠤ੶"))
    if stream is None:
        kwargs[l1l1111_Krypto_ (u"ࠬࡹࡴࡳࡧࡤࡱࠬ੷")] = l1ll1lll11l_Krypto_()
    runner = l1lll111111_Krypto_.TextTestRunner(verbosity=verbosity, **kwargs)
    result = runner.run(suite)
    if not result.wasSuccessful():
        if stream is None:
            l1l11l11_Krypto_.stderr.write(stream.getvalue())
        raise l1ll1lll1l1_Krypto_(l1l1111_Krypto_ (u"ࠨࡓࡦ࡮ࡩ࠱ࡹ࡫ࡳࡵࠢࡩࡥ࡮ࡲࡥࡥࠤ੸"), result)
    return result
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    tests = []
    from l111ll1_Krypto_.l1ll1lll1ll_Krypto_ import l11111l_Krypto_; tests += l11111l_Krypto_.l1ll1llll11_Krypto_(l1ll1lll111_Krypto_=l1ll1lll111_Krypto_)
    from l111ll1_Krypto_.l1ll1lll1ll_Krypto_ import l1lll1ll1_Krypto_;   tests += l1lll1ll1_Krypto_.l1ll1llll11_Krypto_(l1ll1lll111_Krypto_=l1ll1lll111_Krypto_)
    from l111ll1_Krypto_.l1ll1lll1ll_Krypto_ import l11l1l1lll_Krypto_; tests += l11l1l1lll_Krypto_.l1ll1llll11_Krypto_(l1ll1lll111_Krypto_=l1ll1lll111_Krypto_)
    from l111ll1_Krypto_.l1ll1lll1ll_Krypto_ import l11l11l1_Krypto_; tests += l11l11l1_Krypto_.l1ll1llll11_Krypto_(l1ll1lll111_Krypto_=l1ll1lll111_Krypto_)
    from l111ll1_Krypto_.l1ll1lll1ll_Krypto_ import l1ll1l11l1_Krypto_; tests += l1ll1l11l1_Krypto_.l1ll1llll11_Krypto_(l1ll1lll111_Krypto_=l1ll1lll111_Krypto_)
    from l111ll1_Krypto_.l1ll1lll1ll_Krypto_ import l1l111ll_Krypto_;   tests += l1l111ll_Krypto_.l1ll1llll11_Krypto_(l1ll1lll111_Krypto_=l1ll1lll111_Krypto_)
    from l111ll1_Krypto_.l1ll1lll1ll_Krypto_ import Signature;   tests += Signature.l1ll1llll11_Krypto_(l1ll1lll111_Krypto_=l1ll1lll111_Krypto_)
    return tests
if __name__ == l1l1111_Krypto_ (u"ࠧࡠࡡࡰࡥ࡮ࡴ࡟ࡠࠩ੹"):
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧ੺"))