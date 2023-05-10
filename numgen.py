# Module numgen
# Berisi fungsi untuk mendapatkan angka acak (random number)
# KAMUS
    # seed : integer
# ALGORITMA
from time import time
seed = int(time()) 
# seed bergantung waktu agar terus berubah

# B01 - Random Number Generator
# function randomize(lower_bound : integer, upper_bound : integer ) -> integer
# Mengembalikan angka random dengan algoritma Linear Congruential Generator (LCG).
def randomize(lower_bound : int, upper_bound : int) -> int:
    # KAMUS LOKAL:
        #const a : integer = 1583458089
        # const b : integer = 1132489760
        # m : integer
    # ALGORITMA
    a = 1583458089
    b = 1132489760
    m = (2**31) - 1
    global seed
    seed = (a*seed + b) % m
    while seed % (upper_bound + 1) < lower_bound:
        seed = (a*seed + b) % m
    return seed % (upper_bound + 1)