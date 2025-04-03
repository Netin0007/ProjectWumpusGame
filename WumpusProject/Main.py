import os
import random


class Caverna:
    def __init__(self, tamanho, num_wumpus, num_abismos):
        self.tamanho = tamanho
        self.mapa = [['[ ]' for _ in range(tamanho)] for _ in range(tamanho)]
        self.itens = self.gerar_itens()
        self.wumpus = self.gerar_wumpus()
        self.abismos = self.gerar_abismos(num_abismos)

    def gerar_itens(self):
        itens = []
        for _ in range(3):
            while True:
                x, y = random.randint(0, self.tamanho - 1), random.randint(0, self.tamanho - 1)
                if (x, y) not in itens:
                    itens.append((x, y))
                    self.mapa[x][y] = "[]"
                    break
        return itens

    def gerar_wumpus(self):
        while True:
            wumpus_pos = (random.randint(0, self.tamanho - 1), random.randint(0, self.tamanho - 1))
            if wumpus_pos not in self.itens:
                self.mapa[wumpus_pos[0]][wumpus_pos[1]] = "[👻]"
            return wumpus_pos

    def gerar_abismos(self, num_abismos):
        abismos = []
        for _ in range(num_abismos):
            while True:
                abismos_pos = (random.randint(0, self.tamanho - 1), random.randint(0, self.tamanho - 1))
                if abismos_pos not in abismos and abismos_pos not in self.wumpus and abismos_pos not in self.itens:
                    abismos.append(abismos_pos)
                    self.mapa[abismos_pos[0]][abismos_pos[1]] = "[💨]"
                    self.adicionar_brisas(abismos_pos)  # Adiciona brisa ao redor do abismo
                    break
        return abismos

    def adicionar_brisas(self, abismo_pos):
        x, y = abismo_pos
        adjacentes = [
            (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)
        ]
        for adj in adjacentes:
            adj_x, adj_y = adj
            if 0 <= adj_x < self.tamanho and 0 <= adj_y < self.tamanho:
                if self.mapa[adj_x][adj_y] == '[💰]':
                    self.mapa[adj_x][adj_y] = "[B]"

    def exibir(self, playerPosition):
        print(f"\nMapa {self.tamanho}x{self.tamanho} - Sua posição atual: {playerPosition}")
        print("Posições especiais (de acordo com o jogador):")
        print("W: Wumpus, A: Abismo, *: Item, B: Brisa")

        for i in range(self.tamanho):
            for j in range(self.tamanho):
                if (i, j) == playerPosition:
                    print("♿", end=" ")
                elif (i, j) in self.itens:
                    print("💰", end=" ")
                elif (i, j) == self.wumpus:
                    print("👻", end=" ")
                elif (i, j) in self.abismos:
                    print("🔘", end=" ")
                elif self.mapa[i][j] == "[B]":
                    print("💨", end=" ")
                else:
                    print("❓", end=" ")
            print()

        if playerPosition in self.abismos:
            print("Você caiu em um abismo! Jogo terminado.")
        elif playerPosition in self.itens:
            print("Você coletou um item!")
        elif playerPosition == self.wumpus:
            print("Você encontrou o Wumpus!")


class Pontos:
    def __init__(self):
        self.pontos = []

    def addPontos(self, nome, pontos):
        self.pontos.append({"nome": nome, "pontos": pontos})
        self.pontos = sorted(self.pontos, key=lambda x: x['pontos'], reverse=True)
        self.pontos = self.pontos[:5]  # Mantém apenas os 5 melhores

    def mostraPontos(self):
        if not self.pontos:
            print("Nenhuma pontuação registrada ainda.")
        else:
            print("Ranking dos Melhores Jogadores:")
            for i, jogador in enumerate(self.pontos, 1):
                print(f"{i}. {jogador['nome']} - {jogador['pontos']} pontos")


