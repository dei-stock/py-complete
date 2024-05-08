def getLargest(arrNum):
    largest = arrNum[0]
    for n in arrNum:
        if n > largest:
            largest = n
    return largest

def showPattern(rCount, cCount):
    for r in range(rCount):
        for c in range(cCount):
            print('X\t', end=" ")
        print()

def showOptions():
    print('1. Largest Number')
    print('2. Pattern')
    print('3. Exit Program')
    
while True:
    showOptions();
    choice = int(input('Enter desired program: '))
    if choice == 1:
        nums = [5,3,7,9,2]
        largest = getLargest(nums)
        print('Largest is:', largest)
    elif choice == 2:
        row = 5
        col = 5
        showPattern(row, col)
    elif choice == 3:
        print('Thanks for using MyApp 1.0. Bye...')
        break
    else:
        print('Invalid input, please enter 1-3 only...')