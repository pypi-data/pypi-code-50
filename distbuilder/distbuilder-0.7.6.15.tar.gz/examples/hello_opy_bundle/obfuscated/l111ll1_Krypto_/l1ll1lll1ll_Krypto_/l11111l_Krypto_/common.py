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
l1l1111_Krypto_ (u"ࠤࠥࠦࡘ࡫࡬ࡧ࠯ࡷࡩࡸࡺࡩ࡯ࡩࠣࡪࡴࡸࠠࡑࡻࡆࡶࡾࡶࡴࡰࠢ࡫ࡥࡸ࡮ࠠ࡮ࡱࡧࡹࡱ࡫ࡳࠣࠤࠥ੻")
__revision__ = l1l1111_Krypto_ (u"ࠥࠨࡎࡪࠤࠣ੼")
import sys as l1l11l11_Krypto_
import unittest as l1lll111111_Krypto_
from binascii import a2b_hex as l1ll111llll_Krypto_,b2a_hex as l1llll1l1l1_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
if l1l11l11_Krypto_.hexversion < 0x02030000:
    def dict(**kwargs):
        return kwargs.copy()
else:
    dict = dict
class _1ll11llll1_Krypto_: pass
def _1ll1l11ll1_Krypto_(d, k, default=_1ll11llll1_Krypto_):
    l1l1111_Krypto_ (u"ࠦࠧࠨࡇࡦࡶࠣࡥࡳࠦࡩࡵࡧࡰࠤ࡫ࡸ࡯࡮ࠢࡤࠤࡩ࡯ࡣࡵ࡫ࡲࡲࡦࡸࡹ࠭ࠢࡤࡲࡩࠦࡲࡦ࡯ࡲࡺࡪࠦࡩࡵࠢࡩࡶࡴࡳࠠࡵࡪࡨࠤࡩ࡯ࡣࡵ࡫ࡲࡲࡦࡸࡹ࠯ࠤࠥࠦ੽")
    try:
        l111l111ll_Krypto_ = d[k]
    except KeyError:
        if default is _1ll11llll1_Krypto_:
            raise
        return default
    del d[k]
    return l111l111ll_Krypto_
