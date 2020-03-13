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
from l111ll1_Krypto_.l1l111ll_Krypto_.l111l1ll_Krypto_ import l1ll1lllll_Krypto_, l1ll111ll1_Krypto_
import sys as l1l11l11_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
__all__ = [ l1l1111_Krypto_ (u"ࠬࡊࡥࡳࡑࡥ࡮ࡪࡩࡴࠨᨰ"), l1l1111_Krypto_ (u"࠭ࡄࡦࡴࡌࡲࡹ࡫ࡧࡦࡴࠪᨱ"), l1l1111_Krypto_ (u"ࠧࡅࡧࡵࡓࡨࡺࡥࡵࡕࡷࡶ࡮ࡴࡧࠨᨲ"), l1l1111_Krypto_ (u"ࠨࡆࡨࡶࡓࡻ࡬࡭ࠩᨳ"), l1l1111_Krypto_ (u"ࠩࡇࡩࡷ࡙ࡥࡲࡷࡨࡲࡨ࡫ࠧᨴ"), l1l1111_Krypto_ (u"ࠪࡈࡪࡸࡏࡣ࡬ࡨࡧࡹࡏࡤࠨᨵ") ]
class l11l1ll1ll_Krypto_:
        l1l1111_Krypto_ (u"ࠦࠧࠨࡂࡢࡵࡨࠤࡨࡲࡡࡴࡵࠣࡪࡴࡸࠠࡥࡧࡩ࡭ࡳ࡯࡮ࡨࠢࡤࠤࡸ࡯࡮ࡨ࡮ࡨࠤࡉࡋࡒࠡࡱࡥ࡮ࡪࡩࡴ࠯ࠌࠍࠤࠥࠦࠠࠡࠢࠣࠤࡎࡴࡳࡵࡣࡱࡸ࡮ࡧࡴࡦࠢࡷ࡬࡮ࡹࠠࡤ࡮ࡤࡷࡸࠦࡏࡏࡎ࡜ࠤࡼ࡮ࡥ࡯ࠢࡼࡳࡺࠦࡨࡢࡸࡨࠤࡹࡵࠠࡥࡧࡦࡳࡩ࡫ࠠࡢࠢࡇࡉࡗࠦࡥ࡭ࡧࡰࡩࡳࡺ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᨶ")
        l1lll1l1ll1l_Krypto_ = { l1l1111_Krypto_ (u"࡙ࠬࡅࡒࡗࡈࡒࡈࡋࠧᨷ"): 0x30, l1l1111_Krypto_ (u"࠭ࡂࡊࡖࠣࡗ࡙ࡘࡉࡏࡉࠪᨸ"): 0x03, l1l1111_Krypto_ (u"ࠧࡊࡐࡗࡉࡌࡋࡒࠨᨹ"): 0x02,
                l1l1111_Krypto_ (u"ࠨࡑࡆࡘࡊ࡚ࠠࡔࡖࡕࡍࡓࡍࠧᨺ"): 0x04, l1l1111_Krypto_ (u"ࠩࡑ࡙ࡑࡒࠧᨻ"): 0x05, l1l1111_Krypto_ (u"ࠪࡓࡇࡐࡅࡄࡖࠣࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧᨼ"): 0x06 }
        def __init__(self, l1lll1ll1l11_Krypto_=None, payload=b(l1l1111_Krypto_ (u"ࠫࠬᨽ"))):
                l1l1111_Krypto_ (u"ࠧࠨࠢࡊࡰ࡬ࡸ࡮ࡧ࡬ࡪࡼࡨࠤࡹ࡮ࡥࠡࡆࡈࡖࠥࡵࡢ࡫ࡧࡦࡸࠥࡧࡣࡤࡱࡵࡨ࡮ࡴࡧࠡࡶࡲࠤࡦࠦࡳࡱࡧࡦ࡭࡫࡯ࡣࠡࡶࡼࡴࡪ࠴ࠊࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡘ࡭࡫ࠠࡂࡕࡑ࠲࠶ࠦࡴࡺࡲࡨࠤ࡮ࡹࠠࡦ࡫ࡷ࡬ࡪࡸࠠࡴࡲࡨࡧ࡮࡬ࡩࡦࡦࠣࡥࡸࠦࡴࡩࡧࠣࡅࡘࡔ࠮࠲ࠢࡶࡸࡷ࡯࡮ࡨࠢࠫࡩ࠳࡭࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠫࡘࡋࡑࡖࡇࡑࡇࡊ࠭ࠩ࠭ࠢࡧ࡭ࡷ࡫ࡣࡵ࡮ࡼࠤࡼ࡯ࡴࡩࠢ࡬ࡸࡸࠦ࡮ࡶ࡯ࡨࡶ࡮ࡩࡡ࡭ࠢࡷࡥ࡬ࠦ࡯ࡳࠢࡺ࡭ࡹ࡮ࠠ࡯ࡱࠣࡸࡦ࡭ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡤࡸࠥࡧ࡬࡭ࠢࠫࡒࡴࡴࡥࠪ࠰ࠥࠦࠧᨾ")
                if l1ll1l1lll_Krypto_(l1lll1ll1l11_Krypto_) or l1lll1ll1l11_Krypto_ is None:
                    self.l111l1111ll_Krypto_ = l1lll1ll1l11_Krypto_
                else:
                    if len(l1lll1ll1l11_Krypto_)==1:
                        self.l111l1111ll_Krypto_ = ord(l1lll1ll1l11_Krypto_)
                    else:
                        self.l111l1111ll_Krypto_ = self.l1lll1l1ll1l_Krypto_.get(l1lll1ll1l11_Krypto_)
                self.payload = payload
        def l11l1l1ll1_Krypto_(self, l1lll1ll1l11_Krypto_):
                return self.l1lll1l1ll1l_Krypto_[l1lll1ll1l11_Krypto_]==self.l111l1111ll_Krypto_
        def _1lll1l1l11l_Krypto_(self, l1lll1ll11ll_Krypto_):
                l1l1111_Krypto_ (u"ࠨࠢࠣࡔࡨࡸࡺࡸ࡮ࠡࡣࠣࡦࡾࡺࡥࠡࡵࡷࡶ࡮ࡴࡧࠡࡶ࡫ࡥࡹࠦࡥ࡯ࡥࡲࡨࡪࡹࠠࡵࡪࡨࠤ࡬࡯ࡶࡦࡰࠣࡴࡦࡿ࡬ࡰࡣࡧࠤࡱ࡫࡮ࡨࡶ࡫ࠤ࠭࡯࡮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡦࡾࡺࡥࡴࠫࠣ࡭ࡳࠦࡡࠡࡨࡲࡶࡲࡧࡴࠡࡵࡸ࡭ࡹࡧࡢ࡭ࡧࠣࡪࡴࡸࠠࡢࠢࡇࡉࡗࠦ࡬ࡦࡰࡪࡸ࡭ࠦࡴࡢࡩࠣࠬࡑ࠯࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᨿ")
                if l1lll1ll11ll_Krypto_>127:
                        encoding = l1ll1lllll_Krypto_(l1lll1ll11ll_Krypto_)
                        return l11111l11_Krypto_(len(encoding)+128) + encoding
                return l11111l11_Krypto_(l1lll1ll11ll_Krypto_)
        def encode(self):
                l1l1111_Krypto_ (u"ࠢࠣࠤࡕࡩࡹࡻࡲ࡯ࠢࡤࠤࡨࡵ࡭ࡱ࡮ࡨࡸࡪࠦࡄࡆࡔࠣࡩࡱ࡫࡭ࡦࡰࡷ࠰ࠥ࡬ࡵ࡭࡮ࡼࠤࡪࡴࡣࡰࡦࡨࡨࠥࡧࡳࠡࡣࠣࡘࡑ࡜࠮ࠣࠤࠥᩀ")
                return l11111l11_Krypto_(self.l111l1111ll_Krypto_) + self._1lll1l1l11l_Krypto_(len(self.payload)) + self.payload
        def _1lll1l11lll_Krypto_(self, idx, l11l1l111l_Krypto_):
                l1l1111_Krypto_ (u"ࠣࠤࠥࡋ࡮ࡼࡥ࡯ࠢࡤࠤ࠭ࡶࡡࡳࡶࠣࡳ࡫ࠦࡡࠪࠢࡇࡉࡗࠦࡥ࡭ࡧࡰࡩࡳࡺࠬࠡࡣࡱࡨࠥࡧ࡮ࠡ࡫ࡱࡨࡪࡾࠠࡵࡱࠣࡸ࡭࡫ࠠࡧ࡫ࡵࡷࡹࠦࡢࡺࡶࡨࠤࡴ࡬ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡤࠤࡉࡋࡒࠡ࡮ࡨࡲ࡬ࡺࡨࠡࡶࡤ࡫ࠥ࠮ࡌࠪ࠮ࠣࡶࡪࡺࡵࡳࡰࠣࡥࠥࡺࡵࡱ࡮ࡨࠤࡼ࡯ࡴࡩࠢࡷ࡬ࡪࠦࡰࡢࡻ࡯ࡳࡦࡪࠠࡴ࡫ࡽࡩ࠱ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡣࡱࡨࠥࡺࡨࡦࠢ࡬ࡲࡩ࡫ࡸࠡࡱࡩࠤࡹ࡮ࡥࠡࡨ࡬ࡶࡸࡺࠠࡣࡻࡷࡩࠥࡵࡦࠡࡶ࡫ࡩࠥࡹࡵࡤࡪࠣࡴࡦࡿ࡬ࡰࡣࡧࠤ࠭࡜ࠩ࠯ࠌࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡘࡡࡪࡵࡨࡷࠥࡧࠠࡗࡣ࡯ࡹࡪࡋࡲࡳࡱࡵࠤࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡨࠣࡸ࡭࡫ࠠࡅࡇࡕࠤࡱ࡫࡮ࡨࡶ࡫ࠤ࡮ࡹࠠࡪࡰࡹࡥࡱ࡯ࡤ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡗࡧࡩࡴࡧࡶࠤࡦࡴࠠࡊࡰࡧࡩࡽࡋࡲࡳࡱࡵࠤࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡨࠣࡸ࡭࡫ࠠࡅࡇࡕࠤࡪࡲࡥ࡮ࡧࡱࡸࠥ࡯ࡳࠡࡶࡲࡳࠥࡹࡨࡰࡴࡷ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᩁ")
                length = l1lllllll1_Krypto_(l11l1l111l_Krypto_[idx])
                if length<=127:
                        return (length,idx+1)
                l1lll1ll1111_Krypto_ = l1ll111ll1_Krypto_(l11l1l111l_Krypto_[idx+1:idx+1+(length & 0x7F)])
                if l1lll1ll1111_Krypto_<=127:
                        raise ValueError(l1l1111_Krypto_ (u"ࠤࡑࡳࡹࠦࡡࠡࡆࡈࡖࠥࡲࡥ࡯ࡩࡷ࡬ࠥࡺࡡࡨ࠰ࠥᩂ"))
                return (l1lll1ll1111_Krypto_, idx+1+(length & 0x7F))
        def decode(self, l1lll1ll11l1_Krypto_, l1lll1l1ll11_Krypto_=0):
                l1l1111_Krypto_ (u"ࠥࠦࠧࡊࡥࡤࡱࡧࡩࠥࡧࠠࡤࡱࡰࡴࡱ࡫ࡴࡦࠢࡇࡉࡗࠦࡥ࡭ࡧࡰࡩࡳࡺࠬࠡࡣࡱࡨࠥࡸࡥ࠮࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡩࡸࠦࡴࡩ࡫ࡶࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࡯ࡣ࡬ࡨࡧࡹࠦࡷࡪࡶ࡫ࠤ࡮ࡺ࠮ࠋࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡅࡶࡡࡳࡣࡰࠤࡩ࡫ࡲࡆ࡮ࡨࠤࠥࠦࠠࠡࠢࠣࡅࠥࡩ࡯࡮ࡲ࡯ࡩࡹ࡫ࠠࡅࡇࡕࠤࡪࡲࡥ࡮ࡧࡱࡸ࠳ࠦࡉࡵࠢࡰࡹࡸࡺࠠࡴࡶࡤࡶࡹࠦࡷࡪࡶ࡫ࠤࡦࠦࡄࡆࡔࠣࡘࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡴࡢࡩ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡀࡱࡣࡵࡥࡲࠦ࡮ࡰࡎࡨࡪࡹࡕࡶࡦࡴࡶࠤࠥࡏ࡮ࡥ࡫ࡦࡥࡹ࡫ࠠࡸࡪࡨࡸ࡭࡫ࡲࠡ࡫ࡷࠤ࡮ࡹࠠࡢࡥࡦࡩࡵࡺࡡࡣ࡮ࡨࠤࡹࡵࠠࡤࡱࡰࡴࡱ࡫ࡴࡦࠢࡷ࡬ࡪࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡱࡣࡵࡷ࡮ࡴࡧࠡࡱࡩࠤࡹ࡮ࡥࠡࡆࡈࡖࠥ࡫࡬ࡦ࡯ࡨࡲࡹࠦࡡ࡯ࡦࠣࡪ࡮ࡴࡤࠡࡶ࡫ࡥࡹࠦ࡮ࡰࡶࠣࡥࡱࡲࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡤࡼࡸࡪࡹࠠࡪࡰࠣࡨࡪࡸࡅ࡭ࡧࠣ࡬ࡦࡼࡥࠡࡤࡨࡩࡳࠦࡵࡴࡧࡧ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡁࡴࡨࡸࡺࡸ࡮ࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡉ࡯ࡦࡨࡼࠥࡵࡦࠡࡶ࡫ࡩࠥ࡬ࡩࡳࡵࡷࠤࡺࡴࡵࡴࡧࡧࠤࡧࡿࡴࡦࠢ࡬ࡲࠥࡺࡨࡦࠢࡪ࡭ࡻ࡫࡮ࠡࡆࡈࡖࠥ࡫࡬ࡦ࡯ࡨࡲࡹ࠴ࠊࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡖࡦ࡯ࡳࡦࡵࠣࡥࠥ࡜ࡡ࡭ࡷࡨࡉࡷࡸ࡯ࡳࠢࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡥࡤࡷࡪࠦ࡯ࡧࠢࡳࡥࡷࡹࡩ࡯ࡩࠣࡩࡷࡸ࡯ࡳࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡒࡢ࡫ࡶࡩࡸࠦࡡ࡯ࠢࡌࡲࡩ࡫ࡸࡆࡴࡵࡳࡷࠦࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡪࠥࡺࡨࡦࠢࡇࡉࡗࠦࡥ࡭ࡧࡰࡩࡳࡺࠠࡪࡵࠣࡸࡴࡵࠠࡴࡪࡲࡶࡹ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᩃ")
                try:
                        self.l111l1111ll_Krypto_ = l1lllllll1_Krypto_(l1lll1ll11l1_Krypto_[0])
                        if (self.l111l1111ll_Krypto_ & 0x1F)==0x1F:
                                raise ValueError(l1l1111_Krypto_ (u"࡚ࠦࡴࡳࡶࡲࡳࡳࡷࡺࡥࡥࠢࡇࡉࡗࠦࡴࡢࡩࠥᩄ"))
                        (length,idx) = self._1lll1l11lll_Krypto_(1, l1lll1ll11l1_Krypto_)
                        if l1lll1l1ll11_Krypto_ and len(l1lll1ll11l1_Krypto_) != (idx+length):
                                raise ValueError(l1l1111_Krypto_ (u"ࠧࡔ࡯ࡵࠢࡤࠤࡉࡋࡒࠡࡵࡷࡶࡺࡩࡴࡶࡴࡨࠦᩅ"))
                        self.payload = l1lll1ll11l1_Krypto_[idx:idx+length]
                except IndexError:
                        raise ValueError(l1l1111_Krypto_ (u"ࠨࡎࡰࡶࠣࡥࠥࡼࡡ࡭࡫ࡧࠤࡉࡋࡒࠡࡕࡈࡕ࡚ࡋࡎࡄࡇ࠱ࠦᩆ"))
                return idx+length
