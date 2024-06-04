from caculadora import calculadora

calc = calculadora()

n1 = float(input("digite o primeiro número: "))
n2 = float(input("digite o segundo número: "))
print("calculadora /n somar, subtrair, multiplicar, dividir:")

op=input("escreva o nome da operaçao desejada: ")

if op == 'Somar':
    print(calc.soma(n1,n2))
elif op == 'Subtrair':
    print(calc.subtrair(n1,n2))
elif op == 'multiplicar':
    print == (calc.multiplicar(n1,n2))
elif op == 'dividir':
    print == (calc.dividir(n1,n2))

