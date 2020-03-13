# -*- coding: ascii -*-
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
__revision__ = l1l1111_Krypto_ (u"ࠣࠦࡌࡨࠩࠨ⋉")
__all__ = [l1l1111_Krypto_ (u"ࠩࡦࡩ࡮ࡲ࡟ࡴࡪ࡬ࡪࡹ࠭⋊"), l1l1111_Krypto_ (u"ࠪࡧࡪ࡯࡬ࡠࡦ࡬ࡺࠬ⋋"), l1l1111_Krypto_ (u"ࠫ࡫ࡲ࡯ࡰࡴࡢࡨ࡮ࡼࠧ⋌"), l1l1111_Krypto_ (u"ࠬ࡫ࡸࡢࡥࡷࡣࡱࡵࡧ࠳ࠩ⋍"), l1l1111_Krypto_ (u"࠭ࡥࡹࡣࡦࡸࡤࡪࡩࡷࠩ⋎")]
import sys as l1l11l11_Krypto_
if l1l11l11_Krypto_.version_info[0] == 2 and l1l11l11_Krypto_.version_info[1] == 1:
    from l111ll1_Krypto_.l1l111ll_Krypto_.l1l1ll1l_Krypto_ import *
def l1llll11lll_Krypto_(n, b):
    l1l1111_Krypto_ (u"ࠢࠣࠤࡕࡩࡹࡻࡲ࡯ࠢࡦࡩ࡮ࡲࠨ࡯ࠢ࠲ࠤ࠷࠰ࠪࡣࠫࠣࡻ࡮ࡺࡨࡰࡷࡷࠤࡵ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡣࡱࡽࠥ࡬࡬ࡰࡣࡷ࡭ࡳ࡭࠭ࡱࡱ࡬ࡲࡹࠦ࡯ࡳࠢࡧ࡭ࡻ࡯ࡳࡪࡱࡱࠤࡴࡶࡥࡳࡣࡷ࡭ࡴࡴࡳ࠯ࠌࠍࠤࠥࠦࠠࡕࡪ࡬ࡷࠥ࡯ࡳࠡࡦࡲࡲࡪࠦࡢࡺࠢࡵ࡭࡬࡮ࡴ࠮ࡵ࡫࡭࡫ࡺࡩ࡯ࡩࠣࡲࠥࡨࡹࠡࡤࠣࡦ࡮ࡺࡳࠡࡣࡱࡨࠥ࡯࡮ࡤࡴࡨࡱࡪࡴࡴࡪࡰࡪࠤࡹ࡮ࡥࠡࡴࡨࡷࡺࡲࡴࠡࡤࡼࠤ࠶ࠐࠠࠡࠢࠣ࡭࡫ࠦࡡ࡯ࡻࠣࠫ࠶࠭ࠠࡣ࡫ࡷࡷࠥࡽࡥࡳࡧࠣࡷ࡭࡯ࡦࡵࡧࡧࠤࡴࡻࡴ࠯ࠌࠣࠤࠥࠦࠢࠣࠤ⋏")
    if not isinstance(n, int) or not isinstance(b, int):
        raise TypeError(l1l1111_Krypto_ (u"ࠣࡷࡱࡷࡺࡶࡰࡰࡴࡷࡩࡩࠦ࡯ࡱࡧࡵࡥࡳࡪࠠࡵࡻࡳࡩ࠭ࡹࠩ࠻ࠢࠨࡶࠥࡧ࡮ࡥࠢࠨࡶࠧ⋐") % (type(n).__name__, type(b).__name__))
    assert n >= 0 and b >= 0
    mask = (1 << b) - 1
    if n & mask:
        return (n >> b) + 1
    else:
        return n >> b
def l1ll11111_Krypto_(a, b):
    l1l1111_Krypto_ (u"ࠤࠥࠦࡗ࡫ࡴࡶࡴࡱࠤࡨ࡫ࡩ࡭ࠪࡤࠤ࠴ࠦࡢࠪࠢࡺ࡭ࡹ࡮࡯ࡶࡶࠣࡴࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡢࡰࡼࠤ࡫ࡲ࡯ࡢࡶ࡬ࡲ࡬࠳ࡰࡰ࡫ࡱࡸࠥࡵࡰࡦࡴࡤࡸ࡮ࡵ࡮ࡴ࠰ࠥࠦࠧ⋑")
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError(l1l1111_Krypto_ (u"ࠥࡹࡳࡹࡵࡱࡲࡲࡶࡹ࡫ࡤࠡࡱࡳࡩࡷࡧ࡮ࡥࠢࡷࡽࡵ࡫ࠨࡴࠫ࠽ࠤࠪࡸࠠࡢࡰࡧࠤࠪࡸࠢ⋒") % (type(a).__name__, type(b).__name__))
    (q, r) = divmod(a, b)
    if r:
        return q + 1
    else:
        return q
