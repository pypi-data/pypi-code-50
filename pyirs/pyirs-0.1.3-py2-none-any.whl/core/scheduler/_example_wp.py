"""
# Copyright 2015 Karlsruhe Institute of Technology (KIT)
#
# This file is part of PIRS-2.
#
# PIRS-2 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PIRS-2 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

Example for WorkPlace and InputFile usage.
"""

from pirs.core.scheduler import WorkPlace, InputFile

w = WorkPlace()
i = InputFile() # for input
o = InputFile() # for output
s = InputFile() # for script that produces output (in reality it starts the code)

i.string = 'Input file 1'
i.basename = 'inp'

o.basename = 'out'

s.basename = 'scr.sh'
s.string = """#!/bin/bash -l
cat inp > out
"""
s.executable = True

w.files.append(i)
w.files.append(o)
w.files.append(s)

w.prepare()
i.string = 'Input file 2'
w.prepare()
w.run()

