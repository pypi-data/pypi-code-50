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
l1l1111_Krypto_ (u"ࠦࠧࠨࡓࡦ࡮ࡩ࠱ࡹ࡫ࡳࡵࠢࡶࡹ࡮ࡺࡥࠡࡨࡲࡶࠥࡉࡲࡺࡲࡷࡳ࠳ࡖࡵࡣ࡮࡬ࡧࡐ࡫ࡹ࠯ࡆࡖࡅࠧࠨࠢត")
__revision__ = l1l1111_Krypto_ (u"ࠧࠪࡉࡥࠦࠥថ")
import sys as l1l11l11_Krypto_
import os as l1111111l1_Krypto_
if l1l11l11_Krypto_.version_info[0] == 2 and l1l11l11_Krypto_.version_info[1] == 1:
    from l111ll1_Krypto_.l1l111ll_Krypto_.l1l1ll1l_Krypto_ import *
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
import unittest as l1lll111111_Krypto_
from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l1ll1lllll1_Krypto_ import l1lll1111l1_Krypto_, a2b_hex, b2a_hex
def _11lll11lll_Krypto_(s):
    l1l1111_Krypto_ (u"ࠨࠢࠣࡔࡨࡱࡴࡼࡥࠡࡹ࡫࡭ࡹ࡫ࡳࡱࡣࡦࡩࠥ࡬ࡲࡰ࡯ࠣࡥࠥࡺࡥࡹࡶࠣࡳࡷࠦࡢࡺࡶࡨࠤࡸࡺࡲࡪࡰࡪࠦࠧࠨទ")
    if isinstance(s,str):
        return l1l1111_Krypto_ (u"ࠢࠣធ").join(s.split())
    else:
        return b(l1l1111_Krypto_ (u"ࠣࠤន")).join(s.split())
