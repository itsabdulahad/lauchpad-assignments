lst = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n):
	ele = int(input()) 
	lst.append(ele) 
print(lst)
for i in range(0, n):
	if lst[i] < 5:
		print(lst[i])


