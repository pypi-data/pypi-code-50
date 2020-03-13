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
l1l1111_Krypto_ (u"ࠧࠨࠢࡓࡕࡄࠤࡩ࡯ࡧࡪࡶࡤࡰࠥࡹࡩࡨࡰࡤࡸࡺࡸࡥࠡࡲࡵࡳࡹࡵࡣࡰ࡮ࠣࡻ࡮ࡺࡨࠡࡣࡳࡴࡪࡴࡤࡪࡺࠣࡥࡨࡩ࡯ࡳࡦ࡬ࡲ࡬ࠦࡴࡰࠢࡓࡏࡈ࡙ࠊࠋࡕࡨࡩࠥࡘࡆࡄ࠵࠷࠸࠼ࡥ࡟ࠡࡱࡵࠤࡹ࡮ࡥࠡࡢࡲࡶ࡮࡭ࡩ࡯ࡣ࡯ࠤࡗ࡙ࡁࠡࡎࡤࡦࡸࠦࡳࡱࡧࡦ࡭࡫࡯ࡣࡢࡶ࡬ࡳࡳࡦ࡟ࡠ࠰ࠍࠎ࡙࡮ࡩࡴࠢࡶࡧ࡭࡫࡭ࡦࠢ࡬ࡷࠥࡳ࡯ࡳࡧࠣࡴࡷࡵࡰࡦࡴ࡯ࡽࠥࡩࡡ࡭࡮ࡨࡨࠥࡦࡠࡓࡕࡄࡗࡘࡇ࠭ࡑࡕࡖࡤࡥ࠴ࠊࠋࡈࡲࡶࠥ࡫ࡸࡢ࡯ࡳࡰࡪ࠲ࠠࡢࠢࡶࡩࡳࡪࡥࡳࠢࡰࡥࡾࠦࡡࡶࡶ࡫ࡩࡳࡺࡩࡤࡣࡷࡩࠥࡧࠠ࡮ࡧࡶࡷࡦ࡭ࡥࠡࡷࡶ࡭ࡳ࡭ࠠࡔࡊࡄ࠱࠶ࠦࡡ࡯ࡦࠣࡔࡘ࡙ࠠ࡭࡫࡮ࡩࠏࡺࡨࡪࡵ࠽ࠎࠏࠦࠠࠡࠢࡁࡂࡃࠦࡦࡳࡱࡰࠤࡈࡸࡹࡱࡶࡲ࠲ࡘ࡯ࡧ࡯ࡣࡷࡹࡷ࡫ࠠࡪ࡯ࡳࡳࡷࡺࠠࡑࡍࡆࡗ࠶ࡥࡐࡔࡕࠍࠤࠥࠦࠠ࠿ࡀࡁࠤ࡫ࡸ࡯࡮ࠢࡆࡶࡾࡶࡴࡰ࠰ࡋࡥࡸ࡮ࠠࡪ࡯ࡳࡳࡷࡺࠠࡔࡊࡄࠎࠥࠦࠠࠡࡀࡁࡂࠥ࡬ࡲࡰ࡯ࠣࡇࡷࡿࡰࡵࡱ࠱ࡔࡺࡨ࡬ࡪࡥࡎࡩࡾࠦࡩ࡮ࡲࡲࡶࡹࠦࡒࡔࡃࠍࠤࠥࠦࠠ࠿ࡀࡁࠤ࡫ࡸ࡯࡮ࠢࡆࡶࡾࡶࡴࡰࠢ࡬ࡱࡵࡵࡲࡵࠢࡕࡥࡳࡪ࡯࡮ࠌࠣࠤࠥࠦ࠾࠿ࡀࠍࠤࠥࠦࠠ࠿ࡀࡁࠤࡲ࡫ࡳࡴࡣࡪࡩࠥࡃࠠࠨࡖࡲࠤࡧ࡫ࠠࡴ࡫ࡪࡲࡪࡪࠧࠋࠢࠣࠤࠥࡄ࠾࠿ࠢ࡮ࡩࡾࠦ࠽ࠡࡔࡖࡅ࠳࡯࡭ࡱࡱࡵࡸࡐ࡫ࡹࠩࡱࡳࡩࡳ࠮ࠧࡱࡴ࡬ࡺࡰ࡫ࡹ࠯ࡦࡨࡶࠬ࠯࠮ࡳࡧࡤࡨ࠭࠯ࠩࠋࠢࠣࠤࠥࡄ࠾࠿ࠢ࡫ࠤࡂࠦࡓࡉࡃ࠱ࡲࡪࡽࠨࠪࠌࠣࠤࠥࠦ࠾࠿ࡀࠣ࡬࠳ࡻࡰࡥࡣࡷࡩ࠭ࡳࡥࡴࡵࡤ࡫ࡪ࠯ࠊࠡࠢࠣࠤࡃࡄ࠾ࠡࡵ࡬࡫ࡳ࡫ࡲࠡ࠿ࠣࡔࡐࡉࡓ࠲ࡡࡓࡗࡘ࠴࡮ࡦࡹࠫ࡯ࡪࡿࠩࠋࠢࠣࠤࠥࡄ࠾࠿ࠢࡶ࡭࡬ࡴࡡࡵࡷࡵࡩࠥࡃࠠࡑࡍࡆࡗ࠶ࡥࡐࡔࡕ࠱ࡷ࡮࡭࡮ࠩ࡭ࡨࡽ࠮ࠐࠊࡂࡶࠣࡸ࡭࡫ࠠࡳࡧࡦࡩ࡮ࡼࡥࡳࠢࡶ࡭ࡩ࡫ࠬࠡࡸࡨࡶ࡮࡬ࡩࡤࡣࡷ࡭ࡴࡴࠠࡤࡣࡱࠤࡧ࡫ࠠࡥࡱࡱࡩࠥࡲࡩ࡬ࡧࠣࡹࡸ࡯࡮ࡨࠢࡷ࡬ࡪࠦࡰࡶࡤ࡯࡭ࡨࠦࡰࡢࡴࡷࠤࡴ࡬ࠊࡵࡪࡨࠤࡗ࡙ࡁࠡ࡭ࡨࡽ࠿ࠐࠊࠡࠢࠣࠤࡃࡄ࠾ࠡ࡭ࡨࡽࠥࡃࠠࡓࡕࡄ࠲࡮ࡳࡰࡰࡴࡷࡏࡪࡿࠨࡰࡲࡨࡲ࠭࠭ࡰࡶࡤ࡮ࡩࡾ࠴ࡤࡦࡴࠪ࠭࠳ࡸࡥࡢࡦࠫ࠭࠮ࠐࠠࠡࠢࠣࡂࡃࡄࠠࡩࠢࡀࠤࡘࡎࡁ࠯ࡰࡨࡻ࠭࠯ࠊࠡࠢࠣࠤࡃࡄ࠾ࠡࡪ࠱ࡹࡵࡪࡡࡵࡧࠫࡱࡪࡹࡳࡢࡩࡨ࠭ࠏࠦࠠࠡࠢࡁࡂࡃࠦࡶࡦࡴ࡬ࡪ࡮࡫ࡲࠡ࠿ࠣࡔࡐࡉࡓ࠲ࡡࡓࡗࡘ࠴࡮ࡦࡹࠫ࡯ࡪࡿࠩࠋࠢࠣࠤࠥࡄ࠾࠿ࠢ࡬ࡪࠥࡼࡥࡳ࡫ࡩ࡭ࡪࡸ࠮ࡷࡧࡵ࡭࡫ࡿࠨࡩ࠮ࠣࡷ࡮࡭࡮ࡢࡶࡸࡶࡪ࠯࠺ࠋࠢࠣࠤࠥࡄ࠾࠿ࠢࠣࠤࠥࠦࡰࡳ࡫ࡱࡸࠥࠨࡔࡩࡧࠣࡷ࡮࡭࡮ࡢࡶࡸࡶࡪࠦࡩࡴࠢࡤࡹࡹ࡮ࡥ࡯ࡶ࡬ࡧ࠳ࠨࠊࠡࠢࠣࠤࡃࡄ࠾ࠡࡧ࡯ࡷࡪࡀࠊࠡࠢࠣࠤࡃࡄ࠾ࠡࠢࠣࠤࠥࡶࡲࡪࡰࡷࠤ࡚ࠧࡨࡦࠢࡶ࡭࡬ࡴࡡࡵࡷࡵࡩࠥ࡯ࡳࠡࡰࡲࡸࠥࡧࡵࡵࡪࡨࡲࡹ࡯ࡣ࠯ࠤࠍࠎ࠿ࡻ࡮ࡥࡱࡦࡹࡲ࡫࡮ࡵࡧࡧ࠾ࠥࡥ࡟ࡳࡧࡹ࡭ࡸ࡯࡯࡯ࡡࡢ࠰ࠥࡥ࡟ࡱࡣࡦ࡯ࡦ࡭ࡥࡠࡡࠍࠎ࠳࠴ࠠࡠࡡ࠽ࠤ࡭ࡺࡴࡱ࠼࠲࠳ࡼࡽࡷ࠯࡫ࡨࡸ࡫࠴࡯ࡳࡩ࠲ࡶ࡫ࡩ࠯ࡳࡨࡦ࠷࠹࠺࠷࠯ࡶࡻࡸࠏ࠴࠮ࠡࡡࡢ࠾ࠥ࡮ࡴࡵࡲ࠽࠳࠴ࡽࡷࡸ࠰ࡵࡷࡦ࠴ࡣࡰ࡯࠲ࡶࡸࡧ࡬ࡢࡤࡶ࠳ࡳࡵࡤࡦ࠰ࡤࡷࡵࡅࡩࡥ࠿࠵࠵࠷࠻ࠊࠣࠤࠥᨔ")
__revision__ = l1l1111_Krypto_ (u"ࠨࠤࡊࡦࠧࠦᨕ")
__all__ = [ l1l1111_Krypto_ (u"ࠧ࡯ࡧࡺࠫᨖ"), l1l1111_Krypto_ (u"ࠨࡒࡖࡗࡤ࡙ࡩࡨࡕࡦ࡬ࡪࡳࡥࠨᨗ") ]
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
if sys.version_info[0] == 2 and sys.version_info[1] == 1:
    from l111ll1_Krypto_.l1l111ll_Krypto_.l1l1ll1l_Krypto_ import *
