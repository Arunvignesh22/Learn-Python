
sum_final = 0
for total in range(2, 101, 2):
    sum_final += total

print(f"Addition of even numbers from 1 to 100 is : {sum_final}")

#or

alternate_sum_final = 0
for total in range(2, 101):
    if total % 2 == 0:
        alternate_sum_final += total

print(f"Addition of even numbers from 1 to 100 is : {alternate_sum_final}")

