# Datetime module
# 1 import datetime
# 2 from datetime import * or
from datetime import date, datetime

# date_today = datetime.date.today()
# curr_time = datetime.datetime.now()
date_today = date.today()
curr_time = datetime.now()

print(date_today)
print(curr_time.time())

"""# Random module
from random import randint

rannum = randint(1, 6)"""
"""import random

rannum = random.randint(1, 6)
print(rannum)
"""
"""from greet import *

hello()
bye()"""

""" old way

import greet

greet.hello()
greet.bye()"""