import l111ll1_Krypto_.l1l111ll_Krypto_.l111l1ll_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l111l1ll_Krypto_ import l1llll11lll_Krypto_, l1ll11111_Krypto_, l1ll1lllll_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l1ll1ll11_Krypto_ import l1ll1ll11_Krypto_
class l1llll1l111l_Krypto_:
    l1l1111_Krypto_ (u"ࠤ࡙ࠥࠦ࡮ࡩࡴࠢࡶ࡭࡬ࡴࡡࡵࡷࡵࡩࠥࡹࡣࡩࡧࡰࡩࠥࡩࡡ࡯ࠢࡳࡩࡷ࡬࡯ࡳ࡯ࠣࡔࡐࡉࡓࠋࠌࠣࠤࠥࠦࡤࡦࡨࠣࡣࡤ࡯࡮ࡪࡶࡢࡣ࠭ࡹࡥ࡭ࡨ࠯ࠤࡰ࡫ࡹ࠭ࠢࡰ࡫࡫ࡻ࡮ࡤ࠮ࠣࡷࡦࡲࡴࡍࡧࡱ࠭࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤᨘࠥ")l1l1ll1l1_Krypto_ this l1l111l11_Krypto_
        :l11lllll1_Krypto_:
         key : l1lllllll_Krypto_ l1l11lll1_Krypto_ key object
                l1ll111l1_Krypto_ a l1l111ll1_Krypto_ l11ll1ll1_Krypto_ is given, l1lll11l1_Krypto_ signature and l1llll1llll1_Krypto_ l1ll1l1l1_Krypto_ possible.
                l1ll111l1_Krypto_ a l1llll1ll_Krypto_ l11ll1ll1_Krypto_ is given, l111ll11_Krypto_ l1llll1llll1_Krypto_ is possible.
         l1l1lllll_Krypto_ : callable
                A mask l1111l1l_Krypto_ function that l1l1lll11_Krypto_ l11ll1l1l_Krypto_ parameters: a string l111l11l_Krypto_
                l1l11l11l_Krypto_ as l1ll1111l_Krypto_, and l11lll11l_Krypto_ l1l1l1111_Krypto_ l11111ll_Krypto_ l11lll11l_Krypto_ mask l111l11l_Krypto_ l1llllll1_Krypto_, in bytes.
         l111l11lll1_Krypto_ : int
                l1llllllll11_Krypto_ l11111ll_Krypto_ l11lll11l_Krypto_ l1l1l111ll_Krypto_, in bytes.
        l1l1111_Krypto_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡴࡧ࡯ࡪ࠳ࡥ࡫ࡦࡻࠣࡁࠥࡱࡥࡺࠌࠣࠤࠥࠦࠠࠡࠢࠣࡷࡪࡲࡦ࠯ࡡࡶࡥࡱࡺࡌࡦࡰࠣࡁࠥࡹࡡ࡭ࡶࡏࡩࡳࠐࠠࠡࠢࠣࠤࠥࠦࠠࡴࡧ࡯ࡪ࠳ࡥ࡭ࡨࡨࡸࡲࡨࠦ࠽ࠡ࡯ࡪࡪࡺࡴࡣࠋࠌࠣࠤࠥࠦࡤࡦࡨࠣࡧࡦࡴ࡟ࡴ࡫ࡪࡲ࠭ࡹࡥ࡭ࡨࠬ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᨙ")l1lll11ll_Krypto_ True if this l1llll11l_Krypto_ object l1l1l111l_Krypto_ l1llll1l1_Krypto_ l1l11l1ll_Krypto_ for l1lllll1llll_Krypto_ l1lllll1111l_Krypto_.l1l1111_Krypto_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡴࡨࡸࡺࡸ࡮ࠡࡵࡨࡰ࡫࠴࡟࡬ࡧࡼ࠲࡭ࡧࡳࡠࡲࡵ࡭ࡻࡧࡴࡦࠪࠬࠎࠥࠐࠠࠡࠢࠣࡨࡪ࡬ࠠࡴ࡫ࡪࡲ࠭ࡹࡥ࡭ࡨ࠯ࠤࡲ࡮ࡡࡴࡪࠬ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᨚ")l1l1l1l1l_Krypto_ l11lll11l_Krypto_ l1l111l11_Krypto_
        l1l1111l1_Krypto_ function is named ``l1111111l11_Krypto_-l1llllll1lll_Krypto_-l1llll1ll111_Krypto_``, and is l111llll_Krypto_ in
        section 8.1.1 l11111ll_Krypto_ l1llll111_Krypto_.
        :l11lllll1_Krypto_:
         l1lllll1ll11_Krypto_ : hash object
                l1l11ll11_Krypto_ hash that l111l1ll1_Krypto_ l11ll111l_Krypto_ out l1llll1lll11_Krypto_ l11lll11l_Krypto_ message. l1l1111l1_Krypto_ is l1lllllll_Krypto_ object
                l1111111111_Krypto_ l111l11l_Krypto_ l11lll11l_Krypto_ `l111ll1_Krypto_.l1lll1ll1_Krypto_` module.
        :l1lll11ll_Krypto_: l1l11ll11_Krypto_ l1llllll1lll_Krypto_ signature encoded as a string.
        :l1l111l1l_Krypto_ ValueError:
            l1ll111l1_Krypto_ l11lll11l_Krypto_ l1l11lll1_Krypto_ key length is not l11l1l11_Krypto_ l1lllll11_Krypto_ l111l11l_Krypto_ l1ll1lll1_Krypto_ with l11lll11l_Krypto_ given
            hash l1lllll11lll_Krypto_.
        :l1l111l1l_Krypto_ TypeError:
            l1ll111l1_Krypto_ l11lll11l_Krypto_ l1l11lll1_Krypto_ key l111l1l1_Krypto_ l1ll11l11_Krypto_ l1l111ll1_Krypto_ l11ll1ll1_Krypto_.
        :l1111l11_Krypto_: l11lll1ll_Krypto_ l11lll11l_Krypto_ l1l1l111ll_Krypto_ length and l11lll11l_Krypto_ mask l1111l1l_Krypto_ function l111ll11_Krypto_
                    if l1l11111l_Krypto_ l1111ll1_Krypto_ l11lll111_Krypto_ l1l11111l_Krypto_ l1ll1l1l1_Krypto_ l1l1ll11l_Krypto_.
                    l1l11ll11_Krypto_ l11l1111_Krypto_ l1l1l1ll1_Krypto_ l1l11l11l_Krypto_ l11lll11l_Krypto_ l111l111_Krypto_ parameters l1llll1l1l1l_Krypto_.
        l1l1111_Krypto_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢࡵࡥࡳࡪࡦࡶࡰࡦࠤࡂࠦࡳࡦ࡮ࡩ࠲ࡤࡱࡥࡺ࠰ࡢࡶࡦࡴࡤࡧࡷࡱࡧࠏࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣ࡭࡫ࠦࡳࡦ࡮ࡩ࠲ࡤࡹࡡ࡭ࡶࡏࡩࡳࠦ࠽࠾ࠢࡑࡳࡳ࡫࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡳࡍࡧࡱࠤࡂࠦ࡭ࡩࡣࡶ࡬࠳ࡪࡩࡨࡧࡶࡸࡤࡹࡩࡻࡧࠍࠤࠥࠦࠠࠡࠢࠣࠤࡪࡲࡳࡦ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡵࡏࡩࡳࠦ࠽ࠡࡵࡨࡰ࡫࠴࡟ࡴࡣ࡯ࡸࡑ࡫࡮ࠋࠢࠣࠤࠥࠦࠠࠡࠢ࡬ࡪࠥࡹࡥ࡭ࡨ࠱ࡣࡲ࡭ࡦࡶࡰࡦ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡱ࡬࡬ࠠ࠾ࠢࡶࡩࡱ࡬࠮ࡠ࡯ࡪࡪࡺࡴࡣࠋࠢࠣࠤࠥࠦࠠࠡࠢࡨࡰࡸ࡫࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࡮ࡩࡩࠤࠥࡃࠠ࡭ࡣࡰࡦࡩࡧࠠࡹ࠮ࡼ࠾ࠥࡓࡇࡇ࠳ࠫࡼ࠱ࡿࠬ࡮ࡪࡤࡷ࡭࠯ࠊࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࡱࡴࡪࡂࡪࡶࡶࠤࡂࠦࡃࡳࡻࡳࡸࡴ࠴ࡕࡵ࡫࡯࠲ࡳࡻ࡭ࡣࡧࡵ࠲ࡸ࡯ࡺࡦࠪࡶࡩࡱ࡬࠮ࡠ࡭ࡨࡽ࠳ࡴࠩࠋࠢࠣࠤࠥࠐࠠࠡࠢࠣࠤࠥࠦࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢ࡮ࠤࡂࠦࡣࡦ࡫࡯ࡣࡩ࡯ࡶࠩ࡯ࡲࡨࡇ࡯ࡴࡴ࠮࠻࠭ࠥࠐࠠࠡࠢࠣࠤࠥࠦࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢࡨࡱࠥࡃࠠࡆࡏࡖࡅࡤࡖࡓࡔࡡࡈࡒࡈࡕࡄࡆࠪࡰ࡬ࡦࡹࡨ࠭ࠢࡰࡳࡩࡈࡩࡵࡵ࠰࠵࠱ࠦࡲࡢࡰࡧࡪࡺࡴࡣ࠭ࠢࡰ࡫࡫࠲ࠠࡴࡎࡨࡲ࠮ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢࡰࠤࡂࠦࡳࡦ࡮ࡩ࠲ࡤࡱࡥࡺ࠰ࡧࡩࡨࡸࡹࡱࡶࠫࡩࡲ࠯ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࡗࠥࡃࠠࡣࡥ࡫ࡶ࠭࠶ࡸ࠱࠲ࠬ࠮࠭ࡱ࠭࡭ࡧࡱࠬࡲ࠯ࠩࠡ࠭ࠣࡱࠏࠦࠠࠡࠢࠣࠤࠥࠦࡲࡦࡶࡸࡶࡳࠦࡓࠋࠢࠣࠤࠥࠐࠠࠡࠢࠣࡨࡪ࡬ࠠࡷࡧࡵ࡭࡫ࡿࠨࡴࡧ࡯ࡪ࠱ࠦ࡭ࡩࡣࡶ࡬࠱ࠦࡓࠪ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᨛ")l1lllll11111_Krypto_ that a l1llll1ll1ll_Krypto_ l1l111l11_Krypto_
        l1l1111l1_Krypto_ function l111111l111_Krypto_ if l11lll11l_Krypto_ l11l1111l_Krypto_ l111111llll_Krypto_ l11lll11l_Krypto_ l1l111ll1_Krypto_ l11ll1ll1_Krypto_ l11111ll_Krypto_ l11lll11l_Krypto_ given
        l1l11lll1_Krypto_ key l111l1l1_Krypto_ l1llllll11l1_Krypto_ l1llll1l1lll_Krypto_ l11lll11l_Krypto_ message.
        l1l1111l1_Krypto_ function is l1llllll1ll1_Krypto_ ``l1111111l11_Krypto_-l1llllll1lll_Krypto_-l1llll1lll1l_Krypto_``, and is l111llll_Krypto_ in section
        8.1.2 l11111ll_Krypto_ l1llll111_Krypto_.
        :l11lllll1_Krypto_:
         l1lllll1ll11_Krypto_ : hash object
                l1l11ll11_Krypto_ hash that l111l1ll1_Krypto_ l11ll111l_Krypto_ out l1llll1lll11_Krypto_ l11lll11l_Krypto_ message. l1l1111l1_Krypto_ is l1lllllll_Krypto_ object
                l1111111111_Krypto_ l111l11l_Krypto_ l11lll11l_Krypto_ `l111ll1_Krypto_.l1lll1ll1_Krypto_` module.
         S : string
                l1l11ll11_Krypto_ signature that l1llllll11ll_Krypto_ l111l11l_Krypto_ l1llll1l1_Krypto_ l1lllll1l1ll_Krypto_.
        :l1lll11ll_Krypto_: True if l1llll1llll1_Krypto_ is l111111l1ll_Krypto_. False l111111ll11_Krypto_.
        l1l1111_Krypto_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࠎࠥࠦࠠࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࠎࠥࠦࠠࠡࠢࠣࠤࠥ࡯ࡦࠡࡵࡨࡰ࡫࠴࡟ࡴࡣ࡯ࡸࡑ࡫࡮ࠡ࠿ࡀࠤࡓࡵ࡮ࡦ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡵࡏࡩࡳࠦ࠽ࠡ࡯࡫ࡥࡸ࡮࠮ࡥ࡫ࡪࡩࡸࡺ࡟ࡴ࡫ࡽࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࡥ࡭ࡵࡨ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡷࡑ࡫࡮ࠡ࠿ࠣࡷࡪࡲࡦ࠯ࡡࡶࡥࡱࡺࡌࡦࡰࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡮࡬ࠠࡴࡧ࡯ࡪ࠳ࡥ࡭ࡨࡨࡸࡲࡨࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡳࡧࡧࠢࡀࠤࡸ࡫࡬ࡧ࠰ࡢࡱ࡬࡬ࡵ࡯ࡥࠍࠤࠥࠦࠠࠡࠢࠣࠤࡪࡲࡳࡦ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࡯ࡪࡪࠥࠦ࠽ࠡ࡮ࡤࡱࡧࡪࡡࠡࡺ࠯ࡽ࠿ࠦࡍࡈࡈ࠴ࠬࡽ࠲ࡹ࠭࡯࡫ࡥࡸ࡮ࠩࠋࠌࠣࠤࠥࠦࠠࠡࠢࠣࡱࡴࡪࡂࡪࡶࡶࠤࡂࠦࡃࡳࡻࡳࡸࡴ࠴ࡕࡵ࡫࡯࠲ࡳࡻ࡭ࡣࡧࡵ࠲ࡸ࡯ࡺࡦࠪࡶࡩࡱ࡬࠮ࡠ࡭ࡨࡽ࠳ࡴࠩࠋࠢࠣࠤࠥࠐࠠࠡࠢࠣࠤࠥࠦࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢ࡮ࠤࡂࠦࡣࡦ࡫࡯ࡣࡩ࡯ࡶࠩ࡯ࡲࡨࡇ࡯ࡴࡴ࠮࠻࠭ࠥࠐࠠࠡࠢࠣࠤࠥࠦࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢ࡬ࡪࠥࡲࡥ࡯ࠪࡖ࠭ࠥࠧ࠽ࠡ࡭࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡵࡩࡹࡻࡲ࡯ࠢࡉࡥࡱࡹࡥࠋࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࡩࡲࠦ࠽ࠡࡵࡨࡰ࡫࠴࡟࡬ࡧࡼ࠲ࡪࡴࡣࡳࡻࡳࡸ࡙࠭ࠬࠡ࠲ࠬ࡟࠵ࡣࠊࠡࠢࠣࠤࠥࠦࠠࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࡩࡲࡒࡥ࡯ࠢࡀࠤࡨ࡫ࡩ࡭ࡡࡧ࡭ࡻ࠮࡭ࡰࡦࡅ࡭ࡹࡹ࠭࠲࠮࠻࠭ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡥ࡮ࠢࡀࠤࡧࡩࡨࡳࠪ࠳ࡼ࠵࠶ࠩࠫࠪࡨࡱࡑ࡫࡮࠮࡮ࡨࡲ࠭࡫࡭ࠪࠫࠣ࠯ࠥ࡫࡭ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤࡹࡸࡹ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡳࡧࡶࡹࡱࡺࠠ࠾ࠢࡈࡑࡘࡇ࡟ࡑࡕࡖࡣ࡛ࡋࡒࡊࡈ࡜ࠬࡲ࡮ࡡࡴࡪ࠯ࠤࡪࡳࠬࠡ࡯ࡲࡨࡇ࡯ࡴࡴ࠯࠴࠰ࠥࡳࡧࡧ࠮ࠣࡷࡑ࡫࡮ࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࡩࡽࡩࡥࡱࡶ࡚ࠣࡦࡲࡵࡦࡇࡵࡶࡴࡸ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡲࡦࡶࡸࡶࡳࠦࡆࡢ࡮ࡶࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࡴࡨࡸࡺࡸ࡮ࠡࡴࡨࡷࡺࡲࡴࠋࠢࠣࠤࠥࠐࡤࡦࡨࠣࡑࡌࡌ࠱ࠩ࡯ࡪࡪࡘ࡫ࡥࡥ࠮ࠣࡱࡦࡹ࡫ࡍࡧࡱ࠰ࠥ࡮ࡡࡴࡪࠬ࠾ࠏࠦࠠࠡࠢࠥࠦࠧ᨜")l1lllll1l11l_Krypto_ l1lllll11l11_Krypto_ l1111111lll_Krypto_, l1111111l1l_Krypto_ in B.2.1unScramble_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡕࠢࡀࠤࡧ࠮ࠢࠣࠫࠍࠤࠥࠦࠠࡧࡱࡵࠤࡨࡵࡵ࡯ࡶࡨࡶࠥ࡯࡮ࠡࡴࡤࡲ࡬࡫ࠨࡤࡧ࡬ࡰࡤࡪࡩࡷࠪࡰࡥࡸࡱࡌࡦࡰ࠯ࠤ࡭ࡧࡳࡩ࠰ࡧ࡭࡬࡫ࡳࡵࡡࡶ࡭ࡿ࡫ࠩࠪ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡨࠦ࠽ࠡ࡮ࡲࡲ࡬ࡥࡴࡰࡡࡥࡽࡹ࡫ࡳࠩࡥࡲࡹࡳࡺࡥࡳ࠮ࠣ࠸࠮ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡕࠢࡀࠤ࡙ࠦࠫࠡࡪࡤࡷ࡭࠴࡮ࡦࡹࠫࡱ࡬࡬ࡓࡦࡧࡧࠤ࠰ࠦࡣࠪ࠰ࡧ࡭࡬࡫ࡳࡵࠪࠬࠎࠥࠦࠠࠡࡣࡶࡷࡪࡸࡴࠩ࡮ࡨࡲ࡚࠭ࠩ࠿࠿ࡰࡥࡸࡱࡌࡦࡰࠬࠎࠥࠦࠠࠡࡴࡨࡸࡺࡸ࡮ࠡࡖ࡞࠾ࡲࡧࡳ࡬ࡎࡨࡲࡢࠐࠊࡥࡧࡩࠤࡊࡓࡓࡂࡡࡓࡗࡘࡥࡅࡏࡅࡒࡈࡊ࠮࡭ࡩࡣࡶ࡬࠱ࠦࡥ࡮ࡄ࡬ࡸࡸ࠲ࠠࡳࡣࡱࡨࡋࡻ࡮ࡤ࠮ࠣࡱ࡬࡬ࠬࠡࡵࡏࡩࡳ࠯࠺ࠋࠢࠣࠤࠥࠨࠢࠣ᨝")
    l1llll1l1ll1_Krypto_ l11lll11l_Krypto_ ``l1lllll1l111_Krypto_-l1llllll1lll_Krypto_-l1llll1ll11l_Krypto_`` function, as l1llll1l11l1_Krypto_
    in l1l111l11_Krypto_
    l1l11ll11_Krypto_ l1lll1111_Krypto_ ``l1lllll1l111_Krypto_-l1llllll1lll_Krypto_-l1llll1ll11l_Krypto_`` l111111lll1_Krypto_ l1l1lll11_Krypto_ l11lll11l_Krypto_ message ``M`` as input,
    and hash it l1lllllllll1_Krypto_. l111111l11l_Krypto_, l1llllll1l1l_Krypto_ l1llll1ll1l1_Krypto_ that l11lll11l_Krypto_ message l111l1l1_Krypto_ already
    l1111111ll1_Krypto_ l1llll1l1l11_Krypto_ l11111111ll_Krypto_.
    :l11lllll1_Krypto_:
     l1lllll1ll11_Krypto_ : hash object
            l1l11ll11_Krypto_ hash object that l11111111l1_Krypto_ l11lll11l_Krypto_ digest l11111ll_Krypto_ l11lll11l_Krypto_ message l1lllll11ll1_Krypto_ l1llll1l1lll_Krypto_.
     l1llllllll1l_Krypto_ : int
            l1llllll1111_Krypto_ length l11111ll_Krypto_ l11lll11l_Krypto_ final encoding, in bits.
     l1lllll1lll1_Krypto_ : callable
            l1lllll11l1l_Krypto_ l1llllllllll_Krypto_ function that l1l1lll11_Krypto_ as l111ll11_Krypto_ l1llll1l1111_Krypto_ l1lllllll_Krypto_ int, and l1lllllll11l_Krypto_
            a string l11111ll_Krypto_ l111l1l111_Krypto_ bytes, l111l11l_Krypto_ l1llll1l1_Krypto_ l1l11l1ll_Krypto_ as l1l1l111ll_Krypto_.
     l1lllll111l1_Krypto_ : callable
            A mask l1111l1l_Krypto_ function that l1l1lll11_Krypto_ l11ll1l1l_Krypto_ parameters: a string l111l11l_Krypto_
            l1l11l11l_Krypto_ as l1ll1111l_Krypto_, and l11lll11l_Krypto_ l1l1l1111_Krypto_ l11111ll_Krypto_ l11lll11l_Krypto_ mask l111l11l_Krypto_ l1llllll1_Krypto_, in bytes.
     l111l1l111l_Krypto_ : int
            l1llllllll11_Krypto_ l11111ll_Krypto_ l11lll11l_Krypto_ l1l1l111ll_Krypto_, in bytes.
    :l1lll11ll_Krypto_: l1lllll11l1l_Krypto_ ``l1lllllll1l1_Krypto_`` l1111lll1_Krypto_ l1lllll11_Krypto_ string that l111111l1l1_Krypto_ l11lll11l_Krypto_ hash
            (with ``l1lllllll1l1_Krypto_ = \ceil(l1llllllll1l_Krypto_/8)``).
    :l1l111l1l_Krypto_ ValueError:
        l111111ll1l_Krypto_ digest or l1l1l111ll_Krypto_ length l1ll1l1l1_Krypto_ l1llll1l1l1l_Krypto_ l1lllllll1ll_Krypto_.
    l1l1111_Krypto_ (u"ࠣࠤࠥࠎࠏࠦࠠࠡࠢࡨࡱࡑ࡫࡮ࠡ࠿ࠣࡧࡪ࡯࡬ࡠࡦ࡬ࡺ࠭࡫࡭ࡃ࡫ࡷࡷ࠱࠾ࠩࠋࠌࠣࠤࠥࠦࠊࠡࠢࠣࠤࡱࡳࡡࡴ࡭ࠣࡁࠥ࠶ࠊࠡࠢࠣࠤ࡫ࡵࡲࠡ࡫ࠣ࡭ࡳࠦࡲࡢࡰࡪࡩ࠭࠾ࠪࡦ࡯ࡏࡩࡳ࠳ࡥ࡮ࡄ࡬ࡸࡸ࠯࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢ࡯ࡱࡦࡹ࡫ࠡ࠿ࠣࡰࡲࡧࡳ࡬ࡀࡁ࠵ࠥࢂࠠ࠱ࡺ࠻࠴ࠏࠐࠠࠡࠢࠣࠎࠥࠦࠠࠡࠌࠣࠤࠥࠦࡩࡧࠢࡨࡱࡑ࡫࡮ࠡ࠾ࠣࡱ࡭ࡧࡳࡩ࠰ࡧ࡭࡬࡫ࡳࡵࡡࡶ࡭ࡿ࡫ࠫࡴࡎࡨࡲ࠰࠸࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡵࡥ࡮ࡹࡥࠡࡘࡤࡰࡺ࡫ࡅࡳࡴࡲࡶ࠭ࠨࡄࡪࡩࡨࡷࡹࠦ࡯ࡳࠢࡶࡥࡱࡺࠠ࡭ࡧࡱ࡫ࡹ࡮ࠠࡢࡴࡨࠤࡹࡵ࡯ࠡ࡮ࡲࡲ࡬ࠦࡦࡰࡴࠣ࡫࡮ࡼࡥ࡯ࠢ࡮ࡩࡾࠦࡳࡪࡼࡨ࠲ࠧ࠯ࠊࠡࠢࠣࠤࠏࠦࠠࠡࠢࡶࡥࡱࡺࠠ࠾ࠢࡥࠬࠧࠨࠩࠋࠢࠣࠤࠥ࡯ࡦࠡࡴࡤࡲࡩࡌࡵ࡯ࡥࠣࡥࡳࡪࠠࡴࡎࡨࡲࡃ࠶࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡶࡥࡱࡺࠠ࠾ࠢࡵࡥࡳࡪࡆࡶࡰࡦࠬࡸࡒࡥ࡯ࠫࠍࠤࠥࠦࠠࠋࠢࠣࠤࠥ࡮ࠠ࠾ࠢࡰ࡬ࡦࡹࡨ࠯ࡰࡨࡻ࠭ࡨࡣࡩࡴࠫ࠴ࡽ࠶࠰ࠪࠬ࠻ࠤ࠰ࠦ࡭ࡩࡣࡶ࡬࠳ࡪࡩࡨࡧࡶࡸ࠭࠯ࠠࠬࠢࡶࡥࡱࡺࠩࠋࠢࠣࠤࠥࠐࠠࠡࠢࠣࡨࡧࠦ࠽ࠡࡤࡦ࡬ࡷ࠮࠰ࡹ࠲࠳࠭࠯࠮ࡥ࡮ࡎࡨࡲ࠲ࡹࡌࡦࡰ࠰ࡱ࡭ࡧࡳࡩ࠰ࡧ࡭࡬࡫ࡳࡵࡡࡶ࡭ࡿ࡫࠭࠳ࠫࠣ࠯ࠥࡨࡣࡩࡴࠫ࠴ࡽ࠶࠱ࠪࠢ࠮ࠤࡸࡧ࡬ࡵࠌࠣࠤࠥࠦࠊࠡࠢࠣࠤࡩࡨࡍࡢࡵ࡮ࠤࡂࠦ࡭ࡨࡨࠫ࡬࠳ࡪࡩࡨࡧࡶࡸ࠭࠯ࠬࠡࡧࡰࡐࡪࡴ࠭࡮ࡪࡤࡷ࡭࠴ࡤࡪࡩࡨࡷࡹࡥࡳࡪࡼࡨ࠱࠶࠯ࠊࠡࠢࠣࠤࠏࠦࠠࠡࠢࡰࡥࡸࡱࡥࡥࡆࡅࠤࡂࠦࡳࡵࡴࡻࡳࡷ࠮ࡤࡣ࠮ࡧࡦࡒࡧࡳ࡬ࠫࠍࠤࠥࠦࠠࠋࠢࠣࠤࠥࡳࡡࡴ࡭ࡨࡨࡉࡈࠠ࠾ࠢࡥࡧ࡭ࡸࠨࡣࡱࡵࡨ࠭ࡳࡡࡴ࡭ࡨࡨࡉࡈ࡛࠱࡟ࠬࠤࠫࠦࡾ࡭࡯ࡤࡷࡰ࠯ࠠࠬࠢࡰࡥࡸࡱࡥࡥࡆࡅ࡟࠶ࡀ࡝ࠋࠢࠣࠤࠥࠐࠠࠡࠢࠣࡩࡲࠦ࠽ࠡ࡯ࡤࡷࡰ࡫ࡤࡅࡄࠣ࠯ࠥ࡮࠮ࡥ࡫ࡪࡩࡸࡺࠨࠪࠢ࠮ࠤࡧࡩࡨࡳࠪ࠳ࡼࡇࡉࠩࠋࠢࠣࠤࠥࡸࡥࡵࡷࡵࡲࠥ࡫࡭ࠋࠌࡧࡩ࡫ࠦࡅࡎࡕࡄࡣࡕ࡙ࡓࡠࡘࡈࡖࡎࡌ࡙ࠩ࡯࡫ࡥࡸ࡮ࠬࠡࡧࡰ࠰ࠥ࡫࡭ࡃ࡫ࡷࡷ࠱ࠦ࡭ࡨࡨ࠯ࠤࡸࡒࡥ࡯ࠫ࠽ࠎࠥࠦࠠࠡࠤࠥࠦ᨞")
    l1llll1l1ll1_Krypto_ l11lll11l_Krypto_ ``l1lllll1l111_Krypto_-l1llllll1lll_Krypto_-l1llll1lll1l_Krypto_`` function, as l1llll1l11l1_Krypto_
    in l1l111l11_Krypto_
    ``l1lllll1l111_Krypto_-l1llllll1lll_Krypto_-l1llll1lll1l_Krypto_`` l111111lll1_Krypto_ l1l1lll11_Krypto_ l11lll11l_Krypto_ message ``M`` as input,
    and hash it l1lllllllll1_Krypto_. l111111l11l_Krypto_, l1llllll1l1l_Krypto_ l1llll1ll1l1_Krypto_ that l11lll11l_Krypto_ message l111l1l1_Krypto_ already
    l1111111ll1_Krypto_ l1llll1l1l11_Krypto_ l11111111ll_Krypto_.
    :l11lllll1_Krypto_:
     l1lllll1ll11_Krypto_ : hash object
            l1l11ll11_Krypto_ hash object that l11111111l1_Krypto_ l11lll11l_Krypto_ digest l11111ll_Krypto_ l11lll11l_Krypto_ message l111l11l_Krypto_ l1llll1l1_Krypto_ l1llllll1l11_Krypto_.
     l111lll1l_Krypto_ : string
            l1l11ll11_Krypto_ signature l111l11l_Krypto_ l1l11l1l11_Krypto_, l1llllll111l_Krypto_ l111111111l_Krypto_ that l11lll11l_Krypto_ l1lllllll111_Krypto_ l1llllll11l1_Krypto_ l1llll1l1lll_Krypto_
            l11lll11l_Krypto_ message that l111l1ll1_Krypto_ l1llll1lllll_Krypto_.
     l1llllllll1l_Krypto_ : int
            l1llllllll11_Krypto_ l11111ll_Krypto_ l11lll11l_Krypto_ final encoding (l111lll1l_Krypto_), in bits.
     l1lllll111l1_Krypto_ : callable
            A mask l1111l1l_Krypto_ function that l1l1lll11_Krypto_ l11ll1l1l_Krypto_ parameters: a string l111l11l_Krypto_
            l1l11l11l_Krypto_ as l1ll1111l_Krypto_, and l11lll11l_Krypto_ l1l1l1111_Krypto_ l11111ll_Krypto_ l11lll11l_Krypto_ mask l111l11l_Krypto_ l1llllll1_Krypto_, in bytes.
     l111l1l111l_Krypto_ : int
            l1llllllll11_Krypto_ l11111ll_Krypto_ l11lll11l_Krypto_ l1l1l111ll_Krypto_, in bytes.
    :l1lll11ll_Krypto_: 0 if l11lll11l_Krypto_ encoding is l1lllll1l1l1_Krypto_, 1 if it is l1lllll111ll_Krypto_.
    :l1l111l1l_Krypto_ ValueError:
        l111111ll1l_Krypto_ digest or l1l1l111ll_Krypto_ length l1ll1l1l1_Krypto_ l1llll1l1l1l_Krypto_ l1lllllll1ll_Krypto_.
    l1l1111_Krypto_ (u"ࠤࠥࠦࠏࠐࠠࠡࠢࠣࡩࡲࡒࡥ࡯ࠢࡀࠤࡨ࡫ࡩ࡭ࡡࡧ࡭ࡻ࠮ࡥ࡮ࡄ࡬ࡸࡸ࠲࠸ࠪࠌࠍࠤࠥࠦࠠࠋࠢࠣࠤࠥࡲ࡭ࡢࡵ࡮ࠤࡂࠦ࠰ࠋࠢࠣࠤࠥ࡬࡯ࡳࠢ࡬ࠤ࡮ࡴࠠࡳࡣࡱ࡫ࡪ࠮࠸ࠫࡧࡰࡐࡪࡴ࠭ࡦ࡯ࡅ࡭ࡹࡹࠩ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡰࡲࡧࡳ࡬ࠢࡀࠤࡱࡳࡡࡴ࡭ࡁࡂ࠶ࠦࡼࠡ࠲ࡻ࠼࠵ࠐࠊࠡࠢࠣࠤࠏࠦࠠࠡࠢࠍࠤࠥࠦࠠࡪࡨࠣࡩࡲࡒࡥ࡯ࠢ࠿ࠤࡲ࡮ࡡࡴࡪ࠱ࡨ࡮࡭ࡥࡴࡶࡢࡷ࡮ࢀࡥࠬࡵࡏࡩࡳ࠱࠲࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡶࡪࡺࡵࡳࡰࠣࡊࡦࡲࡳࡦࠌࠣࠤࠥࠦࠊࠡࠢࠣࠤ࡮࡬ࠠࡰࡴࡧࠬࡪࡳ࡛࠮࠳࠽ࡡ࠮ࠧ࠽࠱ࡺࡅࡇ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡳࡧࡷࡹࡷࡴࠠࡇࡣ࡯ࡷࡪࠐࠠࠡࠢࠣࠎࠥࠦࠠࠡ࡯ࡤࡷࡰ࡫ࡤࡅࡄࠣࡁࠥ࡫࡭࡜࠼ࡨࡱࡑ࡫࡮࠮࡯࡫ࡥࡸ࡮࠮ࡥ࡫ࡪࡩࡸࡺ࡟ࡴ࡫ࡽࡩ࠲࠷࡝ࠋࠢࠣࠤࠥ࡮ࠠ࠾ࠢࡨࡱࡠ࡫࡭ࡍࡧࡱ࠱ࡲ࡮ࡡࡴࡪ࠱ࡨ࡮࡭ࡥࡴࡶࡢࡷ࡮ࢀࡥ࠮࠳࠽࠱࠶ࡣࠊࠡࠢࠣࠤࠏࠦࠠࠡࠢ࡬ࡪࠥࡲ࡭ࡢࡵ࡮ࠤࠫࠦࡢࡰࡴࡧࠬࡪࡳ࡛࠱࡟ࠬ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡲࡦࡶࡸࡶࡳࠦࡆࡢ࡮ࡶࡩࠏࠦࠠࠡࠢࠍࠤࠥࠦࠠࡥࡤࡐࡥࡸࡱࠠ࠾ࠢࡰ࡫࡫࠮ࡨ࠭ࠢࡨࡱࡑ࡫࡮࠮࡯࡫ࡥࡸ࡮࠮ࡥ࡫ࡪࡩࡸࡺ࡟ࡴ࡫ࡽࡩ࠲࠷ࠩࠋࠢࠣࠤࠥࠐࠠࠡࠢࠣࡨࡧࠦ࠽ࠡࡵࡷࡶࡽࡵࡲࠩ࡯ࡤࡷࡰ࡫ࡤࡅࡄ࠯ࠤࡩࡨࡍࡢࡵ࡮࠭ࠏࠦࠠࠡࠢࠍࠤࠥࠦࠠࡥࡤࠣࡁࠥࡨࡣࡩࡴࠫࡦࡴࡸࡤࠩࡦࡥ࡟࠵ࡣࠩࠡࠨࠣࢂࡱࡳࡡࡴ࡭ࠬࠤ࠰ࠦࡤࡣ࡝࠴࠾ࡢࠐࠠࠡࠢࠣࠎࠥࠦࠠࠡ࡫ࡩࠤࡳࡵࡴࠡࡦࡥ࠲ࡸࡺࡡࡳࡶࡶࡻ࡮ࡺࡨࠩࡤࡦ࡬ࡷ࠮࠰ࡹ࠲࠳࠭࠯࠮ࡥ࡮ࡎࡨࡲ࠲ࡳࡨࡢࡵ࡫࠲ࡩ࡯ࡧࡦࡵࡷࡣࡸ࡯ࡺࡦ࠯ࡶࡐࡪࡴ࠭࠳ࠫࠣ࠯ࠥࡨࡣࡩࡴࠫ࠴ࡽ࠶࠱ࠪࠫ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡸࡥࡵࡷࡵࡲࠥࡌࡡ࡭ࡵࡨࠎࠥࠦࠠࠡࠌࠣࠤࠥࠦࡳࡢ࡮ࡷࠤࡂࠦࡢࠩࠤࠥ࠭ࠏࠦࠠࠡࠢ࡬ࡪࠥࡹࡌࡦࡰ࠽ࠤࡸࡧ࡬ࡵࠢࡀࠤࡩࡨ࡛࠮ࡵࡏࡩࡳࡀ࡝ࠋࠢࠣࠤࠥࠐࠠࠡࠢࠣ࡬ࡵࠦ࠽ࠡ࡯࡫ࡥࡸ࡮࠮࡯ࡧࡺࠬࡧࡩࡨࡳࠪ࠳ࡼ࠵࠶ࠩࠫ࠺ࠣ࠯ࠥࡳࡨࡢࡵ࡫࠲ࡩ࡯ࡧࡦࡵࡷࠬ࠮ࠦࠫࠡࡵࡤࡰࡹ࠯࠮ࡥ࡫ࡪࡩࡸࡺࠨࠪࠌࠣࠤࠥࠦࠊࠡࠢࠣࠤ࡮࡬ࠠࡩࠣࡀ࡬ࡵࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࡴࡨࡸࡺࡸ࡮ࠡࡈࡤࡰࡸ࡫ࠊࠡࠢࠣࠤࡷ࡫ࡴࡶࡴࡱࠤ࡙ࡸࡵࡦࠌࠍࡨࡪ࡬ࠠ࡯ࡧࡺࠬࡰ࡫ࡹ࠭ࠢࡰ࡫࡫ࡻ࡮ࡤ࠿ࡑࡳࡳ࡫ࠬࠡࡵࡤࡰࡹࡒࡥ࡯࠿ࡑࡳࡳ࡫ࠩ࠻ࠌࠣࠤࠥࠦࠢࠣࠤ᨟")l1lll11ll_Krypto_ a signature l1lllll1ll1l_Krypto_ object `l1llll1l111l_Krypto_` that
    l1l1l111l_Krypto_ l1llll1l1_Krypto_ l1l11l1ll_Krypto_ l111l11l_Krypto_ l1ll1ll1l_Krypto_ l1l111l11_Krypto_
    :l11lllll1_Krypto_:
     key : l1l11lll1_Krypto_ key object
        l1l11ll11_Krypto_ key l111l11l_Krypto_ l1l11l11l_Krypto_ l111l11l_Krypto_ l1l11lll11_Krypto_ or l1l11l1l11_Krypto_ l11lll11l_Krypto_ message. l1l1111l1_Krypto_ is a `l111ll1_Krypto_.l11l11l1_Krypto_.l1l11lll1_Krypto_` object.
        l1llll1l11ll_Krypto_ is l111ll11_Krypto_ possible if *key* is a l1l111ll1_Krypto_ l1l11lll1_Krypto_ key.
     l1l1lllll_Krypto_ : callable
        A mask l1111l1l_Krypto_ function that l1l1lll11_Krypto_ l11ll1l1l_Krypto_ parameters: a string l111l11l_Krypto_
        l1l11l11l_Krypto_ as l1ll1111l_Krypto_, and l11lll11l_Krypto_ l1l1l1111_Krypto_ l11111ll_Krypto_ l11lll11l_Krypto_ mask l111l11l_Krypto_ l1llllll1_Krypto_, in bytes.
        l1ll111l1_Krypto_ not l111llll_Krypto_, l11lll11l_Krypto_ l1lllll1l_Krypto_ l1ll11lll_Krypto_ is l1l11l1ll_Krypto_.
     l111l11lll1_Krypto_ : int
        l1llllllll11_Krypto_ l11111ll_Krypto_ l11lll11l_Krypto_ l1l1l111ll_Krypto_, in bytes. l1ll111l1_Krypto_ not l111llll_Krypto_, it matches l11lll11l_Krypto_ output
        size l11111ll_Krypto_ l11lll11l_Krypto_ hash function.
    l1l1111_Krypto_ (u"ࠥࠦᨠ")"
    return l1llll1l111l_Krypto_(key, l1l1lllll_Krypto_, l111l11lll1_Krypto_)