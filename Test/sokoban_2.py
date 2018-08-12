p = {
    "x": 1,
    "y": 1
}
g = {
    "x": 1,
    "y": 3
}
boxes = [
    {
        "x": 2,
        "y": 2
    },
    {
        "x": 2,
        "y": 1
    }
]
print('''Let's play!
P: player, B: box, G: gate
press W to move up
press S to move down
press A to move left
press D to move right
press 0 to exit''')
while True:
    for y in range(4):
        for x in range(4):
            if x == p["x"] and y == p["y"]:
                print("P ", end=" ")
            elif x == g["x"] and y == g["y"]:
                print("G ", end=" ")
            elif x == boxes[0]["x"] and y == boxes[0]["y"]:
                print("B1 ", end="")
            elif x == boxes[1]["x"] and y == boxes[1]["y"]:
                print("B2 ", end="")
            else:
                print("- ", end=" ")
        print()

    if boxes[0]["x"] ==g["x"] and boxes[0]["y"] == g["y"]:
        boxes[0]["x"] = 10
        boxes[0]["y"] = 10
    if boxes[1]["x"] ==g["x"] and boxes[1]["y"] == g["y"]:
        boxes[1]["x"] = 10
        boxes[1]["y"] = 10

    if boxes[0]["x"] ==10 and boxes[0]["y"] == 10 and boxes[1]["x"] ==10 and boxes[1]["y"] ==10:
        print("Win")
        break
    elif boxes[0]["x"] == 0 and boxes[0]["y"] == 0:
        print("Lose")
        break
    elif boxes[0]["x"] == 3 and boxes[0]["y"] == 0:
        print("Lose")
        break
    elif boxes[0]["x"] ==0 and boxes[0]["y"] == 3:
        print("Lose")
        break
    elif boxes[0]["x"] ==3 and boxes[0]["y"] == 3:
        print("Lose")
        break
    elif boxes[1]["x"] == 0 and boxes[1]["y"] == 0:
        print("Lose")
        break
    elif boxes[1]["x"] == 3 and boxes[1]["y"] == 0:
        print("Lose")
        break
    elif boxes[1]["x"] ==0 and boxes[1]["y"] == 3:
        print("Lose")
        break
    elif boxes[1]["x"] ==3 and boxes[1]["y"] == 3:
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

    if next_px == boxes[0]["x"] and next_py == boxes[0]["y"]:
        if (next_px+dx) == boxes[1]["x"] and (next_py+dy) == boxes[1]["y"]:
            if (boxes[1]["x"] + dx) < 0  or (boxes[1]["x"] + dx) > 3:
                print("box out of map!")
                continue
            elif (boxes[1]["y"] + dy) < 0  or (boxes[1]["y"] + dy) > 3:
                print("box out of map!")
                continue
            else:
                boxes[1]["x"] += dx
                boxes[1]["y"] += dy
        if (boxes[0]["x"] + dx) < 0  or (boxes[0]["x"] + dx) > 3:
            print("box out of map!")
            continue
        elif (boxes[0]["y"] + dy) < 0  or (boxes[0]["y"] + dy) > 3:
            print("box out of map!")
            continue
        else:
            boxes[0]["x"] += dx
            boxes[0]["y"] += dy
    elif next_px == boxes[1]["x"] and next_py == boxes[1]["y"]:
        if (next_px+dx) == boxes[0]["x"] and (next_py+dy) == boxes[0]["y"]:
            if (boxes[0]["x"] + dx) < 0  or (boxes[0]["x"] + dx) > 3:
                print("box out of map!")
                continue
            elif (boxes[0]["y"] + dy) < 0  or (boxes[0]["y"] + dy) > 3:
                print("box out of map!")
                continue
            else:
                boxes[0]["x"] += dx
                boxes[0]["y"] += dy
        if (boxes[1]["x"] + dx) < 0  or (boxes[1]["x"] + dx) > 3:
            print("box out of map!")
            continue
        elif (boxes[1]["y"] + dy) < 0  or (boxes[1]["y"] + dy) > 3:
            print("box out of map!")
            continue
        else:
            boxes[1]["x"] += dx
            boxes[1]["y"] += dy

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
