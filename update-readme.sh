#!/usr/bin/sh
< setup.py sed -e '1,/"""$/d;/^"""/,$d' > README.rst
