from rand import Random

NUMBER_OF_PAIRS = 100000

class Main:
    def main(self):
        r = Random()
        print( r.get_keys_and_values(NUMBER_OF_PAIRS) )

if __name__ == '__main__':
    m = Main()
    m.main()
