import itertools
import operator

# itertools.accumulate(iterable[, func])

data = [1, 2, 3, 4, 5]
result = itertools.accumulate(data, operator.mul)
for each in result:
    print(each)

print("-" * 100)

data = [1, 2, 3, 4, 5]
result = itertools.accumulate(data, max)
for each in result:
    print(each)

print("-" * 100)

# itertools.count(start=0, step=1)

for i in itertools.count(10, 3):
    print(i)
    if i > 20:
        break

print("-" * 100)

# itertools.cycle(iterable)

# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# for m in itertools.cycle(months):
#     print(m)

print("-" * 100)

# itertools.chain(*iterables)

colors_basic = ["red", "yellow", "blue"]
colors_mix = ["green", "orange", "violet"]
result = itertools.chain(colors_basic, colors_mix)
for each in result:
    print(each)

print('-" * 100')

# itertools.compress(data, selectors)

cars = ["Ford", "Opel", "Toyota", "Skoda"]
seletions = [True, False, True, False]
result = itertools.compress(cars, seletions)
for each in result:
    print(each)

print('-' * 100)
# itertools.dropwhile(predicate, iterable)
# drop elements while one of elements will be True, then get all
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
result = itertools.dropwhile(lambda x: x<5, data)
for each in result:
    print(each)

print('-' * 100)

# itertools.filterfalse(predicate, iterable)
# get all that fulfill condition
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
result = itertools.filterfalse(lambda x: x<5, data)
for each in result:
    print(each)

print('-' * 100)
# itertools.islice(iterable, start, stop[, step])

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
result = itertools.islice(months, 6, 8)
for each in result:
    print(each)

print('-' * 100)
# itertools.product(iterbale, iterable)

spades = ["Hearts", "Tiles", "Clovers", "Pikes"]
figures = ["Ace", "King", "Queen", "Jack", "10", "9"]
result = itertools.product(spades, figures)
for each in result:
    print(each)

print('-' * 100)
# itertools.repeat(iterable[, times])

for i in itertools.repeat("tell mi more", 5):
    print(i)

print('-' * 100)
# itertools.starmap(function, iterable)
data = [(1,2), (3,4), (5, 6,)]
result = itertools.starmap(operator.add, data)
for each in result:
    print(each)

print('-' * 100)
# itertools.takewhile(predicate, iterable)
# take elements while one of elements will be True, then get all
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
result = itertools.takewhile(lambda x: x<5, data)
for each in result:
    print(each)

print('-' * 100)

# itertools.tee(iterable, n=2)

cars = ["Ford", "Opel", "Toyota", "Skoda"]
cars1, cars2 = itertools.tee(cars)

for each in cars1:
    print(each)
print('----')
for each in cars2:
    print(each)

print('-' * 100)

# itertools.zip_longest(*iterable, fillvalue=None)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
plan = ["busy", "busy", "busy", "busy", "busy", "busy", "free", "free"]
result = itertools.zip_longest(months, plan, fillvalue="unknown")
for each in result:
    print(each)

