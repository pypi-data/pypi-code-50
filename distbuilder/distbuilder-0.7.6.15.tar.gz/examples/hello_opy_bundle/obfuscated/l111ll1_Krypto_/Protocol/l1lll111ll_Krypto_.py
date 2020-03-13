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
l1l1111_Krypto_ (u"ࠧࠨࠢࡕࡪ࡬ࡷࠥ࡬ࡩ࡭ࡧࠣ࡭ࡲࡶ࡬ࡦ࡯ࡨࡲࡹࡹࠠࡢ࡮࡯࠱ࡴࡸ࠭࡯ࡱࡷ࡬࡮ࡴࡧࠡࡲࡤࡧࡰࡧࡧࡦࠢࡷࡶࡦࡴࡳࡧࡱࡵࡱࡦࡺࡩࡰࡰࡶ࠲ࠏࠐࡁ࡯ࠢࡤࡰࡱ࠳࡯ࡳ࠯ࡱࡳࡹ࡮ࡩ࡯ࡩࠣࡴࡦࡩ࡫ࡢࡩࡨࠤࡹࡸࡡ࡯ࡵࡩࡳࡷࡳࡡࡵ࡫ࡲࡲࠥ࡯ࡳࠡࡱࡱࡩࠥ࡯࡮ࠡࡹ࡫࡭ࡨ࡮ࠠࡴࡱࡰࡩࠥࡺࡥࡹࡶࠣ࡭ࡸࠐࡴࡳࡣࡱࡷ࡫ࡵࡲ࡮ࡧࡧࠤ࡮ࡴࡴࡰࠢࡰࡩࡸࡹࡡࡨࡧࠣࡦࡱࡵࡣ࡬ࡵ࠯ࠤࡸࡻࡣࡩࠢࡷ࡬ࡦࡺࠠࡢ࡮࡯ࠤࡧࡲ࡯ࡤ࡭ࡶࠤࡲࡻࡳࡵࠢࡥࡩࠥࡵࡢࡵࡣ࡬ࡲࡪࡪࠠࡣࡧࡩࡳࡷ࡫ࠊࡵࡪࡨࠤࡷ࡫ࡶࡦࡴࡶࡩࠥࡺࡲࡢࡰࡶࡪࡴࡸ࡭ࡢࡶ࡬ࡳࡳࠦࡣࡢࡰࠣࡦࡪࠦࡡࡱࡲ࡯࡭ࡪࡪ࠮ࠡࠢࡗ࡬ࡺࡹࠬࠡ࡫ࡩࠤࡦࡴࡹࠡࡤ࡯ࡳࡨࡱࡳࠡࡣࡵࡩࠥࡩ࡯ࡳࡴࡸࡴࡹ࡫ࡤࠋࡱࡵࠤࡱࡵࡳࡵ࠮ࠣࡸ࡭࡫ࠠࡰࡴ࡬࡫࡮ࡴࡡ࡭ࠢࡰࡩࡸࡹࡡࡨࡧࠣࡧࡦࡴ࡮ࡰࡶࠣࡦࡪࠦࡲࡦࡲࡵࡳࡩࡻࡣࡦࡦ࠱ࠎࠏࡇ࡮ࠡࡣ࡯ࡰ࠲ࡵࡲ࠮ࡰࡲࡸ࡭࡯࡮ࡨࠢࡳࡥࡨࡱࡡࡨࡧࠣࡸࡷࡧ࡮ࡴࡨࡲࡶࡲࡧࡴࡪࡱࡱࠤ࡮ࡹࠠ࡯ࡱࡷࠤࡪࡴࡣࡳࡻࡳࡸ࡮ࡵ࡮࠭ࠢࡤࡰࡹ࡮࡯ࡶࡩ࡫ࠤࡦࠦࡢ࡭ࡱࡦ࡯ࠏࡩࡩࡱࡪࡨࡶࠥࡧ࡬ࡨࡱࡵ࡭ࡹ࡮࡭ࠡ࡫ࡶࠤࡺࡹࡥࡥ࠰ࠣࠤ࡙࡮ࡥࠡࡧࡱࡧࡷࡿࡰࡵ࡫ࡲࡲࠥࡱࡥࡺࠢ࡬ࡷࠥࡸࡡ࡯ࡦࡲࡱࡱࡿࠠࡨࡧࡱࡩࡷࡧࡴࡦࡦࠣࡥࡳࡪࠠࡪࡵࠍࡩࡽࡺࡲࡢࡥࡷࡥࡧࡲࡥࠡࡨࡵࡳࡲࠦࡴࡩࡧࠣࡱࡪࡹࡳࡢࡩࡨࠤࡧࡲ࡯ࡤ࡭ࡶ࠲ࠏࠐࡔࡩ࡫ࡶࠤࡨࡲࡡࡴࡵࠣ࡭ࡲࡶ࡬ࡦ࡯ࡨࡲࡹࡹࠠࡵࡪࡨࠤࡆࡲ࡬࠮ࡑࡵ࠱ࡓࡵࡴࡩ࡫ࡱ࡫ࠥࡶࡡࡤ࡭ࡤ࡫ࡪࠦࡴࡳࡣࡱࡷ࡫ࡵࡲ࡮ࡣࡷ࡭ࡴࡴࠠࡢ࡮ࡪࡳࡷ࡯ࡴࡩ࡯ࠍࡨࡪࡹࡣࡳ࡫ࡥࡩࡩࠦࡩ࡯࠼ࠍࠎࡗࡵ࡮ࡢ࡮ࡧࠤࡑ࠴ࠠࡓ࡫ࡹࡩࡸࡺ࠮ࠡࠢࠥࡅࡱࡲ࠭ࡐࡴ࠰ࡒࡴࡺࡨࡪࡰࡪࠤࡊࡴࡣࡳࡻࡳࡸ࡮ࡵ࡮ࠡࡣࡱࡨ࡚ࠥࡨࡦࠢࡓࡥࡨࡱࡡࡨࡧࠣࡘࡷࡧ࡮ࡴࡨࡲࡶࡲࠨࠊࡩࡶࡷࡴ࠿࠵࠯ࡵࡪࡨࡳࡷࡿ࠮࡭ࡥࡶ࠲ࡲ࡯ࡴ࠯ࡧࡧࡹ࠴ࢄࡲࡪࡸࡨࡷࡹ࠵ࡦࡶࡵ࡬ࡳࡳ࠴ࡰࡥࡨࠍࠎࠧࠨࠢࣽ")
__revision__ = l1l1111_Krypto_ (u"ࠨࠤࡊࡦࠧࠦࣾ")
import operator as l1ll1ll1l1_Krypto_
import sys as l1l11l11_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l111l1ll_Krypto_ import l1ll111ll1_Krypto_, l1ll1lllll_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
from functools import reduce as l1ll11llll_Krypto_
def l1ll1l1lll_Krypto_(x):
    test = 0
    try:
        test += x
    except TypeError:
        return 0
    return 1
