from model import model

class control:
    def __init__(self):
        self.modelo = model() #Criando um vínculo com a classe model
        self.opcao = -1

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def menu(self):
        print('\n\nEscolha uma das opções abaixo: '   +
              '\n0. Sair'                             +
              '\n1. Exercício 01'                     +
              '\n2. Exercício 02 e Exercício 03'      +
              '\n4. Exercício 04')
        self.setOpcao(int(input()))

    def operacao(self):
        while (self.getOpcao() != 0):
            self.menu()#Mostrando o menu na tela
            if self.getOpcao() == 0:
                print('Obrigado!')
            elif self.getOpcao() == 1:
                self.exercicioUm()
            elif self.getOpcao() == 2:
                self.exercicioDoisETres()
            elif self.getOpcao() == 4:
                self.exercicioQuatro()
            else:
                print('Opção escolhida não é válida!')

    def exercicioUm(self):
        for i in range(20):
            print("Informe a {}ª nota: ".format(int(i+1)))
            nota = float(input())
            #Validando a operação
            while (nota < 0) or (nota > 10):
                print("Nota invalida, digite novamente!")
                nota = float(input())
            #Adicionar no vetor notas a nota
            self.modelo.preencherNotas(nota)
        print("A média das notas é: {}".format(self.modelo.calcularMedia()))
        print("Há {}% notas maiores que a média".format(self.modelo.contarVetor()))

    def exercicioDoisETres(self):
        for i in range(20):
            print("Informe o {}º número: ".format(int(i + 1)))
            num = float(input())
            # Validando a operação
            while (num < 0):
                print("Número invalido, digite novamente!")
                num = float(input())
            # Adicionar no vetor notas a nota
            self.modelo.preencherQ(num)
        print(self.modelo.maiorMenor())

    def exercicioQuatro(self):
        for i in range(10):
            print("Informe o {}º número: ".format(int(i + 1)))
            num = float(input())
            #Adicionar no vetor
            self.modelo.preencherA(num)
        print("Informe um número que será o multiplicador")
        x = int(input())
        self.modelo.preencherM(x)
        print(self.modelo.mostrarM())