class l11llll11ll_Krypto_(l1lll111111_Krypto_.TestCase):
    y = _11lll11lll_Krypto_(l1l1111_Krypto_ (u"ࠤࠥࠦ࠶࠿࠱࠴࠳࠻࠻࠶ࠦࡤ࠸࠷ࡥ࠵࠻࠷࠲ࠡࡣ࠻࠵࠾࡬࠲࠺ࡦࠣ࠻࠽ࡪ࠱ࡣ࠲ࡧ࠻ࠥ࠹࠴࠷ࡨ࠺ࡥࡦ࠽ࠠ࠸ࡤࡥ࠺࠷ࡧ࠸࠶ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠾ࡨࡦࡥ࠸ࡦ࠹࠻ࠦ࠷࠶ࡦࡤ࠽ࡩ࠸࠱ࠡ࠴ࡧ࠷ࡦ࠹࠶ࡦࡨࠣ࠵࠻࠽࠲ࡦࡨ࠹࠺ࠥ࠶ࡢ࠹ࡥ࠺ࡧ࠷࠻ࠠ࠶ࡥࡦ࠴ࡪࡩ࠷࠵ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠽࠻࠸ࡧࡤࡤ࠷࠸ࠦࡦ࠵࠶ࡦ࠴࠻࠼࠹ࠡ࠻࠹࠷࠵ࡧ࠷࠷ࡤࠣ࠴࠸࠶ࡥࡦ࠵࠶࠷ࠧࠨࠢប"))
    g = _11lll11lll_Krypto_(l1l1111_Krypto_ (u"ࠥࠦࠧ࠼࠲࠷ࡦ࠳࠶࠼࠾ࠠ࠴࠻ࡨࡥ࠵ࡧ࠱࠴ࠢ࠷࠵࠸࠷࠶࠴ࡣ࠸ࠤ࠺ࡨ࠴ࡤࡤ࠸࠴࠵ࠦ࠲࠺࠻ࡧ࠹࠺࠸࠲ࠡ࠻࠸࠺ࡨ࡫ࡦࡤࡤࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠹ࡢࡧࡨ࠴࠴࡫࠹ࠠ࠺࠻ࡦࡩ࠷ࡩ࠲ࡦࠢ࠺࠵ࡨࡨ࠹ࡥࡧ࠸ࠤ࡫ࡧ࠲࠵ࡤࡤࡦ࡫ࠦ࠵࠹ࡧ࠸ࡦ࠼࠿࠵ࠡ࠴࠴࠽࠷࠻ࡣ࠺ࡥࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡩ࠴࠳ࡧ࠼ࡪ࠻࡬ࠠ࠵࠸࠷ࡦ࠵࠾࠸ࡤࠢࡦ࠹࠼࠸ࡡࡧ࠷࠶ࠤࡪ࠼ࡤ࠸࠺࠻࠴࠷ࠨࠢࠣផ"))
    p = _11lll11lll_Krypto_(l1l1111_Krypto_ (u"ࠦࠧࠨ࠸ࡥࡨ࠵ࡥ࠹࠿࠴ࠡ࠶࠼࠶࠷࠽࠶ࡢࡣࠣ࠷ࡩ࠸࠵࠸࠷࠼ࡦࠥࡨ࠰࠷࠺࠹࠽ࡨࡨࠠࡦࡣࡦ࠴ࡩ࠾࠳ࡢࠢࡩࡦ࠽ࡪ࠰ࡤࡨ࠺ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡣࡣࡤ࠻࠷࠷࠺ࡦࠡ࠲ࡧ࠻࠽࠾࠲ࡦ࠷ࠣࡨ࠵࠽࠶࠳ࡨࡦ࠹ࠥࡨ࠷࠳࠳࠳ࡩࡦ࡬ࠠࡤ࠴ࡨ࠽ࡦࡪࡡࡤࠢ࠶࠶ࡦࡨ࠷ࡢࡣࡦࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠴࠺࠸࠼࠷ࡩ࡬ࡢࠡࡨ࠻࠷࠼࠸࠴ࡤ࠴ࠣࡩࡨ࠶࠷࠴࠸ࡨࡩࠥ࠹࠱ࡤ࠺࠳࠶࠾࠷ࠢࠣࠤព"))
    q = _11lll11lll_Krypto_(l1l1111_Krypto_ (u"ࠧࠨࠢࡤ࠹࠺࠷࠷࠷࠸ࡤࠢ࠺࠷࠼࡫ࡣ࠹ࡧࡨࠤ࠾࠿࠳ࡣ࠶ࡩ࠶ࡩࠦࡥࡥ࠵࠳ࡪ࠹࠾ࡥࠡࡦࡤࡧࡪ࠿࠱࠶ࡨࠥࠦࠧភ"))
    x = _11lll11lll_Krypto_(l1l1111_Krypto_ (u"ࠨࠢࠣ࠴࠳࠻࠵ࡨ࠳࠳࠴ࠣ࠷ࡩࡨࡡ࠴࠹࠵ࡪࠥࡪࡥ࠲ࡥ࠳ࡪ࡫ࡩࠠ࠸ࡤ࠵ࡩ࠸ࡨ࠴࠺ࠢ࠻ࡦ࠷࠼࠰࠷࠳࠷ࠦࠧࠨម"))
    k = _11lll11lll_Krypto_(l1l1111_Krypto_ (u"ࠢࠣࠤ࠶࠹࠽ࡪࡡࡥ࠷࠺ࠤ࠶࠺࠶࠳࠹࠴࠴࡫ࠦ࠵࠱ࡧ࠵࠹࠹ࡩࡦࠡ࠳ࡤ࠷࠼࠼ࡢ࠳ࡤࠣࡨࡪࡧࡡࡥࡨࡥࡪࠧࠨࠢយ"))
    l11llll111l_Krypto_ = _11lll11lll_Krypto_(l1l1111_Krypto_ (u"ࠣࠤࠥ࠴ࡩ࠻࠱࠷࠹࠵࠽ࠥ࠾࠲࠱࠴ࡨ࠸࠾ࡨࠠ࠵࠳࠴࠺ࡦࡩ࠱࠱ࠢ࠷ࡪࡨ࠹ࡦ࠵࠳࠸ࠤࡦ࡫࠵࠳ࡨ࠼࠵࠼ࠨࠢࠣរ"))
    m = b2a_hex(b(l1l1111_Krypto_ (u"ࠤࡤࡦࡨࠨល")))
    l11llll1111_Krypto_ = _11lll11lll_Krypto_(l1l1111_Krypto_ (u"ࠥࠦࠧࡧ࠹࠺࠻࠶ࡩ࠸࠼ࠠ࠵࠹࠳࠺࠽࠷࠶ࡢࠢࡥࡥ࠸࡫࠲࠶࠹࠴ࠤ࠼࠾࠵࠱ࡥ࠵࠺ࡨࠦ࠹ࡤࡦ࠳ࡨ࠽࠿ࡤࠣࠤࠥវ"))
    r = _11lll11lll_Krypto_(l1l1111_Krypto_ (u"ࠦࠧࠨ࠸ࡣࡣࡦ࠵ࡦࡨ࠶ࠡ࠸࠷࠵࠵࠺࠳࠶ࡥࠣࡦ࠼࠷࠸࠲ࡨ࠼࠹ࠥࡨ࠱࠷ࡣࡥ࠽࠼ࡩࠠ࠺࠴ࡥ࠷࠹࠷ࡣ࠱ࠤࠥࠦឝ"))
    s = _11lll11lll_Krypto_(l1l1111_Krypto_ (u"ࠧࠨࠢ࠵࠳ࡨ࠶࠸࠺࠵ࡧࠢ࠴ࡪ࠺࠼ࡤࡧ࠴࠷ࠤ࠺࠾ࡦ࠵࠴࠹ࡨ࠶ࠦ࠵࠶ࡤ࠷ࡦࡦ࠸ࡤࠡࡤ࠹ࡨࡨࡪ࠸ࡤ࠺ࠥࠦࠧឞ"))
    def setUp(self):
        global l1l111ll11_Krypto_, l1ll1l11l1_Krypto_, l1ll111ll1_Krypto_, size
        from l111ll1_Krypto_.l11l11l1_Krypto_ import l1l111ll11_Krypto_
        from l111ll1_Krypto_ import l1ll1l11l1_Krypto_
        from l111ll1_Krypto_.l1l111ll_Krypto_.l111l1ll_Krypto_ import l1ll111ll1_Krypto_, l11llll1ll_Krypto_, size
        self.l11lll1ll1l_Krypto_ = l1l111ll11_Krypto_
    def l11llll1ll1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠨࠢࠣࡆࡖࡅࠥ࠮ࡤࡦࡨࡤࡹࡱࡺࠠࡪ࡯ࡳࡰࡪࡳࡥ࡯ࡶࡤࡸ࡮ࡵ࡮ࠪࠢࡪࡩࡳ࡫ࡲࡢࡶࡨࡨࠥࡱࡥࡺࠢࠫ࠵ࠥࡧࡲࡨࡷࡰࡩࡳࡺࠩࠣࠤࠥស")
        l11lll11l1l_Krypto_ = self.l11lll1ll1l_Krypto_.l1llllll1_Krypto_(1024)
        self._11lll11111_Krypto_(l11lll11l1l_Krypto_)
        l11lll111ll_Krypto_ = l11lll11l1l_Krypto_.l1l11l111l_Krypto_()
        self._11lll1lll1_Krypto_(l11lll111ll_Krypto_)
    def l11lll1l1l1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠢࠣࠤࡇࡗࡆࠦࠨࡥࡧࡩࡥࡺࡲࡴࠡ࡫ࡰࡴࡱ࡫࡭ࡦࡰࡷࡥࡹ࡯࡯࡯ࠫࠣ࡫ࡪࡴࡥࡳࡣࡷࡩࡩࠦ࡫ࡦࡻࠣࠬ࠷ࠦࡡࡳࡩࡸࡱࡪࡴࡴࡴࠫࠥࠦࠧហ")
        l11lll11l1l_Krypto_ = self.l11lll1ll1l_Krypto_.l1llllll1_Krypto_(1024, l1ll1l11l1_Krypto_.new().read)
        self._11lll11111_Krypto_(l11lll11l1l_Krypto_)
        l11lll111ll_Krypto_ = l11lll11l1l_Krypto_.l1l11l111l_Krypto_()
        self._11lll1lll1_Krypto_(l11lll111ll_Krypto_)
    def l11llll1l11_Krypto_(self):
        l1l1111_Krypto_ (u"ࠣࠤࠥࡈࡘࡇࠠࠩࡦࡨࡪࡦࡻ࡬ࡵࠢ࡬ࡱࡵࡲࡥ࡮ࡧࡱࡸࡦࡺࡩࡰࡰࠬࠤࡨࡵ࡮ࡴࡶࡵࡹࡨࡺࡥࡥࠢ࡮ࡩࡾࠦࠨ࠵࠯ࡷࡹࡵࡲࡥࠪࠤࠥࠦឡ")
        (y, g, p, q) = [l1ll111ll1_Krypto_(a2b_hex(param)) for param in (self.y, self.g, self.p, self.q)]
        l11lll11l1l_Krypto_ = self.l11lll1ll1l_Krypto_.l1l1l1111l_Krypto_((y, g, p, q))
        self._11lll1111l_Krypto_(l11lll11l1l_Krypto_)
    def l11lll1l1ll_Krypto_(self):
        l1l1111_Krypto_ (u"ࠤࠥࠦࡉ࡙ࡁࠡࠪࡧࡩ࡫ࡧࡵ࡭ࡶࠣ࡭ࡲࡶ࡬ࡦ࡯ࡨࡲࡹࡧࡴࡪࡱࡱ࠭ࠥࡩ࡯࡯ࡵࡷࡶࡺࡩࡴࡦࡦࠣ࡯ࡪࡿࠠࠩ࠷࠰ࡸࡺࡶ࡬ࡦࠫࠥࠦࠧអ")
        (y, g, p, q, x) = [l1ll111ll1_Krypto_(a2b_hex(param)) for param in (self.y, self.g, self.p, self.q, self.x)]
        l11lll11l1l_Krypto_ = self.l11lll1ll1l_Krypto_.l1l1l1111l_Krypto_((y, g, p, q, x))
        self._11lll1l111_Krypto_(l11lll11l1l_Krypto_)
        self._11lll1111l_Krypto_(l11lll11l1l_Krypto_)
    def _11lll11111_Krypto_(self, l11lll11l1l_Krypto_):
        self.assertEqual(1, l11lll11l1l_Krypto_.l1l1111l1l_Krypto_())
        self.assertEqual(1, l11lll11l1l_Krypto_.l1l11ll1l1_Krypto_())
        self.assertEqual(0, l11lll11l1l_Krypto_.l1l1111l11_Krypto_())
        self.assertEqual(0, l11lll11l1l_Krypto_.l1l1111ll1_Krypto_())
        self.assertEqual(l11lll11l1l_Krypto_.y, l11lll11l1l_Krypto_.key.y)
        self.assertEqual(l11lll11l1l_Krypto_.g, l11lll11l1l_Krypto_.key.g)
        self.assertEqual(l11lll11l1l_Krypto_.p, l11lll11l1l_Krypto_.key.p)
        self.assertEqual(l11lll11l1l_Krypto_.q, l11lll11l1l_Krypto_.key.q)
        self.assertEqual(l11lll11l1l_Krypto_.x, l11lll11l1l_Krypto_.key.x)
        self.assertEqual(1, l11lll11l1l_Krypto_.p > l11lll11l1l_Krypto_.q)
        self.assertEqual(160, size(l11lll11l1l_Krypto_.q))
        self.assertEqual(0, (l11lll11l1l_Krypto_.p - 1) % l11lll11l1l_Krypto_.q)
        self.assertEqual(l11lll11l1l_Krypto_.y, pow(l11lll11l1l_Krypto_.g, l11lll11l1l_Krypto_.x, l11lll11l1l_Krypto_.p))
        self.assertEqual(1, 0 < l11lll11l1l_Krypto_.x < l11lll11l1l_Krypto_.q)
    def _11lll1lll1_Krypto_(self, l11lll11l1l_Krypto_):
        k = a2b_hex(self.k)
        l11llll1111_Krypto_ = a2b_hex(self.l11llll1111_Krypto_)
        self.assertEqual(0, l11lll11l1l_Krypto_.l1l1111l1l_Krypto_())
        self.assertEqual(1, l11lll11l1l_Krypto_.l1l11ll1l1_Krypto_())
        self.assertEqual(0, l11lll11l1l_Krypto_.l1l1111l11_Krypto_())
        self.assertEqual(0, l11lll11l1l_Krypto_.l1l1111ll1_Krypto_())
        self.assertEqual(l11lll11l1l_Krypto_.y, l11lll11l1l_Krypto_.key.y)
        self.assertEqual(l11lll11l1l_Krypto_.g, l11lll11l1l_Krypto_.key.g)
        self.assertEqual(l11lll11l1l_Krypto_.p, l11lll11l1l_Krypto_.key.p)
        self.assertEqual(l11lll11l1l_Krypto_.q, l11lll11l1l_Krypto_.key.q)
        self.assertEqual(0, hasattr(l11lll11l1l_Krypto_, l1l1111_Krypto_ (u"ࠪࡼࠬឣ")))
        self.assertEqual(0, hasattr(l11lll11l1l_Krypto_.key, l1l1111_Krypto_ (u"ࠫࡽ࠭ឤ")))
        self.assertEqual(1, l11lll11l1l_Krypto_.p > l11lll11l1l_Krypto_.q)
        self.assertEqual(160, size(l11lll11l1l_Krypto_.q))
        self.assertEqual(0, (l11lll11l1l_Krypto_.p - 1) % l11lll11l1l_Krypto_.q)
        self.assertRaises(TypeError, l11lll11l1l_Krypto_.l1l11lll11_Krypto_, l11llll1111_Krypto_, k)
        self.assertEqual(l11lll11l1l_Krypto_.l1l11l111l_Krypto_() == l11lll11l1l_Krypto_.l1l11l111l_Krypto_(),True)
        self.assertEqual(l11lll11l1l_Krypto_.l1l11l111l_Krypto_() != l11lll11l1l_Krypto_.l1l11l111l_Krypto_(),False)
    def _11lll1l111_Krypto_(self, l11lll11l1l_Krypto_):
        k = a2b_hex(self.k)
        l11llll1111_Krypto_ = a2b_hex(self.l11llll1111_Krypto_)
        r = l1ll111ll1_Krypto_(a2b_hex(self.r))
        s = l1ll111ll1_Krypto_(a2b_hex(self.s))
        (l11llll1l1l_Krypto_, l11lll1l11l_Krypto_) = l11lll11l1l_Krypto_.l1l11lll11_Krypto_(l11llll1111_Krypto_, k)
        self.assertEqual((r, s), (l11llll1l1l_Krypto_, l11lll1l11l_Krypto_))
    def _11lll1111l_Krypto_(self, l11lll11l1l_Krypto_):
        l11llll1111_Krypto_ = a2b_hex(self.l11llll1111_Krypto_)
        r = l1ll111ll1_Krypto_(a2b_hex(self.r))
        s = l1ll111ll1_Krypto_(a2b_hex(self.s))
        self.assertEqual(1, l11lll11l1l_Krypto_.l1l11l1l11_Krypto_(l11llll1111_Krypto_, (r, s)))
        self.assertEqual(0, l11lll11l1l_Krypto_.l1l11l1l11_Krypto_(l11llll1111_Krypto_ + b(l1l1111_Krypto_ (u"ࠧࡢ࠰ࠣឥ")), (r, s)))
