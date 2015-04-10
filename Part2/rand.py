######################
# Random class helps generate 
# the random key value pairs
######################

import random

SEED = 10000

class Random:
    def get_random(self):
        return random.randint(0, 63)

    def get_random_char(self):
        return chr(97 + random.randint(0, 25))

    def get_keys_and_values(self, size = 100000):
        random.seed(SEED)
        return_tuples = []
        for index in xrange(size):
            krng = 64 + self.get_random()
            key = ""
            for i in xrange(krng):
                key += str(self.get_random_char())
            vrng = 64 + self.get_random()
            value = ""
            for i in xrange(vrng):
                value += str(self.get_random_char())
            return_tuples.append( (key, value) )

        return return_tuples
            
