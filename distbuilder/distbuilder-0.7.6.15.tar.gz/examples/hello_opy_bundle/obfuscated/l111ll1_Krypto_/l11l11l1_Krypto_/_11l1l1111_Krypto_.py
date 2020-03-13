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
__revision__ = l1l1111_Krypto_ (u"ࠨࠤࡊࡦࠧࠦ৬")
from l111ll1_Krypto_.l11l11l1_Krypto_ import l1l111lll1_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_ import l111l1ll_Krypto_
def l1l11l1111_Krypto_(bits, l1l11ll1ll_Krypto_, l1l1111lll_Krypto_=None, e=65537):
    l1l1111_Krypto_ (u"ࠢࠣࠤࡪࡩࡳ࡫ࡲࡢࡶࡨࠬࡧ࡯ࡴࡴ࠼࡬ࡲࡹ࠲ࠠࡳࡣࡱࡨ࡫ࡻ࡮ࡤ࠼ࡦࡥࡱࡲࡡࡣ࡮ࡨ࠰ࠥࡶࡲࡰࡩࡵࡩࡸࡹ࡟ࡧࡷࡱࡧ࠿ࡩࡡ࡭࡮ࡤࡦࡱ࡫ࠬࠡࡧ࠽࡭ࡳࡺࠩࠋࠌࠣࠤࠥࠦࡇࡦࡰࡨࡶࡦࡺࡥࠡࡣࡱࠤࡗ࡙ࡁࠡ࡭ࡨࡽࠥࡵࡦࠡ࡮ࡨࡲ࡬ࡺࡨࠡࠩࡥ࡭ࡹࡹࠧ࠭ࠢࡳࡹࡧࡲࡩࡤࠢࡨࡼࡵࡵ࡮ࡦࡰࡷࠤࠬ࡫ࠧࠩࡹ࡫࡭ࡨ࡮ࠠ࡮ࡷࡶࡸࠥࡨࡥࠋࠢࠣࠤࠥࡵࡤࡥࠫ࠯ࠤࡺࡹࡩ࡯ࡩࠣࠫࡷࡧ࡮ࡥࡨࡸࡲࡨ࠭ࠠࡵࡱࠣ࡫ࡪࡺࠠࡳࡣࡱࡨࡴࡳࠠࡥࡣࡷࡥࠥࡧ࡮ࡥࠢࠪࡴࡷࡵࡧࡳࡧࡶࡷࡤ࡬ࡵ࡯ࡥࠪ࠰ࠏࠦࠠࠡࠢ࡬ࡪࠥࡶࡲࡦࡵࡨࡲࡹ࠲ࠠࡵࡱࠣࡨ࡮ࡹࡰ࡭ࡣࡼࠤࡹ࡮ࡥࠡࡲࡵࡳ࡬ࡸࡥࡴࡵࠣࡳ࡫ࠦࡴࡩࡧࠣ࡯ࡪࡿࠠࡨࡧࡱࡩࡷࡧࡴࡪࡱࡱ࠲ࠏࠦࠠࠡࠢࠥࠦࠧ৭")
    obj=l111lll111_Krypto_()
    obj.e = int(e)
    if l1l1111lll_Krypto_:
        l1l1111lll_Krypto_(l1l1111_Krypto_ (u"ࠨࡲ࠯ࡵࡡࡴࠧ৮"))
    p = q = 1
    while l111l1ll_Krypto_.size(p*q) < bits:
        p = l1l111lll1_Krypto_.l111ll1lll_Krypto_(bits>>1, obj.e, 1e-12, l1l11ll1ll_Krypto_)
        q = l1l111lll1_Krypto_.l111ll1lll_Krypto_(bits - (bits>>1), obj.e, 1e-12, l1l11ll1ll_Krypto_)
    if p > q:
        (p, q)=(q, p)
    obj.p = p
    obj.q = q
    if l1l1111lll_Krypto_:
        l1l1111lll_Krypto_(l1l1111_Krypto_ (u"ࠩࡸࡠࡳ࠭৯"))
    obj.u = l1l111lll1_Krypto_.l11llll1ll_Krypto_(obj.p, obj.q)
    obj.n = obj.p*obj.q
    if l1l1111lll_Krypto_:
        l1l1111lll_Krypto_(l1l1111_Krypto_ (u"ࠪࡨࡡࡴࠧৰ"))
    obj.d=l1l111lll1_Krypto_.l11llll1ll_Krypto_(obj.e, (obj.p-1)*(obj.q-1))
    assert bits <= 1+obj.size(), l1l1111_Krypto_ (u"ࠦࡌ࡫࡮ࡦࡴࡤࡸࡪࡪࠠ࡬ࡧࡼࠤ࡮ࡹࠠࡵࡱࡲࠤࡸࡳࡡ࡭࡮ࠥৱ")
    return obj
class l111lll111_Krypto_(l1l111lll1_Krypto_.l1l111lll1_Krypto_):
    def size(self):
        l1l1111_Krypto_ (u"ࠧࠨࠢࡴ࡫ࡽࡩ࠭࠯ࠠ࠻ࠢ࡬ࡲࡹࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࠠࡵࡪࡨࠤࡲࡧࡸࡪ࡯ࡸࡱࠥࡴࡵ࡮ࡤࡨࡶࠥࡵࡦࠡࡤ࡬ࡸࡸࠦࡴࡩࡣࡷࠤࡨࡧ࡮ࠡࡤࡨࠤ࡭ࡧ࡮ࡥ࡮ࡨࡨࠥࡨࡹࠡࡶ࡫࡭ࡸࠦ࡫ࡦࡻ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣ৲")
        return l111l1ll_Krypto_.size(self.n) - 1