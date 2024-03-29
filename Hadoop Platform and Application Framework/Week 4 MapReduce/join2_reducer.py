#!/usr/bin/env python
import sys

last_key = None
running_total = 0
ABC_found = False


# Does not include case that records found in chan but not in num

for line in sys.stdin:
    line = line.strip()
    this_key, value = line.split("\t", 1)
    
    if this_key == last_key:
        if value == "ABC":
            ABC_found = True
        else:
            value = int(value)
            running_total += value
    else:
        if ABC_found:
            print("{0}\t{1}".format(last_key, running_total))
        if value.isdigit():
            running_total = int(value)
        else:
            running_total = 0
        last_key = this_key
        ABC_found = False
        
if this_key == last_key:
    if value == "ABC":
        print("{0}\t{1}".format(last_key, running_total))
            
    
    
