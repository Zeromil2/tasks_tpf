from pathlib import Path

ROOT_PATH = Path(__file__).parent  # localização da pasta com o arquivo
def main():
    try:
        with open(ROOT_PATH / "notas_fiscais.txt", "r") as arquivo:
            sequencia = int(arquivo.readline())
            lista_arquivo = [int(numero) for numero in arquivo.readline().split()]  # sequência que está no arquivo
            sequencia_correta = list(range(1, sequencia + 1))  # sequência com todos os números

            for numero in sequencia_correta:  # analisando qual número falta na sequência do arquivo
                if numero not in lista_arquivo:
                    print(numero)
                    break

    except IOError as exc:
        print(f"Erro ao abrir o arquivo {exc}")  # tratamento de exceção no caso de ocorrer algum erro


main()
