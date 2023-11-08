#!/usr/bin/env python

import sys
import re
import urllib.request


def usage():
    sys.stderr.write(f'usage: {sys.argv[0]} <node-ver: 18 or 20>')
    sys.exit(1)
def node_version_fetch(url, src_re):
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')
        return src_re.search(html)
try:
    node_ver = sys.argv[1]
except (IndexError):
    usage()
nver_src_mo = node_version_fetch(
    f'https://nodejs.org/download/release/latest-v{node_ver}.x/',
    re.compile(f'node-v{node_ver}\.(\d+)\.(\d+)\.tar\.gz', re.M)
)
node_full_ver = f'{node_ver}.{nver_src_mo.group(1)}.{nver_src_mo.group(2)}'
print(node_full_ver)
