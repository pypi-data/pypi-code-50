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
l1l1111_Krypto_ (u"࡙ࠥࠦࠧࡥ࡭ࡨ࠰ࡸࡪࡹࡴࠡࡵࡸ࡭ࡹ࡫ࠠࡧࡱࡵࠤࡈࡸࡹࡱࡶࡲ࠲ࡍࡧࡳࡩ࠰ࡖࡌࡆ࠸࠵࠷ࠤࠥࠦ᜞")
__revision__ = l1l1111_Krypto_ (u"ࠦࠩࡏࡤࠥࠤᜟ")
import unittest as l1lll111111_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
class l1l1111ll11_Krypto_(l1lll111111_Krypto_.TestCase):
    def runTest(self):
        l1l1111_Krypto_ (u"ࠧࠨࠢࡔࡊࡄ࠶࠺࠼࠺ࠡ࠷࠴࠶࠴࠻࠲࠱ࠢࡐ࡭ࡇࠦࡴࡦࡵࡷࠦࠧࠨᜠ")
        from l111ll1_Krypto_.l1lll1ll1_Krypto_ import l1lll1ll11_Krypto_
        l1l1111l1l1_Krypto_ = l11111l11_Krypto_(0x00) * (1024*1024)
        h = l1lll1ll11_Krypto_.new(l1l1111l1l1_Krypto_)
        for i in range(511):
            h.update(l1l1111l1l1_Krypto_)
        self.assertEqual(l1l1111_Krypto_ (u"࠭࠹ࡢࡥࡦࡥ࠽࡫࠸ࡤ࠴࠵࠶࠵࠷࠱࠶࠷࠶࠼࠾࡬࠶࠶ࡣࡥࡦ࡫࠼ࡢࡤ࠻࠺࠶࠸࡫ࡤࡤ࠹࠶࠼࠹࡫ࡡࡥ࠺࠳࠹࠵࠹࠸࠴࠻ࡩ࠸࠾ࡪࡣࡤ࠷࠹ࡨ࠼࠼࠷ࠨᜡ"), h.hexdigest())
        for i in range(8):
            h.update(l1l1111l1l1_Krypto_)
        self.assertEqual(l1l1111_Krypto_ (u"ࠧࡢࡤࡩ࠹࠶ࡧࡤ࠺࠷࠷ࡦ࠷࠺࠶࠱࠲࠼ࡨ࡫࡫࠵ࡢ࠷࠳ࡩࡨࡪ࠵࠹࠴ࡩࡨ࠺ࡨ࠸ࡧ࠳ࡥ࠼ࡧ࠸࠷ࡧ࠵࠳࠷࠾࠹࠸࠶࠵ࡦ࠷ࡪ࡬࠷࠳࠳ࡨ࠻࡫ࡧ࠶ࡦࠩᜢ"), h.hexdigest())
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    l1ll11lllll_Krypto_ = [
        (l1l1111_Krypto_ (u"ࠨࡤࡤ࠻࠽࠷࠶ࡣࡨ࠻ࡪ࠵࠷ࡣࡧࡧࡤ࠸࠶࠺࠱࠵࠲ࡧࡩ࠺ࡪࡡࡦ࠴࠵࠶࠸ࡨ࠰࠱࠵࠹࠵ࡦ࠹࠹࠷࠳࠺࠻ࡦ࠿ࡣࡣ࠶࠴࠴࡫࡬࠶࠲ࡨ࠵࠴࠵࠷࠵ࡢࡦࠪᜣ"),
            l1l1111_Krypto_ (u"ࠩࡤࡦࡨ࠭ᜤ")),
        (l1l1111_Krypto_ (u"ࠪ࠶࠹࠾ࡤ࠷ࡣ࠹࠵ࡩ࠸࠰࠷࠵࠻ࡦ࠽࡫࠵ࡤ࠲࠵࠺࠾࠹࠰ࡤ࠵ࡨ࠺࠵࠹࠹ࡢ࠵࠶ࡧࡪ࠺࠵࠺࠸࠷ࡪ࡫࠸࠱࠷࠹ࡩ࠺ࡪࡩࡥࡥࡦ࠷࠵࠾ࡪࡢ࠱࠸ࡦ࠵ࠬᜥ"),
            l1l1111_Krypto_ (u"ࠫࡦࡨࡣࡥࡤࡦࡨࡪࡩࡤࡦࡨࡧࡩ࡫࡭ࡥࡧࡩ࡫ࡪ࡬࡮ࡩࡨࡪ࡬࡮࡭࡯ࡪ࡬࡫࡭࡯ࡱࡰ࡫࡭࡯࡮ࡰࡲࡴ࡬࡮ࡰࡲࡱࡳࡵࡰ࡯ࡱࡳࡵࠬᜦ")),
        (l1l1111_Krypto_ (u"ࠬࡩࡤࡤ࠹࠹ࡩ࠺ࡩ࠹࠺࠳࠷ࡪࡧ࠿࠲࠹࠳ࡤ࠵ࡨ࠽ࡥ࠳࠺࠷ࡨ࠼࠹ࡥ࠷࠹ࡩ࠵࠽࠶࠹ࡢ࠶࠻ࡥ࠹࠿࠷࠳࠲࠳ࡩ࠵࠺࠶ࡥ࠵࠼ࡧࡨࡩ࠷࠲࠳࠵ࡧࡩ࠶ࠧᜧ"),
            l1l1111_Krypto_ (u"࠭ࡡࠨᜨ") * 10**6,
             l1l1111_Krypto_ (u"ࠧࠣࡣࠥࠤ࠯ࠦ࠱࠱ࠬ࠭࠺ࠬᜩ")),
        (l1l1111_Krypto_ (u"ࠨࡨ࠺ࡪࡩ࠶࠱࠸ࡣ࠶ࡧ࠼࠸࠱ࡤࡧ࠺ࡪ࡫࠶࠳ࡧ࠵࠸࠹࠷ࡩ࠰࠹࠳࠶ࡥࡩࡩࡣ࠵࠺ࡥ࠻࡫࠹࠳ࡧ࠲࠺ࡩ࠺࡫࠲ࡣࡣ࠺࠵ࡪ࠸࠳ࡦࡣ࠶࠽࠸ࡪ࠱࠱࠵ࠪᜪ"),
            l1l1111_Krypto_ (u"ࠩࡗ࡬࡮ࡹࠠ࡮ࡧࡶࡷࡦ࡭ࡥࠡ࡫ࡶࠤࡵࡸࡥࡤ࡫ࡶࡩࡱࡿࠠ࠶࠷ࠣࡦࡾࡺࡥࡴࠢ࡯ࡳࡳ࡭ࠬࠡࡶࡲࠤࡹ࡫ࡳࡵࠢࡤࠤࡧࡻࡧ࠯ࠩᜫ"),
            l1l1111_Krypto_ (u"ࠪࡐࡪࡴࡧࡵࡪࠣࡁࠥ࠻࠵ࠡࠪࡰࡳࡩࠦ࠶࠵ࠫࠪᜬ")),
        (l1l1111_Krypto_ (u"ࠫࡪ࠹ࡢ࠱ࡥ࠷࠸࠷࠿࠸ࡧࡥ࠴ࡧ࠶࠺࠹ࡢࡨࡥࡪ࠹ࡩ࠸࠺࠻࠹ࡪࡧ࠿࠲࠵࠴࠺ࡥࡪ࠺࠱ࡦ࠶࠹࠸࠾ࡨ࠹࠴࠶ࡦࡥ࠹࠿࠵࠺࠻࠴ࡦ࠼࠾࠵࠳ࡤ࠻࠹࠺࠭ᜭ"), l1l1111_Krypto_ (u"ࠬ࠭ᜮ")),
        (l1l1111_Krypto_ (u"࠭ࡤ࠴࠴ࡥ࠹࠻࠾ࡣࡥ࠳ࡥ࠽࠻ࡪ࠴࠶࠻ࡨ࠻࠷࠿࠱ࡦࡤࡩ࠸ࡧ࠸࠵ࡥ࠲࠳࠻࡫࠸࠷࠶ࡥ࠼ࡪ࠶࠹࠱࠵࠻ࡥࡩࡪࡨ࠷࠹࠴ࡩࡥࡨ࠶࠷࠲࠸࠹࠵࠸࡬࠸ࠨᜯ"),
         l1l1111_Krypto_ (u"ࠧࡇࡴࡤࡲࡿࠦࡪࡢࡩࡷࠤ࡮ࡳࠠ࡬ࡱࡰࡴࡱ࡫ࡴࡵࠢࡹࡩࡷࡽࡡࡩࡴ࡯ࡳࡸࡺࡥ࡯ࠢࡗࡥࡽ࡯ࠠࡲࡷࡨࡶࠥࡪࡵࡳࡥ࡫ࠤࡇࡧࡹࡦࡴࡱࠫᜰ")),
    ]
    from l111ll1_Krypto_.l1lll1ll1_Krypto_ import l1lll1ll11_Krypto_
    from .common import l1l11l1l11l_Krypto_
    tests = l1l11l1l11l_Krypto_(l1lll1ll11_Krypto_, l1l1111_Krypto_ (u"ࠣࡕࡋࡅ࠷࠻࠶ࠣᜱ"), l1ll11lllll_Krypto_,
        digest_size=32,
        l1llllll11_Krypto_=l1l1111_Krypto_ (u"ࠤ࡟ࡼ࠵࠼࡜ࡹ࠲࠼ࡠࡽ࠼࠰࡝ࡺ࠻࠺ࡡࡾ࠴࠹࡞ࡻ࠴࠶ࡢࡸ࠷࠷࡟ࡼ࠵࠹࡜ࡹ࠲࠷ࡠࡽ࠶࠲࡝ࡺ࠳࠵ࠧᜲ"))
    if l1ll1lll111_Krypto_.get(l1l1111_Krypto_ (u"ࠪࡷࡱࡵࡷࡠࡶࡨࡷࡹࡹࠧᜳ")):
        tests += [l1l1111ll11_Krypto_()]
    return tests
if __name__ == l1l1111_Krypto_ (u"ࠫࡤࡥ࡭ࡢ࡫ࡱࡣࡤ᜴࠭"):
    import unittest as l1lll111111_Krypto_
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"ࠬࡹࡵࡪࡶࡨࠫ᜵"))