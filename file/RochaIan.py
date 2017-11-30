print('Enter a number and i will double it: ')
x=int(input())

if x%2==0:
    print('This number is even')
else:
    print('This number is odd')

def double(x):
    y = 2*x
    return y

print('Your new number is: ' + str(double(x)))


print('Now let\'s draw a square. How big should this square be? ')
y=int(input())

def square(y):
    import turtle
    bob=turtle.Turtle()
    bob.forward(y)
    bob.right(90)
    bob.forward(y)
    bob.right(90)
    bob.forward(y)
    bob.right(90)
    bob.forward(y)

square(y)
