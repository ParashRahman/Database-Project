#!/usr/bin/python2

from main import Main
import sys

# argv[1] should be an element of the set: { btree, hash, indexfile }

m = Main(sys.argv[1])
m.start_application()

