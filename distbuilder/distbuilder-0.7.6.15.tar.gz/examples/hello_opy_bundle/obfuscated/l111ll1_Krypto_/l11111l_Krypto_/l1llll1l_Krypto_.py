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
l1l1111_Krypto_ (u"ࠣࠤࠥࡑࡴࡪࡵ࡭ࡧࠣࡻ࡮ࡺࡨࠡࡦࡨࡪ࡮ࡴࡩࡵ࡫ࡲࡲࡸࠦࡣࡰ࡯ࡰࡳࡳࠦࡴࡰࠢࡤࡰࡱࠦࡢ࡭ࡱࡦ࡯ࠥࡩࡩࡱࡪࡨࡶࡸ࠴ࠢࠣࠤࡃ")
import sys as l1l11l11_Krypto_
if l1l11l11_Krypto_.version_info[0] == 2 and l1l11l11_Krypto_.version_info[1] == 1:
    from l111ll1_Krypto_.l1l111ll_Krypto_.l1l1ll1l_Krypto_ import *
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
l1lll1ll_Krypto_ = 1
l1lllll1_Krypto_ = 2
l1lll11l_Krypto_ = 3
l1llll11_Krypto_ = 4
l1111ll_Krypto_ = 5
l1llllll_Krypto_ = 6
l1111l1_Krypto_ = 7
def _1l1lll1_Krypto_(name, index, args, kwargs, default=None):
    l1l1111_Krypto_ (u"ࠤࠥࠦࡋ࡯࡮ࡥࠢࡤࠤࡵࡧࡲࡢ࡯ࡨࡸࡪࡸࠠࡪࡰࠣࡸࡺࡶ࡬ࡦࠢࡤࡲࡩࠦࡤࡪࡥࡷ࡭ࡴࡴࡡࡳࡻࠣࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠦࡡࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࡶࡪࡩࡥࡪࡸࡨࡷࠧࠨࠢࡄ")
    param = kwargs.get(name)
    if len(args)>index:
        if param:
            raise ValueError(l1l1111_Krypto_ (u"ࠥࡔࡦࡸࡡ࡮ࡧࡷࡩࡷࠦࠧࠦࡵࠪࠤ࡮ࡹࠠࡴࡲࡨࡧ࡮࡬ࡩࡦࡦࠣࡸࡼ࡯ࡣࡦࠤࡅ") % name)
        param = args[index]
    return param or default
