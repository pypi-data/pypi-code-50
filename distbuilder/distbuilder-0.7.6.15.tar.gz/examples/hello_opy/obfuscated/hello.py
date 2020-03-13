# coding: utf-8
from sys import version_info as __11l_HelloOpy_
l1llll_HelloOpy_ = __11l_HelloOpy_[0] == 2
l1l1l_HelloOpy_ = 2048
l1111_HelloOpy_ = 7
def l11ll_HelloOpy_ (l111l_HelloOpy_):
    global l1lll1_HelloOpy_
    l11l1_HelloOpy_ = ord (l111l_HelloOpy_ [-1])
    l1ll_HelloOpy_ = l111l_HelloOpy_ [:-1]
    l1_HelloOpy_ = l11l1_HelloOpy_ % len (l1ll_HelloOpy_)
    l1ll1l_HelloOpy_ = l1ll_HelloOpy_ [:l1_HelloOpy_] + l1ll_HelloOpy_ [l1_HelloOpy_:]
    if l1llll_HelloOpy_:
        l1l1_HelloOpy_ = unicode () .join ([unichr (ord (char) - l1l1l_HelloOpy_ - (l111_HelloOpy_ + l11l1_HelloOpy_) % l1111_HelloOpy_) for l111_HelloOpy_, char in enumerate (l1ll1l_HelloOpy_)])
    else:
        l1l1_HelloOpy_ = str () .join ([chr (ord (char) - l1l1l_HelloOpy_ - (l111_HelloOpy_ + l11l1_HelloOpy_) % l1111_HelloOpy_) for l111_HelloOpy_, char in enumerate (l1ll1l_HelloOpy_)])
    return eval (l1l1_HelloOpy_)
from sys import stdout as l1l11_HelloOpy_
try:
    from tkinter import Tk as l11_HelloOpy_
except:
    from Tkinter import Tk as l11_HelloOpy_
try:
    from tkinter.ttk import Button as l1l_HelloOpy_
except:
    from ttk import Button as l1l_HelloOpy_
def l1lll_HelloOpy_():
    l1l11_HelloOpy_.write( l11ll_HelloOpy_ (u"ࠦࡍ࡫࡬࡭ࡱࠤࡠࡳࠨࠀ") )
    l1l11_HelloOpy_.l1ll1_HelloOpy_()
ll_HelloOpy_ = l11_HelloOpy_()
l1l_HelloOpy_( ll_HelloOpy_, text=l11ll_HelloOpy_ (u"ࠧࡎࡥ࡭࡮ࡲࠤ࡙ࡑࡩ࡯࡭ࡷࡩࡷࠨࠁ"), command=l1lll_HelloOpy_ ).grid()
ll_HelloOpy_.mainloop()