
x = int(input())
y = int(input())
g = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
time = 0
asteroids = []
blanks = []
for t in range(x):
    lst = []
    for v in range(y):
        lst.append("*")
    asteroids.append(lst)
for h in range(g):
    lstt = []
    for k in range(y):
        lstt.append(" ")
    blanks.append(lstt)
ship = None
if y%2==0:
    ship = [" "]*(int(y/2)-1)+["@"]+[" "]*int(y/2)
else:
    ship = [" "]*int(y/2)+["@"]+[" "]*(int(y/2))
ast_blanks = []
for aaa in range(y):
    ast_blanks.append(" ")
find_boolt = True
for qq in asteroids:
    for tt in qq:
        if tt == "*":
            find_boolt = False
if find_boolt == False:
    for columns in asteroids:
        for rows in columns:
            print(rows,end="")
        print()
    for spc in blanks:
        for spcc in spc:
            print(spcc,end="")
        print()
    for gemi in ship:
        print(gemi,end="")
    print()
    print("------------------------------------------------------------------------")
scora = 0
for r in asteroids:
    for e in r:
        if e == "*":
            scora +=1
while True:
    booeln = True
    for x in asteroids:
        for t in x:
            if t == "*":
                booeln = False
    if booeln == True:
        print("YOU WON!")
        for columns in asteroids:
            for rows in columns:
                print(rows, end="")
            print()
        for spc in blanks:
            for spcc in spc:
                print(spcc, end="")
            print()
        for gemi in ship:
            print(gemi, end="")
        print()
        print("------------------------------------------------------------------------")
        score = scora
        for u in asteroids:
            for o in u:
                if o == "*":
                    score -= 1
        print("YOUR SCORE:", score)
        break
    print("Choose your action!")
    ask = input().lower()
    if ask == "left":
        time +=1
        if ship.index("@") != 0:
            ship[ship.index("@")-1] = "@"
            ship[ship.index("@")+1] = " "
    if ask == "right":
        time += 1
        if ship.index("@") != (len(ship)-1):
            ship[ship.index("@")+1] = "@"
            ship[ship.index("@")] = " "
    if ask != "fire" and ask != "left" and ask != "right" and ask != "exit":
        time += 1
    if ask == "fire":
        time +=1
        for shot in reversed(blanks):
            shot[ship.index("@")] = "|"
            for columns in asteroids:
                for rows in columns:
                    print(rows, end="")
                print()
            for spc in blanks:
                for spcc in spc:
                    print(spcc, end="")
                print()
            for gemi in ship:
                print(gemi, end="")
            print()
            print("------------------------------------------------------------------------")
            shot[ship.index("@")] = " "
        for c in reversed(asteroids):
            if c[ship.index("@")] == " ":
                c[ship.index("@")] = "|"
                for columns in asteroids:
                    for rows in columns:
                        print(rows, end="")
                    print()
                for spc in blanks:
                    for spcc in spc:
                        print(spcc, end="")
                    print()
                for gemi in ship:
                    print(gemi, end="")
                print()
                print("------------------------------------------------------------------------")
                c[ship.index("@")] = " "
            else:
                c[ship.index("@")] = " "
                break
    if time % 5 == 0 and time != 0:
        try:
            blanks.pop()
            asteroids.insert(0,ast_blanks)
        except:
            if not "*" in asteroids[-1]:
                asteroids.pop()
                asteroids.insert(0,ast_blanks)
            else:
                print("GAME OVER")
                for columns in asteroids:
                    for rows in columns:
                        print(rows, end="")
                    print()
                for spc in blanks:
                    for spcc in spc:
                        print(spcc, end="")
                    print()
                for gemi in ship:
                    print(gemi, end="")
                print()
                print("------------------------------------------------------------------------")
                score = scora
                for u in asteroids:
                    for o in u:
                        if o == "*":
                            score -= 1
                print("YOUR SCORE:", score)
                break
    find_bool = True
    for n in asteroids:
        for t in n:
            if t == "*":
                find_bool= False
    if find_bool == False:
        for columns in asteroids:
            for rows in columns:
                print(rows, end="")
            print()
        for spc in blanks:
            for spcc in spc:
                print(spcc, end="")
            print()
        for gemi in ship:
            print(gemi, end="")
        print()
        print("------------------------------------------------------------------------")
    if ask == "exit":
        for columns in asteroids:
            for rows in columns:
                print(rows, end="")
            print()
        for spc in blanks:
            for spcc in spc:
                print(spcc, end="")
            print()
        for gemi in ship:
            print(gemi, end="")
        print()
        print("------------------------------------------------------------------------")
        score = scora
        for u in asteroids:
            for o in u:
                if o == "*":
                    score -= 1
        print("YOUR SCORE:", score)
        break
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
