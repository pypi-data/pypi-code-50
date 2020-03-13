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
l1l1111_Krypto_ (u"ࠢࠣࠤࡖࡩࡱ࡬࠭ࡵࡧࡶࡸࠥࡹࡵࡪࡶࡨࠤ࡫ࡵࡲࠡࡩࡨࡲࡪࡸࡩࡤࠢࡆࡶࡾࡶࡴࡰ࠰ࡕࡥࡳࡪ࡯࡮ࠢࡶࡸࡺ࡬ࡦࠡࠤࠥࠦᢱ")
__revision__ = l1l1111_Krypto_ (u"ࠣࠦࡌࡨࠩࠨᢲ")
import binascii as l11l111lll_Krypto_
import pprint as l111llll1ll_Krypto_
import unittest as l1lll111111_Krypto_
import os as l1111111l1_Krypto_
import time as l11111l111_Krypto_
import sys as l1l11l11_Krypto_
if l1l11l11_Krypto_.version_info[0] == 2 and l1l11l11_Krypto_.version_info[1] == 1:
    from l111ll1_Krypto_.l1l111ll_Krypto_.l1l1ll1l_Krypto_ import *
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
try:
    import multiprocessing as l111lllll1l_Krypto_
except ImportError:
    l111lllll1l_Krypto_ = None
import l111ll1_Krypto_.l1ll1l11l1_Krypto_._1111lll11_Krypto_
import l111ll1_Krypto_.l1ll1l11l1_Krypto_.l111l1l111_Krypto_
class l111llll1l1_Krypto_(l1lll111111_Krypto_.TestCase):
    def _111llll11l_Krypto_(self):
        l1l1111_Krypto_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡇࡦࡶࠣࡤࡋࡵࡲࡵࡷࡱࡥࡆࡩࡣࡶ࡯ࡸࡰࡦࡺ࡯ࡳ࠰ࡵࡩࡸ࡫ࡥࡥࡡࡦࡳࡺࡴࡴࡡ࠮ࠣࡸ࡭࡫ࠠࡨ࡮ࡲࡦࡦࡲࠠࡤࡱࡸࡲࡹࠦ࡯ࡧࠢࡷ࡬ࡪࠐࠠࠡࠢࠣࠤࠥࠦࠠ࡯ࡷࡰࡦࡪࡸࠠࡰࡨࠣࡸ࡮ࡳࡥࡴࠢࡷ࡬ࡦࡺࠠࡵࡪࡨࠤࡕࡘࡎࡈࠢ࡫ࡥࡸࠦࡢࡦࡧࡱࠤࡷ࡫ࡳࡦࡧࡧࡩࡩ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᢳ")
        l111lll1l11_Krypto_ = l111ll1_Krypto_.l1ll1l11l1_Krypto_._1111lll11_Krypto_._1111l111l_Krypto_()
        l111lll1l11_Krypto_._lock.acquire()
        try:
            return l111lll1l11_Krypto_._1111l11ll_Krypto_.l1lllll1l1l_Krypto_
        finally:
            l111lll1l11_Krypto_._lock.release()
    def runTest(self):
        if l1l11l11_Krypto_.platform.startswith(l1l1111_Krypto_ (u"ࠪࡻ࡮ࡴࠧᢴ")):
            assert not hasattr(l1111111l1_Krypto_, l1l1111_Krypto_ (u"ࠫ࡫ࡵࡲ࡬ࠩᢵ"))
            return
        l11111l111_Krypto_.sleep(0.15)
        l111ll1llll_Krypto_ = self._111llll11l_Krypto_()
        l111ll1_Krypto_.l1ll1l11l1_Krypto_._1111lll11_Krypto_._1111l111l_Krypto_().l1111ll11l_Krypto_()
        l111ll1_Krypto_.l1ll1l11l1_Krypto_.l1111l11l1_Krypto_(1)
        l111lll11l1_Krypto_ = self._111llll11l_Krypto_()
        self.assertNotEqual(l111ll1llll_Krypto_, l111lll11l1_Krypto_)
        l111ll1l1l1_Krypto_ = []
        for i in range(10):
            l111ll1l1ll_Krypto_, l111lllll11_Krypto_ = l1111111l1_Krypto_.pipe()
            if l1111111l1_Krypto_.l111llll111_Krypto_() == 0:
                l1111111l1_Krypto_.close(l111ll1l1ll_Krypto_)
                f = l1111111l1_Krypto_.fdopen(l111lllll11_Krypto_, l1l1111_Krypto_ (u"ࠧࡽࡢࠣᢶ"))
                l111ll1_Krypto_.l1ll1l11l1_Krypto_.l1lllllll11_Krypto_()
                data = l111ll1_Krypto_.l1ll1l11l1_Krypto_.l1111l11l1_Krypto_(16)
                f.write(data)
                f.close()
                l1111111l1_Krypto_._exit(0)
            l1111111l1_Krypto_.close(l111lllll11_Krypto_)
            l111ll1l1l1_Krypto_.append(l1111111l1_Krypto_.fdopen(l111ll1l1ll_Krypto_, l1l1111_Krypto_ (u"ࠨࡲࡣࠤᢷ")))
        results = []
        l111lll11ll_Krypto_ = {}
        for f in l111ll1l1l1_Krypto_:
            data = l11l111lll_Krypto_.hexlify(f.read())
            results.append(data)
            l111lll11ll_Krypto_[data] = 1
            f.close()
        if len(results) != len(list(l111lll11ll_Krypto_.keys())):
            raise AssertionError(l1l1111_Krypto_ (u"ࠢࡓࡐࡊࠤࡴࡻࡴࡱࡷࡷࠤࡩࡻࡰ࡭࡫ࡦࡥࡹ࡫ࡤࠡࡣࡦࡶࡴࡹࡳࠡࡨࡲࡶࡰ࠮ࠩ࠻࡞ࡱࠩࡸࠨᢸ") %
                                 (l111llll1ll_Krypto_.pformat(results)))
