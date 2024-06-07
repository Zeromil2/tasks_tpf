import requests
import pandas as pd
from pathlib import Path

ROOT_PATH = Path(__file__).parent  # localização da pasta com o arquivo

try:
    with open(ROOT_PATH / "ceps.txt", "r") as arquivo:
        # Lista de CEPs fornecida
        ceps = [cep for cep in arquivo.readline().split(', ')]

except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")

# URL base da API ViaCEP
url_base = "https://viacep.com.br/ws/{}/json/"

# Lista para armazenar os dados dos endereços
enderecos = []

# Função para consultar a API do ViaCEP


def consultar_cep(cep):
    response = requests.get(url_base.format(cep))
    if response.status_code == 200:
        dados = response.json()
        return {
            "cep": cep,
            "logradouro": dados.get("logradouro", "indisponível"),
            "bairro": dados.get("bairro", "indisponível"),
            "cidade": dados.get("localidade", "indisponível"),
            "estado": dados.get("uf", "indisponível")
        }
    else:
        return {
            "cep": cep,
            "logradouro": "indisponível",
            "bairro": "indisponível",
            "cidade": "indisponível",
            "estado": "indisponível"
        }


def main():
    # Consultar todos os CEPs e coletar os dados
    for cep in ceps:
        endereco = consultar_cep(cep)
        enderecos.append(endereco)

    # Criar um DataFrame com os dados coletados
    df = pd.DataFrame(enderecos)

    # Salvar os dados em um arquivo CSV
    df.to_csv("enderecos.csv", index=False)

    print("Dados salvos em enderecos.csv")
    print(df)


main()
