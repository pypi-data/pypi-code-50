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
l1l1111_Krypto_ (u"ࠨࠢࠣࡕࡨࡰ࡫࠳ࡴࡦࡵࡷࡷࠥ࡬࡯ࡳࠢࡆࡶࡾࡶࡴࡰ࠰ࡘࡸ࡮ࡲ࠮ࡄࡱࡸࡲࡹ࡫ࡲࠣࠤࠥ᧝")
__revision__ = l1l1111_Krypto_ (u"ࠢࠥࡋࡧࠨࠧ᧞")
import sys as l1l11l11_Krypto_
if l1l11l11_Krypto_.version_info[0] == 2 and l1l11l11_Krypto_.version_info[1] == 1:
    from l111ll1_Krypto_.l1l111ll_Krypto_.l1l1ll1l_Krypto_ import *
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
import unittest as l1lll111111_Krypto_
class l1111l11111_Krypto_(l1lll111111_Krypto_.TestCase):
    def setUp(self):
        global Counter
        from l111ll1_Krypto_.l1l111ll_Krypto_ import Counter
    def l1111l1lll1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠣࠤࠥࡆ࡮࡭ࠠࡦࡰࡧ࡭ࡦࡴࠬࠡࡵ࡫ࡳࡷࡺࡣࡶࡶࠣࡩࡳࡧࡢ࡭ࡧࡧࠦࠧࠨ᧟")
        c = Counter.new(128)
        self.assertEqual(c.__PCT_CTR_SHORTCUT__,True)
        c = Counter.new(128, l1lll1ll111_Krypto_=False)
        self.assertEqual(c.__PCT_CTR_SHORTCUT__,True)
        c = Counter.new(128, l1ll1l1lll1_Krypto_=False)
        self.assertEqual(c.__PCT_CTR_SHORTCUT__,True)
        c = Counter.new(128, l1lll1ll111_Krypto_=False, l1ll1l1lll1_Krypto_=False)
        self.assertEqual(c.__PCT_CTR_SHORTCUT__,True)
    def l1111l1l111_Krypto_(self):
        l1l1111_Krypto_ (u"ࠤࠥࠦࡑ࡯ࡴࡵ࡮ࡨࠤࡪࡴࡤࡪࡣࡱ࠰ࠥࡹࡨࡰࡴࡷࡧࡺࡺࠠࡦࡰࡤࡦࡱ࡫ࡤࠣࠤࠥ᧠")
        c = Counter.new(128, l1lll1ll111_Krypto_=True)
        self.assertEqual(c.__PCT_CTR_SHORTCUT__,True)
        c = Counter.new(128, l1lll1ll111_Krypto_=True, l1ll1l1lll1_Krypto_=False)
        self.assertEqual(c.__PCT_CTR_SHORTCUT__,True)
    def l1111l11lll_Krypto_(self):
        l1l1111_Krypto_ (u"ࠥࠦࠧࡈࡩࡨࠢࡨࡲࡩ࡯ࡡ࡯࠮ࠣࡷ࡭ࡵࡲࡵࡥࡸࡸࠥࡪࡩࡴࡣࡥࡰࡪࡪࠢࠣࠤ᧡")
        c = Counter.new(128, l1ll1l1lll1_Krypto_=True)
        self.assertRaises(AttributeError, getattr, c, l1l1111_Krypto_ (u"ࠫࡤࡥࡐࡄࡖࡢࡇ࡙ࡘ࡟ࡔࡊࡒࡖ࡙ࡉࡕࡕࡡࡢࠫ᧢"))
        c = Counter.new(128, l1lll1ll111_Krypto_=False, l1ll1l1lll1_Krypto_=True)
        self.assertRaises(AttributeError, getattr, c, l1l1111_Krypto_ (u"ࠬࡥ࡟ࡑࡅࡗࡣࡈ࡚ࡒࡠࡕࡋࡓࡗ࡚ࡃࡖࡖࡢࡣࠬ᧣"))
    def l1111l1l1l1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠨࠢࠣࡎ࡬ࡸࡹࡲࡥࠡࡧࡱࡨ࡮ࡧ࡮࠭ࠢࡶ࡬ࡴࡸࡴࡤࡷࡷࠤࡩ࡯ࡳࡢࡤ࡯ࡩࡩࠨࠢࠣ᧤")
        c = Counter.new(128, l1lll1ll111_Krypto_=True, l1ll1l1lll1_Krypto_=True)
        self.assertRaises(AttributeError, getattr, c, l1l1111_Krypto_ (u"ࠧࡠࡡࡓࡇ࡙ࡥࡃࡕࡔࡢࡗࡍࡕࡒࡕࡅࡘࡘࡤࡥࠧ᧥"))
    def l1111l11l11_Krypto_(self):
        l1l1111_Krypto_ (u"ࠣࠤࠥ࠵࠷࠾࠭ࡣ࡫ࡷ࠰ࠥࡈࡩࡨࠢࡨࡲࡩ࡯ࡡ࡯࠮ࠣࡨࡪ࡬ࡡࡶ࡮ࡷࡷࠧࠨࠢ᧦")
        c = Counter.new(128)
        self.assertEqual(1, c.l111ll1111l_Krypto_())
        self.assertEqual(b(l1l1111_Krypto_ (u"ࠤ࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠴ࠦ᧧")), c())
        self.assertEqual(2, c.l111ll1111l_Krypto_())
        self.assertEqual(b(l1l1111_Krypto_ (u"ࠥࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠶ࠧ᧨")), c())
        for i in range(3, 256):
            self.assertEqual(i, c.l111ll1111l_Krypto_())
            self.assertEqual(b(l1l1111_Krypto_ (u"ࠦࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱ࠤ᧩"))+l11111l11_Krypto_(i), c())
        self.assertEqual(256, c.l111ll1111l_Krypto_())
        self.assertEqual(b(l1l1111_Krypto_ (u"ࠧࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠳࡟ࡼ࠵࠶ࠢ᧪")), c())
    def l1111l111l1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠨࠢࠣ࠳࠵࠼࠲ࡨࡩࡵ࠮ࠣࡐ࡮ࡺࡴ࡭ࡧࠣࡩࡳࡪࡩࡢࡰ࠯ࠤࡩ࡫ࡦࡢࡷ࡯ࡸࡸࠨࠢࠣ᧫")
        c = Counter.new(128, l1lll1ll111_Krypto_=True)
        self.assertEqual(1, c.l111ll1111l_Krypto_())
        self.assertEqual(b(l1l1111_Krypto_ (u"ࠢ࡝ࡺ࠳࠵ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱ࠤ᧬")), c())
        self.assertEqual(2, c.l111ll1111l_Krypto_())
        self.assertEqual(b(l1l1111_Krypto_ (u"ࠣ࡞ࡻ࠴࠷ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲ࠥ᧭")), c())
        for i in range(3, 256):
            self.assertEqual(i, c.l111ll1111l_Krypto_())
            self.assertEqual(l11111l11_Krypto_(i)+b(l1l1111_Krypto_ (u"ࠤ࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶ࠢ᧮")), c())
        self.assertEqual(256, c.l111ll1111l_Krypto_())
        self.assertEqual(b(l1l1111_Krypto_ (u"ࠥࡠࡽ࠶࠰࡝ࡺ࠳࠵ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࠧ᧯")), c())
    def l1111l111ll_Krypto_(self):
        l1l1111_Krypto_ (u"ࠦࠧࠨ࠸࠮ࡤ࡬ࡸ࠱ࠦࡂࡪࡩࠣࡩࡳࡪࡩࡢࡰ࠯ࠤࡼࡸࡡࡱࡣࡵࡳࡺࡴࡤࠣࠤࠥ᧰")
        c = Counter.new(8)
        for i in range(1, 256):
            self.assertEqual(i, c.l111ll1111l_Krypto_())
            self.assertEqual(l11111l11_Krypto_(i), c())
        self.assertRaises(OverflowError, c.l111ll1111l_Krypto_)
        self.assertRaises(OverflowError, c)
        self.assertRaises(OverflowError, c.l111ll1111l_Krypto_)
        self.assertRaises(OverflowError, c)
    def l11111lllll_Krypto_(self):
        l1l1111_Krypto_ (u"ࠧࠨࠢ࠹࠯ࡥ࡭ࡹ࠲ࠠࡍ࡫ࡷࡸࡱ࡫ࠠࡦࡰࡧ࡭ࡦࡴࠬࠡࡹࡵࡥࡵࡧࡲࡰࡷࡱࡨࠧࠨࠢ᧱")
        c = Counter.new(8, l1lll1ll111_Krypto_=True)
        for i in range(1, 256):
            self.assertEqual(i, c.l111ll1111l_Krypto_())
            self.assertEqual(l11111l11_Krypto_(i), c())
        self.assertRaises(OverflowError, c.l111ll1111l_Krypto_)
        self.assertRaises(OverflowError, c)
        self.assertRaises(OverflowError, c.l111ll1111l_Krypto_)
        self.assertRaises(OverflowError, c)
    def l1111l1ll1l_Krypto_(self):
        l1l1111_Krypto_ (u"ࠨࠢࠣ࠺࠰ࡦ࡮ࡺࠬࠡࡄ࡬࡫ࠥ࡫࡮ࡥ࡫ࡤࡲ࠱ࠦࡷࡳࡣࡳࡥࡷࡵࡵ࡯ࡦࠣࡻ࡮ࡺࡨࠡࡣ࡯ࡰࡴࡽ࡟ࡸࡴࡤࡴࡦࡸ࡯ࡶࡰࡧࡁ࡙ࡸࡵࡦࠤࠥࠦ᧲")
        c = Counter.new(8, l1111l1l11l_Krypto_=True)
        for i in range(1, 256):
            self.assertEqual(i, c.l111ll1111l_Krypto_())
            self.assertEqual(l11111l11_Krypto_(i), c())
        self.assertEqual(0, c.l111ll1111l_Krypto_())
        self.assertEqual(b(l1l1111_Krypto_ (u"ࠢ࡝ࡺ࠳࠴ࠧ᧳")), c())
        self.assertEqual(1, c.l111ll1111l_Krypto_())
    def l1111l11ll1_Krypto_(self):
        l1l1111_Krypto_ (u"ࠣࠤࠥ࠼࠲ࡨࡩࡵ࠮ࠣࡐ࡮ࡺࡴ࡭ࡧࠣࡩࡳࡪࡩࡢࡰ࠯ࠤࡼࡸࡡࡱࡣࡵࡳࡺࡴࡤࠡࡹ࡬ࡸ࡭ࠦࡡ࡭࡮ࡲࡻࡤࡽࡲࡢࡲࡤࡶࡴࡻ࡮ࡥ࠿ࡗࡶࡺ࡫ࠢࠣࠤ᧴")
        c = Counter.new(8, l1lll1ll111_Krypto_=True, l1111l1l11l_Krypto_=True)
        for i in range(1, 256):
            self.assertEqual(i, c.l111ll1111l_Krypto_())
            self.assertEqual(l11111l11_Krypto_(i), c())
        self.assertEqual(0, c.l111ll1111l_Krypto_())
        self.assertEqual(b(l1l1111_Krypto_ (u"ࠤ࡟ࡼ࠵࠶ࠢ᧵")), c())
        self.assertEqual(1, c.l111ll1111l_Krypto_())
    def l1111l1l1ll_Krypto_(self):
        l1l1111_Krypto_ (u"ࠥࠦࠧ࠾࠭ࡣ࡫ࡷ࠰ࠥࡈࡩࡨࠢࡨࡲࡩ࡯ࡡ࡯࠮ࠣࡧࡦࡸࡲࡺࠢࡤࡸࡹࡸࡩࡣࡷࡷࡩࠧࠨࠢ᧶")
        c = Counter.new(8)
        for i in range(1, 256):
            self.assertEqual(0, c.l1111l11l1l_Krypto_)
            self.assertEqual(i, c.l111ll1111l_Krypto_())
            self.assertEqual(l11111l11_Krypto_(i), c())
        self.assertEqual(1, c.l1111l11l1l_Krypto_)
    def l1111l1ll11_Krypto_(self):
        l1l1111_Krypto_ (u"ࠦࠧࠨ࠸࠮ࡤ࡬ࡸ࠱ࠦࡌࡪࡶࡷࡰࡪࠦࡥ࡯ࡦ࡬ࡥࡳ࠲ࠠࡤࡣࡵࡶࡾࠦࡡࡵࡶࡵ࡭ࡧࡻࡴࡦࠤࠥࠦ᧷")
        c = Counter.new(8, l1lll1ll111_Krypto_=True)
        for i in range(1, 256):
            self.assertEqual(0, c.l1111l11l1l_Krypto_)
            self.assertEqual(i, c.l111ll1111l_Krypto_())
            self.assertEqual(l11111l11_Krypto_(i), c())
        self.assertEqual(1, c.l1111l11l1l_Krypto_)
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l1ll1lllll1_Krypto_ import l1lll1111l1_Krypto_
    return l1lll1111l1_Krypto_(l1111l11111_Krypto_)
if __name__ == l1l1111_Krypto_ (u"ࠬࡥ࡟࡮ࡣ࡬ࡲࡤࡥࠧ᧸"):
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"࠭ࡳࡶ࡫ࡷࡩࠬ᧹"))