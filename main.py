row_1 = ["⬜", "⬜", "⬜"]
row_2 = ["⬜", "⬜", "⬜"]
row_3 = ["⬜", "⬜", "⬜"]
map = [row_1, row_2, row_3]
print(f"{row_1}\n{row_2}\n{row_3}")

position = input("Where do you want to place the treasure?")
row = int(position[0])
colum = int(position[1])
if row == "1" and colum == "1":
    row_1[0] = "X"
elif row == "2" and colum == "1":
    row_2[0] = "X"
elif row == "3" and colum == "1":
    row_3[0] = "X"
elif row == "1" and colum == "2":
    row_1[1] = "X"
elif row == "2" and colum == "2":
    row_2[1] = "X"
elif row == "3" and colum == "2":
    row_3[1] = "X"
elif row == "1" and colum == "3":
    row_1[2] = "X"
elif row == "2" and colum == "3":
    row_2[2] = "X"
elif row == "3" and colum == "3":
    row_3[2] = "X"
else:
    print("Invalid")
map[row-1][colum-1] = "X"
print(f"{row_1}\n{row_2}\n{row_3}")
