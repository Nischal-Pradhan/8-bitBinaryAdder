
#importing DecimalToBinary and binaryAdder
from Conversion import DecimalToBinary
from byteAdder import binaryAdder

print("\n ***Welcome to the byte adder Application*** \n")
print("\n Please enter numbers greater then or equal to 0 and less then or equal to 255. \n\n")

run="yes"
while run=="yes" or run=="y":
	sucess=False
	while sucess==False:
		try:
                        #input first decimal value
			num1 =int(input("\n Enter the first number: "))
			if num1<0 or num1>255:
				print("Remember, the input value must be between 0 and 255.")
			else:   
				sucess=True
		except:
			print("INVALID INPUT!!! Please enter a valid number.")
			
	sucess=False
	while sucess==False:
		try:
                        #input second decimal value
			num2 =int(input("\n Enter the second number: "))
			if num2<0 and num2>255:
				print("Remember, the input value must be between 0 and 255.")
			else:
				sucess=True
		except:
			print("INVALID INPUT!!! Please enter a valid number.")
	print("\n")
	#values of decimal number are converted and displayed as binary number...
	print(" The binary value of {} is: {}\n".format(num1,DecimalToBinary(num1)))
	print(" The binary value of {} is: {}\n".format(num2,DecimalToBinary(num2)))
	a=DecimalToBinary(num1)
	b=DecimalToBinary(num2)
	Summ=binaryAdder(str(a),str(b))
	print(" The sum of {} and {} is : {}\n".format(a,b,Summ))

	print("\n  ***Thank you for using this Application*** \n")
	run = input(" Do you wish to continue? If yes, type 'yes/y' and if no, type 'no/n': ")
	print("\n")
print("\n BYE BYE!! \n")

