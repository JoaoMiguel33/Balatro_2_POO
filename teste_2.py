import random

class Carta:
    def __init__(self, naipe, valor):
        self._naipe = naipe
        self._valor = valor

    def __str__(self):
        return f"{self._valor} de {self._naipe}"

    @property
    def valor(self):
        return self._valor


class Baralho:
    _NAIPES = ['Espadas', 'Copas', 'Ouros', 'Paus']
    _VALORES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self._cartas = [Carta(naipe, valor) for naipe in self._NAIPES for valor in self._VALORES]

    def embaralhar(self):
        random.shuffle(self._cartas)

    def distribuir_cartas(self, jogadores, num_cartas):
        for jogador in jogadores:
            cartas_distribuidas = [self._cartas.pop() for _ in range(min(num_cartas, len(self._cartas)))]
            jogador.receber_cartas(cartas_distribuidas)


class Jogador:
    def __init__(self, nome):
        self._nome = nome
        self._cartas_em_mao = []

    @property
    def nome(self):
        return self._nome

    def receber_cartas(self, cartas):
        self._cartas_em_mao.extend(cartas)

    def mostrar_cartas(self):
        return ', '.join(str(carta) for carta in self._cartas_em_mao)

    def calcular_pontos(self):
        return sum(Jogo.valor_carta(carta.valor) for carta in self._cartas_em_mao)

    def jogar_carta(self):
        if self._cartas_em_mao:
            return self._cartas_em_mao.pop(0)
        else:
            return None


class JogadorUsuario(Jogador):
    def jogar_carta(self):
        print(f"\nSuas cartas: {self.mostrar_cartas()}")
        while True:
            escolha = input("Escolha uma carta para jogar (1 a {len(self._cartas_em_mao)}): ")
            if escolha.isdigit():
                indice = int(escolha) - 1
                if 0 <= indice < len(self._cartas_em_mao):
                    return self._cartas_em_mao.pop(indice)
            print("Escolha inválida. Tente novamente.")


class Jogo:
    _VALORES_CARTAS = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }

    def __init__(self, jogadores, num_cartas_por_jogador):
        self._baralho = Baralho()
        self._jogadores = jogadores
        self._num_cartas_por_jogador = num_cartas_por_jogador

    def jogar_partida(self):
        self._baralho.embaralhar()
        self._baralho.distribuir_cartas(self._jogadores, self._num_cartas_por_jogador)

        for jogador in self._jogadores:
            print(f"{jogador.nome} tem as cartas: {jogador.mostrar_cartas()}")

        rodada = 1
        while any(jogador._cartas_em_mao for jogador in self._jogadores):
            print(f"\nRodada {rodada}")
            cartas_jogadas = {}

            for jogador in self._jogadores:
                carta = jogador.jogar_carta()
                if carta:
                    cartas_jogadas[jogador] = carta
                    print(f"{jogador.nome} jogou: {carta}")

            if cartas_jogadas:
                vencedor_rodada = max(cartas_jogadas, key=lambda jogador: Jogo.valor_carta(cartas_jogadas[jogador].valor))
                print(f"Vencedor da rodada: {vencedor_rodada.nome}")

            rodada += 1

        vencedor, pontos = self._determinar_vencedor()
        print(f"\nO vencedor final é {vencedor.nome} com {pontos} pontos!")

    @staticmethod
    def valor_carta(valor):
        return Jogo._VALORES_CARTAS.get(valor, 0)

    def _determinar_vencedor(self):
        pontuacoes = {jogador: jogador.calcular_pontos() for jogador in self._jogadores}
        vencedor = max(pontuacoes, key=pontuacoes.get)
        return vencedor, pontuacoes[vencedor]


if __name__ == "__main__":
    jogadores = [Jogador("Zezinho"), Jogador("Mafê"), JogadorUsuario("Você")]
    jogo = Jogo(jogadores, 5)
    jogo.jogar_partida()
