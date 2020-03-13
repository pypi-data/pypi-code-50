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
__revision__ = l1l1111_Krypto_ (u"ࠦࠩࡏࡤࠥࠤខ")
import binascii as l11l111lll_Krypto_
import unittest as l1lll111111_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_ import l11llllll11_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
l1ll11lllll_Krypto_ = [(l1l1111_Krypto_ (u"ࠬࡋࡂ࠴࠵ࡉ࠻࠼ࡋࡅ࠸࠵ࡇ࠸࠵࠻࠳ࠨគ"), l1l1111_Krypto_ (u"࠭ࡔࡊࡆࡈࠤࡎ࡚ࡃࡉࠢࡖࡐࡔ࡝ࠠࡓࡇࡌࡒࠥࡘࡕࡍࡇࠣࡑࡔ࡚ࠧឃ")),
             (l1l1111_Krypto_ (u"ࠧࡄࡅࡄࡇ࠷ࡇࡅࡅ࠷࠼࠵࠵࠻࠶ࡃࡇ࠷ࡊ࠾࠶ࡆࡅ࠶࠷࠵ࡈ࠻࠳࠵࠹࠹࠺ࠬង"),
              l1l1111_Krypto_ (u"ࠨࡔࡄࡗࡍࠦࡂࡖࡕࡋࠤࡒࡏࡌࡌࠢࡏࡓࡔࡑࠠࡃࡃࡇࠤࡇࡘࡉࡎࠢࡄ࡚ࡎࡊࠠࡈࡃࡉࡊࠥࡈࡁࡊࡖࠣࡖࡔ࡚ࠠࡑࡑࡇࠤࡑࡕࡖࡆࠩច")),
             (l1l1111_Krypto_ (u"ࠩࡈࡊࡋ࠾࠱ࡇ࠻ࡅࡊࡇࡉ࠶࠶࠵࠸࠴࠾࠸࠰ࡄࡆࡇ࠻࠹࠷࠶ࡅࡇ࠻࠴࠵࠿ࠧឆ"),
              l1l1111_Krypto_ (u"ࠪࡘࡗࡕࡄࠡࡏࡘࡘࡊࠦࡔࡂࡋࡏࠤ࡜ࡇࡒࡎࠢࡆࡌࡆࡘࠠࡌࡑࡑࡋࠥࡎࡁࡂࡉࠣࡇࡎ࡚࡙ࠡࡄࡒࡖࡊࠦࡏࠡࡖࡈࡅࡑࠦࡁࡘࡎࠪជ"))
             ]
class l11lllll1l1_Krypto_ (l1lll111111_Krypto_.TestCase):
    def runTest (self):
        l1l1111_Krypto_ (u"ࠦࡈ࡮ࡥࡤ࡭ࠣࡧࡴࡴࡶࡦࡴࡷ࡭ࡳ࡭ࠠ࡬ࡧࡼࡷࠥࡺ࡯ࠡࡇࡱ࡫ࡱ࡯ࡳࡩࠤឈ")
        for key, words in l1ll11lllll_Krypto_:
            key=l11l111lll_Krypto_.a2b_hex(b(key))
            self.assertEqual(l11llllll11_Krypto_.l11lllll1ll_Krypto_(key), words)
class l11lllll111_Krypto_ (l1lll111111_Krypto_.TestCase):
    def runTest (self):
        l1l1111_Krypto_ (u"ࠧࡉࡨࡦࡥ࡮ࠤࡨࡵ࡮ࡷࡧࡵࡸ࡮ࡴࡧࠡࡇࡱ࡫ࡱ࡯ࡳࡩࠢࡶࡸࡷ࡯࡮ࡨࡵࠣࡸࡴࠦ࡫ࡦࡻࡶࠦញ")
        for key, words in l1ll11lllll_Krypto_:
            key=l11l111lll_Krypto_.a2b_hex(b(key))
            self.assertEqual(l11llllll11_Krypto_.l11lllll11l_Krypto_(words), key)
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    return [l11lllll1l1_Krypto_(), l11lllll111_Krypto_()]
if __name__ == l1l1111_Krypto_ (u"ࠨ࡟ࡠ࡯ࡤ࡭ࡳࡥ࡟ࠣដ"):
    l1lll111111_Krypto_.main()