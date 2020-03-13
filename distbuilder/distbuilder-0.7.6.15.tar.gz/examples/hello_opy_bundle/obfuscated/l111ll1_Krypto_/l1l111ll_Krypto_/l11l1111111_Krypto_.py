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
__revision__ = l1l1111_Krypto_ (u"ࠨࠤࡊࡦࠧࠦ᪓")
from l111ll1_Krypto_.l11lll1_Krypto_ import l11ll11_Krypto_
import l111ll1_Krypto_.l1ll1l11l1_Krypto_
import warnings as l11ll1ll11_Krypto_
class l11l1111ll1_Krypto_:
    l1l1111_Krypto_ (u"ࠢࠣࠤࡇࡩࡵࡸࡥࡤࡣࡷࡩࡩ࠴ࠠࠡࡗࡶࡩࠥࡘࡡ࡯ࡦࡲࡱ࠳ࡴࡥࡸࠪࠬࠤ࡮ࡴࡳࡵࡧࡤࡨ࠳ࠐࠊࠡࠢࠣࠤࡘ࡫ࡥࠡࡪࡷࡸࡵࡀ࠯࠰ࡹࡺࡻ࠳ࡶࡹࡤࡴࡼࡴࡹࡵ࠮ࡰࡴࡪ࠳ࡷࡧ࡮ࡥࡲࡲࡳࡱ࠳ࡢࡳࡱ࡮ࡩࡳࠐࠠࠡࠢࠣࠦࠧࠨ᪔")
    def __init__(self, l1lll111111l_Krypto_ = 160, l1llll11l_Krypto_=None, hash=None, file=None):
        l11ll1ll11_Krypto_.warn(l1l1111_Krypto_ (u"ࠣࡖ࡫࡭ࡸࠦࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱࠤࡺࡹࡥࡴࠢࡕࡥࡳࡪ࡯࡮ࡒࡲࡳࡱ࠲ࠠࡸࡪ࡬ࡧ࡭ࠦࡩࡴࠢࡅࡖࡔࡑࡅࡏࠢ࡬ࡲࠥࡵ࡬ࡥࡧࡵࠤࡷ࡫࡬ࡦࡣࡶࡩࡸ࠴ࠠࠡࡕࡨࡩࠥ࡮ࡴࡵࡲ࠽࠳࠴ࡽࡷࡸ࠰ࡳࡽࡨࡸࡹࡱࡶࡲ࠲ࡴࡸࡧ࠰ࡴࡤࡲࡩࡶ࡯ࡰ࡮࠰ࡦࡷࡵ࡫ࡦࡰࠥ᪕"),
            l11ll11_Krypto_)
        self.__1lll11111ll_Krypto_ = l111ll1_Krypto_.l1ll1l11l1_Krypto_.new()
        self.bytes = l1lll111111l_Krypto_
        self.bits = self.bytes * 8
        self.l11l11111l1_Krypto_ = self.bits
    def l1lll11lll1_Krypto_(self, l11l1111l1_Krypto_):
        return self.__1lll11111ll_Krypto_.read(l11l1111l1_Krypto_)
    def _1ll1llllll1_Krypto_(self, l1llll111l1_Krypto_):
        self.l11l11111l1_Krypto_ += l1llll111l1_Krypto_
        if self.l11l11111l1_Krypto_ < 0:
            self.l11l11111l1_Krypto_ = 0
        elif self.l11l11111l1_Krypto_ > self.bits:
            self.l11l11111l1_Krypto_ = self.bits
    def _1lll1111111_Krypto_(self, l11l1111l1_Krypto_=0, l1lll111lll_Krypto_=l1l1111_Krypto_ (u"ࠤ࠲ࡨࡪࡼ࠯ࡶࡴࡤࡲࡩࡵ࡭ࠣ᪖")):
        l1l1111_Krypto_ (u"ࠥࠦࠧࡊࡵ࡮࡯ࡼࠤࡤࡸࡡ࡯ࡦࡲࡱ࡮ࢀࡥࠩࠫࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠧࠨࠢ᪗")
        self.__1lll11111ll_Krypto_.flush()
    def l11l111111l_Krypto_(self, l11l1111l1_Krypto_=0):
        l1l1111_Krypto_ (u"ࠦࠧࠨࡄࡶ࡯ࡰࡽࠥࡸࡡ࡯ࡦࡲࡱ࡮ࢀࡥࠩࠫࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠧࠨࠢ᪘")
        self.__1lll11111ll_Krypto_.flush()
    def l11l1111l1l_Krypto_(self, s=l1l1111_Krypto_ (u"ࠬ࠭᪙")):
        l1l1111_Krypto_ (u"ࠨࠢࠣࡆࡸࡱࡲࡿࠠࡴࡶ࡬ࡶ࠭࠯ࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࠤࠥࠦ᪚")
        self.__1lll11111ll_Krypto_.flush()
    def l1ll1lllll1l_Krypto_(self, l11l1111l1_Krypto_=3):
        l1l1111_Krypto_ (u"ࠢࠣࠤࡇࡹࡲࡳࡹࠡࡵࡷ࡭ࡷࡥ࡮ࠩࠫࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠧࠨࠢ᪛")
        self.__1lll11111ll_Krypto_.flush()
    def l11l11111ll_Krypto_(self, s=l1l1111_Krypto_ (u"ࠨࠩ᪜")):
        l1l1111_Krypto_ (u"ࠤࠥࠦࡉࡻ࡭࡮ࡻࠣࡥࡩࡪ࡟ࡦࡸࡨࡲࡹ࠮ࠩࠡࡨࡸࡲࡨࡺࡩࡰࡰࠥࠦࠧ᪝")
        self.__1lll11111ll_Krypto_.flush()
    def l1lll11111l1_Krypto_(self, l11l1111l1_Krypto_):
        l1l1111_Krypto_ (u"ࠥࠦࠧࡊࡵ࡮࡯ࡼࠤ࡬࡫ࡴࡃࡻࡷࡩࡸ࠮ࠩࠡࡨࡸࡲࡨࡺࡩࡰࡰࠥࠦࠧ᪞")
        return self.l1lll11lll1_Krypto_(l11l1111l1_Krypto_)
    def l1ll1lllllll_Krypto_(self, event, s=l1l1111_Krypto_ (u"ࠦࠧ᪟")):
        l1l1111_Krypto_ (u"ࠧࠨࠢࡅࡷࡰࡱࡾࠦࡡࡥࡦࡈࡺࡪࡴࡴࠩࠫࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠧࠨࠢ᪠")
        return self.l11l11111ll_Krypto_()