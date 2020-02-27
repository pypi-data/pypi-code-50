#!python
# -*- coding:utf-8 -*-
import os

"""
Author:Noboru Yamamoto, KEK, Japan (c) 2009-2013

contact info: http://gofer.kek.jp/
or https://plus.google.com/i/xW1BWwWsj3s:2rbmfOGOM4c

Thanks to:
   Dr. Shuei Yamada(KEK, Japan) for improved vxi11scan.py

Revision Info:
$Author: noboru $
$Date: 2020/02/07 09:55:59 $
$Header: /Users/noboru/src/python/VXI11/PyVXI11-Current/cVXI11_revision.py,v 43487ff44ea6 2020/02/07 09:55:59 noboru $
$Id: cVXI11_revision.py,v 43487ff44ea6 2020/02/07 09:55:59 noboru $
$RCSfile: setup.py,v $
$Revision: 43487ff44ea6 $
$Source: /Users/noboru/src/python/VXI11/PyVXI11-Current/cVXI11_revision.py,v $
"""

# macros managedd by mercurial keyword extension
HGTag="$HGTag: 1.14.12-43487ff44ea6 $"
HGdate="$HGdate: Fri, 07 Feb 2020 18:55:59 +0900 $"
HGTagShort="$HGTagShort: 1.14.12 $"
HGlastlog="$lastlog: revision update $"

CVSAuthor="$Author: noboru $"
CVSDate="$Date: 2020/02/07 09:55:59 $"
CVSRev="$Revision: 43487ff44ea6 $"
CVSSource="$Header: /Users/noboru/src/python/VXI11/PyVXI11-Current/cVXI11_revision.py,v 43487ff44ea6 2020/02/07 09:55:59 noboru $"
CVSFile="$Source: /Users/noboru/src/python/VXI11/PyVXI11-Current/cVXI11_revision.py,v $"
CVSId="$Id: cVXI11_revision.py,v 43487ff44ea6 2020/02/07 09:55:59 noboru $"
#
#

rev=HGTag[HGTag.index(":")+1:HGTag.index("-")].strip()
