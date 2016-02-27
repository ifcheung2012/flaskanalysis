import numpy as np
import itertools


# get top `topcounts` numbers of a large amout of data list
# order by show times of these numbers
def alg_get_top_list(dataset, topcounts):
    complete = np.concatenate(dataset)
    uvals, uind = np.unique(complete, return_inverse=True)
    return uvals[np.bincount(uind).argsort()[-topcounts:]][::-1]


def gen_combinations(datalist, kind_num):
    result = []
    tmp = itertools.combinations(datalist, kind_num)
    print(tmp)
    for i in tmp:
        result.append(i)
    return result


# get random combination
def alg_getrandom_one_from_combinations(datalist=(i+1 for i in xrange(33)), kind_num=2):
    import random
    comblist = gen_combinations(datalist, kind_num)
    ran = random.choice(xrange(len(comblist)))
    return set(comblist[ran - 1])


if __name__ == '__main__':
    a1 = [['03', '04', '18', '22', '25', '29'], ['02', '04', '07', '09', '14', '29'], \
          ['06', '08', '11', '13', '17', '19'], ['04', '08', '22', '23', '27', '29'], \
          ['03', '05', '15', '22', '24', '25']]

    ar = np.array(a1, dtype=int)
    print(ar[1])
    res = alg_getrandom_one_from_combinations()
    print(res)
    comb = set(ar[1]) & set(res)
    print(comb)

