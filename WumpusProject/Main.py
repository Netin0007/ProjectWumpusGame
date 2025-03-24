import os
    
class Caverna:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.mapa = [
            ['[ ]' for _ in range(tamanho)] for _ in range(tamanho)
        ]

    def exibir(self, playerPosition):
        
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                if (i, j) == playerPosition:
                    print("[P]", end=" ")
                else:
                    print(self.mapa[i][j], end=" ")
            print()


class Pontos:
    def __init__ (self):
        self.pontos = []
        
    def addPontos (self, nome , pontos):
        self.pontos.append({"nome": nome, "pontos": pontos})
        
        self.pontos = sorted(self.pontos, key=lambda x: x['pontos'], reverse=True)

        self.pontos = self.pontos[:5]

    def mostraPontos(self):
        if not self.pontos:
            print("Nenhuma pontuação registrada ainda.")
        else:
            for i, jogador in enumerate(self.pontos, 1):
                print(f"{i}. {jogador['nome']} - {jogador['pontos']} pontos")


class Jogador:
    def __init__(self, nome):
        self.nome = nome
        
        
        
        
        
        

class NovoJogo:
    def __init__(self):
        self.caverna = None
        self.nome = ""
        self.dificuldade = ""
        self.posicao = (0, 0)
        
    def cadastro (self):
        self.nome = input("Digite seu nome:\n")
        
        self.dificuldade = input("DIficuldades:\neasy: 4x4\nnormal: 6x6\nhard: 10x10\n").lower()
        
        if self.dificuldade == "easy":
            self.caverna = Caverna(4)
        elif self.dificuldade == "normal":
            self.caverna = Caverna(6)
        elif self.dificuldade == "hard":
            self.caverna = Caverna(10)
        else:
            print("Dificuldade inválida! Usando 'normal' por padrão.")
            self.caverna = Caverna(6)
        
    def jogar(self):
        while True:
            os.system("cls")
            self.caverna.exibir(self.posicao)

            move = input("use W/A/S/D para mover-se (Q para fechar o jogo)").lower()
            if move == "w" and self.posicao[0] > 0:
                self.posicao = (self.posicao[0] - 1, self.posicao[1])
            elif move == "s" and self.posicao[0] < self.caverna.tamanho - 1:
                self.posicao = (self.posicao[0] + 1, self.posicao[1])
            elif move == "a" and self.posicao[1] > 0:
                self.posicao = (self.posicao[0], self.posicao[1] - 1)
            elif move == "d" and self.posicao[1] < self.caverna.tamanho - 1:
                self.posicao = (self.posicao[0], self.posicao[1] + 1)
            elif move == "q":
                print("encerrando jogo..")
                break
            else:
                print("movimento invalido..")
    
        
class menuInicial:
        
    def __init__(self):
        self.menu = ["Novo Jogo", "Continuar", "Ranking", "Sair"]
        self.linha = 0
        self.pontos = Pontos()
            
    def exibirMenu(self):
        print("MENU PRINCIPAL")
        for i, v in enumerate(self.menu):
            if i == self.linha:
                print(f"> {v} <")
            else:
                print(f"  {v}")
                
    def escolha(self):
        escolha = input("escolha uma ação(W/S): \n").upper()
        if escolha == "W" and self.linha > 0:
            self.linha -= 1
        elif escolha == "S" and self.linha < len(self.menu) -1:
            self.linha += 1
        elif escolha == "":
            self.executa()
            
    def executa(self):
        op = self.menu[self.linha]
        if op == "Sair":
            print("saindo...\n")
            exit()
           
        elif op == "Ranking":
            self.pontos.mostraPontos()
            input("Pressione Enter para voltar ao menu...")
        elif op == "Novo Jogo":
            nwgame = NovoJogo()
            nwgame.cadastro()
            nwgame.jogar()
        elif op == "Continuar":
            print("começar jogo") 
            input("Pressione Enter para voltar ao menu...") 
                        
    def run (self):
        
        while True:
            os.system('cls')
            print()
            self.exibirMenu()
            self.escolha()
           


if __name__ == "__main__":
    
    menu = menuInicial()    
    menu.run()
    