class l1lll1ll111l_Krypto_(l11l1ll1ll_Krypto_):
        def __init__(self, value = 0):
                l1l1111_Krypto_ (u"ࠢࠣࠤࡆࡰࡦࡹࡳࠡࡶࡲࠤࡲࡵࡤࡦ࡮ࠣࡥࡳࠦࡉࡏࡖࡈࡋࡊࡘࠠࡅࡇࡕࠤࡪࡲࡥ࡮ࡧࡱࡸ࠳ࠐࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡏ࡭ࡲ࡯ࡴࡢࡶ࡬ࡳࡳࡀࠠࡰࡰ࡯ࡽࠥࡴ࡯࡯࠯ࡱࡩ࡬ࡧࡴࡪࡸࡨࠤࡻࡧ࡬ࡶࡧࡶࠤࡦࡸࡥࠡࡵࡸࡴࡵࡵࡲࡵࡧࡧ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᩇ")
                l11l1ll1ll_Krypto_.__init__(self, l1l1111_Krypto_ (u"ࠨࡋࡑࡘࡊࡍࡅࡓࠩᩈ"))
                self.value = value
        def encode(self):
                l1l1111_Krypto_ (u"ࠤࠥࠦࡗ࡫ࡴࡶࡴࡱࠤࡦࠦࡣࡰ࡯ࡳࡰࡪࡺࡥࠡࡋࡑࡘࡊࡍࡅࡓࠢࡇࡉࡗࠦࡥ࡭ࡧࡰࡩࡳࡺࠬࠡࡨࡸࡰࡱࡿࠠࡦࡰࡦࡳࡩ࡫ࡤࠡࡣࡶࠤࡦࠦࡔࡍࡘ࠱ࠦࠧࠨᩉ")
                self.payload = l1ll1lllll_Krypto_(self.value)
                if l1lllllll1_Krypto_(self.payload[0])>127:
                        self.payload = l11111l11_Krypto_(0x00) + self.payload
                return l11l1ll1ll_Krypto_.encode(self)
        def decode(self, l1lll1ll11l1_Krypto_, l1lll1l1ll11_Krypto_=0):
                l1l1111_Krypto_ (u"ࠥࠦࠧࡊࡥࡤࡱࡧࡩࠥࡧࠠࡤࡱࡰࡴࡱ࡫ࡴࡦࠢࡌࡒ࡙ࡋࡇࡆࡔࠣࡈࡊࡘࠠࡦ࡮ࡨࡱࡪࡴࡴ࠭ࠢࡤࡲࡩࠦࡲࡦ࠯࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡪࡹࠠࡵࡪ࡬ࡷࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡰࡤ࡭ࡩࡨࡺࠠࡸ࡫ࡷ࡬ࠥ࡯ࡴ࠯ࠌࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡆࡰࡢࡴࡤࡱࠥࡪࡥࡳࡇ࡯ࡩࠥࠦࠠࠡࠢࠣࠤࡆࠦࡣࡰ࡯ࡳࡰࡪࡺࡥࠡࡋࡑࡘࡊࡍࡅࡓࠢࡇࡉࡗࠦࡥ࡭ࡧࡰࡩࡳࡺ࠮ࠡࡋࡷࠤࡲࡻࡳࡵࠢࡶࡸࡦࡸࡴࠡࡹ࡬ࡸ࡭ࠦࡡࠡࡆࡈࡖࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡉࡏࡖࡈࡋࡊࡘࠠࡵࡣࡪ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡁࡲࡤࡶࡦࡳࠠ࡯ࡱࡏࡩ࡫ࡺࡏࡷࡧࡵࡷࠥࠦࡉ࡯ࡦ࡬ࡧࡦࡺࡥࠡࡹ࡫ࡩࡹ࡮ࡥࡳࠢ࡬ࡸࠥ࡯ࡳࠡࡣࡦࡧࡪࡶࡴࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡥࡲࡱࡵࡲࡥࡵࡧࠣࡸ࡭࡫ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡲࡤࡶࡸ࡯࡮ࡨࠢࡲࡪࠥࡺࡨࡦࠢࡇࡉࡗࠦࡥ࡭ࡧࡰࡩࡳࡺࠠࡢࡰࡧࠤ࡫࡯࡮ࡥࠢࡷ࡬ࡦࡺࠠ࡯ࡱࡷࠤࡦࡲ࡬ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡥࡽࡹ࡫ࡳࠡ࡫ࡱࠤࡩ࡫ࡲࡆ࡮ࡨࠤ࡭ࡧࡶࡦࠢࡥࡩࡪࡴࠠࡶࡵࡨࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡂࡵࡩࡹࡻࡲ࡯ࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡊࡰࡧࡩࡽࠦ࡯ࡧࠢࡷ࡬ࡪࠦࡦࡪࡴࡶࡸࠥࡻ࡮ࡶࡵࡨࡨࠥࡨࡹࡵࡧࠣ࡭ࡳࠦࡴࡩࡧࠣ࡫࡮ࡼࡥ࡯ࠢࡇࡉࡗࠦࡥ࡭ࡧࡰࡩࡳࡺ࠮ࠋࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡗࡧࡩࡴࡧࡶࠤࡦࠦࡖࡢ࡮ࡸࡩࡊࡸࡲࡰࡴࠣࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩࡧࠢࡷ࡬ࡪࠦࡄࡆࡔࠣࡩࡱ࡫࡭ࡦࡰࡷࠤ࡮ࡹࠠ࡯ࡱࡷࠤࡦࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡸࡤࡰ࡮ࡪࠠ࡯ࡱࡱ࠱ࡳ࡫ࡧࡢࡶ࡬ࡺࡪࠦࡉࡏࡖࡈࡋࡊࡘ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡖࡦ࡯ࡳࡦࡵࠣࡥࡳࠦࡉ࡯ࡦࡨࡼࡊࡸࡲࡰࡴࠣࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩࡧࠢࡷ࡬ࡪࠦࡄࡆࡔࠣࡩࡱ࡫࡭ࡦࡰࡷࠤ࡮ࡹࠠࡵࡱࡲࠤࡸ࡮࡯ࡳࡶ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᩊ")
                l1lll1l1l1l1_Krypto_ = l11l1ll1ll_Krypto_.decode(self, l1lll1ll11l1_Krypto_, l1lll1l1ll11_Krypto_)
                if self.l111l1111ll_Krypto_!=self.l1lll1l1ll1l_Krypto_[l1l1111_Krypto_ (u"ࠫࡎࡔࡔࡆࡉࡈࡖࠬᩋ")]:
                        raise ValueError (l1l1111_Krypto_ (u"ࠧࡔ࡯ࡵࠢࡤࠤࡉࡋࡒࠡࡋࡑࡘࡊࡍࡅࡓ࠰ࠥᩌ"))
                if l1lllllll1_Krypto_(self.payload[0])>127:
                        raise ValueError (l1l1111_Krypto_ (u"ࠨࡎࡦࡩࡤࡸ࡮ࡼࡥࠡࡋࡑࡘࡊࡍࡅࡓ࠰ࠥᩍ"))
                self.value = l1ll111ll1_Krypto_(self.payload)
                return l1lll1l1l1l1_Krypto_
