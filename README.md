
# 💸 API de Caixa Eletrônico (Melhorada)

Esta API simula o funcionamento de um caixa eletrônico, recebendo um valor de saque e retornando a menor quantidade de cédulas necessárias. Agora com melhorias de validação, estrutura e legibilidade de código!

## 📌 Cédulas Suportadas
- R$ 100
- R$ 50
- R$ 20
- R$ 10
- R$ 5
- R$ 2

---

## ⚙️ Pré-requisitos

- Python 3.x
- Flask

---

## 📥 Instalação

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install Flask
```

---

## ▶️ Como usar

### 1. Inicie o servidor Flask:

```bash
python caixa_eletronico.py
```

### 2. Faça uma requisição POST para:

```
http://127.0.0.1:5000/api/saque
```

### Corpo da requisição (JSON):

```json
{ "valor": 380 }
```

---

## 🧪 Exemplos de uso

### 🔁 Usando `curl`:

```bash
curl -X POST -H "Content-Type: application/json" -d "{\"valor\": 380}" http://127.0.0.1:5000/api/saque
```

### 🧪 Usando Postman:

1. Método: `POST`
2. URL: `http://127.0.0.1:5000/api/saque`
3. Headers:
   - Key: `Content-Type`
   - Value: `application/json`
4. Body (raw → JSON):
```json
{ "valor": 72 }
```

### 💻 Usando PowerShell:

```powershell
$headers = @{ "Content-Type" = "application/json" }
$body = @{ valor = 120 } | ConvertTo-Json
Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/saque" -Method Post -Headers $headers -Body $body
```

---

## 🛠 Melhorias e Validações

### ✅ Validação de Entrada
- Verificação se o JSON está presente.
- Confirmação se `valor` existe, é numérico e inteiro positivo.

### ⚙️ Algoritmo Eficiente
- Utiliza programação dinâmica para calcular a menor quantidade de cédulas possíveis.

### 🔒 Robustez
- Retorna mensagens de erro claras em caso de:
  - Dados ausentes
  - Tipo de dado incorreto
  - Valores inválidos (zero ou negativos)
  - Impossibilidade de saque com as cédulas disponíveis

---

## 📌 Possíveis Erros e Mensagens

| Situação                              | Mensagem de Erro                                              |
|---------------------------------------|----------------------------------------------------------------|
| Campo ausente no JSON                 | `"Campo 'valor' não encontrado no JSON."`                     |
| Valor é string                        | `"Valor inválido. Isso é uma string, não é um valor numérico."` |
| Valor não é inteiro                   | `"Valor inválido. O campo 'valor' deve ser um número inteiro."` |
| Valor negativo ou zero                | `"Valor inválido. Insira um número inteiro positivo."`        |
| Saque impossível com cédulas          | `"Não é possível fornecer este valor com as cédulas disponíveis."` |

---

## 💡 Contribuições Futuras

- Adicionar suporte a moedas (centavos)
- Integração com banco de dados para simular múltiplos caixas
- Autenticação de usuário para simular contas bancárias
