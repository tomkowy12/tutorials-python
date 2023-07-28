import itertools

def get_factors(x):
 
    ret_list = []
    for i in range(1, x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list

def check_perfect_number(number: int) -> bool:
    return sum(get_factors(number)) == number

for item in itertools.filterfalse(lambda x: not check_perfect_number(x), range(1, 10001)):
    print(item, len(get_factors(item)))

print("*" * 50)

def check_if_has_dividers(x):
 
    for i in range(2, x):
        if x % i == 0:
            return True
    else:
        return False
    
# not optimal:
# prime_numbers = list(itertools.filterfalse(lambda x: check_if_has_dividers(x), range(1, 10000)))
# print(prime_numbers)

# print(prime_numbers[:10])

prime_numbers = itertools.islice(itertools.filterfalse(lambda x: check_if_has_dividers(x), range(10000000)), 10)
print(list(prime_numbers))
