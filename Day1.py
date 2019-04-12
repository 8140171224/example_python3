print(42 == 42)
print(42==99)
print(2!=5)
print(2!=2)
print('hello' == 'hello')
print('hello' == 'Hello')
print('dog' != 'cat')
print(True == True)
print(True != False)
print(42 == 42.0)
print(42 == '42')
print(42 < 100)
print(42 > 100)
eggCount = 42
print(eggCount <= 42)
my_age = 20
print(my_age >= 10)
print(True and True)
print(True and False)
print(False or True)
print(False or False)
print(not True)
print(not not not not True)
print((4 < 5) and (5 < 6))
print((4 < 5) and (9 < 6))
print((1==2) or (2==2))
name = input("username \n")
password = input("password \n")
if name == 'aakash':

    print(f"Hello {name}")
if password == 'Padhiyar':
    print("access granted")

else:
    print("wrong password.")

name = input('username \n')
age = int(input('enter your keyword'))
if name == 'aakash':
    print('Hi, aakash')
elif age < 12:
    print('You are not aakash, Kiddo')
elif age > 2000:
    print('unlike you are not  , aakash is not an undead, immortal vampire')
else:
    print('your not aakash :\n')

age = int(input("what is your age : "))

name = input("What is your name : ")

mobile_number = int(input(" enter your mobile number :"))
print(f' Here is my age : {age}\n and your name {name} \n mobile number :{mobile_number} ')

spam = 0
if spam < 5:
    print('Hello,Worls!')
    spam = spam + 1


while spam < 5:
    print('Hello,World!')
    spam = spam + 1

name = ''
while name != 'aakash':
    print('Please type your name')
    name = input()
print('Thank you')

while True:
    name = input("please type your name .")
    if name == 'aakash':
        break
print('Thankyoiu')
while True :
    print('aakash  ')

while True:
    name = input('Who are you?')
    if name != 'aakash':

        continue
    password = input('HEello aakash  What is your password ?')
    if password == 'aakash1':
        break
print('Access granted')

print('My name is :')
for i in range(5):
    print(f"Jimmy Five Times ({i})")

total = 0
for num in range(101):
    total=total+num
    print(total)

print('my name is ')
i = 0
while i <= 5:
    print(f'aakash{i}')
    i=i+1
n = int(input())
i = 1
for i in range(1, n):
    print(i)
print(i+1)


n = int(input('which number t=table you want: '))
b = int(input('upto where: '))
for i in range(n, b, n):
    print(i)
print(i + n)

for i in range(5, -1, -1):
   print(i)

import random
for i in range(5):
    print(random.randint(1, 10))

import sys
hile True:
   print('Type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
    print(f'you typed {response}')

