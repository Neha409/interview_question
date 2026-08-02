l = [3, 4, 5, 9, 10, 16, 20, 25]
square_list = []
for i in l:
    num = int(i**0.5)
    #print(num)
    if num * num == i:
        square_list.append(i)

print(f"Perfect square list = {square_list}")