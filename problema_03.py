from pathlib import Path

ROOT_PATH = Path(__file__).parent  # localização da pasta com o arquivo


def maior_sequencia(lista_sequencia):
    if not lista_sequencia:
        return None, 0

    max_valor = None
    max_contagem = 0
    contagem_atual = 1
    valor_atual = lista_sequencia[0]

    for i in range(1, len(lista_sequencia)):
        if lista_sequencia[i] == valor_atual:
            contagem_atual += 1
        else:
            if contagem_atual > max_contagem:
                max_contagem = contagem_atual
                max_valor = valor_atual
            valor_atual = lista_sequencia[i]
            contagem_atual = 1

    # Verificação final para a última sequência
    if contagem_atual > max_contagem:
        max_contagem = contagem_atual
        max_valor = valor_atual

    return max_valor, max_contagem


try:
    with open(ROOT_PATH / "medicoes.txt", "r") as arquivo:
        tamanho_lista = arquivo.readline()
        lista_medicoes = [medicao for medicao in arquivo.readline().split(', ')]

        medicao_comparada = lista_medicoes[0]  # para iniciar comparando com o primeiro item da lista

        valor, contagem = maior_sequencia(lista_medicoes)

        print(f"{contagem} medições de {valor}")


except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")