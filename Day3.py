print('''Day3 List \n \n ''')

example = [1, 2, 3]
print(example)

xample1 = ['cat', 'bat', 'rat', 'elephant']
print(example1)

example2 = ['hello', 3.4452, True, None, 42]
print(example2)

spam  = ['cat', 'bat', 'rat', 'elephant']
print(spam[0])
print(spam[1])
print(spam[2])
print(spam[3])

print('Hello ' + spam[0])

print(f"The {spam[1]}  ate the {spam[0]}")

print(spam[20000])
print(spam[int(1.0)])

spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]

print(spam[0])
print(spam[0][0])
print(spam[1][4])

print(spam[-1])
print(spam[-3])

print(f"The {spam[-1]} is afraid  of the {spam[-3]}.")

print(spam[0:4])
rint(spam[1:3])
print(spam[0:-1])

print(spam[:2])
print(spam[1:])
print(spam[:])

spam = ['cat', 'dog', 'mouse']

print(len(spam))

spam  = ['cat', 'bat', 'rat', 'elephant']

spam[1] = 'aakash'

print(spam)

spam[2] = spam[1]

print(spam)
spam[-1] = 12345
print(spam)

mix = [1, 2, 3] + ['a', 'b', 'c']
print(mix)
mix2 = ['X', 'Y', 'Z']  * 3
print(mix2)
spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
print(spam)

del  spam[2]
print(spam)

del  spam[2]

print(spam)

catName1 = input('Enter the name of cat 1:\n')
catName2 = input('Enter the name of cat 2:\n')
catName3 = input('Enter the name of cat 3:\n')
catName4 = input('Enter the name of cat 4:\n')
catName5 = input('Enter the name of cat 5:\n')
catName6 = input('Enter the name of cat 6:\n')

print('The cats names are: 'f'{catName1} {catName2} {catName3} {catName4} {catName5} {catName6} ')


carNames = []
while True:
    name = input(f"Enter the name of cat {str(len(carNames) + 1)} (or enter nothing to stop.); ")
    if name == '':
        break
    carNames = carNames + [name]
print('The cat name are; ')
for name in carNames:
    print('  ' + name)
