from itertools import permutations
import numpy as np

if __name__ == '__main__':
    tmp = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 0]))
    print(len(tmp))
    all_possible_variants = np.array(tmp, dtype=int)
    all_possible_variants = all_possible_variants.reshape((362880, 3, 3))
    hsh_tbl = {}
    # print(all_possible_variats)
    for i, state in enumerate(all_possible_variants):
        hsh = hash(bytes(state))
        if hsh_tbl.get(hsh) is None:
            hsh_tbl[hsh] = i
        else:
            print("error", i)
    print(max(hsh_tbl.values()))
