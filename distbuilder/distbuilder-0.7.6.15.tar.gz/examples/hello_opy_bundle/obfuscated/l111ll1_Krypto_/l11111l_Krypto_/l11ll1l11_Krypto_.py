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
l1l1111_Krypto_ (u"ࠣࠤࠥࡖࡘࡇࠠࡦࡰࡦࡶࡾࡶࡴࡪࡱࡱࠤࡵࡸ࡯ࡵࡱࡦࡳࡱࠦࡡࡤࡥࡲࡶࡩ࡯࡮ࡨࠢࡷࡳࠥࡖࡋࡄࡕࠍࠎࡘ࡫ࡥࠡࡔࡉࡇ࠸࠺࠴࠸ࡡࡢࠤࡴࡸࠠࡵࡪࡨࠤࡥࡵࡲࡪࡩ࡬ࡲࡦࡲࠠࡓࡕࡄࠤࡑࡧࡢࡴࠢࡶࡴࡪࡩࡩࡧ࡫ࡦࡥࡹ࡯࡯࡯ࡢࡢࡣࠥ࠴ࠊࠋࡖ࡫࡭ࡸࠦࡳࡤࡪࡨࡱࡪࠦࡩࡴࠢࡰࡳࡷ࡫ࠠࡱࡴࡲࡴࡪࡸ࡬ࡺࠢࡦࡥࡱࡲࡥࡥࠢࡣࡤࡗ࡙ࡁࡆࡕ࠰ࡔࡐࡉࡓ࠲࠯ࡹ࠵ࡤ࠻ࡠࡡ࠰ࠍࠎ࠯࠰ࡉࡧࠢࡼࡳࡺࠦࡡࡳࡧࠣࡨࡪࡹࡩࡨࡰ࡬ࡲ࡬ࠦࡡࠡࡰࡨࡻࠥࡶࡲࡰࡶࡲࡧࡴࡲࠬࠡࡥࡲࡲࡸ࡯ࡤࡦࡴࠣࡹࡸ࡯࡮ࡨࠢࡷ࡬ࡪࠦ࡭ࡰࡴࡨࠤࡷࡵࡢࡶࡵࡷࠤࡕࡑࡃࡔࠌࠍࡅࡸࠦࡡ࡯ࠢࡨࡼࡦࡳࡰ࡭ࡧ࠯ࠤࡦࠦࡳࡦࡰࡧࡩࡷࠦ࡭ࡢࡻࠣࡩࡳࡩࡲࡺࡲࡷࠤࡦࠦ࡭ࡦࡵࡶࡥ࡬࡫ࠠࡪࡰࠣࡸ࡭࡯ࡳࠡࡹࡤࡽ࠿ࠐࠊࠡࠢࠣࠤࠥࠦࠠࠡࡀࡁࡂࠥ࡬ࡲࡰ࡯ࠣࡇࡷࡿࡰࡵࡱ࠱ࡇ࡮ࡶࡨࡦࡴࠣ࡭ࡲࡶ࡯ࡳࡶࠣࡔࡐࡉࡓ࠲ࡡࡹ࠵ࡤ࠻ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡀࡁࡂࠥ࡬ࡲࡰ࡯ࠣࡇࡷࡿࡰࡵࡱ࠱ࡔࡺࡨ࡬ࡪࡥࡎࡩࡾࠦࡩ࡮ࡲࡲࡶࡹࠦࡒࡔࡃࠍࠤࠥࠦࠠࠡࠢࠣࠤࡃࡄ࠾ࠡࡨࡵࡳࡲࠦࡃࡳࡻࡳࡸࡴ࠴ࡈࡢࡵ࡫ࠤ࡮ࡳࡰࡰࡴࡷࠤࡘࡎࡁࠋࠢࠣࠤࠥࠦࠠࠡࠢࡁࡂࡃࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠿ࡀࡁࠤࡲ࡫ࡳࡴࡣࡪࡩࠥࡃࠠࠨࡖࡲࠤࡧ࡫ࠠࡦࡰࡦࡶࡾࡶࡴࡦࡦࠪࠎࠥࠦࠠࠡࠢࠣࠤࠥࡄ࠾࠿ࠢ࡫ࠤࡂࠦࡓࡉࡃ࠱ࡲࡪࡽࠨ࡮ࡧࡶࡷࡦ࡭ࡥࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࡂࡃࡄࠊࠡࠢࠣࠤࠥࠦࠠࠡࡀࡁࡂࠥࡱࡥࡺࠢࡀࠤࡗ࡙ࡁ࠯࡫ࡰࡴࡴࡸࡴࡌࡧࡼࠬࡴࡶࡥ࡯ࠪࠪࡴࡺࡨ࡫ࡦࡻ࠱ࡨࡪࡸࠧࠪ࠰ࡵࡩࡦࡪࠨࠪࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࡃࡄ࠾ࠡࡥ࡬ࡴ࡭࡫ࡲࠡ࠿ࠣࡔࡐࡉࡓ࠲ࡡࡹ࠵ࡤ࠻࠮࡯ࡧࡺࠬࡰ࡫ࡹࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࡂࡃࡄࠠࡤ࡫ࡳ࡬ࡪࡸࡴࡦࡺࡷࠤࡂࠦࡣࡪࡲ࡫ࡩࡷ࠴ࡥ࡯ࡥࡵࡽࡵࡺࠨ࡮ࡧࡶࡷࡦ࡭ࡥࠬࡪ࠱ࡨ࡮࡭ࡥࡴࡶࠫ࠭࠮ࠐࠊࡂࡶࠣࡸ࡭࡫ࠠࡳࡧࡦࡩ࡮ࡼࡥࡳࠢࡶ࡭ࡩ࡫ࠬࠡࡦࡨࡧࡷࡿࡰࡵ࡫ࡲࡲࠥࡩࡡ࡯ࠢࡥࡩࠥࡪ࡯࡯ࡧࠣࡹࡸ࡯࡮ࡨࠢࡷ࡬ࡪࠦࡰࡳ࡫ࡹࡥࡹ࡫ࠠࡱࡣࡵࡸࠥࡵࡦࠋࡶ࡫ࡩࠥࡘࡓࡂࠢ࡮ࡩࡾࡀࠊࠋࠢࠣࠤࠥࠦࠠࠡࠢࡁࡂࡃࠦࡆࡳࡱࡰࠤࡈࡸࡹࡱࡶࡲ࠲ࡍࡧࡳࡩࠢ࡬ࡱࡵࡵࡲࡵࠢࡖࡌࡆࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠿ࡀࡁࠤ࡫ࡸ࡯࡮ࠢࡆࡶࡾࡶࡴࡰࠢ࡬ࡱࡵࡵࡲࡵࠢࡕࡥࡳࡪ࡯࡮ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡂࡃࡄࠊࠡࠢࠣࠤࠥࠦࠠࠡࡀࡁࡂࠥࡱࡥࡺࠢࡀࠤࡗ࡙ࡁ࠯࡫ࡰࡴࡴࡸࡴࡌࡧࡼࠬࡴࡶࡥ࡯ࠪࠪࡴࡷ࡯ࡶ࡬ࡧࡼ࠲ࡩ࡫ࡲࠨࠫ࠱ࡶࡪࡧࡤࠩࠫࠬࠎࠥࠦࠠࠡࠢࠣࠤࠥࡄ࠾࠿ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡂࡃࡄࠠࡥࡵ࡬ࡾࡪࠦ࠽ࠡࡕࡋࡅ࠳ࡪࡩࡨࡧࡶࡸࡤࡹࡩࡻࡧࠍࠤࠥࠦࠠࠡࠢࠣࠤࡃࡄ࠾ࠡࡵࡨࡲࡹ࡯࡮ࡦ࡮ࠣࡁࠥࡘࡡ࡯ࡦࡲࡱ࠳ࡴࡥࡸࠪࠬ࠲ࡷ࡫ࡡࡥࠪ࠴࠹࠰ࡪࡳࡪࡼࡨ࠭ࠥࠦࠠࠡࠢࠣࠎࠥࠦࠠࠡࠢࠣࠤࠥࡄ࠾࠿ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡂࡃࡄࠠࡤ࡫ࡳ࡬ࡪࡸࠠ࠾ࠢࡓࡏࡈ࡙࠱ࡠࡸ࠴ࡣ࠺࠴࡮ࡦࡹࠫ࡯ࡪࡿࠩࠋࠢࠣࠤࠥࠦࠠࠡࠢࡁࡂࡃࠦ࡭ࡦࡵࡶࡥ࡬࡫ࠠ࠾ࠢࡦ࡭ࡵ࡮ࡥࡳ࠰ࡧࡩࡨࡸࡹࡱࡶࠫࡧ࡮ࡶࡨࡦࡴࡷࡩࡽࡺࠬࠡࡵࡨࡲࡹ࡯࡮ࡦ࡮ࠬࠎࠥࠦࠠࠡࠢࠣࠤࠥࡄ࠾࠿ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡂࡃࡄࠠࡥ࡫ࡪࡩࡸࡺࠠ࠾ࠢࡖࡌࡆ࠴࡮ࡦࡹࠫࡱࡪࡹࡳࡢࡩࡨ࡟࠿࠳ࡤࡴ࡫ࡽࡩࡢ࠯࠮ࡥ࡫ࡪࡩࡸࡺࠨࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࡂࡃࡄࠠࡪࡨࠣࡨ࡮࡭ࡥࡴࡶࡀࡁࡲ࡫ࡳࡴࡣࡪࡩࡠ࠳ࡤࡴ࡫ࡽࡩ࠿ࡣ࠺ࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤࡃࡄ࠾ࠡࠢࠣࠤࠥࡶࡲࡪࡰࡷࠤࠧࡋ࡮ࡤࡴࡼࡴࡹ࡯࡯࡯ࠢࡺࡥࡸࠦࡣࡰࡴࡵࡩࡨࡺ࠮ࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡂࡃࡄࠠࡦ࡮ࡶࡩ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠿ࡀࡁࠤࠥࠦࠠࠡࡲࡵ࡭ࡳࡺࠠࠣࡇࡱࡧࡷࡿࡰࡵ࡫ࡲࡲࠥࡽࡡࡴࠢࡱࡳࡹࠦࡣࡰࡴࡵࡩࡨࡺ࠮ࠣࠌࠍ࠾ࡺࡴࡤࡰࡥࡸࡱࡪࡴࡴࡦࡦ࠽ࠤࡤࡥࡲࡦࡸ࡬ࡷ࡮ࡵ࡮ࡠࡡ࠯ࠤࡤࡥࡰࡢࡥ࡮ࡥ࡬࡫࡟ࡠࠌࠍ࠲࠳ࠦ࡟ࡠ࠼ࠣ࡬ࡹࡺࡰ࠻࠱࠲ࡻࡼࡽ࠮ࡪࡧࡷࡪ࠳ࡵࡲࡨ࠱ࡵࡪࡨ࠵ࡲࡧࡥ࠶࠸࠹࠽࠮ࡵࡺࡷࠎ࠳࠴ࠠࡠࡡ࠽ࠤ࡭ࡺࡴࡱ࠼࠲࠳ࡼࡽࡷ࠯ࡴࡶࡥ࠳ࡩ࡯࡮࠱ࡵࡷࡦࡲࡡࡣࡵ࠲ࡲࡴࡪࡥ࠯ࡣࡶࡴࡄ࡯ࡤ࠾࠴࠴࠶࠺࠴ࠊࠣࠤࠥࡴ")
__revision__ = l1l1111_Krypto_ (u"ࠤࠧࡍࡩࠪࠢࡵ")
__all__ = [ l1l1111_Krypto_ (u"ࠪࡲࡪࡽࠧࡶ"), l1l1111_Krypto_ (u"ࠫࡕࡑࡃࡔ࠳࠴࠹ࡤࡉࡩࡱࡪࡨࡶࠬࡷ") ]
from l111ll1_Krypto_.l1l111ll_Krypto_.l111l1ll_Krypto_ import l1ll11111_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
import l111ll1_Krypto_.l1l111ll_Krypto_.l111l1ll_Krypto_
class l11l1ll1l_Krypto_:
    l1l1111_Krypto_ (u"ࠧࠨࠢࡕࡪ࡬ࡷࠥࡩࡩࡱࡪࡨࡶࠥࡩࡡ࡯ࠢࡳࡩࡷ࡬࡯ࡳ࡯ࠣࡔࡐࡉࡓࠋࠌࠣࠤࠥࠦࡤࡦࡨࠣࡣࡤ࡯࡮ࡪࡶࡢࡣ࠭ࡹࡥ࡭ࡨ࠯ࠤࡰ࡫ࡹࠪ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢࡸ")l1l1ll1l1_Krypto_ this l1l111l11_Krypto_
        :l11lllll1_Krypto_:
         key : l1lllllll_Krypto_ l1l11lll1_Krypto_ key object
          l1ll111l1_Krypto_ a l1l111ll1_Krypto_ l11ll1ll1_Krypto_ is given, l1lll11l1_Krypto_ l1l1ll111_Krypto_ and l1l11l1l1_Krypto_ l1ll1l1l1_Krypto_ possible.
          l1ll111l1_Krypto_ a l1llll1ll_Krypto_ l11ll1ll1_Krypto_ is given, l111ll11_Krypto_ l1l1ll111_Krypto_ is possible.
        l1l1111_Krypto_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡷࡪࡲࡦ࠯ࡡ࡮ࡩࡾࠦ࠽ࠡ࡭ࡨࡽࠏࠐࠠࠡࠢࠣࡨࡪ࡬ࠠࡤࡣࡱࡣࡪࡴࡣࡳࡻࡳࡸ࠭ࡹࡥ࡭ࡨࠬ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤࡹ")l1lll11ll_Krypto_ True if this l1llll11l_Krypto_ object l1l1l111l_Krypto_ l1llll1l1_Krypto_ l1l11l1ll_Krypto_ for l1l1ll111_Krypto_.l1l1111_Krypto_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡷ࡫ࡴࡶࡴࡱࠤࡸ࡫࡬ࡧ࠰ࡢ࡯ࡪࡿ࠮ࡤࡣࡱࡣࡪࡴࡣࡳࡻࡳࡸ࠭࠯ࠊࠋࠢࠣࠤࠥࡪࡥࡧࠢࡦࡥࡳࡥࡤࡦࡥࡵࡽࡵࡺࠨࡴࡧ࡯ࡪ࠮ࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦࡺ")l1lll11ll_Krypto_ True if this l1llll11l_Krypto_ object l1l1l111l_Krypto_ l1llll1l1_Krypto_ l1l11l1ll_Krypto_ for l1l11l1l1_Krypto_.l1l1111_Krypto_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡸࡥࡵࡷࡵࡲࠥࡹࡥ࡭ࡨ࠱ࡣࡰ࡫ࡹ࠯ࡥࡤࡲࡤࡪࡥࡤࡴࡼࡴࡹ࠮ࠩࠋࠌࠣࠤࠥࠦࡤࡦࡨࠣࡩࡳࡩࡲࡺࡲࡷࠬࡸ࡫࡬ࡧ࠮ࠣࡱࡪࡹࡳࡢࡩࡨ࠭࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥࡻ")l1l1l1l1l_Krypto_ l11lll11l_Krypto_ l1l111l11_Krypto_
        l1l1111l1_Krypto_ function is named ``l1lll1l1l_Krypto_-l11l1llll_Krypto_-l11l11lll_Krypto_-l1l1ll1ll_Krypto_``, and is l111llll_Krypto_ in
        section 7.2.1 l11111ll_Krypto_ l1llll111_Krypto_.
        l11l111ll_Krypto_ a l111l1lll_Krypto_ l1111llll_Krypto_ l11l1l1ll_Krypto_ `l111ll1_Krypto_.l11111l_Krypto_.l11ll1l11_Krypto_`.
        :l11lllll1_Krypto_:
         message : l1111lll1_Krypto_ string
                l1l11ll11_Krypto_ message l111l11l_Krypto_ l1_Krypto_, l1ll1llll_Krypto_ l1lll111l_Krypto_ as l1ll11l1_Krypto_. l1ll1l111_Krypto_ l1l1l111l_Krypto_ l1llll1l1_Krypto_ l11111ll_Krypto_
                l1lll1l11_Krypto_ length, l11l111l_Krypto_ not l1l1l11l1_Krypto_ l1l1l11ll_Krypto_ l11lll11l_Krypto_ l1l11lll1_Krypto_ l111lll1_Krypto_ (in bytes) l1l1llll1_Krypto_ 11.
        :l1lll11ll_Krypto_: A l1111lll1_Krypto_ string, l11lll11l_Krypto_ l1ll111l_Krypto_ in which l11lll11l_Krypto_ message is l11l1ll1_Krypto_.
            l1ll1l111_Krypto_ is as l1lllll11_Krypto_ as l11lll11l_Krypto_ l1l11lll1_Krypto_ l111lll1_Krypto_ (in bytes).
        :l1l111l1l_Krypto_ ValueError:
            l1ll111l1_Krypto_ l11lll11l_Krypto_ l1l11lll1_Krypto_ key length is not l11l1l11_Krypto_ l1lllll11_Krypto_ l111l11l_Krypto_ l1ll1lll1_Krypto_ with l11lll11l_Krypto_ given
            message.
        l1l1111_Krypto_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦࡲࡢࡰࡧࡊࡺࡴࡣࠡ࠿ࠣࡷࡪࡲࡦ࠯ࡡ࡮ࡩࡾ࠴࡟ࡳࡣࡱࡨ࡫ࡻ࡮ࡤࠌࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࡱࡴࡪࡂࡪࡶࡶࠤࡂࠦࡃࡳࡻࡳࡸࡴ࠴ࡕࡵ࡫࡯࠲ࡳࡻ࡭ࡣࡧࡵ࠲ࡸ࡯ࡺࡦࠪࡶࡩࡱ࡬࠮ࡠ࡭ࡨࡽ࠳ࡴࠩࠋࠢࠣࠤࠥࠦࠠࠡࠢ࡮ࠤࡂࠦࡣࡦ࡫࡯ࡣࡩ࡯ࡶࠩ࡯ࡲࡨࡇ࡯ࡴࡴ࠮࠻࠭ࠥࠐࠠࠡࠢࠣࠤࠥࠦࠠ࡮ࡎࡨࡲࠥࡃࠠ࡭ࡧࡱࠬࡲ࡫ࡳࡴࡣࡪࡩ࠮ࠐࠠࠡࠢࠣࠎࠥࠦࠠࠡࠢࠣࠤࠥࠐࠠࠡࠢࠣࠤࠥࠦࠠࡪࡨࠣࡱࡑ࡫࡮ࠡࡀࠣ࡯࠲࠷࠱࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡳࡣ࡬ࡷࡪࠦࡖࡢ࡮ࡸࡩࡊࡸࡲࡰࡴࠫࠦࡕࡲࡡࡪࡰࡷࡩࡽࡺࠠࡪࡵࠣࡸࡴࡵࠠ࡭ࡱࡱ࡫࠳ࠨࠩࠋࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤࡨࡲࡡࡴࡵࠣࡲࡴࡴ࡚ࡦࡴࡲࡖࡦࡴࡤࡃࡻࡷࡩ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡩ࡫ࡦࠡࡡࡢ࡭ࡳ࡯ࡴࡠࡡࠫࡷࡪࡲࡦ࠭ࠢࡵࡪ࠮ࡀࠠࡴࡧ࡯ࡪ࠳ࡸࡦ࠾ࡴࡩࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡧࡩ࡫ࠦ࡟ࡠࡥࡤࡰࡱࡥ࡟ࠩࡵࡨࡰ࡫࠲ࠠࡤࠫ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡷࡩ࡫࡯ࡩࠥࡨ࡯ࡳࡦࠫࡧ࠮ࡃ࠽࠱ࡺ࠳࠴࠿ࠦࡣ࠾ࡵࡨࡰ࡫࠴ࡲࡧࠪ࠴࠭ࡠ࠶࡝ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡶࡪࡺࡵࡳࡰࠣࡧࠏࠦࠠࠡࠢࠣࠤࠥࠦࡰࡴࠢࡀࠤࡹࡵࡢࡺࡶࡨࡷ࠭ࡲࡩࡴࡶࠫࡱࡦࡶࠨ࡯ࡱࡱ࡞ࡪࡸ࡯ࡓࡣࡱࡨࡇࡿࡴࡦࠪࡵࡥࡳࡪࡆࡶࡰࡦ࠭࠱ࠦࡲࡢࡰࡧࡊࡺࡴࡣࠩ࡭࠰ࡱࡑ࡫࡮࠮࠵ࠬ࠭࠮࠯ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࡩࡲࠦ࠽ࠡࡤࠫࠫࡡࡾ࠰࠱࡞ࡻ࠴࠷࠭ࠩࠡ࠭ࠣࡴࡸࠦࠫࠡࡤࡦ࡬ࡷ࠮࠰ࡹ࠲࠳࠭ࠥ࠱ࠠ࡮ࡧࡶࡷࡦ࡭ࡥࠋࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤࡲࠦ࠽ࠡࡵࡨࡰ࡫࠴࡟࡬ࡧࡼ࠲ࡪࡴࡣࡳࡻࡳࡸ࠭࡫࡭࠭ࠢ࠳࠭ࡠ࠶࡝ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤࡨࠦ࠽ࠡࡤࡦ࡬ࡷ࠮࠰ࡹ࠲࠳࠭࠯࠮࡫࠮࡮ࡨࡲ࠭ࡳࠩࠪࠢ࠮ࠤࡲࠐࠠࠡࠢࠣࠤࠥࠦࠠࡳࡧࡷࡹࡷࡴࠠࡤࠌࠣࠤࠥࠦࠊࠡࠢࠣࠤࡩ࡫ࡦࠡࡦࡨࡧࡷࡿࡰࡵࠪࡶࡩࡱ࡬ࠬࠡࡥࡷ࠰ࠥࡹࡥ࡯ࡶ࡬ࡲࡪࡲࠩ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨࡼ")l1lll1lll_Krypto_ a l1l111l11_Krypto_
        l1l1111l1_Krypto_ function is named ``l1lll1l1l_Krypto_-l11l1llll_Krypto_-l11l11lll_Krypto_-l11llll1l_Krypto_``, and is l111llll_Krypto_ in
        section 7.2.2 l11111ll_Krypto_ l1llll111_Krypto_.
        l11l111ll_Krypto_ a l111l1lll_Krypto_ l1111llll_Krypto_ l11l1l1ll_Krypto_ `l111ll1_Krypto_.l11111l_Krypto_.l11ll1l11_Krypto_`.
        :l11lllll1_Krypto_:
         ct : l1111lll1_Krypto_ string
                l1l11ll11_Krypto_ l1ll111l_Krypto_ that contains l11lll11l_Krypto_ message l111l11l_Krypto_ l1l11llll_Krypto_.
         sentinel : any type
                l1l11ll11_Krypto_ object l111l11l_Krypto_ return l111l11l_Krypto_ l111l11ll_Krypto_ that l1lllllll_Krypto_ error l111l1ll1_Krypto_ l11ll1111_Krypto_ l11l11111_Krypto_ l1l11l1l1_Krypto_.
        :l1lll11ll_Krypto_: A l1111lll1_Krypto_ string. l1ll1l111_Krypto_ is l11l11l11_Krypto_ l11lll11l_Krypto_ l1lll1111_Krypto_ message or l11lll11l_Krypto_ ``sentinel`` (in case l11111ll_Krypto_ l1lllllll_Krypto_ error).
        :l1l111l1l_Krypto_ ValueError:
            l1ll111l1_Krypto_ l11lll11l_Krypto_ l1ll111l_Krypto_ length is l11l1l1l_Krypto_
        :l1l111l1l_Krypto_ TypeError:
            l1ll111l1_Krypto_ l11lll11l_Krypto_ l1l11lll1_Krypto_ key l111l1l1_Krypto_ l1ll11l11_Krypto_ l1l111ll1_Krypto_ l11ll1ll1_Krypto_.
        :l1111l11_Krypto_:
            l11l1lll1_Krypto_ l11l1l1l1_Krypto_ **l111l1111_Krypto_** l111l111l_Krypto_ l11lll11l_Krypto_ l11l1111l_Krypto_ l11ll11ll_Krypto_ l111l1l11_Krypto_ l11lll11l_Krypto_ l1ll111l_Krypto_ l1111ll1_Krypto_ that
            this function l111ll1ll_Krypto_ l11lll11l_Krypto_ ``sentinel`` value.
            l111lllll_Krypto_ with l1l1l1l11_Krypto_ l11ll11l1_Krypto_ (for a l11l1ll11_Krypto_ l111l11l1_Krypto_ l11111ll_Krypto_ l11l11l1l_Krypto_ l11l1l111_Krypto_ l11l111l_Krypto_ l111l1l1l_Krypto_ l111lll11_Krypto_),
            l1lllllll_Krypto_ l11l1l11l_Krypto_ is l111ll111_Krypto_ l111l11l_Krypto_ l111llll1_Krypto_ l11lll11l_Krypto_ l1ll11l1_Krypto_ l11111ll_Krypto_ any other l1l1ll111_Krypto_ that l11l11ll1_Krypto_ l11ll111l_Krypto_ out
            with l11lll11l_Krypto_ l111l111_Krypto_ l1l11lll1_Krypto_ l1llll1ll_Krypto_ key (l11l1l1ll_Krypto_ `l11l111l1_Krypto_ (u"ࡵࠫࡸࡦ࡟ࡠࠢࡤࡸࡹࡧࡣ࡬ࠫ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡋࡱࠤ࡬࡫࡮ࡦࡴࡤࡰ࠱ࠦࡩࡵࠢࡶ࡬ࡴࡻ࡬ࡥࠢࡱࡳࡹࠦࡢࡦࠢࡳࡳࡸࡹࡩࡣ࡮ࡨࠤ࡫ࡵࡲࠡࡶ࡫ࡩࠥࡵࡴࡩࡧࡵࠤࡵࡧࡲࡵࡻࠣࡸࡴࠦࡤࡪࡵࡷ࡭ࡳ࡭ࡵࡪࡵ࡫ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡺ࡬ࡪࡺࡨࡦࡴࠣࡴࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡢࡶࠣࡸ࡭࡫ࠠࡴࡧࡵࡺࡪࡸࠠࡴ࡫ࡧࡩࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡨࡥࡤࡣࡸࡷࡪࠦࡴࡩࡧࠣࡺࡦࡲࡵࡦࠢࡵࡩࡹࡻࡲ࡯ࡧࡧࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡺࡥࡸࠦࡡࠡࡢࡣࡷࡪࡴࡴࡪࡰࡨࡰࡥࡦࠠࡢࡵࠣࡳࡵࡶ࡯ࡴࡧࡧࠤࡹࡵࠠࡢࠢࡵࡥࡳࡪ࡯࡮࠮ࠣ࡭ࡳࡼࡡ࡭࡫ࡧࠤࡲ࡫ࡳࡴࡣࡪࡩ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡍࡳࠦࡦࡢࡥࡷ࠰ࠥࡺࡨࡦࠢࡶࡩࡨࡵ࡮ࡥࠢࡲࡴࡹ࡯࡯࡯ࠢ࡬ࡷࠥࡴ࡯ࡵࠢࡷ࡬ࡦࡺࠠࡶࡰ࡯࡭ࡰ࡫࡬ࡺ࠼ࠣࡩࡳࡩࡲࡺࡲࡷ࡭ࡴࡴࠠࡥࡱࡱࡩࠥࡧࡣࡤࡱࡵࡨ࡮ࡴࡧࠡࡶࡲࠤࡕࡑࡃࡔࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡦ࡯ࡥࡩࡩࡹࠠ࡯ࡱࠣ࡫ࡴࡵࡤࠡ࡫ࡱࡸࡪ࡭ࡲࡪࡶࡼࠤࡨ࡮ࡥࡤ࡭࠱ࠤ࡙࡮ࡥࡳࡧࠣ࡭ࡸࠦࡲࡰࡷࡪ࡬ࡱࡿࠠࡰࡰࡨࠤࡨ࡮ࡡ࡯ࡥࡨࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࡬ࡲࠥ࠸࡞࠲࠸ࠣࡪࡴࡸࠠࡢࠢࡵࡥࡳࡪ࡯࡮ࠢࡦ࡭ࡵ࡮ࡥࡳࡶࡨࡼࡹࠦࡴࡰࠢࡥࡩࠥࡸࡥࡵࡷࡵࡲࡪࡪࠠࡢࡵࠣࡥࠥࡼࡡ࡭࡫ࡧࠤࡲ࡫ࡳࡴࡣࡪࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠬࡦࡲࡴࡩࡱࡸ࡫࡭ࠦࡲࡢࡰࡧࡳࡲࠦ࡬ࡰࡱ࡮࡭ࡳ࡭ࠩ࠯ࠌࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡏࡴࠡ࡫ࡶࠤࡹ࡮ࡥࡳࡧࡩࡳࡷ࡫ࠠࡢࡦࡹ࡭ࡸࡧࡢ࡭ࡧࡧࠤࡹࡵ࠺ࠋࠢࠣࠤࠥࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠶࠴ࠠࡔࡧ࡯ࡩࡨࡺࠠࡢࡵࠣࡤࡥࡹࡥ࡯ࡶ࡬ࡲࡪࡲࡠࡡࠢࡤࠤࡻࡧ࡬ࡶࡧࠣࡸ࡭ࡧࡴࠡࡴࡨࡷࡪࡳࡢ࡭ࡧࡶࠤࡦࠦࡰ࡭ࡣࡸࡷࡦࡨ࡬ࡦࠢࡵࡥࡳࡪ࡯࡮࠮ࠣ࡭ࡳࡼࡡ࡭࡫ࡧࠤࡲ࡫ࡳࡴࡣࡪࡩ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠷࠴ࠠࡏࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠤࡧࡧࡣ࡬ࠢࡤࡲࠥ࡫ࡲࡳࡱࡵࠤࡦࡹࠠࡴࡱࡲࡲࠥࡧࡳࠡࡻࡲࡹࠥࡪࡥࡵࡧࡦࡸࠥࡧࠠࡡࡢࡶࡩࡳࡺࡩ࡯ࡧ࡯ࡤࡥࠦࡶࡢ࡮ࡸࡩ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡑࡷࡷࠤࡩ࡯ࡦࡧࡧࡵࡩࡳࡺ࡬ࡺ࠮ࠣࡽࡴࡻࠠࡴࡪࡲࡹࡱࡪࠠ࡯ࡱࡷࠤࡪࡾࡰ࡭࡫ࡦ࡭ࡹࡲࡹࠡࡥ࡫ࡩࡨࡱࠠࡪࡨࠣࡸ࡭࡫ࠠࡳࡧࡷࡹࡷࡴࡥࡥࠢࡹࡥࡱࡻࡥࠡ࡫ࡶࠤࡹ࡮ࡥࠡࡢࡣࡷࡪࡴࡴࡪࡰࡨࡰࡥࡦࠠࡰࡴࠣࡲࡴࡺ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠳࠯ࠢࡆࡳࡻ࡫ࡲࠡࡣ࡯ࡰࠥࡶ࡯ࡴࡵ࡬ࡦࡱ࡫ࠠࡦࡴࡵࡳࡷࡹࠠࡸ࡫ࡷ࡬ࠥࡧࠠࡴ࡫ࡱ࡫ࡱ࡫ࠬࠡࡩࡨࡲࡪࡸࡩࡤࠢࡨࡶࡷࡵࡲࠡ࡫ࡱࡨ࡮ࡩࡡࡵࡱࡵ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠸࠳ࠦࡅ࡮ࡤࡨࡨࠥ࡯࡮ࡵࡱࠣࡸ࡭࡫ࠠࡥࡧࡩ࡭ࡳ࡯ࡴࡪࡱࡱࠤࡴ࡬ࠠࡡࡢࡰࡩࡸࡹࡡࡨࡧࡣࡤࠥ࠮ࡡࡵࠢࡷ࡬ࡪࠦࡰࡳࡱࡷࡳࡨࡵ࡬ࠡ࡮ࡨࡺࡪࡲࠩࠡࡣࠣࡨ࡮࡭ࡥࡴࡶࠣࠬࡪ࠴ࡧ࠯ࠢࡣࡤࡘࡎࡁ࠮࠳ࡣࡤ࠮࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡋࡷࠤ࡮ࡹࠠࡳࡧࡦࡳࡲࡳࡥ࡯ࡦࡨࡨࠥ࡬࡯ࡳࠢ࡬ࡸࠥࡺ࡯ࠡࡤࡨࠤࡹ࡮ࡥࠡࡴ࡬࡫࡭ࡺ࡭ࡰࡵࡷࠤࡵࡧࡲࡵࠢࡣࡤࡲ࡫ࡳࡴࡣࡪࡩࡥࡦ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠵࠯࡚ࠢ࡬ࡪࡸࡥࠡࡲࡲࡷࡸ࡯ࡢ࡭ࡧ࠯ࠤࡲࡵ࡮ࡪࡶࡲࡶࠥࡺࡨࡦࠢࡱࡹࡲࡨࡥࡳࠢࡲࡪࠥ࡫ࡲࡳࡱࡵࡷࠥࡪࡵࡦࠢࡷࡳࠥࡩࡩࡱࡪࡨࡶࡹ࡫ࡸࡵࡵࠣࡳࡷ࡯ࡧࡪࡰࡤࡸ࡮ࡴࡧࠡࡨࡵࡳࡲࠦࡴࡩࡧࠣࡷࡦࡳࡥࠡࡲࡤࡶࡹࡿࠬࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡤࡲࡩࠦࡳ࡭ࡱࡺࠤࡩࡵࡷ࡯ࠢࡷ࡬ࡪࠦࡲࡢࡶࡨࠤࡴ࡬ࠠࡵࡪࡨࠤࡷ࡫ࡱࡶࡧࡶࡸࡸࠦࡦࡳࡱࡰࠤࡸࡻࡣࡩࠢࡳࡥࡷࡺࡹࠡࠪࡲࡶࠥ࡫ࡶࡦࡰࠣࡦࡱࡧࡣ࡬࡮࡬ࡷࡹࠦࡩࡵࠢࡤࡰࡹࡵࡧࡦࡶ࡫ࡩࡷ࠯࠮ࠋࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠰ࠪࡊࡨࠣࡽࡴࡻࠠࡢࡴࡨࠤࡩ࡫ࡳࡪࡩࡱ࡭ࡳ࡭ࠠࡢࠢࡱࡩࡼࠦࡰࡳࡱࡷࡳࡨࡵ࡬࠭ࠢࡦࡳࡳࡹࡩࡥࡧࡵࠤࡺࡹࡩ࡯ࡩࠣࡸ࡭࡫ࠠ࡮ࡱࡵࡩࠥࡸ࡯ࡣࡷࡶࡸࠥࡖࡋࡄࡕࠍࠤࠥࠦࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠮࠯ࠢࡢࡣ࠿ࠦࡨࡵࡶࡳ࠾࠴࠵ࡷࡸࡹ࠱ࡦࡪࡲ࡬࠮࡮ࡤࡦࡸ࠴ࡣࡰ࡯࠲ࡹࡸ࡫ࡲ࠰ࡤ࡯ࡩ࡮ࡩࡨࡦࡰ࠲ࡴࡦࡶࡥࡳࡵ࠲ࡴࡰࡩࡳ࠯ࡲࡶࠎࠥࠦࠠࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨࠊࠡࠢࠣࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡯ࡲࡨࡇ࡯ࡴࡴࠢࡀࠤࡈࡸࡹࡱࡶࡲ࠲࡚ࡺࡩ࡭࠰ࡱࡹࡲࡨࡥࡳ࠰ࡶ࡭ࡿ࡫ࠨࡴࡧ࡯ࡪ࠳ࡥ࡫ࡦࡻ࠱ࡲ࠮ࠐࠠࠡࠢࠣࠤࠥࠦࠠ࡬ࠢࡀࠤࡨ࡫ࡩ࡭ࡡࡧ࡭ࡻ࠮࡭ࡰࡦࡅ࡭ࡹࡹࠬ࠹ࠫࠣࠎࠥࠦࠠࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࠎࠥࠦࠠࠡࠢࠣࠤࠥ࡯ࡦࠡ࡮ࡨࡲ࠭ࡩࡴࠪࠢࠤࡁࠥࡱ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡲࡢ࡫ࡶࡩࠥ࡜ࡡ࡭ࡷࡨࡉࡷࡸ࡯ࡳࠪࠥࡇ࡮ࡶࡨࡦࡴࡷࡩࡽࡺࠠࡸ࡫ࡷ࡬ࠥ࡯࡮ࡤࡱࡵࡶࡪࡩࡴࠡ࡮ࡨࡲ࡬ࡺࡨ࠯ࠤࠬࠎࠥࠦࠠࠡࠢࠣࠤࠥࠐࠠࠡࠢࠣࠤࠥࠦࠠ࡮ࠢࡀࠤࡸ࡫࡬ࡧ࠰ࡢ࡯ࡪࡿ࠮ࡥࡧࡦࡶࡾࡶࡴࠩࡥࡷ࠭ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࡧࡰࠤࡂࠦࡢࡤࡪࡵࠬ࠵ࡾ࠰࠱ࠫ࠭ࠬࡰ࠳࡬ࡦࡰࠫࡱ࠮࠯ࠠࠬࠢࡰࠎࠥࠦࠠࠡࠢࠣࠤࠥࠐࠠࠡࠢࠣࠤࠥࠦࠠࡴࡧࡳࠤࡂࠦࡥ࡮࠰ࡩ࡭ࡳࡪࠨࡣࡥ࡫ࡶ࠭࠶ࡸ࠱࠲ࠬ࠰࠷࠯ࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡫ࡩࠤࠥࡴ࡯ࡵࠢࡨࡱ࠳ࡹࡴࡢࡴࡷࡷࡼ࡯ࡴࡩࠪࡥࠬࠬࡽ")\l111ll11l_Krypto_\l111ll1l1_Krypto_')) or sep<10:
            return sentinel
        return l111lll1l_Krypto_[sep+1:]
def new(key):
    l1l1111_Krypto_ (u"ࠦࠧࠨࡒࡦࡶࡸࡶࡳࠦࡡࠡࡥ࡬ࡴ࡭࡫ࡲࠡࡱࡥ࡮ࡪࡩࡴࠡࡢࡓࡏࡈ࡙࠱࠲࠷ࡢࡇ࡮ࡶࡨࡦࡴࡣࠤࡹ࡮ࡡࡵࠢࡦࡥࡳࠦࡢࡦࠢࡸࡷࡪࡪࠠࡵࡱࠣࡴࡪࡸࡦࡰࡴࡰࠤࡕࡑࡃࡔࠌࠍࠤࠥࠦࠠ࠻ࡒࡤࡶࡦࡳࡥࡵࡧࡵࡷ࠿ࠐࠠࠡࠢࠣࠤࡰ࡫ࡹࠡ࠼ࠣࡖࡘࡇࠠ࡬ࡧࡼࠤࡴࡨࡪࡦࡥࡷࠎࠥࠦࠠࠡࠢࠣࡘ࡭࡫ࠠ࡬ࡧࡼࠤࡹࡵࠠࡶࡵࡨࠤࡹࡵࠠࡦࡰࡦࡶࡾࡶࡴࠡࡱࡵࠤࡩ࡫ࡣࡳࡻࡳࡸࠥࡺࡨࡦࠢࡰࡩࡸࡹࡡࡨࡧ࠱ࠤ࡙࡮ࡩࡴࠢ࡬ࡷࠥࡧࠠࡡࡅࡵࡽࡵࡺ࡯࠯ࡒࡸࡦࡱ࡯ࡣࡌࡧࡼ࠲ࡗ࡙ࡁࡡࠢࡲࡦ࡯࡫ࡣࡵ࠰ࠍࠤࠥࠦࠠࠡࠢࡇࡩࡨࡸࡹࡱࡶ࡬ࡳࡳࠦࡩࡴࠢࡲࡲࡱࡿࠠࡱࡱࡶࡷ࡮ࡨ࡬ࡦࠢ࡬ࡪࠥ࠰࡫ࡦࡻ࠭ࠤ࡮ࡹࠠࡢࠢࡳࡶ࡮ࡼࡡࡵࡧࠣࡖࡘࡇࠠ࡬ࡧࡼ࠲ࠏࠐࠠࠡࠢࠣࠦࠧࠨࡾ")
    return l11l1ll1l_Krypto_(key)