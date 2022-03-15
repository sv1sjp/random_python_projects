
print("Linear Feedback Shift Register by DimitrisV SV1SJP")
state=int(input("Give me 4-digit: "),2)

for i in range(20):
	print("{:04b}".format(state))
	newbit = (state ^ (state >> 1 )) & 1
	state= (state >> 1) | (newbit<<3)