class NovoJogo:
    def __init__(self, ranking):
        self.caverna = None
        self.nome = ""
        self.dificuldade = ["Facíl(4x4)", "Normal(6x6)", "Dificil(10x10)"]
        self.posicao = (0, 0)
        self.dif = 0
        self.pontuacao = 0  # Inicializa a pontuação
        self.ranking = ranking  # Armazena a referência ao ranking

    def exibirDificuldade(self):
        print("DIFICULDADES\n")
        for inx, value in enumerate(self.dificuldade):
            if inx == self.dif:
                print(f'> {value} <')
            else:
                print(f' {value}')

    def escDif(self):
        esc = input("Escolha uma ação(W/S): \n").upper()
        if esc == "W" and self.dif > 0:
            self.dif -= 1
        elif esc == "S" and self.dif < len(self.dificuldade) - 1:
            self.dif += 1
        elif esc == "":
            self.exe()

    def exe(self):
        ex = self.dificuldade[self.dif]
        if ex == "Facíl(4x4)":
            self.caverna = Caverna(4, 1 , 1)
            self.posicao = (0, 0)
        elif ex == "Normal(6x6)":
            self.caverna = Caverna(6, 1 , 2)
            self.posicao = (0, 0)
        elif ex == "Dificil(10x10)":
            self.caverna = Caverna(10, 2 , 5)
            self.posicao = (0, 0)
        else:
            print("Dificuldade inválida! Usando 'normal' por padrão.")
            self.caverna = Caverna(6, 1 , 2)
            self.posicao = (0, 0)

    def cadastro(self):
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

            move = input("Use W/A/S/D para mover-se (Q para fechar o jogo): ").lower()
            if move in ["w", "s", "a", "d"]:
                self.mover(move)
            elif move == "q":
                print("Encerrando jogo...")
                self.ranking.addPontos(self.nome, self.pontuacao)  # Adiciona a pontuação ao ranking ao sair
                break  # Termina o jogo
            else:
                print("Movimento inválido...")

            if self.posicao in self.caverna.abismos:
                print("Você caiu em um abismo! Jogo terminado.")
                self.ranking.addPontos(self.nome, self.pontuacao)
                self.fim_de_jogo()

            if self.posicao == self.caverna.wumpus:
                print("Você encontrou o Wumpus! Jogo terminado.")
                self.ranking.addPontos(self.nome, self.pontuacao)
                self.fim_de_jogo()

            if not self.caverna.itens:
                print(f"Você coletou todos os itens! Sua pontuação final é: {self.pontuacao}")
                self.ranking.addPontos(self.nome, self.pontuacao)
                self.fim_de_jogo()

    def mover(self, direcao):
        x, y = self.posicao
        if direcao == "w" and x > 0:
            x -= 1
        elif direcao == "s" and x < self.caverna.tamanho - 1:
            x += 1
        elif direcao == "a" and y > 0:
            y -= 1
        elif direcao == "d" and y < self.caverna.tamanho - 1:
            y += 1

        self.posicao = (x, y)

        if self.posicao in self.caverna.abismos:
            print("Você caiu em um abismo! Jogo terminado.")
            self.ranking.addPontos(self.nome, self.pontuacao)
            self.fim_de_jogo()

        if self.posicao in self.caverna.itens:
            self.pontuacao += 10  # Adiciona 10 pontos por item coletado
            self.caverna.itens.remove(self.posicao)  # Remove o item coletado
            self.caverna.mapa[x][y] = '[ ]'  # Remove a representação do item no mapa
            print(f"Você coletou um item! Pontuação: {self.pontuacao}")

    def fim_de_jogo(self):
        resposta = input("Você deseja jogar novamente (S/N)? ").upper()
        if resposta == "S":
            self.cadastro()  # Reinicia o jogo
        else:
            self.ranking.addPontos(self.nome, self.pontuacao)  # Adiciona a pontuação ao ranking antes de sair
            print("Saindo...")
            exit()  # Encerra o jogo


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
        escolha = input("Escolha uma ação(W/S): \n").upper()
        if escolha == "W" and self.linha > 0:
            self.linha -= 1
        elif escolha == "S" and self.linha < len(self.menu) - 1:
            self.linha += 1
        elif escolha == "":
            self.executa()

    def executa(self):
        op = self.menu[self.linha]
        if op == "Sair":
            print("Saindo...\n")
            exit()
        elif op == "Ranking":
            self.pontos.mostraPontos()
            input("Pressione Enter para voltar ao menu...")
        elif op == "Novo Jogo":
            nwgame = NovoJogo(self.pontos)  # Passa o ranking para o novo jogo
            nwgame.cadastro()

    def run(self):
        while True:
            os.system('cls')
            print()
            self.exibirMenu()
            self.escolha()


if __name__ == "__main__":
    menu = menuInicial()
    menu.run()
