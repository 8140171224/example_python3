print('''Day 2  start Functions\n\n\n''')

def hello():
    print('Aakash, Padhiyar')
   print('Dhaval, Padhiyar')
   print('Ashok, Padhiyar!!!')

hello()
hello()
hello()

def hello(name):
    print('Hello ' + name)

hello('aakash')
hello('dhaval')

import random
def getAnswer(answerNumber):

    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

print(getAnswer(random.randint(1, 9)))

spam = print('Hello')

None == spam

print('Hello', end=' me ')
print('World')

print('cats', 'dogs', 'mice', sep=',')


def spam():
    eggs = 31337
spam()
print(spam(eggs))

def spam():
    eggs = 99
    bacon()
    print(eggs)
def bacon():
    ham = 101
    eggs = 0
spam()

def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)


def spam():
    eggs = 'spam local'
    print(eggs)
def bacon():

    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)
eggs = 'global'
bacon()
print(eggs)

def spam():
    global eggs
    eggs = 'spam'
eggs = 'global'
spam()
print(eggs)


def spam():
    global eggs
    eggs = 'spam'
def bacon():
    eggs = 'bacon'
def ham():
    print(eggs)
eggs = 42
spam()
print(eggs)


def spam():
    print(eggs)
    eggs = spam()

eggs = 'global'
spam()

def spam(divideBy):
    return 42 / divideBy

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

def spam(divideBy):
    return 42 / divideBy
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error : Invalid argument.')

import random

secretNumber = random.randint(1, 20)
print('I am thinking od a number between 1 to 20')

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break

if guess == secretNumber:
    print('Good job! You Guessed my number in ' + str(guessesTaken) + ' guesses!')

else:
    print('Nope. The number I was thinking os was '+ str(secretNumber) )


