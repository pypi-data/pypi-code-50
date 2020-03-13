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
l1l1111_Krypto_ (u"ࠢࠣࠤࡖࡩࡱ࡬࠭ࡵࡧࡶࡸࠥࡹࡵࡪࡶࡨࠤ࡫ࡵࡲࠡࡅࡵࡽࡵࡺ࡯࠯ࡒࡸࡦࡱ࡯ࡣࡌࡧࡼ࠲ࡗ࡙ࡁࠣࠤࠥᡝ")
__revision__ = l1l1111_Krypto_ (u"ࠣࠦࡌࡨࠩࠨᡞ")
import sys as l1l11l11_Krypto_
import os as l1111111l1_Krypto_
if l1l11l11_Krypto_.version_info[0] == 2 and l1l11l11_Krypto_.version_info[1] == 1:
    from l111ll1_Krypto_.l1l111ll_Krypto_.l1l1ll1l_Krypto_ import *
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
import unittest as l1lll111111_Krypto_
from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l1ll1lllll1_Krypto_ import l1lll1111l1_Krypto_, a2b_hex, b2a_hex
class l11l11ll11l_Krypto_(l1lll111111_Krypto_.TestCase):
    l1ll11l1_Krypto_ = l1l1111_Krypto_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡨࡦࠥ࠽ࡡࠡ࠳࠼ࠤࡦࡩࠠࡦ࠻ࠣࡩ࠸ࠦ࠰࠱ࠢ࠹࠷ࠥ࠻࠰ࠡࡧ࠶ࠤ࠷࠿ࠠ࠶࠲ࠣ࠸ࡧࠦ࠴࠶ࠢࡨ࠶ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡣࡢࠢ࠻࠶ࠥ࠹࠱ࠡ࠲ࡥࠤ࠷࠼ࠠࡥࡥࠣࡨ࠽ࠦ࠷ࡥࠢ࠸ࡧࠥ࠼࠸ࠡࡨ࠴ࠤࡪ࡫ࠠࡢ࠺ࠣࡪ࠺ࠦ࠵࠳ࠢ࠹࠻ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡣ࠴ࠢ࠴ࡦࠥ࠸ࡥࠡ࠺ࡥࠤࡧ࠺ࠠ࠳࠷ࠣ࠵࡫ࠦ࠸࠵ࠢࡧ࠻ࠥ࡫࠰ࠡࡤ࠵ࠤࡨ࠶ࠠ࠵࠸ࠣ࠶࠻ࠦࡦ࠶ࠢࡤࡪࠏࠦࠠࠡࠢࠣࠤࠥࠦࡦ࠺ࠢ࠶ࡩࠥࡪࡣࠡࡨࡥࠤ࠷࠻ࠠࡤ࠻ࠣࡧ࠷ࠦࡢ࠴ࠢࡩࡪࠥ࠾ࡡࠡࡧ࠴ࠤ࠵࡫ࠠ࠹࠵ࠣ࠽ࡦࠦ࠲ࡥࠢࡧࡦࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠴ࡤࠢࡧࡧࠥ࡬ࡥࠡ࠶ࡩࠤ࡫࠺ࠠ࠸࠹ࠣ࠶࠽ࠦࡢ࠵ࠢࡤ࠵ࠥࡨ࠷ࠡࡥ࠴ࠤ࠸࠼ࠠ࠳ࡤࠣࡥࡦࠦࡤ࠳ࠢ࠼ࡥࠏࠦࠠࠡࠢࠣࠤࠥࠦࡢ࠵ࠢ࠻ࡨࠥ࠸࠸ࠡ࠸࠼ࠤࡩ࠻ࠠ࠱࠴ࠣ࠸࠶ࠦ࠲࠲ࠢ࠷࠷ࠥ࠻࠸ࠡ࠳࠴ࠤ࠺࠿ࠠ࠲ࡤࠣࡩ࠸ࠦ࠹࠳ࠢࡩ࠽ࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠸࠳ࠢࡩࡦࠥ࠹ࡥࠡ࠺࠺ࠤࡩ࠶ࠠ࠺࠷ࠣࡥࡪࠦࡢ࠵ࠢ࠳࠸ࠥ࠺࠸ࠡࡦࡥࠤ࠾࠽ࠠ࠳ࡨࠣ࠷ࡦࠦࡣ࠲ࠢ࠷ࡪࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠷ࡣࠢࡦ࠶ࠥ࠽࠵ࠡ࠳࠼ࠤ࠺࠸ࠠ࠹࠳ࠣࡧࡪࠦ࠳࠳ࠢࡧ࠶ࠥ࡬࠱ࠡࡤ࠺ࠤ࠻ࡪࠠ࠵ࡦࠣ࠷࠺ࠦ࠳ࡦࠢ࠵ࡨࠏࠦࠠࠡࠢࠥࠦࠧᡟ")
    l1ll111l_Krypto_ = l1l1111_Krypto_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠲࠴ࠣ࠹࠸ࠦࡥ࠱ࠢ࠷ࡨࠥࡩ࠰ࠡࡣ࠸ࠤ࠸࠿ࠠ࠸ࡤࠣࡦ࠹ࠦ࠴ࡢࠢ࠺ࡥࠥࡨ࠸ࠡ࠹ࡨࠤ࠾ࡨࠠࡧ࠴ࠣࡥ࠵ࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠴࠻ࠣࡥ࠸ࠦ࠳ࡥࠢ࠴ࡩࠥ࠿࠹ࠡ࠸ࡩࠤࡨ࠾ࠠ࠳ࡣࠣ࠽࠹ࠦࡣࡤࠢࡧ࠷ࠥ࠶࠰ࠡ࠹࠷ࠤࡨ࠿ࠠ࠶ࡦࠣࡪ࠼ࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠷࠵ࠣ࠻࠷ࠦ࠲࠱ࠢ࠴࠻ࠥ࠶࠶ࠡ࠻ࡨࠤ࠺࠸ࠠ࠷࠺ࠣࡨࡦࠦ࠵ࡥࠢ࠴ࡧࠥ࠶ࡢࠡ࠶ࡩࠤ࠽࠽ࠠ࠳ࡥࠣࡪ࠻ࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠶࠵ࠣࡧ࠶ࠦ࠱ࡥࠢࡩ࠼ࠥ࠸࠳ࠡ࠳࠷ࠤࡦ࠼ࠠ࠸࠻ࠣ࠺࠽ࠦࡤࡧࠢࡨࡥࠥ࡫࠲ࠡ࠺ࡧࠤࡪ࡬ࠠ࠱࠶ࠣࡦࡧࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠷ࡦࠣ࠼࠹ࠦࡢ࠲ࠢࡦ࠷ࠥ࠷ࡤࠡ࠸࠸ࠤ࠹ࡧࠠ࠲࠻ࠣ࠻࠵ࠦࡥ࠶ࠢ࠺࠼ࠥ࠹ࡢࠡࡦ࠹ࠤࡪࡨࠠ࠺࠸ࠣࡥ࠵ࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠳࠶ࠣࡧ࠷ࠦࡣࡢࠢ࠵ࡪࠥ࠺ࡡࠡ࠻࠳ࠤ࡫࡫ࠠ࠺ࡨࠣ࠶ࡪࠦࡦ࠶ࠢࡦ࠽ࠥࡩ࠱ࠡ࠶࠳ࠤࡪ࠻ࠠࡣࡤࠣ࠸࠽ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡥࡣࠣ࠽࠺ࠦ࠳࠷ࠢࡤࡨࠥ࠾࠷ࠡ࠲࠳ࠤࡨ࠾ࠠ࠵ࡨࠣࡧ࠾ࠦ࠱࠴ࠢ࠳ࡥࠥࡪࡥࠡࡣ࠺ࠤ࠹࡫ࠠ࠶࠷ࠣ࠼ࡩࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠶࠳ࠣࡥ࠼ࠦ࠴ࡥࠢࡧࡪࠥ࠾࠵ࠡࡦ࠻ࠤࡧ࠻ࠠ࠱ࡦࠣࡩ࠾ࠦ࠶࠹ࠢ࠶࠼ࠥࡪ࠶ࠡ࠲࠹ࠤ࠸࡫ࠠ࠱࠻ࠣ࠹࠺ࠐࠠࠡࠢࠣࠦࠧࠨᡠ")
    l111lll1_Krypto_ = l1l1111_Krypto_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡤࡥࠤ࡫࠾ࠠ࠳ࡨࠣ࠴࠾ࠦ࠰࠷ࠢ࠻࠶ࠥࡩࡥࠡ࠻ࡦࠤ࠷࠹ࠠ࠴࠺ࠣࡥࡨࠦ࠲ࡣࠢ࠼ࡨࠥࡧ࠸ࠡ࠹࠴ࠤ࡫࠽ࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠵࠹ࠤ࠽ࡪࠠ࠱࠹ࠣࡩࡪࠦࡤ࠵ࠢ࠴࠴ࠥ࠺࠳ࠡࡣ࠷ࠤ࠹࠶ࠠࡥ࠸ࠣࡦ࠻ࠦࡦ࠱ࠢ࠺࠸ࠥ࠻࠴ࠡࡨ࠸ࠤ࠶࡬ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡤ࠻ࠤࡩ࡬ࠠࡣࡣࠣࡥ࡫ࠦ࠰࠴ࠢ࠸ࡧࠥ࠶࠲ࠡࡣࡥࠤ࠻࠷ࠠࡦࡣࠣ࠸࠽ࠦࡣࡦࠢࡨࡦࠥ࠼ࡦࠡࡥࡧࠤ࠹࠾ࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠹࠹ࠤࡪࡪࠠ࠶࠴ࠣ࠴ࡩࠦ࠶࠱ࠢࡨ࠵ࠥ࡫ࡣࠡ࠶࠹ࠤ࠶࠿ࠠ࠸࠳ࠣ࠽ࡩࠦ࠸ࡢࠢ࠸ࡦࠥ࠾ࡢࠡ࠺࠳ࠤ࠼࡬ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡣࡩࠤࡧ࠾ࠠࡦ࠲ࠣࡥ࠸ࠦࡤࡧࠢࡦ࠻ࠥ࠹࠷ࠡ࠹࠵ࠤ࠸࡫ࠠࡦ࠸ࠣࡦ࠹ࠦࡢ࠸ࠢࡧ࠽ࠥ࠹ࡡࠡ࠴࠸ࠤ࠽࠺ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡧࡨࠤ࠻ࡧࠠ࠷࠶ࠣ࠽ࡩࠦ࠰࠷ࠢ࠳࠽ࠥ࠻࠳ࠡ࠹࠷ࠤ࠽࠾ࠠ࠴࠶ࠣࡦ࠷ࠦ࠴࠶ࠢ࠷࠹ࠥ࠿࠸ࠡ࠵࠼ࠤ࠹࡫ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡧ࠳ࠤࡦࡧࠠࡣ࠳ࠣ࠶ࡩࠦ࠷ࡣࠢ࠹࠵ࠥࡧ࠵ࠡ࠳ࡩࠤ࠺࠸ࠠ࠸ࡣࠣ࠽ࡦࠦ࠴࠲ࠢࡩ࠺ࠥࡩ࠱ࠡ࠸࠻ࠤ࠼࡬ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡧ࠵ࠤ࠺࠹ࠠ࠸࠴ࠣ࠽࠽ࠦࡣࡢࠢ࠵ࡥࠥ࠾ࡦࠡ࠷࠼ࠤ࠹࠼ࠠࡧ࠺ࠣࡩ࠺ࠦࡦࡥࠢ࠳࠽ࠥ࠷ࡤࠡࡤࡧࠤࡨࡨࠊࠡࠢࠣࠤࠧࠨࠢᡡ")
    e = 0x11
    l11l1l11111_Krypto_ = l1l1111_Krypto_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡦ࠽ࠥ࠽ࡦࠡࡤ࠴ࠤ࡫࠶ࠠ࠳࠹ࠣࡪ࠹ࠦ࠵࠴ࠢࡩ࠺ࠥ࠹࠴ࠡ࠳࠵ࠤ࠸࠹ࠠࡦࡣࠣࡥࡦࠦࡤ࠲ࠢࡧ࠽ࠥ࠹࠵ࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠶ࡪࠥ࠼ࡣࠡ࠶࠵ࠤࡩ࠶ࠠ࠹࠺ࠣ࠺࠻ࠦࡢ࠲ࠢࡧ࠴ࠥ࠻ࡡࠡ࠲ࡩࠤ࠷࠶ࠠ࠴࠷ࠣ࠴࠷ࠦ࠸ࡣࠢ࠼ࡨࠥ࠾࠶ࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠼࠼ࠥ࠺࠰ࠡࡤ࠷ࠤ࠶࠼ࠠ࠷࠸ࠣࡦ࠹ࠦ࠲ࡦࠢ࠼࠶ࠥ࡫ࡡࠡ࠲ࡧࠤࡦ࠹ࠠࡣ࠶ࠣ࠷࠷ࠦ࠰࠵ࠢࡥ࠹ࠥࡩࡦࠋࠢࠣࠤࠥࠦࠠࠡࠢࡦࡩࠥ࠹࠳ࠡ࠷࠵ࠤ࠺࠸ࠠ࠵ࡦࠣ࠴࠹ࠦ࠱࠷ࠢࡤ࠹ࠥࡧ࠴ࠡ࠶࠴ࠤࡪ࠽ࠠ࠱࠲ࠣࡥ࡫ࠦ࠴࠷ࠢ࠴࠹ࠥ࠶࠳ࠋࠢࠣࠤࠥࠨࠢࠣᡢ")
    def setUp(self):
        global l1l11lll1_Krypto_, l1ll1l11l1_Krypto_, l1ll111ll1_Krypto_
        from l111ll1_Krypto_.l11l11l1_Krypto_ import l1l11lll1_Krypto_
        from l111ll1_Krypto_ import l1ll1l11l1_Krypto_
        from l111ll1_Krypto_.l1l111ll_Krypto_.l111l1ll_Krypto_ import l1ll111ll1_Krypto_, l11llll1ll_Krypto_
        self.n = l1ll111ll1_Krypto_(a2b_hex(self.l111lll1_Krypto_))
        self.p = l1ll111ll1_Krypto_(a2b_hex(self.l11l1l11111_Krypto_))
        self.q = divmod(self.n, self.p)[0]
        self.d = l11llll1ll_Krypto_(self.e, (self.p-1)*(self.q-1))
        self.u = l11llll1ll_Krypto_(self.p, self.q)
        self.l11l1llll11_Krypto_ = l1l11lll1_Krypto_
    def l11llll1ll1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠨࠢࠣࡔࡖࡅࠥ࠮ࡤࡦࡨࡤࡹࡱࡺࠠࡪ࡯ࡳࡰࡪࡳࡥ࡯ࡶࡤࡸ࡮ࡵ࡮ࠪࠢࡪࡩࡳ࡫ࡲࡢࡶࡨࡨࠥࡱࡥࡺࠢࠫ࠵ࠥࡧࡲࡨࡷࡰࡩࡳࡺࠩࠣࠤࠥᡣ")
        l11l11lll1l_Krypto_ = self.l11l1llll11_Krypto_.l1llllll1_Krypto_(1024)
        self._11lll11111_Krypto_(l11l11lll1l_Krypto_)
        self._11ll1llll1_Krypto_(l11l11lll1l_Krypto_)
        l11lll111ll_Krypto_ = l11l11lll1l_Krypto_.l1l11l111l_Krypto_()
        self._11lll1lll1_Krypto_(l11lll111ll_Krypto_)
        self._11ll1l1lll_Krypto_(l11l11lll1l_Krypto_)
    def l11lll1l1l1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠢࠣࠤࡕࡗࡆࠦࠨࡥࡧࡩࡥࡺࡲࡴࠡ࡫ࡰࡴࡱ࡫࡭ࡦࡰࡷࡥࡹ࡯࡯࡯ࠫࠣ࡫ࡪࡴࡥࡳࡣࡷࡩࡩࠦ࡫ࡦࡻࠣࠬ࠷ࠦࡡࡳࡩࡸࡱࡪࡴࡴࡴࠫࠥࠦࠧᡤ")
        l11l11lll1l_Krypto_ = self.l11l1llll11_Krypto_.l1llllll1_Krypto_(1024, l1ll1l11l1_Krypto_.new().read)
        self._11lll11111_Krypto_(l11l11lll1l_Krypto_)
        self._11ll1llll1_Krypto_(l11l11lll1l_Krypto_)
        l11lll111ll_Krypto_ = l11l11lll1l_Krypto_.l1l11l111l_Krypto_()
        self._11lll1lll1_Krypto_(l11lll111ll_Krypto_)
        self._11ll1l1lll_Krypto_(l11l11lll1l_Krypto_)
    def l11l11l111l_Krypto_(self):
        l11l11lll1l_Krypto_ = self.l11l1llll11_Krypto_.l1llllll1_Krypto_(1024, l1ll1l11l1_Krypto_.new().read,e=65537)
        self._11lll11111_Krypto_(l11l11lll1l_Krypto_)
        self._11ll1llll1_Krypto_(l11l11lll1l_Krypto_)
        l11lll111ll_Krypto_ = l11l11lll1l_Krypto_.l1l11l111l_Krypto_()
        self._11lll1lll1_Krypto_(l11lll111ll_Krypto_)
        self._11ll1l1lll_Krypto_(l11l11lll1l_Krypto_)
        self.assertEqual(65537,l11l11lll1l_Krypto_.e)
    def l11l11l1ll1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠣࠤࠥࡖࡘࡇࠠࠩࡦࡨࡪࡦࡻ࡬ࡵࠢ࡬ࡱࡵࡲࡥ࡮ࡧࡱࡸࡦࡺࡩࡰࡰࠬࠤࡨࡵ࡮ࡴࡶࡵࡹࡨࡺࡥࡥࠢ࡮ࡩࡾࠦࠨ࠳࠯ࡷࡹࡵࡲࡥࠪࠤࠥࠦᡥ")
        l11lll111ll_Krypto_ = self.l11l1llll11_Krypto_.l1l1l1111l_Krypto_((self.n, self.e))
        self._11lll1lll1_Krypto_(l11lll111ll_Krypto_)
        self._11l11l11l1_Krypto_(l11lll111ll_Krypto_)
        self._11l11ll1ll_Krypto_(l11lll111ll_Krypto_)
    def l11l11l11ll_Krypto_(self):
        l1l1111_Krypto_ (u"ࠤࠥࠦࡗ࡙ࡁࠡࠪࡧࡩ࡫ࡧࡵ࡭ࡶࠣ࡭ࡲࡶ࡬ࡦ࡯ࡨࡲࡹࡧࡴࡪࡱࡱ࠭ࠥࡩ࡯࡯ࡵࡷࡶࡺࡩࡴࡦࡦࠣ࡯ࡪࡿࠠࠩ࠵࠰ࡸࡺࡶ࡬ࡦࠫࠥࠦࠧᡦ")
        l11l11lll1l_Krypto_ = self.l11l1llll11_Krypto_.l1l1l1111l_Krypto_((self.n, self.e, self.d))
        self._11l11l11l1_Krypto_(l11l11lll1l_Krypto_)
        self._11l11lllll_Krypto_(l11l11lll1l_Krypto_)
        self._11l111llll_Krypto_(l11l11lll1l_Krypto_)
        self._11l11ll1ll_Krypto_(l11l11lll1l_Krypto_)
    def l11llll1l11_Krypto_(self):
        l1l1111_Krypto_ (u"ࠥࠦࠧࡘࡓࡂࠢࠫࡨࡪ࡬ࡡࡶ࡮ࡷࠤ࡮ࡳࡰ࡭ࡧࡰࡩࡳࡺࡡࡵ࡫ࡲࡲ࠮ࠦࡣࡰࡰࡶࡸࡷࡻࡣࡵࡧࡧࠤࡰ࡫ࡹࠡࠪ࠷࠱ࡹࡻࡰ࡭ࡧࠬࠦࠧࠨᡧ")
        l11l11lll1l_Krypto_ = self.l11l1llll11_Krypto_.l1l1l1111l_Krypto_((self.n, self.e, self.d, self.p))
        self._11l11l11l1_Krypto_(l11l11lll1l_Krypto_)
        self._11l11lllll_Krypto_(l11l11lll1l_Krypto_)
        self._11l111llll_Krypto_(l11l11lll1l_Krypto_)
        self._11l11ll1ll_Krypto_(l11l11lll1l_Krypto_)
    def l11lll1l1ll_Krypto_(self):
        l1l1111_Krypto_ (u"ࠦࠧࠨࡒࡔࡃࠣࠬࡩ࡫ࡦࡢࡷ࡯ࡸࠥ࡯࡭ࡱ࡮ࡨࡱࡪࡴࡴࡢࡶ࡬ࡳࡳ࠯ࠠࡤࡱࡱࡷࡹࡸࡵࡤࡶࡨࡨࠥࡱࡥࡺࠢࠫ࠹࠲ࡺࡵࡱ࡮ࡨ࠭ࠧࠨࠢᡨ")
        l11l11lll1l_Krypto_ = self.l11l1llll11_Krypto_.l1l1l1111l_Krypto_((self.n, self.e, self.d, self.p, self.q))
        self._11lll11111_Krypto_(l11l11lll1l_Krypto_)
        self._11l11l11l1_Krypto_(l11l11lll1l_Krypto_)
        self._11l11lllll_Krypto_(l11l11lll1l_Krypto_)
        self._11l111llll_Krypto_(l11l11lll1l_Krypto_)
        self._11l11ll1ll_Krypto_(l11l11lll1l_Krypto_)
    def l11l111l1ll_Krypto_(self):
        l1l1111_Krypto_ (u"ࠧࠨࠢࡓࡕࡄࠤ࠭ࡪࡥࡧࡣࡸࡰࡹࠦࡩ࡮ࡲ࡯ࡩࡲ࡫࡮ࡵࡣࡷ࡭ࡴࡴࠩࠡࡥࡲࡲࡸࡺࡲࡶࡥࡷࡩࡩࠦ࡫ࡦࡻࠣࠬ࠻࠳ࡴࡶࡲ࡯ࡩ࠮ࠨࠢࠣᡩ")
        l11l11lll1l_Krypto_ = self.l11l1llll11_Krypto_.l1l1l1111l_Krypto_((self.n, self.e, self.d, self.p, self.q, self.u))
        self._11lll11111_Krypto_(l11l11lll1l_Krypto_)
        self._11l11l11l1_Krypto_(l11l11lll1l_Krypto_)
        self._11l11lllll_Krypto_(l11l11lll1l_Krypto_)
        self._11l111llll_Krypto_(l11l11lll1l_Krypto_)
        self._11l11ll1ll_Krypto_(l11l11lll1l_Krypto_)
    def l11l11l1l11_Krypto_(self):
        l11l11lll1l_Krypto_ = self.l11l1llll11_Krypto_.l1l1l1111l_Krypto_([self.n, self.e, self.d])
        self.assertTrue(l11l11lll1l_Krypto_.p==self.p or l11l11lll1l_Krypto_.p==self.q)
        self.assertTrue(l11l11lll1l_Krypto_.q==self.p or l11l11lll1l_Krypto_.q==self.q)
        self.assertTrue(l11l11lll1l_Krypto_.q*l11l11lll1l_Krypto_.p == self.n)
        self.assertRaises(ValueError, self.l11l1llll11_Krypto_.l1l1l1111l_Krypto_, [self.n, self.e, self.n-1])
    def _11lll11111_Krypto_(self, l11l11lll1l_Krypto_):
        self.assertEqual(1, l11l11lll1l_Krypto_.l1l1111l1l_Krypto_())
        self.assertEqual(1, l11l11lll1l_Krypto_.l1l11ll1l1_Krypto_())
        self.assertEqual(1, l11l11lll1l_Krypto_.l1l1111l11_Krypto_())
        self.assertEqual(1, l11l11lll1l_Krypto_.l1l1111ll1_Krypto_())
        self.assertEqual(l11l11lll1l_Krypto_.n, l11l11lll1l_Krypto_.key.n)
        self.assertEqual(l11l11lll1l_Krypto_.e, l11l11lll1l_Krypto_.key.e)
        self.assertEqual(l11l11lll1l_Krypto_.d, l11l11lll1l_Krypto_.key.d)
        self.assertEqual(l11l11lll1l_Krypto_.p, l11l11lll1l_Krypto_.key.p)
        self.assertEqual(l11l11lll1l_Krypto_.q, l11l11lll1l_Krypto_.key.q)
        self.assertEqual(l11l11lll1l_Krypto_.u, l11l11lll1l_Krypto_.key.u)
        self.assertEqual(l11l11lll1l_Krypto_.n, l11l11lll1l_Krypto_.p * l11l11lll1l_Krypto_.q)
        self.assertEqual(1, l11l11lll1l_Krypto_.d * l11l11lll1l_Krypto_.e % ((l11l11lll1l_Krypto_.p-1) * (l11l11lll1l_Krypto_.q-1)))
        self.assertEqual(1, l11l11lll1l_Krypto_.p * l11l11lll1l_Krypto_.u % l11l11lll1l_Krypto_.q)
        self.assertEqual(1, l11l11lll1l_Krypto_.p > 1)
        self.assertEqual(1, l11l11lll1l_Krypto_.q > 1)
        self.assertEqual(1, l11l11lll1l_Krypto_.e > 1)
        self.assertEqual(1, l11l11lll1l_Krypto_.d > 1)
    def _11lll1lll1_Krypto_(self, l11l11lll1l_Krypto_):
        l1ll111l_Krypto_ = a2b_hex(self.l1ll111l_Krypto_)
        self.assertEqual(0, l11l11lll1l_Krypto_.l1l1111l1l_Krypto_())
        self.assertEqual(1, l11l11lll1l_Krypto_.l1l11ll1l1_Krypto_())
        self.assertEqual(1, l11l11lll1l_Krypto_.l1l1111l11_Krypto_())
        self.assertEqual(1, l11l11lll1l_Krypto_.l1l1111ll1_Krypto_())
        self.assertEqual(l11l11lll1l_Krypto_.n, l11l11lll1l_Krypto_.key.n)
        self.assertEqual(l11l11lll1l_Krypto_.e, l11l11lll1l_Krypto_.key.e)
        self.assertEqual(0, hasattr(l11l11lll1l_Krypto_, l1l1111_Krypto_ (u"࠭ࡤࠨᡪ")))
        self.assertEqual(0, hasattr(l11l11lll1l_Krypto_, l1l1111_Krypto_ (u"ࠧࡱࠩᡫ")))
        self.assertEqual(0, hasattr(l11l11lll1l_Krypto_, l1l1111_Krypto_ (u"ࠨࡳࠪᡬ")))
        self.assertEqual(0, hasattr(l11l11lll1l_Krypto_, l1l1111_Krypto_ (u"ࠩࡸࠫᡭ")))
        self.assertEqual(0, hasattr(l11l11lll1l_Krypto_.key, l1l1111_Krypto_ (u"ࠪࡨࠬᡮ")))
        self.assertEqual(0, hasattr(l11l11lll1l_Krypto_.key, l1l1111_Krypto_ (u"ࠫࡵ࠭ᡯ")))
        self.assertEqual(0, hasattr(l11l11lll1l_Krypto_.key, l1l1111_Krypto_ (u"ࠬࡷࠧᡰ")))
        self.assertEqual(0, hasattr(l11l11lll1l_Krypto_.key, l1l1111_Krypto_ (u"࠭ࡵࠨᡱ")))
        self.assertEqual(1, l11l11lll1l_Krypto_.e > 1)
        self.assertRaises(TypeError, l11l11lll1l_Krypto_.l1l11lll11_Krypto_, l1ll111l_Krypto_, b(l1l1111_Krypto_ (u"ࠢࠣᡲ")))
        self.assertRaises(TypeError, l11l11lll1l_Krypto_.l1lllll_Krypto_, l1ll111l_Krypto_)
        self.assertEqual(l11l11lll1l_Krypto_.l1l11l111l_Krypto_() == l11l11lll1l_Krypto_.l1l11l111l_Krypto_(),True)
        self.assertEqual(l11l11lll1l_Krypto_.l1l11l111l_Krypto_() != l11l11lll1l_Krypto_.l1l11l111l_Krypto_(),False)
    def _11ll1llll1_Krypto_(self, l11l11lll1l_Krypto_):
        l1ll111l_Krypto_ = a2b_hex(self.l1ll111l_Krypto_)
        l1ll11l1_Krypto_ = l11l11lll1l_Krypto_.l1lllll_Krypto_((l1ll111l_Krypto_,))
        (l11l111ll11_Krypto_,) = l11l11lll1l_Krypto_.l1_Krypto_(l1ll11l1_Krypto_, b(l1l1111_Krypto_ (u"ࠣࠤᡳ")))
        self.assertEqual(b2a_hex(l1ll111l_Krypto_), b2a_hex(l11l111ll11_Krypto_))
        l11l11ll111_Krypto_ = l1ll1l11l1_Krypto_.new().read(len(l1ll111l_Krypto_)-1)
        l11l11lll11_Krypto_ = l11l11lll1l_Krypto_.l11lll1111_Krypto_(l1ll111l_Krypto_, l11l11ll111_Krypto_)
        l11l111lll1_Krypto_ = l11l11lll1l_Krypto_.l1lllll_Krypto_((l11l11lll11_Krypto_,))
        l11l11ll1l1_Krypto_ = l11l11lll1l_Krypto_.l11ll1ll1l_Krypto_(l11l111lll1_Krypto_, l11l11ll111_Krypto_)
        self.assertEqual(b2a_hex(l1ll11l1_Krypto_), b2a_hex(l11l11ll1l1_Krypto_))
        l11l11l1111_Krypto_ = l11l11lll1l_Krypto_.l1l11lll11_Krypto_(l1ll111l_Krypto_, b(l1l1111_Krypto_ (u"ࠤࠥᡴ")))
        self.assertEqual((l1ll111ll1_Krypto_(l1ll11l1_Krypto_),), l11l11l1111_Krypto_)
        self.assertEqual(1, l11l11lll1l_Krypto_.l1l11l1l11_Krypto_(l1ll111l_Krypto_, (l1ll111ll1_Krypto_(l1ll11l1_Krypto_),)))
    def _11ll1l1lll_Krypto_(self, l11l11lll1l_Krypto_):
        l1ll11l1_Krypto_ = a2b_hex(self.l1ll11l1_Krypto_)
        (l11l111ll11_Krypto_,) = l11l11lll1l_Krypto_.l1_Krypto_(l1ll11l1_Krypto_, b(l1l1111_Krypto_ (u"ࠥࠦᡵ")))
        l11l11lll1l_Krypto_.l1l11l1l11_Krypto_(l11l111ll11_Krypto_, (l1ll111ll1_Krypto_(l1ll11l1_Krypto_),))
    def _11l11l11l1_Krypto_(self, l11l11lll1l_Krypto_):
        l1ll11l1_Krypto_ = a2b_hex(self.l1ll11l1_Krypto_)
        l1ll111l_Krypto_ = a2b_hex(self.l1ll111l_Krypto_)
        (l11l111ll11_Krypto_,) = l11l11lll1l_Krypto_.l1_Krypto_(l1ll11l1_Krypto_, b(l1l1111_Krypto_ (u"ࠦࠧᡶ")))
        self.assertEqual(b2a_hex(l1ll111l_Krypto_), b2a_hex(l11l111ll11_Krypto_))
    def _11l11lllll_Krypto_(self, l11l11lll1l_Krypto_):
        l1ll11l1_Krypto_ = a2b_hex(self.l1ll11l1_Krypto_)
        l1ll111l_Krypto_ = a2b_hex(self.l1ll111l_Krypto_)
        l11l11l1l1l_Krypto_ = l11l11lll1l_Krypto_.l1lllll_Krypto_((l1ll111l_Krypto_,))
        self.assertEqual(b2a_hex(l1ll11l1_Krypto_), b2a_hex(l11l11l1l1l_Krypto_))
        l11l11ll111_Krypto_ = l1ll1l11l1_Krypto_.new().read(len(l1ll111l_Krypto_)-1)
        l11l11lll11_Krypto_ = l11l11lll1l_Krypto_.l11lll1111_Krypto_(l1ll111l_Krypto_, l11l11ll111_Krypto_)
        l11l111lll1_Krypto_ = l11l11lll1l_Krypto_.l1lllll_Krypto_((l11l11lll11_Krypto_,))
        l11l11ll1l1_Krypto_ = l11l11lll1l_Krypto_.l11ll1ll1l_Krypto_(l11l111lll1_Krypto_, l11l11ll111_Krypto_)
        self.assertEqual(b2a_hex(l1ll11l1_Krypto_), b2a_hex(l11l11ll1l1_Krypto_))
    def _11l11ll1ll_Krypto_(self, l11l11lll1l_Krypto_):
        signature = l1ll111ll1_Krypto_(a2b_hex(self.l1ll11l1_Krypto_))
        message = a2b_hex(self.l1ll111l_Krypto_)
        t = (signature,)
        self.assertEqual(1, l11l11lll1l_Krypto_.l1l11l1l11_Krypto_(message, t))
        t2 = (signature, l1l1111_Krypto_ (u"ࠬ࠭ᡷ"))
        self.assertEqual(1, l11l11lll1l_Krypto_.l1l11l1l11_Krypto_(message, t2))
    def _11l111llll_Krypto_(self, l11l11lll1l_Krypto_):
        signature = l1ll111ll1_Krypto_(a2b_hex(self.l1ll11l1_Krypto_))
        message = a2b_hex(self.l1ll111l_Krypto_)
        self.assertEqual((signature,), l11l11lll1l_Krypto_.l1l11lll11_Krypto_(message, b(l1l1111_Krypto_ (u"ࠨࠢᡸ"))))
