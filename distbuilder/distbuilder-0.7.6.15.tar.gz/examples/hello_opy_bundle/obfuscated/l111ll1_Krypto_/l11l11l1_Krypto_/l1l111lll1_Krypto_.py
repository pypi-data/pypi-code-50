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
__revision__ = l1l1111_Krypto_ (u"ࠤࠧࡍࡩࠪࠢॿ")
import types as l11ll1l1ll_Krypto_,warnings as l11ll1ll11_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l111l1ll_Krypto_ import *
class l1l111lll1_Krypto_:
    l1l1111_Krypto_ (u"ࠥࠦࠧࡇ࡮ࠡࡣࡥࡷࡹࡸࡡࡤࡶࠣࡧࡱࡧࡳࡴࠢࡩࡳࡷࠦࡡࠡࡲࡸࡦࡱ࡯ࡣࠡ࡭ࡨࡽࠥࡵࡢ࡫ࡧࡦࡸ࠳ࠐࠊࠡࠢࠣࠤ࠿ࡻ࡮ࡥࡱࡦࡹࡲ࡫࡮ࡵࡧࡧ࠾ࠥࡥ࡟ࡨࡧࡷࡷࡹࡧࡴࡦࡡࡢ࠰ࠥࡥ࡟ࡴࡧࡷࡷࡹࡧࡴࡦࡡࡢ࠰ࠥࡥ࡟ࡦࡳࡢࡣ࠱ࠦ࡟ࡠࡰࡨࡣࡤ࠲ࠠࡷࡣ࡯࡭ࡩࡧࡴࡦࠌࠣࠤࠥࠦࠢࠣࠤঀ")
    def __init__(self):
        pass
    def __getstate__(self):
        l1l1111_Krypto_ (u"ࠦࠧࠨࡔࡰࠢ࡮ࡩࡪࡶࠠ࡬ࡧࡼࠤࡴࡨࡪࡦࡥࡷࡷࠥࡶ࡬ࡢࡶࡩࡳࡷࡳ࠭ࡪࡰࡧࡩࡵ࡫࡮ࡥࡧࡱࡸ࠱ࠦࡴࡩࡧࠣ࡯ࡪࡿࠠࡥࡣࡷࡥࠥ࡯ࡳࠋࠢࠣࠤࠥࠦࠠࠡࠢࡦࡳࡳࡼࡥࡳࡶࡨࡨࠥࡺ࡯ࠡࡵࡷࡥࡳࡪࡡࡳࡦࠣࡔࡾࡺࡨࡰࡰࠣࡰࡴࡴࡧࠡ࡫ࡱࡸࡪ࡭ࡥࡳࡵࠣࡦࡪ࡬࡯ࡳࡧࠣࡦࡪ࡯࡮ࡨࠌࠣࠤࠥࠦࠠࠡࠢࠣࡻࡷ࡯ࡴࡵࡧࡱࠤࡴࡻࡴ࠯ࠢࠣࡍࡹࠦࡷࡪ࡮࡯ࠤࡹ࡮ࡥ࡯ࠢࡥࡩࠥࡸࡥࡤࡱࡱࡺࡪࡸࡴࡦࡦࠣࡥࡸࠦ࡮ࡦࡥࡨࡷࡸࡧࡲࡺࠢࡲࡲࠏࠦࠠࠡࠢࠣࠤࠥࠦࡲࡦࡵࡷࡳࡷࡧࡴࡪࡱࡱ࠲ࠧࠨࠢঁ")
        d=self.__dict__
        for key in self.l1l1l11111_Krypto_:
            if key in d: d[key]=int(d[key])
        return d
    def __setstate__(self, d):
        l1l1111_Krypto_ (u"ࠧࠨࠢࡐࡰࠣࡹࡳࡶࡩࡤ࡭࡯࡭ࡳ࡭ࠠࡢࠢ࡮ࡩࡾࠦ࡯ࡣ࡬ࡨࡧࡹ࠲ࠠࡵࡪࡨࠤࡰ࡫ࡹࠡࡦࡤࡸࡦࠦࡩࡴࠢࡦࡳࡳࡼࡥࡳࡶࡨࡨࠥࡺ࡯ࠡࡶ࡫ࡩࠥࡨࡩࡨࠌࡱࡹࡲࡨࡥࡳࠢࡵࡩࡵࡸࡥࡴࡧࡱࡸࡦࡺࡩࡰࡰࠣࡦࡪ࡯࡮ࡨࠢࡸࡷࡪࡪࠬࠡࡹ࡫ࡩࡹ࡮ࡥࡳࠢࡷ࡬ࡦࡺࠠࡪࡵࠣࡔࡾࡺࡨࡰࡰࠣࡰࡴࡴࡧࠋ࡫ࡱࡸࡪ࡭ࡥࡳࡵ࠯ࠤࡒࡖ࡚ࠡࡱࡥ࡮ࡪࡩࡴࡴ࠮ࠣࡳࡷࠦࡷࡩࡣࡷࡩࡻ࡫ࡲ࠯ࠤࠥࠦং")
        for key in self.l1l1l11111_Krypto_:
            if key in d: self.__dict__[key]=l11lllll11_Krypto_(d[key])
    def l1_Krypto_(self, l1ll11l1_Krypto_, l1l111ll1l_Krypto_):
        l1l1111_Krypto_ (u"ࠨࠢࠣࡇࡱࡧࡷࡿࡰࡵࠢࡤࠤࡵ࡯ࡥࡤࡧࠣࡳ࡫ࠦࡤࡢࡶࡤ࠲ࠏࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠻ࡒࡤࡶࡦࡳࡥࡵࡧࡵࠤࡵࡲࡡࡪࡰࡷࡩࡽࡺ࠺ࠡࡖ࡫ࡩࠥࡶࡩࡦࡥࡨࠤࡴ࡬ࠠࡥࡣࡷࡥࠥࡺ࡯ࠡࡧࡱࡧࡷࡿࡰࡵ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࠿࡚ࡹࡱࡧࠣࡴࡱࡧࡩ࡯ࡶࡨࡼࡹࡀࠠࡣࡻࡷࡩࠥࡹࡴࡳ࡫ࡱ࡫ࠥࡵࡲࠡ࡮ࡲࡲ࡬ࠐࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠼ࡓࡥࡷࡧ࡭ࡦࡶࡨࡶࠥࡑ࠺ࠡࡃࠣࡶࡦࡴࡤࡰ࡯ࠣࡴࡦࡸࡡ࡮ࡧࡷࡩࡷࠦࡲࡦࡳࡸ࡭ࡷ࡫ࡤࠡࡤࡼࠤࡸࡵ࡭ࡦࠢࡤࡰ࡬ࡵࡲࡪࡶ࡫ࡱࡸࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠻ࡖࡼࡴࡪࠦࡋ࠻ࠢࡥࡽࡹ࡫ࠠࡴࡶࡵ࡭ࡳ࡭ࠠࡰࡴࠣࡰࡴࡴࡧࠋࠌࠣࠤࠥࠦࠠࠡࠢࠣ࠾ࡗ࡫ࡴࡶࡴࡱ࠾ࠥࡇࠠࡵࡷࡳࡰࡪࠦࡷࡪࡶ࡫ࠤࡹࡽ࡯ࠡ࡫ࡷࡩࡲࡹ࠮ࠡࡇࡤࡧ࡭ࠦࡩࡵࡧࡰࠤ࡮ࡹࠠࡰࡨࠣࡸ࡭࡫ࠠࡴࡣࡰࡩࠥࡺࡹࡱࡧࠣࡥࡸࠦࡴࡩࡧࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࡶ࡬ࡢ࡫ࡱࡸࡪࡾࡴࠡࠪࡶࡸࡷ࡯࡮ࡨࠢࡲࡶࠥࡲ࡯࡯ࡩࠬ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤঃ")
        l11ll1l1l1_Krypto_=0
        if isinstance(l1ll11l1_Krypto_, bytes):
            l1ll11l1_Krypto_=l1ll111ll1_Krypto_(l1ll11l1_Krypto_) ; l11ll1l1l1_Krypto_=1
        if isinstance(l1l111ll1l_Krypto_, bytes):
            l1l111ll1l_Krypto_=l1ll111ll1_Krypto_(l1l111ll1l_Krypto_)
        l1ll111l_Krypto_=self._1l11l1lll_Krypto_(l1ll11l1_Krypto_, l1l111ll1l_Krypto_)
        if l11ll1l1l1_Krypto_: return tuple(map(l1ll1lllll_Krypto_, l1ll111l_Krypto_))
        else: return l1ll111l_Krypto_
    def l1lllll_Krypto_(self, l1ll111l_Krypto_):
        l1l1111_Krypto_ (u"ࠢࠣࠤࡇࡩࡨࡸࡹࡱࡶࠣࡥࠥࡶࡩࡦࡥࡨࠤࡴ࡬ࠠࡥࡣࡷࡥ࠳ࠦࠊࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠽ࡔࡦࡸࡡ࡮ࡧࡷࡩࡷࠦࡣࡪࡲ࡫ࡩࡷࡺࡥࡹࡶ࠽ࠤ࡙࡮ࡥࠡࡲ࡬ࡩࡨ࡫ࠠࡰࡨࠣࡨࡦࡺࡡࠡࡶࡲࠤࡩ࡫ࡣࡳࡻࡳࡸ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠻ࡖࡼࡴࡪࠦࡣࡪࡲ࡫ࡩࡷࡺࡥࡹࡶ࠽ࠤࡧࡿࡴࡦࠢࡶࡸࡷ࡯࡮ࡨ࠮ࠣࡰࡴࡴࡧࠡࡱࡵࠤࡦࠦ࠲࠮࡫ࡷࡩࡲࠦࡴࡶࡲ࡯ࡩࠥࡧࡳࠡࡴࡨࡸࡺࡸ࡮ࡦࡦࠣࡦࡾࠦࡠࡦࡰࡦࡶࡾࡶࡴࡡࠌࠍࠤࠥࠦࠠࠡࠢࠣࠤ࠿ࡘࡥࡵࡷࡵࡲ࠿ࠦࡁࠡࡤࡼࡸࡪࠦࡳࡵࡴ࡬ࡲ࡬ࠦࡩࡧࠢࡦ࡭ࡵ࡮ࡥࡳࡶࡨࡼࡹࠦࡷࡢࡵࠣࡥࠥࡨࡹࡵࡧࠣࡷࡹࡸࡩ࡯ࡩࠣࡳࡷࠦࡡࠡࡶࡸࡴࡱ࡫ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࡲࡪࠥࡨࡹࡵࡧࠣࡷࡹࡸࡩ࡯ࡩࡶ࠲ࠥࡇࠠ࡭ࡱࡱ࡫ࠥࡵࡴࡩࡧࡵࡻ࡮ࡹࡥ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨ঄")
        l11ll1l1l1_Krypto_=0
        if not isinstance(l1ll111l_Krypto_, tuple):
            l1ll111l_Krypto_=(l1ll111l_Krypto_,)
        if isinstance(l1ll111l_Krypto_[0], bytes):
            l1ll111l_Krypto_=tuple(map(l1ll111ll1_Krypto_, l1ll111l_Krypto_)) ; l11ll1l1l1_Krypto_=1
        l1ll11l1_Krypto_=self._1l111l111_Krypto_(l1ll111l_Krypto_)
        if l11ll1l1l1_Krypto_: return l1ll1lllll_Krypto_(l1ll11l1_Krypto_)
        else: return l1ll11l1_Krypto_
    def l1l11lll11_Krypto_(self, M, l1l111ll1l_Krypto_):
        l1l1111_Krypto_ (u"ࠣࠤࠥࡗ࡮࡭࡮ࠡࡣࠣࡴ࡮࡫ࡣࡦࠢࡲࡪࠥࡪࡡࡵࡣ࠱ࠎࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠺ࡑࡣࡵࡥࡲ࡫ࡴࡦࡴࠣࡑ࠿ࠦࡔࡩࡧࠣࡴ࡮࡫ࡣࡦࠢࡲࡪࠥࡪࡡࡵࡣࠣࡸࡴࠦࡥ࡯ࡥࡵࡽࡵࡺ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠽ࡘࡾࡶࡥࠡࡏ࠽ࠤࡧࡿࡴࡦࠢࡶࡸࡷ࡯࡮ࡨࠢࡲࡶࠥࡲ࡯࡯ࡩࠍࠎࠥࠦࠠࠡࠢࠣࠤࠥࡀࡐࡢࡴࡤࡱࡪࡺࡥࡳࠢࡎ࠾ࠥࡇࠠࡳࡣࡱࡨࡴࡳࠠࡱࡣࡵࡥࡲ࡫ࡴࡦࡴࠣࡶࡪࡷࡵࡪࡴࡨࡨࠥࡨࡹࠡࡵࡲࡱࡪࠦࡡ࡭ࡩࡲࡶ࡮ࡺࡨ࡮ࡵࠍࠤࠥࠦࠠࠡࠢࠣࠤ࠿࡚ࡹࡱࡧࠣࡏ࠿ࠦࡢࡺࡶࡨࠤࡸࡺࡲࡪࡰࡪࠤࡴࡸࠠ࡭ࡱࡱ࡫ࠏࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠻ࡔࡨࡸࡺࡸ࡮࠻ࠢࡄࠤࡹࡻࡰ࡭ࡧࠣࡻ࡮ࡺࡨࠡࡶࡺࡳࠥ࡯ࡴࡦ࡯ࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤঅ")
        if (not self.l1l1111l1l_Krypto_()):
            raise TypeError(l1l1111_Krypto_ (u"ࠩࡓࡶ࡮ࡼࡡࡵࡧࠣ࡯ࡪࡿࠠ࡯ࡱࡷࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠠࡪࡰࠣࡸ࡭࡯ࡳࠡࡱࡥ࡮ࡪࡩࡴࠨআ"))
        if isinstance(M, bytes): M=l1ll111ll1_Krypto_(M)
        if isinstance(l1l111ll1l_Krypto_, bytes): l1l111ll1l_Krypto_=l1ll111ll1_Krypto_(l1l111ll1l_Krypto_)
        return self._1l11l1l1l_Krypto_(M, l1l111ll1l_Krypto_)
    def l1l11l1l11_Krypto_ (self, M, signature):
        l1l1111_Krypto_ (u"ࠥࠦࠧ࡜ࡥࡳ࡫ࡩࡽࠥࡺࡨࡦࠢࡹࡥࡱ࡯ࡤࡪࡶࡼࠤࡴ࡬ࠠࡢࠢࡶ࡭࡬ࡴࡡࡵࡷࡵࡩ࠳ࠐࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠼ࡓࡥࡷࡧ࡭ࡦࡶࡨࡶࠥࡓ࠺ࠡࡖ࡫ࡩࠥ࡫ࡸࡱࡧࡦࡸࡪࡪࠠ࡮ࡧࡶࡷࡦ࡭ࡥ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣ࠾࡙ࡿࡰࡦࠢࡐ࠾ࠥࡨࡹࡵࡧࠣࡷࡹࡸࡩ࡯ࡩࠣࡳࡷࠦ࡬ࡰࡰࡪࠎࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠺ࡑࡣࡵࡥࡲ࡫ࡴࡦࡴࠣࡷ࡮࡭࡮ࡢࡶࡸࡶࡪࡀࠠࡕࡪࡨࠤࡸ࡯ࡧ࡯ࡣࡷࡹࡷ࡫ࠠࡵࡱࠣࡺࡪࡸࡩࡧࡻ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡀࡔࡺࡲࡨࠤࡸ࡯ࡧ࡯ࡣࡷࡹࡷ࡫࠺ࠡࡶࡸࡴࡱ࡫ࠠࡸ࡫ࡷ࡬ࠥࡺࡷࡰࠢ࡬ࡸࡪࡳࡳ࠭ࠢࡤࡷࠥࡸࡥࡵࡷࡵࡲࠥࡨࡹࠡࡢࡶ࡭࡬ࡴࡠࠋࠌࠣࠤࠥࠦࠠࠡࠢࠣ࠾ࡗ࡫ࡴࡶࡴࡱ࠾࡚ࠥࡲࡶࡧࠣ࡭࡫ࠦࡴࡩࡧࠣࡷ࡮࡭࡮ࡢࡶࡸࡶࡪࠦࡩࡴࠢࡦࡳࡷࡸࡥࡤࡶ࠯ࠤࡋࡧ࡬ࡴࡧࠣࡳࡹ࡮ࡥࡳࡹ࡬ࡷࡪ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦই")
        if isinstance(M, bytes): M=l1ll111ll1_Krypto_(M)
        return self._1l11111l1_Krypto_(M, signature)
    def validate (self, M, signature):
        l11ll1ll11_Krypto_.warn(l1l1111_Krypto_ (u"ࠦࡻࡧ࡬ࡪࡦࡤࡸࡪ࠮ࠩࠡ࡯ࡨࡸ࡭ࡵࡤࠡࡰࡤࡱࡪࠦࡩࡴࠢࡲࡦࡸࡵ࡬ࡦࡶࡨ࠿ࠥࡻࡳࡦࠢࡹࡩࡷ࡯ࡦࡺࠪࠬࠦঈ"),
                      DeprecationWarning)
    def l11lll1111_Krypto_(self, M, B):
        l1l1111_Krypto_ (u"ࠧࠨࠢࡃ࡮࡬ࡲࡩࠦࡡࠡ࡯ࡨࡷࡸࡧࡧࡦࠢࡷࡳࠥࡶࡲࡦࡸࡨࡲࡹࠦࡣࡦࡴࡷࡥ࡮ࡴࠠࡴ࡫ࡧࡩ࠲ࡩࡨࡢࡰࡱࡩࡱࠦࡡࡵࡶࡤࡧࡰࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣ࠾ࡕࡧࡲࡢ࡯ࡨࡸࡪࡸࠠࡎ࠼ࠣࡘ࡭࡫ࠠ࡮ࡧࡶࡷࡦ࡭ࡥࠡࡶࡲࠤࡧࡲࡩ࡯ࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡀࡔࡺࡲࡨࠤࡒࡀࠠࡣࡻࡷࡩࠥࡹࡴࡳ࡫ࡱ࡫ࠥࡵࡲࠡ࡮ࡲࡲ࡬ࠐࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠼ࡓࡥࡷࡧ࡭ࡦࡶࡨࡶࠥࡈ࠺ࠡࡄ࡯࡭ࡳࡪࡩ࡯ࡩࠣࡪࡦࡩࡴࡰࡴ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡀࡔࡺࡲࡨࠤࡇࡀࠠࡣࡻࡷࡩࠥࡹࡴࡳ࡫ࡱ࡫ࠥࡵࡲࠡ࡮ࡲࡲ࡬ࠐࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠼ࡕࡩࡹࡻࡲ࡯࠼ࠣࡅࠥࡨࡹࡵࡧࠣࡷࡹࡸࡩ࡯ࡩࠣ࡭࡫ࠦࡍࠡࡹࡤࡷࠥࡹ࡯࠯ࠢࡄࠤࡱࡵ࡮ࡨࠢࡲࡸ࡭࡫ࡲࡸ࡫ࡶࡩ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥউ")
        l11ll1l1l1_Krypto_=0
        if isinstance(M, bytes):
            M=l1ll111ll1_Krypto_(M) ; l11ll1l1l1_Krypto_=1
        if isinstance(B, bytes): B=l1ll111ll1_Krypto_(B)
        l11ll1lll1_Krypto_=self._1l1111111_Krypto_(M, B)
        if l11ll1l1l1_Krypto_: return l1ll1lllll_Krypto_(l11ll1lll1_Krypto_)
        else: return l11ll1lll1_Krypto_
    def l11ll1ll1l_Krypto_(self, M, B):
        l1l1111_Krypto_ (u"ࠨࠢࠣࡗࡱࡦࡱ࡯࡮ࡥࠢࡤࠤࡲ࡫ࡳࡴࡣࡪࡩࠥࡧࡦࡵࡧࡵࠤࡨࡸࡹࡱࡶࡲ࡫ࡷࡧࡰࡩ࡫ࡦࠤࡵࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠎࠥࠦࠠࠡࠢࠣࠤࠥࡀࡐࡢࡴࡤࡱࡪࡺࡥࡳࠢࡐ࠾࡚ࠥࡨࡦࠢࡨࡲࡨࡵࡤࡦࡦࠣࡱࡪࡹࡳࡢࡩࡨࠤࡹࡵࠠࡶࡰࡥࡰ࡮ࡴࡤ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣ࠾࡙ࡿࡰࡦࠢࡐ࠾ࠥࡨࡹࡵࡧࠣࡷࡹࡸࡩ࡯ࡩࠣࡳࡷࠦ࡬ࡰࡰࡪࠎࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠺ࡑࡣࡵࡥࡲ࡫ࡴࡦࡴࠣࡆ࠿ࠦࡂ࡭࡫ࡱࡨ࡮ࡴࡧࠡࡨࡤࡧࡹࡵࡲ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣ࠾࡙ࡿࡰࡦࠢࡅ࠾ࠥࡨࡹࡵࡧࠣࡷࡹࡸࡩ࡯ࡩࠣࡳࡷࠦ࡬ࡰࡰࡪࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣঊ")
        l11ll1l1l1_Krypto_=0
        if isinstance(M, bytes):
            M=l1ll111ll1_Krypto_(M) ; l11ll1l1l1_Krypto_=1
        if isinstance(B, bytes): B=l1ll111ll1_Krypto_(B)
        l11ll1llll_Krypto_=self._1l11lll1l_Krypto_(M, B)
        if l11ll1l1l1_Krypto_: return l1ll1lllll_Krypto_(l11ll1llll_Krypto_)
        else: return l11ll1llll_Krypto_
    def l1l11ll1l1_Krypto_ (self):
        l1l1111_Krypto_ (u"ࠢࠣࠤࡗࡩࡱࡲࠠࡪࡨࠣࡸ࡭࡫ࠠࡢ࡮ࡪࡳࡷ࡯ࡴࡩ࡯ࠣࡧࡦࡴࠠࡥࡧࡤࡰࠥࡽࡩࡵࡪࠣࡧࡷࡿࡰࡵࡱࡪࡶࡦࡶࡨࡪࡥࠣࡷ࡮࡭࡮ࡢࡶࡸࡶࡪࡹ࠮ࠋࠌࠣࠤࠥࠦࠠࠡࠢࠣࡘ࡭࡯ࡳࠡࡲࡵࡳࡵ࡫ࡲࡵࡻࠣࡧࡴࡴࡣࡦࡴࡱࡷࠥࡺࡨࡦࠢ࠭ࡥࡱ࡭࡯ࡳ࡫ࡷ࡬ࡲ࠰ࠬࠡࡰࡲࡸࠥࡺࡨࡦࠢ࡮ࡩࡾࠦࡩࡵࡵࡨࡰ࡫࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡋࡷࠤࡲࡧࡹࠡࡪࡤࡴࡵ࡫࡮ࠡࡶ࡫ࡥࡹࠦࡴࡩ࡫ࡶࠤࡵࡧࡲࡵ࡫ࡦࡹࡱࡧࡲࠡ࡭ࡨࡽࠥࡵࡢ࡫ࡧࡦࡸࠥ࡮ࡡࡴࡰࠪࡸࠥ࡭࡯ࡵࠌࠣࠤࠥࠦࠠࠡࠢࠣࡸ࡭࡫ࠠࡱࡴ࡬ࡺࡦࡺࡥࠡ࡫ࡱࡪࡴࡸ࡭ࡢࡶ࡬ࡳࡳࠦࡲࡦࡳࡸ࡭ࡷ࡫ࡤࠡࡶࡲࠤ࡬࡫࡮ࡦࡴࡤࡸࡪࠦࡡࠡࡵ࡬࡫ࡳࡧࡴࡶࡴࡨ࠲ࠏࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠻ࡔࡨࡸࡺࡸ࡮࠻ࠢࡥࡳࡴࡲࡥࡢࡰࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢঋ")
        return 1
    def l1l1111l11_Krypto_ (self):
        l1l1111_Krypto_ (u"ࠣࠤࠥࡘࡪࡲ࡬ࠡ࡫ࡩࠤࡹ࡮ࡥࠡࡣ࡯࡫ࡴࡸࡩࡵࡪࡰࠤࡨࡧ࡮ࠡࡦࡨࡥࡱࠦࡷࡪࡶ࡫ࠤࡩࡧࡴࡢࠢࡨࡲࡨࡸࡹࡱࡶ࡬ࡳࡳ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢࡗ࡬࡮ࡹࠠࡱࡴࡲࡴࡪࡸࡴࡺࠢࡦࡳࡳࡩࡥࡳࡰࡶࠤࡹ࡮ࡥࠡࠬࡤࡰ࡬ࡵࡲࡪࡶ࡫ࡱ࠯࠲ࠠ࡯ࡱࡷࠤࡹ࡮ࡥࠡ࡭ࡨࡽࠥ࡯ࡴࡴࡧ࡯ࡪ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡊࡶࠣࡱࡦࡿࠠࡩࡣࡳࡴࡪࡴࠠࡵࡪࡤࡸࠥࡺࡨࡪࡵࠣࡴࡦࡸࡴࡪࡥࡸࡰࡦࡸࠠ࡬ࡧࡼࠤࡴࡨࡪࡦࡥࡷࠤ࡭ࡧࡳ࡯ࠩࡷࠤ࡬ࡵࡴࠋࠢࠣࠤࠥࠦࠠࠡࠢࡷ࡬ࡪࠦࡰࡳ࡫ࡹࡥࡹ࡫ࠠࡪࡰࡩࡳࡷࡳࡡࡵ࡫ࡲࡲࠥࡸࡥࡲࡷ࡬ࡶࡪࡪࠠࡵࡱࠣࡨࡪࡩࡲࡺࡲࡷࠤࡩࡧࡴࡢ࠰ࠍࠎࠥࠦࠠࠡࠢࠣࠤࠥࡀࡒࡦࡶࡸࡶࡳࡀࠠࡣࡱࡲࡰࡪࡧ࡮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧঌ")
        return 1
    def l1l1111ll1_Krypto_ (self):
        l1l1111_Krypto_ (u"ࠤ࡙ࠥࠦ࡫࡬࡭ࠢ࡬ࡪࠥࡺࡨࡦࠢࡤࡰ࡬ࡵࡲࡪࡶ࡫ࡱࠥࡩࡡ࡯ࠢࡧࡩࡦࡲࠠࡸ࡫ࡷ࡬ࠥࡪࡡࡵࡣࠣࡦࡱ࡯࡮ࡥ࡫ࡱ࡫࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࡖ࡫࡭ࡸࠦࡰࡳࡱࡳࡩࡷࡺࡹࠡࡥࡲࡲࡨ࡫ࡲ࡯ࡵࠣࡸ࡭࡫ࠠࠫࡣ࡯࡫ࡴࡸࡩࡵࡪࡰ࠮࠱ࠦ࡮ࡰࡶࠣࡸ࡭࡫ࠠ࡬ࡧࡼࠤ࡮ࡺࡳࡦ࡮ࡩ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡉࡵࠢࡰࡥࡾࠦࡨࡢࡲࡳࡩࡳࠦࡴࡩࡣࡷࠤࡹ࡮ࡩࡴࠢࡳࡥࡷࡺࡩࡤࡷ࡯ࡥࡷࠦ࡫ࡦࡻࠣࡳࡧࡰࡥࡤࡶࠣ࡬ࡦࡹ࡮ࠨࡶࠣ࡫ࡴࡺࠊࠡࠢࠣࠤࠥࠦࠠࠡࡶ࡫ࡩࠥࡶࡲࡪࡸࡤࡸࡪࠦࡩ࡯ࡨࡲࡶࡲࡧࡴࡪࡱࡱࠤࡷ࡫ࡱࡶ࡫ࡵࡩࡩࠦࡣࡢࡴࡵࡽࠥࡵࡵࡵࠢࡥࡰ࡮ࡴࡤࡪࡰࡪ࠲ࠏࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠻ࡔࡨࡸࡺࡸ࡮࠻ࠢࡥࡳࡴࡲࡥࡢࡰࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢ঍")
        return 0
    def size (self):
        l1l1111_Krypto_ (u"࡚ࠥࠦࠧࡥ࡭࡮ࠣࡸ࡭࡫ࠠ࡮ࡣࡻ࡭ࡲࡻ࡭ࠡࡰࡸࡱࡧ࡫ࡲࠡࡱࡩࠤࡧ࡯ࡴࡴࠢࡷ࡬ࡦࡺࠠࡤࡣࡱࠤࡧ࡫ࠠࡩࡣࡱࡨࡱ࡫ࡤࠡࡤࡼࠤࡹ࡮ࡩࡴࠢ࡮ࡩࡾ࠴ࠊࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠽ࡖࡪࡺࡵࡳࡰ࠽ࠤ࡮ࡴࡴࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧ঎")
        return 0
    def l1l1111l1l_Krypto_ (self):
        l1l1111_Krypto_ (u"ࠦࠧࠨࡔࡦ࡮࡯ࠤ࡮࡬ࠠࡵࡪࡨࠤࡰ࡫ࡹࠡࡱࡥ࡮ࡪࡩࡴࠡࡥࡲࡲࡹࡧࡩ࡯ࡵࠣࡴࡷ࡯ࡶࡢࡶࡨࠤࡨࡵ࡭ࡱࡱࡱࡩࡳࡺࡳ࠯ࠌࠍࠤࠥࠦࠠࠡࠢࠣࠤ࠿ࡘࡥࡵࡷࡵࡲ࠿ࠦࡢࡰࡱ࡯ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣএ")
        return 0
    def l1l11l111l_Krypto_ (self):
        l1l1111_Krypto_ (u"ࠧࠨࠢࡄࡱࡱࡷࡹࡸࡵࡤࡶࠣࡥࠥࡴࡥࡸࠢ࡮ࡩࡾࠦࡣࡢࡴࡵࡽ࡮ࡴࡧࠡࡱࡱࡰࡾࠦࡴࡩࡧࠣࡴࡺࡨ࡬ࡪࡥࠣ࡭ࡳ࡬࡯ࡳ࡯ࡤࡸ࡮ࡵ࡮࠯ࠌࠍࠤࠥࠦࠠࠡࠢࠣࠤ࠿ࡘࡥࡵࡷࡵࡲ࠿ࠦࡁࠡࡰࡨࡻࠥࡦࡰࡶࡤ࡮ࡩࡾࡦࠠࡰࡤ࡭ࡩࡨࡺ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧঐ")
        return self
    def __eq__ (self, other):
        l1l1111_Krypto_ (u"ࠨࠢࠣࡡࡢࡩࡶࡥ࡟ࠩࡱࡷ࡬ࡪࡸࠩ࠻ࠢ࠳࠰ࠥ࠷ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡅࡲࡱࡵࡧࡲࡦࠢࡸࡷࠥࡺ࡯ࠡࡱࡷ࡬ࡪࡸࠠࡧࡱࡵࠤࡪࡷࡵࡢ࡮࡬ࡸࡾ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦ঑")
        return self.__getstate__() == other.__getstate__()
    def __ne__ (self, other):
        l1l1111_Krypto_ (u"ࠢࠣࠤࡢࡣࡳ࡫࡟ࡠࠪࡲࡸ࡭࡫ࡲࠪ࠼ࠣ࠴࠱ࠦ࠱ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡆࡳࡲࡶࡡࡳࡧࠣࡹࡸࠦࡴࡰࠢࡲࡸ࡭࡫ࡲࠡࡨࡲࡶࠥ࡯࡮ࡦࡳࡸࡥࡱ࡯ࡴࡺ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢ঒")
        return not self.__eq__(other)