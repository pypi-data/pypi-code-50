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
l1l1111_Krypto_ (u"ࠢࠣࠤࡖࡩࡱ࡬࠭ࡵࡧࡶࡸࡸࠦࡦࡰࡴࠣࡇࡷࡿࡰࡵࡱ࠱࡙ࡹ࡯࡬࠯ࡣࡶࡲ࠶ࠨࠢࠣ᥼")
__revision__ = l1l1111_Krypto_ (u"ࠣࠦࡌࡨࠩࠨ᥽")
import unittest as l1lll111111_Krypto_
import sys as l1l11l11_Krypto_
from l111ll1_Krypto_.l1l111ll_Krypto_.l1l11ll1_Krypto_ import *
from l111ll1_Krypto_.l1l111ll_Krypto_.l11l1lll1l_Krypto_ import l11l11llll_Krypto_, l11l1ll1ll_Krypto_
class l111l111ll1_Krypto_(l1lll111111_Krypto_.TestCase):
	def l111l111l11_Krypto_(self):
		l11l1l111l_Krypto_ = l11l1ll1ll_Krypto_(b(l1l1111_Krypto_ (u"ࠩ࡟ࡼ࠸࠹ࠧ᥾")))
		self.assertEqual(l11l1l111l_Krypto_.encode(), b(l1l1111_Krypto_ (u"ࠪࡠࡽ࠹࠳࡝ࡺ࠳࠴ࠬ᥿")))
		l11l1l111l_Krypto_.payload = b(l1l1111_Krypto_ (u"ࠫࡡࡾ࠴࠶ࠩᦀ"))
		self.assertEqual(l11l1l111l_Krypto_.encode(), b(l1l1111_Krypto_ (u"ࠬࡢࡸ࠴࠵࡟ࡼ࠵࠷࡜ࡹ࠶࠸ࠫᦁ")))
		self.assertEqual(l11l1l111l_Krypto_.encode(), b(l1l1111_Krypto_ (u"࠭࡜ࡹ࠵࠶ࡠࡽ࠶࠱࡝ࡺ࠷࠹ࠬᦂ")))
		l11l1l111l_Krypto_ = l11l1ll1ll_Krypto_(b(0x33))
		l11l1l111l_Krypto_.payload = b(l1l1111_Krypto_ (u"ࠧ࡝ࡺ࠷࠹ࠬᦃ"))
		self.assertEqual(l11l1l111l_Krypto_.encode(), b(l1l1111_Krypto_ (u"ࠨ࡞ࡻ࠷࠸ࡢࡸ࠱࠳࡟ࡼ࠹࠻ࠧᦄ")))
	def l111l11l11l_Krypto_(self):
		l11l1l111l_Krypto_ = l11l1ll1ll_Krypto_(l1l1111_Krypto_ (u"ࠩࡖࡉࡖ࡛ࡅࡏࡅࡈࠫᦅ"))
		self.assertEqual(l11l1l111l_Krypto_.encode(), b(l1l1111_Krypto_ (u"ࠪࡠࡽ࠹࠰࡝ࡺ࠳࠴ࠬᦆ")))
		l11l1l111l_Krypto_ = l11l1ll1ll_Krypto_(l1l1111_Krypto_ (u"ࠫࡇࡏࡔࠡࡕࡗࡖࡎࡔࡇࠨᦇ"))
		self.assertEqual(l11l1l111l_Krypto_.encode(), b(l1l1111_Krypto_ (u"ࠬࡢࡸ࠱࠵࡟ࡼ࠵࠶ࠧᦈ")))
	def l1111ll111l_Krypto_(self):
		l11l1l111l_Krypto_ = l11l1ll1ll_Krypto_(b(l1l1111_Krypto_ (u"࠭࡜ࡹ࠵࠷ࠫᦉ")))
		l11l1l111l_Krypto_.payload = b(l1l1111_Krypto_ (u"ࠢ࠱ࠤᦊ"))*128
		self.assertEqual(l11l1l111l_Krypto_.encode(), b(l1l1111_Krypto_ (u"ࠨ࡞ࡻ࠷࠹ࡢࡸ࠹࠳࡟ࡼ࠽࠶ࠧᦋ") + l1l1111_Krypto_ (u"ࠤ࠳ࠦᦌ")*128))
	def l1111lll11l_Krypto_(self):
		l11l1l111l_Krypto_ = l11l1ll1ll_Krypto_()
		l11l1l111l_Krypto_.decode(b(l1l1111_Krypto_ (u"ࠪࡠࡽ࠸࠰࡝ࡺ࠳࠶ࡡࡾ࠰࠲࡞ࡻ࠴࠷࠭ᦍ")))
		self.assertEqual(l11l1l111l_Krypto_.payload, b(l1l1111_Krypto_ (u"ࠦࡡࡾ࠰࠲࡞ࡻ࠴࠷ࠨᦎ")))
		self.assertEqual(l11l1l111l_Krypto_.l111l1111ll_Krypto_, 0x20)
	def l1111lll1l1_Krypto_(self):
		l11l1l111l_Krypto_ = l11l1ll1ll_Krypto_()
		l11l1l111l_Krypto_.decode(b(l1l1111_Krypto_ (u"ࠬࡢࡸ࠳࠴࡟ࡼ࠽࠷࡜ࡹ࠺࠳ࠫᦏ") + l1l1111_Krypto_ (u"ࠨ࠱ࠣᦐ")*128))
		self.assertEqual(l11l1l111l_Krypto_.payload, b(l1l1111_Krypto_ (u"ࠢ࠲ࠤᦑ"))*128)
		self.assertEqual(l11l1l111l_Krypto_.l111l1111ll_Krypto_, 0x22)
class l1111llllll_Krypto_(l1lll111111_Krypto_.TestCase):
	def l111l11l111_Krypto_(self):
		l11l1l111l_Krypto_ = l11l11llll_Krypto_()
		self.assertEqual(l11l1l111l_Krypto_.encode(), b(l1l1111_Krypto_ (u"ࠨ࠲࡟ࡼ࠵࠶ࠧᦒ")))
		self.assertFalse(l11l1l111l_Krypto_.l11l11l11l_Krypto_())
		l11l1l111l_Krypto_.append(0)
		self.assertEqual(l11l1l111l_Krypto_.encode(), b(l1l1111_Krypto_ (u"ࠩ࠳ࡠࡽ࠶࠳࡝ࡺ࠳࠶ࡡࡾ࠰࠲࡞ࡻ࠴࠵࠭ᦓ")))
		self.assertTrue(l11l1l111l_Krypto_.l11l11l11l_Krypto_())
		self.assertEqual(l11l1l111l_Krypto_.encode(), b(l1l1111_Krypto_ (u"ࠪ࠴ࡡࡾ࠰࠴࡞ࡻ࠴࠷ࡢࡸ࠱࠳࡟ࡼ࠵࠶ࠧᦔ")))
	def l111l111l1l_Krypto_(self):
		l11l1l111l_Krypto_ = l11l11llll_Krypto_()
		l11l1l111l_Krypto_.append(127)
		self.assertEqual(l11l1l111l_Krypto_.encode(), b(l1l1111_Krypto_ (u"ࠫ࠵ࡢࡸ࠱࠵࡟ࡼ࠵࠸࡜ࡹ࠲࠴ࡠࡽ࠽ࡦࠨᦕ")))
		l11l1l111l_Krypto_[0] = 1
		self.assertEqual(len(l11l1l111l_Krypto_),1)
		self.assertEqual(l11l1l111l_Krypto_[0],1)
		self.assertEqual(l11l1l111l_Krypto_[-1],1)
		self.assertEqual(l11l1l111l_Krypto_.encode(), b(l1l1111_Krypto_ (u"ࠬ࠶࡜ࡹ࠲࠶ࡠࡽ࠶࠲࡝ࡺ࠳࠵ࡡࡾ࠰࠲ࠩᦖ")))
		l11l1l111l_Krypto_[:] = [1]
		self.assertEqual(len(l11l1l111l_Krypto_),1)
		self.assertEqual(l11l1l111l_Krypto_[0],1)
		self.assertEqual(l11l1l111l_Krypto_.encode(), b(l1l1111_Krypto_ (u"࠭࠰࡝ࡺ࠳࠷ࡡࡾ࠰࠳࡞ࡻ࠴࠶ࡢࡸ࠱࠳ࠪᦗ")))
	def l1111lll1ll_Krypto_(self):
		l11l1l111l_Krypto_ = l11l11llll_Krypto_()
		l11l1l111l_Krypto_.append(0x180)
		self.assertEqual(l11l1l111l_Krypto_.encode(), b(l1l1111_Krypto_ (u"ࠧ࠱࡞ࡻ࠴࠹ࡢࡸ࠱࠴࡟ࡼ࠵࠸࡜ࡹ࠲࠴ࡠࡽ࠾࠰ࠨᦘ")))
	def l1111ll11l1_Krypto_(self):
		l11l1l111l_Krypto_ = l11l11llll_Krypto_()
		l11l1l111l_Krypto_.append(2**2048)
		self.assertEqual(l11l1l111l_Krypto_.encode(), b(l1l1111_Krypto_ (u"ࠨ࠲࡟ࡼ࠽࠸࡜ࡹ࠲࠴ࡠࡽ࠶࠵ࠨᦙ"))+
		b(l1l1111_Krypto_ (u"ࠩ࡟ࡼ࠵࠸࡜ࡹ࠺࠵ࡠࡽ࠶࠱࡝ࡺ࠳࠵ࡡࡾ࠰࠲࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲ࠪᦚ"))+
		b(l1l1111_Krypto_ (u"ࠪࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࠫᦛ"))+
		b(l1l1111_Krypto_ (u"ࠫࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࠬᦜ"))+
		b(l1l1111_Krypto_ (u"ࠬࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵࠭ᦝ"))+
		b(l1l1111_Krypto_ (u"࠭࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶ࠧᦞ"))+
		b(l1l1111_Krypto_ (u"ࠧ࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰ࠨᦟ"))+
		b(l1l1111_Krypto_ (u"ࠨ࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱ࠩᦠ"))+
        b(l1l1111_Krypto_ (u"ࠩ࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲ࠪᦡ"))+
		b(l1l1111_Krypto_ (u"ࠪࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࠫᦢ"))+
		b(l1l1111_Krypto_ (u"ࠫࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࠬᦣ"))+
		b(l1l1111_Krypto_ (u"ࠬࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵࠭ᦤ"))+
		b(l1l1111_Krypto_ (u"࠭࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶ࠧᦥ"))+
		b(l1l1111_Krypto_ (u"ࠧ࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰ࠨᦦ"))+
		b(l1l1111_Krypto_ (u"ࠨ࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱ࠩᦧ"))+
		b(l1l1111_Krypto_ (u"ࠩ࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲ࠪᦨ"))+
		b(l1l1111_Krypto_ (u"ࠪࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࠫᦩ"))+
		b(l1l1111_Krypto_ (u"ࠫࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࠬᦪ"))+
		b(l1l1111_Krypto_ (u"ࠬࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵࠭ᦫ"))+
		b(l1l1111_Krypto_ (u"࠭࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰ࠨ᦬")))
	def l1111ll1lll_Krypto_(self):
		l11l1l111l_Krypto_ = l11l11llll_Krypto_()
		l11l1l111l_Krypto_.append(0xFF)
		self.assertEqual(l11l1l111l_Krypto_.encode(), b(l1l1111_Krypto_ (u"ࠧ࠱࡞ࡻ࠴࠹ࡢࡸ࠱࠴࡟ࡼ࠵࠸࡜ࡹ࠲࠳ࡠࡽ࡬ࡦࠨ᦭")))
	def l1111llll11_Krypto_(self):
		l11l1l111l_Krypto_ = l11l11llll_Krypto_()
		l11l1l111l_Krypto_.append(0x180)
		l11l1l111l_Krypto_.append(0xFF)
		self.assertEqual(l11l1l111l_Krypto_.encode(), b(l1l1111_Krypto_ (u"ࠨ࠲࡟ࡼ࠵࠾࡜ࡹ࠲࠵ࡠࡽ࠶࠲࡝ࡺ࠳࠵ࡡࡾ࠸࠱࡞ࡻ࠴࠷ࡢࡸ࠱࠴࡟ࡼ࠵࠶࡜ࡹࡨࡩࠫ᦮")))
		self.assertTrue(l11l1l111l_Krypto_.l11l11l11l_Krypto_())
		l11l1l111l_Krypto_.append(0x01)
		l11l1l111l_Krypto_[1:] = [9,8]
		self.assertEqual(len(l11l1l111l_Krypto_),3)
		self.assertEqual(l11l1l111l_Krypto_[1:],[9,8])
		self.assertEqual(l11l1l111l_Krypto_[1:-1],[9])
		self.assertEqual(l11l1l111l_Krypto_.encode(), b(l1l1111_Krypto_ (u"ࠩ࠳ࡠࡽ࠶ࡁ࡝ࡺ࠳࠶ࡡࡾ࠰࠳࡞ࡻ࠴࠶ࡢࡸ࠹࠲࡟ࡼ࠵࠸࡜ࡹ࠲࠴ࡠࡽ࠶࠹࡝ࡺ࠳࠶ࡡࡾ࠰࠲࡞ࡻ࠴࠽࠭᦯")))
	def l1111llll11_Krypto_(self):
		l11l1l111l_Krypto_ = l11l11llll_Krypto_()
		l11l1l111l_Krypto_.append(0x180)
		l11l1l111l_Krypto_.append(b(l1l1111_Krypto_ (u"ࠪࡠࡽ࠶࠰࡝ࡺ࠳࠶ࡡࡾ࠰࠱࡞ࡻ࠴࠵࠭ᦰ")))
		self.assertEqual(l11l1l111l_Krypto_.encode(), b(l1l1111_Krypto_ (u"ࠫ࠵ࡢࡸ࠱࠺࡟ࡼ࠵࠸࡜ࡹ࠲࠵ࡠࡽ࠶࠱࡝ࡺ࠻࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠷ࡢࡸ࠱࠲࡟ࡼ࠵࠶ࠧᦱ")))
		self.assertFalse(l11l1l111l_Krypto_.l11l11l11l_Krypto_())
	def l111l111111_Krypto_(self):
		l11l1l111l_Krypto_ = l11l11llll_Krypto_()
		l11l1l111l_Krypto_.decode(b(l1l1111_Krypto_ (u"ࠬ࠶࡜ࡹ࠲࠳ࠫᦲ")))
		self.assertEqual(len(l11l1l111l_Krypto_),0)
		l11l1l111l_Krypto_.decode(b(l1l1111_Krypto_ (u"࠭࠰࡝ࡺ࠳࠷ࡡࡾ࠰࠳࡞ࡻ࠴࠶ࡢࡸ࠱࠲ࠪᦳ")))
		self.assertEqual(len(l11l1l111l_Krypto_),1)
		self.assertEqual(l11l1l111l_Krypto_[0],0)
		l11l1l111l_Krypto_.decode(b(l1l1111_Krypto_ (u"ࠧ࠱࡞ࡻ࠴࠸ࡢࡸ࠱࠴࡟ࡼ࠵࠷࡜ࡹ࠲࠳ࠫᦴ")))
		self.assertEqual(len(l11l1l111l_Krypto_),1)
		self.assertEqual(l11l1l111l_Krypto_[0],0)
	def l1111ll1l11_Krypto_(self):
		l11l1l111l_Krypto_ = l11l11llll_Krypto_()
		l11l1l111l_Krypto_.decode(b(l1l1111_Krypto_ (u"ࠨ࠲࡟ࡼ࠵࠹࡜ࡹ࠲࠵ࡠࡽ࠶࠱࡝ࡺ࠺ࡪࠬᦵ")))
		self.assertEqual(len(l11l1l111l_Krypto_),1)
		self.assertEqual(l11l1l111l_Krypto_[0],127)
	def l1111lll111_Krypto_(self):
		l11l1l111l_Krypto_ = l11l11llll_Krypto_()
		l11l1l111l_Krypto_.decode(b(l1l1111_Krypto_ (u"ࠩ࠳ࡠࡽ࠶࠴࡝ࡺ࠳࠶ࡡࡾ࠰࠳࡞ࡻ࠴࠶ࡢࡸ࠹࠲ࠪᦶ")))
		self.assertEqual(len(l11l1l111l_Krypto_),1)
		self.assertEqual(l11l1l111l_Krypto_[0],0x180)
	def l1111ll1ll1_Krypto_(self):
		l11l1l111l_Krypto_ = l11l11llll_Krypto_()
		l11l1l111l_Krypto_.decode(b(l1l1111_Krypto_ (u"ࠪ࠴ࡡࡾ࠸࠳࡞ࡻ࠴࠶ࡢࡸ࠱࠷ࠪᦷ"))+
		b(l1l1111_Krypto_ (u"ࠫࡡࡾ࠰࠳࡞ࡻ࠼࠷ࡢࡸ࠱࠳࡟ࡼ࠵࠷࡜ࡹ࠲࠴ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࠬᦸ"))+
		b(l1l1111_Krypto_ (u"ࠬࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵࠭ᦹ"))+
		b(l1l1111_Krypto_ (u"࠭࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶ࠧᦺ"))+
		b(l1l1111_Krypto_ (u"ࠧ࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰ࠨᦻ"))+
		b(l1l1111_Krypto_ (u"ࠨ࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱ࠩᦼ"))+
		b(l1l1111_Krypto_ (u"ࠩ࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲ࠪᦽ"))+
		b(l1l1111_Krypto_ (u"ࠪࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࠫᦾ"))+
        b(l1l1111_Krypto_ (u"ࠫࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࠬᦿ"))+
		b(l1l1111_Krypto_ (u"ࠬࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵࠭ᧀ"))+
		b(l1l1111_Krypto_ (u"࠭࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶ࠧᧁ"))+
		b(l1l1111_Krypto_ (u"ࠧ࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰ࠨᧂ"))+
		b(l1l1111_Krypto_ (u"ࠨ࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱ࠩᧃ"))+
		b(l1l1111_Krypto_ (u"ࠩ࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲ࠪᧄ"))+
		b(l1l1111_Krypto_ (u"ࠪࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࠫᧅ"))+
		b(l1l1111_Krypto_ (u"ࠫࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࠬᧆ"))+
		b(l1l1111_Krypto_ (u"ࠬࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵࠭ᧇ"))+
		b(l1l1111_Krypto_ (u"࠭࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶ࠧᧈ"))+
		b(l1l1111_Krypto_ (u"ࠧ࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰ࠨᧉ"))+
		b(l1l1111_Krypto_ (u"ࠨ࡞ࡻ࠴࠵ࡢࡸ࠱࠲࡟ࡼ࠵࠶࡜ࡹ࠲࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࡡࡾ࠰࠱࡞ࡻ࠴࠵ࡢࡸ࠱࠲ࠪ᧊")))
		self.assertEqual(len(l11l1l111l_Krypto_),1)
		self.assertEqual(l11l1l111l_Krypto_[0],2**2048)
	def l111l11111l_Krypto_(self):
		l11l1l111l_Krypto_ = l11l11llll_Krypto_()
		l11l1l111l_Krypto_.decode(b(l1l1111_Krypto_ (u"ࠩ࠳ࡠࡽ࠶࠴࡝ࡺ࠳࠶ࡡࡾ࠰࠳࡞ࡻ࠴࠵ࡢࡸࡧࡨࠪ᧋")))
		self.assertEqual(len(l11l1l111l_Krypto_),1)
		self.assertEqual(l11l1l111l_Krypto_[0],0xFF)
	def l1111lllll1_Krypto_(self):
		l11l1l111l_Krypto_ = l11l11llll_Krypto_()
		l11l1l111l_Krypto_.decode(b(l1l1111_Krypto_ (u"ࠪ࠴ࡡࡾ࠰࠹࡞ࡻ࠴࠷ࡢࡸ࠱࠴࡟ࡼ࠵࠷࡜ࡹ࠺࠳ࡠࡽ࠶࠲࡝ࡺ࠳࠶ࡡࡾ࠰࠱࡞ࡻࡪ࡫࠭᧌")))
		self.assertEqual(len(l11l1l111l_Krypto_),2)
		self.assertEqual(l11l1l111l_Krypto_[0],0x180)
		self.assertEqual(l11l1l111l_Krypto_[1],0xFF)
	def l111l111lll_Krypto_(self):
		l11l1l111l_Krypto_ = l11l11llll_Krypto_()
		l11l1l111l_Krypto_.decode(b(l1l1111_Krypto_ (u"ࠫ࠵ࡢࡸ࠱ࡃ࡟ࡼ࠵࠸࡜ࡹ࠲࠵ࡠࡽ࠶࠱࡝ࡺ࠻࠴ࡡࡾ࠲࠵࡞ࡻ࠴࠷ࡢࡸࡣ࠸࡟ࡼ࠻࠹࡜ࡹ࠳࠵ࡠࡽ࠶࠰ࠨ᧍")))
		self.assertEqual(len(l11l1l111l_Krypto_),3)
		self.assertEqual(l11l1l111l_Krypto_[0],0x180)
		self.assertEqual(l11l1l111l_Krypto_[1],b(l1l1111_Krypto_ (u"ࠬࡢࡸ࠳࠶࡟ࡼ࠵࠸࡜ࡹࡤ࠹ࡠࡽ࠼࠳ࠨ᧎")))
		self.assertEqual(l11l1l111l_Krypto_[2],b(l1l1111_Krypto_ (u"࠭࡜ࡹ࠳࠵ࡠࡽ࠶࠰ࠨ᧏")))
	def l1111ll1l1l_Krypto_(self):
		l11l1l111l_Krypto_ = l11l11llll_Krypto_()
		l11l1l111l_Krypto_.decode(b(l1l1111_Krypto_ (u"ࠧ࠱࡞ࡻ࠴࠻ࡢࡸ࠳࠶࡟ࡼ࠵࠸࡜ࡹࡤ࠹ࡠࡽ࠼࠳࡝ࡺ࠴࠶ࡡࡾ࠰࠱ࠩ᧐")))
		self.assertEqual(len(l11l1l111l_Krypto_),2)
		self.assertEqual(l11l1l111l_Krypto_[0],b(l1l1111_Krypto_ (u"ࠨ࡞ࡻ࠶࠹ࡢࡸ࠱࠴࡟ࡼࡧ࠼࡜ࡹ࠸࠶ࠫ᧑")))
		self.assertEqual(l11l1l111l_Krypto_[1],b(l1l1111_Krypto_ (u"ࠩ࡟ࡼ࠶࠸࡜ࡹ࠲࠳ࠫ᧒")))
	def l1111ll1111_Krypto_(self):
		l11l1l111l_Krypto_ = l11l11llll_Krypto_()
		self.assertRaises(ValueError, l11l1l111l_Krypto_.decode, b(l1l1111_Krypto_ (u"ࠪࠫ᧓")))
		self.assertRaises(ValueError, l11l1l111l_Krypto_.decode, b(l1l1111_Krypto_ (u"ࠫࡡࡾ࠰࠱ࠩ᧔")))
		self.assertRaises(ValueError, l11l1l111l_Krypto_.decode, b(l1l1111_Krypto_ (u"ࠬࡢࡸ࠴࠲ࠪ᧕")))
	def l1111l1llll_Krypto_(self):
		l11l1l111l_Krypto_ = l11l11llll_Krypto_()
		self.assertRaises(ValueError, l11l1l111l_Krypto_.decode, b(l1l1111_Krypto_ (u"࠭࡜ࡹ࠵࠳ࡠࡽ࠶࠰࡝ࡺ࠳࠴ࠬ᧖")), True)
	def l1111ll11ll_Krypto_(self):
		l11l1l111l_Krypto_ = l11l11llll_Krypto_()
		self.assertRaises(ValueError, l11l1l111l_Krypto_.decode, b(l1l1111_Krypto_ (u"ࠧ࡝ࡺ࠶࠴ࡡࡾ࠰࠵࡞ࡻ࠴࠷ࡢࡸ࠱࠳࡟ࡼ࠵࠷࡜ࡹ࠲࠳ࠫ᧗")))
		self.assertRaises(ValueError, l11l1l111l_Krypto_.decode, b(l1l1111_Krypto_ (u"ࠨ࡞ࡻ࠷࠵ࡢࡸ࠹࠳࡟ࡼ࠵࠹࡜ࡹ࠲࠵ࡠࡽ࠶࠱࡝ࡺ࠳࠵ࠬ᧘")))
		self.assertRaises(ValueError, l11l1l111l_Krypto_.decode, b(l1l1111_Krypto_ (u"ࠩ࡟ࡼ࠸࠶࡜ࡹ࠲࠷ࡠࡽ࠶࠲࡝ࡺ࠻࠵ࡡࡾ࠰࠲࡞ࡻ࠴࠶࠭᧙")))
	def l1111llll1l_Krypto_(self):
		l11l1l111l_Krypto_ = l11l11llll_Krypto_()
		self.assertRaises(ValueError, l11l1l111l_Krypto_.decode, b(l1l1111_Krypto_ (u"ࠪࡠࡽ࠹࠰࡝ࡺ࠳࠸ࡡࡾ࠰࠳࡞ࡻ࠴࠶ࡢࡸࡇࡈࠪ᧚")))
def l1ll1llll11_Krypto_(l1ll1lll111_Krypto_={}):
    from l111ll1_Krypto_.l1ll1lll1ll_Krypto_.l1ll1lllll1_Krypto_ import l1lll1111l1_Krypto_
    l111l1111l1_Krypto_ = []
    l111l1111l1_Krypto_ += l1lll1111l1_Krypto_(l111l111ll1_Krypto_)
    l111l1111l1_Krypto_ += l1lll1111l1_Krypto_(l1111llllll_Krypto_)
    return l111l1111l1_Krypto_
if __name__ == l1l1111_Krypto_ (u"ࠫࡤࡥ࡭ࡢ࡫ࡱࡣࡤ࠭᧛"):
    suite = lambda: l1lll111111_Krypto_.TestSuite(l1ll1llll11_Krypto_())
    l1lll111111_Krypto_.main(defaultTest=l1l1111_Krypto_ (u"ࠬࡹࡵࡪࡶࡨࠫ᧜"))