import itertools as it
import math 

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

results1 = list(it.permutations(notes, 4))
for result in results1:
    print(result)
    
print("4-notes melody, notes cannot repeat - it is variation without repeating - there are {} possibilities".format(
    math.factorial(len(notes))/math.factorial(len(notes) - 4)))

results2 = it.product(notes, repeat=4)
for result in results2:
    print(result)

print("4-notes melody - notes can repeat - it is variation with repeating - there are {} possibilities".format(
        pow(len(notes), 4)))