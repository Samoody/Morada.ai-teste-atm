# API de Caixa Eletrônico

Esta API simula o funcionamento de um caixa eletrônico. Ela recebe um valor de saque desejado e retorna a quantidade de cédulas de cada valor necessárias para compor esse saque, utilizando a menor quantidade de cédulas possível. As cédulas consideradas são: 100, 50, 20, 10, 5 e 2.

## Pré-requisitos

- Python 3.x instalado
- Flask instalado

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio

2. Crie um ambiente virtual e ative-o (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate   # No Windows, use `venv\Scripts\activate`

3. Instale as dependências:
    ```bash 
    pip install Flask
    
  # USO
1. Inicie o servidor Flask:
``` 
    python caixa_eletronico.py
```

2. Faça uma requisição POST para http://127.0.0.1:5000/api/saque com o seguinte corpo JSON, como por exemplo:

    {
    "valor": 380
     { "valor": 120 }, { "valor": 72 }, { "valor": 85 }
    }


Usando curl
Para fazer uma requisição utilizando cURL, execute o seguinte comando no terminal:


    curl -X POST -H "Content-Type: application/json" -d "{\"valor\": 380}" http://127.0.0.1:5000/api/saque 
```
    curl -X POST -H "Content-Type: application/json" -d "{\"valor\": 120}" http://127.0.0.1:5000/api/saque
```
          
    curl -X POST -H "Content-Type: application/json" -d "{\"valor\": 72}" http://127.0.0.1:5000/api/saque
 ```
            
            curl -X POST -H "Content-Type: application/json" -d "{\"valor\": 85}" http://127.0.0.1:5000/api/saque
```
 

Inicie o servidor Flask:

        python caixa_eletronico.py
       
    
        
       
# Usando o Postman
1. Abra o Postman.

2. Clique em "New" e selecione "Request".
3. Nomeie a requisição e adicione-a a uma coleção.
4. Selecione o método HTTP como POST.
5. No campo URL, insira http://127.0.0.1:5000/api/saque.
6. Vá para a aba "Headers" e adicione um cabeçalho:
Key: Content-Type
Value: application/json
7. Vá para a aba "Body", selecione "raw" e escolha JSON no menu suspenso.
8. Insira o seguinte JSON no campo de texto

    {
    "valor": 380  { "valor": 120 }, { "valor": 72 }, { "valor": 85 }
    }

9. Clique em "Send".

# Usando PowerShell no Windows

1. Abra o PowerShell.

2. Defina os cabeçalhos e o corpo da requisição:
```
    $headers = @{
        "Content-Type" = "application/json"
    }

    $body = @{
        valor = 380
    } | ConvertTo-Json
```
3. Envie a requisição
```
    Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/saque" -Method Post -Headers $headers -Body $body
```

# Desafios Enfrentados 

1. Tratamento de Entradas Inválidas Garantir: que o valor inserido é um número inteiro positivo foi um desafio, pois era necessário validar a entrada e retornar mensagens de erro apropriadas em caso de entradas inválidas.

2. Eficiência na Distribuição de Cédulas Implementar: uma lógica que sempre retorne a menor quantidade de cédulas possível envolveu pensar em um algoritmo que pudesse lidar eficientemente com a divisão do valor de saque pelas cédulas disponíveis.

3. Erros e Exceções: Foi necessário lidar com cenários onde o valor de saque não podia ser atendido com as cédulas disponíveis. A implementação incluiu o tratamento adequado de erros e exceções para garantir a robustez da API.

4. Documentação e Testes: Garantir que o código estivesse bem documentado e criar testes adequados para validar a lógica de saque foram etapas cruciais para assegurar a qualidade e a manutenção do projeto.