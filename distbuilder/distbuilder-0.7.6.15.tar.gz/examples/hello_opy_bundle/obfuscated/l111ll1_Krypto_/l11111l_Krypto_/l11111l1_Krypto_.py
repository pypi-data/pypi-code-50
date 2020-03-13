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
l1l1111_Krypto_ (u"ࠦࠧࠨࡒࡔࡃࠣࡩࡳࡩࡲࡺࡲࡷ࡭ࡴࡴࠠࡱࡴࡲࡸࡴࡩ࡯࡭ࠢࡤࡧࡨࡵࡲࡥ࡫ࡱ࡫ࠥࡺ࡯ࠡࡒࡎࡇࡘࠐࠊࡔࡧࡨࠤࡗࡌࡃ࠴࠶࠷࠻ࡤࡥࠠࡰࡴࠣࡸ࡭࡫ࠠࡡࡱࡵ࡭࡬࡯࡮ࡢ࡮ࠣࡖࡘࡇࠠࡍࡣࡥࡷࠥࡹࡰࡦࡥ࡬ࡪ࡮ࡩࡡࡵ࡫ࡲࡲࡥࡥ࡟ࠡ࠰ࠍࠎ࡙࡮ࡩࡴࠢࡶࡧ࡭࡫࡭ࡦࠢ࡬ࡷࠥࡳ࡯ࡳࡧࠣࡴࡷࡵࡰࡦࡴ࡯ࡽࠥࡩࡡ࡭࡮ࡨࡨࠥࡦࡠࡓࡕࡄࡉࡘ࠳ࡏࡂࡇࡓࡤࡥ࠴ࠊࠋࡃࡶࠤࡦࡴࠠࡦࡺࡤࡱࡵࡲࡥ࠭ࠢࡤࠤࡸ࡫࡮ࡥࡧࡵࠤࡲࡧࡹࠡࡧࡱࡧࡷࡿࡰࡵࠢࡤࠤࡲ࡫ࡳࡴࡣࡪࡩࠥ࡯࡮ࠡࡶ࡫࡭ࡸࠦࡷࡢࡻ࠽ࠎࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠾࠿ࡀࠣࡪࡷࡵ࡭ࠡࡅࡵࡽࡵࡺ࡯࠯ࡅ࡬ࡴ࡭࡫ࡲࠡ࡫ࡰࡴࡴࡸࡴࠡࡒࡎࡇࡘ࠷࡟ࡐࡃࡈࡔࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠾࠿ࡀࠣࡪࡷࡵ࡭ࠡࡅࡵࡽࡵࡺ࡯࠯ࡒࡸࡦࡱ࡯ࡣࡌࡧࡼࠤ࡮ࡳࡰࡰࡴࡷࠤࡗ࡙ࡁࠋࠢࠣࠤࠥࠦࠠࠡࠢࡁࡂࡃࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠿ࡀࡁࠤࡲ࡫ࡳࡴࡣࡪࡩࠥࡃࠠࠨࡖࡲࠤࡧ࡫ࠠࡦࡰࡦࡶࡾࡶࡴࡦࡦࠪࠎࠥࠦࠠࠡࠢࠣࠤࠥࡄ࠾࠿ࠢ࡮ࡩࡾࠦ࠽ࠡࡔࡖࡅ࠳࡯࡭ࡱࡱࡵࡸࡐ࡫ࡹࠩࡱࡳࡩࡳ࠮ࠧࡱࡷࡥ࡯ࡪࡿ࠮ࡥࡧࡵࠫ࠮࠴ࡲࡦࡣࡧࠬ࠮࠯ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡀࡁࡂࠥࡩࡩࡱࡪࡨࡶࠥࡃࠠࡑࡍࡆࡗ࠶ࡥࡏࡂࡇࡓ࠲ࡳ࡫ࡷࠩ࡭ࡨࡽ࠮ࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠿ࡀࡁࠤࡨ࡯ࡰࡩࡧࡵࡸࡪࡾࡴࠡ࠿ࠣࡧ࡮ࡶࡨࡦࡴ࠱ࡩࡳࡩࡲࡺࡲࡷࠬࡲ࡫ࡳࡴࡣࡪࡩ࠮ࠐࠊࡂࡶࠣࡸ࡭࡫ࠠࡳࡧࡦࡩ࡮ࡼࡥࡳࠢࡶ࡭ࡩ࡫ࠬࠡࡦࡨࡧࡷࡿࡰࡵ࡫ࡲࡲࠥࡩࡡ࡯ࠢࡥࡩࠥࡪ࡯࡯ࡧࠣࡹࡸ࡯࡮ࡨࠢࡷ࡬ࡪࠦࡰࡳ࡫ࡹࡥࡹ࡫ࠠࡱࡣࡵࡸࠥࡵࡦࠋࡶ࡫ࡩࠥࡘࡓࡂࠢ࡮ࡩࡾࡀࠊࠋࠢࠣࠤࠥࠦࠠࠡࠢࡁࡂࡃࠦ࡫ࡦࡻࠣࡁࠥࡘࡓࡂ࠰࡬ࡱࡵࡵࡲࡵࡍࡨࡽ࠭ࡵࡰࡦࡰࠫࠫࡵࡸࡩࡷ࡭ࡨࡽ࠳ࡪࡥࡳࠩࠬ࠲ࡷ࡫ࡡࡥࠪࠬ࠭ࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠾࠿ࡀࠣࡧ࡮ࡶࡨࡦࡴࠣࡁࠥࡖࡋࡄࡕ࠴ࡣࡔࡇࡐ࠯ࡰࡨࡻ࠭ࡱࡥࡺࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࡃࡄ࠾ࠡ࡯ࡨࡷࡸࡧࡧࡦࠢࡀࠤࡨ࡯ࡰࡩࡧࡵ࠲ࡩ࡫ࡣࡳࡻࡳࡸ࠭ࡩࡩࡱࡪࡨࡶࡹ࡫ࡸࡵࠫࠍࠎ࠿ࡻ࡮ࡥࡱࡦࡹࡲ࡫࡮ࡵࡧࡧ࠾ࠥࡥ࡟ࡳࡧࡹ࡭ࡸ࡯࡯࡯ࡡࡢ࠰ࠥࡥ࡟ࡱࡣࡦ࡯ࡦ࡭ࡥࡠࡡࠍࠎ࠳࠴ࠠࡠࡡ࠽ࠤ࡭ࡺࡴࡱ࠼࠲࠳ࡼࡽࡷ࠯࡫ࡨࡸ࡫࠴࡯ࡳࡩ࠲ࡶ࡫ࡩ࠯ࡳࡨࡦ࠷࠹࠺࠷࠯ࡶࡻࡸࠏ࠴࠮ࠡࡡࡢ࠾ࠥ࡮ࡴࡵࡲ࠽࠳࠴ࡽࡷࡸ࠰ࡵࡷࡦ࠴ࡣࡰ࡯࠲ࡶࡸࡧ࡬ࡢࡤࡶ࠳ࡳࡵࡤࡦ࠰ࡤࡷࡵࡅࡩࡥ࠿࠵࠵࠷࠻࠮ࠋࠤࠥࠦࡩ")
__revision__ = l1l1111_Krypto_ (u"ࠧࠪࡉࡥࠦࠥࡪ")
__all__ = [ l1l1111_Krypto_ (u"࠭࡮ࡦࡹࠪ࡫"), l1l1111_Krypto_ (u"ࠧࡑࡍࡆࡗ࠶ࡕࡁࡆࡒࡢࡇ࡮ࡶࡨࡦࡴࠪ࡬") ]
import l111ll1_Krypto_.Signature.l11llllll_Krypto_
import l111ll1_Krypto_.l1lll1ll1_Krypto_.l1l111lll_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
import l111ll1_Krypto_.l1l111ll_Krypto_.l111l1ll_Krypto_
from   l111ll1_Krypto_.l1l111ll_Krypto_.l111l1ll_Krypto_ import l1ll11111_Krypto_
from   l111ll1_Krypto_.l1l111ll_Krypto_.l1ll1ll11_Krypto_ import l1ll1ll11_Krypto_
class l1111lll_Krypto_:
    l1l1111_Krypto_ (u"ࠣࠤࠥࡘ࡭࡯ࡳࠡࡥ࡬ࡴ࡭࡫ࡲࠡࡥࡤࡲࠥࡶࡥࡳࡨࡲࡶࡲࠦࡐࡌࡅࡖࠎࠏࠦࠠࠡࠢࡧࡩ࡫ࠦ࡟ࡠ࡫ࡱ࡭ࡹࡥ࡟ࠩࡵࡨࡰ࡫࠲ࠠ࡬ࡧࡼ࠰ࠥ࡮ࡡࡴࡪࡄࡰ࡬ࡵࠬࠡ࡯ࡪࡪࡺࡴࡣ࠭ࠢ࡯ࡥࡧ࡫࡬ࠪ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢ࡭")l1l1ll1l1_Krypto_ this l1l111l11_Krypto_
        :l11lllll1_Krypto_:
         key : l1lllllll_Krypto_ l1l11lll1_Krypto_ key object
          l1ll111l1_Krypto_ a l1l111ll1_Krypto_ l11ll1ll1_Krypto_ is given, l1lll11l1_Krypto_ l1l1ll111_Krypto_ and l1l11l1l1_Krypto_ l1ll1l1l1_Krypto_ possible.
          l1ll111l1_Krypto_ a l1llll1ll_Krypto_ l11ll1ll1_Krypto_ is given, l111ll11_Krypto_ l1l1ll111_Krypto_ is possible.
         l1l1l1lll_Krypto_ : hash object
                l1l11ll11_Krypto_ hash function l111l11l_Krypto_ l1l11l11l_Krypto_. l1l1111l1_Krypto_ l1l1l111l_Krypto_ l1llll1l1_Krypto_ a module l1ll1l11l_Krypto_ `l111ll1_Krypto_.l1lll1ll1_Krypto_`
                or l1lllllll_Krypto_ l1ll111ll_Krypto_ hash object l1ll11l1l_Krypto_ from any l11111ll_Krypto_ l1l1l1l11_Krypto_ modules. l1ll111l1_Krypto_ not l111llll_Krypto_,
                `l111ll1_Krypto_.l1lll1ll1_Krypto_.l1l111lll_Krypto_` (that is, l1l111lll_Krypto_-1) is l1l11l1ll_Krypto_.
         l1l1lllll_Krypto_ : callable
                A mask l1111l1l_Krypto_ function that l1l1lll11_Krypto_ l11ll1l1l_Krypto_ parameters: a string l111l11l_Krypto_
                l1l11l11l_Krypto_ as l1ll1111l_Krypto_, and l11lll11l_Krypto_ l1l1l1111_Krypto_ l11111ll_Krypto_ l11lll11l_Krypto_ mask l111l11l_Krypto_ l1llllll1_Krypto_, in bytes.
                l1ll111l1_Krypto_ not l111llll_Krypto_, l11lll11l_Krypto_ l1lllll1l_Krypto_ l1ll11lll_Krypto_ is l1l11l1ll_Krypto_ (a l1l11l111_Krypto_ l1l1111ll_Krypto_).
         label : string
                A label l111l11l_Krypto_ l11l11ll_Krypto_ l111l11l_Krypto_ this l1l11ll1l_Krypto_ l1l1ll111_Krypto_. l1ll111l1_Krypto_ not l111llll_Krypto_,
                l1lllllll_Krypto_ empty string is l1l11l1ll_Krypto_. l11llll11_Krypto_ a label l111111l_Krypto_ not l1ll11ll1_Krypto_
                l1l111111_Krypto_.
        :l1111l11_Krypto_: l11lll1ll_Krypto_ l11lll11l_Krypto_ mask l1111l1l_Krypto_ function l111ll11_Krypto_ if l1l11111l_Krypto_ l1111ll1_Krypto_ l11lll111_Krypto_ l1l11111l_Krypto_ l1ll1l1l1_Krypto_ l1l1ll11l_Krypto_.
                    l11ll1lll_Krypto_ and l11l1111_Krypto_ l1l1l1ll1_Krypto_ l1l11l11l_Krypto_ l11lll11l_Krypto_ l111l111_Krypto_ l1l1lll1l_Krypto_.
        l1l1111_Krypto_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡳࡦ࡮ࡩ࠲ࡤࡱࡥࡺࠢࡀࠤࡰ࡫ࡹࠋࠌࠣࠤࠥࠦࠠࠡࠢࠣ࡭࡫ࠦࡨࡢࡵ࡫ࡅࡱ࡭࡯࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡴࡧ࡯ࡪ࠳ࡥࡨࡢࡵ࡫ࡓࡧࡰࠠ࠾ࠢ࡫ࡥࡸ࡮ࡁ࡭ࡩࡲࠎࠥࠦࠠࠡࠢࠣࠤࠥ࡫࡬ࡴࡧ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡶࡩࡱ࡬࠮ࡠࡪࡤࡷ࡭ࡕࡢ࡫ࠢࡀࠤࡈࡸࡹࡱࡶࡲ࠲ࡍࡧࡳࡩ࠰ࡖࡌࡆࠐࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡫ࡩࠤࡲ࡭ࡦࡶࡰࡦ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡷࡪࡲࡦ࠯ࡡࡰ࡫࡫ࠦ࠽ࠡ࡯ࡪࡪࡺࡴࡣࠋࠢࠣࠤࠥࠦࠠࠡࠢࡨࡰࡸ࡫࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡳࡦ࡮ࡩ࠲ࡤࡳࡧࡧࠢࡀࠤࡱࡧ࡭ࡣࡦࡤࠤࡽ࠲ࡹ࠻ࠢࡆࡶࡾࡶࡴࡰ࠰ࡖ࡭࡬ࡴࡡࡵࡷࡵࡩ࠳ࡖࡋࡄࡕ࠴ࡣࡕ࡙ࡓ࠯ࡏࡊࡊ࠶࠮ࡸ࠭ࡻ࠯ࡷࡪࡲࡦ࠯ࡡ࡫ࡥࡸ࡮ࡏࡣ࡬ࠬࠎࠏࠦࠠࠡࠢࠣࠤࠥࠦࡳࡦ࡮ࡩ࠲ࡤࡲࡡࡣࡧ࡯ࠤࡂࠦ࡬ࡢࡤࡨࡰࠏࠐࠠࠡࠢࠣࡨࡪ࡬ࠠࡤࡣࡱࡣࡪࡴࡣࡳࡻࡳࡸ࠭ࡹࡥ࡭ࡨࠬ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤ࡮")l1lll11ll_Krypto_ True/1 if this l1llll11l_Krypto_ object l1l1l111l_Krypto_ l1llll1l1_Krypto_ l1l11l1ll_Krypto_ for l1l1ll111_Krypto_.l1l1111_Krypto_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡳࡧࡷࡹࡷࡴࠠࡴࡧ࡯ࡪ࠳ࡥ࡫ࡦࡻ࠱ࡧࡦࡴ࡟ࡦࡰࡦࡶࡾࡶࡴࠩࠫࠍࠎࠥࠦࠠࠡࡦࡨࡪࠥࡩࡡ࡯ࡡࡧࡩࡨࡸࡹࡱࡶࠫࡷࡪࡲࡦࠪ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢ࡯")l1lll11ll_Krypto_ True/1 if this l1llll11l_Krypto_ object l1l1l111l_Krypto_ l1llll1l1_Krypto_ l1l11l1ll_Krypto_ for l1l11l1l1_Krypto_.l1l1111_Krypto_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡴࡨࡸࡺࡸ࡮ࠡࡵࡨࡰ࡫࠴࡟࡬ࡧࡼ࠲ࡨࡧ࡮ࡠࡦࡨࡧࡷࡿࡰࡵࠪࠬࠎࠏࠦࠠࠡࠢࡧࡩ࡫ࠦࡥ࡯ࡥࡵࡽࡵࡺࠨࡴࡧ࡯ࡪ࠱ࠦ࡭ࡦࡵࡶࡥ࡬࡫ࠩ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨࡰ")l1l1l1l1l_Krypto_ l11lll11l_Krypto_ l1l111l11_Krypto_
        l1l1111l1_Krypto_ function is named ``l1lll1l1l_Krypto_-l1111111_Krypto_-l1l1ll1ll_Krypto_``, and is l111llll_Krypto_ in
        section 7.1.1 l11111ll_Krypto_ l1llll111_Krypto_.
        :l11lllll1_Krypto_:
         message : string
                l1l11ll11_Krypto_ message l111l11l_Krypto_ l1_Krypto_, l1ll1llll_Krypto_ l1lll111l_Krypto_ as l1ll11l1_Krypto_. l1ll1l111_Krypto_ l1l1l111l_Krypto_ l1llll1l1_Krypto_ l11111ll_Krypto_
                l1lll1l11_Krypto_ length, l11l111l_Krypto_ not l1l1l11l1_Krypto_ l1l1l11ll_Krypto_ l11lll11l_Krypto_ l1l11lll1_Krypto_ l111lll1_Krypto_ (in bytes)
                l1l1llll1_Krypto_ 2, l1l1llll1_Krypto_ l11lll1l1_Krypto_ l11lll11l_Krypto_ hash output size.
        :l1lll11ll_Krypto_: A string, l11lll11l_Krypto_ l1ll111l_Krypto_ in which l11lll11l_Krypto_ message is l11l1ll1_Krypto_.
            l1ll1l111_Krypto_ is as l1lllll11_Krypto_ as l11lll11l_Krypto_ l1l11lll1_Krypto_ l111lll1_Krypto_ (in bytes).
        :l1l111l1l_Krypto_ ValueError:
            l1ll111l1_Krypto_ l11lll11l_Krypto_ l1l11lll1_Krypto_ key length is not l11l1l11_Krypto_ l1lllll11_Krypto_ l111l11l_Krypto_ l1ll1lll1_Krypto_ with l11lll11l_Krypto_ given
            message.
        l1l1111_Krypto_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢࡵࡥࡳࡪࡆࡶࡰࡦࠤࡂࠦࡳࡦ࡮ࡩ࠲ࡤࡱࡥࡺ࠰ࡢࡶࡦࡴࡤࡧࡷࡱࡧࠏࠦࠠࠡࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦ࡭ࡰࡦࡅ࡭ࡹࡹࠠ࠾ࠢࡆࡶࡾࡶࡴࡰ࠰ࡘࡸ࡮ࡲ࠮࡯ࡷࡰࡦࡪࡸ࠮ࡴ࡫ࡽࡩ࠭ࡹࡥ࡭ࡨ࠱ࡣࡰ࡫ࡹ࠯ࡰࠬࠎࠥࠦࠠࠡࠢࠣࠤࠥࡱࠠ࠾ࠢࡦࡩ࡮ࡲ࡟ࡥ࡫ࡹࠬࡲࡵࡤࡃ࡫ࡷࡷ࠱࠾ࠩࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣ࡬ࡑ࡫࡮ࠡ࠿ࠣࡷࡪࡲࡦ࠯ࡡ࡫ࡥࡸ࡮ࡏࡣ࡬࠱ࡨ࡮࡭ࡥࡴࡶࡢࡷ࡮ࢀࡥࠋࠢࠣࠤࠥࠦࠠࠡࠢࡰࡐࡪࡴࠠ࠾ࠢ࡯ࡩࡳ࠮࡭ࡦࡵࡶࡥ࡬࡫ࠩࠋࠢࠣࠤࠥࠐࠠࠡࠢࠣࠤࠥࠦࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢࡳࡷࡤࡲࡥ࡯ࠢࡀࠤࡰ࠳࡭ࡍࡧࡱ࠱࠷࠰ࡨࡍࡧࡱ࠱࠷ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡪࡨࠣࡴࡸࡥ࡬ࡦࡰ࠿࠴࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡷࡧࡩࡴࡧ࡚ࠣࡦࡲࡵࡦࡇࡵࡶࡴࡸࠨࠣࡒ࡯ࡥ࡮ࡴࡴࡦࡺࡷࠤ࡮ࡹࠠࡵࡱࡲࠤࡱࡵ࡮ࡨ࠰ࠥ࠭ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡮ࡋࡥࡸ࡮ࠠ࠾ࠢࡶࡩࡱ࡬࠮ࡠࡪࡤࡷ࡭ࡕࡢ࡫࠰ࡱࡩࡼ࠮ࡳࡦ࡮ࡩ࠲ࡤࡲࡡࡣࡧ࡯࠭࠳ࡪࡩࡨࡧࡶࡸ࠭࠯ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࡴࡸࠦ࠽ࠡࡤࡦ࡬ࡷ࠮࠰ࡹ࠲࠳࠭࠯ࡶࡳࡠ࡮ࡨࡲࠏࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࡦࡥࠤࡂࠦ࡬ࡉࡣࡶ࡬ࠥ࠱ࠠࡱࡵࠣ࠯ࠥࡨࡣࡩࡴࠫ࠴ࡽ࠶࠱ࠪࠢ࠮ࠤࡲ࡫ࡳࡴࡣࡪࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࡴࡲࡷࠥࡃࠠࡳࡣࡱࡨࡋࡻ࡮ࡤࠪ࡫ࡐࡪࡴࠩࠋࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤࡩࡨࡍࡢࡵ࡮ࠤࡂࠦࡳࡦ࡮ࡩ࠲ࡤࡳࡧࡧࠪࡵࡳࡸ࠲ࠠ࡬࠯࡫ࡐࡪࡴ࠭࠲ࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦ࡭ࡢࡵ࡮ࡩࡩࡊࡂࠡ࠿ࠣࡷࡹࡸࡸࡰࡴࠫࡨࡧ࠲ࠠࡥࡤࡐࡥࡸࡱࠩࠋࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤࡸ࡫ࡥࡥࡏࡤࡷࡰࠦ࠽ࠡࡵࡨࡰ࡫࠴࡟࡮ࡩࡩࠬࡲࡧࡳ࡬ࡧࡧࡈࡇ࠲ࠠࡩࡎࡨࡲ࠮ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢࡰࡥࡸࡱࡥࡥࡕࡨࡩࡩࠦ࠽ࠡࡵࡷࡶࡽࡵࡲࠩࡴࡲࡷ࠱ࠦࡳࡦࡧࡧࡑࡦࡹ࡫ࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࠎࠥࠦࠠࠡࠢࠣࠤࠥ࡫࡭ࠡ࠿ࠣࡦࡨ࡮ࡲࠩ࠲ࡻ࠴࠵࠯ࠠࠬࠢࡰࡥࡸࡱࡥࡥࡕࡨࡩࡩࠦࠫࠡ࡯ࡤࡷࡰ࡫ࡤࡅࡄࠍࠤࠥࠦࠠࠡࠢࠣࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦ࡭ࠡ࠿ࠣࡷࡪࡲࡦ࠯ࡡ࡮ࡩࡾ࠴ࡥ࡯ࡥࡵࡽࡵࡺࠨࡦ࡯࠯ࠤ࠵࠯࡛࠱࡟ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦࡣࠡ࠿ࠣࡦࡨ࡮ࡲࠩ࠲ࡻ࠴࠵࠯ࠪࠩ࡭࠰ࡰࡪࡴࠨ࡮ࠫࠬࠤ࠰ࠦ࡭ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡵࡩࡹࡻࡲ࡯ࠢࡦࠎࠥࠦࠠࠡࠌࠣࠤࠥࠦࡤࡦࡨࠣࡨࡪࡩࡲࡺࡲࡷࠬࡸ࡫࡬ࡧ࠮ࠣࡧࡹ࠯࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧࡱ")l1lll1lll_Krypto_ a l1l111l11_Krypto_
        l1l1111l1_Krypto_ function is named ``l1lll1l1l_Krypto_-l1111111_Krypto_-l11llll1l_Krypto_``, and is l111llll_Krypto_ in
        section 7.1.2 l11111ll_Krypto_ l1llll111_Krypto_.
        :l11lllll1_Krypto_:
         ct : string
                l1l11ll11_Krypto_ l1ll111l_Krypto_ that contains l11lll11l_Krypto_ message l111l11l_Krypto_ l1l11llll_Krypto_.
        :l1lll11ll_Krypto_: A string, l11lll11l_Krypto_ l1lll1111_Krypto_ message.
        :l1l111l1l_Krypto_ ValueError:
            l1ll111l1_Krypto_ l11lll11l_Krypto_ l1ll111l_Krypto_ length is l11l1l1l_Krypto_, or if l11lll11l_Krypto_ l1l11l1l1_Krypto_ l111111l_Krypto_ not
            l111ll1l_Krypto_.
        :l1l111l1l_Krypto_ TypeError:
            l1ll111l1_Krypto_ l11lll11l_Krypto_ l1l11lll1_Krypto_ key l111l1l1_Krypto_ l1ll11l11_Krypto_ l1l111ll1_Krypto_ l11ll1ll1_Krypto_.
        l1l1111_Krypto_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࠎࠥࠦࠠࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࠎࠥࠦࠠࠡࠢࠣࠤࠥࡳ࡯ࡥࡄ࡬ࡸࡸࠦ࠽ࠡࡅࡵࡽࡵࡺ࡯࠯ࡗࡷ࡭ࡱ࠴࡮ࡶ࡯ࡥࡩࡷ࠴ࡳࡪࡼࡨࠬࡸ࡫࡬ࡧ࠰ࡢ࡯ࡪࡿ࠮࡯ࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࡰࠦ࠽ࠡࡥࡨ࡭ࡱࡥࡤࡪࡸࠫࡱࡴࡪࡂࡪࡶࡶ࠰࠽࠯ࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢ࡫ࡐࡪࡴࠠ࠾ࠢࡶࡩࡱ࡬࠮ࡠࡪࡤࡷ࡭ࡕࡢ࡫࠰ࡧ࡭࡬࡫ࡳࡵࡡࡶ࡭ࡿ࡫ࠊࠡࠢࠣࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡫ࡩࠤࡱ࡫࡮ࠩࡥࡷ࠭ࠥࠧ࠽ࠡ࡭ࠣࡳࡷࠦ࡫࠽ࡪࡏࡩࡳ࠱࠲࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡳࡣ࡬ࡷࡪࠦࡖࡢ࡮ࡸࡩࡊࡸࡲࡰࡴࠫࠦࡈ࡯ࡰࡩࡧࡵࡸࡪࡾࡴࠡࡹ࡬ࡸ࡭ࠦࡩ࡯ࡥࡲࡶࡷ࡫ࡣࡵࠢ࡯ࡩࡳ࡭ࡴࡩ࠰ࠥ࠭ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡯ࠣࡁࠥࡹࡥ࡭ࡨ࠱ࡣࡰ࡫ࡹ࠯ࡦࡨࡧࡷࡿࡰࡵࠪࡦࡸ࠮ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢࡨࡱࠥࡃࠠࡣࡥ࡫ࡶ࠭࠶ࡸ࠱࠲ࠬ࠮࠭ࡱ࠭࡭ࡧࡱࠬࡲ࠯ࠩࠡ࠭ࠣࡱࠏࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡮ࡋࡥࡸ࡮ࠠ࠾ࠢࡶࡩࡱ࡬࠮ࡠࡪࡤࡷ࡭ࡕࡢ࡫࠰ࡱࡩࡼ࠮ࡳࡦ࡮ࡩ࠲ࡤࡲࡡࡣࡧ࡯࠭࠳ࡪࡩࡨࡧࡶࡸ࠭࠯ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࡽࠥࡃࠠࡦ࡯࡞࠴ࡢࠐࠠࠡࠢࠣࠤࠥࠦࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤࡲࡧࡳ࡬ࡧࡧࡗࡪ࡫ࡤࠡ࠿ࠣࡩࡲࡡ࠱࠻ࡪࡏࡩࡳ࠱࠱࡞ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡱࡦࡹ࡫ࡦࡦࡇࡆࠥࡃࠠࡦ࡯࡞࡬ࡑ࡫࡮ࠬ࠳࠽ࡡࠏࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࡵࡨࡩࡩࡓࡡࡴ࡭ࠣࡁࠥࡹࡥ࡭ࡨ࠱ࡣࡲ࡭ࡦࠩ࡯ࡤࡷࡰ࡫ࡤࡅࡄ࠯ࠤ࡭ࡒࡥ࡯ࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦࡳࡦࡧࡧࠤࡂࠦࡳࡵࡴࡻࡳࡷ࠮࡭ࡢࡵ࡮ࡩࡩ࡙ࡥࡦࡦ࠯ࠤࡸ࡫ࡥࡥࡏࡤࡷࡰ࠯ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࡨࡧࡓࡡࡴ࡭ࠣࡁࠥࡹࡥ࡭ࡨ࠱ࡣࡲ࡭ࡦࠩࡵࡨࡩࡩ࠲ࠠ࡬࠯࡫ࡐࡪࡴ࠭࠲ࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦࡤࡣࠢࡀࠤࡸࡺࡲࡹࡱࡵࠬࡲࡧࡳ࡬ࡧࡧࡈࡇ࠲ࠠࡥࡤࡐࡥࡸࡱࠩࠋࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤࡻࡧ࡬ࡪࡦࠣࡁࠥ࠷ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡱࡱࡩࠥࡃࠠࡥࡤ࡞࡬ࡑ࡫࡮࠻࡟࠱ࡪ࡮ࡴࡤࠩࡤࡦ࡬ࡷ࠮࠰ࡹ࠲࠴࠭࠮ࠐࠠࠡࠢࠣࠤࠥࠦࠠ࡭ࡊࡤࡷ࡭࠷ࠠ࠾ࠢࡧࡦࡠࡀࡨࡍࡧࡱࡡࠏࠦࠠࠡࠢࠣࠤࠥࠦࡩࡧࠢ࡯ࡌࡦࡹࡨ࠲ࠣࡀࡰࡍࡧࡳࡩ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡸࡤࡰ࡮ࡪࠠ࠾ࠢ࠳ࠎࠥࠦࠠࠡࠢࠣࠤࠥ࡯ࡦࠡࡱࡱࡩࡁ࠶࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡶࡢ࡮࡬ࡨࠥࡃࠠ࠱ࠌࠣࠤࠥࠦࠠࠡࠢࠣ࡭࡫ࠦࡢࡰࡴࡧࠬࡾ࠯ࠡ࠾࠲࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡹࡥࡱ࡯ࡤࠡ࠿ࠣ࠴ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡩࡧࠢࡱࡳࡹࠦࡶࡢ࡮࡬ࡨ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡷࡧࡩࡴࡧ࡚ࠣࡦࡲࡵࡦࡇࡵࡶࡴࡸࠨࠣࡋࡱࡧࡴࡸࡲࡦࡥࡷࠤࡩ࡫ࡣࡳࡻࡳࡸ࡮ࡵ࡮࠯ࠤࠬࠎࠥࠦࠠࠡࠢࠣࠤࠥࠐࠠࠡࠢࠣࠤࠥࠦࠠࡳࡧࡷࡹࡷࡴࠠࡥࡤ࡞࡬ࡑ࡫࡮ࠬࡱࡱࡩ࠰࠷࠺࡞ࠌࠍࡨࡪ࡬ࠠ࡯ࡧࡺࠬࡰ࡫ࡹ࠭ࠢ࡫ࡥࡸ࡮ࡁ࡭ࡩࡲࡁࡓࡵ࡮ࡦ࠮ࠣࡱ࡬࡬ࡵ࡯ࡥࡀࡒࡴࡴࡥ࠭ࠢ࡯ࡥࡧ࡫࡬࠾ࡤࠫࠫࠬ࠯ࠩ࠻ࠌࠣࠤࠥࠦࠢࠣࠤࡲ")l1lll11ll_Krypto_ a l1llll11l_Krypto_ object `l1111lll_Krypto_` that l1l1l111l_Krypto_ l1llll1l1_Krypto_ l1l11l1ll_Krypto_ l111l11l_Krypto_ l1ll1ll1l_Krypto_ l1l111l11_Krypto_
    :l11lllll1_Krypto_:
     key : l1l11lll1_Krypto_ key object
      l1l11ll11_Krypto_ key l111l11l_Krypto_ l1l11l11l_Krypto_ l111l11l_Krypto_ l1_Krypto_ or l1lllll_Krypto_ l11lll11l_Krypto_ message. l1l1111l1_Krypto_ is a `l111ll1_Krypto_.l11l11l1_Krypto_.l1l11lll1_Krypto_` object.
      l1ll1l1ll_Krypto_ is l111ll11_Krypto_ possible if *key* is a l1l111ll1_Krypto_ l1l11lll1_Krypto_ key.
     l1l1l1lll_Krypto_ : hash object
      l1l11ll11_Krypto_ hash function l111l11l_Krypto_ l1l11l11l_Krypto_. l1l1111l1_Krypto_ l1l1l111l_Krypto_ l1llll1l1_Krypto_ a module l1ll1l11l_Krypto_ `l111ll1_Krypto_.l1lll1ll1_Krypto_`
      or l1lllllll_Krypto_ l1ll111ll_Krypto_ hash object l1ll11l1l_Krypto_ from any l11111ll_Krypto_ l1l1l1l11_Krypto_ modules. l1ll111l1_Krypto_ not l111llll_Krypto_,
      `l111ll1_Krypto_.l1lll1ll1_Krypto_.l1l111lll_Krypto_` (that is, l1l111lll_Krypto_-1) is l1l11l1ll_Krypto_.
     l1l1lllll_Krypto_ : callable
      A mask l1111l1l_Krypto_ function that l1l1lll11_Krypto_ l11ll1l1l_Krypto_ parameters: a string l111l11l_Krypto_
      l1l11l11l_Krypto_ as l1ll1111l_Krypto_, and l11lll11l_Krypto_ l1l1l1111_Krypto_ l11111ll_Krypto_ l11lll11l_Krypto_ mask l111l11l_Krypto_ l1llllll1_Krypto_, in bytes.
      l1ll111l1_Krypto_ not l111llll_Krypto_, l11lll11l_Krypto_ l1lllll1l_Krypto_ l1ll11lll_Krypto_ is l1l11l1ll_Krypto_ (a l1l11l111_Krypto_ l1l1111ll_Krypto_).
     label : string
      A label l111l11l_Krypto_ l11l11ll_Krypto_ l111l11l_Krypto_ this l1l11ll1l_Krypto_ l1l1ll111_Krypto_. l1ll111l1_Krypto_ not l111llll_Krypto_,
      l1lllllll_Krypto_ empty string is l1l11l1ll_Krypto_. l11llll11_Krypto_ a label l111111l_Krypto_ not l1ll11ll1_Krypto_
      l1l111111_Krypto_.
    :l1111l11_Krypto_: l11lll1ll_Krypto_ l11lll11l_Krypto_ mask l1111l1l_Krypto_ function l111ll11_Krypto_ if l1l11111l_Krypto_ l1111ll1_Krypto_ l11lll111_Krypto_ l1l11111l_Krypto_ l1ll1l1l1_Krypto_ l1l1ll11l_Krypto_.
      l11ll1lll_Krypto_ and l11l1111_Krypto_ l1l1l1ll1_Krypto_ l1l11l11l_Krypto_ l11lll11l_Krypto_ l111l111_Krypto_ l1l1lll1l_Krypto_.
    l1l1111_Krypto_ (u"ࠢࠣࡳ")"
    return l1111lll_Krypto_(key, l1l1l1lll_Krypto_, l1l1lllll_Krypto_, label)