def _111ll1l11l_Krypto_(q):
    a = l111ll1_Krypto_.l1ll1l11l1_Krypto_.l1111l11l1_Krypto_(16)
    l11111l111_Krypto_.sleep(0.1)
    b = l111ll1_Krypto_.l1ll1l11l1_Krypto_.l1111l11l1_Krypto_(16)
    q.put(l11l111lll_Krypto_.b2a_hex(a))
    q.put(l11l111lll_Krypto_.b2a_hex(b))
    q.put(None)
class l111llllll1_Krypto_(l1lll111111_Krypto_.TestCase):
    def runTest(self):
        l111ll1lll1_Krypto_ = 5
        manager = l111lllll1l_Krypto_.Manager()
        l111lll1lll_Krypto_ = [manager.Queue(1) for i in range(l111ll1lll1_Krypto_)]
        l11111l111_Krypto_.sleep(0.15)
        l111ll1_Krypto_.l1ll1l11l1_Krypto_._1111lll11_Krypto_._1111l111l_Krypto_().l1111ll11l_Krypto_()
        l111ll1_Krypto_.l1ll1l11l1_Krypto_.l1111l11l1_Krypto_(1)
        l111ll1ll1l_Krypto_ = l111lllll1l_Krypto_.Pool(processes=l111ll1lll1_Krypto_, initializer=l111ll1_Krypto_.l1ll1l11l1_Krypto_.l1lllllll11_Krypto_)
        l111lll1ll1_Krypto_ = l111ll1ll1l_Krypto_.l111ll1ll11_Krypto_(_111ll1l11l_Krypto_, l111lll1lll_Krypto_)
        l111lll1l1l_Krypto_ = [l111lll1lll_Krypto_[i].get(30) for i in range(l111ll1lll1_Krypto_)]
        l111lll1111_Krypto_ = [l111lll1lll_Krypto_[i].get(30) for i in range(l111ll1lll1_Krypto_)]
        res = list(zip(l111lll1l1l_Krypto_, l111lll1111_Krypto_))
        l111lll1ll1_Krypto_.get(30)
        l111ll1ll1l_Krypto_.close()
        l111ll1ll1l_Krypto_.join()
        if len(set(l111lll1l1l_Krypto_)) != len(l111lll1l1l_Krypto_) or len(set(res)) != len(res):
            raise AssertionError(l1l1111_Krypto_ (u"ࠣࡔࡑࡋࠥࡵࡵࡵࡲࡸࡸࠥࡪࡵࡱ࡮࡬ࡧࡦࡺࡥࡥࠢࡤࡧࡷࡵࡳࡴࠢࡩࡳࡷࡱࠨࠪ࠼࡟ࡲࠪࡹࠢᢹ") %
                                 (l111llll1ll_Krypto_.pformat(res),))
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    tests = []
    tests += [l111llll1l1_Krypto_()]
    if l111lllll1l_Krypto_ is not None:
        tests += [l111llllll1_Krypto_()]
    return tests
if __name__ == l1l1111_Krypto_ (u"ࠩࡢࡣࡲࡧࡩ࡯ࡡࡢࠫᢺ"):
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"ࠪࡷࡺ࡯ࡴࡦࠩᢻ"))