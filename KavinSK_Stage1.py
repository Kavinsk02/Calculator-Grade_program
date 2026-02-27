number1,number2,is_operator=input().split(",")
number1=int(number1.strip())
number2=int(number2.strip())
is_operator=is_operator.strip()
if is_operator =="+":
  print("Result =", number1 + number2)
elif is_operator =="-":
  print("Result =", number1 - number2)
elif is_operator =="*":
  print("Result =", number1 * number2)
elif is_operator =="/":
  if number2 ==0:
    print("number2 divisible by zero not allowed")
  else:
    print("Result =",number1/number2)
else:
  print("Invalid operator")
