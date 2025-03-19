### 🗺️ Buscador de Restaurantes no Google Maps

Um script em python que utiliza api do |Google Maps para buscar restaurantes em uma localização específica. Após executado o script exibe informações como: nome do estabelcimento; n° sde telefone.

## Descrição

    - O script faz o uso do PLACES API do google, onde ele busca restaurantes à partir das informações fornecedidas dentro do script.

        1- Busca por estabelecimentos próximos: Utiliza a API Nearby Search para encontrar estabelecimentos dentro do raio especificado.

        2- Detalhes do estabelecimento: Para cada estabelecimento encontrado, o script faz uma segunda requisição a API Place Details para obter o telefone de contato.

    O resultado é exibido diretamente no terminal, com o nome e o telefone de cada estabelecimento.

## 🚀 Funcionalidades

    * Busca em uma localização específica (Restaurantes, bares, bistrô, café, qualquer tipo de estabelecimento que for 
    requisitado);
    * Exibe nome, e contato dos estabelecimentos listados;

    * Fácil de usar e configurar;

    * Integração com a API do google mapas;

## 📦 Pré-requisitos

    - Uma chave da PLACES API (É bem fácil conseguir essa chave, basta acessar, console.cloud.google e ir na sessão de api)
    
    - Ter instalado na máquina python 3.x

    - Instalar a biblioteca requests ( "pip install requests" )

## 🧩 Estrutura do Código

    O script está organizado da seguinte forma:

    Função buscar_restaurantes:

    Realiza a busca de estabelecimentos próximos usando a API Nearby Search.

    Para cada estabelecimento encontrado, faz uma segunda requisição à API Place Details para obter o telefone.

    Exibe o nome e o telefone no terminal.

## Parâmetros personalizáveis:

    location: Coordenadas geográficas (latitude, longitude) da localização desejada.

    radius: Raio de busca em metros (padrão: 30 km).

    tipo_estabelecimento: Tipos de estabelecimentos a serem buscados (padrão: restaurant|cafe).

## 📄 Exemplo de Uso

    Aqui está um exemplo de como o script funciona:
    ![alt text](<Captura de tela 2025-03-18 204652.png>)
    

## 👨‍💻 Autor

    Marcelo Andrade de Olivera

    GitHub: tielo-ma

    LinkedIn: https://www.linkedin.com/in/marcelo-andrade-984170310/

## 🙌 Agradecimentos

    Google Maps API pela incrível ferramenta de geolocalização.

    Comunidade Python por tornar o desenvolvimento tão acessível.


