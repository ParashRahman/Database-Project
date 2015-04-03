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
        for index in range(size):
            krng = 64 + self.get_random()
            key = ""
            for i in range(krng):
                key += str(self.get_random_char())
            vrng = 64 + self.get_random()
            value = ""
            for i in range(vrng):
                value += str(self.get_random_char())
            return_tuples.append( (key, value) )

        return return_tuples
            
