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
l1l1111_Krypto_ (u"ࠨࠢࠣࡒࡸࡶࡪࠦࡐࡺࡶ࡫ࡳࡳࠦࡩ࡮ࡲ࡯ࡩࡲ࡫࡮ࡵࡣࡷ࡭ࡴࡴࠠࡰࡨࠣࡸ࡭࡫ࠠࡓࡕࡄ࠱ࡷ࡫࡬ࡢࡶࡨࡨࠥࡶ࡯ࡳࡶ࡬ࡳࡳࡹࠠࡰࡨࠣࡇࡷࡿࡰࡵࡱ࠱ࡔࡺࡨ࡬ࡪࡥࡎࡩࡾ࠴࡟ࡧࡣࡶࡸࡲࡧࡴࡩ࠰ࠥࠦࠧ৳")
__revision__ = l1l1111_Krypto_ (u"ࠢࠥࡋࡧࠨࠧ৴")
__all__ = [l1l1111_Krypto_ (u"ࠨࡴࡶࡥࡤࡩ࡯࡯ࡵࡷࡶࡺࡩࡴࠨ৵")]
import sys as l1l11l11_Krypto_
if l1l11l11_Krypto_.version_info[0] == 2 and l1l11l11_Krypto_.version_info[1] == 1:
    from l111ll1_Krypto_.l1l111ll_Krypto_.l1l1ll1l_Krypto_ import *
from l111ll1_Krypto_.l1l111ll_Krypto_.l111l1ll_Krypto_ import size, l11llll1ll_Krypto_, l11llllll1_Krypto_
class error(Exception):
    pass
class _111l1lll1_Krypto_(object):
    def _1l1111111_Krypto_(self, m, r):
        return m * pow(r, self.e, self.n)
    def _1l11lll1l_Krypto_(self, m, r):
        return l11llll1ll_Krypto_(r, self.n) * m % self.n
    def _1l111l111_Krypto_(self, c):
        if not self.l1l1111l1l_Krypto_():
            raise TypeError(l1l1111_Krypto_ (u"ࠤࡑࡳࠥࡶࡲࡪࡸࡤࡸࡪࠦ࡫ࡦࡻࠥ৶"))
        if (hasattr(self,l1l1111_Krypto_ (u"ࠪࡴࠬ৷")) and hasattr(self,l1l1111_Krypto_ (u"ࠫࡶ࠭৸")) and hasattr(self,l1l1111_Krypto_ (u"ࠬࡻࠧ৹"))):
            l111ll1111_Krypto_ = pow(c, self.d % (self.p-1), self.p)
            l111l1ll1l_Krypto_ = pow(c, self.d % (self.q-1), self.q)
            h = l111l1ll1l_Krypto_ - l111ll1111_Krypto_
            if (h<0):
                h = h + self.q
            h = h*self.u % self.q
            return h*self.p+l111ll1111_Krypto_
        return pow(c, self.d, self.n)
    def _1l11l1lll_Krypto_(self, m):
        return pow(m, self.e, self.n)
    def _1l11l1l1l_Krypto_(self, m):
        if not self.l1l1111l1l_Krypto_():
            raise TypeError(l1l1111_Krypto_ (u"ࠨࡎࡰࠢࡳࡶ࡮ࡼࡡࡵࡧࠣ࡯ࡪࡿࠢ৺"))
        return self._1l111l111_Krypto_(m)
    def _1l11111l1_Krypto_(self, m, sig):
        return self._1l11l1lll_Krypto_(sig) == m
    def l1l1111l1l_Krypto_(self):
        return hasattr(self, l1l1111_Krypto_ (u"ࠧࡥࠩ৻"))
    def size(self):
        l1l1111_Krypto_ (u"ࠣࠤࠥࡖࡪࡺࡵࡳࡰࠣࡸ࡭࡫ࠠ࡮ࡣࡻ࡭ࡲࡻ࡭ࠡࡰࡸࡱࡧ࡫ࡲࠡࡱࡩࠤࡧ࡯ࡴࡴࠢࡷ࡬ࡦࡺࠠࡤࡣࡱࠤࡧ࡫ࠠࡦࡰࡦࡶࡾࡶࡴࡦࡦࠥࠦࠧৼ")
        return size(self.n) - 1
