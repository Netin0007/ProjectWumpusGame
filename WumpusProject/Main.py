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

        

class NovoJogo:
    def __init__(self):
        self.caverna = None
        self.nome = ""
        self.dificuldade = ["Facíl(4x4)", "Normal(6x6)", "Dificil(10x10)"]
        self.posicao = (0, 0)
        self.dif = 0
        
    def exibirDificuldade(self):
        print("DIFICULDADES\n")
        
        for inx, value in enumerate(self.dificuldade):
            if inx == self.dif:
                print(f'> {value} <')
            else:
                print(f' {value}')
                
    
    def escDif(self):
        
        esc = input("escolha uma ação(W/S): \n").upper()
        if esc == "W" and self.dif > 0:
            self.dif -= 1
        elif esc == "S" and self.dif < len(self.dificuldade) -1:
            self.dif += 1
        elif esc == "":
            self.exe()
        
        
    def exe(self):
        ex = self.dificuldade[self.dif]
        if ex == "Facíl(4x4)":
            self.caverna = Caverna(4)
            self.posicao = (0, 0)
        elif ex == "Normal(6x6)":
            self.caverna = Caverna(6)
            self.posicao = (0, 0)
        elif ex == "Dificil(10x10)":
            self.caverna = Caverna(10)
            self.posicao = (0, 0)
        else:
            print("Dificuldade inválida! Usando 'normal' por padrão.")
            self.caverna(6)
            self.posicao = (0, 0)
        
        

    def cadastro (self):
   
        self.nome = input("Digite seu nome:\n")
       
        while True:
            os.system("cls")
            self.exibirDificuldade()
            self.escDif()
            if self.caverna:
                break
        self.jogar()
        
        

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
                m = menuInicial()
                m.run()
            
            else:
                print("movimento invalido..")
    
        
class menuInicial:
        
    def __init__(self):
        self.menu = ["Novo Jogo", "Ranking", "Sair"]
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
                        
    def run (self):
        
        while True:
            os.system('cls')
            print()
            self.exibirMenu()
            self.escolha()
           


if __name__ == "__main__":
    
    menu = menuInicial()    
    menu.run()
    