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
__revision__ = l1l1111_Krypto_ (u"ࠣࠦࡌࡨࠩࠨਟ")
import sys as l1l11l11_Krypto_
if l1l11l11_Krypto_.version_info[0] == 2 and l1l11l11_Krypto_.version_info[1] == 1:
    from l111ll1_Krypto_.l1l111ll_Krypto_.l1l1ll1l_Krypto_ import *
import os as l1111111l1_Krypto_
import threading as l1lllllllll_Krypto_
import struct as l1l1l1ll11_Krypto_
import time as l11111l111_Krypto_
from math import floor as l1111l1l11_Krypto_
from l111ll1_Krypto_.l1ll1l11l1_Krypto_ import l111111111_Krypto_
from l111ll1_Krypto_.l1ll1l11l1_Krypto_.l1111l1l1l_Krypto_ import l11111lll1_Krypto_
class _1111lllll_Krypto_(object):
    def __init__(self, l1111llll1_Krypto_, l1111111ll_Krypto_):
        self._1llllllll1_Krypto_ = l1111llll1_Krypto_
        self._1111ll1l1_Krypto_ = l1111111ll_Krypto_
        self._1111l1111_Krypto_ = 0
    def l11111ll1l_Krypto_(self, data):
        self._1llllllll1_Krypto_.l1111l1lll_Krypto_(self._1111ll1l1_Krypto_, self._1111l1111_Krypto_, data)
        self._1111l1111_Krypto_ = (self._1111l1111_Krypto_ + 1) & 31
class _111111l1l_Krypto_(object):
    def __init__(self, l1111llll1_Krypto_):
        self._11111111l_Krypto_ = l111111111_Krypto_.new()
        self._11111l11l_Krypto_ = _1111lllll_Krypto_(l1111llll1_Krypto_, 255)
        self._1111ll111_Krypto_ = _1111lllll_Krypto_(l1111llll1_Krypto_, 254)
        self._1111ll1ll_Krypto_ = _1111lllll_Krypto_(l1111llll1_Krypto_, 253)
    def l1111ll11l_Krypto_(self):
        for i in range(2):
            block = self._11111111l_Krypto_.read(32*32)
            for p in range(32):
                self._11111l11l_Krypto_.l11111ll1l_Krypto_(block[p*32:(p+1)*32])
            block = None
        self._11111111l_Krypto_.flush()
    def l111111lll_Krypto_(self):
        self._11111l11l_Krypto_.l11111ll1l_Krypto_(self._11111111l_Krypto_.read(8))
        t = l11111l111_Krypto_.l11111l111_Krypto_()
        self._1111ll111_Krypto_.l11111ll1l_Krypto_(l1l1l1ll11_Krypto_.pack(l1l1111_Krypto_ (u"ࠤࡃࡍࠧਠ"), int(2**30 * (t - l1111l1l11_Krypto_(t)))))
        t = l11111l111_Krypto_.clock()
        self._1111ll1ll_Krypto_.l11111ll1l_Krypto_(l1l1l1ll11_Krypto_.pack(l1l1111_Krypto_ (u"ࠥࡄࡎࠨਡ"), int(2**30 * (t - l1111l1l11_Krypto_(t)))))
class _1111lll11_Krypto_(object):
    def __init__(self):
        self.closed = False
        self._1111l11ll_Krypto_ = l11111lll1_Krypto_.l11111lll1_Krypto_()
        self._1111lll1l_Krypto_ = _111111l1l_Krypto_(self._1111l11ll_Krypto_)
        self.l1111ll11l_Krypto_()
    def l1111ll11l_Krypto_(self):
        l1l1111_Krypto_ (u"ࠦࠧࠨࡉ࡯࡫ࡷ࡭ࡦࡲࡩࡻࡧࠣࡸ࡭࡫ࠠࡳࡣࡱࡨࡴࡳࠠ࡯ࡷࡰࡦࡪࡸࠠࡨࡧࡱࡩࡷࡧࡴࡰࡴࠣࡥࡳࡪࠠࡴࡧࡨࡨࠥ࡯ࡴࠡࡹ࡬ࡸ࡭ࠦࡥ࡯ࡶࡵࡳࡵࡿࠠࡧࡴࡲࡱࠏࠦࠠࠡࠢࠣࠤࠥࠦࡴࡩࡧࠣࡳࡵ࡫ࡲࡢࡶ࡬ࡲ࡬ࠦࡳࡺࡵࡷࡩࡲ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦਢ")
        self._11111ll11_Krypto_ = l1111111l1_Krypto_.getpid()
        self._1111lll1l_Krypto_.l1111ll11l_Krypto_()
        self._1111l11ll_Krypto_._11111l1l1_Krypto_()
    def close(self):
        self.closed = True
        self._11111111l_Krypto_ = None
        self._1111l11ll_Krypto_ = None
    def flush(self):
        pass
    def read(self, l11l1111l1_Krypto_):
        l1l1111_Krypto_ (u"ࠧࠨࠢࡓࡧࡷࡹࡷࡴࠠࡏࠢࡥࡽࡹ࡫ࡳࠡࡨࡵࡳࡲࠦࡴࡩࡧࠣࡖࡓࡍ࠮ࠣࠤࠥਣ")
        if self.closed:
            raise ValueError(l1l1111_Krypto_ (u"ࠨࡉ࠰ࡑࠣࡳࡵ࡫ࡲࡢࡶ࡬ࡳࡳࠦ࡯࡯ࠢࡦࡰࡴࡹࡥࡥࠢࡩ࡭ࡱ࡫ࠢਤ"))
        if not isinstance(l11l1111l1_Krypto_, int):
            raise TypeError(l1l1111_Krypto_ (u"ࠢࡢࡰࠣ࡭ࡳࡺࡥࡨࡧࡵࠤ࡮ࡹࠠࡳࡧࡴࡹ࡮ࡸࡥࡥࠤਥ"))
        if l11l1111l1_Krypto_ < 0:
            raise ValueError(l1l1111_Krypto_ (u"ࠣࡥࡤࡲࡳࡵࡴࠡࡴࡨࡥࡩࠦࡴࡰࠢࡨࡲࡩࠦ࡯ࡧࠢ࡬ࡲ࡫࡯࡮ࡪࡶࡨࠤࡸࡺࡲࡦࡣࡰࠦਦ"))
        self._1111lll1l_Krypto_.l111111lll_Krypto_()
        l111l111ll_Krypto_ = self._1111l11ll_Krypto_.l111111ll1_Krypto_(l11l1111l1_Krypto_)
        self._1111l1ll1_Krypto_()
        return l111l111ll_Krypto_
    def _1111l1ll1_Krypto_(self):
        if l1111111l1_Krypto_.getpid() != self._11111ll11_Krypto_:
            raise AssertionError(l1l1111_Krypto_ (u"ࠤࡓࡍࡉࠦࡣࡩࡧࡦ࡯ࠥ࡬ࡡࡪ࡮ࡨࡨ࠳ࠦࡒࡏࡉࠣࡱࡺࡹࡴࠡࡤࡨࠤࡷ࡫࠭ࡪࡰ࡬ࡸ࡮ࡧ࡬ࡪࡼࡨࡨࠥࡧࡦࡵࡧࡵࠤ࡫ࡵࡲ࡬ࠪࠬ࠲ࠥࡎࡩ࡯ࡶ࠽ࠤ࡙ࡸࡹࠡࡔࡤࡲࡩࡵ࡭࠯ࡣࡷࡪࡴࡸ࡫ࠩࠫࠥਧ"))
