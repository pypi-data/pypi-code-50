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
l1l1111_Krypto_ (u"ࠦࠧࠨࠊࡓࡕࡄࠤࡩ࡯ࡧࡪࡶࡤࡰࠥࡹࡩࡨࡰࡤࡸࡺࡸࡥࠡࡲࡵࡳࡹࡵࡣࡰ࡮ࠣࡥࡨࡩ࡯ࡳࡦ࡬ࡲ࡬ࠦࡴࡰࠢࡓࡏࡈ࡙ࠊࠋࡕࡨࡩࠥࡘࡆࡄ࠵࠷࠸࠼ࡥ࡟ࠡࡱࡵࠤࡹ࡮ࡥࠡࡢࡲࡶ࡮࡭ࡩ࡯ࡣ࡯ࠤࡗ࡙ࡁࠡࡎࡤࡦࡸࠦࡳࡱࡧࡦ࡭࡫࡯ࡣࡢࡶ࡬ࡳࡳࡦ࡟ࡠ࠰ࠍࠎ࡙࡮ࡩࡴࠢࡶࡧ࡭࡫࡭ࡦࠢ࡬ࡷࠥࡳ࡯ࡳࡧࠣࡴࡷࡵࡰࡦࡴ࡯ࡽࠥࡩࡡ࡭࡮ࡨࡨࠥࡦࡠࡓࡕࡄࡗࡘࡇ࠭ࡑࡍࡆࡗ࠶࠳ࡶ࠲ࡡ࠸ࡤࡥ࠴ࠊࠋࡈࡲࡶࠥ࡫ࡸࡢ࡯ࡳࡰࡪ࠲ࠠࡢࠢࡶࡩࡳࡪࡥࡳࠢࡰࡥࡾࠦࡡࡶࡶ࡫ࡩࡳࡺࡩࡤࡣࡷࡩࠥࡧࠠ࡮ࡧࡶࡷࡦ࡭ࡥࠡࡷࡶ࡭ࡳ࡭ࠠࡔࡊࡄ࠱࠶ࠦ࡬ࡪ࡭ࡨࠎࡹ࡮ࡩࡴ࠼ࠍࠎࠥࠦࠠࠡࠢࠣࠤࠥࡄ࠾࠿ࠢࡩࡶࡴࡳࠠࡄࡴࡼࡴࡹࡵ࠮ࡔ࡫ࡪࡲࡦࡺࡵࡳࡧࠣ࡭ࡲࡶ࡯ࡳࡶࠣࡔࡐࡉࡓ࠲ࡡࡹ࠵ࡤ࠻ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡀࡁࡂࠥ࡬ࡲࡰ࡯ࠣࡇࡷࡿࡰࡵࡱ࠱ࡌࡦࡹࡨࠡ࡫ࡰࡴࡴࡸࡴࠡࡕࡋࡅࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠾࠿ࡀࠣࡪࡷࡵ࡭ࠡࡅࡵࡽࡵࡺ࡯࠯ࡒࡸࡦࡱ࡯ࡣࡌࡧࡼࠤ࡮ࡳࡰࡰࡴࡷࠤࡗ࡙ࡁࠋࠢࠣࠤࠥࠦࠠࠡࠢࡁࡂࡃࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠿ࡀࡁࠤࡲ࡫ࡳࡴࡣࡪࡩࠥࡃࠠࠨࡖࡲࠤࡧ࡫ࠠࡴ࡫ࡪࡲࡪࡪࠧࠋࠢࠣࠤࠥࠦࠠࠡࠢࡁࡂࡃࠦ࡫ࡦࡻࠣࡁࠥࡘࡓࡂ࠰࡬ࡱࡵࡵࡲࡵࡍࡨࡽ࠭ࡵࡰࡦࡰࠫࠫࡵࡸࡩࡷ࡭ࡨࡽ࠳ࡪࡥࡳࠩࠬ࠲ࡷ࡫ࡡࡥࠪࠬ࠭ࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠾࠿ࡀࠣ࡬ࠥࡃࠠࡔࡊࡄ࠲ࡳ࡫ࡷࠩ࡯ࡨࡷࡸࡧࡧࡦࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࡃࡄ࠾ࠡࡵ࡬࡫ࡳ࡫ࡲࠡ࠿ࠣࡔࡐࡉࡓ࠲ࡡࡹ࠵ࡤ࠻࠮࡯ࡧࡺࠬࡰ࡫ࡹࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࡂࡃࡄࠠࡴ࡫ࡪࡲࡦࡺࡵࡳࡧࠣࡁࠥࡹࡩࡨࡰࡨࡶ࠳ࡹࡩࡨࡰࠫ࡬࠮ࠐࠊࡂࡶࠣࡸ࡭࡫ࠠࡳࡧࡦࡩ࡮ࡼࡥࡳࠢࡶ࡭ࡩ࡫ࠬࠡࡸࡨࡶ࡮࡬ࡩࡤࡣࡷ࡭ࡴࡴࠠࡤࡣࡱࠤࡧ࡫ࠠࡥࡱࡱࡩࠥࡻࡳࡪࡰࡪࠤࡹ࡮ࡥࠡࡲࡸࡦࡱ࡯ࡣࠡࡲࡤࡶࡹࠦ࡯ࡧࠌࡷ࡬ࡪࠦࡒࡔࡃࠣ࡯ࡪࡿ࠺ࠋࠌࠣࠤࠥࠦࠠࠡࠢࠣࡂࡃࡄࠠ࡬ࡧࡼࠤࡂࠦࡒࡔࡃ࠱࡭ࡲࡶ࡯ࡳࡶࡎࡩࡾ࠮࡯ࡱࡧࡱࠬࠬࡶࡵࡣ࡭ࡨࡽ࠳ࡪࡥࡳࠩࠬ࠲ࡷ࡫ࡡࡥࠪࠬ࠭ࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠾࠿ࡀࠣ࡬ࠥࡃࠠࡔࡊࡄ࠲ࡳ࡫ࡷࠩ࡯ࡨࡷࡸࡧࡧࡦࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࡃࡄ࠾ࠡࡸࡨࡶ࡮࡬ࡩࡦࡴࠣࡁࠥࡖࡋࡄࡕ࠴ࡣࡻ࠷࡟࠶࠰ࡱࡩࡼ࠮࡫ࡦࡻࠬࠎࠥࠦࠠࠡࠢࠣࠤࠥࡄ࠾࠿ࠢ࡬ࡪࠥࡼࡥࡳ࡫ࡩ࡭ࡪࡸ࠮ࡷࡧࡵ࡭࡫ࡿࠨࡩ࠮ࠣࡷ࡮࡭࡮ࡢࡶࡸࡶࡪ࠯࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡁࡂࡃࠦࠠࠡࠢࡳࡶ࡮ࡴࡴࠡࠤࡗ࡬ࡪࠦࡳࡪࡩࡱࡥࡹࡻࡲࡦࠢ࡬ࡷࠥࡧࡵࡵࡪࡨࡲࡹ࡯ࡣ࠯ࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡃࡄ࠾ࠡࡧ࡯ࡷࡪࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࡀࡁࡂࠥࠦࠠࠡࡲࡵ࡭ࡳࡺࠠࠣࡖ࡫ࡩࠥࡹࡩࡨࡰࡤࡸࡺࡸࡥࠡ࡫ࡶࠤࡳࡵࡴࠡࡣࡸࡸ࡭࡫࡮ࡵ࡫ࡦ࠲ࠧࠐࠊ࠻ࡷࡱࡨࡴࡩࡵ࡮ࡧࡱࡸࡪࡪ࠺ࠡࡡࡢࡶࡪࡼࡩࡴ࡫ࡲࡲࡤࡥࠬࠡࡡࡢࡴࡦࡩ࡫ࡢࡩࡨࡣࡤࠐࠊ࠯࠰ࠣࡣࡤࡀࠠࡩࡶࡷࡴ࠿࠵࠯ࡸࡹࡺ࠲࡮࡫ࡴࡧ࠰ࡲࡶ࡬࠵ࡲࡧࡥ࠲ࡶ࡫ࡩ࠳࠵࠶࠺࠲ࡹࡾࡴࠋ࠰࠱ࠤࡤࡥ࠺ࠡࡪࡷࡸࡵࡀ࠯࠰ࡹࡺࡻ࠳ࡸࡳࡢ࠰ࡦࡳࡲ࠵ࡲࡴࡣ࡯ࡥࡧࡹ࠯࡯ࡱࡧࡩ࠳ࡧࡳࡱࡁ࡬ࡨࡂ࠸࠱࠳࠷ࠍࠦࠧࠨᨡ")
__revision__ = l1l1111_Krypto_ (u"ࠧࠪࡉࡥࠦࠥᨢ")
__all__ = [ l1l1111_Krypto_ (u"࠭࡮ࡦࡹࠪᨣ"), l1l1111_Krypto_ (u"ࠧࡑࡍࡆࡗ࠶࠷࠵ࡠࡕ࡬࡫ࡘࡩࡨࡦ࡯ࡨࠫᨤ") ]
import l111ll1_Krypto_.l1l111ll_Krypto_.l111l1ll_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l111l1ll_Krypto_ import l1ll11111_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l11l1lll1l_Krypto_ import l11l11llll_Krypto_, l11l1ll1l1_Krypto_, l1lll1lll11l_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
class l1llll111ll1_Krypto_:
    l1l1111_Krypto_ (u"ࠣࠤࠥࡘ࡭࡯ࡳࠡࡵ࡬࡫ࡳࡧࡴࡶࡴࡨࠤࡸࡩࡨࡦ࡯ࡨࠤࡨࡧ࡮ࠡࡲࡨࡶ࡫ࡵࡲ࡮ࠢࡓࡏࡈ࡙ࠊࠋࠢࠣࠤࠥࡪࡥࡧࠢࡢࡣ࡮ࡴࡩࡵࡡࡢࠬࡸ࡫࡬ࡧ࠮ࠣ࡯ࡪࡿࠩ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᨥ")l1l1ll1l1_Krypto_ this l1l111l11_Krypto_
        :l11lllll1_Krypto_:
         key : l1lllllll_Krypto_ l1l11lll1_Krypto_ key object
          l1ll111l1_Krypto_ a l1l111ll1_Krypto_ l11ll1ll1_Krypto_ is given, l1lll11l1_Krypto_ signature and l1llll1llll1_Krypto_ l1ll1l1l1_Krypto_ possible.
          l1ll111l1_Krypto_ a l1llll1ll_Krypto_ l11ll1ll1_Krypto_ is given, l111ll11_Krypto_ l1llll1llll1_Krypto_ is possible.
        l1l1111_Krypto_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡳࡦ࡮ࡩ࠲ࡤࡱࡥࡺࠢࡀࠤࡰ࡫ࡹࠋࠌࠣࠤࠥࠦࡤࡦࡨࠣࡧࡦࡴ࡟ࡴ࡫ࡪࡲ࠭ࡹࡥ࡭ࡨࠬ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᨦ")l1lll11ll_Krypto_ True if this l1llll11l_Krypto_ object l1l1l111l_Krypto_ l1llll1l1_Krypto_ l1l11l1ll_Krypto_ for l1lllll1llll_Krypto_ l1lllll1111l_Krypto_.l1l1111_Krypto_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡳࡧࡷࡹࡷࡴࠠࡴࡧ࡯ࡪ࠳ࡥ࡫ࡦࡻ࠱࡬ࡦࡹ࡟ࡱࡴ࡬ࡺࡦࡺࡥࠩࠫࠍࠎࠥࠦࠠࠡࡦࡨࡪࠥࡹࡩࡨࡰࠫࡷࡪࡲࡦ࠭ࠢࡰ࡬ࡦࡹࡨࠪ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᨧ")l1l1l1l1l_Krypto_ l11lll11l_Krypto_ l1l111l11_Krypto_
        l1l1111l1_Krypto_ function is named ``l1111111l11_Krypto_-l11l1llll_Krypto_-l11l11lll_Krypto_-l1llll1ll111_Krypto_``, and is l111llll_Krypto_ in
        section 8.2.1 l11111ll_Krypto_ l1llll111_Krypto_.
        :l11lllll1_Krypto_:
         l1lllll1ll11_Krypto_ : hash object
                l1l11ll11_Krypto_ hash that l111l1ll1_Krypto_ l11ll111l_Krypto_ out l1llll1lll11_Krypto_ l11lll11l_Krypto_ message. l1l1111l1_Krypto_ is l1lllllll_Krypto_ object
                l1111111111_Krypto_ l111l11l_Krypto_ l11lll11l_Krypto_ `l111ll1_Krypto_.l1lll1ll1_Krypto_` module.
        :l1lll11ll_Krypto_: l1l11ll11_Krypto_ signature encoded as a string.
        :l1l111l1l_Krypto_ ValueError:
            l1ll111l1_Krypto_ l11lll11l_Krypto_ l1l11lll1_Krypto_ key length is not l11l1l11_Krypto_ l1lllll11_Krypto_ l111l11l_Krypto_ l1ll1lll1_Krypto_ with l11lll11l_Krypto_ given
            hash l1lllll11lll_Krypto_.
        :l1l111l1l_Krypto_ TypeError:
            l1ll111l1_Krypto_ l11lll11l_Krypto_ l1l11lll1_Krypto_ key l111l1l1_Krypto_ l1ll11l11_Krypto_ l1l111ll1_Krypto_ l11ll1ll1_Krypto_.
        l1l1111_Krypto_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࠌࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࡱࡴࡪࡂࡪࡶࡶࠤࡂࠦࡃࡳࡻࡳࡸࡴ࠴ࡕࡵ࡫࡯࠲ࡳࡻ࡭ࡣࡧࡵ࠲ࡸ࡯ࡺࡦࠪࡶࡩࡱ࡬࠮ࡠ࡭ࡨࡽ࠳ࡴࠩࠋࠢࠣࠤࠥࠦࠠࠡࠢ࡮ࠤࡂࠦࡣࡦ࡫࡯ࡣࡩ࡯ࡶࠩ࡯ࡲࡨࡇ࡯ࡴࡴ࠮࠻࠭ࠥࠐࠠࠡࠢࠣࠎࠥࠦࠠࠡࠢࠣࠤࠥࠐࠠࠡࠢࠣࠤࠥࠦࠠࡦ࡯ࠣࡁࠥࡋࡍࡔࡃࡢࡔࡐࡉࡓ࠲ࡡ࡙࠵ࡤ࠻࡟ࡆࡐࡆࡓࡉࡋࠨ࡮ࡪࡤࡷ࡭࠲ࠠ࡬ࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦ࡭ࠡ࠿ࠣࡷࡪࡲࡦ࠯ࡡ࡮ࡩࡾ࠴ࡤࡦࡥࡵࡽࡵࡺࠨࡦ࡯ࠬࠎࠥࠦࠠࠡࠢࠣࠤࠥࠐࠠࠡࠢࠣࠤࠥࠦࠠࡔࠢࡀࠤࡧࡩࡨࡳࠪ࠳ࡼ࠵࠶ࠩࠫࠪ࡮࠱ࡱ࡫࡮ࠩ࡯ࠬ࠭ࠥ࠱ࠠ࡮ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡶࡪࡺࡵࡳࡰࠣࡗࠏࠦࠠࠡࠢࠍࠤࠥࠦࠠࡥࡧࡩࠤࡻ࡫ࡲࡪࡨࡼࠬࡸ࡫࡬ࡧ࠮ࠣࡱ࡭ࡧࡳࡩ࠮ࠣࡗ࠮ࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᨨ")l1lllll11111_Krypto_ that a l1llll1ll1ll_Krypto_ l1l111l11_Krypto_
        l1l1111l1_Krypto_ function l111111l111_Krypto_ if l11lll11l_Krypto_ l11l1111l_Krypto_ l111111llll_Krypto_ l11lll11l_Krypto_ l1l111ll1_Krypto_ l11ll1ll1_Krypto_ l11111ll_Krypto_ l11lll11l_Krypto_ key
        l1llllll11l1_Krypto_ l1llll1l1lll_Krypto_ l11lll11l_Krypto_ message.
        l1l1111l1_Krypto_ function is named ``l1111111l11_Krypto_-l11l1llll_Krypto_-l11l11lll_Krypto_-l1llll1lll1l_Krypto_``, and is l111llll_Krypto_ in
        section 8.2.2 l11111ll_Krypto_ l1llll111_Krypto_.
        :l11lllll1_Krypto_:
         l1lllll1ll11_Krypto_ : hash object
                l1l11ll11_Krypto_ hash that l111l1ll1_Krypto_ l11ll111l_Krypto_ out l1llll1lll11_Krypto_ l11lll11l_Krypto_ message. l1l1111l1_Krypto_ is l1lllllll_Krypto_ object
                l1111111111_Krypto_ l111l11l_Krypto_ l11lll11l_Krypto_ `l111ll1_Krypto_.l1lll1ll1_Krypto_` module.
         S : string
                l1l11ll11_Krypto_ signature that l1llllll11ll_Krypto_ l111l11l_Krypto_ l1llll1l1_Krypto_ l1lllll1l1ll_Krypto_.
        :l1lll11ll_Krypto_: True if l1llll1llll1_Krypto_ is l111111l1ll_Krypto_. False l111111ll11_Krypto_.
        l1l1111_Krypto_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤࡲࡵࡤࡃ࡫ࡷࡷࠥࡃࠠࡄࡴࡼࡴࡹࡵ࠮ࡖࡶ࡬ࡰ࠳ࡴࡵ࡮ࡤࡨࡶ࠳ࡹࡩࡻࡧࠫࡷࡪࡲࡦ࠯ࡡ࡮ࡩࡾ࠴࡮ࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣ࡯ࠥࡃࠠࡤࡧ࡬ࡰࡤࡪࡩࡷࠪࡰࡳࡩࡈࡩࡵࡵ࠯࠼࠮ࠦࠊࠡࠢࠣࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡫ࡩࠤࡱ࡫࡮ࠩࡕࠬࠤࠦࡃࠠ࡬࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡴࡨࡸࡺࡸ࡮ࠡ࠲ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࠎࠥࠦࠠࠡࠢࠣࠤࠥࡳࠠ࠾ࠢࡶࡩࡱ࡬࠮ࡠ࡭ࡨࡽ࠳࡫࡮ࡤࡴࡼࡴࡹ࠮ࡓ࠭ࠢ࠳࠭ࡠ࠶࡝ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤࡪࡳ࠱ࠡ࠿ࠣࡦࡨ࡮ࡲࠩ࠲ࡻ࠴࠵࠯ࠪࠩ࡭࠰ࡰࡪࡴࠨ࡮ࠫࠬࠤ࠰ࠦ࡭ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤࡹࡸࡹ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡦ࡯࠵ࠤࡂࠦࡅࡎࡕࡄࡣࡕࡑࡃࡔ࠳ࡢ࡚࠶ࡥ࠵ࡠࡇࡑࡇࡔࡊࡅࠩ࡯࡫ࡥࡸ࡮ࠬࠡ࡭ࠬࠎࠥࠦࠠࠡࠢࠣࠤࠥ࡫ࡸࡤࡧࡳࡸࠥ࡜ࡡ࡭ࡷࡨࡉࡷࡸ࡯ࡳ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡴࡨࡸࡺࡸ࡮ࠡ࠲ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࠎࠥࠦࠠࠡࠢࠣࠤࠥࠐࠠࠡࠢࠣࠤࠥࠦࠠࡳࡧࡷࡹࡷࡴࠠࡦ࡯࠴ࡁࡂ࡫࡭࠳ࠌࠣࠤࠥࠦࠊࡥࡧࡩࠤࡊࡓࡓࡂࡡࡓࡏࡈ࡙࠱ࡠࡘ࠴ࡣ࠺ࡥࡅࡏࡅࡒࡈࡊ࠮ࡨࡢࡵ࡫࠰ࠥ࡫࡭ࡍࡧࡱ࠭࠿ࠐࠠࠡࠢࠣࠦࠧࠨᨩ")
    l1llll1l1ll1_Krypto_ l11lll11l_Krypto_ ``l1lllll1l111_Krypto_-l11l1llll_Krypto_-l11l11lll_Krypto_-l1llll1ll11l_Krypto_`` function, as l1llll1l11l1_Krypto_
    in l1l111l11_Krypto_
    ``l1lllll1l111_Krypto_-l11l1llll_Krypto_-l11l11lll_Krypto_-l1llll1ll11l_Krypto_`` l111111lll1_Krypto_ l1l1lll11_Krypto_ l11lll11l_Krypto_ message ``M`` as input,
    and hash it l1lllllllll1_Krypto_. l111111l11l_Krypto_, l1llllll1l1l_Krypto_ l1llll1ll1l1_Krypto_ that l11lll11l_Krypto_ message l111l1l1_Krypto_ already
    l1111111ll1_Krypto_ l1llll1l1l11_Krypto_ l11111111ll_Krypto_.
    :l11lllll1_Krypto_:
     hash : hash object
            l1l11ll11_Krypto_ hash object that l11111111l1_Krypto_ l11lll11l_Krypto_ digest l11111ll_Krypto_ l11lll11l_Krypto_ message l1lllll11ll1_Krypto_ l1llll1l1lll_Krypto_.
     l1lllllll1l1_Krypto_ : int
            l1l11ll11_Krypto_ length l11lll11l_Krypto_ final encoding l1l1l1ll1_Krypto_ l1llll1111ll_Krypto_, in bytes.
    :l1111l11_Krypto_: l11lll11l_Krypto_ l1lll1llll1l_Krypto_ l1lllll1l_Krypto_ (l1llll11111l_Krypto_) l1lll1lll1ll_Krypto_ that ``l1llll11l1ll_Krypto_``
        l1llll11lll1_Krypto_ l111l11l_Krypto_ l1llll1l1_Krypto_ l1lll1lllll1_Krypto_-encoded. l1l1111l1_Krypto_ l1llll11l111_Krypto_ that old l1llll11l11l_Krypto_
        l1lll1lll111_Krypto_ l1llll1111ll_Krypto_ length l1lll1llllll_Krypto_ in l1llll11ll1l_Krypto_ l1llll11l1l1_Krypto_, which
        is not l1lll1lll1l1_Krypto_ in l1lll1llll11_Krypto_. l1llll11llll_Krypto_ encoding l1lll1ll1lll_Krypto_ l1llll1l1_Krypto_
        l1llll111lll_Krypto_ l1llll111l1l_Krypto_ this function.
    :l1111l11_Krypto_: l11lll11l_Krypto_ l111l111_Krypto_ l1lllll1l_Krypto_ l1llll1l11l1_Krypto_ ``l1llll11ll11_Krypto_`` l111l11l_Krypto_ l1llll1l1_Krypto_
        l11111ll_Krypto_ ``l1llll111111_Krypto_`` type, where l11lll11l_Krypto_ l1lll1ll1ll1_Krypto_
        item is optional. l1llll1111l1_Krypto_ for ``l1lllll1l1_Krypto_/4/5`` l1llll111l11_Krypto_
        ``l1lll1ll1ll1_Krypto_`` l1lll1ll1lll_Krypto_ l1llll1l1_Krypto_ l1llll111lll_Krypto_ l1llll111l1l_Krypto_ this function.
    :l1lll11ll_Krypto_: l1lllll11l1l_Krypto_ ``l1lllllll1l1_Krypto_`` l1111lll1_Krypto_ l1lllll11_Krypto_ string that l111111l1l1_Krypto_ l11lll11l_Krypto_ hash.
    l1l1111_Krypto_ (u"ࠨࠢࠣࠌࠍࠤࠥࠦࠠࠋࠢࠣࠤࠥࠐࠠࠡࠢࠣࠎࠥࠦࠠࠡࠌࠣࠤࠥࠦࠊࠡࠢࠣࠤࠏࠦࠠࠡࠢࠍࠤࠥࠦࠠࠋࠢࠣࠤࠥࠐࠠࠡࠢࠣࠎࠥࠦࠠࠡࠌࠣࠤࠥࠦࠊࠡࠢࠣࠤࠏࠦࠠࠡࠢࠍࠤࠥࠦࠠࠋࠢࠣࠤࠥࠐࠠࠡࠢࠣࠎࠥࠦࠠࠡࠌࠣࠤࠥࠦࠊࠡࠢࠣࠤࡩ࡯ࡧࡦࡵࡷࡅࡱ࡭࡯ࠡࠢࡀࠤࡉ࡫ࡲࡔࡧࡴࡹࡪࡴࡣࡦࠪ࡞࡬ࡦࡹࡨ࠯ࡱ࡬ࡨ࠱ࠦࡄࡦࡴࡑࡹࡱࡲࠨࠪ࠰ࡨࡲࡨࡵࡤࡦࠪࠬࡡ࠮ࠐࠠࠡࠢࠣࡨ࡮࡭ࡥࡴࡶࠣࠤࠥࠦࠠࠡ࠿ࠣࡈࡪࡸࡏࡤࡶࡨࡸࡘࡺࡲࡪࡰࡪࠬ࡭ࡧࡳࡩ࠰ࡧ࡭࡬࡫ࡳࡵࠪࠬ࠭ࠏࠦࠠࠡࠢࡧ࡭࡬࡫ࡳࡵࡋࡱࡪࡴࠦࠠ࠾ࠢࡇࡩࡷ࡙ࡥࡲࡷࡨࡲࡨ࡫ࠨ࡜ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡦ࡬࡫ࡪࡹࡴࡂ࡮ࡪࡳ࠳࡫࡮ࡤࡱࡧࡩ࠭࠯ࠬࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡥ࡫ࡪࡩࡸࡺ࠮ࡦࡰࡦࡳࡩ࡫ࠨࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࡟ࠬ࠲ࡪࡴࡣࡰࡦࡨࠬ࠮ࠐࠊࠡࠢࠣࠤࠏࠦࠠࠡࠢࠍࠤࠥࠦࠠࡪࡨࠣࡩࡲࡒࡥ࡯࠾࡯ࡩࡳ࠮ࡤࡪࡩࡨࡷࡹࡏ࡮ࡧࡱࠬ࠯࠶࠷࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡵࡥ࡮ࡹࡥࠡࡘࡤࡰࡺ࡫ࡅࡳࡴࡲࡶ࠭ࠨࡓࡦ࡮ࡨࡧࡹ࡫ࡤࠡࡪࡤࡷ࡭ࠦࡡ࡭ࡩࡲࡶ࡮ࡺࡨࠡࡪࡤࡷࠥࡧࠠࡵࡱࡲࠤࡱࡵ࡮ࡨࠢࡧ࡭࡬࡫ࡳࡵࠢࠫࠩࡩࠦࡢࡺࡶࡨࡷ࠮࠴ࠢࠡࠧࠣࡰࡪࡴࠨࡥ࡫ࡪࡩࡸࡺࠩࠪࠌࠣࠤࠥࠦࡐࡔࠢࡀࠤࡧࡩࡨࡳࠪ࠳ࡼࡋࡌࠩࠡࠬࠣࠬࡪࡳࡌࡦࡰࠣ࠱ࠥࡲࡥ࡯ࠪࡧ࡭࡬࡫ࡳࡵࡋࡱࡪࡴ࠯ࠠ࠮ࠢ࠶࠭ࠏࠦࠠࠡࠢࡵࡩࡹࡻࡲ࡯ࠢࡥࠬࠧࡢࡸ࠱࠲࡟ࡼ࠵࠷ࠢࠪࠢ࠮ࠤࡕ࡙ࠠࠬࠢࡥࡧ࡭ࡸࠨ࠱ࡺ࠳࠴࠮ࠦࠫࠡࡦ࡬࡫ࡪࡹࡴࡊࡰࡩࡳࠏࠐࡤࡦࡨࠣࡲࡪࡽࠨ࡬ࡧࡼ࠭࠿ࠐࠠࠡࠢࠣࠦࠧࠨᨪ")l1lll11ll_Krypto_ a signature l1lllll1ll1l_Krypto_ object `l1llll111ll1_Krypto_` that
    l1l1l111l_Krypto_ l1llll1l1_Krypto_ l1l11l1ll_Krypto_ l111l11l_Krypto_ l1ll1ll1l_Krypto_ l1l111l11_Krypto_
    :l11lllll1_Krypto_:
     key : l1l11lll1_Krypto_ key object
      l1l11ll11_Krypto_ key l111l11l_Krypto_ l1l11l11l_Krypto_ l111l11l_Krypto_ l1l11lll11_Krypto_ or l1l11l1l11_Krypto_ l11lll11l_Krypto_ message. l1l1111l1_Krypto_ is a `l111ll1_Krypto_.l11l11l1_Krypto_.l1l11lll1_Krypto_` object.
      l1llll1l11ll_Krypto_ is l111ll11_Krypto_ possible if *key* is a l1l111ll1_Krypto_ l1l11lll1_Krypto_ key.
    l1l1111_Krypto_ (u"ࠢࠣᨫ")"
    return l1llll111ll1_Krypto_(key)