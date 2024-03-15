from itertools import combinations
import math

def find_all_combinations(lst):
    all_combinations = list(combinations(lst, 3))
    return all_combinations

def lcm_of_combinations(lst):
    lcm_list = []
    for combination in lst:
        lcm_val = math.lcm(combination[0], math.lcm(combination[1], combination[2]))
        lcm_list.append(lcm_val)
    return lcm_list

data = list(map(int,input().split()))
result = find_all_combinations(data)
lcm_results = lcm_of_combinations(result)
print(min(lcm_results))