class _11111l1ll_Krypto_(_1111lll11_Krypto_):
    def __init__(self):
        self._lock = l1lllllllll_Krypto_.Lock()
        _1111lll11_Krypto_.__init__(self)
    def close(self):
        self._lock.acquire()
        try:
            return _1111lll11_Krypto_.close(self)
        finally:
            self._lock.release()
    def l1111ll11l_Krypto_(self):
        self._lock.acquire()
        try:
            return _1111lll11_Krypto_.l1111ll11l_Krypto_(self)
        finally:
            self._lock.release()
    def read(self, bytes):
        self._lock.acquire()
        try:
            return _1111lll11_Krypto_.read(self, bytes)
        finally:
            self._lock.release()
class l111l11111_Krypto_(object):
    def __init__(self, l111111l11_Krypto_):
        self.closed = False
        self._11111llll_Krypto_ = l111111l11_Krypto_
    def __enter__(self):
        l1l1111_Krypto_ (u"ࠥࠦࠧࡖࡅࡑࠢ࠶࠸࠸ࠦࡳࡶࡲࡳࡳࡷࡺࠢࠣࠤਨ")
    def __exit__(self):
        l1l1111_Krypto_ (u"ࠦࠧࠨࡐࡆࡒࠣ࠷࠹࠹ࠠࡴࡷࡳࡴࡴࡸࡴࠣࠤࠥ਩")
        self.close()
    def close(self):
        self.closed = True
        self._11111llll_Krypto_ = None
    def read(self, bytes):
        if self.closed:
            raise ValueError(l1l1111_Krypto_ (u"ࠧࡏ࠯ࡐࠢࡲࡴࡪࡸࡡࡵ࡫ࡲࡲࠥࡵ࡮ࠡࡥ࡯ࡳࡸ࡫ࡤࠡࡨ࡬ࡰࡪࠨਪ"))
        return self._11111llll_Krypto_.read(bytes)
    def flush(self):
        if self.closed:
            raise ValueError(l1l1111_Krypto_ (u"ࠨࡉ࠰ࡑࠣࡳࡵ࡫ࡲࡢࡶ࡬ࡳࡳࠦ࡯࡯ࠢࡦࡰࡴࡹࡥࡥࠢࡩ࡭ࡱ࡫ࠢਫ"))
_1lllllll1l_Krypto_ = l1lllllllll_Krypto_.Lock()
_11111llll_Krypto_ = None
def _1111l111l_Krypto_():
    global _11111llll_Krypto_
    _1lllllll1l_Krypto_.acquire()
    try:
        if _11111llll_Krypto_ is None:
            _11111llll_Krypto_ = _11111l1ll_Krypto_()
        return _11111llll_Krypto_
    finally:
        _1lllllll1l_Krypto_.release()
def new():
    return l111l11111_Krypto_(_1111l111l_Krypto_())
def l1111ll11l_Krypto_():
    _1111l111l_Krypto_().l1111ll11l_Krypto_()
def l1111l11l1_Krypto_(n):
    l1l1111_Krypto_ (u"ࠢࠣࠤࡕࡩࡹࡻࡲ࡯ࠢࡷ࡬ࡪࠦࡳࡱࡧࡦ࡭࡫࡯ࡥࡥࠢࡱࡹࡲࡨࡥࡳࠢࡲࡪࠥࡩࡲࡺࡲࡷࡳ࡬ࡸࡡࡱࡪ࡬ࡧࡦࡲ࡬ࡺ࠯ࡶࡸࡷࡵ࡮ࡨࠢࡵࡥࡳࡪ࡯࡮ࠢࡥࡽࡹ࡫ࡳ࠯ࠤࠥࠦਬ")
    return _1111l111l_Krypto_().read(n)