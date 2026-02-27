number1,number2,is_operator=input().split(",")
number1=int(number1.strip())
number2=int(number2.strip())
is_operator=is_operator.strip()
if is_operator =="+":
  result= number1 + number2
  print("Result =",result )
elif is_operator =="-":
  result= number1 - number2
  print("Result =", result)
elif is_operator =="*":
  result= number1 * number2
  print("Result =", result)
elif is_operator =="/":
  if number2 ==0:
    print("number2 divisible by zero not allowed")
  else:
    result= number1 / number2
    print("Result =",result)
else:
  print("Invalid operator")

if(result>0):
  print("positive")
elif(result <0):
  print("negative")
else:
  print("zero")
