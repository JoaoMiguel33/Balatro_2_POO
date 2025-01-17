import random

class Carta:
    def __init__(self, naipe, valor):
        self.naipe = naipe
        self.valor = valor

    def exibir(self):
        return f"{self.valor} de {self.naipe}"

class Baralho:
    def __init__(self):
        naipes = ['Espadas', 'Copas', 'Ouros', 'Paus']
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cartas = [Carta(naipe, valor) for naipe in naipes for valor in valores]

    def embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir_cartas(self, jogadores, num_cartas):
        for jogador in jogadores:
            jogador.cartas_em_mao = [self.cartas.pop() for _ in range(num_cartas)]

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.cartas_em_mao = []

    def mostrar_cartas(self):
        return [carta.exibir() for carta in self.cartas_em_mao]

class Jogo:
    def __init__(self, jogadores, num_cartas_por_jogador):
        self.baralho = Baralho()
        self.jogadores = jogadores
        self.num_cartas_por_jogador = num_cartas_por_jogador

    def jogar_partida(self):
        self.baralho.embaralhar()
        self.baralho.distribuir_cartas(self.jogadores, self.num_cartas_por_jogador)

        for jogador in self.jogadores:
            print(f"{jogador.nome} tem as cartas: {', '.join(jogador.mostrar_cartas())}")

        pontos = self.calcular_pontos()
        vencedor = self.determinar_vencedor(pontos)
        print(f"O vencedor é {vencedor.nome} com {pontos[vencedor]} pontos!")

    def calcular_pontos(self):
        pontos = {}
        for jogador in self.jogadores:
            pontos[jogador] = 0
            for carta in jogador.cartas_em_mao:
                pontos[jogador] += self.valor_carta(carta.valor)

        return pontos

    def valor_carta(self, valor):
        valores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        return valores[valor]

    def determinar_vencedor(self, pontos):
        vencedor = max(pontos, key=pontos.get)
        return vencedor


jogadores = [Jogador("Monteiro"), Jogador("Mafê")]
jogo = Jogo(jogadores, 2)
jogo.jogar_partida()
