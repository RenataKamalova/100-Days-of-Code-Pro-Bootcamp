from turtle import position


row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
map[int(position) % 10 - 1][int(position) // 10 - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")
