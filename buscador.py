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
#vou colocar uma condição para verificar se o status da api é ok, pois assim garante que só continue rodando se estiver tudo certo
    if resultados.get('status') != 'OK':
        print("Erro na requisição solicitada", resultados.get('status'))
        return