def l11111l11ll_Krypto_(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError(l1l1111_Krypto_ (u"ࠦࡺࡴࡳࡶࡲࡳࡳࡷࡺࡥࡥࠢࡲࡴࡪࡸࡡ࡯ࡦࠣࡸࡾࡶࡥࠩࡵࠬ࠾ࠥࠫࡲࠡࡣࡱࡨࠥࠫࡲࠣ⋓") % (type(a).__name__, type(b).__name__))
    (q, r) = divmod(a, b)
    return q
def l1llll11l1l_Krypto_(num):
    l1l1111_Krypto_ (u"ࠧࠨࠢࡇ࡫ࡱࡨࠥࡧ࡮ࡥࠢࡵࡩࡹࡻࡲ࡯ࠢࡤࡲࠥ࡯࡮ࡵࡧࡪࡩࡷࠦࡩࠡࡀࡀࠤ࠵ࠦࡳࡶࡥ࡫ࠤࡹ࡮ࡡࡵࠢࡱࡹࡲࠦ࠽࠾ࠢ࠵࠮࠯࡯࠮ࠋࠌࠣࠤࠥࠦࡉࡧࠢࡱࡳࠥࡹࡵࡤࡪࠣ࡭ࡳࡺࡥࡨࡧࡵࠤࡪࡾࡩࡴࡶࡶ࠰ࠥࡺࡨࡪࡵࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥࡸࡡࡪࡵࡨࡷࠥ࡜ࡡ࡭ࡷࡨࡉࡷࡸ࡯ࡳ࠰ࠍࠤࠥࠦࠠࠣࠤࠥ⋔")
    if not isinstance(num, int):
        raise TypeError(l1l1111_Krypto_ (u"ࠨࡵ࡯ࡵࡸࡴࡵࡵࡲࡵࡧࡧࠤࡴࡶࡥࡳࡣࡱࡨࠥࡺࡹࡱࡧ࠽ࠤࠪࡸࠢ⋕") % (type(num).__name__,))
    n = int(num)
    if n <= 0:
        raise ValueError(l1l1111_Krypto_ (u"ࠢࡤࡣࡱࡲࡴࡺࠠࡤࡱࡰࡴࡺࡺࡥࠡ࡮ࡲ࡫ࡦࡸࡩࡵࡪࡰࠤࡴ࡬ࠠ࡯ࡱࡱ࠱ࡵࡵࡳࡪࡶ࡬ࡺࡪࠦ࡮ࡶ࡯ࡥࡩࡷࠨ⋖"))
    i = 0
    while n != 0:
        if (n & 1) and n != 1:
            raise ValueError(l1l1111_Krypto_ (u"ࠣࡐࡲࠤࡸࡵ࡬ࡶࡶ࡬ࡳࡳࠦࡣࡰࡷ࡯ࡨࠥࡨࡥࠡࡨࡲࡹࡳࡪࠢ⋗"))
        i += 1
        n >>= 1
    i -= 1
    assert num == (1 << i)
    return i
def l1llll1l11l_Krypto_(p, d, l11111ll1ll_Krypto_=False):
    l1l1111_Krypto_ (u"ࠤࠥࠦࡋ࡯࡮ࡥࠢࡤࡲࡩࠦࡲࡦࡶࡸࡶࡳࠦࡡ࡯ࠢ࡬ࡲࡹ࡫ࡧࡦࡴࠣࡲࠥࡹࡵࡤࡪࠣࡸ࡭ࡧࡴࠡࡲࠣࡁࡂࠦ࡮ࠡࠬࠣࡨࠏࠐࠠࠡࠢࠣࡍ࡫ࠦ࡮ࡰࠢࡶࡹࡨ࡮ࠠࡪࡰࡷࡩ࡬࡫ࡲࠡࡧࡻ࡭ࡸࡺࡳ࠭ࠢࡷ࡬࡮ࡹࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࡵࡥ࡮ࡹࡥࡴ࡙ࠢࡥࡱࡻࡥࡆࡴࡵࡳࡷ࠴ࠊࠋࠢࠣࠤࠥࡈ࡯ࡵࡪࠣࡳࡵ࡫ࡲࡢࡰࡧࡷࠥࡳࡵࡴࡶࠣࡦࡪࠦࡩ࡯ࡶࡨ࡫ࡪࡸࡳ࠯ࠌࠍࠤࠥࠦࠠࡊࡨࠣࡸ࡭࡫ࠠࡴࡧࡦࡳࡳࡪࠠࡰࡲࡨࡶࡦࡴࡤࠡ࡫ࡶࠤࡿ࡫ࡲࡰ࠮ࠣࡸ࡭࡯ࡳࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡤ࡭ࡸ࡫࡛ࠠࡧࡵࡳࡉ࡯ࡶࡪࡵ࡬ࡳࡳࡋࡲࡳࡱࡵࠎࠥࠦࠠࠡࡷࡱࡰࡪࡹࡳࠡࡣ࡯ࡰࡴࡽ࡟ࡥ࡫ࡹࡾࡪࡸ࡯ࠡ࡫ࡶࠤࡹࡸࡵࡦࠢࠫࡨࡪ࡬ࡡࡶ࡮ࡷ࠾ࠥࡌࡡ࡭ࡵࡨ࠭࠳ࠐࠠࠡࠢࠣࠦࠧࠨ⋘")
    if not isinstance(p, int) or not isinstance(d, int):
        raise TypeError(l1l1111_Krypto_ (u"ࠥࡹࡳࡹࡵࡱࡲࡲࡶࡹ࡫ࡤࠡࡱࡳࡩࡷࡧ࡮ࡥࠢࡷࡽࡵ࡫ࠨࡴࠫ࠽ࠤࠪࡸࠠࡢࡰࡧࠤࠪࡸࠢ⋙") % (type(p).__name__, type(d).__name__))
    if d == 0 and l11111ll1ll_Krypto_:
        n = 0
        if p != n * d:
            raise ValueError(l1l1111_Krypto_ (u"ࠦࡓࡵࠠࡴࡱ࡯ࡹࡹ࡯࡯࡯ࠢࡦࡳࡺࡲࡤࠡࡤࡨࠤ࡫ࡵࡵ࡯ࡦࠥ⋚"))
    else:
        (n, r) = divmod(p, d)
        if r != 0:
            raise ValueError(l1l1111_Krypto_ (u"ࠧࡔ࡯ࠡࡵࡲࡰࡺࡺࡩࡰࡰࠣࡧࡴࡻ࡬ࡥࠢࡥࡩࠥ࡬࡯ࡶࡰࡧࠦ⋛"))
    assert p == n * d
    return n