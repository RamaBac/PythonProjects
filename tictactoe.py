for i in range(2):
	print("    |    |    ")
	print("______________")
print("    |    |    ")
poslst = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
y = 0
for i in range(9) :
    if y == 1 : break
    o = input("Enter your position: ")
    if poslst[int(o)-1] == "X" or poslst[int(o)-1] == "O" or int(o) < 1 or int(o) > 9 or int(o)%1 != 0 or o == "" :
        print("You tried to cheat. You lose your turn.")
        continue
        # i starts from 0 -8
    if i%2 != 0:
        poslst[int(o)-1] = "O"
    else :
        poslst[int(o)-1] = "X"
    print(" ", poslst[0], "  | ", poslst[1], "  | ", poslst[2], "   ")
    print("___________________")
    print(" ", poslst[3], "  | ", poslst[4], "  | ", poslst[5], "   ")
    print("___________________")
    print(" ", poslst[6], "  | ", poslst[7], "  | ", poslst[8], "   ")
    a = ['X', 'X', 'X']
    b = ['O', 'O', 'O']

    for i in [0, 3, 6]:
       if [poslst[i], poslst[i+1], poslst[i+2]] == a or [poslst[i], poslst[i+1], poslst[i+2]] == b :
           print(poslst[i], "is the winner!")
           y == y + 1
           break
    for i in [0, 1, 2] :
        if [poslst[i], poslst[i+3], poslst[i+6]] == a or [poslst[i], poslst[i+3], poslst[i+6]] == b :
            print(poslst[i], "is the winner!")
            y = y + 1
            break
    if poslst[0] == poslst[4] == poslst[8] == 'X' or poslst[0] == poslst[4] == poslst[8] == 'O' :
        print(poslst[0], "wins!")
        y = y + 1
        break
    elif poslst[2] == poslst[4] == poslst[6] == 'X' or poslst[2] == poslst[4] == poslst[6] == 'O' :
        print(poslst[2], "wins!")
        y = y + 1
        break
if y == 0 :
    print("It's a draw!")
