import random

def random_with_sum(number_of_values, asserted_sum):
    trial = 0
    
    while True:
        numbers = []
        trial += 1
        for _ in range(0, number_of_values):
            numbers.append(random.randint(1, 100))
        if sum(numbers) == 100:
            yield((trial, numbers))
            trial = 0

for i in range(10):
    (number_of_trials, numbers) = next(random_with_sum(3, 100))
    print(number_of_trials, numbers)

print("done")