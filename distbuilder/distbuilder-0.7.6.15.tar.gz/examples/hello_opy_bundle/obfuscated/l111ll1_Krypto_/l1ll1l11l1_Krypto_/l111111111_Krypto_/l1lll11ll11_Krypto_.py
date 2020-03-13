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
__revision__ = l1l1111_Krypto_ (u"ࠨࠤࡊࡦࠧࠦ੎")
__all__ = [l1l1111_Krypto_ (u"ࠧࡘ࡫ࡱࡨࡴࡽࡳࡓࡐࡊࠫ੏")]
from . import l1lll1l1111_Krypto_
from .rng_base import l1lll1l11ll_Krypto_
class l1lll11ll1l_Krypto_(l1lll1l11ll_Krypto_):
    name = l1l1111_Krypto_ (u"ࠣ࠾ࡆࡶࡾࡶࡴࡈࡧࡱࡖࡦࡴࡤࡰ࡯ࡁࠦ੐")
    def __init__(self):
        self.__1lll11llll_Krypto_ = l1lll1l1111_Krypto_.new()
        l1lll1l11ll_Krypto_.__init__(self)
    def flush(self):
        l1l1111_Krypto_ (u"ࠤࠥࠦ࡜ࡵࡲ࡬ࠢࡤࡶࡴࡻ࡮ࡥࠢࡺࡩࡦࡱ࡮ࡦࡵࡶࠤ࡮ࡴࠠࡘ࡫ࡱࡨࡴࡽࡳࠡࡔࡑࡋ࠳ࠐࠊࠡࠢࠣࠤࠥࠦࠠࠡࡖ࡫ࡩࠥࡉࡲࡺࡲࡷࡋࡪࡴࡒࡢࡰࡧࡳࡲࠦ࡭ࡦࡥ࡫ࡥࡳ࡯ࡳ࡮ࠢ࡬ࡲࠥࡹ࡯࡮ࡧࠣࡺࡪࡸࡳࡪࡱࡱࡷࠥࡵࡦ࡙ࠡ࡬ࡲࡩࡵࡷࡴࠢࡤࡰࡱࡵࡷࡴࠢࡤࡲࠏࠦࠠࠡࠢࠣࠤࠥࠦࡡࡵࡶࡤࡧࡰ࡫ࡲࠡࡶࡲࠤࡱ࡫ࡡࡳࡰࠣ࠵࠷࠾ࠠࡌ࡫ࡅࠤࡴ࡬ࠠࡱࡣࡶࡸࠥࡧ࡮ࡥࠢࡩࡹࡹࡻࡲࡦࠢࡲࡹࡹࡶࡵࡵ࠰ࠣࠤࡆࡹࠠࡢࠢࡺࡳࡷࡱࡡࡳࡱࡸࡲࡩ࠲ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡶ࡫࡭ࡸࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡴࡨࡥࡩࡹࠠ࠲࠴࠻ࠤࡐ࡯ࡂࠡࡱࡩࠤࠬࡸࡡ࡯ࡦࡲࡱࠬࠦࡤࡢࡶࡤࠤ࡫ࡸ࡯࡮࡚ࠢ࡭ࡳࡪ࡯ࡸࡵࠣࡥࡳࡪࠠࡥ࡫ࡶࡧࡦࡸࡤࡴࠌࠣࠤࠥࠦࠠࠡࠢࠣ࡭ࡹ࠴ࠊࠋࠢࠣࠤࠥࠦࠠࠡࠢࡉࡳࡷࠦ࡭ࡰࡴࡨࠤ࡮ࡴࡦࡰࡴࡰࡥࡹ࡯࡯࡯ࠢࡤࡦࡴࡻࡴࠡࡶ࡫ࡩࠥࡽࡥࡢ࡭ࡱࡩࡸࡹࡥࡴࠢ࡬ࡲࠥࡉࡲࡺࡲࡷࡋࡪࡴࡒࡢࡰࡧࡳࡲ࠲ࠠࡴࡧࡨࠎࠥࠦࠠࠡࠢࠣࠤࠥࡥࡃࡳࡻࡳࡸࡦࡴࡡ࡭ࡻࡶ࡭ࡸࠦ࡯ࡧࠢࡷ࡬ࡪࠦࡒࡢࡰࡧࡳࡲࠦࡎࡶ࡯ࡥࡩࡷࠦࡇࡦࡰࡨࡶࡦࡺ࡯ࡳࠢࡲࡪࠥࡺࡨࡦ࡚ࠢ࡭ࡳࡪ࡯ࡸࡵࠣࡓࡵ࡫ࡲࡢࡶ࡬ࡲ࡬ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡔࡻࡶࡸࡪࡳ࡟࠭ࠢࡥࡽࠥࡒࡥࡰࠢࡇࡳࡷࡸࡥ࡯ࡦࡲࡶ࡫ࠦࡡ࡯ࡦࠣ࡞ࡻ࡯ࠠࡈࡷࡷࡸࡪࡸ࡭ࡢࡰࠣࡥࡳࡪࠠࡃࡧࡱࡲࡾࠦࡐࡪࡰ࡮ࡥࡸࠐࠠࠡࠢࠣࠤࠥࠦࠠࡩࡶࡷࡴ࠿࠵࠯ࡦࡲࡵ࡭ࡳࡺ࠮ࡪࡣࡦࡶ࠳ࡵࡲࡨ࠱࠵࠴࠵࠽࠯࠵࠳࠼ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣੑ")
        if self.closed:
            raise ValueError(l1l1111_Krypto_ (u"ࠥࡍ࠴ࡕࠠࡰࡲࡨࡶࡦࡺࡩࡰࡰࠣࡳࡳࠦࡣ࡭ࡱࡶࡩࡩࠦࡦࡪ࡮ࡨࠦ੒"))
        data = self.__1lll11llll_Krypto_.l1lll11lll1_Krypto_(128*1024)
        assert (len(data) == 128*1024)
        l1lll1l11ll_Krypto_.flush(self)
    def _1lll1l111l_Krypto_(self):
        self.__1lll11llll_Krypto_ = None
    def _read(self, l11l1111l1_Krypto_):
        self.flush()
        data = self.__1lll11llll_Krypto_.l1lll11lll1_Krypto_(l11l1111l1_Krypto_)
        self.flush()
        return data
def new(*args, **kwargs):
    return l1lll11ll1l_Krypto_(*args, **kwargs)