class l11l11l1lll_Krypto_(l11l11ll11l_Krypto_):
    def setUp(self):
        l11l11ll11l_Krypto_.setUp(self)
        self.l11l1llll11_Krypto_ = l1l11lll1_Krypto_.l11l111ll1_Krypto_(l1l11l1ll1_Krypto_=True)
    def l11llll1ll1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠢࠣࠤࡕࡗࡆࠦࠨࡠࡨࡤࡷࡹࡳࡡࡵࡪࠣ࡭ࡲࡶ࡬ࡦ࡯ࡨࡲࡹࡧࡴࡪࡱࡱ࠭ࠥ࡭ࡥ࡯ࡧࡵࡥࡹ࡫ࡤࠡ࡭ࡨࡽࠥ࠮࠱ࠡࡣࡵ࡫ࡺࡳࡥ࡯ࡶࠬࠦࠧࠨ᡹")
        l11l11ll11l_Krypto_.l11llll1ll1_Krypto_(self)
    def l11lll1l1l1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠣࠤࠥࡖࡘࡇࠠࠩࡡࡩࡥࡸࡺ࡭ࡢࡶ࡫ࠤ࡮ࡳࡰ࡭ࡧࡰࡩࡳࡺࡡࡵ࡫ࡲࡲ࠮ࠦࡧࡦࡰࡨࡶࡦࡺࡥࡥࠢ࡮ࡩࡾࠦࠨ࠳ࠢࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷ࠮ࠨࠢࠣ᡺")
        l11l11ll11l_Krypto_.l11lll1l1l1_Krypto_(self)
    def l11l11l1ll1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠤࠥࠦࡗ࡙ࡁࠡࠪࡢࡪࡦࡹࡴ࡮ࡣࡷ࡬ࠥ࡯࡭ࡱ࡮ࡨࡱࡪࡴࡴࡢࡶ࡬ࡳࡳ࠯ࠠࡤࡱࡱࡷࡹࡸࡵࡤࡶࡨࡨࠥࡱࡥࡺࠢࠫ࠶࠲ࡺࡵࡱ࡮ࡨ࠭ࠧࠨࠢ᡻")
        l11l11ll11l_Krypto_.l11l11l1ll1_Krypto_(self)
    def l11l11l11ll_Krypto_(self):
        l1l1111_Krypto_ (u"ࠥࠦࠧࡘࡓࡂࠢࠫࡣ࡫ࡧࡳࡵ࡯ࡤࡸ࡭ࠦࡩ࡮ࡲ࡯ࡩࡲ࡫࡮ࡵࡣࡷ࡭ࡴࡴࠩࠡࡥࡲࡲࡸࡺࡲࡶࡥࡷࡩࡩࠦ࡫ࡦࡻࠣࠬ࠸࠳ࡴࡶࡲ࡯ࡩ࠮ࠨࠢࠣ᡼")
        l11l11ll11l_Krypto_.l11l11l11ll_Krypto_(self)
    def l11llll1l11_Krypto_(self):
        l1l1111_Krypto_ (u"ࠦࠧࠨࡒࡔࡃࠣࠬࡤ࡬ࡡࡴࡶࡰࡥࡹ࡮ࠠࡪ࡯ࡳࡰࡪࡳࡥ࡯ࡶࡤࡸ࡮ࡵ࡮ࠪࠢࡦࡳࡳࡹࡴࡳࡷࡦࡸࡪࡪࠠ࡬ࡧࡼࠤ࠭࠺࠭ࡵࡷࡳࡰࡪ࠯ࠢࠣࠤ᡽")
        l11l11ll11l_Krypto_.l11llll1l11_Krypto_(self)
    def l11lll1l1ll_Krypto_(self):
        l1l1111_Krypto_ (u"ࠧࠨࠢࡓࡕࡄࠤ࠭ࡥࡦࡢࡵࡷࡱࡦࡺࡨࠡ࡫ࡰࡴࡱ࡫࡭ࡦࡰࡷࡥࡹ࡯࡯࡯ࠫࠣࡧࡴࡴࡳࡵࡴࡸࡧࡹ࡫ࡤࠡ࡭ࡨࡽࠥ࠮࠵࠮ࡶࡸࡴࡱ࡫ࠩࠣࠤࠥ᡾")
        l11l11ll11l_Krypto_.l11lll1l1ll_Krypto_(self)
    def l11l111l1ll_Krypto_(self):
        l1l1111_Krypto_ (u"ࠨࠢࠣࡔࡖࡅࠥ࠮࡟ࡧࡣࡶࡸࡲࡧࡴࡩࠢ࡬ࡱࡵࡲࡥ࡮ࡧࡱࡸࡦࡺࡩࡰࡰࠬࠤࡨࡵ࡮ࡴࡶࡵࡹࡨࡺࡥࡥࠢ࡮ࡩࡾࠦࠨ࠷࠯ࡷࡹࡵࡲࡥࠪࠤࠥࠦ᡿")
        l11l11ll11l_Krypto_.l11l111l1ll_Krypto_(self)
    def l11l11l1l11_Krypto_(self):
        l11l11ll11l_Krypto_.l11l11l1l11_Krypto_(self)
