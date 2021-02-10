num = int(input("What Size Game GoPy? "))
matrix_list, matrix_list2, starting_point = [], [], 0
control_list = [a for a in range(num**2)]
for i in range(num):
    inner_list = []
    for j in range(num):
        inner_list.append(starting_point)
        starting_point = starting_point + 1
    matrix_list.append(inner_list)


def change(inp, player):
    if -1 < inp < num**2:
        if (player == 1 and control_list[inp] == "X") or (player == 2 and control_list[inp] == "O"):
            print("You have made this choice before")
        elif (player == 1 and control_list[inp] == "O") or (player == 2 and control_list[inp] == "X"):
            print("The other player select this cell before")
        for sublist in matrix_list:
            while inp in sublist:
                if player == 1:
                    sublist[sublist.index(inp)], control_list[inp] = "X", "X"
                elif player == 2:
                    sublist[sublist.index(inp)], control_list[inp] = "O", "O"
    else:
        print("Please enter a valid number")


def draw():
    global matrix_list2
    matrix_list2 = []
    for sublist in matrix_list:
        inner_list2 = []
        for val in sublist:
            inner_list2.append(str(val).rjust(4))
            if len(inner_list2) == num:
                matrix_list2.append(inner_list2)
                inner_list2 = []
    for k in matrix_list2:
        b = ' '.join(map(str, k))
        print(b)


def check():
    l2, l3, s = [], [], True
    ind, ind2, ind3 = -1, 0, num - 1
    for sublist in matrix_list:
        if sublist.count(sublist[0]) == len(sublist):
            print("Winner: " + str(sublist[0]))
            quit()
    for sublist in matrix_list:
        if isinstance(sublist[ind2], str):
            l2.append(sublist[ind2])
        ind2 = ind2 + 1
        if len(l2) == len(range(num)):
            if l2.count(l2[0]) == len(range(num)):
                print("Winner: " + str(l2[0]))
                quit()
            else:
                pass
    for sublist in matrix_list:
        if isinstance(sublist[ind3], str):
            l3.append(sublist[ind3])
        ind3 = ind3 - 1
        if len(l3) == len(range(num)):
            if l3.count(l3[0]) == len(range(num)):
                print("Winner: " + str(l3[0]))
                quit()
            else:
                pass
    while s:
        ind, l1 = ind + 1, []
        if ind == num - 1:
            s = False
        for sublist in matrix_list:
            if isinstance(sublist[ind], str):
                l1.append(sublist[ind])
                if l1.count(l1[0]) == len(range(num)):
                    print("Winner: " + str(sublist[ind]))
                    quit()


def check_if_draw():
    draw_list, a = [], True
    while True:
        for sub_list in matrix_list:
            while all(isinstance(val, str) for val in sub_list):
                draw_list.append(a)
                break
        if len(draw_list) == num:
            print("No winner")
            quit()
        break


draw()
while True:
    change(int(input("Player 1 turn --> ")), 1)
    draw()
    check()
    check_if_draw()
    change(int(input("Player 2 turn --> ")), 2)
    draw()
    check()
    check_if_draw()
