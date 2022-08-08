print("****************************")
print("Conversor de numeros romanos")
print("****************************")

algarismo_romano = str(input("Digite o algarismo romano a ser covertido: ").strip().upper())

print("Algarismo romano para conversão -> {}".format(algarismo_romano))
algarismos_romanos_convertidos = []

for algarismo in algarismo_romano:
    if(algarismo == "I"):
        algarismos_romanos_convertidos.append(1)

    if (algarismo == "V" ):
        algarismos_romanos_convertidos.append(5)

    if (algarismo == "X"):
        algarismos_romanos_convertidos.append(10)

    if (algarismo == "L"):
        algarismos_romanos_convertidos.append(50)

    if (algarismo == "C"):
        algarismos_romanos_convertidos.append(100)

    if (algarismo == "D"):
        algarismos_romanos_convertidos.append(500)

    if (algarismo == "M"):
        algarismos_romanos_convertidos.append(1000)


def romano_para_inteiro(cada_simbolo_covertido):
    i = 0
    resultado = 0

    while(i < len(cada_simbolo_covertido)):

        inteiro_1 = algarismos_romanos_convertidos[i]

        if(i + 1 < len(cada_simbolo_covertido)):

            inteiro_2 = algarismos_romanos_convertidos[i + 1]

            if(inteiro_1 >= inteiro_2):
                resultado = resultado + inteiro_1
                i = i + 1

            else:

                resultado = resultado + inteiro_2 - inteiro_1
                i = i + 2
        else:
            resultado = resultado + inteiro_1
            i = i + 1

    return resultado


print("Convertidos por cada letra {}".format(algarismos_romanos_convertidos))

print("O resultado do algatismo romano para inteiro foi: {}".format(romano_para_inteiro(algarismos_romanos_convertidos)))
