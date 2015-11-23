#! usr/bin/ env python3
# quickweather.py

import json, requests, sys

# compute location from command line args
if len(sys.argv) < 2:
    print('Usage: quickweather.py location')
