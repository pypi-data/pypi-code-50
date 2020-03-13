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
l1l1111_Krypto_ (u"ࠦࠧࠨࡃࡰ࡯ࡳࡥࡹ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡣࡰࡦࡨࠤ࡫ࡵࡲࠡࡪࡤࡲࡩࡲࡩ࡯ࡩࠣࡷࡹࡸࡩ࡯ࡩ࠲ࡦࡾࡺࡥࡴࠢࡦ࡬ࡦࡴࡧࡦࡵࠣࡪࡷࡵ࡭ࠡࡒࡼࡸ࡭ࡵ࡮ࠡ࠴࠱ࡼࠥࡺ࡯ࠡࡒࡼ࠷ࡰࠐࠊࡊࡰࠣࡔࡾࡺࡨࡰࡰࠣ࠶࠳ࡾࠬࠡࡵࡷࡶ࡮ࡴࡧࡴࠢࠫࡳ࡫ࠦࡴࡺࡲࡨࠤࠬ࠭ࡳࡵࡴࠪࠫ࠮ࠦࡣࡰࡰࡷࡥ࡮ࡴࠠࡣ࡫ࡱࡥࡷࡿࠠࡥࡣࡷࡥ࠱ࠦࡩ࡯ࡥ࡯ࡹࡩ࡯࡮ࡨࠢࡨࡲࡨࡵࡤࡦࡦࠍ࡙ࡳ࡯ࡣࡰࡦࡨࠤࡹ࡫ࡸࡵࠢࠫࡩ࠳࡭࠮ࠡࡗࡗࡊ࠲࠾ࠩ࠯ࠢࠣࡘ࡭࡫ࠠࡴࡧࡳࡥࡷࡧࡴࡦࠢࡷࡽࡵ࡫ࠠࠨࠩࡸࡲ࡮ࡩ࡯ࡥࡧࠪࠫࠥ࡮࡯࡭ࡦࡶࠤ࡚ࡴࡩࡤࡱࡧࡩࠥࡺࡥࡹࡶ࠱ࠎ࡚ࡴࡩࡤࡱࡧࡩࠥࡲࡩࡵࡧࡵࡥࡱࡹࠠࡢࡴࡨࠤࡸࡶࡥࡤ࡫ࡩ࡭ࡪࡪࠠࡷ࡫ࡤࠤࡹ࡮ࡥࠡࡷࠪ࠲࠳࠴ࠧࠡࡲࡵࡩ࡫࡯ࡸ࠯ࠢࠣࡍࡳࡪࡥࡹ࡫ࡱ࡫ࠥࡵࡲࠡࡵ࡯࡭ࡨ࡯࡮ࡨࠌࡨ࡭ࡹ࡮ࡥࡳࠢࡷࡽࡵ࡫ࠠࡢ࡮ࡺࡥࡾࡹࠠࡱࡴࡲࡨࡺࡩࡥࡴࠢࡤࠤࡸࡺࡲࡪࡰࡪࠤࡴ࡬ࠠࡵࡪࡨࠤࡸࡧ࡭ࡦࠢࡷࡽࡵ࡫ࠠࡢࡵࠣࡸ࡭࡫ࠠࡰࡴ࡬࡫࡮ࡴࡡ࡭࠰ࠍࡈࡦࡺࡡࠡࡴࡨࡥࡩࠦࡦࡳࡱࡰࠤࡦࠦࡦࡪ࡮ࡨࠤ࡮ࡹࠠࡢ࡮ࡺࡥࡾࡹࠠࡰࡨࠣࠫࠬ࠭ࡳࡵࡴࠪࠫࠥࡺࡹࡱࡧ࠱ࠎࠏࡏ࡮ࠡࡒࡼࡸ࡭ࡵ࡮ࠡ࠵࠱ࡼ࠱ࠦࡳࡵࡴ࡬ࡲ࡬ࡹࠠࠩࡶࡼࡴࡪࠦࠧࠨࡵࡷࡶࠬ࠭ࠩࠡ࡯ࡤࡽࠥࡵ࡮࡭ࡻࠣࡧࡴࡴࡴࡢ࡫ࡱࠤ࡚ࡴࡩࡤࡱࡧࡩࠥࡺࡥࡹࡶ࠱ࠤ࡙࡮ࡥࠡࡷࠪ࠲࠳࠴ࠧࠋࡲࡵࡩ࡫࡯ࡸࠡࡣࡱࡨࠥࡺࡨࡦࠢࠪࠫࡺࡴࡩࡤࡱࡧࡩࠬ࠭ࠠࡵࡻࡳࡩࠥࡧࡲࡦࠢࡱࡳࡼࠦࡲࡦࡦࡸࡲࡩࡧ࡮ࡵ࠰ࠣࠤࡆࠦ࡮ࡦࡹࠣࡸࡾࡶࡥࠡࠪࡦࡥࡱࡲࡥࡥࠌࠪࠫࡧࡿࡴࡦࡵࠪࠫ࠮ࠦࡨࡢࡵࠣࡸࡴࠦࡢࡦࠢࡸࡷࡪࡪࠠࡧࡱࡵࠤࡧ࡯࡮ࡢࡴࡼࠤࡩࡧࡴࡢࠢࠫ࡭ࡳࡩ࡬ࡶࡦ࡬ࡲ࡬ࠦࡡ࡯ࡻࠣࡴࡦࡸࡴࡪࡥࡸࡰࡦࡸࠊࠨࠩࡨࡲࡨࡵࡤࡪࡰࡪࠫࠬࠦ࡯ࡧࠢࡤࠤࡸࡺࡲࡪࡰࡪ࠭࠳ࠦࠠࡕࡪࡨࠤࡧ࠭࠮࠯࠰ࠪࠤࡵࡸࡥࡧ࡫ࡻࠤࡦࡲ࡬ࡰࡹࡶࠤࡴࡴࡥࠡࡶࡲࠤࡸࡶࡥࡤ࡫ࡩࡽࠥࡧࠠࡣ࡫ࡱࡥࡷࡿࠊ࡭࡫ࡷࡩࡷࡧ࡬࠯ࠢࠣࡍࡳࡪࡥࡹ࡫ࡱ࡫ࠥࡵࡲࠡࡵ࡯࡭ࡨ࡯࡮ࡨࠢࡤࠤࡸࡺࡲࡪࡰࡪࠤࡵࡸ࡯ࡥࡷࡦࡩࡸࠦࡡ࡯ࡱࡷ࡬ࡪࡸࠠࡴࡶࡵ࡭ࡳ࡭࠮ࠡࠢࡖࡰ࡮ࡩࡩ࡯ࡩࠣࡥࠥࡨࡹࡵࡧࠍࡷࡹࡸࡩ࡯ࡩࠣࡴࡷࡵࡤࡶࡥࡨࡷࠥࡧ࡮ࡰࡶ࡫ࡩࡷࠦࡢࡺࡶࡨࠤࡸࡺࡲࡪࡰࡪ࠰ࠥࡨࡵࡵࠢࡷ࡬ࡪࠦࡩ࡯ࡦࡨࡼ࡮ࡴࡧࠡࡱࡳࡩࡷࡧࡴࡪࡱࡱࠤࡵࡸ࡯ࡥࡷࡦࡩࡸࠦࡡ࡯ࠌ࡬ࡲࡹ࡫ࡧࡦࡴ࠱ࠤࠥࡊࡡࡵࡣࠣࡶࡪࡧࡤࠡࡨࡵࡳࡲࠦࡡࠡࡨ࡬ࡰࡪࠦࡩࡴࠢࡲࡪࠥ࠭ࠧࠨࡵࡷࡶࠬ࠭ࠠࡵࡻࡳࡩࠥ࡯ࡦࠡࡶ࡫ࡩࠥ࡬ࡩ࡭ࡧࠣࡻࡦࡹࠠࡰࡲࡨࡲࡪࡪࠠࡪࡰࠍࡸࡪࡾࡴࠡ࡯ࡲࡨࡪ࠲ࠠࡰࡴࠣࡳ࡫ࠦࠧࠨࡤࡼࡸࡪࡹࠧࠨࠢࡷࡽࡵ࡫ࠠࡰࡶ࡫ࡩࡷࡽࡩࡴࡧ࠱ࠎࠏ࡙ࡩ࡯ࡥࡨࠤࡕࡿࡃࡳࡻࡳࡸࡴࠦࡡࡪ࡯ࡶࠤࡦࡺࠠࡴࡷࡳࡴࡴࡸࡴࡪࡰࡪࠤࡧࡵࡴࡩࠢࡓࡽࡹ࡮࡯࡯ࠢ࠵࠲ࡽࠦࡡ࡯ࡦࠣ࠷࠳ࡾࠬࠡࡶ࡫ࡩࠥ࡬࡯࡭࡮ࡲࡻ࡮ࡴࡧࠡࡪࡨࡰࡵ࡫ࡲࠋࡨࡸࡲࡨࡺࡩࡰࡰࡶࠤࡦࡸࡥࠡࡷࡶࡩࡩࠦࡴࡰࠢ࡮ࡩࡪࡶࠠࡵࡪࡨࠤࡷ࡫ࡳࡵࠢࡲࡪࠥࡺࡨࡦࠢ࡯࡭ࡧࡸࡡࡳࡻࠣࡥࡸࠦࡩ࡯ࡦࡨࡴࡪࡴࡤࡦࡰࡷࠤࡦࡹࠠࡱࡱࡶࡷ࡮ࡨ࡬ࡦࠌࡩࡶࡴࡳࠠࡵࡪࡨࠤࡦࡩࡴࡶࡣ࡯ࠤࡕࡿࡴࡩࡱࡱࠤࡻ࡫ࡲࡴ࡫ࡲࡲ࠳ࠐࠊࡊࡰࠣ࡫ࡪࡴࡥࡳࡣ࡯࠰ࠥࡺࡨࡦࠢࡦࡳࡩ࡫ࠠࡴࡪࡲࡹࡱࡪࠠࡢ࡮ࡺࡥࡾࡹࠠࡥࡧࡤࡰࠥࡽࡩࡵࡪࠣࡦ࡮ࡴࡡࡳࡻࠣࡷࡹࡸࡩ࡯ࡩࡶ࠰ࠥࡧ࡮ࡥࠢࡸࡷࡪࠦࡩ࡯ࡶࡨ࡫ࡪࡸࡳࠋ࡫ࡱࡷࡹ࡫ࡡࡥࠢࡲࡪࠥ࠷࠭ࡣࡻࡷࡩࠥࡩࡨࡢࡴࡤࡧࡹ࡫ࡲࠡࡵࡷࡶ࡮ࡴࡧࡴ࠰ࠍࠎࡧ࠮ࡳࠪࠌࠣࠤࠥࠦࡔࡢ࡭ࡨࠤࡦࠦࡴࡦࡺࡷࠤࡸࡺࡲࡪࡰࡪࠤࡱ࡯ࡴࡦࡴࡤࡰࠥ࠮ࡷࡪࡶ࡫ࠤࡳࡵࠠࡱࡴࡨࡪ࡮ࡾࠠࡰࡴࠣࡻ࡮ࡺࡨࠡࡷࠪ࠲࠳࠴ࠧࠡࡲࡵࡩ࡫࡯ࡸࠪࠢࡤࡲࡩࠐࠠࠡࠢࠣࡱࡦࡱࡥࠡࡣࠣࡦࡾࡺࡥࠡࡵࡷࡶ࡮ࡴࡧ࠯ࠌࡥࡧ࡭ࡸࠨࡤࠫࠍࠤࠥࠦࠠࡕࡣ࡮ࡩࠥࡧ࡮ࠡ࡫ࡱࡸࡪ࡭ࡥࡳࠢࡤࡲࡩࠦ࡭ࡢ࡭ࡨࠤࡦࠦ࠱࠮ࡥ࡫ࡥࡷࡧࡣࡵࡧࡵࠤࡧࡿࡴࡦࠢࡶࡸࡷ࡯࡮ࡨ࠰ࠍࡦࡴࡸࡤࠩࡥࠬࠎࠥࠦࠠࠡࡖࡤ࡯ࡪࠦࡴࡩࡧࠣࡶࡪࡹࡵ࡭ࡶࠣࡳ࡫ࠦࡩ࡯ࡦࡨࡼ࡮ࡴࡧࠡࡱࡱࠤࡦࠦࡢࡺࡶࡨࠤࡸࡺࡲࡪࡰࡪࠤࡦࡴࡤࠡ࡯ࡤ࡯ࡪࠦࡡ࡯ࠢ࡬ࡲࡹ࡫ࡧࡦࡴ࠱ࠎࡹࡵࡢࡺࡶࡨࡷ࠭ࡹࠩࠋࠢࠣࠤ࡚ࠥࡡ࡬ࡧࠣࡥࠥࡺࡥࡹࡶࠣࡷࡹࡸࡩ࡯ࡩ࠯ࠤࡦࠦࡢࡺࡶࡨࠤࡸࡺࡲࡪࡰࡪ࠰ࠥࡵࡲࠡࡣࠣࡷࡪࡷࡵࡦࡰࡦࡩࠥࡵࡦࠡࡥ࡫ࡥࡷࡧࡣࡵࡧࡵࠤࡹࡧ࡫ࡦࡰࠣࡪࡷࡵ࡭ࠋࠢࠣࠤࠥࡧࠠࡣࡻࡷࡩࠥࡹࡴࡳ࡫ࡱ࡫ࠥࡧ࡮ࡥࠢࡰࡥࡰ࡫ࠠࡢࠢࡥࡽࡹ࡫ࠠࡴࡶࡵ࡭ࡳ࡭࠮ࠋࠤࠥࠦ᪊")
__revision__ = l1l1111_Krypto_ (u"ࠧࠪࡉࡥࠦࠥ᪋")
import sys as l1l11l11_Krypto_
if l1l11l11_Krypto_.version_info[0] == 2:
    def b(s):
        return s
    def l11111l11_Krypto_(s):
        return chr(s)
    def l11l1111ll_Krypto_(s):
        return str(s)
    def l1lllllll1_Krypto_(s):
        return ord(s)
    if l1l11l11_Krypto_.version_info[1] == 1:
        def tobytes(s):
            try:
                return s.encode(l1l1111_Krypto_ (u"࠭࡬ࡢࡶ࡬ࡲ࠲࠷ࠧ᪌"))
            except:
                return l1l1111_Krypto_ (u"ࠧࠨ᪍").join(s)
    else:
        def tobytes(s):
            if isinstance(s, str):
                return s.encode(l1l1111_Krypto_ (u"ࠣ࡮ࡤࡸ࡮ࡴ࠭࠲ࠤ᪎"))
            else:
                return l1l1111_Krypto_ (u"ࠩࠪ᪏").join(s)
else:
    def b(s):
       return s.encode(l1l1111_Krypto_ (u"ࠥࡰࡦࡺࡩ࡯࠯࠴ࠦ᪐"))
    def l11111l11_Krypto_(s):
        return bytes([s])
    def l11l1111ll_Krypto_(s):
        if isinstance(s,str):
            return bytes(s,l1l1111_Krypto_ (u"ࠦࡱࡧࡴࡪࡰ࠰࠵ࠧ᪑"))
        else:
            return bytes(s)
    def l1lllllll1_Krypto_(s):
        return s
    def tobytes(s):
        if isinstance(s,bytes):
            return s
        else:
            if isinstance(s,str):
                return s.encode(l1l1111_Krypto_ (u"ࠧࡲࡡࡵ࡫ࡱ࠱࠶ࠨ᪒"))
            else:
                return bytes(s)