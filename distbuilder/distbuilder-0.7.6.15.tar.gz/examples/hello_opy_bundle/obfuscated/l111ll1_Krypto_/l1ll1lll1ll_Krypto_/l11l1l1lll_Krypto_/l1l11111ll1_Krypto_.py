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
__revision__ = l1l1111_Krypto_ (u"ࠥࠨࡎࡪࠤࠣ᝝")
import unittest as l1lll111111_Krypto_
from l111ll1_Krypto_.l11l1l1lll_Krypto_ import l1lll111ll_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
text = b(l1l1111_Krypto_ (u"ࠦࠧࠨ࡜ࠋ࡙࡫ࡩࡳࠦࡩ࡯ࠢࡷ࡬ࡪࠦࡃࡰࡷࡵࡷࡪࠦ࡯ࡧࠢ࡫ࡹࡲࡧ࡮ࠡࡧࡹࡩࡳࡺࡳ࠭ࠢ࡬ࡸࠥࡨࡥࡤࡱࡰࡩࡸࠦ࡮ࡦࡥࡨࡷࡸࡧࡲࡺࠢࡩࡳࡷࠦ࡯࡯ࡧࠣࡴࡪࡵࡰ࡭ࡧࠣࡸࡴࠐࡤࡪࡵࡶࡳࡱࡼࡥࠡࡶ࡫ࡩࠥࡶ࡯࡭࡫ࡷ࡭ࡨࡧ࡬ࠡࡤࡤࡲࡩࡹࠠࡸࡪ࡬ࡧ࡭ࠦࡨࡢࡸࡨࠤࡨࡵ࡮࡯ࡧࡦࡸࡪࡪࠠࡵࡪࡨࡱࠥࡽࡩࡵࡪࠣࡥࡳࡵࡴࡩࡧࡵ࠰ࠥࡧ࡮ࡥࠢࡷࡳࠏࡧࡳࡴࡷࡰࡩࠥࡧ࡭ࡰࡰࡪࠤࡹ࡮ࡥࠡࡲࡲࡻࡪࡸࡳࠡࡱࡩࠤࡹ࡮ࡥࠡࡧࡤࡶࡹ࡮ࠬࠡࡶ࡫ࡩࠥࡹࡥࡱࡣࡵࡥࡹ࡫ࠠࡢࡰࡧࠤࡪࡷࡵࡢ࡮ࠣࡷࡹࡧࡴࡪࡱࡱࠤࡹࡵࠠࡸࡪ࡬ࡧ࡭ࠐࡴࡩࡧࠣࡐࡦࡽࡳࠡࡱࡩࠤࡓࡧࡴࡶࡴࡨࠤࡦࡴࡤࠡࡱࡩࠤࡓࡧࡴࡶࡴࡨࠫࡸࠦࡇࡰࡦࠣࡩࡳࡺࡩࡵ࡮ࡨࠤࡹ࡮ࡥ࡮࠮ࠣࡥࠥࡪࡥࡤࡧࡱࡸࠥࡸࡥࡴࡲࡨࡧࡹࠦࡴࡰࠢࡷ࡬ࡪࠐ࡯ࡱ࡫ࡱ࡭ࡴࡴࡳࠡࡱࡩࠤࡲࡧ࡮࡬࡫ࡱࡨࠥࡸࡥࡲࡷ࡬ࡶࡪࡹࠠࡵࡪࡤࡸࠥࡺࡨࡦࡻࠣࡷ࡭ࡵࡵ࡭ࡦࠣࡨࡪࡩ࡬ࡢࡴࡨࠤࡹ࡮ࡥࠡࡥࡤࡹࡸ࡫ࡳࠡࡹ࡫࡭ࡨ࡮ࠠࡪ࡯ࡳࡩࡱࠐࡴࡩࡧࡰࠤࡹࡵࠠࡵࡪࡨࠤࡸ࡫ࡰࡢࡴࡤࡸ࡮ࡵ࡮࠯ࠌࠍ࡛ࡪࠦࡨࡰ࡮ࡧࠤࡹ࡮ࡥࡴࡧࠣࡸࡷࡻࡴࡩࡵࠣࡸࡴࠦࡢࡦࠢࡶࡩࡱ࡬࠭ࡦࡸ࡬ࡨࡪࡴࡴ࠭ࠢࡷ࡬ࡦࡺࠠࡢ࡮࡯ࠤࡲ࡫࡮ࠡࡣࡵࡩࠥࡩࡲࡦࡣࡷࡩࡩࠦࡥࡲࡷࡤࡰ࠱ࠦࡴࡩࡣࡷࠎࡹ࡮ࡥࡺࠢࡤࡶࡪࠦࡥ࡯ࡦࡲࡻࡪࡪࠠࡣࡻࠣࡸ࡭࡫ࡩࡳࠢࡆࡶࡪࡧࡴࡰࡴࠣࡻ࡮ࡺࡨࠡࡥࡨࡶࡹࡧࡩ࡯ࠢࡸࡲࡦࡲࡩࡦࡰࡤࡦࡱ࡫ࠠࡓ࡫ࡪ࡬ࡹࡹࠬࠡࡶ࡫ࡥࡹࠦࡡ࡮ࡱࡱ࡫ࠏࡺࡨࡦࡵࡨࠤࡦࡸࡥࠡࡎ࡬ࡪࡪ࠲ࠠࡍ࡫ࡥࡩࡷࡺࡹ࠭ࠢࡤࡲࡩࠦࡴࡩࡧࠣࡴࡺࡸࡳࡶ࡫ࡷࠤࡴ࡬ࠠࡉࡣࡳࡴ࡮ࡴࡥࡴࡵ࠱ࠤ࡙࡮ࡡࡵࠢࡷࡳࠥࡹࡥࡤࡷࡵࡩࠥࡺࡨࡦࡵࡨࠎࡷ࡯ࡧࡩࡶࡶ࠰ࠥࡍ࡯ࡷࡧࡵࡲࡲ࡫࡮ࡵࡵࠣࡥࡷ࡫ࠠࡪࡰࡶࡸ࡮ࡺࡵࡵࡧࡧࠤࡦࡳ࡯࡯ࡩࠣࡑࡪࡴࠬࠡࡦࡨࡶ࡮ࡼࡩ࡯ࡩࠣࡸ࡭࡫ࡩࡳࠢ࡭ࡹࡸࡺࠠࡱࡱࡺࡩࡷࡹࠠࡧࡴࡲࡱࠏࡺࡨࡦࠢࡦࡳࡳࡹࡥ࡯ࡶࠣࡳ࡫ࠦࡴࡩࡧࠣ࡫ࡴࡼࡥࡳࡰࡨࡨ࠳ࠦࡔࡩࡣࡷࠤࡼ࡮ࡥ࡯ࡧࡹࡩࡷࠦࡡ࡯ࡻࠣࡊࡴࡸ࡭ࠡࡱࡩࠤࡌࡵࡶࡦࡴࡱࡱࡪࡴࡴࠡࡤࡨࡧࡴࡳࡥࡴࠌࡧࡩࡸࡺࡲࡶࡥࡷ࡭ࡻ࡫ࠠࡰࡨࠣࡸ࡭࡫ࡳࡦࠢࡨࡲࡩࡹࠬࠡ࡫ࡷࠤ࡮ࡹࠠࡵࡪࡨࠤࡗ࡯ࡧࡩࡶࠣࡳ࡫ࠦࡴࡩࡧࠣࡔࡪࡵࡰ࡭ࡧࠣࡸࡴࠦࡡ࡭ࡶࡨࡶࠥࡵࡲࠡࡶࡲࠎࡦࡨ࡯࡭࡫ࡶ࡬ࠥ࡯ࡴ࠭ࠢࡤࡲࡩࠦࡴࡰࠢ࡬ࡲࡸࡺࡩࡵࡷࡷࡩࠥࡴࡥࡸࠢࡊࡳࡻ࡫ࡲ࡯࡯ࡨࡲࡹ࠲ࠠ࡭ࡣࡼ࡭ࡳ࡭ࠠࡪࡶࡶࠤ࡫ࡵࡵ࡯ࡦࡤࡸ࡮ࡵ࡮ࠡࡱࡱࠤࡸࡻࡣࡩࠌࡳࡶ࡮ࡴࡣࡪࡲ࡯ࡩࡸࠦࡡ࡯ࡦࠣࡳࡷ࡭ࡡ࡯࡫ࡽ࡭ࡳ࡭ࠠࡪࡶࡶࠤࡵࡵࡷࡦࡴࡶࠤ࡮ࡴࠠࡴࡷࡦ࡬ࠥ࡬࡯ࡳ࡯࠯ࠤࡦࡹࠠࡵࡱࠣࡸ࡭࡫࡭ࠡࡵ࡫ࡥࡱࡲࠠࡴࡧࡨࡱࠥࡳ࡯ࡴࡶࠍࡰ࡮ࡱࡥ࡭ࡻࠣࡸࡴࠦࡥࡧࡨࡨࡧࡹࠦࡴࡩࡧ࡬ࡶ࡙ࠥࡡࡧࡧࡷࡽࠥࡧ࡮ࡥࠢࡋࡥࡵࡶࡩ࡯ࡧࡶࡷ࠳ࠐࠢࠣࠤ᝞"))
class l1l11111lll_Krypto_ (l1lll111111_Krypto_.TestCase):
    def runTest(self):
        l1l1111_Krypto_ (u"࡙ࠧࡩ࡮ࡲ࡯ࡩࠥࡺࡥࡴࡶࠣࡳ࡫ࠦࡁ࡭࡮ࡒࡶࡓࡵࡴࡩ࡫ࡱ࡫ࠧ᝟")
        from l111ll1_Krypto_.l11111l_Krypto_ import l111lll_Krypto_
        import base64 as l1lll111l1_Krypto_
        for i in range(50):
            x = l1lll111ll_Krypto_.l1lll111ll_Krypto_(l111lll_Krypto_)
            l1ll1l1l1l_Krypto_ = x.digest(text)
            y = l1lll111ll_Krypto_.l1lll111ll_Krypto_(l111lll_Krypto_)
            l1l11111l1l_Krypto_ = y.l1ll1llll1_Krypto_(l1ll1l1l1l_Krypto_)
            self.assertEqual(text, l1l11111l1l_Krypto_)
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    return [l1l11111lll_Krypto_()]
if __name__ == l1l1111_Krypto_ (u"ࠨ࡟ࡠ࡯ࡤ࡭ࡳࡥ࡟ࠣᝠ"):
    l1lll111111_Krypto_.main()