#
# Copyright (C) 2020 Czwl Cd
# Website: https://github.com/czwl
#
# SPDX-License-Identifier: Apache-2.0
#

import os
import stat
import sys
from pathlib import Path


def find_hgconf(path):
    path = os.path.realpath(path)
    s = os.stat(path)[stat.ST_DEV]
    ps = s
    while path != "/" and ps == s:
        parent = os.path.dirname(path)
        ps = os.stat(parent)[stat.ST_DEV]

        confpath = Path(parent) / ".hgitconf"
        if confpath.exists():
            return confpath
        if ps == s:
            path = parent
    return path