class l1ll1l1111l_Krypto_(l1lll111111_Krypto_.TestCase):
    def __init__(self, module, params):
        l1lll111111_Krypto_.TestCase.__init__(self)
        self.module = module
        params = params.copy()
        self.description = _1ll1l11ll1_Krypto_(params, l1l1111_Krypto_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪ੾"))
        self.key = b(_1ll1l11ll1_Krypto_(params, l1l1111_Krypto_ (u"࠭࡫ࡦࡻࠪ੿")))
        self.l1ll11l1_Krypto_ = b(_1ll1l11ll1_Krypto_(params, l1l1111_Krypto_ (u"ࠧࡱ࡮ࡤ࡭ࡳࡺࡥࡹࡶࠪ઀")))
        self.l1ll111l_Krypto_ = b(_1ll1l11ll1_Krypto_(params, l1l1111_Krypto_ (u"ࠨࡥ࡬ࡴ࡭࡫ࡲࡵࡧࡻࡸࠬઁ")))
        self.module_name = _1ll1l11ll1_Krypto_(params, l1l1111_Krypto_ (u"ࠩࡰࡳࡩࡻ࡬ࡦࡡࡱࡥࡲ࡫ࠧં"), None)
        mode = _1ll1l11ll1_Krypto_(params, l1l1111_Krypto_ (u"ࠪࡱࡴࡪࡥࠨઃ"), None)
        self.l1ll1ll1lll_Krypto_ = str(mode)
        if mode is not None:
            self.mode = getattr(self.module, l1l1111_Krypto_ (u"ࠦࡒࡕࡄࡆࡡࠥ઄") + mode)
            self.l1ll1l1l111_Krypto_ = _1ll1l11ll1_Krypto_(params, l1l1111_Krypto_ (u"ࠬ࡯ࡶࠨઅ"), None)
            if self.l1ll1l1l111_Krypto_ is not None: self.l1ll1l1l111_Krypto_ = b(self.l1ll1l1l111_Krypto_)
            self.l1ll1ll1l1l_Krypto_ = _1ll1l11ll1_Krypto_(params, l1l1111_Krypto_ (u"࠭ࡥ࡯ࡥࡵࡽࡵࡺࡥࡥࡡ࡬ࡺࠬઆ"), None)
            if self.l1ll1ll1l1l_Krypto_ is not None:
                self.l1ll1ll1l1l_Krypto_ = b(self.l1ll1ll1l1l_Krypto_)
        else:
            self.mode = None
            self.l1ll1l1l111_Krypto_ = None
        self.l1ll11ll111_Krypto_ = params
    def shortDescription(self):
        return self.description
    def _1ll1l1l1l1_Krypto_(self, l1ll111l1ll_Krypto_=0):
        params = self.l1ll11ll111_Krypto_.copy()
        if hasattr(self.module, l1l1111_Krypto_ (u"ࠢࡎࡑࡇࡉࡤࡉࡔࡓࠤઇ")) and self.mode == self.module.l1llllll_Krypto_:
            from l111ll1_Krypto_.l1l111ll_Krypto_ import Counter
            l1ll11l11ll_Krypto_ = _1ll1l11ll1_Krypto_(params, l1l1111_Krypto_ (u"ࠨࡥࡷࡶࡤࡩ࡬ࡢࡵࡶࠫઈ"), Counter.new)
            l1ll111ll11_Krypto_ = _1ll1l11ll1_Krypto_(params, l1l1111_Krypto_ (u"ࠩࡦࡸࡷࡥࡰࡢࡴࡤࡱࡸ࠭ઉ"), {}).copy()
            if l1l1111_Krypto_ (u"ࠪࡴࡷ࡫ࡦࡪࡺࠪઊ") in l1ll111ll11_Krypto_: l1ll111ll11_Krypto_[l1l1111_Krypto_ (u"ࠫࡵࡸࡥࡧ࡫ࡻࠫઋ")] = l1ll111llll_Krypto_(b(l1ll111ll11_Krypto_[l1l1111_Krypto_ (u"ࠬࡶࡲࡦࡨ࡬ࡼࠬઌ")]))
            if l1l1111_Krypto_ (u"࠭ࡳࡶࡨࡩ࡭ࡽ࠭ઍ") in l1ll111ll11_Krypto_: l1ll111ll11_Krypto_[l1l1111_Krypto_ (u"ࠧࡴࡷࡩࡪ࡮ࡾࠧ઎")] = l1ll111llll_Krypto_(b(l1ll111ll11_Krypto_[l1l1111_Krypto_ (u"ࠨࡵࡸࡪ࡫࡯ࡸࠨએ")]))
            if l1l1111_Krypto_ (u"ࠩࡱࡦ࡮ࡺࡳࠨઐ") not in l1ll111ll11_Krypto_:
                l1ll111ll11_Krypto_[l1l1111_Krypto_ (u"ࠪࡲࡧ࡯ࡴࡴࠩઑ")] = 8*(self.module.block_size - len(l1ll111ll11_Krypto_.get(l1l1111_Krypto_ (u"ࠫࡵࡸࡥࡧ࡫ࡻࠫ઒"), l1l1111_Krypto_ (u"ࠬ࠭ઓ"))) - len(l1ll111ll11_Krypto_.get(l1l1111_Krypto_ (u"࠭ࡳࡶࡨࡩ࡭ࡽ࠭ઔ"), l1l1111_Krypto_ (u"ࠧࠨક"))))
            params[l1l1111_Krypto_ (u"ࠨࡥࡲࡹࡳࡺࡥࡳࠩખ")] = l1ll11l11ll_Krypto_(**l1ll111ll11_Krypto_)
        if self.mode is None:
            return self.module.new(l1ll111llll_Krypto_(self.key), **params)
        elif self.l1ll1l1l111_Krypto_ is None:
            return self.module.new(l1ll111llll_Krypto_(self.key), self.mode, **params)
        else:
            if l1ll111l1ll_Krypto_ and self.mode == self.module.l1111l1_Krypto_:
                return self.module.new(l1ll111llll_Krypto_(self.key), self.mode, l1ll111llll_Krypto_(self.l1ll1ll1l1l_Krypto_), **params)
            else:
                return self.module.new(l1ll111llll_Krypto_(self.key), self.mode, l1ll111llll_Krypto_(self.l1ll1l1l111_Krypto_), **params)
    def runTest(self):
        l1ll11l1_Krypto_ = l1ll111llll_Krypto_(self.l1ll11l1_Krypto_)
        l1ll111l_Krypto_ = l1ll111llll_Krypto_(self.l1ll111l_Krypto_)
        l1ll111l11l_Krypto_ = l1llll1l1l1_Krypto_(self._1ll1l1l1l1_Krypto_().l1_Krypto_(l1ll11l1_Krypto_))
        l1ll11ll1l1_Krypto_ = l1llll1l1l1_Krypto_(self._1ll1l1l1l1_Krypto_(1).l1lllll_Krypto_(l1ll111l_Krypto_))
        l1ll1l11l11_Krypto_ = l1llll1l1l1_Krypto_(self._1ll1l1l1l1_Krypto_().l1_Krypto_(l1ll11l1_Krypto_))
        l1ll11lll11_Krypto_ = l1llll1l1l1_Krypto_(self._1ll1l1l1l1_Krypto_(1).l1lllll_Krypto_(l1ll111l_Krypto_))
        if hasattr(self.module, l1l1111_Krypto_ (u"ࠤࡐࡓࡉࡋ࡟ࡐࡒࡈࡒࡕࡍࡐࠣગ")) and self.mode == self.module.l1111l1_Krypto_:
            l1ll111lll1_Krypto_ = len(self.l1ll1ll1l1l_Krypto_)
            self.assertEqual(self.l1ll1ll1l1l_Krypto_, l1ll111l11l_Krypto_[:l1ll111lll1_Krypto_])
            self.assertEqual(self.l1ll1ll1l1l_Krypto_, l1ll1l11l11_Krypto_[:l1ll111lll1_Krypto_])
            l1ll111l11l_Krypto_ = l1ll111l11l_Krypto_[l1ll111lll1_Krypto_:]
            l1ll1l11l11_Krypto_ = l1ll1l11l11_Krypto_[l1ll111lll1_Krypto_:]
        self.assertEqual(self.l1ll111l_Krypto_, l1ll111l11l_Krypto_)
        self.assertEqual(self.l1ll111l_Krypto_, l1ll1l11l11_Krypto_)
        self.assertEqual(self.l1ll11l1_Krypto_, l1ll11ll1l1_Krypto_)
        self.assertEqual(self.l1ll11l1_Krypto_, l1ll11lll11_Krypto_)
class l1ll11l11l1_Krypto_(l1ll1l1111l_Krypto_):
    def shortDescription(self):
        l1ll11ll11l_Krypto_ = self.module_name
        if self.mode is not None:
            l1ll11ll11l_Krypto_ += l1l1111_Krypto_ (u"ࠥࠤ࡮ࡴࠠࠦࡵࠣࡱࡴࡪࡥࠣઘ") % (self.l1ll1ll1lll_Krypto_,)
        return l1l1111_Krypto_ (u"ࠦࠪࡹࠠࡴࡪࡲࡹࡱࡪࠠࡣࡧ࡫ࡥࡻ࡫ࠠ࡭࡫࡮ࡩࠥࡧࠠࡴࡶࡵࡩࡦࡳࠠࡤ࡫ࡳ࡬ࡪࡸࠢઙ") % (l1ll11ll11l_Krypto_,)
    def runTest(self):
        l1ll11l1_Krypto_ = l1ll111llll_Krypto_(self.l1ll11l1_Krypto_)
        l1ll111l_Krypto_ = l1ll111llll_Krypto_(self.l1ll111l_Krypto_)
        l1ll1l11l1l_Krypto_ = []
        l1llll11l_Krypto_ = self._1ll1l1l1l1_Krypto_()
        for i in range(0, len(l1ll11l1_Krypto_), 3):
            l1ll1l11l1l_Krypto_.append(l1llll11l_Krypto_.l1_Krypto_(l1ll11l1_Krypto_[i:i+3]))
        l1ll1l11l1l_Krypto_ = l1llll1l1l1_Krypto_(b(l1l1111_Krypto_ (u"ࠧࠨચ")).join(l1ll1l11l1l_Krypto_))
        self.assertEqual(self.l1ll111l_Krypto_, l1ll1l11l1l_Krypto_)
        l1ll1l111ll_Krypto_ = []
        l1llll11l_Krypto_ = self._1ll1l1l1l1_Krypto_()
        for i in range(0, len(l1ll111l_Krypto_), 3):
            l1ll1l111ll_Krypto_.append(l1llll11l_Krypto_.l1_Krypto_(l1ll111l_Krypto_[i:i+3]))
        l1ll1l111ll_Krypto_ = l1llll1l1l1_Krypto_(b(l1l1111_Krypto_ (u"ࠨࠢછ")).join(l1ll1l111ll_Krypto_))
        self.assertEqual(self.l1ll11l1_Krypto_, l1ll1l111ll_Krypto_)
class l1ll11l1111_Krypto_(l1lll111111_Krypto_.TestCase):
    def __init__(self, module, params):
        l1lll111111_Krypto_.TestCase.__init__(self)
        self.module = module
        self.key = b(params[l1l1111_Krypto_ (u"ࠧ࡬ࡧࡼࠫજ")])
        self.module_name = params.get(l1l1111_Krypto_ (u"ࠨ࡯ࡲࡨࡺࡲࡥࡠࡰࡤࡱࡪ࠭ઝ"), None)
    def shortDescription(self):
        return l1l1111_Krypto_ (u"ࠤࠥࠦࡗ࡫ࡧࡳࡧࡶࡷ࡮ࡵ࡮ࠡࡶࡨࡷࡹࡀࠠࠦࡵ࠱ࡲࡪࡽࠨ࡬ࡧࡼ࠰ࠥࠫࡳ࠯ࡏࡒࡈࡊࡥࡃࡕࡔࠬࠤࡸ࡮࡯ࡶ࡮ࡧࠤࡷࡧࡩࡴࡧࠣࡘࡾࡶࡥࡆࡴࡵࡳࡷ࠲ࠠ࡯ࡱࡷࠤࡸ࡫ࡧࡧࡣࡸࡰࡹࠨࠢࠣઞ") % (self.module_name, self.module_name)
    def runTest(self):
        self.assertRaises(TypeError, self.module.new, l1ll111llll_Krypto_(self.key), self.module.l1llllll_Krypto_)
class l1ll1l1ll11_Krypto_(l1lll111111_Krypto_.TestCase):
    def __init__(self, module, params):
        l1lll111111_Krypto_.TestCase.__init__(self)
        self.module = module
        self.key = b(params[l1l1111_Krypto_ (u"ࠪ࡯ࡪࡿࠧટ")])
        self.module_name = params.get(l1l1111_Krypto_ (u"ࠫࡲࡵࡤࡶ࡮ࡨࡣࡳࡧ࡭ࡦࠩઠ"), None)
    def shortDescription(self):
        return l1l1111_Krypto_ (u"ࠧࠨࠢࡓࡧࡪࡶࡪࡹࡳࡪࡱࡱࠤࡹ࡫ࡳࡵ࠼ࠣࠩࡸࠦࡷࡪࡶ࡫ࠤࡒࡕࡄࡆࡡࡆࡘࡗࠦࡳࡩࡱࡸࡰࡩࠦࡲࡢ࡫ࡶࡩࠥࡕࡶࡦࡴࡩࡰࡴࡽࡅࡳࡴࡲࡶࠥࡵ࡮ࠡࡹࡵࡥࡵࡧࡲࡰࡷࡱࡨࠥࡽࡨࡦࡰࠣࡷ࡭ࡵࡲࡵࡥࡸࡸࠥࡻࡳࡦࡦࠥࠦࠧડ") % (self.module_name,)
    def runTest(self):
        from l111ll1_Krypto_.l1l111ll_Krypto_ import Counter
        for l1ll1l1lll1_Krypto_ in (0, 1):
            for l1lll1ll111_Krypto_ in (0, 1):
                l1ll1l1l11l_Krypto_ = Counter.new(8*self.module.block_size, l1llll11111_Krypto_=2**(8*self.module.block_size)-1, l1lll1ll111_Krypto_=l1lll1ll111_Krypto_, l1ll1l1lll1_Krypto_=l1ll1l1lll1_Krypto_)
                l1llll11l_Krypto_ = self.module.new(l1ll111llll_Krypto_(self.key), self.module.l1llllll_Krypto_, l1lll1llll1_Krypto_=l1ll1l1l11l_Krypto_)
                block = b(l1l1111_Krypto_ (u"ࠨ࡜ࡹ࠲࠳ࠦઢ")) * self.module.block_size
                l1llll11l_Krypto_.l1_Krypto_(block)
                self.assertRaises(OverflowError, l1llll11l_Krypto_.l1_Krypto_, block)
class l1ll1ll111l_Krypto_(l1lll111111_Krypto_.TestCase):
    def __init__(self, module, params):
        l1lll111111_Krypto_.TestCase.__init__(self)
        self.module = module
        self.key = b(params[l1l1111_Krypto_ (u"ࠧ࡬ࡧࡼࠫણ")])
        self.description = params[l1l1111_Krypto_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭ત")]
    def shortDescription(self):
        return self.description
    def runTest(self):
        l1l1111_Krypto_ (u"ࠤࠥࠦࡗ࡫ࡧࡳࡧࡶࡷ࡮ࡵ࡮ࠡࡶࡨࡷࡹࡀࠠ࡮࠰ࡱࡩࡼ࠮࡫ࡦࡻ࠯ࠤࡲ࠴ࡍࡐࡆࡈࡣࡈࡌࡂ࠭ࠢࡶࡩ࡬ࡳࡥ࡯ࡶࡢࡷ࡮ࢀࡥ࠾ࡐࠬࠤࡸ࡮࡯ࡶ࡮ࡧࠤࡷ࡫ࡱࡶ࡫ࡵࡩࠥࡹࡥࡨ࡯ࡨࡲࡹࡥࡳࡪࡼࡨࠤࡹࡵࠠࡣࡧࠣࡥࠥࡳࡵ࡭ࡶ࡬ࡴࡱ࡫ࠠࡰࡨࠣ࠼ࠥࡨࡩࡵࡵࠥࠦࠧથ")
        for i in range(1, 8):
            self.assertRaises(ValueError, self.module.new, l1ll111llll_Krypto_(self.key), self.module.l1lll11l_Krypto_, l1l1llll_Krypto_=i)
        self.module.new(l1ll111llll_Krypto_(self.key), self.module.l1lll11l_Krypto_, l1l1111_Krypto_ (u"ࠥࡠ࠵ࠨદ")*self.module.block_size, l1l1llll_Krypto_=8)
class l1ll1ll1111_Krypto_(l1lll111111_Krypto_.TestCase):
    def __init__(self, module, params):
        from l111ll1_Krypto_ import l1ll1l11l1_Krypto_
        l1lll111111_Krypto_.TestCase.__init__(self)
        self.module = module
        self.l1ll1l1l111_Krypto_ = l1ll1l11l1_Krypto_.l1111l11l1_Krypto_(module.block_size)
        self.key = b(params[l1l1111_Krypto_ (u"ࠫࡰ࡫ࡹࠨધ")])
        self.l1ll11l1_Krypto_ = 100 * b(params[l1l1111_Krypto_ (u"ࠬࡶ࡬ࡢ࡫ࡱࡸࡪࡾࡴࠨન")])
        self.module_name = params.get(l1l1111_Krypto_ (u"࠭࡭ࡰࡦࡸࡰࡪࡥ࡮ࡢ࡯ࡨࠫ઩"), None)
    def shortDescription(self):
        return l1l1111_Krypto_ (u"ࠢࠣࠤࠨࡷࠥ࠴ࡤࡦࡥࡵࡽࡵࡺࠨࠪࠢࡲࡹࡹࡶࡵࡵࠢࡲࡪࠥ࠴ࡥ࡯ࡥࡵࡽࡵࡺࠨࠪࠢࡶ࡬ࡴࡻ࡬ࡥࠢࡱࡳࡹࠦࡢࡦࠢࡪࡥࡷࡨ࡬ࡦࡦࠥࠦࠧપ") % (self.module_name,)
    def runTest(self):
        for mode in (self.module.l1lll1ll_Krypto_, self.module.l1lllll1_Krypto_, self.module.l1lll11l_Krypto_, self.module.l1111ll_Krypto_, self.module.l1111l1_Krypto_):
            l1ll11lll1l_Krypto_ = self.module.new(l1ll111llll_Krypto_(self.key), mode, self.l1ll1l1l111_Krypto_)
            l1ll111l_Krypto_ = l1ll11lll1l_Krypto_.l1_Krypto_(self.l1ll11l1_Krypto_)
            if mode != self.module.l1111l1_Krypto_:
                l1ll11ll1ll_Krypto_ = self.module.new(l1ll111llll_Krypto_(self.key), mode, self.l1ll1l1l111_Krypto_)
            else:
                l1ll111ll1l_Krypto_ = l1ll111l_Krypto_[:self.module.block_size+2]
                l1ll111l_Krypto_ = l1ll111l_Krypto_[self.module.block_size+2:]
                l1ll11ll1ll_Krypto_ = self.module.new(l1ll111llll_Krypto_(self.key), mode, l1ll111ll1l_Krypto_)
            l1ll1l1ll1l_Krypto_ = l1ll11ll1ll_Krypto_.l1lllll_Krypto_(l1ll111l_Krypto_)
            self.assertEqual(self.l1ll11l1_Krypto_, l1ll1l1ll1l_Krypto_)
class l1ll1ll1ll1_Krypto_(l1lll111111_Krypto_.TestCase):
    def __init__(self, module, params):
        l1lll111111_Krypto_.TestCase.__init__(self)
        self.module = module
        self.key = b(params[l1l1111_Krypto_ (u"ࠨ࡭ࡨࡽࠬફ")])
    def shortDescription(self):
        return l1l1111_Krypto_ (u"ࠤࡐࡓࡉࡋ࡟ࡑࡉࡓࠤࡼࡧࡳࠡ࡫ࡰࡴࡱ࡫࡭ࡦࡰࡷࡩࡩࠦࡩ࡯ࡥࡲࡶࡷ࡫ࡣࡵ࡮ࡼࠤࡦࡴࡤࠡ࡫ࡱࡷࡪࡩࡵࡳࡧ࡯ࡽ࠳ࠦࡉࡵࠩࡶࠤࡨࡵ࡭ࡱ࡮ࡨࡸࡪࡲࡹࠡࡤࡤࡲ࡮ࡹࡨࡦࡦࠣࡲࡴࡽ࠮ࠣબ")
    def runTest(self):
        self.assertRaises(ValueError, self.module.new, l1ll111llll_Krypto_(self.key),
                self.module.l1llll11_Krypto_)
class l1ll1ll1l11_Krypto_(l1lll111111_Krypto_.TestCase):
    def __init__(self, module, params):
        l1lll111111_Krypto_.TestCase.__init__(self)
        self.module = module
        self.key = b(params[l1l1111_Krypto_ (u"ࠪ࡯ࡪࡿࠧભ")])
    def shortDescription(self):
        return l1l1111_Krypto_ (u"ࠦࡈ࡮ࡥࡤ࡭ࠣࡸ࡭ࡧࡴࠡࡣ࡯ࡰࠥࡳ࡯ࡥࡧࡶࠤࡪࡾࡣࡦࡲࡷࠤࡒࡕࡄࡆࡡࡈࡇࡇࠦࡡ࡯ࡦࠣࡑࡔࡊࡅࡠࡅࡗࡖࠥࡸࡥࡲࡷ࡬ࡶࡪࠦࡡ࡯ࠢࡌ࡚ࠥࡵࡦࠡࡶ࡫ࡩࠥࡶࡲࡰࡲࡨࡶࠥࡲࡥ࡯ࡩࡷ࡬ࠧમ")
    def runTest(self):
        self.assertRaises(ValueError, self.module.new, l1ll111llll_Krypto_(self.key),
                self.module.l1lllll1_Krypto_, l1l1111_Krypto_ (u"ࠧࠨય"))
        self.assertRaises(ValueError, self.module.new, l1ll111llll_Krypto_(self.key),
                self.module.l1lll11l_Krypto_, l1l1111_Krypto_ (u"ࠨࠢર"))
        self.assertRaises(ValueError, self.module.new, l1ll111llll_Krypto_(self.key),
                self.module.l1111ll_Krypto_, l1l1111_Krypto_ (u"ࠢࠣ઱"))
        self.assertRaises(ValueError, self.module.new, l1ll111llll_Krypto_(self.key),
                self.module.l1111l1_Krypto_, l1l1111_Krypto_ (u"ࠣࠤલ"))
        self.module.new(l1ll111llll_Krypto_(self.key), self.module.l1lll1ll_Krypto_, l1l1111_Krypto_ (u"ࠤࠥળ"))
        self.module.new(l1ll111llll_Krypto_(self.key), self.module.l1llllll_Krypto_, l1l1111_Krypto_ (u"ࠥࠦ઴"), l1lll1llll1_Krypto_=self._1ll11l1l11_Krypto_)
    def _1ll11l1l11_Krypto_(self):
        return l1l1111_Krypto_ (u"ࠦࡡ࠶ࠢવ") * self.module.block_size
def l1ll1ll11l1_Krypto_(module, module_name, l1ll11lllll_Krypto_):
    tests = []
    l1ll111l1l1_Krypto_ = 0
    for i in range(len(l1ll11lllll_Krypto_)):
        row = l1ll11lllll_Krypto_[i]
        params = {l1l1111_Krypto_ (u"ࠬࡳ࡯ࡥࡧࠪશ"): l1l1111_Krypto_ (u"࠭ࡅࡄࡄࠪષ")}
        if len(row) == 3:
            (params[l1l1111_Krypto_ (u"ࠧࡱ࡮ࡤ࡭ࡳࡺࡥࡹࡶࠪસ")], params[l1l1111_Krypto_ (u"ࠨࡥ࡬ࡴ࡭࡫ࡲࡵࡧࡻࡸࠬહ")], params[l1l1111_Krypto_ (u"ࠩ࡮ࡩࡾ࠭઺")]) = row
        elif len(row) == 4:
            (params[l1l1111_Krypto_ (u"ࠪࡴࡱࡧࡩ࡯ࡶࡨࡼࡹ࠭઻")], params[l1l1111_Krypto_ (u"ࠫࡨ࡯ࡰࡩࡧࡵࡸࡪࡾࡴࠨ઼")], params[l1l1111_Krypto_ (u"ࠬࡱࡥࡺࠩઽ")], params[l1l1111_Krypto_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫા")]) = row
        elif len(row) == 5:
            (params[l1l1111_Krypto_ (u"ࠧࡱ࡮ࡤ࡭ࡳࡺࡥࡹࡶࠪિ")], params[l1l1111_Krypto_ (u"ࠨࡥ࡬ࡴ࡭࡫ࡲࡵࡧࡻࡸࠬી")], params[l1l1111_Krypto_ (u"ࠩ࡮ࡩࡾ࠭ુ")], params[l1l1111_Krypto_ (u"ࠪࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨૂ")], l1ll11ll111_Krypto_) = row
            params.update(l1ll11ll111_Krypto_)
        else:
            raise AssertionError(l1l1111_Krypto_ (u"࡚ࠦࡴࡳࡶࡲࡳࡳࡷࡺࡥࡥࠢࡷࡹࡵࡲࡥࠡࡵ࡬ࡾࡪࠦࠥࡥࠤૃ") % (len(row),))
        l1ll1l1llll_Krypto_ = params.copy()
        l1ll11l1l1l_Krypto_ = _1ll1l11ll1_Krypto_(l1ll1l1llll_Krypto_, l1l1111_Krypto_ (u"ࠬࡱࡥࡺࠩૄ"))
        l1ll1l11lll_Krypto_ = _1ll1l11ll1_Krypto_(l1ll1l1llll_Krypto_, l1l1111_Krypto_ (u"࠭ࡰ࡭ࡣ࡬ࡲࡹ࡫ࡸࡵࠩૅ"))
        l1ll11l1ll1_Krypto_ = _1ll1l11ll1_Krypto_(l1ll1l1llll_Krypto_, l1l1111_Krypto_ (u"ࠧࡤ࡫ࡳ࡬ࡪࡸࡴࡦࡺࡷࠫ૆"))
        l1ll1l111l1_Krypto_ = _1ll1l11ll1_Krypto_(l1ll1l1llll_Krypto_, l1l1111_Krypto_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭ે"), None)
        l1ll11l111l_Krypto_ = l1ll1l1llll_Krypto_.get(l1l1111_Krypto_ (u"ࠩࡰࡳࡩ࡫ࠧૈ"), l1l1111_Krypto_ (u"ࠪࡉࡈࡈࠧૉ"))
        if l1ll11l111l_Krypto_ == l1l1111_Krypto_ (u"ࠫࡊࡉࡂࠨ૊"):
            _1ll1l11ll1_Krypto_(l1ll1l1llll_Krypto_, l1l1111_Krypto_ (u"ࠬࡳ࡯ࡥࡧࠪો"), l1l1111_Krypto_ (u"࠭ࡅࡄࡄࠪૌ"))
        if l1ll1l111l1_Krypto_ is not None:
            description = l1ll1l111l1_Krypto_
        elif l1ll11l111l_Krypto_ == l1l1111_Krypto_ (u"ࠧࡆࡅࡅ્ࠫ") and not l1ll1l1llll_Krypto_:
            description = l1l1111_Krypto_ (u"ࠣࡲࡀࠩࡸ࠲ࠠ࡬࠿ࠨࡷࠧ૎") % (l1ll1l11lll_Krypto_, l1ll11l1l1l_Krypto_)
        else:
            description = l1l1111_Krypto_ (u"ࠤࡳࡁࠪࡹࠬࠡ࡭ࡀࠩࡸ࠲ࠠࠦࡴࠥ૏") % (l1ll1l11lll_Krypto_, l1ll11l1l1l_Krypto_, l1ll1l1llll_Krypto_)
        name = l1l1111_Krypto_ (u"ࠥࠩࡸࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࡲࡤࡶࡦࡳࡳ࡜ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧ࡞ࠢࡀࠤࡳࡧ࡭ࡦࠌࠣࠤࠥࠦࠠࠡࠢࠣࡴࡦࡸࡡ࡮ࡵ࡞ࠫࡲࡵࡤࡶ࡮ࡨࡣࡳࡧ࡭ࡦࠩࡠࠤࡂࠦ࡭ࡰࡦࡸࡰࡪࡥ࡮ࡢ࡯ࡨࠎࠏࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡫ࡩࠤࡳࡵࡴࠡࡧࡻࡸࡷࡧ࡟ࡵࡧࡶࡸࡸࡥࡡࡥࡦࡨࡨ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡹ࡫ࡳࡵࡵࠣ࠯ࡂ࡛ࠦࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡇ࡙ࡘࡓࡦࡩࡩࡥࡺࡲࡴࡕࡧࡶࡸ࠭ࡳ࡯ࡥࡷ࡯ࡩ࠱ࠦࡰࡢࡴࡤࡱࡸ࠯ࠬࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡇ࡙ࡘࡗࡳࡣࡳࡥࡷࡵࡵ࡯ࡦࡗࡩࡸࡺࠨ࡮ࡱࡧࡹࡱ࡫ࠬࠡࡲࡤࡶࡦࡳࡳࠪ࠮ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡉࡆࡃࡕࡨ࡫ࡲ࡫࡮ࡵࡕ࡬ࡾࡪ࡚ࡥࡴࡶࠫࡱࡴࡪࡵ࡭ࡧ࠯ࠤࡵࡧࡲࡢ࡯ࡶ࠭࠱ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡔࡲࡹࡳࡪࡴࡳ࡫ࡳࡘࡪࡹࡴࠩ࡯ࡲࡨࡺࡲࡥ࠭ࠢࡳࡥࡷࡧ࡭ࡴࠫ࠯ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡐࡈࡒࡗࡩࡸࡺࠨ࡮ࡱࡧࡹࡱ࡫ࠬࠡࡲࡤࡶࡦࡳࡳࠪ࠮ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡏࡖࡍࡧࡱ࡫ࡹ࡮ࡔࡦࡵࡷࠬࡲࡵࡤࡶ࡮ࡨ࠰ࠥࡶࡡࡳࡣࡰࡷ࠮࠲ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡣࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡫ࡸࡵࡴࡤࡣࡹ࡫ࡳࡵࡵࡢࡥࡩࡪࡥࡥࠢࡀࠤ࠶ࠐࠊࠡࠢࠣࠤࠥࠦࠠࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࡸࡪࡹࡴࡴ࠰ࡤࡴࡵ࡫࡮ࡥࠪࡆ࡭ࡵ࡮ࡥࡳࡕࡨࡰ࡫࡚ࡥࡴࡶࠫࡱࡴࡪࡵ࡭ࡧ࠯ࠤࡵࡧࡲࡢ࡯ࡶ࠭࠮ࠐࠊࠡࠢࠣࠤࠥࠦࠠࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣ࡭࡫ࠦࡰࡠ࡯ࡲࡨࡪࠦ࠽࠾ࠢࠪࡇ࡙ࡘࠧ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡵࡧࡶࡸࡸ࠴ࡡࡱࡲࡨࡲࡩ࠮ࡃࡪࡲ࡫ࡩࡷ࡙ࡴࡳࡧࡤࡱ࡮ࡴࡧࡔࡧ࡯ࡪ࡙࡫ࡳࡵࠪࡰࡳࡩࡻ࡬ࡦ࠮ࠣࡴࡦࡸࡡ࡮ࡵࠬ࠭ࠏࠐࠠࠡࠢࠣࠤࠥࠦࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢ࡬ࡪࠥࡶ࡟࡮ࡱࡧࡩࠥࡃ࠽ࠡࠩࡆࡘࡗ࠭ࠠࡢࡰࡧࠤࠬࡩࡴࡳࡡࡦࡰࡦࡹࡳࠨࠢࡱࡳࡹࠦࡩ࡯ࠢࡳࡥࡷࡧ࡭ࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡲࡤࡶࡦࡳࡳ࠳ࠢࡀࠤࡵࡧࡲࡢ࡯ࡶ࠲ࡨࡵࡰࡺࠪࠬࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡳࡥࡷࡧ࡭ࡴ࠴࡞ࠫࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩࡠࠤ࠰ࡃࠠࠣૐ") (l1ll11l1lll_Krypto_ disabled)l1l1111_Krypto_ (u"ࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡧࡹࡸ࡟ࡱࡣࡵࡥࡲࡹ࠲ࠡ࠿ࠣࡴࡦࡸࡡ࡮ࡵ࠱࡫ࡪࡺࠨࠨࡥࡷࡶࡤࡶࡡࡳࡣࡰࡷࠬ࠲ࠠࡼࡿࠬ࠲ࡨࡵࡰࡺࠪࠬࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡳࡥࡷࡧ࡭ࡴ࠴࡞ࠫࡨࡺࡲࡠࡲࡤࡶࡦࡳࡳࠨ࡟ࠣࡁࠥࡩࡴࡳࡡࡳࡥࡷࡧ࡭ࡴ࠴ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࡫ࡩࠤࠬࡪࡩࡴࡣࡥࡰࡪࡥࡳࡩࡱࡵࡸࡨࡻࡴࠨࠢࡱࡳࡹࠦࡩ࡯ࠢࡳࡥࡷࡧ࡭ࡴ࠴࡞ࠫࡨࡺࡲࡠࡲࡤࡶࡦࡳࡳࠨ࡟࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡰࡢࡴࡤࡱࡸ࠸࡛ࠨࡥࡷࡶࡤࡶࡡࡳࡣࡰࡷࠬࡣ࡛ࠨࡦ࡬ࡷࡦࡨ࡬ࡦࡡࡶ࡬ࡴࡸࡴࡤࡷࡷࠫࡢࠦ࠽ࠡ࠳ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡶࡨࡷࡹࡹ࠮ࡢࡲࡳࡩࡳࡪࠨࡄ࡫ࡳ࡬ࡪࡸࡓࡦ࡮ࡩࡘࡪࡹࡴࠩ࡯ࡲࡨࡺࡲࡥ࠭ࠢࡳࡥࡷࡧ࡭ࡴ࠴ࠬ࠭ࠏࠦࠠࠡࠢࡵࡩࡹࡻࡲ࡯ࠢࡷࡩࡸࡺࡳࠋࠌࡧࡩ࡫ࠦ࡭ࡢ࡭ࡨࡣࡸࡺࡲࡦࡣࡰࡣࡹ࡫ࡳࡵࡵࠫࡱࡴࡪࡵ࡭ࡧ࠯ࠤࡲࡵࡤࡶ࡮ࡨࡣࡳࡧ࡭ࡦ࠮ࠣࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠯࠺ࠋࠢࠣࠤࠥࡺࡥࡴࡶࡶࠤࡂ࡛ࠦ࡞ࠌࠣࠤࠥࠦࡦࡰࡴࠣ࡭ࠥ࡯࡮ࠡࡴࡤࡲ࡬࡫ࠨ࡭ࡧࡱࠬࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠩࠪ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡷࡵࡷࠡ࠿ࠣࡸࡪࡹࡴࡠࡦࡤࡸࡦࡡࡩ࡞ࠌࠍࠤࠥࠦࠠࠡࠢࠣࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦࡰࡢࡴࡤࡱࡸࠦ࠽ࠡࡽࢀࠎࠥࠦࠠࠡࠢࠣࠤࠥ࡯ࡦࠡ࡮ࡨࡲ࠭ࡸ࡯ࡸࠫࠣࡁࡂࠦ࠳࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠩࡲࡤࡶࡦࡳࡳ࡜ࠩࡳࡰࡦ࡯࡮ࡵࡧࡻࡸࠬࡣࠬࠡࡲࡤࡶࡦࡳࡳ࡜ࠩࡦ࡭ࡵ࡮ࡥࡳࡶࡨࡼࡹ࠭࡝࠭ࠢࡳࡥࡷࡧ࡭ࡴ࡝ࠪ࡯ࡪࡿࠧ࡞ࠫࠣࡁࠥࡸ࡯ࡸࠌࠣࠤࠥࠦࠠࠡࠢࠣࡩࡱ࡯ࡦࠡ࡮ࡨࡲ࠭ࡸ࡯ࡸࠫࠣࡁࡂࠦ࠴࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠩࡲࡤࡶࡦࡳࡳ࡜ࠩࡳࡰࡦ࡯࡮ࡵࡧࡻࡸࠬࡣࠬࠡࡲࡤࡶࡦࡳࡳ࡜ࠩࡦ࡭ࡵ࡮ࡥࡳࡶࡨࡼࡹ࠭࡝࠭ࠢࡳࡥࡷࡧ࡭ࡴ࡝ࠪ࡯ࡪࡿࠧ࡞࠮ࠣࡴࡦࡸࡡ࡮ࡵ࡞ࠫࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩࡠ࠭ࠥࡃࠠࡳࡱࡺࠎࠥࠦࠠࠡࠢࠣࠤࠥ࡫࡬ࡪࡨࠣࡰࡪࡴࠨࡳࡱࡺ࠭ࠥࡃ࠽ࠡ࠷࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠫࡴࡦࡸࡡ࡮ࡵ࡞ࠫࡵࡲࡡࡪࡰࡷࡩࡽࡺࠧ࡞࠮ࠣࡴࡦࡸࡡ࡮ࡵ࡞ࠫࡨ࡯ࡰࡩࡧࡵࡸࡪࡾࡴࠨ࡟࠯ࠤࡵࡧࡲࡢ࡯ࡶ࡟ࠬࡱࡥࡺࠩࡠ࠰ࠥࡶࡡࡳࡣࡰࡷࡠ࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫࡢ࠲ࠠࡦࡺࡷࡶࡦࡥࡰࡢࡴࡤࡱࡸ࠯ࠠ࠾ࠢࡵࡳࡼࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡵࡧࡲࡢ࡯ࡶ࠲ࡺࡶࡤࡢࡶࡨࠬࡪࡾࡴࡳࡣࡢࡴࡦࡸࡡ࡮ࡵࠬࠎࠥࠦࠠࠡࠢࠣࠤࠥ࡫࡬ࡴࡧ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡵࡥ࡮ࡹࡥࠡࡃࡶࡷࡪࡸࡴࡪࡱࡱࡉࡷࡸ࡯ࡳࠪࠥ૑")l1ll1ll11ll_Krypto_ tuple size %l1ll1l11111_Krypto_ (u"ࠧࠦࠥࠡࠪ࡯ࡩࡳ࠮ࡲࡰࡹࠬ࠰࠮࠯ࠊࠋࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤࡵ࠸ࠠ࠾ࠢࡳࡥࡷࡧ࡭ࡴ࠰ࡦࡳࡵࡿࠨࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࡴࡤࡱࡥࡺࠢࡀࠤࡤ࡫ࡸࡵࡴࡤࡧࡹ࠮ࡰ࠳࠮ࠣࠫࡰ࡫ࡹࠨࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࡵࡥࡰ࡭ࡣ࡬ࡲࡹ࡫ࡸࡵࠢࡀࠤࡤ࡫ࡸࡵࡴࡤࡧࡹ࠮ࡰ࠳࠮ࠣࠫࡵࡲࡡࡪࡰࡷࡩࡽࡺࠧࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࡴࡤࡩࡩࡱࡪࡨࡶࡹ࡫ࡸࡵࠢࡀࠤࡤ࡫ࡸࡵࡴࡤࡧࡹ࠮ࡰ࠳࠮ࠣࠫࡨ࡯ࡰࡩࡧࡵࡸࡪࡾࡴࠨࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࡵࡥࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠤࡂࠦ࡟ࡦࡺࡷࡶࡦࡩࡴࠩࡲ࠵࠰ࠥ࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫ࠱ࠦࡎࡰࡰࡨ࠭ࠏࠐࠠࠡࠢࠣࠤࠥࠦࠠࡪࡨࠣࡴࡤࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠣ࡭ࡸࠦ࡮ࡰࡶࠣࡒࡴࡴࡥ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠥࡃࠠࡱࡡࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠊࠡࠢࠣࠤࠥࠦࠠࠡࡧ࡯࡭࡫ࠦ࡮ࡰࡶࠣࡴ࠷ࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠣࡁࠥࠨ૒")p=%s, k=%l1ll1l1l1ll_Krypto_ (u"ࠨࠠࠦࠢࠫࡴࡤࡶ࡬ࡢ࡫ࡱࡸࡪࡾࡴ࠭ࠢࡳࡣࡰ࡫ࡹࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࡩࡱࡹࡥ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠥࡃࠠࠣ૓")p=%s, k=%s, %l1l1111_Krypto_ (u"ࡲࠣࠢࠨࠤ࠭ࡶ࡟ࡱ࡮ࡤ࡭ࡳࡺࡥࡹࡶ࠯ࠤࡵࡥ࡫ࡦࡻ࠯ࠤࡵ࠸ࠩࠋࠢࠣࠤࠥࠦࠠࠡࠢࡱࡥࡲ࡫ࠠ࠾ࠢࠥ૔")%s
        params[l1l1111_Krypto_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭૕")] = name
        params[l1l1111_Krypto_ (u"ࠩࡰࡳࡩࡻ࡬ࡦࡡࡱࡥࡲ࡫ࠧ૖")] = module_name
        tests.append(l1ll1l1111l_Krypto_(module, params))
        tests.append(l1ll11l11l1_Krypto_(module, params))
    return tests