class l11l11llll_Krypto_(l11l1ll1ll_Krypto_):
        l1l1111_Krypto_ (u"ࠢࠣࠤࡆࡰࡦࡹࡳࠡࡶࡲࠤࡲࡵࡤࡦ࡮ࠣࡥ࡙ࠥࡅࡒࡗࡈࡒࡈࡋࠠࡅࡇࡕࠤࡪࡲࡥ࡮ࡧࡱࡸ࠳ࠐࠊࠡࠢࠣࠤࠥࠦࠠࠡࡖ࡫࡭ࡸࠦ࡯ࡣ࡬ࡨࡧࡹࠦࡢࡦࡪࡤࡺࡪࠦ࡬ࡪ࡭ࡨࠤࡦࠦࡤࡺࡰࡤࡱ࡮ࡩࠠࡑࡻࡷ࡬ࡴࡴࠠࡴࡧࡴࡹࡪࡴࡣࡦ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡘࡻࡢ࠮ࡧ࡯ࡩࡲ࡫࡮ࡵࡵࠣࡸ࡭ࡧࡴࠡࡣࡵࡩࠥࡏࡎࡕࡇࡊࡉࡗࡹࠬࠡ࡮ࡲࡳࡰࠦ࡬ࡪ࡭ࡨࠤࡕࡿࡴࡩࡱࡱࠤ࡮ࡴࡴࡦࡩࡨࡶࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡃࡱࡽࠥࡵࡴࡩࡧࡵࠤࡸࡻࡢ࠮ࡧ࡯ࡩࡲ࡫࡮ࡵࠢ࡬ࡷࠥࡧࠠࡣ࡫ࡱࡥࡷࡿࠠࡴࡶࡵ࡭ࡳ࡭ࠠࡦࡰࡦࡳࡩ࡫ࡤࠡࡣࡶࠤࡹ࡮ࡥࠡࡥࡲࡱࡵࡲࡥࡵࡧࠣࡈࡊࡘࠊࠡࠢࠣࠤࠥࠦࠠࠡࡵࡸࡦ࠲࡫࡬ࡦ࡯ࡨࡲࡹࠦࠨࡕࡎ࡙࠭࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᩎ")
        def __init__(self, l1lll1l11l1l_Krypto_=None):
                l1l1111_Krypto_ (u"ࠣࠤࠥࡍࡳ࡯ࡴࡪࡣ࡯࡭ࡿ࡫ࠠࡵࡪࡨࠤࡘࡋࡑࡖࡇࡑࡇࡊࠦࡄࡆࡔࠣࡳࡧࡰࡥࡤࡶ࠱ࠤࡆࡲࡷࡢࡻࡶࠤࡪࡳࡰࡵࡻࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡯࡮ࡪࡶ࡬ࡥࡱࡲࡹ࠯ࠤࠥࠦᩏ")
                l11l1ll1ll_Krypto_.__init__(self, l1l1111_Krypto_ (u"ࠩࡖࡉࡖ࡛ࡅࡏࡅࡈࠫᩐ"))
                if l1lll1l11l1l_Krypto_==None:
                    self._1lll1l1l111_Krypto_ = []
                else:
                    self._1lll1l1l111_Krypto_ = l1lll1l11l1l_Krypto_
        def __delitem__(self, n):
                del self._1lll1l1l111_Krypto_[n]
        def __getitem__(self, n):
                return self._1lll1l1l111_Krypto_[n]
        def __setitem__(self, key, value):
                self._1lll1l1l111_Krypto_[key] = value
        def __setslice__(self,i,j,l1lll1l1llll_Krypto_):
                self._1lll1l1l111_Krypto_[i:j] = l1lll1l1llll_Krypto_
        def __delslice__(self,i,j):
                del self._1lll1l1l111_Krypto_[i:j]
        def __getslice__(self, i, j):
                return self._1lll1l1l111_Krypto_[max(0, i):max(0, j)]
        def __len__(self):
                return len(self._1lll1l1l111_Krypto_)
        def append(self, item):
                return self._1lll1l1l111_Krypto_.append(item)
        def l1lll1l1lll1_Krypto_(self):
                l1l1111_Krypto_ (u"ࠥࠦࠧࡘࡥࡵࡷࡵࡲࠥࡺࡨࡦࠢࡱࡹࡲࡨࡥࡳࠢࡲࡪࠥ࡯ࡴࡦ࡯ࡶࠤ࡮ࡴࠠࡵࡪ࡬ࡷࠥࡹࡥࡲࡷࡨࡲࡨ࡫ࠠࡵࡪࡤࡸࠥࡧࡲࡦࠢࡱࡹࡲࡨࡥࡳࡵ࠱ࠦࠧࠨᩑ")
                return len(list(filter(l1ll1l1lll_Krypto_, self._1lll1l1l111_Krypto_)))
        def l11l11l11l_Krypto_(self):
                l1l1111_Krypto_ (u"ࠦࠧࠨࡒࡦࡶࡸࡶࡳࠦࡔࡳࡷࡨࠤ࡮࡬ࠠࡢ࡮࡯ࠤ࡮ࡺࡥ࡮ࡵࠣ࡭ࡳࠦࡴࡩ࡫ࡶࠤࡸ࡫ࡱࡶࡧࡱࡧࡪࠦࡡࡳࡧࠣࡲࡺࡳࡢࡦࡴࡶ࠲ࠧࠨࠢᩒ")
                return self._1lll1l1l111_Krypto_ and self.l1lll1l1lll1_Krypto_()==len(self._1lll1l1l111_Krypto_)
        def encode(self):
                l1l1111_Krypto_ (u"ࠧࠨࠢࡓࡧࡷࡹࡷࡴࠠࡵࡪࡨࠤࡉࡋࡒࠡࡧࡱࡧࡴࡪࡩ࡯ࡩࠣࡪࡴࡸࠠࡵࡪࡨࠤࡆ࡙ࡎ࠯࠳ࠣࡗࡊࡗࡕࡆࡐࡆࡉ࠱ࠦࡣࡰࡰࡷࡥ࡮ࡴࡩ࡯ࡩࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡺࡨࡦࠢࡱࡳࡳ࠳࡮ࡦࡩࡤࡸ࡮ࡼࡥࠡ࡫ࡱࡸࡪ࡭ࡥࡳࡵࠣࡥࡳࡪࠠ࡭ࡱࡱ࡫ࡸࠦࡡࡥࡦࡨࡨࠥࡺ࡯ࠡࡶ࡫࡭ࡸࠦ࡯ࡣ࡬ࡨࡧࡹ࠴ࠊࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡐ࡮ࡳࡩࡵࡣࡷ࡭ࡴࡴ࠺ࠡࡔࡤ࡭ࡸ࡫ࡳࠡࡣ࡚ࠣࡦࡲࡵࡦࡇࡵࡶࡴࡸࠠࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭࡫ࠦࡩࡵࠢࡶࡳࡲ࡫ࠠࡦ࡮ࡨࡱࡪࡴࡴࡴࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡮ࡴࠠࡵࡪࡨࠤࡸ࡫ࡱࡶࡧࡱࡧࡪࠦࡡࡳࡧࠣࡲࡪ࡯ࡴࡩࡧࡵࠤࡕࡿࡴࡩࡱࡱࠤ࡮ࡴࡴࡦࡩࡨࡶࡸࠦ࡮ࡰࡴࠣࡧࡴࡳࡰ࡭ࡧࡷࡩࠥࡊࡅࡓࠢࡌࡒ࡙ࡋࡇࡆࡔࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᩓ")
                self.payload = b(l1l1111_Krypto_ (u"࠭ࠧᩔ"))
                for item in self._1lll1l1l111_Krypto_:
                        try:
                                self.payload += item
                        except:
                                try:
                                        self.payload += l1lll1ll111l_Krypto_(item).encode()
                                except:
                                        raise ValueError(l1l1111_Krypto_ (u"ࠢࡕࡴࡼ࡭ࡳ࡭ࠠࡵࡱࠣࡈࡊࡘࠠࡦࡰࡦࡳࡩ࡫ࠠࡢࡰࠣࡹࡳࡱ࡮ࡰࡹࡱࠤࡴࡨࡪࡦࡥࡷࠦᩕ"))
                return l11l1ll1ll_Krypto_.encode(self)
        def decode(self, l1lll1ll11l1_Krypto_, l1lll1l1ll11_Krypto_=0):
                l1l1111_Krypto_ (u"ࠣࠤࠥࡈࡪࡩ࡯ࡥࡧࠣࡥࠥࡩ࡯࡮ࡲ࡯ࡩࡹ࡫ࠠࡔࡇࡔ࡙ࡊࡔࡃࡆࠢࡇࡉࡗࠦࡥ࡭ࡧࡰࡩࡳࡺࠬࠡࡣࡱࡨࠥࡸࡥ࠮࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡩࡸࠦࡴࡩ࡫ࡶࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࡯ࡣ࡬ࡨࡧࡹࠦࡷࡪࡶ࡫ࠤ࡮ࡺ࠮ࠋࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡅࡶࡡࡳࡣࡰࠤࡩ࡫ࡲࡆ࡮ࡨࠤࠥࠦࠠࠡࠢࠣࡅࠥࡩ࡯࡮ࡲ࡯ࡩࡹ࡫ࠠࡔࡇࡔ࡙ࡊࡔࡃࡆࠢࡇࡉࡗࠦࡥ࡭ࡧࡰࡩࡳࡺ࠮ࠡࡋࡷࠤࡲࡻࡳࡵࠢࡶࡸࡦࡸࡴࠡࡹ࡬ࡸ࡭ࠦࡡࠡࡆࡈࡖࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡓࡆࡓࡘࡉࡓࡉࡅࠡࡶࡤ࡫࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡂࡳࡥࡷࡧ࡭ࠡࡰࡲࡐࡪ࡬ࡴࡐࡸࡨࡶࡸࠦࠠࡊࡰࡧ࡭ࡨࡧࡴࡦࠢࡺ࡬ࡪࡺࡨࡦࡴࠣ࡭ࡹࠦࡩࡴࠢࡤࡧࡨ࡫ࡰࡵࡣࡥࡰࡪࠦࡴࡰࠢࡦࡳࡲࡶ࡬ࡦࡶࡨࠤࡹ࡮ࡥࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡳࡥࡷࡹࡩ࡯ࡩࠣࡳ࡫ࠦࡴࡩࡧࠣࡈࡊࡘࠠࡦ࡮ࡨࡱࡪࡴࡴࠡࡣࡱࡨࠥ࡬ࡩ࡯ࡦࠣࡸ࡭ࡧࡴࠡࡰࡲࡸࠥࡧ࡬࡭ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡦࡾࡺࡥࡴࠢ࡬ࡲࠥࡪࡥࡳࡇ࡯ࡩࠥ࡮ࡡࡷࡧࠣࡦࡪ࡫࡮ࠡࡷࡶࡩࡩ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡃࡶࡪࡺࡵࡳࡰࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡋࡱࡨࡪࡾࠠࡰࡨࠣࡸ࡭࡫ࠠࡧ࡫ࡵࡷࡹࠦࡵ࡯ࡷࡶࡩࡩࠦࡢࡺࡶࡨࠤ࡮ࡴࠠࡵࡪࡨࠤ࡬࡯ࡶࡦࡰࠣࡈࡊࡘࠠࡦ࡮ࡨࡱࡪࡴࡴ࠯ࠌࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡊࡅࡓࠢࡌࡒ࡙ࡋࡇࡆࡔࡶࠤࡦࡸࡥࠡࡦࡨࡧࡴࡪࡥࡥࠢ࡬ࡲࡹࡵࠠࡑࡻࡷ࡬ࡴࡴࠠࡪࡰࡷࡩ࡬࡫ࡲࡴ࠰ࠣࡅࡳࡿࠠࡰࡶ࡫ࡩࡷࠦࡄࡆࡔࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡫࡬ࡦ࡯ࡨࡲࡹࠦࡩࡴࠢࡱࡳࡹࠦࡤࡦࡥࡲࡨࡪࡪ࠮ࠡࡋࡷࡷࠥࡼࡡ࡭࡫ࡧ࡭ࡹࡿࠠࡪࡵࠣࡲࡴࡺࠠࡤࡪࡨࡧࡰ࡫ࡤ࠯ࠌࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡘࡡࡪࡵࡨࡷࠥࡧࠠࡗࡣ࡯ࡹࡪࡋࡲࡳࡱࡵࠤࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡨࠣࡸ࡭࡫ࠠࡅࡇࡕࠤࡪࡲࡥ࡮ࡧࡱࡸࠥ࡯ࡳࠡࡰࡲࡸࠥࡧࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡹࡥࡱ࡯ࡤࠡࡆࡈࡖ࡙ࠥࡅࡒࡗࡈࡒࡈࡋ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡖࡦ࡯ࡳࡦࡵࠣࡥࡳࠦࡉ࡯ࡦࡨࡼࡊࡸࡲࡰࡴࠣࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩࡧࠢࡷ࡬ࡪࠦࡄࡆࡔࠣࡩࡱ࡫࡭ࡦࡰࡷࠤ࡮ࡹࠠࡵࡱࡲࠤࡸ࡮࡯ࡳࡶ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᩖ")
                self._1lll1l1l111_Krypto_ = []
                try:
                        l1lll1l1l1l1_Krypto_ = l11l1ll1ll_Krypto_.decode(self, l1lll1ll11l1_Krypto_, l1lll1l1ll11_Krypto_)
                        if self.l111l1111ll_Krypto_!=self.l1lll1l1ll1l_Krypto_[l1l1111_Krypto_ (u"ࠩࡖࡉࡖ࡛ࡅࡏࡅࡈࠫᩗ")]:
                                raise ValueError(l1l1111_Krypto_ (u"ࠥࡒࡴࡺࠠࡢࠢࡇࡉࡗࠦࡓࡆࡓࡘࡉࡓࡉࡅ࠯ࠤᩘ"))
                        idx = 0
                        while idx<len(self.payload):
                                l111l1111ll_Krypto_ = l1lllllll1_Krypto_(self.payload[idx])
                                if l111l1111ll_Krypto_==self.l1lll1l1ll1l_Krypto_[l1l1111_Krypto_ (u"ࠫࡎࡔࡔࡆࡉࡈࡖࠬᩙ")]:
                                        l1lll1l11l11_Krypto_ = l1lll1ll111l_Krypto_()
                                        idx += l1lll1l11l11_Krypto_.decode(self.payload[idx:])
                                        self._1lll1l1l111_Krypto_.append(l1lll1l11l11_Krypto_.value)
                                else:
                                        l1lll1ll1l1l_Krypto_,l1lll1l1l1ll_Krypto_ = self._1lll1l11lll_Krypto_(idx+1,self.payload)
                                        self._1lll1l1l111_Krypto_.append(self.payload[idx:l1lll1l1l1ll_Krypto_+l1lll1ll1l1l_Krypto_])
                                        idx = l1lll1l1l1ll_Krypto_ + l1lll1ll1l1l_Krypto_
                except IndexError:
                        raise ValueError(l1l1111_Krypto_ (u"ࠧࡔ࡯ࡵࠢࡤࠤࡻࡧ࡬ࡪࡦࠣࡈࡊࡘࠠࡔࡇࡔ࡙ࡊࡔࡃࡆ࠰ࠥᩚ"))
                return l1lll1l1l1l1_Krypto_
