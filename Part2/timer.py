######################
# Small file to hold timer function
######################

import time 

# when called, this function returns current sys time
# in microseconds
current_micro_time = lambda: time.time() * 1000000
