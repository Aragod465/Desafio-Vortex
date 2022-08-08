import random


class Constelacoes:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, u, v):

        valor_certo = False
        if self.grafo[u][v] == 1:

            while(not valor_certo):
                u2 = random.randrange(0, 4)
                v2 = random.randrange(0, 4)

                if(u2 != v2):
                    valor_certo = True

            g.adiciona_aresta(u2, v2)

        else:
            self.grafo[u][v] = 1

            self.grafo[v][u] = 1

    def mostra_matriz(self, valorx, valory):

        for i in range(self.vertices):
            print(self.grafo[i])

        if self.grafo[valorx][valory] == 1:
            print("Tem ligação a estrela {} com a estrela {}".format(valorx, valory))
        else:
            print("Não tem ligação a estrela {} com a estrela {}".format(valorx, valory))


i2 = 0
estrelas_no_espaço = []
estrelas_espaço = int(input("Digite a quantidade de estrelas (Minimo -> 4/Maximo -> 8): "))
print("*****************")

while(i2 < estrelas_espaço):
    estrelas_no_espaço.append(i2)
    i2 = i2 + 1

g = Constelacoes(estrelas_espaço)
i = 1

if(estrelas_espaço <= 8 and estrelas_espaço >= 4):

    print("Estrelas a serem observadas: {}".format(estrelas_no_espaço))
    estrela_1 = int(input("Digite a primera estrela que quer observar: "))
    estrela_2 = int(input("Digite a segunda estrela que quer observar: "))

    if(estrelas_no_espaço.__contains__(estrela_1) and estrelas_no_espaço.__contains__(estrela_2)):

        while(i <= estrelas_espaço):

            ligação = random.randrange(0, estrelas_espaço)
            ligação_2 = random.randrange(0, estrelas_espaço)

            if(ligação == ligação_2):
                i = i - 1

            else:
                g.adiciona_aresta(ligação, ligação_2)

            i = i + 1

        g.mostra_matriz(estrela_1, estrela_2)
    else:
        print("Esse valor de estrela não existe")

else:
    print("Valor de estrela invalido, digite um valor no minimo 4 e no maximo 8")
