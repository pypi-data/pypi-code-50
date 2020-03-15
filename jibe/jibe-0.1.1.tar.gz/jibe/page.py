# Jibe
# A Full-Stack Pure-Python Web Framework.
# Copyright (c) 2020 Juan Pablo Caram
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from jinja2 import Template, Environment, DictLoader
from pathlib import Path

path = Path(__file__).parent.absolute()
with open(f'{path}/page.html') as f:
    html = f.read()
htmlt = Template(html)
