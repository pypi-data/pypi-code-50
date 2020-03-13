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
__revision__ = l1l1111_Krypto_ (u"ࠧࠪࡉࡥࠦࠥ৤")
from l111ll1_Krypto_.l11l11l1_Krypto_.l1l111lll1_Krypto_ import *
from l111ll1_Krypto_.l1l111ll_Krypto_ import l111l1ll_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l111l1ll_Krypto_ import l1ll111ll1_Krypto_, l1ll1lllll_Krypto_
from l111ll1_Krypto_.l1lll1ll1_Krypto_ import l1l111lll_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
class error (Exception):
    pass
def l111lll11l_Krypto_(l1l11ll1ll_Krypto_):
    S=l1l11ll1ll_Krypto_(20)
    l111lllll1_Krypto_=l1l111lll_Krypto_.new(S).digest()
    l111lll1l1_Krypto_=l1l111lll_Krypto_.new(l1ll1lllll_Krypto_(l1ll111ll1_Krypto_(S)+1)).digest()
    q = l11lllll11_Krypto_(0)
    for i in range(0,20):
        c=l1lllllll1_Krypto_(l111lllll1_Krypto_[i])^l1lllllll1_Krypto_(l111lll1l1_Krypto_[i])
        if i==0:
            c=c | 128
        if i==19:
            c= c | 1
        q=q*256+c
    while (not l11lll1l1l_Krypto_(q)):
        q=q+2
    if pow(2,159) < q < pow(2,160):
        return S, q
    raise RuntimeError(l1l1111_Krypto_ (u"࠭ࡂࡢࡦࠣࡵࠥࡼࡡ࡭ࡷࡨࠤ࡬࡫࡮ࡦࡴࡤࡸࡪࡪࠧ৥"))
def l1l11l1111_Krypto_(bits, l1l11ll1ll_Krypto_, l1l1111lll_Krypto_=None):
    l1l1111_Krypto_ (u"ࠢࠣࠤࡪࡩࡳ࡫ࡲࡢࡶࡨࠬࡧ࡯ࡴࡴ࠼࡬ࡲࡹ࠲ࠠࡳࡣࡱࡨ࡫ࡻ࡮ࡤ࠼ࡦࡥࡱࡲࡡࡣ࡮ࡨ࠰ࠥࡶࡲࡰࡩࡵࡩࡸࡹ࡟ࡧࡷࡱࡧ࠿ࡩࡡ࡭࡮ࡤࡦࡱ࡫ࠩࠋࠌࠣࠤࠥࠦࡇࡦࡰࡨࡶࡦࡺࡥࠡࡣࠣࡈࡘࡇࠠ࡬ࡧࡼࠤࡴ࡬ࠠ࡭ࡧࡱ࡫ࡹ࡮ࠠࠨࡤ࡬ࡸࡸ࠭ࠬࠡࡷࡶ࡭ࡳ࡭ࠠࠨࡴࡤࡲࡩ࡬ࡵ࡯ࡥࠪࠤࡹࡵࠠࡨࡧࡷࠎࠥࠦࠠࠡࡴࡤࡲࡩࡵ࡭ࠡࡦࡤࡸࡦࠦࡡ࡯ࡦࠣࠫࡵࡸ࡯ࡨࡴࡨࡷࡸࡥࡦࡶࡰࡦࠫ࠱ࠦࡩࡧࠢࡳࡶࡪࡹࡥ࡯ࡶ࠯ࠤࡹࡵࠠࡥ࡫ࡶࡴࡱࡧࡹࠋࠢࠣࠤࠥࡺࡨࡦࠢࡳࡶࡴ࡭ࡲࡦࡵࡶࠤࡴ࡬ࠠࡵࡪࡨࠤࡰ࡫ࡹࠡࡩࡨࡲࡪࡸࡡࡵ࡫ࡲࡲ࠳ࠐࠠࠡࠢࠣࠦࠧࠨ০")
    if bits<160:
        raise ValueError(l1l1111_Krypto_ (u"ࠨࡍࡨࡽࠥࡲࡥ࡯ࡩࡷ࡬ࠥࡂࠠ࠲࠸࠳ࠤࡧ࡯ࡴࡴࠩ১"))
    obj=l11l11111l_Krypto_()
    if l1l1111lll_Krypto_:
        l1l1111lll_Krypto_(l1l1111_Krypto_ (u"ࠩࡳ࠰ࡶࡢ࡮ࠨ২"))
    while (1):
        S, obj.q = l111lll11l_Krypto_(l1l11ll1ll_Krypto_)
        n=divmod(bits-1, 160)[0]
        C, l11l1111l1_Krypto_, l11l111111_Krypto_ = 0, 2, {}
        b=(obj.q >> 5) & 15
        l111lll1ll_Krypto_=pow(l11lllll11_Krypto_(2), b)
        l111llllll_Krypto_=pow(l11lllll11_Krypto_(2), bits-1)
        while C<4096:
            for k in range(0, n+1):
                l11l111111_Krypto_[k]=l1ll111ll1_Krypto_(l1l111lll_Krypto_.new(S+l11l1111ll_Krypto_(l11l1111l1_Krypto_)+l11l1111ll_Krypto_(k)).digest())
            l111llll1l_Krypto_=l11l111111_Krypto_[n] % l111lll1ll_Krypto_
            for k in range(n-1, -1, -1):
                l111llll1l_Krypto_=(l111llll1l_Krypto_<<160)+l11l111111_Krypto_[k]
            X=l111llll1l_Krypto_+l111llllll_Krypto_
            p=X-(X%(2*obj.q)-1)
            if l111llllll_Krypto_<=p and l11lll1l1l_Krypto_(p):
                break
            C, l11l1111l1_Krypto_ = C+1, l11l1111l1_Krypto_+n+1
        if C<4096:
            break
        if l1l1111lll_Krypto_:
            l1l1111lll_Krypto_(l1l1111_Krypto_ (u"ࠪ࠸࠵࠿࠶ࠡ࡯ࡸࡰࡹ࡯ࡰ࡭ࡧࡶࠤ࡫ࡧࡩ࡭ࡧࡧࡠࡳ࠭৩"))
    obj.p = p
    l111llll11_Krypto_=divmod(p-1, obj.q)[0]
    if l1l1111lll_Krypto_:
        l1l1111lll_Krypto_(l1l1111_Krypto_ (u"ࠫ࡭࠲ࡧ࡝ࡰࠪ৪"))
    while (1):
        h=l1ll111ll1_Krypto_(l1l11ll1ll_Krypto_(bits)) % (p-1)
        g=pow(h, l111llll11_Krypto_, p)
        if 1<h<p-1 and g>1:
            break
    obj.g=g
    if l1l1111lll_Krypto_:
        l1l1111lll_Krypto_(l1l1111_Krypto_ (u"ࠬࡾࠬࡺ࡞ࡱࠫ৫"))
    while (1):
        x=l1ll111ll1_Krypto_(l1l11ll1ll_Krypto_(20))
        if 0 < x < obj.q:
            break
    obj.x, obj.y = x, pow(g, x, p)
    return obj
class l11l11111l_Krypto_:
    pass