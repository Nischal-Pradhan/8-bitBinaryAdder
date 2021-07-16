#BASIC GATES


#basic not gate
def NOTGate(a):
	if a==0:
		return 1
	else:
		return 0
	
#basic or gate
def ORGate(a,b):
	if a==b==0:
		return 0
	else:
		return 1
	
#basic and gate
def ANDGate(a,b):
	if a==b==1:
		return 1
	else:
		return 0

#basic xor gate
def XORGate(a,b):
	a1 = ANDGate(a, NOTGate(b))
	b1 = ANDGate(b, NOTGate(a))
	return (ORGate(a1,b1))

#half adder
def halfAdder(a,b):
	num1 = XORGate(a,b)
	num2 = ANDGate(a,b)
	return (num1,num2)

#full adder
def fullAdder(a,b,c=0):
	sum1, c1 = halfAdder(a,b)
	sum2, c2 = halfAdder(sum1,c)
	return (sum2,ORGate(c1, c2))

#calculating the binary addition
#binary addition
def binaryAdder(a,b):
	if a>b:
		tmp=a
		a=b
		b=tmp
	c=0
	result=""
	for i in range(len(a)-1,-1,-1):
		Summ,c= fullAdder(int(a[i]),int(b[i]),c)
		result+=str(Summ)
	result+=str(c)
	result=result[::-1]

	l = len(result)
	if len(result)<8:
		for i in range(l,8):
			result="0"+result
	return result
