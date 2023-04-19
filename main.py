def int_generator(num1, num2, num3):
    ## Checa se algum dos 3 números é divisível por 10. Critério 5
    if num1 % 10 == 0 or num2 % 10 == 0 or num3 % 10 == 0:
        return 10
    ## Se não, checa se o primeiro número é divisível por 2. Critério 1
    elif num1 % 2 == 0:
        ## Se sim, checa se os próximos números obedecem a algum outro critério. Critério 4
        if num2 % 3 == 0:
            return str(num1) + str(num2)
        elif num3 % 5 == 0:
            return str(num1) + str(num3)
        else:
            return num1
    ## Se não, checa se o segundo número é divisível por 3. Critério 2
    elif num2 % 3 == 0:
        ## Se sim, checa se o número 3 obedece ao critério 3
        if num3 % 5 == 0:
            return str(num2) + str(num3)
        else:
            return num2
    ## Se não, checa se o número 3 é divisível por 5. Critério 3
    elif num3 % 5 == 0:
        return num3
    ## Se não obedecer nenhum critério, retorna 0
    else:
        return 0

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
resultado = int_generator(num1, num2, num3)
print(f"Resultado: {resultado}")