def l11l11lll1_Krypto_(n, e, d=None, p=None, q=None, u=None):
    l1l1111_Krypto_ (u"ࠤࠥࠦࡈࡵ࡮ࡴࡶࡵࡹࡨࡺࠠࡢࡰࠣࡖࡘࡇࡋࡦࡻࠣࡳࡧࡰࡥࡤࡶࠥࠦࠧ৽")
    assert isinstance(n, int)
    assert isinstance(e, int)
    assert isinstance(d, (int, type(None)))
    assert isinstance(p, (int, type(None)))
    assert isinstance(q, (int, type(None)))
    assert isinstance(u, (int, type(None)))
    obj = _111l1lll1_Krypto_()
    obj.n = n
    obj.e = e
    if d is None:
        return obj
    obj.d = d
    if p is not None and q is not None:
        obj.p = p
        obj.q = q
    else:
        l111ll11ll_Krypto_ = d*e-1
        t = l111ll11ll_Krypto_
        while t%2==0:
            t=divmod(t,2)[0]
        l111l1llll_Krypto_ = 0
        a = 2
        while not l111l1llll_Krypto_ and a<100:
            k = t
            while k<l111ll11ll_Krypto_:
                l111ll1l1l_Krypto_ = pow(a,k,n)
                if l111ll1l1l_Krypto_!=1 and l111ll1l1l_Krypto_!=(n-1) and pow(l111ll1l1l_Krypto_,2,n)==1:
                    obj.p = l11llllll1_Krypto_(l111ll1l1l_Krypto_+1,n)
                    l111l1llll_Krypto_ = 1
                    break
                k = k*2
            a = a+2
        if not l111l1llll_Krypto_:
            raise ValueError(l1l1111_Krypto_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡣࡰ࡯ࡳࡹࡹ࡫ࠠࡧࡣࡦࡸࡴࡸࡳࠡࡲࠣࡥࡳࡪࠠࡲࠢࡩࡶࡴࡳࠠࡦࡺࡳࡳࡳ࡫࡮ࡵࠢࡧ࠲ࠧ৾"))
        assert ((n % obj.p)==0)
        obj.q = divmod(n,obj.p)[0]
    if u is not None:
        obj.u = u
    else:
        obj.u = l11llll1ll_Krypto_(obj.p, obj.q)
    return obj
class _111ll11l1_Krypto_(object):
    def size(self):
        l1l1111_Krypto_ (u"ࠦࠧࠨࡒࡦࡶࡸࡶࡳࠦࡴࡩࡧࠣࡱࡦࡾࡩ࡮ࡷࡰࠤࡳࡻ࡭ࡣࡧࡵࠤࡴ࡬ࠠࡣ࡫ࡷࡷࠥࡺࡨࡢࡶࠣࡧࡦࡴࠠࡣࡧࠣࡩࡳࡩࡲࡺࡲࡷࡩࡩࠨࠢࠣ৿")
        return size(self.p) - 1
    def l1l1111l1l_Krypto_(self):
        return hasattr(self, l1l1111_Krypto_ (u"ࠬࡾࠧ਀"))
    def _1l11l1l1l_Krypto_(self, m, k):
        if not self.l1l1111l1l_Krypto_():
            raise TypeError(l1l1111_Krypto_ (u"ࠨࡎࡰࠢࡳࡶ࡮ࡼࡡࡵࡧࠣ࡯ࡪࡿࠢਁ"))
        if not (1 < k < self.q):
            raise ValueError(l1l1111_Krypto_ (u"ࠢ࡬ࠢ࡬ࡷࠥࡴ࡯ࡵࠢࡥࡩࡹࡽࡥࡦࡰࠣ࠶ࠥࡧ࡮ࡥࠢࡴ࠱࠶ࠨਂ"))
        l111ll1ll1_Krypto_ = l11llll1ll_Krypto_(k, self.q)
        r = pow(self.g, k, self.p) % self.q
        s = (l111ll1ll1_Krypto_ * (m + self.x * r)) % self.q
        return (r, s)
    def _1l11111l1_Krypto_(self, m, r, s):
        if not (0 < r < self.q) or not (0 < s < self.q):
            return False
        w = l11llll1ll_Krypto_(s, self.q)
        l111ll1l11_Krypto_ = (m*w) % self.q
        l111ll111l_Krypto_ = (r*w) % self.q
        v = (pow(self.g, l111ll1l11_Krypto_, self.p) * pow(self.y, l111ll111l_Krypto_, self.p) % self.p) % self.q
        return v == r
def l1l111l1ll_Krypto_(y, g, p, q, x=None):
    assert isinstance(y, int)
    assert isinstance(g, int)
    assert isinstance(p, int)
    assert isinstance(q, int)
    assert isinstance(x, (int, type(None)))
    obj = _111ll11l1_Krypto_()
    obj.y = y
    obj.g = g
    obj.p = p
    obj.q = q
    if x is not None: obj.x = x
    return obj