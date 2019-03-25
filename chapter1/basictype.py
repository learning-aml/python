x = 3
print(type(x))

print(x)

t = True
print(type(t))
print(t and False)
print(t or False)

hello = "hello"
world = "workd"
print(hello)
print(len(hello))
print(hello + ' ' + world)
hw = '%s %s %d' % (hello, world, 12)
print(hw)

s = "hello"
print(s.upper())
print(s.replace('l', 'tll'))

xs = [1, 2, 4, 5]
print(xs)
print(xs[0])
print(xs[-1])
xs.append('test')
print(xs)
print(xs.pop())
print(xs)

nums = range(5)
print(nums)
print(nums[2:4])
print(nums[:-1])

animinals = ["cat", "dog", "monkey"]
for animal in animinals:
    print(animal)

    for idx1, animal in enumerate(animinals):
        print('#%d: %s' % (idx1 + 1, animal))

nums = [0, 1, 2, 3, 4]
even_squares = [x**2 for x in nums if x % 2 == 0]
print(even_squares)

dicts = {'cat': 'cute', 'dog': 'fucn'}
print(dicts['cat'])
print('cat' in dicts)
dicts['dd'] = 'dd'
print(dicts)
print(dicts['dd'])
print(dicts.get('dds', "N/A"))
del dicts['dd']
print(dicts)

for animal, legs in dicts.items():
    print(animal, legs)

d = {(x, x + 1): x for x in range(10)}  # Create a dictionary with tuple keys
t = (5, 6)  # Create a tuple
print(type(t))  # Prints "<type 'tuple'>"
print(d[t])  # Prints "5"
print(d[(1, 2)])  # Prints "1"
