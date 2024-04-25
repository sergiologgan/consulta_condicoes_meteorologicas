import sys
import io
import requests

# Configurar o sys.stdin para usar utf-8
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

def obter_informacoes_meteorologicas(cidade, api_key):
    try:
        # URL base da API do OpenWeatherMap
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        
        # Parâmetros para a solicitação GET
        parametros = {
            'q': cidade,
            'appid': api_key,
            'units': 'metric',  # para obter a temperatura em Celsius
            'lang': 'pt_br'     # para obter a descrição do clima em português
        }

        # Fazer a solicitação GET
        response = requests.get(base_url, params=parametros)

        # Verificar se a solicitação foi bem-sucedida
        response.raise_for_status()

        # Extrair dados em formato JSON
        dados_clima = response.json()

        # Extrair a descrição do clima e a temperatura
        descricao_clima = dados_clima['weather'][0]['description']
        temperatura_atual = dados_clima['main']['temp']
        temperatura_minima = dados_clima['main']['temp_min']
        temperatura_maxima = dados_clima['main']['temp_max']
        sensacao = dados_clima['main']['feels_like']

        # Exibir os resultados
        print('\n\n')
        print(f'Clima em {cidade}: {descricao_clima.capitalize()}')
        print(f'Temperatura atual: {temperatura_atual}°C')
        print(f'Mínima: {temperatura_minima}°C')
        print(f'Máxima de: {temperatura_maxima}°C')
        print(f'Sensação de {sensacao}º')
        print()

    except requests.RequestException as e:
        print(f"Erro ao conectar com a API do OpenWeatherMap: {e}")
    except KeyError as e:
        print(f"Erro ao extrair os dados: {e}")

# Solicitar ao usuário a cidade e a chave API
cidade = input('Digite o nome da cidade: ')
api_key = '2eb2b180071c06d3e773ff44c01641ee'

# Chamar a função com os dados do usuário
obter_informacoes_meteorologicas(cidade, api_key)
