p = {
    "x": 1,
    "y": 1
}
b = {
    "x": 2,
    "y": 2
}
g = {
    "x": 1,
    "y": 3
}
while True:
    for y in range(4):
        for x in range(4):
            if x  == p["x"] and y == p["y"]:
                print("P ", end="")
            elif x == b["x"] and y == b["y"]:
                print("B ", end="")
            elif x == g["x"] and y == g["y"]:
                print("G ", end="")
            else:
                print("- ", end="")
        print()
    if b["x"] ==g["x"] and b["y"] == g["y"]:
        print("Win")
        break
    elif b["x"] ==0 and b["y"] == 0:
        print("Lose")
        break
    elif b["x"] ==3 and b["y"] == 0:
        print("Lose")
        break
    elif b["x"] ==0 and b["y"] == 3:
        print("Lose")
        break
    elif b["x"] ==3 and b["y"] == 3:
        print("Lose")
        break

    move = input("Your move (W/A/S/D)? ").upper()

    next_px = p["x"]
    next_py = p["y"]
    dx = 0
    dy = 0

    if move == "D":
        dx = 1
    elif move == "A":
        dx = -1
    elif move == "S":
        dy = 1
    elif move == "W":
        dy = -1
    elif move == "0":
        print("Exit")
        break
    else:
        print("error")

    next_px += dx
    next_py += dy

    if next_px == g["x"] and next_py == g["y"]:
        print("cant move")
        continue

    if next_px == b["x"] and next_py == b["y"]:
        if (b["x"] + dx) < 0  or (b["x"] + dx) > 3:
            print("box out of map!")
            continue
        elif (b["y"] + dy) < 0  or (b["y"] + dy) > 3:
            print("box out of map!")
            continue
        else:
            b["x"] += dx
            b["y"] += dy

    if 0 <= next_px < 4:
        p["x"] = next_px
    else:
        print("out of map")
        continue

    if 0 <= next_py < 4:
        p["y"] = next_py
    else:
        print("out of map")
        continue
