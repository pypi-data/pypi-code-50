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
from binascii import hexlify as l1111l111_Krypto_
from functools import reduce as l1ll11llll_Krypto_
from unittest import TestCase as l1ll1ll11ll1_Krypto_,main as l1ll1l11l11l_Krypto_
from l111ll1_Krypto_.l11111l_Krypto_ import l111lll_Krypto_
from l111ll1_Krypto_.l11l1l1lll_Krypto_.l1l1l1l1l1_Krypto_ import l1l1l11l11_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_ import Counter
from math import sqrt as l1ll11lll111_Krypto_
from l111_Krypto_ import l1_Krypto_, l1lllll_Krypto_, _1ll11llll11_Krypto_, l1ll1l1llll1_Krypto_,      _1ll1l111ll1_Krypto_, l1ll1ll1111l_Krypto_, l1ll1l111111_Krypto_, l1ll1ll11lll_Krypto_, _1ll1l11lll1_Krypto_,      _1ll1l11ll1l_Krypto_, l1ll11lll1ll_Krypto_, l1ll1l1lllll_Krypto_, _1ll11ll111l_Krypto_
class l1ll1l1l111l_Krypto_(l1ll1ll11ll1_Krypto_):
    def l1ll11llll1l_Krypto_(self):
        l1ll1l1l11ll_Krypto_ = l1lllll_Krypto_(l1l1111_Krypto_ (u"ࠬࡶࡡࡴࡵࡺࡳࡷࡪࠧ⋷"), l1_Krypto_(l1l1111_Krypto_ (u"࠭ࡰࡢࡵࡶࡻࡴࡸࡤࠨ⋸"), l1l1111_Krypto_ (u"ࡢࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⋹")))
        assert l1ll1l1l11ll_Krypto_ == l1l1111_Krypto_ (u"ࡣࠩࡰࡩࡸࡹࡡࡨࡧࠪ⋺"), l1ll1l1l11ll_Krypto_
    def l1ll11ll1lll_Krypto_(self):
        l1ll1l1ll1l1_Krypto_ = l1l1111_Krypto_ (u"ࡤࠪࡷࡴࡳࡥࠡࡵࡷࡶ࡮ࡴࡧࠨ⋻").decode(l1l1111_Krypto_ (u"ࠪࡹࡹ࡬࠸ࠨ⋼"))
        try:
            l1lllll_Krypto_(l1l1111_Krypto_ (u"ࠫࡵࡧࡳࡴࡹࡲࡶࡩ࠭⋽"), l1ll1l1ll1l1_Krypto_)
            assert False, l1l1111_Krypto_ (u"ࠬ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡦࡴࡵࡳࡷ࠭⋾")
        except l1ll1l1llll1_Krypto_ as e:
            assert l1l1111_Krypto_ (u"࠭ࡢࡺࡶࡨࡷࠬ⋿") in str(e), e
    def l1ll1l1l1111_Krypto_(self):
        l1ll1l1l11ll_Krypto_ = l1lllll_Krypto_(l1l1111_Krypto_ (u"ࡢࠨࡲࡤࡷࡸࡽ࡯ࡳࡦࠪ⌀"), l1_Krypto_(l1l1111_Krypto_ (u"ࡣࠩࡳࡥࡸࡹࡷࡰࡴࡧࠫ⌁"), l1l1111_Krypto_ (u"ࡤࠪࡱࡪࡹࡳࡢࡩࡨࠫ⌂")))
        assert l1ll1l1l11ll_Krypto_ == l1l1111_Krypto_ (u"ࡥࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ⌃"), l1ll1l1l11ll_Krypto_
        l1ll1l1l11ll_Krypto_ = l1lllll_Krypto_(l1l1111_Krypto_ (u"ࠫࡵࡧࡳࡴࡹࡲࡶࡩ࠭⌄"), l1_Krypto_(l1l1111_Krypto_ (u"ࡧ࠭ࡰࡢࡵࡶࡻࡴࡸࡤࠨ⌅"), l1l1111_Krypto_ (u"ࡨࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⌆")))
        assert l1ll1l1l11ll_Krypto_ == l1l1111_Krypto_ (u"ࡢࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⌇"), l1ll1l1l11ll_Krypto_
        l1ll1l1l11ll_Krypto_ = l1lllll_Krypto_(l1l1111_Krypto_ (u"ࡣࠩࡳࡥࡸࡹࡷࡰࡴࡧࠫ⌈"), l1_Krypto_(l1l1111_Krypto_ (u"ࠩࡳࡥࡸࡹࡷࡰࡴࡧࠫ⌉"), l1l1111_Krypto_ (u"ࡥࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ⌊")))
        assert l1ll1l1l11ll_Krypto_ == l1l1111_Krypto_ (u"ࡦࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭⌋"), l1ll1l1l11ll_Krypto_
    def l1ll1l111l1l_Krypto_(self):
        def u(string):
            l1ll11lll11l_Krypto_ = type(l1l1111_Krypto_ (u"ࡧ࠭ࠧ⌌").decode(l1l1111_Krypto_ (u"࠭ࡵࡵࡨ࠻ࠫ⌍")))
            if not isinstance(string, l1ll11lll11l_Krypto_):
                return string.decode(l1l1111_Krypto_ (u"ࠧࡶࡶࡩ࠼ࠬ⌎"))
            return string
        l1ll11lllll1_Krypto_ = u(l1l1111_Krypto_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⌏"))
        l1ll11ll1l1l_Krypto_ = u(l1l1111_Krypto_ (u"ࠩࢨࢧ⢱ࠪࢢ⢢⢤⢦⢨⢪⢬⢧⢩⢫⢭⢯⢲⢴⢯⢺ࠩ⌐"))
        l1ll1l1l11ll_Krypto_ = l1lllll_Krypto_(l1l1111_Krypto_ (u"ࠪࡴࡦࡹࡳࡸࡱࡵࡨࠬ⌑"), l1_Krypto_(l1l1111_Krypto_ (u"ࠫࡵࡧࡳࡴࡹࡲࡶࡩ࠭⌒"), l1ll11lllll1_Krypto_))
        assert l1ll1l1l11ll_Krypto_.decode(l1l1111_Krypto_ (u"ࠬࡻࡴࡧ࠺ࠪ⌓")) == l1l1111_Krypto_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ⌔"), l1ll1l1l11ll_Krypto_
        l1ll1l1l11ll_Krypto_ = l1lllll_Krypto_(l1l1111_Krypto_ (u"ࠧࡱࡣࡶࡷࡼࡵࡲࡥࠩ⌕"), l1_Krypto_(l1l1111_Krypto_ (u"ࠨࡲࡤࡷࡸࡽ࡯ࡳࡦࠪ⌖"), l1ll11lllll1_Krypto_.encode(l1l1111_Krypto_ (u"ࠩࡸࡸ࡫࠾ࠧ⌗"))))
        assert l1ll1l1l11ll_Krypto_ == l1l1111_Krypto_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⌘").encode(l1l1111_Krypto_ (u"ࠫࡺࡺࡦ࠹ࠩ⌙")), l1ll1l1l11ll_Krypto_
        l1ll1l1l11ll_Krypto_ = l1lllll_Krypto_(l1l1111_Krypto_ (u"ࠬࡶࡡࡴࡵࡺࡳࡷࡪࠧ⌚"), l1_Krypto_(l1l1111_Krypto_ (u"࠭ࡰࡢࡵࡶࡻࡴࡸࡤࠨ⌛"), l1ll11ll1l1l_Krypto_))
        assert l1ll1l1l11ll_Krypto_.decode(l1l1111_Krypto_ (u"ࠧࡶࡶࡩ࠼ࠬ⌜")) == l1ll11ll1l1l_Krypto_, l1ll1l1l11ll_Krypto_
        l1ll1l1l11ll_Krypto_ = l1lllll_Krypto_(l1l1111_Krypto_ (u"ࠨࡲࡤࡷࡸࡽ࡯ࡳࡦࠪ⌝"), l1_Krypto_(l1l1111_Krypto_ (u"ࠩࡳࡥࡸࡹࡷࡰࡴࡧࠫ⌞"), l1ll11ll1l1l_Krypto_.encode(l1l1111_Krypto_ (u"ࠪࡹࡹ࡬࠸ࠨ⌟"))))
        assert l1ll1l1l11ll_Krypto_ == l1ll11ll1l1l_Krypto_.encode(l1l1111_Krypto_ (u"ࠫࡺࡺࡦ࠹ࠩ⌠")), l1ll1l1l11ll_Krypto_
    def l1ll11ll11ll_Krypto_(self):
        key = l1l1l11l11_Krypto_(l1l1111_Krypto_ (u"ࡧ࠭ࡰࡢࡵࡶࡻࡴࡸࡤࠨ⌡"), l1l1111_Krypto_ (u"ࡨࠧࡴࡣ࡯ࡸࠬ⌢"))
        assert key == l1l1111_Krypto_ (u"ࡢࠨࡰ࡟ࡼ࠽࠾࡜ࡹࡤࡨࡠࡽ࠾ࡢ࡝ࡺࡤࡨࢃࡢࡸࡢࡧ࡟ࡼ࠾ࡪ࡜ࡹ࠻ࡨࡠࡽ࠷࠰࡝ࡺࡤࡥࡡࡾ࠰࠷࡞ࡻ࠵࠷ࠪ࡜ࡹ࠲࠶ࡓࠬ⌣"), key
    def l1ll1l1lll1l_Krypto_(self):
        l1ll1l11llll_Krypto_, l1ll1l111lll_Krypto_ = _1ll11llll11_Krypto_(l1l1111_Krypto_ (u"ࠨࡲࡤࡷࡸࡽ࡯ࡳࡦࠪ⌤"), l1l1111_Krypto_ (u"ࡤࠪࡷࡦࡲࡴࠨ⌥"), 10000)
        assert l1ll1l11llll_Krypto_ != l1ll1l111lll_Krypto_
        assert l1ll1l11llll_Krypto_ == l1l1111_Krypto_ (u"ࡥࠫࡣࡢࡸࡤ࠲࠮ࡠࡽ࠿࠱࡝ࡺࡤ࠸ࡡࡾࡢ࠶࡞ࡻ࠽ࡨࡵ࡙࡝ࡺࡧࡨࡤࡢࡸࡣࡧࡏࡠࡽࡧ࠶ࡊ࡞ࡻࡩࡨࡢࡸࡦ࠶࡟ࡼ࡫ࡧ࡜ࡹ࠺࠸࡬ࡡࡾࡣࡥ࡞ࡻࡦ࠽ࡢࡸࡣࡣ࠹ࡠࡽࡩࡦࡂࡄࡱࡠࡽ࠾࠸࡝ࡺ࠳࠹ࡗ࠱ࠧ⌦"), l1ll1l11llll_Krypto_
        assert len(l1ll1l11llll_Krypto_) * 8 == 256, len(l1ll1l11llll_Krypto_)
        assert l1ll1l111lll_Krypto_ == l1l1111_Krypto_ (u"ࡦࠬࡢࡸࡢ࠶࡟ࡼࡪ࠸࡜ࡹࡣࡨࡠࡽࡧࡣ࡝ࡺ࠴࠽ࡡࡾࡡ࠵࡞ࡻ࠼࠷ࡢࡸ࠲࠷࡟ࡼ࠵࠷࡜ࡹࡥࡩࡤࡡࡾ࠹࠲ࠨ࡟ࡼࡦࡨ࡜ࡹ࠲࠴ࡠࡽࡪࡦࠦࡨ࡟ࡼ࠶࠶࡜ࡹ࠺࠶ࡠࡽࡨࡦࡧ࡞ࡻࡪ࠾ࡤࡒ࡝ࡺ࠴࠻ࡡࡾࡦࡦ࡞ࡻࡩ࠸ࡢࡸ࠲࠻࡟ࡼ࠽࠻࡜ࡹ࠲࠷ࡠࡽࡨ࠱ࠨ⌧"), l1ll1l111lll_Krypto_
        assert len(l1ll1l111lll_Krypto_) * 8 == 256, len(l1ll1l111lll_Krypto_)
    def l1ll1l1ll11l_Krypto_(self):
        l1ll1l11111l_Krypto_ = bytearray(l1_Krypto_(l1l1111_Krypto_ (u"ࠬࡶࡡࡴࡵࡺࡳࡷࡪࠧ⌨"), l1l1111_Krypto_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ〈")))
        l1ll1l11111l_Krypto_[10] = l1ll1l11111l_Krypto_[10] ^ 85
        try:
            l1lllll_Krypto_(l1l1111_Krypto_ (u"ࠧࡱࡣࡶࡷࡼࡵࡲࡥࠩ〉"), l1ll1l11111l_Krypto_)
            assert False, l1l1111_Krypto_ (u"ࠨࡧࡻࡴࡪࡩࡴࡦࡦࠣࡩࡷࡸ࡯ࡳࠩ⌫")
        except l1ll1l1llll1_Krypto_ as e:
            assert l1l1111_Krypto_ (u"ࠩࡰࡳࡩ࡯ࡦࡪࡧࡧࠫ⌬") in str(e), e
    def l1ll1l11l111_Krypto_(self):
        l1ll1l11111l_Krypto_ = bytearray(l1_Krypto_(l1l1111_Krypto_ (u"ࠪࡴࡦࡹࡳࡸࡱࡵࡨࠬ⌭"), l1l1111_Krypto_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ⌮")))
        try:
            l1lllll_Krypto_(l1l1111_Krypto_ (u"ࠬࡨࡡࡥࡲࡤࡷࡸࡽ࡯ࡳࡦࠪ⌯"), l1ll1l11111l_Krypto_)
            assert False, l1l1111_Krypto_ (u"࠭ࡥࡹࡲࡨࡧࡹ࡫ࡤࠡࡧࡵࡶࡴࡸࠧ⌰")
        except l1ll1l1llll1_Krypto_ as e:
            assert l1l1111_Krypto_ (u"ࠧࡃࡣࡧࠤࡵࡧࡳࡴࡹࡲࡶࡩ࠭⌱") in str(e), e
    def l1ll11lll1l1_Krypto_(self):
        try:
            l1_Krypto_(l1l1111_Krypto_ (u"ࠨࠩ⌲"), l1l1111_Krypto_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ⌳"))
            assert False, l1l1111_Krypto_ (u"ࠪࡩࡽࡶࡥࡤࡶࡨࡨࠥ࡫ࡲࡳࡱࡵࠫ⌴")
        except ValueError as e:
            assert l1l1111_Krypto_ (u"ࠫࡵࡧࡳࡴࡹࡲࡶࡩ࠭⌵") in str(e), e
    def l1ll1l1l1l11_Krypto_(self):
        l1ll11ll11l1_Krypto_ = l1_Krypto_(l1l1111_Krypto_ (u"ࠬࡶࡡࡴࡵࡺࡳࡷࡪࠧ⌶"), l1l1111_Krypto_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ⌷"))
        l1ll1ll111l1_Krypto_ = l1_Krypto_(l1l1111_Krypto_ (u"ࠧࡱࡣࡶࡷࡼࡵࡲࡥࠩ⌸"), l1l1111_Krypto_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⌹"))
        assert l1ll11ll11l1_Krypto_ != l1ll1ll111l1_Krypto_
    def l1ll1ll111ll_Krypto_(self):
        l1ll1l11111l_Krypto_ = l1_Krypto_(l1l1111_Krypto_ (u"ࠩࡳࡥࡸࡹࡷࡰࡴࡧࠫ⌺"), l1l1111_Krypto_ (u"ࠪࠫ⌻"))
        assert not l1lllll_Krypto_(l1l1111_Krypto_ (u"ࠫࡵࡧࡳࡴࡹࡲࡶࡩ࠭⌼"), l1ll1l11111l_Krypto_)
        try:
            l1lllll_Krypto_(l1l1111_Krypto_ (u"ࠬࡶࡡࡴࡵࡺࡳࡷࡪࠧ⌽"), bytes(bytearray(l1ll1l11111l_Krypto_)[:-1]))
            assert False, l1l1111_Krypto_ (u"࠭ࡥࡹࡲࡨࡧࡹ࡫ࡤࠡࡧࡵࡶࡴࡸࠧ⌾")
        except l1ll1l1llll1_Krypto_ as e:
            assert l1l1111_Krypto_ (u"ࠧࡎ࡫ࡶࡷ࡮ࡴࡧࠨ⌿") in str(e), e
        try:
            l1lllll_Krypto_(l1l1111_Krypto_ (u"ࠨࡲࡤࡷࡸࡽ࡯ࡳࡦࠪ⍀"), bytes(bytearray()))
            assert False, l1l1111_Krypto_ (u"ࠩࡨࡼࡵ࡫ࡣࡵࡧࡧࠤࡪࡸࡲࡰࡴࠪ⍁")
        except l1ll1l1llll1_Krypto_ as e:
            assert l1l1111_Krypto_ (u"ࠪࡑ࡮ࡹࡳࡪࡰࡪࠫ⍂") in str(e), e
    def l1ll11l1llll_Krypto_(self):
        l1ll1l11111l_Krypto_ = bytearray(l1_Krypto_(l1l1111_Krypto_ (u"ࠫࡵࡧࡳࡴࡹࡲࡶࡩ࠭⍃"), l1l1111_Krypto_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭⍄")))
        assert l1ll1l11111l_Krypto_[:l1ll1l1lllll_Krypto_] == l1ll1ll1111l_Krypto_[l1ll11lll1ll_Krypto_]
        for i in range(len(l1ll1ll1111l_Krypto_)):
            l1ll1l1l11l1_Krypto_ = bytearray(l1ll1l11111l_Krypto_)
            l1ll1l1l11l1_Krypto_[i] = 1
            try:
                _1ll1l11lll1_Krypto_(l1ll1l1l11l1_Krypto_)
                _1ll1l11ll1l_Krypto_(l1ll1l1l11l1_Krypto_)
                assert False, l1l1111_Krypto_ (u"࠭ࡥࡹࡲࡨࡧࡹ࡫ࡤࠡࡧࡵࡶࡴࡸࠧ⍅")
            except l1ll1l1llll1_Krypto_ as e:
                assert l1l1111_Krypto_ (u"ࠧࡣࡣࡧࠤ࡭࡫ࡡࡥࡧࡵࠫ⍆") in str(e), e
                if i > 1: assert l1l1111_Krypto_ (u"ࠨ࡯ࡲࡶࡪࠦࡲࡦࡥࡨࡲࡹࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡰࡨࠣࡷ࡮ࡳࡰ࡭ࡧ࠰ࡧࡷࡿࡰࡵࠩ⍇") in str(e), e
                else: assert l1l1111_Krypto_ (u"ࠩࡱࡳࡹࠦࡧࡦࡰࡨࡶࡦࡺࡥࡥࠢࡥࡽࠥࡹࡩ࡮ࡲ࡯ࡩ࠲ࡩࡲࡺࡲࡷࠫ⍈") in str(e)
        l1ll1l1l11l1_Krypto_ = bytearray(l1ll1l11111l_Krypto_)
        l1ll1l1l11l1_Krypto_[len(l1ll1ll1111l_Krypto_)] = 1
        try:
            l1lllll_Krypto_(l1l1111_Krypto_ (u"ࠪࡴࡦࡹࡳࡸࡱࡵࡨࠬ⍉"), l1ll1l1l11l1_Krypto_)
            assert False, l1l1111_Krypto_ (u"ࠫࡪࡾࡰࡦࡥࡷࡩࡩࠦࡥࡳࡴࡲࡶࠬ⍊")
        except l1ll1l1llll1_Krypto_ as e:
            assert l1l1111_Krypto_ (u"ࠬ࡬࡯ࡳ࡯ࡤࡸࠬ⍋") not in str(e), e
class l1ll1ll11111_Krypto_(l1ll1ll11ll1_Krypto_):
    def l1ll11llllll_Krypto_(self):
        l1ll1l1l11l_Krypto_ = Counter.new(8, l1llll11111_Krypto_=255, l1111l1l11l_Krypto_=False)
        try:
            l1ll1l1l11l_Krypto_()
            l1ll1l1l11l_Krypto_()
            assert False, l1l1111_Krypto_ (u"࠭ࡥࡹࡲࡨࡧࡹ࡫ࡤࠡࡧࡵࡶࡴࡸࠧ⍌")
        except Exception as e:
            assert l1l1111_Krypto_ (u"ࠧࡸࡴࡤࡴࡵ࡫ࡤࠨ⍍") in str(e), e
        l1ll1l1l11l_Krypto_ = Counter.new(8, l1llll11111_Krypto_=255, l1111l1l11l_Krypto_=True)
        l1ll1l1l11l_Krypto_()
        l1ll1l1l11l_Krypto_()
        l1ll1l1l11l_Krypto_ = Counter.new(8, l1llll11111_Krypto_=255)
        try:
            l1ll1l1l11l_Krypto_()
            l1ll1l1l11l_Krypto_()
            assert False, l1l1111_Krypto_ (u"ࠨࡧࡻࡴࡪࡩࡴࡦࡦࠣࡩࡷࡸ࡯ࡳࠩ⍎")
        except Exception as e:
            assert l1l1111_Krypto_ (u"ࠩࡺࡶࡦࡶࡰࡦࡦࠪ⍏") in str(e), e
    def l1ll1l1l1ll1_Krypto_(self):
        l1l1l111ll_Krypto_ = _1ll1l111ll1_Krypto_(l1ll1ll11lll_Krypto_[l1ll11lll1ll_Krypto_]//8)
        l1ll1l1l11l_Krypto_ = Counter.new(l1ll1l111111_Krypto_, prefix=l1l1l111ll_Krypto_[:l1ll1l111111_Krypto_//8])
        count = l1ll1l1l11l_Krypto_()
        assert len(count) == l111lll_Krypto_.block_size, count
class l1ll1l11ll11_Krypto_(l1ll1ll11ll1_Krypto_):
    def l1ll1l1l1lll_Krypto_(self):
        b = _1ll1l111ll1_Krypto_(100)
        assert len(b) == 100
        assert 0 == l1ll11llll_Krypto_(lambda x, y: x & y, bytearray(b)), b
        assert 255 == l1ll11llll_Krypto_(lambda x, y: x | y, bytearray(b)), b
    def l1ll1ll11l1l_Krypto_(self):
        b = _1ll1l111ll1_Krypto_(255*10)
        assert l1ll11llll_Krypto_(lambda a, b: a and b, (n in b for n in range(256)), True)
        b = _1ll1l111ll1_Krypto_(255)
        assert not l1ll11llll_Krypto_(lambda a, b: a and b, (n in b for n in range(256)), True)
    def l1ll1ll11l11_Krypto_(self):
        for l in range(0, 40):
            n = 100
            sum = [0 for _ in range(n)]
            for _ in range(n):
                l1ll11l1lll1_Krypto_ = _1ll1l111ll1_Krypto_(l)
                assert len(l1ll11l1lll1_Krypto_) == l
                for (i, r) in enumerate(l1ll11l1lll1_Krypto_):
                    sum[i] += r
            for i in range(l):
                l1ll1l1l1l1l_Krypto_ = sum[i] / (127.5 * n)
                assert abs(l1ll1l1l1l1l_Krypto_ - 1) < 3.3 / l1ll11lll111_Krypto_(n), l1l1111_Krypto_ (u"ࠥࡰࡪࡴࡧࡵࡪࠣࠩࡩࠦࡳࡶ࡯ࠣࠩࡩࠦࡦࡰࡴࠣࠩࡩࠦࡳࡢ࡯ࡳࡰࡪࡹࠬࠡࡰࡲࡶࡲࠦࡴࡰࠢࠨࡪࠧ⍐") % (l, sum[i], n, l1ll1l1l1l1l_Krypto_)
    def l1ll1l1ll1ll_Krypto_(self):
        l1ll11ll1111_Krypto_ = []
        for l1ll1l11l1ll_Krypto_ in range(8):
            for l in range(1, 40):
                l1ll11l1lll1_Krypto_ = _1ll1l111ll1_Krypto_(l)
                l1ll11ll1l11_Krypto_ = _1ll11ll111l_Krypto_(l1ll11l1lll1_Krypto_)
                for i in range(l):
                    for j in range(8):
                        l1ll1l1111l1_Krypto_ = bytearray(l1ll11l1lll1_Krypto_)
                        assert l1ll11ll1l11_Krypto_ == _1ll11ll111l_Krypto_(l1ll1l1111l1_Krypto_)
                        l1ll1l1111l1_Krypto_[i] ^= 2**j
                        l1l11l11ll1_Krypto_ = _1ll11ll111l_Krypto_(l1ll1l1111l1_Krypto_)
                        if l1ll11ll1l11_Krypto_ == l1l11l11ll1_Krypto_:
                            state = (l, i, j)
                            assert state not in l1ll11ll1111_Krypto_, l1l1111_Krypto_ (u"ࠦࠪࡹࠠࠦࡵࠣ࠳ࠥࠫࡳࠣ⍑") % (state, l1111l111_Krypto_(l1ll11ll1l11_Krypto_), l1111l111_Krypto_(l1l11l11ll1_Krypto_))
                            l1ll11ll1111_Krypto_.append(state)
class l1ll1l1lll11_Krypto_(l1ll1ll11ll1_Krypto_):
    def l1ll1l111l11_Krypto_(self):
        l1ll1l11111l_Krypto_ = l1l1111_Krypto_ (u"ࡧ࠭ࡳࡤ࡞ࡻ࠴࠵ࡢࡸ࠱࠲࠾ࡠࡽࡪࡦࡽࠬࡡࡠࡽࡪࡢࡌ࡞ࡻࡧࡦࡢࡸࡧࡧࡂࠩࡡࡾ࠹࠶࡞ࡻࡧ࠵ࡢࡸ࠲ࡣ࡟ࡼࡪ࠹࡜ࡳࡢ࡟ࡼ࠽࠺ࡆ࡝ࡺࡨࡧࡡࡾࡣ࠺࡞ࡻ࠼࠻ࡢࡸ࠱࠲࡟ࡼ࠾࠶࡜ࡹ࠹ࡩࡠࡽ࡫࠷࡝ࡺࡧ࠵ࡡࡾࡢࡤ࡞ࡻࡥ࠺ࡢࡸࡣ࠴࡟ࡼ࠾ࡩ࡜ࡹ࠲࠵ࡠࡽࡩ࠰࡝ࡺࡥ࠽ࡡࡾࡢ࠵࡞ࡻ࠼࠾ࡢࡸࡤ࠷࡟ࡼ࠾࠻࡜ࡹࡣ࠼ࡠࡽࡩ࠰࡝ࡰ࡟ࡼࡦࡩ࡜ࡹ࠲࠴ࡠࡽ࡫࠷࡝ࡺࡩࡦࡡࡾ࠰࠸࡫ࠥࡆࡡࡾࡢ࠶࡞ࡻࡩࡩࡐ࡜ࡹࡧ࠺ࡠࡽ࡫ࡤ࡝ࡺ࠼࠹ࠬ⍒")
        l1ll1l1l11ll_Krypto_ = l1lllll_Krypto_(l1l1111_Krypto_ (u"࠭ࡰࡢࡵࡶࡻࡴࡸࡤࠨ⍓"), l1ll1l11111l_Krypto_)
        assert l1ll1l1l11ll_Krypto_ == l1l1111_Krypto_ (u"ࡢࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⍔"), l1ll1l1l11ll_Krypto_
    def l1ll1l1ll111_Krypto_(self):
        l1ll1l11111l_Krypto_ = l1l1111_Krypto_ (u"ࡣࠩࡶࡧࡡࡾ࠰࠱࡞ࡻ࠴࠶ࡰࡘ࡝ࡺࡧࡧࡡࡾࡢࡥ࡛࡟ࡶࡦࡢࡸࡣࡨ࡟ࡼ࠽࡫࡜ࡹ࠳࠺ࡠࡽ࡫ࡣ࡝ࡺࡩࡨࡡࡾࡥࡣࡓ࡟ࡼࡦ࠶࡜ࡹࡧ࠶ࡠࡽࡩࡥ࡝ࡺ࠼ࡦࡡࡾࡥ࠵࡞ࡻࡥ࠼ࡢࡸࡣࡦ࡟ࡼ࠾ࡪ࡜ࡹ࠻ࡧࡎࡡࡾ࠱࠷࡞ࡻ࠽࠽ࡢࡸ࠲࠳ࡢࡍ࡚ࡢࡸ࠹࠴ࡏࡠࡽ࠿࠶࡝ࡺࡨ࠻ࡡࡾ࠹࠷ࡓ࡟ࡼ࠵࠷࡜ࡹ࠻࠷ࡠࡽ࡫࠶࡝ࡺࡨ࠸ࡡࡾࡥࡣ࠺࡟ࡼࡨ࠿࡜ࡹࡨ࠵ࡠࡽࡪࡤ࠽ࡶࠫࡠࡽ࡫࠰࡝ࡺࡩ࠸ࡡࡾ࠹࠷࡬ࡼࡠࡽࡩ࠹࡝ࡺࡩ࠹ࡡࡾࡣ࠶࡞ࡻࡦ࠻ࡢࡸࡢ࠲࡟ࡼࡨ࠹ࡀࡓ࡞ࡻࡨ࠼ࡢࡸ࠸ࡨ࡟ࡼࡪࡪ࡜ࡹࡥ࠳ࡁࡡࡾ࠱࠹࡞ࡻࡪࡨ࡞࡜ࡹࡨ࠳ࡠࡽ࡬࠴ࠨ⍕")
        l1ll1l1l11ll_Krypto_ = l1lllll_Krypto_(l1l1111_Krypto_ (u"ࠩࡳࡥࡸࡹࡷࡰࡴࡧࠫ⍖"), l1ll1l11111l_Krypto_)
        assert l1ll1l1l11ll_Krypto_ == l1l1111_Krypto_ (u"ࡥࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ⍗"), l1ll1l1l11ll_Krypto_
    def l1ll1l1111ll_Krypto_(self):
        l1ll1l11111l_Krypto_ = l1l1111_Krypto_ (u"ࡦࠬࡹࡣ࡝ࡺ࠳࠴ࡡࡾ࠰࠳ࡩࠬࡼࡡࡾ࠷ࡧ࡞ࡻࡦ࡫ࡢࡸࡤ࠺࡟ࡼࡪ࠻࡜ࡹࡨࡩࡠࡷࡵࡒ࡝ࡺ࠼ࡦࡡࡾ࠰ࡦࠌࠣࠤࠥࠦࠠࠡࠢࠣࡴࡹ࡫ࡸࡵࠢࡀࠤࡩ࡫ࡣࡳࡻࡳࡸ࠭࠭⍘")l1ll1l11l1l1_Krypto_ (u"ࠬ࠲ࠠࡤࡶࡨࡼࡹ࠯ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡣࡶࡷࡪࡸࡴࠡࡲࡷࡩࡽࡺࠠ࠾࠿ࠣࡦࠬ⍙")l1ll11ll1ll1_Krypto_ (u"࠭ࠬࠡࡲࡷࡩࡽࡺࠊࠋࠌࡷࡶࡾࡀࠊࠋࠢࠣࠤࠥࡻ࡮ࡪࡥࡲࡨࡪ࠮ࠩࠡࠢࠍࠎࠥࠦࠠࠡࡥ࡯ࡥࡸࡹࠠࡕࡧࡶࡸࡕࡿࡴࡩࡱࡱ࠶࠼࡙ࡹ࡯ࡶࡤࡼ࡚࠭ࡥࡴࡶࡆࡥࡸ࡫ࠩ࠻ࠌࠍࠤࠥࠦࠠࠡࠢࠣࠤࡩ࡫ࡦࠡࡶࡨࡷࡹࡥࡰࡺࡶ࡫ࡳࡳ࠸࠷ࠩࡵࡨࡰ࡫࠯࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡰࡵࡧࡻࡸࠥࡃࠠࡥࡧࡦࡶࡾࡶࡴࠩࠩ⍚")l1ll1l11l1l1_Krypto_ (u"ࠧ࠭ࠢࡨࡲࡨࡸࡹࡱࡶࠫࠫ⍛")l1ll1l11l1l1_Krypto_ (u"ࠨ࠮ࠣࠫ⍜")l1ll11ll1ll1_Krypto_ (u"ࠩࠬ࠭ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡥࡸࡹࡥࡳࡶࠣࡴࡹ࡫ࡸࡵࠢࡀࡁࠥ࠭⍝")l1ll11ll1ll1_Krypto_ (u"ࠪ࠰ࠥࡶࡴࡦࡺࡷࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡲࡷࡩࡽࡺࠠ࠾ࠢࡧࡩࡨࡸࡹࡱࡶࠫࡹࠬ⍞")l1ll1l11l1l1_Krypto_ (u"ࠫ࠱ࠦࡥ࡯ࡥࡵࡽࡵࡺࠨࡶࠩ⍟")l1ll1l11l1l1_Krypto_ (u"ࠬ࠲ࠠࡶࠩ⍠")l1ll11ll1ll1_Krypto_ (u"࠭ࠩࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡢࡵࡶࡩࡷࡺࠠࡱࡶࡨࡼࡹࠦ࠽࠾ࠢࡸࠫ⍡")l1ll11ll1ll1_Krypto_ (u"ࠧ࠭ࠢࡳࡸࡪࡾࡴࠋࠌࡨࡼࡨ࡫ࡰࡵࠢࡑࡥࡲ࡫ࡅࡳࡴࡲࡶ࠿ࠐࠊࠡࠢࠣࠤࡨࡲࡡࡴࡵࠣࡘࡪࡹࡴࡑࡻࡷ࡬ࡴࡴ࠳ࡔࡻࡱࡸࡦࡾࠨࡕࡧࡶࡸࡈࡧࡳࡦࠫ࠽ࠎࠏࠦࠠࠡࠢࠣࠤࠥࠦࡤࡦࡨࠣࡸࡪࡹࡴࡠࡲࡼࡸ࡭ࡵ࡮࠴ࠪࡶࡩࡱ࡬ࠩ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡱࡶࡨࡼࡹࠦ࠽ࠡࡦࡨࡧࡷࡿࡰࡵࠪࡥࠫ⍢")l1ll1l11l1l1_Krypto_ (u"ࠨ࠮ࠣࡩࡳࡩࡲࡺࡲࡷࠬࡧ࠭⍣")l1ll1l11l1l1_Krypto_ (u"ࠩ࠯ࠤࡧ࠭⍤")l1ll11ll1ll1_Krypto_ (u"ࠪ࠭࠮ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡦࡹࡳࡦࡴࡷࠤࡵࡺࡥࡹࡶࠣࡁࡂࠦࡢࠨ⍥")l1ll11ll1ll1_Krypto_ (u"ࠫ࠱ࠦࡰࡵࡧࡻࡸࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡴࡹ࡫ࡸࡵࠢࡀࠤࡩ࡫ࡣࡳࡻࡳࡸ࠭࠭⍦")l1ll1l11l1l1_Krypto_ (u"ࠬ࠲ࠠࡦࡰࡦࡶࡾࡶࡴࠩࠩ⍧")l1ll1l11l1l1_Krypto_ (u"࠭ࠬࠡࠩ⍨")l1ll11ll1ll1_Krypto_ (u"ࠧࠪࠫ࠱ࡨࡪࡩ࡯ࡥࡧࠫࠫ⍩")l1ll1ll1l111_Krypto_ (u"ࠨࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡣࡶࡷࡪࡸࡴࠡࡲࡷࡩࡽࡺࠠ࠾࠿ࠣࠫ⍪")l1ll11ll1ll1_Krypto_ (u"ࠩ࠯ࠤࡵࡺࡥࡹࡶࠍࠎࠏ࡯ࡦࠡࡡࡢࡲࡦࡳࡥࡠࡡࠣࡁࡂࠦࠧ⍫")__main__':
    l1ll1l11l11l_Krypto_()