class l11lll11ll1_Krypto_(l11llll11ll_Krypto_):
    def setUp(self):
        l11llll11ll_Krypto_.setUp(self)
        self.l11lll1ll1l_Krypto_ = l1l111ll11_Krypto_.l1l11ll11l_Krypto_(l1l11l1ll1_Krypto_=True)
    def l11llll1ll1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠨࠢࠣࡆࡖࡅࠥ࠮࡟ࡧࡣࡶࡸࡲࡧࡴࡩࠢ࡬ࡱࡵࡲࡥ࡮ࡧࡱࡸࡦࡺࡩࡰࡰࠬࠤ࡬࡫࡮ࡦࡴࡤࡸࡪࡪࠠ࡬ࡧࡼࠤ࠭࠷ࠠࡢࡴࡪࡹࡲ࡫࡮ࡵࠫࠥࠦࠧឦ")
        l11llll11ll_Krypto_.l11llll1ll1_Krypto_(self)
    def l11lll1l1l1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠢࠣࠤࡇࡗࡆࠦࠨࡠࡨࡤࡷࡹࡳࡡࡵࡪࠣ࡭ࡲࡶ࡬ࡦ࡯ࡨࡲࡹࡧࡴࡪࡱࡱ࠭ࠥ࡭ࡥ࡯ࡧࡵࡥࡹ࡫ࡤࠡ࡭ࡨࡽࠥ࠮࠲ࠡࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶ࠭ࠧࠨࠢឧ")
        l11llll11ll_Krypto_.l11lll1l1l1_Krypto_(self)
    def l11llll1l11_Krypto_(self):
        l1l1111_Krypto_ (u"ࠣࠤࠥࡈࡘࡇࠠࠩࡡࡩࡥࡸࡺ࡭ࡢࡶ࡫ࠤ࡮ࡳࡰ࡭ࡧࡰࡩࡳࡺࡡࡵ࡫ࡲࡲ࠮ࠦࡣࡰࡰࡶࡸࡷࡻࡣࡵࡧࡧࠤࡰ࡫ࡹࠡࠪ࠷࠱ࡹࡻࡰ࡭ࡧࠬࠦࠧࠨឨ")
        l11llll11ll_Krypto_.l11llll1l11_Krypto_(self)
    def l11lll1l1ll_Krypto_(self):
        l1l1111_Krypto_ (u"ࠤࠥࠦࡉ࡙ࡁࠡࠪࡢࡪࡦࡹࡴ࡮ࡣࡷ࡬ࠥ࡯࡭ࡱ࡮ࡨࡱࡪࡴࡴࡢࡶ࡬ࡳࡳ࠯ࠠࡤࡱࡱࡷࡹࡸࡵࡤࡶࡨࡨࠥࡱࡥࡺࠢࠫ࠹࠲ࡺࡵࡱ࡮ࡨ࠭ࠧࠨࠢឩ")
        l11llll11ll_Krypto_.l11lll1l1ll_Krypto_(self)
