import hashlib
import string
import random
from random import randrange

md5 = lambda key: hashlib.md5(key.encode('utf8')).hexdigest()
rand_hex = lambda: format(randrange(256), '02x')
rand_char = lambda: random.choice(string.ascii_letters)
get_color = lambda hash: f'#{hash[:6]}'
get_random_color = lambda: f'#{rand_hex()}{rand_hex()}{rand_hex()}'
get_random_string = lambda len=16: ''.join(rand_char() for _ in range(len))
flatten_grid = lambda grid: [x for row in grid for x in row]
odd_to_zero = lambda x: x if x % 2 == 0 else 0
filter_odd_numbers = lambda grid: [odd_to_zero(x) for x in grid]
