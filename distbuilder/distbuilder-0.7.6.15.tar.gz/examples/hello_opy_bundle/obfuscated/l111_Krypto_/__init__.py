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
from l111ll1_Krypto_.l11111l_Krypto_ import l111lll_Krypto_
from l111ll1_Krypto_.l1lll1ll1_Krypto_ import l1lll1ll11_Krypto_, l11111ll1_Krypto_
from l111ll1_Krypto_.l11l1l1lll_Krypto_.l1l1l1l1l1_Krypto_ import l1l1l11l11_Krypto_
from l111ll1_Krypto_.l1ll1l11l1_Krypto_.l111l1l111_Krypto_ import l111l1111l_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_ import Counter
l1ll111ll1ll_Krypto_ = (10000, 10000, 100000)
l1ll11l1ll11_Krypto_ = 256
l1ll1ll11lll_Krypto_ = (128, 256, 256)
HASH = l1lll1ll11_Krypto_
PREFIX = l1l1111_Krypto_ (u"ࡥࠫࡸࡩࠧ⍬")
l1ll1ll1111l_Krypto_ = (PREFIX + l1l1111_Krypto_ (u"ࡦࠬࡢࡸ࠱࠲࡟ࡼ࠵࠶ࠧ⍭"), PREFIX + l1l1111_Krypto_ (u"ࡧ࠭࡜ࡹ࠲࠳ࡠࡽ࠶࠱ࠨ⍮"), PREFIX + l1l1111_Krypto_ (u"ࡨࠧ࡝ࡺ࠳࠴ࡡࡾ࠰࠳ࠩ⍯"))
l1ll11lll1ll_Krypto_ = 2
l1ll1l111111_Krypto_ = l111lll_Krypto_.block_size*8//2
for l1ll11l1l1l1_Krypto_ in l1ll1ll11lll_Krypto_:
    assert l1ll1l111111_Krypto_ <= l1ll11l1l1l1_Krypto_
l1ll1l1lllll_Krypto_ = 4
for header in l1ll1ll1111l_Krypto_:
    assert len(header) == l1ll1l1lllll_Krypto_
