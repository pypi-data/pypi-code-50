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
from l111_Krypto_ import l1_Krypto_, l1lllll_Krypto_
from os.path import exists as l1llll_Krypto_
from os import unlink as l1ll1ll1lll1_Krypto_
l1ll1ll1ll1l_Krypto_ = l1l1111_Krypto_ (u"ࠨࡳࡦࡥࡵࡩࡹࠨ⋣")
l1ll1lll1111_Krypto_ = l1l1111_Krypto_ (u"ࠢࡦࡰࡦࡶࡾࡶࡴࡦࡦ࠱ࡸࡽࡺࠢ⋤")
def main():
    if l1llll_Krypto_(l1ll1lll1111_Krypto_):
        print(l1l1111_Krypto_ (u"ࠣࡴࡨࡥࡩ࡯࡮ࡨ࠰࠱࠲ࠧ⋥"))
        data = l1ll1ll1llll_Krypto_(l1ll1ll1ll1l_Krypto_, l1ll1lll1111_Krypto_)
        print(l1l1111_Krypto_ (u"ࠤࡵࡩࡦࡪࠠࠦࡵࠣࡪࡷࡵ࡭ࠡࠧࡶࠦ⋦") % (data, l1ll1lll1111_Krypto_))
        l1ll1ll1ll11_Krypto_ = int(data.split(l1l1111_Krypto_ (u"ࠥࠤࠧ⋧"))[0]) - 1
    else:
        l1ll1ll1ll11_Krypto_ = 10
    if l1ll1ll1ll11_Krypto_ > 0:
        data = l1l1111_Krypto_ (u"ࠦࠪࡪࠠࡨࡴࡨࡩࡳࠦࡢࡰࡶࡷࡰࡪࡹࠢ⋨") % l1ll1ll1ll11_Krypto_
        print(l1l1111_Krypto_ (u"ࠧࡽࡲࡪࡶ࡬ࡲ࡬࠴࠮࠯ࠤ⋩"))
        l1ll1lll111l_Krypto_(l1ll1ll1ll1l_Krypto_, l1ll1lll1111_Krypto_, data)
        print(l1l1111_Krypto_ (u"ࠨࡷࡳࡱࡷࡩࠥࠫࡳࠡࡶࡲࠤࠪࡹࠢ⋪") % (data, l1ll1lll1111_Krypto_))
    else:
        l1ll1ll1lll1_Krypto_(l1ll1lll1111_Krypto_)
        print(l1l1111_Krypto_ (u"ࠢࡥࡧ࡯ࡩࡹ࡫ࡤࠡࠧࡶࠦ⋫") % l1ll1lll1111_Krypto_)
def l1ll1ll1llll_Krypto_(l1l1l11l1l_Krypto_, filename, string=True):
    with open(filename, l1l1111_Krypto_ (u"ࠨࡴࡥࠫ⋬")) as input:
        l1ll111l_Krypto_ = input.read()
        l1ll11l1_Krypto_ = l1lllll_Krypto_(l1l1l11l1l_Krypto_, l1ll111l_Krypto_)
        if string:
            return l1ll11l1_Krypto_.decode(l1l1111_Krypto_ (u"ࠩࡸࡸ࡫࠾ࠧ⋭"))
        else:
            return l1ll11l1_Krypto_
def l1ll1lll111l_Krypto_(l1l1l11l1l_Krypto_, filename, l1ll11l1_Krypto_):
    with open(filename, l1l1111_Krypto_ (u"ࠪࡻࡧ࠭⋮")) as output:
        l1ll111l_Krypto_ = l1_Krypto_(l1l1l11l1l_Krypto_, l1ll11l1_Krypto_)
        output.write(l1ll111l_Krypto_)
if __name__ == l1l1111_Krypto_ (u"ࠫࡤࡥ࡭ࡢ࡫ࡱࡣࡤ࠭⋯"):
    main()