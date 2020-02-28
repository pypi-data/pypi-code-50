#!python
# -*- coding:utf-8 -*-
import os

"""
Author:Noboru Yamamoto, KEK, Japan (c) 2009-2019

contact info: http://gofer.kek.jp/
or https://plus.google.com/i/xW1BWwWsj3s:2rbmfOGOM4c

Thanks to:
   Dr. Shuei Yamada(KEK, Japan) for improved vxi11scan.py

Revision Info:
$Author: noboru $
$Date: 2020/02/27 11:04:34 $
$Header: /Users/noboru/src/python/VXI11/PyVXI11-Current/cVXI11_revision.py,v 389447d3352a 2020/02/27 11:04:34 noboru $
$Id: cVXI11_revision.py,v 389447d3352a 2020/02/27 11:04:34 noboru $
$RCSfile: setup.py,v $
$Revision: 389447d3352a $
$Source: /Users/noboru/src/python/VXI11/PyVXI11-Current/cVXI11_revision.py,v $
"""

# macros managedd by mercurial keyword extension
HGTag="$HGTag: 1.15.10-389447d3352a $"
HGdate="$HGdate: Thu, 27 Feb 2020 20:04:34 +0900 $"
#HGTagShort="$HGTagShort: 1.15.10 $"
from hgstamp import HGTagShort
HGlastlog="$lastlog: release $"

CVSAuthor="$Author: noboru $"
CVSDate="$Date: 2020/02/27 11:04:34 $"
CVSRev="$Revision: 389447d3352a $"
CVSSource="$Header: /Users/noboru/src/python/VXI11/PyVXI11-Current/cVXI11_revision.py,v 389447d3352a 2020/02/27 11:04:34 noboru $"
CVSFile="$Source: /Users/noboru/src/python/VXI11/PyVXI11-Current/cVXI11_revision.py,v $"
CVSId="$Id: cVXI11_revision.py,v 389447d3352a 2020/02/27 11:04:34 noboru $"
#
#

rev=HGTag[HGTag.index(":")+1:HGTag.index("-")].strip()
