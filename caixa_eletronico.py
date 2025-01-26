from flask import Flask, request, jsonify

app = Flask(__name__)

def calcular_cedulas_dinamico(valor):
    cedulas = [100, 50, 20, 10, 5, 2]
    n = len(cedulas)
    dp = [float('inf')] * (valor + 1)
    dp[0] = 0
    escolha = [-1] * (valor + 1)

    for i in range(n):
        for j in range(cedulas[i], valor + 1):
            if dp[j - cedulas[i]] + 1 < dp[j]:
                dp[j] = dp[j - cedulas[i]] + 1
                escolha[j] = i

    if dp[valor] == float('inf'):
        return None  

    resultado = {str(cedula): 0 for cedula in cedulas}
    while valor > 0:
        idx = escolha[valor]
        if idx == -1:
            return None
        resultado[str(cedulas[idx])] += 1
        valor -= cedulas[idx]
    
    return resultado

@app.route('/api/saque', methods=['POST'])
def saque():
    dados = request.get_json()

    if not dados:
        return jsonify({'error': 'Nenhum dado recebido.'}), 400

    if 'valor' not in dados:
        return jsonify({'error': 'Campo "valor" não encontrado no JSON.'}), 400

    valor = dados['valor']

    if isinstance(valor, str):
        return jsonify({'error': 'Valor inválido. Isso é uma string, não é um valor numérico.'}), 400

    if not isinstance(valor, int):
        return jsonify({'error': 'Valor inválido. O campo "valor" deve ser um número inteiro.'}), 400

    if valor <= 0:
        return jsonify({'error': 'Valor inválido. Insira um número inteiro positivo.'}), 400

    resultado = calcular_cedulas_dinamico(valor)
    if resultado is None:
        return jsonify({'error': 'Não é possível fornecer este valor com as cédulas disponíveis.'}), 400
    
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