class l1lll1l1_Krypto_:
    l1l1111_Krypto_ (u"ࠦࠧࠨࡃ࡭ࡣࡶࡷࠥࡳ࡯ࡥࡧ࡯ࡰ࡮ࡴࡧࠡࡣࡱࠤࡦࡨࡳࡵࡴࡤࡧࡹࠦࡢ࡭ࡱࡦ࡯ࠥࡩࡩࡱࡪࡨࡶ࠳ࠨࠢࠣࡆ")
    def __init__(self, factory, key, *args, **kwargs):
        self.mode = _1l1lll1_Krypto_(l1l1111_Krypto_ (u"ࠬࡳ࡯ࡥࡧࠪࡇ"), 0, args, kwargs, default=l1lll1ll_Krypto_)
        self.block_size = factory.block_size
        if self.mode != l1111l1_Krypto_:
            self._1ll1111_Krypto_ = factory.new(key, *args, **kwargs)
            self.l1l11lll_Krypto_ = self._1ll1111_Krypto_.l1l11lll_Krypto_
        else:
            self._1l1ll11_Krypto_ = False
            self._1l1l1ll_Krypto_ = False
            self.l1l11lll_Krypto_ = _1l1lll1_Krypto_(l1l1111_Krypto_ (u"࠭ࡩࡷࠩࡈ"), 1, args, kwargs)
            if not self.l1l11lll_Krypto_:
                raise ValueError(l1l1111_Krypto_ (u"ࠢࡎࡑࡇࡉࡤࡕࡐࡆࡐࡓࡋࡕࠦࡲࡦࡳࡸ࡭ࡷ࡫ࡳࠡࡣࡱࠤࡎ࡜ࠢࡉ"))
            l1l11l1l_Krypto_ = factory.new(key, l1lll11l_Krypto_,
                    b(l1l1111_Krypto_ (u"ࠨ࡞ࡻ࠴࠵࠭ࡊ"))*self.block_size,
                    l1l1llll_Krypto_=self.block_size*8)
            if len(self.l1l11lll_Krypto_) == self.block_size:
                self._1l1l1l1_Krypto_ = l1l11l1l_Krypto_.l1_Krypto_(
                    self.l1l11lll_Krypto_ + self.l1l11lll_Krypto_[-2:] +
                    b(l1l1111_Krypto_ (u"ࠩ࡟ࡼ࠵࠶ࠧࡋ"))*(self.block_size-2)
                    )[:self.block_size+2]
            elif len(self.l1l11lll_Krypto_) == self.block_size+2:
                self._1l1l1l1_Krypto_ = self.l1l11lll_Krypto_
                self.l1l11lll_Krypto_ = l1l11l1l_Krypto_.l1lllll_Krypto_(self.l1l11lll_Krypto_ +
                    b(l1l1111_Krypto_ (u"ࠪࡠࡽ࠶࠰ࠨࡌ"))*(self.block_size-2)
                    )[:self.block_size+2]
                if self.l1l11lll_Krypto_[-2:] != self.l1l11lll_Krypto_[-4:-2]:
                    raise ValueError(l1l1111_Krypto_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤ࡮ࡴࡴࡦࡩࡵ࡭ࡹࡿࠠࡤࡪࡨࡧࡰࠦࡦࡰࡴࠣࡓࡕࡋࡎࡑࡉࡓࠤࡎ࡜ࠢࡍ"))
                self.l1l11lll_Krypto_ = self.l1l11lll_Krypto_[:-2]
            else:
                raise ValueError(l1l1111_Krypto_ (u"ࠧࡒࡥ࡯ࡩࡷ࡬ࠥࡵࡦࠡࡋ࡙ࠤࡲࡻࡳࡵࠢࡥࡩࠥࠫࡤࠡࡱࡵࠤࠪࡪࠠࡣࡻࡷࡩࡸࠦࡦࡰࡴࠣࡑࡔࡊࡅࡠࡑࡓࡉࡓࡖࡇࡑࠤࡎ")
                    % (self.block_size, self.block_size+2))
            self._1ll1111_Krypto_ = factory.new(key, l1lll11l_Krypto_,
                self._1l1l1l1_Krypto_[-self.block_size:],
                l1l1llll_Krypto_=self.block_size*8)
    def l1_Krypto_(self, l1ll11l1_Krypto_):
        l1l1111_Krypto_ (u"ࠨࠢࠣࡇࡱࡧࡷࡿࡰࡵࠢࡧࡥࡹࡧࠠࡸ࡫ࡷ࡬ࠥࡺࡨࡦࠢ࡮ࡩࡾࠦࡡ࡯ࡦࠣࡸ࡭࡫ࠠࡱࡣࡵࡥࡲ࡫ࡴࡦࡴࡶࠤࡸ࡫ࡴࠡࡣࡷࠤ࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࢀࡡࡵ࡫ࡲࡲ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢࡗ࡬ࡪࠦࡣࡪࡲ࡫ࡩࡷࠦ࡯ࡣ࡬ࡨࡧࡹࠦࡩࡴࠢࡶࡸࡦࡺࡥࡧࡷ࡯࠿ࠥ࡫࡮ࡤࡴࡼࡴࡹ࡯࡯࡯ࠢࡲࡪࠥࡧࠠ࡭ࡱࡱ࡫ࠥࡨ࡬ࡰࡥ࡮ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡵࡦࠡࡦࡤࡸࡦࠦࡣࡢࡰࠣࡦࡪࠦࡢࡳࡱ࡮ࡩࡳࠦࡵࡱࠢ࡬ࡲࠥࡺࡷࡰࠢࡲࡶࠥࡳ࡯ࡳࡧࠣࡧࡦࡲ࡬ࡴࠢࡷࡳࠥࡦࡥ࡯ࡥࡵࡽࡵࡺࠨࠪࡢ࠱ࠎࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࡨࡢࡶࠣ࡭ࡸ࠲ࠠࡵࡪࡨࠤࡸࡺࡡࡵࡧࡰࡩࡳࡺ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡄ࠾࠿ࠢࡦ࠲ࡪࡴࡣࡳࡻࡳࡸ࠭ࡧࠩࠡ࠭ࠣࡧ࠳࡫࡮ࡤࡴࡼࡴࡹ࠮ࡢࠪࠌࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡮ࡹࠠࡢ࡮ࡺࡥࡾࡹࠠࡦࡳࡸ࡭ࡻࡧ࡬ࡦࡰࡷࠤࡹࡵ࠺ࠋࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡀࡁࡂࠥࡩ࠮ࡦࡰࡦࡶࡾࡶࡴࠩࡣ࠮ࡦ࠮ࠐࠊࠡࠢࠣࠤࠥࠦࠠࠡࡖ࡫ࡥࡹࠦࡡ࡭ࡵࡲࠤࡲ࡫ࡡ࡯ࡵࠣࡸ࡭ࡧࡴࠡࡻࡲࡹࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡥࡶࡵࡨࠤࡦࡴࠠࡰࡤ࡭ࡩࡨࡺࠠࡧࡱࡵࠤࡪࡴࡣࡳࡻࡳࡸ࡮ࡴࡧࠋࠢࠣࠤࠥࠦࠠࠡࠢࡲࡶࠥࡪࡥࡤࡴࡼࡴࡹ࡯࡮ࡨࠢࡲࡸ࡭࡫ࡲࠡࡦࡤࡸࡦࠦࡷࡪࡶ࡫ࠤࡹ࡮ࡥࠡࡵࡤࡱࡪࠦ࡫ࡦࡻ࠱ࠎࠏࠦࠠࠡࠢࠣࠤࠥࠦࡔࡩ࡫ࡶࠤ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࡤࡰࡧࡶࠤࡳࡵࡴࠡࡲࡨࡶ࡫ࡵࡲ࡮ࠢࡤࡲࡾࠦࡰࡢࡦࡧ࡭ࡳ࡭࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡆࡰࡴࠣࡤࡒࡕࡄࡆࡡࡈࡇࡇࡦࠬࠡࡢࡐࡓࡉࡋ࡟ࡄࡄࡆࡤ࠱ࠦࡡ࡯ࡦࠣࡤࡒࡕࡄࡆࡡࡒࡊࡇࡦࠬࠡࠬࡳࡰࡦ࡯࡮ࡵࡧࡻࡸ࠯ࠦ࡬ࡦࡰࡪࡸ࡭ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠬ࡮ࡴࠠࡣࡻࡷࡩࡸ࠯ࠠ࡮ࡷࡶࡸࠥࡨࡥࠡࡣࠣࡱࡺࡲࡴࡪࡲ࡯ࡩࠥࡵࡦࠡࠬࡥࡰࡴࡩ࡫ࡠࡵ࡬ࡾࡪ࠰࠮ࠋࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡆࡰࡴࠣࡤࡒࡕࡄࡆࡡࡆࡊࡇࡦࠬࠡࠬࡳࡰࡦ࡯࡮ࡵࡧࡻࡸ࠯ࠦ࡬ࡦࡰࡪࡸ࡭ࠦࠨࡪࡰࠣࡦࡾࡺࡥࡴࠫࠣࡱࡺࡹࡴࠡࡤࡨࠤࡦࠦ࡭ࡶ࡮ࡷ࡭ࡵࡲࡥࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡵࡦࠡࠬࡶࡩ࡬ࡳࡥ࡯ࡶࡢࡷ࡮ࢀࡥࠫ࠱࠻࠲ࠏࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡊࡴࡸࠠࡡࡏࡒࡈࡊࡥࡃࡕࡔࡣ࠰ࠥ࠰ࡰ࡭ࡣ࡬ࡲࡹ࡫ࡸࡵࠬࠣࡧࡦࡴࠠࡣࡧࠣࡳ࡫ࠦࡡ࡯ࡻࠣࡰࡪࡴࡧࡵࡪ࠱ࠎࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡉࡳࡷࠦࡠࡎࡑࡇࡉࡤࡕࡐࡆࡐࡓࡋࡕࡦࠬࠡࠬࡳࡰࡦ࡯࡮ࡵࡧࡻࡸ࠯ࠦ࡭ࡶࡵࡷࠤࡧ࡫ࠠࡢࠢࡰࡹࡱࡺࡩࡱ࡮ࡨࠤࡴ࡬ࠠࠫࡤ࡯ࡳࡨࡱ࡟ࡴ࡫ࡽࡩ࠯࠲ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡺࡴ࡬ࡦࡵࡶࠤ࡮ࡺࠠࡪࡵࠣࡸ࡭࡫ࠠ࡭ࡣࡶࡸࠥࡩࡨࡶࡰ࡮ࠤࡴ࡬ࠠࡵࡪࡨࠤࡲ࡫ࡳࡴࡣࡪࡩ࠳ࠐࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠼ࡓࡥࡷࡧ࡭ࡦࡶࡨࡶࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡴࡱࡧࡩ࡯ࡶࡨࡼࡹࠦ࠺ࠡࡤࡼࡸࡪࠦࡳࡵࡴ࡬ࡲ࡬ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡙࡮ࡥࠡࡲ࡬ࡩࡨ࡫ࠠࡰࡨࠣࡨࡦࡺࡡࠡࡶࡲࠤࡪࡴࡣࡳࡻࡳࡸ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠻ࡔࡨࡸࡺࡸ࡮࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡵࡪࡨࠤࡪࡴࡣࡳࡻࡳࡸࡪࡪࠠࡥࡣࡷࡥ࠱ࠦࡡࡴࠢࡤࠤࡧࡿࡴࡦࠢࡶࡸࡷ࡯࡮ࡨ࠰ࠣࡍࡹࠦࡩࡴࠢࡤࡷࠥࡲ࡯࡯ࡩࠣࡥࡸࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠯ࡶ࡬ࡢ࡫ࡱࡸࡪࡾࡴࠫࠢࡺ࡭ࡹ࡮ࠠࡰࡰࡨࠤࡪࡾࡣࡦࡲࡷ࡭ࡴࡴ࠺ࠡࡹ࡫ࡩࡳࠦࡥ࡯ࡥࡵࡽࡵࡺࡩ࡯ࡩࠣࡸ࡭࡫ࠠࡧ࡫ࡵࡷࡹࠦ࡭ࡦࡵࡶࡥ࡬࡫ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡩࡨࡶࡰ࡮ࠤࡼ࡯ࡴࡩࠢࡣࡑࡔࡊࡅࡠࡑࡓࡉࡓࡖࡇࡑࡢ࠯ࠤࡹ࡮ࡥࠡࡧࡱࡧࡾࡶࡴࡦࡦࠣࡍ࡛ࠦࡩࡴࠢࡳࡶࡪࡶࡥ࡯ࡦࡨࡨࠥࡺ࡯ࠡࡶ࡫ࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡶࡪࡺࡵࡳࡰࡨࡨࠥࡩࡩࡱࡪࡨࡶࡹ࡫ࡸࡵ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢࡏ")
        if self.mode == l1111l1_Krypto_:
            l1l1l111_Krypto_ = (self.block_size - len(l1ll11l1_Krypto_) % self.block_size) % self.block_size
            if l1l1l111_Krypto_>0:
                if self._1l1l1ll_Krypto_:
                    raise ValueError(l1l1111_Krypto_ (u"ࠢࡐࡰ࡯ࡽࠥࡺࡨࡦࠢ࡯ࡥࡸࡺࠠࡤࡪࡸࡲࡰࠦࡩࡴࠢࡤࡰࡱࡵࡷࡦࡦࠣࡸࡴࠦࡨࡢࡸࡨࠤࡱ࡫࡮ࡨࡶ࡫ࠤࡳࡵࡴࠡ࡯ࡸࡰࡹ࡯ࡰ࡭ࡧࠣࡳ࡫ࠦࠥࡥࠢࡥࡽࡹ࡫ࡳࠣࡐ"),
                        self.block_size)
                self._1l1l1ll_Krypto_ = True
                l1l1l11l_Krypto_ = l1ll11l1_Krypto_ + b(l1l1111_Krypto_ (u"ࠨ࡞ࡻ࠴࠵࠭ࡑ"))*l1l1l111_Krypto_
                res = self._1ll1111_Krypto_.l1_Krypto_(l1l1l11l_Krypto_)[:len(l1ll11l1_Krypto_)]
            else:
                res = self._1ll1111_Krypto_.l1_Krypto_(l1ll11l1_Krypto_)
            if not self._1l1ll11_Krypto_:
                res = self._1l1l1l1_Krypto_ + res
                self._1l1ll11_Krypto_ = True
            return res
        return self._1ll1111_Krypto_.l1_Krypto_(l1ll11l1_Krypto_)
    def l1lllll_Krypto_(self, l1ll111l_Krypto_):
        l1l1111_Krypto_ (u"ࠤࠥࠦࡉ࡫ࡣࡳࡻࡳࡸࠥࡪࡡࡵࡣࠣࡻ࡮ࡺࡨࠡࡶ࡫ࡩࠥࡱࡥࡺࠢࡤࡲࡩࠦࡴࡩࡧࠣࡴࡦࡸࡡ࡮ࡧࡷࡩࡷࡹࠠࡴࡧࡷࠤࡦࡺࠠࡪࡰ࡬ࡸ࡮ࡧ࡬ࡪࡼࡤࡸ࡮ࡵ࡮࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠎࠥࠦࠠࠡࠢࠣࠤ࡚ࠥࡨࡦࠢࡦ࡭ࡵ࡮ࡥࡳࠢࡲࡦ࡯࡫ࡣࡵࠢ࡬ࡷࠥࡹࡴࡢࡶࡨࡪࡺࡲ࠻ࠡࡦࡨࡧࡷࡿࡰࡵ࡫ࡲࡲࠥࡵࡦࠡࡣࠣࡰࡴࡴࡧࠡࡤ࡯ࡳࡨࡱࠊࠡࠢࠣࠤࠥࠦࠠࠡࡱࡩࠤࡩࡧࡴࡢࠢࡦࡥࡳࠦࡢࡦࠢࡥࡶࡴࡱࡥ࡯ࠢࡸࡴࠥ࡯࡮ࠡࡶࡺࡳࠥࡵࡲࠡ࡯ࡲࡶࡪࠦࡣࡢ࡮࡯ࡷࠥࡺ࡯ࠡࡢࡧࡩࡨࡸࡹࡱࡶࠫ࠭ࡥ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡖ࡫ࡥࡹࠦࡩࡴ࠮ࠣࡸ࡭࡫ࠠࡴࡶࡤࡸࡪࡳࡥ࡯ࡶ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡀࡁࡂࠥࡩ࠮ࡥࡧࡦࡶࡾࡶࡴࠩࡣࠬࠤ࠰ࠦࡣ࠯ࡦࡨࡧࡷࡿࡰࡵࠪࡥ࠭ࠏࠐࠠࠡࠢࠣࠤࠥࠦࠠࡪࡵࠣࡥࡱࡽࡡࡺࡵࠣࡩࡶࡻࡩࡷࡣ࡯ࡩࡳࡺࠠࡵࡱ࠽ࠎࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡃࡄ࠾ࠡࡥ࠱ࡨࡪࡩࡲࡺࡲࡷࠬࡦ࠱ࡢࠪࠌࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡙࡮ࡡࡵࠢࡤࡰࡸࡵࠠ࡮ࡧࡤࡲࡸࠦࡴࡩࡣࡷࠤࡾࡵࡵࠡࡥࡤࡲࡳࡵࡴࠡࡴࡨࡹࡸ࡫ࠠࡢࡰࠣࡳࡧࡰࡥࡤࡶࠣࡪࡴࡸࠠࡦࡰࡦࡶࡾࡶࡴࡪࡰࡪࠎࠥࠦࠠࠡࠢࠣࠤࠥࡵࡲࠡࡦࡨࡧࡷࡿࡰࡵ࡫ࡱ࡫ࠥࡵࡴࡩࡧࡵࠤࡩࡧࡴࡢࠢࡺ࡭ࡹ࡮ࠠࡵࡪࡨࠤࡸࡧ࡭ࡦࠢ࡮ࡩࡾ࠴ࠊࠋࠢࠣࠤࠥࠦࠠࠡࠢࡗ࡬࡮ࡹࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࡧࡳࡪࡹࠠ࡯ࡱࡷࠤࡵ࡫ࡲࡧࡱࡵࡱࠥࡧ࡮ࡺࠢࡳࡥࡩࡪࡩ࡯ࡩ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡉࡳࡷࠦࡠࡎࡑࡇࡉࡤࡋࡃࡃࡢ࠯ࠤࡥࡓࡏࡅࡇࡢࡇࡇࡉࡠ࠭ࠢࡤࡲࡩࠦࡠࡎࡑࡇࡉࡤࡕࡆࡃࡢ࠯ࠤ࠯ࡩࡩࡱࡪࡨࡶࡹ࡫ࡸࡵࠬࠣࡰࡪࡴࡧࡵࡪࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠩ࡫ࡱࠤࡧࡿࡴࡦࡵࠬࠤࡲࡻࡳࡵࠢࡥࡩࠥࡧࠠ࡮ࡷ࡯ࡸ࡮ࡶ࡬ࡦࠢࡲࡪࠥ࠰ࡢ࡭ࡱࡦ࡯ࡤࡹࡩࡻࡧ࠭࠲ࠏࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡊࡴࡸࠠࡡࡏࡒࡈࡊࡥࡃࡇࡄࡣ࠰ࠥ࠰ࡣࡪࡲ࡫ࡩࡷࡺࡥࡹࡶ࠭ࠤࡱ࡫࡮ࡨࡶ࡫ࠤ࠭࡯࡮ࠡࡤࡼࡸࡪࡹࠩࠡ࡯ࡸࡷࡹࠦࡢࡦࠢࡤࠤࡲࡻ࡬ࡵ࡫ࡳࡰࡪࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡳ࡫ࠦࠪࡴࡧࡪࡱࡪࡴࡴࡠࡵ࡬ࡾࡪ࠰࠯࠹࠰ࠍࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡈࡲࡶࠥࡦࡍࡐࡆࡈࡣࡈ࡚ࡒࡡ࠮ࠣ࠮ࡨ࡯ࡰࡩࡧࡵࡸࡪࡾࡴࠫࠢࡦࡥࡳࠦࡢࡦࠢࡲࡪࠥࡧ࡮ࡺࠢ࡯ࡩࡳ࡭ࡴࡩ࠰ࠍࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡈࡲࡶࠥࡦࡍࡐࡆࡈࡣࡔࡖࡅࡏࡒࡊࡔࡥ࠲ࠠࠫࡲ࡯ࡥ࡮ࡴࡴࡦࡺࡷ࠮ࠥࡳࡵࡴࡶࠣࡦࡪࠦࡡࠡ࡯ࡸࡰࡹ࡯ࡰ࡭ࡧࠣࡳ࡫ࠦࠪࡣ࡮ࡲࡧࡰࡥࡳࡪࡼࡨ࠮࠱ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡹࡳࡲࡥࡴࡵࠣ࡭ࡹࠦࡩࡴࠢࡷ࡬ࡪࠦ࡬ࡢࡵࡷࠤࡨ࡮ࡵ࡯࡭ࠣࡳ࡫ࠦࡴࡩࡧࠣࡱࡪࡹࡳࡢࡩࡨ࠲ࠏࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠻ࡒࡤࡶࡦࡳࡥࡵࡧࡵࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡦ࡭ࡵ࡮ࡥࡳࡶࡨࡼࡹࠦ࠺ࠡࡤࡼࡸࡪࠦࡳࡵࡴ࡬ࡲ࡬ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡙࡮ࡥࠡࡲ࡬ࡩࡨ࡫ࠠࡰࡨࠣࡨࡦࡺࡡࠡࡶࡲࠤࡩ࡫ࡣࡳࡻࡳࡸ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠻ࡔࡨࡸࡺࡸ࡮࠻ࠢࡷ࡬ࡪࠦࡤࡦࡥࡵࡽࡵࡺࡥࡥࠢࡧࡥࡹࡧࠠࠩࡤࡼࡸࡪࠦࡳࡵࡴ࡬ࡲ࡬࠲ࠠࡢࡵࠣࡰࡴࡴࡧࠡࡣࡶࠤ࠯ࡩࡩࡱࡪࡨࡶࡹ࡫ࡸࡵࠬࠬ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤࡒ")
        if self.mode == l1111l1_Krypto_:
            l1l1l111_Krypto_ = (self.block_size - len(l1ll111l_Krypto_) % self.block_size) % self.block_size
            if l1l1l111_Krypto_>0:
                if self._1l1l1ll_Krypto_:
                    raise ValueError(l1l1111_Krypto_ (u"ࠥࡓࡳࡲࡹࠡࡶ࡫ࡩࠥࡲࡡࡴࡶࠣࡧ࡭ࡻ࡮࡬ࠢ࡬ࡷࠥࡧ࡬࡭ࡱࡺࡩࡩࠦࡴࡰࠢ࡫ࡥࡻ࡫ࠠ࡭ࡧࡱ࡫ࡹ࡮ࠠ࡯ࡱࡷࠤࡲࡻ࡬ࡵ࡫ࡳࡰࡪࠦ࡯ࡧࠢࠨࡨࠥࡨࡹࡵࡧࡶࠦࡓ"),
                        self.block_size)
                self._1l1l1ll_Krypto_ = True
                l1l1l11l_Krypto_ = l1ll111l_Krypto_ + b(l1l1111_Krypto_ (u"ࠫࡡࡾ࠰࠱ࠩࡔ"))*l1l1l111_Krypto_
                res = self._1ll1111_Krypto_.l1lllll_Krypto_(l1l1l11l_Krypto_)[:len(l1ll111l_Krypto_)]
            else:
                res = self._1ll1111_Krypto_.l1lllll_Krypto_(l1ll111l_Krypto_)
            return res
        return self._1ll1111_Krypto_.l1lllll_Krypto_(l1ll111l_Krypto_)