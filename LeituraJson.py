import json
from   Diretorio import NomeArquivo

def LerJson():
    arquivo = NomeArquivo()

    # load: Carregar arquivo
    # loads: Carregar arquivo em uma lista de objetos
    with open(arquivo, 'r') as file:
        json_data = json.loads(json.dumps(json.load(file), indent=4))
    # with

    return json_data
# ReadJson