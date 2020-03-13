# coding: utf-8
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
__revision__ = l1l1111_Krypto_ (u"ࠢࠥࡋࡧࠨࠧᝡ")
import unittest as l1lll111111_Krypto_
from l111ll1_Krypto_.l11l1l1lll_Krypto_ import l1l1llll1l_Krypto_
text = l1l1111_Krypto_ (u"ࠣࠤࠥࡠࠏ࡝ࡨࡦࡰࠣ࡭ࡳࠦࡴࡩࡧࠣࡇࡴࡻࡲࡴࡧࠣࡳ࡫ࠦࡨࡶ࡯ࡤࡲࠥ࡫ࡶࡦࡰࡷࡷ࠱ࠦࡩࡵࠢࡥࡩࡨࡵ࡭ࡦࡵࠣࡲࡪࡩࡥࡴࡵࡤࡶࡾࠦࡦࡰࡴࠣࡳࡳ࡫ࠠࡱࡧࡲࡴࡱ࡫ࠠࡵࡱࠍࡨ࡮ࡹࡳࡰ࡮ࡹࡩࠥࡺࡨࡦࠢࡳࡳࡱ࡯ࡴࡪࡥࡤࡰࠥࡨࡡ࡯ࡦࡶࠤࡼ࡮ࡩࡤࡪࠣ࡬ࡦࡼࡥࠡࡥࡲࡲࡳ࡫ࡣࡵࡧࡧࠤࡹ࡮ࡥ࡮ࠢࡺ࡭ࡹ࡮ࠠࡢࡰࡲࡸ࡭࡫ࡲ࠭ࠢࡤࡲࡩࠦࡴࡰࠌࡤࡷࡸࡻ࡭ࡦࠢࡤࡱࡴࡴࡧࠡࡶ࡫ࡩࠥࡶ࡯ࡸࡧࡵࡷࠥࡵࡦࠡࡶ࡫ࡩࠥ࡫ࡡࡳࡶ࡫࠰ࠥࡺࡨࡦࠢࡶࡩࡵࡧࡲࡢࡶࡨࠤࡦࡴࡤࠡࡧࡴࡹࡦࡲࠠࡴࡶࡤࡸ࡮ࡵ࡮ࠡࡶࡲࠤࡼ࡮ࡩࡤࡪࠍࡸ࡭࡫ࠠࡍࡣࡺࡷࠥࡵࡦࠡࡐࡤࡸࡺࡸࡥࠡࡣࡱࡨࠥࡵࡦࠡࡐࡤࡸࡺࡸࡥࠨࡵࠣࡋࡴࡪࠠࡦࡰࡷ࡭ࡹࡲࡥࠡࡶ࡫ࡩࡲ࠲ࠠࡢࠢࡧࡩࡨ࡫࡮ࡵࠢࡵࡩࡸࡶࡥࡤࡶࠣࡸࡴࠦࡴࡩࡧࠍࡳࡵ࡯࡮ࡪࡱࡱࡷࠥࡵࡦࠡ࡯ࡤࡲࡰ࡯࡮ࡥࠢࡵࡩࡶࡻࡩࡳࡧࡶࠤࡹ࡮ࡡࡵࠢࡷ࡬ࡪࡿࠠࡴࡪࡲࡹࡱࡪࠠࡥࡧࡦࡰࡦࡸࡥࠡࡶ࡫ࡩࠥࡩࡡࡶࡵࡨࡷࠥࡽࡨࡪࡥ࡫ࠤ࡮ࡳࡰࡦ࡮ࠍࡸ࡭࡫࡭ࠡࡶࡲࠤࡹ࡮ࡥࠡࡵࡨࡴࡦࡸࡡࡵ࡫ࡲࡲ࠳ࠐࠊࡘࡧࠣ࡬ࡴࡲࡤࠡࡶ࡫ࡩࡸ࡫ࠠࡵࡴࡸࡸ࡭ࡹࠠࡵࡱࠣࡦࡪࠦࡳࡦ࡮ࡩ࠱ࡪࡼࡩࡥࡧࡱࡸ࠱ࠦࡴࡩࡣࡷࠤࡦࡲ࡬ࠡ࡯ࡨࡲࠥࡧࡲࡦࠢࡦࡶࡪࡧࡴࡦࡦࠣࡩࡶࡻࡡ࡭࠮ࠣࡸ࡭ࡧࡴࠋࡶ࡫ࡩࡾࠦࡡࡳࡧࠣࡩࡳࡪ࡯ࡸࡧࡧࠤࡧࡿࠠࡵࡪࡨ࡭ࡷࠦࡃࡳࡧࡤࡸࡴࡸࠠࡸ࡫ࡷ࡬ࠥࡩࡥࡳࡶࡤ࡭ࡳࠦࡵ࡯ࡣ࡯࡭ࡪࡴࡡࡣ࡮ࡨࠤࡗ࡯ࡧࡩࡶࡶ࠰ࠥࡺࡨࡢࡶࠣࡥࡲࡵ࡮ࡨࠌࡷ࡬ࡪࡹࡥࠡࡣࡵࡩࠥࡒࡩࡧࡧ࠯ࠤࡑ࡯ࡢࡦࡴࡷࡽ࠱ࠦࡡ࡯ࡦࠣࡸ࡭࡫ࠠࡱࡷࡵࡷࡺ࡯ࡴࠡࡱࡩࠤࡍࡧࡰࡱ࡫ࡱࡩࡸࡹ࠮ࠡࡖ࡫ࡥࡹࠦࡴࡰࠢࡶࡩࡨࡻࡲࡦࠢࡷ࡬ࡪࡹࡥࠋࡴ࡬࡫࡭ࡺࡳ࠭ࠢࡊࡳࡻ࡫ࡲ࡯࡯ࡨࡲࡹࡹࠠࡢࡴࡨࠤ࡮ࡴࡳࡵ࡫ࡷࡹࡹ࡫ࡤࠡࡣࡰࡳࡳ࡭ࠠࡎࡧࡱ࠰ࠥࡪࡥࡳ࡫ࡹ࡭ࡳ࡭ࠠࡵࡪࡨ࡭ࡷࠦࡪࡶࡵࡷࠤࡵࡵࡷࡦࡴࡶࠤ࡫ࡸ࡯࡮ࠌࡷ࡬ࡪࠦࡣࡰࡰࡶࡩࡳࡺࠠࡰࡨࠣࡸ࡭࡫ࠠࡨࡱࡹࡩࡷࡴࡥࡥ࠰ࠣࡘ࡭ࡧࡴࠡࡹ࡫ࡩࡳ࡫ࡶࡦࡴࠣࡥࡳࡿࠠࡇࡱࡵࡱࠥࡵࡦࠡࡉࡲࡺࡪࡸ࡮࡮ࡧࡱࡸࠥࡨࡥࡤࡱࡰࡩࡸࠐࡤࡦࡵࡷࡶࡺࡩࡴࡪࡸࡨࠤࡴ࡬ࠠࡵࡪࡨࡷࡪࠦࡥ࡯ࡦࡶ࠰ࠥ࡯ࡴࠡ࡫ࡶࠤࡹ࡮ࡥࠡࡔ࡬࡫࡭ࡺࠠࡰࡨࠣࡸ࡭࡫ࠠࡑࡧࡲࡴࡱ࡫ࠠࡵࡱࠣࡥࡱࡺࡥࡳࠢࡲࡶࠥࡺ࡯ࠋࡣࡥࡳࡱ࡯ࡳࡩࠢ࡬ࡸ࠱ࠦࡡ࡯ࡦࠣࡸࡴࠦࡩ࡯ࡵࡷ࡭ࡹࡻࡴࡦࠢࡱࡩࡼࠦࡇࡰࡸࡨࡶࡳࡳࡥ࡯ࡶ࠯ࠤࡱࡧࡹࡪࡰࡪࠤ࡮ࡺࡳࠡࡨࡲࡹࡳࡪࡡࡵ࡫ࡲࡲࠥࡵ࡮ࠡࡵࡸࡧ࡭ࠐࡰࡳ࡫ࡱࡧ࡮ࡶ࡬ࡦࡵࠣࡥࡳࡪࠠࡰࡴࡪࡥࡳ࡯ࡺࡪࡰࡪࠤ࡮ࡺࡳࠡࡲࡲࡻࡪࡸࡳࠡ࡫ࡱࠤࡸࡻࡣࡩࠢࡩࡳࡷࡳࠬࠡࡣࡶࠤࡹࡵࠠࡵࡪࡨࡱࠥࡹࡨࡢ࡮࡯ࠤࡸ࡫ࡥ࡮ࠢࡰࡳࡸࡺࠊ࡭࡫࡮ࡩࡱࡿࠠࡵࡱࠣࡩ࡫࡬ࡥࡤࡶࠣࡸ࡭࡫ࡩࡳࠢࡖࡥ࡫࡫ࡴࡺࠢࡤࡲࡩࠦࡈࡢࡲࡳ࡭ࡳ࡫ࡳࡴ࠰ࠍࠦࠧࠨᝢ")
class l1l111111ll_Krypto_ (l1lll111111_Krypto_.TestCase):
    def runTest(self):
        l1l1111_Krypto_ (u"ࠤࡖ࡭ࡲࡶ࡬ࡦࠢࡷࡩࡸࡺࡳࠡࡱࡩࠤࡨ࡮ࡡࡧࡨ࡬ࡲ࡬ࠦࡡ࡯ࡦࠣࡻ࡮ࡴ࡮ࡰࡹ࡬ࡲ࡬ࠨᝣ")
        l1l1llll1l_Krypto_.l1ll1111ll_Krypto_()
        l1l1llll1l_Krypto_.l1ll1111ll_Krypto_(0.5, 1)
        self.assertRaises(ValueError, l1l1llll1l_Krypto_.l1ll1111ll_Krypto_, l1ll1111l1_Krypto_=-1)
        self.assertRaises(ValueError, l1l1llll1l_Krypto_.l1ll1111ll_Krypto_, l1l1lll1ll_Krypto_=-1)
        data = [(1, l1l1111_Krypto_ (u"ࠪࡨࡦࡺࡡ࠲ࠩᝤ"), l1l1111_Krypto_ (u"ࠫࡩࡧࡴࡢ࠳ࠪᝥ")), (2, l1l1111_Krypto_ (u"ࠬࡪࡡࡵࡣ࠵ࠫᝦ"), l1l1111_Krypto_ (u"࠭ࡤࡢࡶࡤ࠶ࠬᝧ"))]
        c = l1l1llll1l_Krypto_.l1ll1111ll_Krypto_(1.0, 1)
        c.l1l1ll11l1_Krypto_(data)
        l1l1ll11l1_Krypto_ = c.l1l1ll11l1_Krypto_(data)
        self.assertEqual(len(l1l1ll11l1_Krypto_), 4)
        c = l1l1llll1l_Krypto_.l1ll1111ll_Krypto_(0.0, 1)
        l1l1ll11l1_Krypto_ = c.l1l1ll11l1_Krypto_(data)
        self.assertEqual(len(l1l1ll11l1_Krypto_), 2)
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    return [l1l111111ll_Krypto_()]
if __name__ == l1l1111_Krypto_ (u"ࠢࡠࡡࡰࡥ࡮ࡴ࡟ࡠࠤᝨ"):
    l1lll111111_Krypto_.main()