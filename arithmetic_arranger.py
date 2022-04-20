def arithmetic_arranger(problems, optional = False):

  # Error: Too many problems.
  ops = len(problems)
  if ops > 5 : 
    return "Error: Too many problems."


  operand1 = []
  operand2 = []
  operator = []

  
  for prblm in problems :
    operand1.append(prblm.split(" ")[0])
    operand2.append(prblm.split(" ")[2])

    # Error: Operator must be '+' or '-'.
    operation = prblm.split(" ")[1]
    if operation == '*' or operation == '/' : 
      return "Error: Operator must be '+' or '-'."
    else : 
      operator.append(operation)

  
  diff = []
  for num1, num2 in zip(operand1, operand2) :

    # Error: Numbers must only contain digits.
    try :
      int(num1)
      int(num2)
    except :
      return "Error: Numbers must only contain digits."
    
    # Error: Numbers cannot be more than four digits.
    if len(num1) > 4 or len(num2) > 4 :
      return "Error: Numbers cannot be more than four digits."
    
    diff.append(abs(len(num1) - len(num2)))

  
  line1 = ["  "]
  line2 = []
  line3 = [""]
  
  for i in range(len(operand1)) :
    line2.append(operator[i])
    line2.append(" ")

    line3.append("--")
 
    if len(operand1[i]) < len(operand2[i]) :
      for j in range(diff[i]) :
        line1.append(" ")

      for j in range(len(operand2[i])) :
         line3.append("-")
      
    else :
      for j in range(diff[i]) :
        line2.append(" ")

      for j in range(len(operand1[i])) :
         line3.append("-")

    
      
    line1.append(operand1[i])
    line1.append("      ") 

    line2.append(operand2[i])
    line2.append("    ")

    line3.append("    ")

  
  #Interface
  str1 = ""
  for ele in line1 : 
    str1 += ele

  str2 = ""
  for ele in line2 : 
    str2 += ele
  
  str3 = ""
  for ele in line3 : 
    str3 += ele


  if optional == True :
    result = []
    for num1, op, num2 in zip(operand1, operator, operand2) :
      if op == "+" :
        result.append(int(num1) + int(num2))
      if op == "-" :
        result.append(int(num1) - int(num2))

    line4 = [""]
    for i in range(len(result)) :
      line4.append(" ")
      a = max(len(operand1[i]), len(operand2[i])) - len(str(result[i]))
      if a >= 0 :
        line4.append(" ")
      
      for j in range(a) :
        line4.append(" ")
      
      line4.append(str(result[i]))
      line4.append("    ")

    #Interface
    str4 = ""
    for ele in line4 : 
      str4 += ele

    return str1.rstrip() + "\n" + str2.rstrip() + "\n" + str3.rstrip() + "\n" + str4.rstrip()
    


    

  interface = str1.rstrip() + "\n" + str2.rstrip() + "\n" + str3.rstrip()
  
  return interface
