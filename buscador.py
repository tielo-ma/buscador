#importando a biblioteca requests essencial para fazer a requisição http
import requests

#logo abaixo vou definir uma função com todos os parametros a ser definidos
def buscar_restaurantes (api_key, location, radius=30000, tipo_estabelecimento='Restaurant'):

#vale ressaltar que o endpoint é usado para buscar lugares próximos a uma localização específica
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    params = { #um dicionário com os parametros essenciais para o script entender a minha busca
        'location': location,
        'radius': radius,
        'type': tipo_estabelecimento,
        'key': api_key
    }

#esqueci destas partes, onde o response é a variavel que vai ser responsavel por guardar a resposta da requisição a api, e 
# o resultados seria pra converter essa resposta para json, visando melhor a visualização dos dados
    response = requests.get(url, params=params)
    resultados = response.json()

#vou colocar uma condição para verificar se o status da api é ok, pois assim garante que só continue rodando se estiver tudo certo
    if resultados.get('status') != 'OK':
        print("Erro na requisição solicitada", resultados.get('status'))
        return
#vou adicionar mais uma condição para mostrar caso o resultado seja não encontrado
    if not resultados.get('results'):
        print("Nenhum estabelecimento encontrado")
        return

#aqui vou iterar a lista de resultados, assim ele me processa cada item individualmente, e as informações que quero extrair
    for lugar in resultados.get('results', []):
        nome = lugar.get('name')
        telefone = lugar.get('formatted_phone_number', 'Telefone não dispoível')
        print(f"Nome: {nome}, Telefone: {telefone}")