class l1lll111ll_Krypto_:
    l1l1111_Krypto_ (u"ࠢࠣࠤࡆࡰࡦࡹࡳࠡ࡫ࡰࡴࡱ࡫࡭ࡦࡰࡷ࡭ࡳ࡭ࠠࡵࡪࡨࠤࡆࡲ࡬࠮ࡱࡵ࠱ࡓࡵࡴࡩ࡫ࡱ࡫ࠥࡶࡡࡤ࡭ࡤ࡫ࡪࠦࡴࡳࡣࡱࡷ࡫ࡵࡲ࡮࠰ࠍࠎࠥࠦࠠࠡࡏࡨࡸ࡭ࡵࡤࡴࠢࡩࡳࡷࠦࡳࡶࡤࡦࡰࡦࡹࡳࡪࡰࡪ࠾ࠏࠐࠠࠡࠢࠣࠤࠥࠦࠠࡠ࡫ࡱࡺࡪࡴࡴ࡬ࡧࡼࠬࡰ࡫ࡹࡠࡵ࡬ࡾࡪ࠯࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹࠠࡢࠢࡵࡥࡳࡪ࡯࡮࡮ࡼࠤ࡬࡫࡮ࡦࡴࡤࡸࡪࡪࠠ࡬ࡧࡼ࠲ࠥࠦࡓࡶࡤࡦࡰࡦࡹࡳࡦࡵࠣࡧࡦࡴࠠࡶࡵࡨࠤࡹ࡮ࡩࡴࠢࡷࡳࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࡭ࡲࡶ࡬ࡦ࡯ࡨࡲࡹࠦࡢࡦࡶࡷࡩࡷࠦࡲࡢࡰࡧࡳࡲࠦ࡫ࡦࡻࠣ࡫ࡪࡴࡥࡳࡣࡷ࡭ࡳ࡭ࠠࡢ࡮ࡪࡳࡷ࡯ࡴࡩ࡯ࡶ࠲ࠥࠦࡔࡩࡧࠣࡨࡪ࡬ࡡࡶ࡮ࡷࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡤࡰ࡬ࡵࡲࡪࡶ࡫ࡱࠥ࡯ࡳࠡࡲࡵࡳࡧࡧࡢ࡭ࡻࠣࡲࡴࡺࠠࡷࡧࡵࡽࠥࡩࡲࡺࡲࡷࡳ࡬ࡸࡡࡱࡪ࡬ࡧࡦࡲ࡬ࡺࠢࡶࡩࡨࡻࡲࡦ࠰ࠍࠎࠥࠦࠠࠡࠤࠥࠦࣿ")
    def __init__(self, l1ll1l1l11_Krypto_, mode=None, l1l11lll_Krypto_=None):
        l1l1111_Krypto_ (u"ࠣࠤࠥࡅࡱࡲࡏࡳࡐࡲࡸ࡭࡯࡮ࡨࠪࡦ࡭ࡵ࡮ࡥࡳ࡯ࡲࡨࡺࡲࡥ࠭ࠢࡰࡳࡩ࡫࠽ࡏࡱࡱࡩ࠱ࠦࡉࡗ࠿ࡑࡳࡳ࡫ࠩࠋࠌࠣࠤࠥࠦࠠࠡࠢࠣࡧ࡮ࡶࡨࡦࡴࡰࡳࡩࡻ࡬ࡦࠢ࡬ࡷࠥࡧࠠ࡮ࡱࡧࡹࡱ࡫ࠠࡪ࡯ࡳࡰࡪࡳࡥ࡯ࡶ࡬ࡲ࡬ࠦࡴࡩࡧࠣࡧ࡮ࡶࡨࡦࡴࠣࡥࡱ࡭࡯ࡳ࡫ࡷ࡬ࡲࠦࡴࡰࠌࠣࠤࠥࠦࠠࠡࠢࠣࡹࡸ࡫࠮ࠡࠢࡌࡸࠥࡳࡵࡴࡶࠣࡴࡷࡵࡶࡪࡦࡨࠤࡹ࡮ࡥࠡࡒࡈࡔ࠷࠽࠲ࠡ࡫ࡱࡸࡪࡸࡦࡢࡥࡨ࠲ࠏࠐࠠࠡࠢࠣࠤࠥࠦࠠࡏࡱࡷࡩࠥࡺࡨࡢࡶࠣࡸ࡭࡫ࠠࡦࡰࡦࡶࡾࡶࡴࡪࡱࡱࠤࡰ࡫ࡹࠡ࡫ࡶࠤࡷࡧ࡮ࡥࡱࡰࡰࡾࠦࡧࡦࡰࡨࡶࡦࡺࡥࡥࠌࠣࠤࠥࠦࠠࠡࠢࠣࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡨࡧ࡬࡭ࡻࠣࡻ࡭࡫࡮ࠡࡰࡨࡩࡩ࡫ࡤ࠯ࠢࠣࡓࡵࡺࡩࡰࡰࡤࡰࠥࡧࡲࡨࡷࡰࡩࡳࡺࡳࠡ࡯ࡲࡨࡪࠦࡡ࡯ࡦࠣࡍ࡛ࠦࡡࡳࡧࠍࠤࠥࠦࠠࠡࠢࠣࠤࡵࡧࡳࡴࡧࡧࠤࡩ࡯ࡲࡦࡥࡷࡰࡾࠦࡴࡩࡴࡲࡹ࡬࡮ࠠࡵࡱࠣࡸ࡭࡫ࠠࡤ࡫ࡳ࡬ࡪࡸ࡭ࡰࡦࡸࡰࡪ࠴࡮ࡦࡹࠫ࠭ࠥࡳࡥࡵࡪࡲࡨࡀࠦࡴࡩࡧࡼࠎࠥࠦࠠࠡࠢࠣࠤࠥࡧࡲࡦࠢࡷ࡬ࡪࠦࡦࡦࡧࡧࡦࡦࡩ࡫ࠡ࡯ࡲࡨࡪࠦࡡ࡯ࡦࠣ࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡿࡧࡴࡪࡱࡱࠤࡻ࡫ࡣࡵࡱࡵࠤࡹࡵࠠࡶࡵࡨ࠲ࠥࠦࡁ࡭࡮ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡹ࡮ࡲࡦࡧࠣࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠦ࡭ࡶࡵࡷࠤࡧ࡫ࠠࡵࡪࡨࠤࡸࡧ࡭ࡦࠢࡩࡳࡷࠦࡴࡩࡧࠣࡳࡧࡰࡥࡤࡶࠣࡹࡸ࡫ࡤࠡࡶࡲࠤࡨࡸࡥࡢࡶࡨࠎࠥࠦࠠࠡࠢࠣࠤࠥࡺࡨࡦࠢࡧ࡭࡬࡫ࡳࡵ࠮ࠣࡥࡳࡪࠠࡵࡱࠣࡹࡳࡪࡩࡨࡧࡶࡸࠬ࡯ࡦࡺࠢࡷ࡬ࡪࠦ࡭ࡦࡵࡶࡥ࡬࡫ࠠࡣ࡮ࡲࡧࡰࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧऀ")
        self.__1ll1ll1ll_Krypto_ = l1ll1l1l11_Krypto_
        self.__1ll1ll111_Krypto_ = mode
        self.__1ll111l1l_Krypto_ = l1l11lll_Krypto_
        self.__1ll11l11l_Krypto_ = l1ll1l1l11_Krypto_.l111l1l_Krypto_
        if not l1ll1l1lll_Krypto_(self.__1ll11l11l_Krypto_) or self.__1ll11l11l_Krypto_==0:
            self.__1ll11l11l_Krypto_ = 16
    __1ll1l11ll_Krypto_ = l11111l11_Krypto_(0x69)
    def digest(self, text):
        l1l1111_Krypto_ (u"ࠤࠥࠦࡩ࡯ࡧࡦࡵࡷࠬࡹ࡫ࡸࡵ࠼ࡶࡸࡷ࡯࡮ࡨࠫࠣ࠾ࠥࡡࡳࡵࡴ࡬ࡲ࡬ࡣࠊࠋࠢࠣࠤࠥࠦࠠࠡࠢࡓࡩࡷ࡬࡯ࡳ࡯ࠣࡸ࡭࡫ࠠࡂ࡮࡯࠱ࡴࡸ࠭ࡏࡱࡷ࡬࡮ࡴࡧࠡࡲࡤࡧࡰࡧࡧࡦࠢࡷࡶࡦࡴࡳࡧࡱࡵࡱࠥࡵ࡮ࠡࡶ࡫ࡩࠥ࡭ࡩࡷࡧࡱࠎࠥࠦࠠࠡࠢࠣࠤࠥࡹࡴࡳ࡫ࡱ࡫࠳ࠦࠠࡐࡷࡷࡴࡺࡺࠠࡪࡵࠣࡥࠥࡲࡩࡴࡶࠣࡳ࡫ࠦ࡭ࡦࡵࡶࡥ࡬࡫ࠠࡣ࡮ࡲࡧࡰࡹࠠࡥࡧࡶࡧࡷ࡯ࡢࡪࡰࡪࠤࡹ࡮ࡥࠋࠢࠣࠤࠥࠦࠠࠡࠢࡷࡶࡦࡴࡳࡧࡱࡵࡱࡪࡪࠠࡵࡧࡻࡸ࠱ࠦࡷࡩࡧࡵࡩࠥ࡫ࡡࡤࡪࠣࡦࡱࡵࡣ࡬ࠢ࡬ࡷࠥࡧࠠࡴࡶࡵ࡭ࡳ࡭ࠠࡰࡨࠣࡦ࡮ࡺࠠ࡭ࡧࡱ࡫ࡹ࡮ࠠࡦࡳࡸࡥࡱࠐࠠࠡࠢࠣࠤࠥࠦࠠࡵࡱࠣࡸ࡭࡫ࠠࡤ࡫ࡳ࡬ࡪࡸ࡭ࡰࡦࡸࡰࡪ࠭ࡳࠡࡤ࡯ࡳࡨࡱ࡟ࡴ࡫ࡽࡩ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥँ")
        key = self._1ll1l1111_Krypto_(self.__1ll11l11l_Krypto_)
        l1ll1l1ll1_Krypto_ = self.__1ll1l11ll_Krypto_ * self.__1ll11l11l_Krypto_
        l1ll11l1l1_Krypto_ = self.__1ll1l111l_Krypto_(key)
        l1lll1111l_Krypto_ = self.__1ll1l111l_Krypto_(l1ll1l1ll1_Krypto_)
        block_size = self.__1ll1ll1ll_Krypto_.block_size
        l1ll111l11_Krypto_ = block_size - (len(text) % block_size)
        text = text + b(l1l1111_Krypto_ (u"ࠪࠤࠬं")) * l1ll111l11_Krypto_
        s = divmod(len(text), block_size)[0]
        l1ll11l111_Krypto_ = []
        l1ll111lll_Krypto_ = []
        for i in range(1, s+1):
            start = (i-1) * block_size
            end = start + block_size
            l1lll11111_Krypto_ = text[start:end]
            assert len(l1lll11111_Krypto_) == block_size
            l1ll11ll1l_Krypto_ = l1ll11l1l1_Krypto_.l1_Krypto_(l1ll1lllll_Krypto_(i, block_size))
            l1ll11l1ll_Krypto_ = l1ll111ll1_Krypto_(l1lll11111_Krypto_) ^ l1ll111ll1_Krypto_(l1ll11ll1l_Krypto_)
            l1ll11l111_Krypto_.append(l1ll11l1ll_Krypto_)
            hi = l1lll1111l_Krypto_.l1_Krypto_(l1ll1lllll_Krypto_(l1ll11l1ll_Krypto_ ^ i, block_size))
            l1ll111lll_Krypto_.append(l1ll111ll1_Krypto_(hi))
        i = i + 1
        l1ll11ll1l_Krypto_ = l1ll11l1l1_Krypto_.l1_Krypto_(l1ll1lllll_Krypto_(i, block_size))
        l1ll11l1ll_Krypto_ = l1ll111l11_Krypto_ ^ l1ll111ll1_Krypto_(l1ll11ll1l_Krypto_)
        l1ll11l111_Krypto_.append(l1ll11l1ll_Krypto_)
        hi = l1lll1111l_Krypto_.l1_Krypto_(l1ll1lllll_Krypto_(l1ll11l1ll_Krypto_ ^ i, block_size))
        l1ll111lll_Krypto_.append(l1ll111ll1_Krypto_(hi))
        l1ll1lll11_Krypto_ = l1ll111ll1_Krypto_(key) ^ l1ll11llll_Krypto_(l1ll1ll1l1_Krypto_.xor, l1ll111lll_Krypto_)
        l1ll11l111_Krypto_.append(l1ll1lll11_Krypto_)
        return [l1ll1lllll_Krypto_(i,self.__1ll1ll1ll_Krypto_.block_size) for i in l1ll11l111_Krypto_]
    def l1ll1llll1_Krypto_(self, l1ll11l111_Krypto_):
        l1l1111_Krypto_ (u"ࠦࠧࠨࡵ࡯ࡦ࡬࡫ࡪࡹࡴࠩࡤ࡯ࡳࡨࡱࡳࠡ࠼ࠣ࡟ࡸࡺࡲࡪࡰࡪࡡ࠮ࠦ࠺ࠡࡵࡷࡶ࡮ࡴࡧࠋࠌࠣࠤࠥࠦࠠࠡࠢࠣࡔࡪࡸࡦࡰࡴࡰࠤࡹ࡮ࡥࠡࡴࡨࡺࡪࡸࡳࡦࠢࡳࡥࡨࡱࡡࡨࡧࠣࡸࡷࡧ࡮ࡴࡨࡲࡶࡲࡧࡴࡪࡱࡱࠤࡴࡴࠠࡢࠢ࡯࡭ࡸࡺࠠࡰࡨࠣࡱࡪࡹࡳࡢࡩࡨࠎࠥࠦࠠࠡࠢࠣࠤࠥࡨ࡬ࡰࡥ࡮ࡷ࠳ࠦࠠࡏࡱࡷࡩࠥࡺࡨࡢࡶࠣࡸ࡭࡫ࠠࡤ࡫ࡳ࡬ࡪࡸ࡭ࡰࡦࡸࡰࡪࠦࡵࡴࡧࡧࠤ࡫ࡵࡲࠡࡤࡲࡸ࡭ࠦࡴࡳࡣࡱࡷ࡫ࡵࡲ࡮ࡣࡷ࡭ࡴࡴࡳࠋࠢࠣࠤࠥࠦࠠࠡࠢࡰࡹࡸࡺࠠࡣࡧࠣࡸ࡭࡫ࠠࡴࡣࡰࡩ࠳ࠦࠠࡣ࡮ࡲࡧࡰࡹࠠࡪࡵࠣࡥࠥࡲࡩࡴࡶࠣࡳ࡫ࠦࡳࡵࡴ࡬ࡲ࡬ࡹࠠࡰࡨࠣࡦ࡮ࡺࠠ࡭ࡧࡱ࡫ࡹ࡮ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡧࡴࡹࡦࡲࠠࡵࡱࠣࡸ࡭࡫ࠠࡤ࡫ࡳ࡬ࡪࡸ࡭ࡰࡦࡸࡰࡪ࠭ࡳࠡࡤ࡯ࡳࡨࡱ࡟ࡴ࡫ࡽࡩ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥः")
        if len(l1ll11l111_Krypto_) < 2:
            raise ValueError(l1l1111_Krypto_ (u"ࠧࡒࡩࡴࡶࠣࡱࡺࡹࡴࠡࡤࡨࠤࡦࡺࠠ࡭ࡧࡤࡷࡹࠦ࡬ࡦࡰࡪࡸ࡭ࠦ࠲࠯ࠤऄ"))
        l1ll11l111_Krypto_ = list(map(l1ll111ll1_Krypto_, l1ll11l111_Krypto_))
        l1ll1l1ll1_Krypto_ = self.__1ll1l11ll_Krypto_ * self.__1ll11l11l_Krypto_
        l1lll1111l_Krypto_ = self.__1ll1l111l_Krypto_(l1ll1l1ll1_Krypto_)
        block_size = self.__1ll1ll1ll_Krypto_.block_size
        l1ll111lll_Krypto_ = []
        for i in range(1, len(l1ll11l111_Krypto_)):
            l1ll11l1ll_Krypto_ = l1ll11l111_Krypto_[i-1] ^ i
            hi = l1lll1111l_Krypto_.l1_Krypto_(l1ll1lllll_Krypto_(l1ll11l1ll_Krypto_, block_size))
            l1ll111lll_Krypto_.append(l1ll111ll1_Krypto_(hi))
        key = l1ll11l111_Krypto_[-1] ^ l1ll11llll_Krypto_(l1ll1ll1l1_Krypto_.xor, l1ll111lll_Krypto_)
        l1ll11l1l1_Krypto_ = self.__1ll1l111l_Krypto_(l1ll1lllll_Krypto_(key, self.__1ll11l11l_Krypto_))
        parts = []
        for i in range(1, len(l1ll11l111_Krypto_)):
            l1ll11ll1l_Krypto_ = l1ll11l1l1_Krypto_.l1_Krypto_(l1ll1lllll_Krypto_(i, block_size))
            l1lll11111_Krypto_ = l1ll11l111_Krypto_[i-1] ^ l1ll111ll1_Krypto_(l1ll11ll1l_Krypto_)
            parts.append(l1lll11111_Krypto_)
        l1ll111l11_Krypto_ = int(parts[-1])
        text = b(l1l1111_Krypto_ (u"࠭ࠧअ")).join(map(l1ll1lllll_Krypto_, parts[:-1]))
        return text[:-l1ll111l11_Krypto_]
    def _1ll1l1111_Krypto_(self, l111l1l_Krypto_):
        from l111ll1_Krypto_ import l1ll1l11l1_Krypto_
        return l1ll1l11l1_Krypto_.new().read(l111l1l_Krypto_)
    def __1ll1l111l_Krypto_(self, key):
        if self.__1ll1ll111_Krypto_ is None and self.__1ll111l1l_Krypto_ is None:
            return self.__1ll1ll1ll_Krypto_.new(key)
        elif self.__1ll111l1l_Krypto_ is None:
            return self.__1ll1ll1ll_Krypto_.new(key, self.__1ll1ll111_Krypto_)
        else:
            return self.__1ll1ll1ll_Krypto_.new(key, self.__1ll1ll111_Krypto_, self.__1ll111l1l_Krypto_)
