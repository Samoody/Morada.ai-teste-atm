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
        return None  # Impossível formar o valor com as cédulas disponíveis

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
