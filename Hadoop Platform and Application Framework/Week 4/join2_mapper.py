#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    key_value = line.split(",")
    
    if key_value[1][1:].isdigit():
        print("%s\t%s" % (key_value[0], key_value[1][1:]))
    else:
        if key_value[1][1:] == "ABC":
            print("%s\t%s" % (key_value[0], key_value[1][1:]))
