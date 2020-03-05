#!python
# -*- coding:utf-8 -*-
import os

"""
Author:Noboru Yamamoto, KEK, Japan (c) 2009-2020

contact info: http://gofer.kek.jp/
or https://plus.google.com/i/xW1BWwWsj3s:2rbmfOGOM4c

Thanks to:
   Dr. Shuei Yamada(KEK, Japan) for improved vxi11scan.py

Revision Info:
$Author: noboru $
$Date: 2020-02-28 14:20:48 +0900 $
$Header: /Users/noboru/src/python/VXI11/PyVXI11-Current/cVXI11_revision.py,v 30a63ece63a8 2020/02/28 05:20:48 noboru $
$Id: cVXI11_revision.py,v 30a63ece63a8 2020/02/28 05:20:48 noboru $
$RCSfile: setup.py,v $
$Revision: 30a63ece63a8 $
$Source: /Users/noboru/src/python/VXI11/PyVXI11-Current/cVXI11_revision.py,v $
"""

# macros managedd by mercurial keyword extension
HGTag="$HGTag: 1.15.18-30a63ece63a8 $"
HGdate="$HGdate: Fri, 28 Feb 2020 14:20:48 +0900 $"
#HGTagShort="$HGTagShort: 1.15.18 $"
from hgstamp import HGTagShort
HGlastlog="$lastlog: release $"

CVSAuthor="$Author: noboru $"
CVSDate="$Date: 2020-02-28 14:20:48 +0900 $"
CVSRev="$Revision: 30a63ece63a8 $"
CVSSource="$Header: /Users/noboru/src/python/VXI11/PyVXI11-Current/cVXI11_revision.py,v 30a63ece63a8 2020/02/28 05:20:48 noboru $"
CVSFile="$Source: /Users/noboru/src/python/VXI11/PyVXI11-Current/cVXI11_revision.py,v $"
CVSId="$Id: cVXI11_revision.py,v 30a63ece63a8 2020/02/28 05:20:48 noboru $"
#
#

rev=HGTag[HGTag.index(":")+1:HGTag.index("-")].strip()