class l11lll111l1_Krypto_(l11llll11ll_Krypto_):
    def setUp(self):
        l11llll11ll_Krypto_.setUp(self)
        self.l11lll1ll1l_Krypto_ = l1l111ll11_Krypto_.l1l11ll11l_Krypto_(l1l11l1ll1_Krypto_=False)
    def l11llll1ll1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠥࠦࠧࡊࡓࡂࠢࠫࡣࡸࡲ࡯ࡸ࡯ࡤࡸ࡭ࠦࡩ࡮ࡲ࡯ࡩࡲ࡫࡮ࡵࡣࡷ࡭ࡴࡴࠩࠡࡩࡨࡲࡪࡸࡡࡵࡧࡧࠤࡰ࡫ࡹࠡࠪ࠴ࠤࡦࡸࡧࡶ࡯ࡨࡲࡹ࠯ࠢࠣࠤឪ")
        l11llll11ll_Krypto_.l11llll1ll1_Krypto_(self)
    def l11lll1l1l1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠦࠧࠨࡄࡔࡃࠣࠬࡤࡹ࡬ࡰࡹࡰࡥࡹ࡮ࠠࡪ࡯ࡳࡰࡪࡳࡥ࡯ࡶࡤࡸ࡮ࡵ࡮ࠪࠢࡪࡩࡳ࡫ࡲࡢࡶࡨࡨࠥࡱࡥࡺࠢࠫ࠶ࠥࡧࡲࡨࡷࡰࡩࡳࡺࡳࠪࠤࠥࠦឫ")
        l11llll11ll_Krypto_.l11lll1l1l1_Krypto_(self)
    def l11llll1l11_Krypto_(self):
        l1l1111_Krypto_ (u"ࠧࠨࠢࡅࡕࡄࠤ࠭ࡥࡳ࡭ࡱࡺࡱࡦࡺࡨࠡ࡫ࡰࡴࡱ࡫࡭ࡦࡰࡷࡥࡹ࡯࡯࡯ࠫࠣࡧࡴࡴࡳࡵࡴࡸࡧࡹ࡫ࡤࠡ࡭ࡨࡽࠥ࠮࠴࠮ࡶࡸࡴࡱ࡫ࠩࠣࠤࠥឬ")
        l11llll11ll_Krypto_.l11llll1l11_Krypto_(self)
    def l11lll1l1ll_Krypto_(self):
        l1l1111_Krypto_ (u"ࠨࠢࠣࡆࡖࡅࠥ࠮࡟ࡴ࡮ࡲࡻࡲࡧࡴࡩࠢ࡬ࡱࡵࡲࡥ࡮ࡧࡱࡸࡦࡺࡩࡰࡰࠬࠤࡨࡵ࡮ࡴࡶࡵࡹࡨࡺࡥࡥࠢ࡮ࡩࡾࠦࠨ࠶࠯ࡷࡹࡵࡲࡥࠪࠤࠥࠦឭ")
        l11llll11ll_Krypto_.l11lll1l1ll_Krypto_(self)
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    tests = []
    tests += l1lll1111l1_Krypto_(l11llll11ll_Krypto_)
    try:
        from l111ll1_Krypto_.l11l11l1_Krypto_ import _1l11ll111_Krypto_
        tests += l1lll1111l1_Krypto_(l11lll11ll1_Krypto_)
    except ImportError:
        from distutils.sysconfig import get_config_var as l11lll11l11_Krypto_
        import inspect as l11llll11l1_Krypto_
        _11lll1ll11_Krypto_ = l1111111l1_Krypto_.path.normpath(l1111111l1_Krypto_.path.dirname(l1111111l1_Krypto_.path.abspath(
            l11llll11l1_Krypto_.getfile(l11llll11l1_Krypto_.currentframe())))
            +l1l1111_Krypto_ (u"ࠢ࠰࠰࠱࠳࠳࠴࠯ࡑࡷࡥࡰ࡮ࡩࡋࡦࡻ࠲ࡣ࡫ࡧࡳࡵ࡯ࡤࡸ࡭ࠨឮ")+l11lll11l11_Krypto_(l1l1111_Krypto_ (u"ࠣࡕࡒࠦឯ")))
        if l1111111l1_Krypto_.path.exists(_11lll1ll11_Krypto_):
            raise ImportError(l1l1111_Krypto_ (u"ࠤ࡚࡬࡮ࡲࡥࠡࡶ࡫ࡩࠥࡥࡦࡢࡵࡷࡱࡦࡺࡨࠡ࡯ࡲࡨࡺࡲࡥࠡࡧࡻ࡭ࡸࡺࡳ࠭ࠢ࡬ࡱࡵࡵࡲࡵ࡫ࡱ࡫ࠥࠨឰ")+
                l1l1111_Krypto_ (u"ࠥ࡭ࡹࠦࡦࡢ࡫࡯ࡩࡩ࠴ࠠࡕࡪ࡬ࡷࠥࡳࡡࡺࠢࡳࡳ࡮ࡴࡴࠡࡶࡲࠤࡹ࡮ࡥࠡࡩࡰࡴࠥࡵࡲࠡ࡯ࡳ࡭ࡷࠦࡳࡩࡣࡵࡩࡩࠦ࡬ࡪࡤࡵࡥࡷࡿࠠࠣឱ")+
                l1l1111_Krypto_ (u"ࠦࡳࡵࡴࠡࡤࡨ࡭ࡳ࡭ࠠࡪࡰࠣࡸ࡭࡫ࠠࡱࡣࡷ࡬࠳ࠦ࡟ࡧࡣࡶࡸࡲࡧࡴࡩࠢࡺࡥࡸࠦࡦࡰࡷࡱࡨࠥࡧࡴࠡࠤឲ")+_11lll1ll11_Krypto_)
    tests += l1lll1111l1_Krypto_(l11lll111l1_Krypto_)
    return tests
if __name__ == l1l1111_Krypto_ (u"ࠬࡥ࡟࡮ࡣ࡬ࡲࡤࡥࠧឳ"):
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"࠭ࡳࡶ࡫ࡷࡩࠬ឴"))