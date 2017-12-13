def hello():
    print('Hey do you want to go on an adventure?')
    start=input('(yes/no): ')
    return start
x = hello()

if x=='yes' or x=='Yes':
    print('Fantastic!')
    game=True
elif x=='no' or x=='No':
    print('of course....')
    game=False
if game==False:
    print('I guess you are not up to it.')

def secondchoice():
    game==True
    second=input('First Pick a weapon- (Axe, Blade, or Bow) ')
    return second
if game ==True:
    y = secondchoice()

if y=='Axe' or y=='axe':
    print('(The Axe will kill most enemies with one blow but has very slow attack speed.)')
    weapon=input('Are you sure you want this weapon? (yes/no)')
    if weapon=='yes' or weapon=='Yes':
        game=True
    elif weapon=='no' or weapon=='No':
        second=input('Pick a weapon- (Axe, Blade, or Bow) ')
        if second=='Axe' or second=='axe':
            print('(The Axe will kill most enemies with one blow but has very slow attack speed.)')
        elif second=='blade' or second=='Blade':
            print('(The Blade has faster attack speed and a decent amount of damage.)')
        elif second=='bow' or second=='Bow':
            print('(The Bow is a long range weapon that has decent damage.)')
        game=True
elif y=='Blade' or y=='blade':
    print('(The Blade has faster attack speed and a decent amount of damage.)')
    weapon=input('Are you sure want this weapon? (yes/no)')
    if weapon=='yes' or weapon=='Yes':
        game=True
    elif weapon=='no' or weapon=='No':
        second=input('Pick a weapon- (Axe, Blade, or Bow) ')
        if second=='Axe' or second=='axe':
            print('(The Axe will kill most enemies with one blow but has very slow attack speed.)')
        elif second=='blade' or second=='Blade':
            print('(The Blade has faster attack speed and a decent amount of damage.)')
        elif second=='bow' or second=='Bow':
            print('(The Bow is a long range weapon that has decent damage.)')
    game=True
elif y=='Bow' or y=='bow':
    print('(The Bow is a long range weapon that has decent damage.)')
    weapon=input('Are you sure you want this weapon? (yes/no)')
    if weapon=='yes' or weapon=='Yes':
        game=True
    elif weapon=='no' or weapon=='No':
        second=input('Pick a weapon- (Axe, Blade, or Bow) ')
        if second=='Axe' or second=='axe':
            print('(The Axe will kill most enemies with one blow but has very slow attack speed.)')
        elif second=='blade' or second=='Blade':
            print('(The Blade has faster attack speed and a decent amount of damage.)')
        elif second=='bow' or second=='Bow':
            print('(The Bow is a long range weapon that has decent damage.)')
        game=True
def thirdchoice():
    move=input('There is a cave that cuts through the mountain. Shall we take the long way, and trek around the mountain or go through the cave. (cave/path)') 
    return move
z = thirdchoice()

if z=='cave' or z=='Cave':
    print('You start your climb up the mountain and find the opening to the cave. "You can still turn back to the mountain path". Will you turn back to the path (yes/no)')
    choice=input()
    if choice=='yes' or choice=='Yes':
        print('You begin up the mountain path. You turn the corner and...To Be Continued...')
    elif choice=='no' or choice=='No':
        print('You head into the cave, when you hear a loud crash...the opening to the cave has collapsed...To Be Continued.')
    game==True
elif z=='path' or z=='Path':
    print('You begin up the mountain path. You turn the corner and...To Be Continued...')
    game==True
