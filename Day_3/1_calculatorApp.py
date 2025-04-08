import calculator
#from calculator import add, subtract, multiply, divide #(drawback is it will overwrite if they have same name)
#from calculator import add as a  #Alias 
ch = int(input('ENtere your choice 1. Add 2. Substract 3. Multiply 4. Divide \n'))
n1 = int(input('Enter First Num: '))
n2 = int(input('Enter Second Num: '))

match ch:
    case 1:
        res = calculator.add(n1, n2)
        print(res)
    case 2:
        res = calculator.subtract(n1, n2)
        print(res)    
    case 3:
        res = calculator.multiply(n1, n2)
        print(res)
    case 4:
        res = calculator.divide(n1, n2)
        print(res)    





