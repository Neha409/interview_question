
s = "{[()]}"

pair = {
    "{" : "}",
    "[" :"]",
    "(" : ")"

}
first_half,second_half = "",""
for i in range(int(len(s)/2)):
    first_half = first_half + s[i]
print(first_half)

for j in range(int(len(s)/2), len(s)):
    second_half = second_half + s[j]

print(second_half)
second_half_res = ""
j=0
match = 0
if len(first_half) == len(second_half):
    for i in range(len(first_half)-1 ,-1,-1):
        #print(i)
        com = pair.get(first_half[i])
        #print(com)
        #print(j)
        if j < len(second_half) and com == second_half[j]:
            #print(f" sceond half {second_half[j]}")
            match = match + 1
        j = j + 1

    if match == len(first_half):
        print("this is Balanaced Brackets")
    else:
        print("this is unbalanced brackets")
else:
    print("this is unbalanced brackets")