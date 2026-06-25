

x= [3,4,5,6,7,8,9] 

last_element = x[-1]

frist_element = x[0]

range = last_element - frist_element
``
r = int((range/2) + 1)
print(r)
count = 0
for i in x:
	for j in range(1, r):
		res = j * j 

		if res == i :
			print(j)
			count = count +1 
