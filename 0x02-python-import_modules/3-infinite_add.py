#!/usr/bin/env python3

import sys

args = sys.argv[1:]

# Convert arguments to integers and sum them up
result = sum(int(arg) for arg in args)

# Print the result followed by a new line
print(result)
