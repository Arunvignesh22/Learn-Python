row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

if position[0] == '1' and position[1] == '1':
    row1[0] = "x"
elif position[0] == '1' and position[1] == '2':
    row1[1] = "X"
elif position[0] == '1' and position[1] == '3':
    row1[2] = "X"
elif position[0] == '2' and position[1] == '1':
    row2[0] = "x"
elif position[0] == '2' and position[1] == '2':
    row2[1] = "x"
elif position[0] == '2' and position[1] == '3':
    row2[2] = "x"
elif position[0] == '3' and position[1] == '1':
    row3[0] = "x"
elif position[0] == '3' and position[1] == '2':
    row3[1] = "x"
elif position[0] == '3' and position[1] == '3':
    row3[2] = "x"

print(f"{row1}\n{row2}\n{row3}")