def l1_Krypto_(l1l1l11l1l_Krypto_, data):
    l1l1111_Krypto_ (u"ࠧࠨࠩࠍࠤࠥࠦࠠࡆࡰࡦࡶࡾࡶࡴࠡࡵࡲࡱࡪࠦࡤࡢࡶࡤ࠲ࠥࠦࡉ࡯ࡲࡸࡸࠥࡩࡡ࡯ࠢࡥࡩࠥࡨࡹࡵࡧࡶࠤࡴࡸࠠࡢࠢࡶࡸࡷ࡯࡮ࡨࠢࠫࡻ࡭࡯ࡣࡩࠢࡺ࡭ࡱࡲࠠࡣࡧࠣࡩࡳࡩ࡯ࡥࡧࡧࠎࠥࠦࠠࠡࡷࡶ࡭ࡳ࡭ࠠࡖࡖࡉ࠱࠽࠯࠮ࠋࠌࠣࠤࠥࠦࡀࡱࡣࡵࡥࡲࠦࡰࡢࡵࡶࡻࡴࡸࡤ࠻ࠢࡗ࡬ࡪࠦࡳࡦࡥࡵࡩࡹࠦࡶࡢ࡮ࡸࡩࠥࡻࡳࡦࡦࠣࡥࡸࠦࡴࡩࡧࠣࡦࡦࡹࡩࡴࠢࡩࡳࡷࠦࡡࠡ࡭ࡨࡽ࠳ࠐࠠࠡࠢࠣࡘ࡭࡯ࡳࠡࡵ࡫ࡳࡺࡲࡤࠡࡤࡨࠤࡦࡹࠠ࡭ࡱࡱ࡫ࠥࡧࡳࠡࡸࡤࡶ࡮࡫ࡤࠡࡣࡶࠤࡵࡵࡳࡴ࡫ࡥࡰࡪ࠴ࠠࠡࡖࡵࡽࠥࡺ࡯ࠡࡣࡹࡳ࡮ࡪࠠࡤࡱࡰࡱࡴࡴࠠࡸࡱࡵࡨࡸ࠴ࠊࠋࠢࠣࠤࠥࡆࡰࡢࡴࡤࡱࠥࡪࡡࡵࡣ࠽ࠤ࡙࡮ࡥࠡࡦࡤࡸࡦࠦࡴࡰࠢࡥࡩࠥ࡫࡮ࡤࡴࡼࡴࡹ࡫ࡤ࠯ࠌࠍࠤࠥࠦࠠࡁࡴࡨࡸࡺࡸ࡮࠻ࠢࡗ࡬ࡪࠦࡥ࡯ࡥࡵࡽࡵࡺࡥࡥࠢࡧࡥࡹࡧࠬࠡࡣࡶࠤࡧࡿࡴࡦࡵ࠱ࠎࠥࠦࠠࠡࠩࠪࠫ⍰")
    data = _1ll11l11111_Krypto_(data)
    _1ll111lllll_Krypto_(data)
    l1l1l111ll_Krypto_ = bytes(_1ll1l111ll1_Krypto_(l1ll1ll11lll_Krypto_[l1ll11lll1ll_Krypto_]//8))
    l1ll11l111l1_Krypto_, l1ll11l11lll_Krypto_ = _1ll11llll11_Krypto_(l1l1l11l1l_Krypto_, l1l1l111ll_Krypto_, l1ll111ll1ll_Krypto_[l1ll11lll1ll_Krypto_])
    l1lll1llll1_Krypto_ = Counter.new(l1ll1l111111_Krypto_, prefix=l1l1l111ll_Krypto_[:l1ll1l111111_Krypto_//8])
    l1llll11l_Krypto_ = l111lll_Krypto_.new(l1ll11l11lll_Krypto_, l111lll_Krypto_.MODE_CTR, counter=l1lll1llll1_Krypto_)
    l11l1ll1_Krypto_ = l1llll11l_Krypto_.l1_Krypto_(data)
    l1ll11l11ll1_Krypto_ = _1ll111lll11_Krypto_(l1ll11l111l1_Krypto_, l1ll1ll1111l_Krypto_[l1ll11lll1ll_Krypto_] + l1l1l111ll_Krypto_ + l11l1ll1_Krypto_)
    return l1ll1ll1111l_Krypto_[l1ll11lll1ll_Krypto_] + l1l1l111ll_Krypto_ + l11l1ll1_Krypto_ + l1ll11l11ll1_Krypto_
def l1lllll_Krypto_(l1l1l11l1l_Krypto_, data):
    l1l1111_Krypto_ (u"ࠨࠩࠪࠎࠥࠦࠠࠡࡆࡨࡧࡷࡿࡰࡵࠢࡶࡳࡲ࡫ࠠࡥࡣࡷࡥ࠳ࠦࠠࡊࡰࡳࡹࡹࠦ࡭ࡶࡵࡷࠤࡧ࡫ࠠࡣࡻࡷࡩࡸ࠴ࠊࠋࠢࠣࠤࠥࡆࡰࡢࡴࡤࡱࠥࡶࡡࡴࡵࡺࡳࡷࡪ࠺ࠡࡖ࡫ࡩࠥࡹࡥࡤࡴࡨࡸࠥࡼࡡ࡭ࡷࡨࠤࡺࡹࡥࡥࠢࡤࡷࠥࡺࡨࡦࠢࡥࡥࡸ࡯ࡳࠡࡨࡲࡶࠥࡧࠠ࡬ࡧࡼ࠲ࠏࠦࠠࠡࠢࡗ࡬࡮ࡹࠠࡴࡪࡲࡹࡱࡪࠠࡣࡧࠣࡥࡸࠦ࡬ࡰࡰࡪࠤࡦࡹࠠࡷࡣࡵ࡭ࡪࡪࠠࡢࡵࠣࡴࡴࡹࡳࡪࡤ࡯ࡩ࠳ࠦࠠࡕࡴࡼࠤࡹࡵࠠࡢࡸࡲ࡭ࡩࠦࡣࡰ࡯ࡰࡳࡳࠦࡷࡰࡴࡧࡷ࠳ࠐࠊࠡࠢࠣࠤࡅࡶࡡࡳࡣࡰࠤࡩࡧࡴࡢ࠼ࠣࡘ࡭࡫ࠠࡥࡣࡷࡥࠥࡺ࡯ࠡࡤࡨࠤࡩ࡫ࡣࡳࡻࡳࡸࡪࡪࠬࠡࡶࡼࡴ࡮ࡩࡡ࡭࡮ࡼࠤࡦࡹࠠࡣࡻࡷࡩࡸ࠴ࠊࠋࠢࠣࠤࠥࡆࡲࡦࡶࡸࡶࡳࡀࠠࡕࡪࡨࠤࡩ࡫ࡣࡳࡻࡳࡸࡪࡪࠠࡥࡣࡷࡥ࠱ࠦࡡࡴࠢࡥࡽࡹ࡫ࡳ࠯ࠢࠣࡍ࡫ࠦࡴࡩࡧࠣࡳࡷ࡯ࡧࡪࡰࡤࡰࠥࡳࡥࡴࡵࡤ࡫ࡪࠦࡷࡢࡵࠣࡥࠏࠦࠠࠡࠢࡶࡸࡷ࡯࡮ࡨࠢࡼࡳࡺࠦࡣࡢࡰࠣࡶࡪ࠳ࡣࡳࡧࡤࡸࡪࠦࡴࡩࡣࡷࠤࡺࡹࡩ࡯ࡩࠣࡤࡷ࡫ࡳࡶ࡮ࡷ࠲ࡩ࡫ࡣࡰࡦࡨࠬࠬࡻࡴࡧ࠺ࠪ࠭ࡥ࠴ࠊࠡࠢࠣࠤࠬ࠭ࠧ⍱")
    _1ll11l1ll1l_Krypto_(data)
    _1ll1l11lll1_Krypto_(data)
    version = _1ll1l11ll1l_Krypto_(data)
    _1ll11l111ll_Krypto_(data, version)
    raw = data[l1ll1l1lllll_Krypto_:]
    l1l1l111ll_Krypto_ = raw[:l1ll1ll11lll_Krypto_[version]//8]
    l1ll11l111l1_Krypto_, l1ll11l11lll_Krypto_ = _1ll11llll11_Krypto_(l1l1l11l1l_Krypto_, l1l1l111ll_Krypto_, l1ll111ll1ll_Krypto_[version])
    l1ll11l11ll1_Krypto_ = raw[-HASH.digest_size:]
    l1ll111llll1_Krypto_ = _1ll111lll11_Krypto_(l1ll11l111l1_Krypto_, data[:-HASH.digest_size])
    _1ll11l1l11l_Krypto_(l1ll11l111l1_Krypto_, l1ll11l11ll1_Krypto_, l1ll111llll1_Krypto_)
    l1lll1llll1_Krypto_ = Counter.new(l1ll1l111111_Krypto_, prefix=l1l1l111ll_Krypto_[:l1ll1l111111_Krypto_//8])
    l1llll11l_Krypto_ = l111lll_Krypto_.new(l1ll11l11lll_Krypto_, l111lll_Krypto_.l1llllll_Krypto_, l1lll1llll1_Krypto_=l1lll1llll1_Krypto_)
    return l1llll11l_Krypto_.l1lllll_Krypto_(raw[l1ll1ll11lll_Krypto_[version]//8:-HASH.digest_size])
class l1ll1l1llll1_Krypto_(Exception): pass
class l1ll11l1l1ll_Krypto_(Exception): pass
def _1ll11l1ll1l_Krypto_(data):
    l1ll11lll11l_Krypto_ = type(l1l1111_Krypto_ (u"ࡤࠪࠫ⍲").decode(l1l1111_Krypto_ (u"ࠪࡹࡹ࡬࠸ࠨ⍳")))
    if isinstance(data, l1ll11lll11l_Krypto_):
        raise l1ll1l1llll1_Krypto_(l1l1111_Krypto_ (u"ࠫࡉࡧࡴࡢࠢࡷࡳࠥࡪࡥࡤࡴࡼࡴࡹࠦ࡭ࡶࡵࡷࠤࡧ࡫ࠠࡣࡻࡷࡩࡸࡁࠠࠨ⍴") +
        l1l1111_Krypto_ (u"ࠬࡿ࡯ࡶࠢࡦࡥࡳࡴ࡯ࡵࠢࡸࡷࡪࠦࡡࠡࡵࡷࡶ࡮ࡴࡧࠡࡤࡨࡧࡦࡻࡳࡦࠢࡱࡳࠥࡹࡴࡳ࡫ࡱ࡫ࠥ࡫࡮ࡤࡱࡧ࡭ࡳ࡭ࠠࡸ࡫࡯ࡰࠥࡧࡣࡤࡧࡳࡸࠥࡧ࡬࡭ࠢࡳࡳࡸࡹࡩࡣ࡮ࡨࠤࡨ࡮ࡡࡳࡣࡦࡸࡪࡸࡳ࠯ࠩ⍵"))
def _1ll111lllll_Krypto_(data):
    if len(data) > 2**l1ll1l111111_Krypto_:
        raise l1ll11l1l1ll_Krypto_(l1l1111_Krypto_ (u"࠭ࡍࡦࡵࡶࡥ࡬࡫ࠠࡵࡱࡲࠤࡱࡵ࡮ࡨ࠰ࠪ⍶"))
def _1ll11l111ll_Krypto_(data, version):
    if len(data) < l1ll1l1lllll_Krypto_ + l1ll1ll11lll_Krypto_[version]//8 + HASH.digest_size:
        raise l1ll1l1llll1_Krypto_(l1l1111_Krypto_ (u"ࠧࡎ࡫ࡶࡷ࡮ࡴࡧࠡࡦࡤࡸࡦ࠴ࠧ⍷"))
def _1ll1l11lll1_Krypto_(data):
    if len(data) >= 2 and data[:2] != PREFIX:
        raise l1ll1l1llll1_Krypto_(l1l1111_Krypto_ (u"ࠨࡆࡤࡸࡦࠦࡰࡢࡵࡶࡩࡩࠦࡴࡰࠢࡧࡩࡨࡸࡹࡱࡶࠣࡻࡪࡸࡥࠡࡰࡲࡸࠥ࡭ࡥ࡯ࡧࡵࡥࡹ࡫ࡤࠡࡤࡼࠤࡸ࡯࡭ࡱ࡮ࡨ࠱ࡨࡸࡹࡱࡶࠣࠬࡧࡧࡤࠡࡪࡨࡥࡩ࡫ࡲࠪ࠰ࠪ⍸"))
def _1ll1l11ll1l_Krypto_(data):
    if len(data) >= l1ll1l1lllll_Krypto_:
        try:
            return l1ll1ll1111l_Krypto_.index(data[:l1ll1l1lllll_Krypto_])
        except:
            raise l1ll1l1llll1_Krypto_(
                l1l1111_Krypto_ (u"ࠩࡗ࡬ࡪࠦࡤࡢࡶࡤࠤࡦࡶࡰࡦࡣࡵࠤࡹࡵࠠࡣࡧࠣࡩࡳࡩࡲࡺࡲࡷࡩࡩࠦࡷࡪࡶ࡫ࠤࡦࠦ࡭ࡰࡴࡨࠤࡷ࡫ࡣࡦࡰࡷࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥࡵࡦࠡࡵ࡬ࡱࡵࡲࡥ࠮ࡥࡵࡽࡵࡺࠠࠩࡤࡤࡨࠥ࡮ࡥࡢࡦࡨࡶ࠮࠴ࠠࠨ⍹") +
                l1l1111_Krypto_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣࡹࡵࡪࡡࡵࡧࠣࡸ࡭࡫ࠠ࡭࡫ࡥࡶࡦࡸࡹࠡࡣࡱࡨࠥࡺࡲࡺࠢࡤ࡫ࡦ࡯࡮࠯ࠩ⍺"))
    else:
        raise l1ll1l1llll1_Krypto_(l1l1111_Krypto_ (u"ࠫࡒ࡯ࡳࡴ࡫ࡱ࡫ࠥ࡮ࡥࡢࡦࡨࡶ࠳࠭⍻"))
def _1ll11l1l11l_Krypto_(key, l1ll11l11ll1_Krypto_, l1ll111llll1_Krypto_):
    if _1ll111lll11_Krypto_(key, l1ll11l11ll1_Krypto_) != _1ll111lll11_Krypto_(key, l1ll111llll1_Krypto_):
        raise l1ll1l1llll1_Krypto_(l1l1111_Krypto_ (u"ࠬࡈࡡࡥࠢࡳࡥࡸࡹࡷࡰࡴࡧࠤࡴࡸࠠࡤࡱࡵࡶࡺࡶࡴࠡ࠱ࠣࡱࡴࡪࡩࡧ࡫ࡨࡨࠥࡪࡡࡵࡣ࠱ࠫ⍼"))
def _1ll11l1l111_Krypto_(l1l1l11l1l_Krypto_, l1l1l111ll_Krypto_, l1ll11l11l11_Krypto_, count):
    return l1l1l11l11_Krypto_(l1l1l11l1l_Krypto_, l1l1l111ll_Krypto_, l1l1l111l1_Krypto_=l1ll11l11l11_Krypto_,
                  count=count, l1l1l11ll1_Krypto_=lambda p,s: l11111ll1_Krypto_.new(p,s,HASH).digest())
def _1ll11llll11_Krypto_(l1l1l11l1l_Krypto_, l1l1l111ll_Krypto_, l1ll111lll1l_Krypto_):
    if not l1l1l111ll_Krypto_: raise ValueError(l1l1111_Krypto_ (u"࠭ࡍࡪࡵࡶ࡭ࡳ࡭ࠠࡴࡣ࡯ࡸ࠳࠭⍽"))
    if not l1l1l11l1l_Krypto_: raise ValueError(l1l1111_Krypto_ (u"ࠧࡎ࡫ࡶࡷ࡮ࡴࡧࠡࡲࡤࡷࡸࡽ࡯ࡳࡦ࠱ࠫ⍾"))
    l1ll11l1111l_Krypto_ = l1ll11l1ll11_Krypto_ // 8
    keys = _1ll11l1l111_Krypto_(_1ll11l11111_Krypto_(l1l1l11l1l_Krypto_), l1l1l111ll_Krypto_, 2*l1ll11l1111l_Krypto_, l1ll111lll1l_Krypto_)
    return keys[:l1ll11l1111l_Krypto_], keys[l1ll11l1111l_Krypto_:]
def _1ll11ll111l_Krypto_(l1ll11l11l1l_Krypto_):
    return bytearray(_1ll11l1l111_Krypto_(bytes(l1ll11l11l1l_Krypto_), l1l1111_Krypto_ (u"ࡣࠩࠪ⍿"), len(l1ll11l11l1l_Krypto_), 1))
def _1ll1l111ll1_Krypto_(n):
    return _1ll11ll111l_Krypto_(bytearray(l111l1111l_Krypto_(8) for _ in range(n)))
def _1ll111lll11_Krypto_(key, data):
    return l11111ll1_Krypto_.new(key, data, HASH).digest()
def _1ll11l11111_Krypto_(data):
    l1ll11lll11l_Krypto_ = type(l1l1111_Krypto_ (u"ࡤࠪࠫ⎀").decode(l1l1111_Krypto_ (u"ࠪࡹࡹ࡬࠸ࠨ⎁")))
    if isinstance(data, l1ll11lll11l_Krypto_):
        return data.encode(l1l1111_Krypto_ (u"ࠫࡺࡺࡦ࠹ࠩ⎂"))
    return data