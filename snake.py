import random

def gameWin(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


print("Com Turn: Snake(s) , water(w) or gun(g)?: ")
ranNo = random.randint(1,3)
if ranNo == 1:
    comp = "s"
elif ranNo == 2:
    comp = "w"
elif ranNo == 3:
    comp = "g"
you = input("Player's  Turn: Snake(s) , water(w) or gun(g)?: ")
a = gameWin(comp,you)

print(f"Computer choose: {comp}")
print(f"You choose: {you}")

if a == None:
    print("This game is tie")
elif a == True:
    print("You win")
else:
    print("You loose")