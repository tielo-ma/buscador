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

#aqui vai ser o bloco que será responsável por fazer a requisição http get á api e converter a resposta que vem em json para um dicionário em py
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

#mudei para fazer duas requisições pois em meus testes internos o código me voltou apenas o nome o restaurante, e todo os telefones como inexistente
    for lugar in resultados.get('results', []):
        place_id = lugar.get('place_id')
        nome = lugar.get('name')

#depois de algumas pesquisas, entendi que a versão antiga que estava codando ela tentava buscar as informações na primeira requisição
#mas o campo formatted_phone_number não estava me voltando nada, para obter mais informações usarei o Place_details
        url_details = "https://maps.googleapis.com/maps/api/place/details/json"
        params_details = {
            'place_id': place_id,
            'fields': 'formatted_phone_number',
            'key': api_key
        }
#aqui mais um campo para fazer a requisição e transformar a responsa que vem em json para um dicionário
        response_details = requests.get(url_details, params=params_details)
        resultados_details = response_details.json()

#aqui irei adicionar um bloco para tratamentos de erros para a requisição esperada
        if resultados_details.get('status') != 'OK':
            telefone = 'Telefone não disponível'
        else:
            telefone = resultados_details.get('result', {}).get('formatted_phone_number','Telefone não disponível')

        print(f"Nome: {nome}, Telefone: {telefone}")

#aqui irei criar o bloco principal do script, aqui será definida a chave da api que por segurança não vou deixar aqui, e também esse bloco de código vai chamar a função <buscar_restaurantes>
if __name__ == "__main__":
    api_key = 'suave chave da api aqui'
    location = '-5.812757,-35.255127' #aqui são as coordenadas geográficas de natal, copie a da sua cidade aqui
    buscar_restaurantes(api_key, location)

