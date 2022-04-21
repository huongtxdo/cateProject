"""
only used for testing functions, syntax
"""

import random
import datetime

timeNow = datetime.datetime.utcnow().timestamp()
random.seed(int(timeNow))
print(random.randint(0,9))