if __name__ == l1l1111_Krypto_ (u"ࠧࡠࡡࡰࡥ࡮ࡴ࡟ࡠࠩआ"):
    import sys as l1l11l11_Krypto_
    import getopt as l1ll1lll1l_Krypto_
    import base64 as l1lll111l1_Krypto_
    l1ll11ll11_Krypto_ = l1l1111_Krypto_ (u"ࠨࠩࠪࡠࠏ࡚ࡥࡴࡶࠣࡱࡴࡪࡵ࡭ࡧࠣࡹࡸࡧࡧࡦ࠼ࠣࠩ࠭ࡶࡲࡰࡩࡵࡥࡲ࠯ࡳࠡ࡝࠰ࡧࠥࡩࡩࡱࡪࡨࡶࡢ࡛ࠦ࠮࡮ࡠࠤࡠ࠳ࡨ࡞ࠌࠍ࡛࡭࡫ࡲࡦ࠼ࠍࠤࠥࠦࠠ࠮࠯ࡦ࡭ࡵ࡮ࡥࡳࠢࡰࡳࡩࡻ࡬ࡦࠌࠣࠤࠥࠦ࠭ࡤࠢࡰࡳࡩࡻ࡬ࡦࠌࠣࠤࠥࠦࠠࠡࠢࠣࡇ࡮ࡶࡨࡦࡴࠣࡱࡴࡪࡵ࡭ࡧࠣࡸࡴࠦࡵࡴࡧ࠱ࠤࠥࡊࡥࡧࡣࡸࡰࡹࡀࠠࠦࠪࡦ࡭ࡵ࡮ࡥࡳ࡯ࡲࡨࡺࡲࡥࠪࡵࠍࠎࠥࠦࠠࠡ࠯࠰ࡥࡸࡲ࡯࡯ࡩࠍࠤࠥࠦࠠ࠮࡮ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡕࡸࡩ࡯ࡶࠣࡸ࡭࡫ࠠࡦࡰࡦࡳࡩ࡫ࡤࠡ࡯ࡨࡷࡸࡧࡧࡦࠢࡥࡰࡴࡩ࡫ࡴࠢࡤࡷࠥࡲ࡯࡯ࡩࠣ࡭ࡳࡺࡥࡨࡧࡵࡷࠥ࡯࡮ࡴࡶࡨࡥࡩࠦ࡯ࡧࠢࡥࡥࡸ࡫࠶࠵ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡩࡳࡩ࡯ࡥࡧࡧࠤࡸࡺࡲࡪࡰࡪࡷࠏࠐࠠࠡࠢࠣ࠱࠲࡮ࡥ࡭ࡲࠍࠤࠥࠦࠠ࠮ࡪࠍࠤࠥࠦࠠࠡࠢࠣࠤࡕࡸࡩ࡯ࡶࠣࡸ࡭࡯ࡳࠡࡪࡨࡰࡵࠦ࡭ࡦࡵࡶࡥ࡬࡫ࠊࠨࠩࠪइ")
    l1ll1l1l11_Krypto_ = l1l1111_Krypto_ (u"ࠩࡄࡉࡘ࠭ई")
    l1ll1ll11l_Krypto_ = 0
    def usage(code, msg=None):
        if msg:
            print(msg)
        print(l1ll11ll11_Krypto_ % {l1l1111_Krypto_ (u"ࠪࡴࡷࡵࡧࡳࡣࡰࠫउ"): l1l11l11_Krypto_.argv[0],
                          l1l1111_Krypto_ (u"ࠫࡨ࡯ࡰࡩࡧࡵࡱࡴࡪࡵ࡭ࡧࠪऊ"): l1ll1l1l11_Krypto_})
        l1l11l11_Krypto_.exit(code)
    try:
        opts, args = l1ll1lll1l_Krypto_.l1ll1lll1l_Krypto_(l1l11l11_Krypto_.argv[1:],
                                   l1l1111_Krypto_ (u"ࠬࡩ࠺࡭ࠩऋ"), [l1l1111_Krypto_ (u"࠭ࡣࡪࡲ࡫ࡩࡷࡃࠧऌ"), l1l1111_Krypto_ (u"ࠧࡢࡵ࡯ࡳࡳ࡭ࠧऍ")])
    except l1ll1lll1l_Krypto_.error as msg:
        usage(1, msg)
    if args:
        usage(1, l1l1111_Krypto_ (u"ࠨࡖࡲࡳࠥࡳࡡ࡯ࡻࠣࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ऎ"))
    for opt, arg in opts:
        if opt in (l1l1111_Krypto_ (u"ࠩ࠰࡬ࠬए"), l1l1111_Krypto_ (u"ࠪ࠱࠲࡮ࡥ࡭ࡲࠪऐ")):
            usage(0)
        elif opt in (l1l1111_Krypto_ (u"ࠫ࠲ࡩࠧऑ"), l1l1111_Krypto_ (u"ࠬ࠳࠭ࡤ࡫ࡳ࡬ࡪࡸࠧऒ")):
            l1ll1l1l11_Krypto_ = arg
        elif opt in (l1l1111_Krypto_ (u"࠭࠭࡭ࠩओ"), l1l1111_Krypto_ (u"ࠧ࠮࠯ࡤࡷࡱࡵ࡮ࡨࠩऔ")):
            l1ll1ll11l_Krypto_ = 1
    module = __import__(l1l1111_Krypto_ (u"ࠨࡅࡵࡽࡵࡺ࡯࠯ࡅ࡬ࡴ࡭࡫ࡲ࠯ࠩक")+l1ll1l1l11_Krypto_, None, None, [l1l1111_Krypto_ (u"ࠩࡱࡩࡼ࠭ख")])
    x = l1lll111ll_Krypto_(module)
    print(l1l1111_Krypto_ (u"ࠪࡓࡷ࡯ࡧࡪࡰࡤࡰࠥࡺࡥࡹࡶ࠽ࡠࡳࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠩग"))
    print(__doc__)
    print(l1l1111_Krypto_ (u"ࠫࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠨघ"))
    l1ll1l1l1l_Krypto_ = x.digest(b(__doc__))
    print(l1l1111_Krypto_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪࠦࡢ࡭ࡱࡦ࡯ࡸࡀࠧङ"))
    for i, l1ll11lll1_Krypto_ in zip(list(range(len(l1ll1l1l1l_Krypto_))), l1ll1l1l1l_Krypto_):
        print(l1l1111_Krypto_ (u"࠭ࠠࠡࠢࠣࠩ࠸ࡪࠧच") % i, end=l1l1111_Krypto_ (u"ࠧࠡࠩछ"))
        if l1ll1ll11l_Krypto_:
            print(l1ll111ll1_Krypto_(l1ll11lll1_Krypto_))
        else:
            print(l1lll111l1_Krypto_.encodestring(l1ll11lll1_Krypto_)[:-1])
    y = l1lll111ll_Krypto_(module)
    text = y.l1ll1llll1_Krypto_(l1ll1l1l1l_Krypto_)
    if text == b(__doc__):
        print(l1l1111_Krypto_ (u"ࠨࡖ࡫ࡩࡾࠦ࡭ࡢࡶࡦ࡬ࠦ࠭ज"))
    else:
        print(l1l1111_Krypto_ (u"ࠩࡗ࡬ࡪࡿࠠࡥ࡫ࡩࡪࡪࡸࠡࠨझ"))