class l1lll1lll11l_Krypto_(l11l1ll1ll_Krypto_):
    def __init__(self, value = b(l1l1111_Krypto_ (u"࠭ࠧᩛ"))):
        l11l1ll1ll_Krypto_.__init__(self, l1l1111_Krypto_ (u"ࠧࡐࡅࡗࡉ࡙ࠦࡓࡕࡔࡌࡒࡌ࠭ᩜ"))
        self.payload = value
    def decode(self, l1lll1ll11l1_Krypto_, l1lll1l1ll11_Krypto_=0):
        p = l11l1ll1ll_Krypto_.decode(l1lll1ll11l1_Krypto_, l1lll1l1ll11_Krypto_)
        if not self.l11l1l1ll1_Krypto_(l1l1111_Krypto_ (u"ࠣࡑࡆࡘࡊ࡚ࠠࡔࡖࡕࡍࡓࡍࠢᩝ")):
            raise ValueError(l1l1111_Krypto_ (u"ࠤࡑࡳࡹࠦࡡࠡࡸࡤࡰ࡮ࡪࠠࡐࡅࡗࡉ࡙ࠦࡓࡕࡔࡌࡒࡌ࠴ࠢᩞ"))
        return p
class l11l1ll1l1_Krypto_(l11l1ll1ll_Krypto_):
    def __init__(self):
        l11l1ll1ll_Krypto_.__init__(self, l1l1111_Krypto_ (u"ࠪࡒ࡚ࡒࡌࠨ᩟"))
class l1lll1l11ll1_Krypto_(l11l1ll1ll_Krypto_):
    def __init__(self):
        l11l1ll1ll_Krypto_.__init__(self, l1l1111_Krypto_ (u"ࠫࡔࡈࡊࡆࡅࡗࠤࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨ᩠"))
    def decode(self, l1lll1ll11l1_Krypto_, l1lll1l1ll11_Krypto_=0):
        p = l11l1ll1ll_Krypto_.decode(l1lll1ll11l1_Krypto_, l1lll1l1ll11_Krypto_)
        if not self.l11l1l1ll1_Krypto_(l1l1111_Krypto_ (u"ࠧࡕࡂࡋࡇࡆࡘࠥࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠤᩡ")):
            raise ValueError(l1l1111_Krypto_ (u"ࠨࡎࡰࡶࠣࡥࠥࡼࡡ࡭࡫ࡧࠤࡔࡈࡊࡆࡅࡗࠤࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒ࠯ࠤᩢ"))
        return p
def l1ll1l1lll_Krypto_(x):
    test = 0
    try:
        test += x
    except TypeError:
        return 0
    return 1