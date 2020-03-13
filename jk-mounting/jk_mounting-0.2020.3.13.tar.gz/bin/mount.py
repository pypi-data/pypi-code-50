#!/usr/bin/env python3





import os
import sys

import jk_mounting
import jk_json
import jk_console






mounter = jk_mounting.Mounter()

interesting = []
for mi in mounter.getMountInfos2(isRegularDevice = True, isNetworkDevice=True):
	interesting.append(mi)
interesting.sort(key=lambda x: x.mountPoint)

table = jk_console.SimpleTable()
headRow = table.addRow("mount point", "device", "file system", "mode")
headRow.hlineAfterRow = True

for mi in interesting:
	table.addRow(mi.mountPoint, mi.device, mi.fsType, "r" if mi.isReadOnly else "rw")

print()
table.print()
print()