class l11l111ll1l_Krypto_(l11l11ll11l_Krypto_):
    def setUp(self):
        l11l11ll11l_Krypto_.setUp(self)
        self.l11l1llll11_Krypto_ = l1l11lll1_Krypto_.l11l111ll1_Krypto_(l1l11l1ll1_Krypto_=False)
    def l11llll1ll1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠢࠣࠤࡕࡗࡆࠦࠨࡠࡵ࡯ࡳࡼࡳࡡࡵࡪࠣ࡭ࡲࡶ࡬ࡦ࡯ࡨࡲࡹࡧࡴࡪࡱࡱ࠭ࠥ࡭ࡥ࡯ࡧࡵࡥࡹ࡫ࡤࠡ࡭ࡨࡽࠥ࠮࠱ࠡࡣࡵ࡫ࡺࡳࡥ࡯ࡶࠬࠦࠧࠨᢀ")
        l11l11ll11l_Krypto_.l11llll1ll1_Krypto_(self)
    def l11lll1l1l1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠣࠤࠥࡖࡘࡇࠠࠩࡡࡶࡰࡴࡽ࡭ࡢࡶ࡫ࠤ࡮ࡳࡰ࡭ࡧࡰࡩࡳࡺࡡࡵ࡫ࡲࡲ࠮ࠦࡧࡦࡰࡨࡶࡦࡺࡥࡥࠢ࡮ࡩࡾࠦࠨ࠳ࠢࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷ࠮ࠨࠢࠣᢁ")
        l11l11ll11l_Krypto_.l11lll1l1l1_Krypto_(self)
    def l11l11l1ll1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠤࠥࠦࡗ࡙ࡁࠡࠪࡢࡷࡱࡵࡷ࡮ࡣࡷ࡬ࠥ࡯࡭ࡱ࡮ࡨࡱࡪࡴࡴࡢࡶ࡬ࡳࡳ࠯ࠠࡤࡱࡱࡷࡹࡸࡵࡤࡶࡨࡨࠥࡱࡥࡺࠢࠫ࠶࠲ࡺࡵࡱ࡮ࡨ࠭ࠧࠨࠢᢂ")
        l11l11ll11l_Krypto_.l11l11l1ll1_Krypto_(self)
    def l11l11l11ll_Krypto_(self):
        l1l1111_Krypto_ (u"ࠥࠦࠧࡘࡓࡂࠢࠫࡣࡸࡲ࡯ࡸ࡯ࡤࡸ࡭ࠦࡩ࡮ࡲ࡯ࡩࡲ࡫࡮ࡵࡣࡷ࡭ࡴࡴࠩࠡࡥࡲࡲࡸࡺࡲࡶࡥࡷࡩࡩࠦ࡫ࡦࡻࠣࠬ࠸࠳ࡴࡶࡲ࡯ࡩ࠮ࠨࠢࠣᢃ")
        l11l11ll11l_Krypto_.l11l11l11ll_Krypto_(self)
    def l11llll1l11_Krypto_(self):
        l1l1111_Krypto_ (u"ࠦࠧࠨࡒࡔࡃࠣࠬࡤࡹ࡬ࡰࡹࡰࡥࡹ࡮ࠠࡪ࡯ࡳࡰࡪࡳࡥ࡯ࡶࡤࡸ࡮ࡵ࡮ࠪࠢࡦࡳࡳࡹࡴࡳࡷࡦࡸࡪࡪࠠ࡬ࡧࡼࠤ࠭࠺࠭ࡵࡷࡳࡰࡪ࠯ࠢࠣࠤᢄ")
        l11l11ll11l_Krypto_.l11llll1l11_Krypto_(self)
    def l11lll1l1ll_Krypto_(self):
        l1l1111_Krypto_ (u"ࠧࠨࠢࡓࡕࡄࠤ࠭ࡥࡳ࡭ࡱࡺࡱࡦࡺࡨࠡ࡫ࡰࡴࡱ࡫࡭ࡦࡰࡷࡥࡹ࡯࡯࡯ࠫࠣࡧࡴࡴࡳࡵࡴࡸࡧࡹ࡫ࡤࠡ࡭ࡨࡽࠥ࠮࠵࠮ࡶࡸࡴࡱ࡫ࠩࠣࠤࠥᢅ")
        l11l11ll11l_Krypto_.l11lll1l1ll_Krypto_(self)
    def l11l111l1ll_Krypto_(self):
        l1l1111_Krypto_ (u"ࠨࠢࠣࡔࡖࡅࠥ࠮࡟ࡴ࡮ࡲࡻࡲࡧࡴࡩࠢ࡬ࡱࡵࡲࡥ࡮ࡧࡱࡸࡦࡺࡩࡰࡰࠬࠤࡨࡵ࡮ࡴࡶࡵࡹࡨࡺࡥࡥࠢ࡮ࡩࡾࠦࠨ࠷࠯ࡷࡹࡵࡲࡥࠪࠤࠥࠦᢆ")
        l11l11ll11l_Krypto_.l11l111l1ll_Krypto_(self)
    def l11l11l1l11_Krypto_(self):
        l11l11ll11l_Krypto_.l11l11l1l11_Krypto_(self)
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    tests = []
    tests += l1lll1111l1_Krypto_(l11l11ll11l_Krypto_)
    try:
        from l111ll1_Krypto_.l11l11l1_Krypto_ import _1l11ll111_Krypto_
        tests += l1lll1111l1_Krypto_(l11l11l1lll_Krypto_)
    except ImportError:
        from distutils.sysconfig import get_config_var as l11lll11l11_Krypto_
        import inspect as l11llll11l1_Krypto_
        _11lll1ll11_Krypto_ = l1111111l1_Krypto_.path.normpath(l1111111l1_Krypto_.path.dirname(l1111111l1_Krypto_.path.abspath(
            l11llll11l1_Krypto_.getfile(l11llll11l1_Krypto_.currentframe())))
            +l1l1111_Krypto_ (u"ࠢ࠰࠰࠱࠳࠳࠴࠯ࡑࡷࡥࡰ࡮ࡩࡋࡦࡻ࠲ࡣ࡫ࡧࡳࡵ࡯ࡤࡸ࡭ࠨᢇ")+l11lll11l11_Krypto_(l1l1111_Krypto_ (u"ࠣࡕࡒࠦᢈ")))
        if l1111111l1_Krypto_.path.exists(_11lll1ll11_Krypto_):
            raise ImportError(l1l1111_Krypto_ (u"ࠤ࡚࡬࡮ࡲࡥࠡࡶ࡫ࡩࠥࡥࡦࡢࡵࡷࡱࡦࡺࡨࠡ࡯ࡲࡨࡺࡲࡥࠡࡧࡻ࡭ࡸࡺࡳ࠭ࠢ࡬ࡱࡵࡵࡲࡵ࡫ࡱ࡫ࠥࠨᢉ")+
                l1l1111_Krypto_ (u"ࠥ࡭ࡹࠦࡦࡢ࡫࡯ࡩࡩ࠴ࠠࡕࡪ࡬ࡷࠥࡳࡡࡺࠢࡳࡳ࡮ࡴࡴࠡࡶࡲࠤࡹ࡮ࡥࠡࡩࡰࡴࠥࡵࡲࠡ࡯ࡳ࡭ࡷࠦࡳࡩࡣࡵࡩࡩࠦ࡬ࡪࡤࡵࡥࡷࡿࠠࠣᢊ")+
                l1l1111_Krypto_ (u"ࠦࡳࡵࡴࠡࡤࡨ࡭ࡳ࡭ࠠࡪࡰࠣࡸ࡭࡫ࠠࡱࡣࡷ࡬࠳ࠦ࡟ࡧࡣࡶࡸࡲࡧࡴࡩࠢࡺࡥࡸࠦࡦࡰࡷࡱࡨࠥࡧࡴࠡࠤᢋ")+_11lll1ll11_Krypto_)
    if l1ll1lll111_Krypto_.get(l1l1111_Krypto_ (u"ࠬࡹ࡬ࡰࡹࡢࡸࡪࡹࡴࡴࠩᢌ"),1):
        tests += l1lll1111l1_Krypto_(l11l111ll1l_Krypto_)
    return tests
if __name__ == l1l1111_Krypto_ (u"࠭࡟ࡠ࡯ࡤ࡭ࡳࡥ࡟ࠨᢍ"):
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭ᢎ"))