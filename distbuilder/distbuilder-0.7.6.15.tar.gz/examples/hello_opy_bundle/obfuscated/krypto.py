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
from sys import stdout as l11111_Krypto_,argv as l1ll1ll_Krypto_
from os.path import normpath as l1lll1_Krypto_,join as l1l1l_Krypto_,dirname as l1ll1l_Krypto_,realpath as l11l11_Krypto_,exists as l1llll_Krypto_
import traceback as l111l_Krypto_
from six import PY2 as l1ll111_Krypto_
from future.moves.configparser import RawConfigParser as l11ll_Krypto_
import argparse as l1lll1l_Krypto_
import l111_Krypto_
l1l11l1_Krypto_ = l1ll1l_Krypto_( l11l11_Krypto_( l1ll1ll_Krypto_[0] ) )
l11l1l_Krypto_ = l1l1111_Krypto_ (u"ࠦࡰࡸࡹࡱࡶࡲ࠲࡮ࡴࡩࠣࠀ")
l1l1ll1_Krypto_      = l1l1111_Krypto_ (u"ࠧࡪࡥࡧࡣࡸࡰࡹࠨࠁ")
l11_Krypto_         = l1l1111_Krypto_ (u"ࠨࡵࡵࡨ࠰࠼ࠧࠂ")
def main():
    try :
        l1l111_Krypto_, l1llll1_Krypto_, l111ll_Krypto_, l1ll_Krypto_, l1l11l_Krypto_ = l1111l_Krypto_()
        l1l1ll_Krypto_, l1l1_Krypto_ = l1ll1_Krypto_( l111ll_Krypto_ )
        if not l1l11l_Krypto_ and l1llll_Krypto_( l1llll1_Krypto_ ):
            raise Exception(
                l1l1111_Krypto_ (u"ࠢࡅࡧࡶࡸ࡮ࡴࡡࡵ࡫ࡲࡲࠥ࡬ࡩ࡭ࡧࠣࡩࡽ࡯ࡳࡵࡵࠤࠤ࡚ࡹࡥࠡࡱࡹࡩࡷࡽࡲࡪࡶࡨࠤࡸࡽࡩࡵࡥ࡫ࠤ࠭࠳࡯ࠪࠢࡷࡳࠥࡧ࡬࡭ࡱࡺ࠲࠳࠴ࠢࠃ") )
        l11111_Krypto_.write( l1l1111_Krypto_ (u"ࠣࡒࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫࠳࠴࠮ࠣࠄ") )
        with open( l1l111_Krypto_,  l1l1111_Krypto_ (u"ࠩࡵࡦࠬࠅ") ) as l1l1l1l_Krypto_: l111l1_Krypto_ = l1l1l1l_Krypto_.read()
        l11lll_Krypto_ = ( l1l1l1_Krypto_( l111l1_Krypto_, l1l1ll_Krypto_, l1l1_Krypto_ ) if l1ll_Krypto_ else
                     l1ll11l_Krypto_( l111l1_Krypto_, l1l1ll_Krypto_, l1l1_Krypto_ ) )
        with open( l1llll1_Krypto_, l1l1111_Krypto_ (u"ࠪࡻࡧ࠭ࠆ") ) as l1ll11_Krypto_: l1ll11_Krypto_.write( l11lll_Krypto_ )
        l11111_Krypto_.write( l1l1111_Krypto_ (u"ࠦࡘࡻࡣࡤࡧࡶࡷࠦࠨࠇ") )
    except : l111l_Krypto_.print_exc()
def l1111l_Krypto_():
    parser = l1lll1l_Krypto_.ArgumentParser(
        description=l1l1111_Krypto_ (u"ࠧࡑࡒ࡚ࡒࡗࡓ࠿ࠦࡓࡪ࡯ࡳࡰࡪࠦࡓࡺ࡯ࡰࡩࡹࡸࡩࡤࠢࡈࡲࡨࡸࡹࡱࡶ࡬ࡳࡳࠦࡕࡵ࡫࡯࡭ࡹࡿࠢࠈ") )
    parser.add_argument( l1l1111_Krypto_ (u"ࠨࡳࡤࡴࡓࡥࡹ࡮ࠢࠉ"),  help=l1l1111_Krypto_ (u"ࠢࡱࡣࡷ࡬ࠥࡺ࡯ࠡࡵࡲࡹࡷࡩࡥࠡࡨ࡬ࡰࡪࠨࠊ") )
    parser.add_argument( l1l1111_Krypto_ (u"ࠣࡦࡨࡷࡹࡖࡡࡵࡪࠥࠋ"), help=l1l1111_Krypto_ (u"ࠤࡳࡥࡹ࡮ࠠࡵࡱࠣࡨࡪࡹࡴࡪࡰࡤࡸ࡮ࡵ࡮ࠡࡨ࡬ࡰࡪࠨࠌ") )
    parser.add_argument( l1l1111_Krypto_ (u"ࠥ࠱ࡨࠨࠍ"), l1l1111_Krypto_ (u"ࠦ࠲࠳ࡣࡰࡰࡩ࡭࡬ࡖࡡࡵࡪࠥࠎ"),
        help=l1l1111_Krypto_ (u"ࠧ࠮࡯ࡱࡶ࡬ࡳࡳࡧ࡬ࠪࠢࡳࡥࡹ࡮ࠠࡵࡱࠣࡧࡴࡴࡦࡪࡩࠣࡪ࡮ࡲࡥࠡࠪࡧࡩ࡫ࡧࡵ࡭ࡶࡶࠤࡹࡵࠠࡢࡦ࡭ࡥࡨ࡫࡮ࡵࠢࠨࡷ࠮ࠨࠏ")
            % (l11l1l_Krypto_,) )
    parser.add_argument( l1l1111_Krypto_ (u"࠭࠭ࡥࠩࠐ"), l1l1111_Krypto_ (u"ࠢ࠮࠯ࡧࡩࡨࡸࡹࡱࡶࠥࠑ"), default=False, action=l1l1111_Krypto_ (u"ࠨࡵࡷࡳࡷ࡫࡟ࡵࡴࡸࡩࠬࠒ"),
        help=l1l1111_Krypto_ (u"ࠤࠫࡳࡵࡺࡩࡰࡰࡤࡰ࠮ࠦࡤࡦࡥࡵࡽࡵࡺࠠࡴࡹ࡬ࡸࡨ࡮ࠠࠩࡦࡨࡪࡦࡻ࡬ࡵࡵࠣࡸࡴࠦࡥ࡯ࡥࡵࡽࡵࡺࠩࠣࠓ") )
    parser.add_argument( l1l1111_Krypto_ (u"ࠪ࠱ࡴ࠭ࠔ"), l1l1111_Krypto_ (u"ࠦ࠲࠳࡯ࡷࡧࡵࡻࡷ࡯ࡴࡦࠤࠕ"), default=False, action=l1l1111_Krypto_ (u"ࠬࡹࡴࡰࡴࡨࡣࡹࡸࡵࡦࠩࠖ"),
        help=l1l1111_Krypto_ (u"ࠨࠨࡰࡲࡷ࡭ࡴࡴࡡ࡭ࠫࠣࡳࡻ࡫ࡲࡸࡴ࡬ࡸࡪࠦࡳࡸ࡫ࡷࡧ࡭ࠦࠨࡵࡱࠣࡥࡱࡲ࡯ࡸࠢࡧࡩࡸࡺࡩ࡯ࡣࡷ࡭ࡴࡴࠠࡰࡸࡨࡶࡼࡸࡩࡵࡧࠬࠦࠗ") )
    args = vars(parser.parse_args())
    return ( l1lll1_Krypto_(args.get(l1l1111_Krypto_ (u"ࠢࡴࡥࡵࡔࡦࡺࡨࠣ࠘"))), l1lll1_Krypto_(args.get(l1l1111_Krypto_ (u"ࠣࡦࡨࡷࡹࡖࡡࡵࡪࠥ࠙"))),
             args.get(l1l1111_Krypto_ (u"ࠤࡦࡳࡳ࡬ࡩࡨࡒࡤࡸ࡭ࠨࠚ")), args.get(l1l1111_Krypto_ (u"ࠥࡨࡪࡩࡲࡺࡲࡷࠦࠛ")), args.get(l1l1111_Krypto_ (u"ࠦࡴࡼࡥࡳࡹࡵ࡭ࡹ࡫ࠢࠜ")) )
def l1ll1_Krypto_( l111ll_Krypto_=None ):
    parser = l11ll_Krypto_()
    l111ll_Krypto_ = ( l1l1l_Krypto_( l1l11l1_Krypto_, l11l1l_Krypto_ )
                   if l111ll_Krypto_ is None else
                   l1lll1_Krypto_( l111ll_Krypto_ ) )
    parser.read( l111ll_Krypto_ )
    l1l1ll_Krypto_ = parser.get( l1l1ll1_Krypto_, l1l1111_Krypto_ (u"ࠧࡱࡥࡺࠤࠝ") )
    try:    l1l1_Krypto_ = parser.get( l1l1ll1_Krypto_, l1l1111_Krypto_ (u"ࠨࡥ࡯ࡥࡲࡨ࡮ࡴࡧࠣࠞ") )
    except: l1l1_Krypto_ = l11_Krypto_
    return ( l1l1ll_Krypto_, l1l1_Krypto_ )
def l1ll11l_Krypto_( ll_Krypto_, l1l1ll_Krypto_, l1l1_Krypto_ ) :
    if l1ll111_Krypto_ : ll_Krypto_ = ll_Krypto_.encode( l1l1_Krypto_ )
    return l111_Krypto_.l1_Krypto_( l1l1ll_Krypto_, ll_Krypto_ )
def l1l1l1_Krypto_( l1lll11_Krypto_, l1l1ll_Krypto_, l1l1_Krypto_ ) :
    ll_Krypto_ = l111_Krypto_.l1lllll_Krypto_( l1l1ll_Krypto_, l1lll11_Krypto_ )
    if l1ll111_Krypto_ : ll_Krypto_ = ll_Krypto_.decode( l1l1_Krypto_ )
    return ll_Krypto_
if __name__ == l1l1111_Krypto_ (u"ࠢࡠࡡࡰࡥ࡮ࡴ࡟ࡠࠤࠟ") : main()