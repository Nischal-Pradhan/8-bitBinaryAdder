def DecimalToBinary(number):
	number=int(number)
	bit=[]
	actualBinary=[]
	actualBinaryNumber=""
	while number !=0:
		remainder=number%2
		bit.append(remainder)
		number=number//2
	for i in range(len(bit)-1,-1,-1):
		actualBinary.append(bit[i])
		actualBinaryNumber = actualBinaryNumber +str(bit[i])
		l = len(actualBinaryNumber)
	if len(actualBinaryNumber)<8:
		for i in range(l,8):
			actualBinaryNumber="0"+actualBinaryNumber
	return actualBinaryNumber
