from flask import Flask, request, jsonify
from flask_cors import CORS
from __init__ import calc_func, gauss_elimination, extrapolar, gauss_jacobi, gauss_seidel, inter_newton, inter_newton_inv, lagrange, bissection, newton_raphson, secante, newton_colis
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route('/api/bolzano', methods=['POST'])
def bolzano():
    data = request.json

    func = data.get('func', '')     
    x_min = data.get('x_min', 0)     
    x_max = data.get('x_max', 1)     
    precision = data.get('precision', 0.001)

    result = calc_func(func, x_min, x_max, precision)
    
    return jsonify({'result': result})


@app.route('/api/bissection', methods=['POST'])
def bissection_flask():
    data = request.json

    func = data.get('func', '')    
    tol = data.get('tol', 0.01)
    intervalo1 = data.get('intervalo1', 25)
    intervalo2 = data.get('intervalo2', 26)
    intervalo = (intervalo1, intervalo2)
    parada_opts = data.get('parada_opts', 0)
    
    root, erro, iterator, log = bissection(func, intervalo, tol, parada_opts)

    return jsonify({'result': {'raiz': root, "erro": erro, "iterator": iterator, "log": log}})


@app.route('/api/newton_raphson', methods=['POST'])
def newton_raphson_flask():
    data = request.json
    func = data.get('func', '')
    func_dx = data.get('func_dx', '')
    x_inicial = data.get('x_inicial', 1)
    tol = data.get('tol', 0.001)

    root, erro, iterator, log = newton_raphson(func, func_dx, x_inicial, tol)

    return jsonify({'result': {'raiz': root, "erro": erro, "iterator": iterator, "log": log}})


@app.route('/api/secante', methods=['POST'])
def secante_flask():
    data = request.json

    func = data.get('func', '')
    tol = data.get('tol', 0.01)
    intervalo1 = data.get('intervalo1', 25)
    intervalo2 = data.get('intervalo2', 26)
    intervalo = (intervalo1, intervalo2)

    root, log = secante(func, tol, intervalo)

    return jsonify({'result': {'raiz': root, "log": log}})


@app.route('/api/elim_gauss', methods=['POST'])
def elim_gauss_flask():
    data = request.json

    variable_matrix = data.get('variable_matrix', '')
    constant_matrix = data.get('constant_matrix', '')
    
    print("Variable Matrix:", variable_matrix)
    print("Constant Matrix:", constant_matrix)
    
    answer, log = gauss_elimination(variable_matrix, constant_matrix)

    return jsonify({'result': {'answer': answer, 'log': log}})


@app.route('/api/gauss_jacobi', methods=['POST'])
def gauss_jacobi_flask():
    data = request.json

    variable_matrix = data.get('variable_matrix', '')
    constant_matrix = data.get('constant_matrix', '')
    x0 = data.get('x0', '')
    precision = data.get('precision', 2)
    max_iterations = data.get('max_iterations', 30)

    x, i, log = gauss_jacobi(variable_matrix, constant_matrix, x0, precision, max_iterations)  

    return jsonify({'result': {'x': x, 'iterations': i,  'log': log}})


@app.route('/api/gauss_seidel', methods=['POST'])
def gauss_seidel_flask():
    data = request.json

    variable_matrix = data.get('variable_matrix', '')
    constant_matrix = data.get('constant_matrix', '')
    x0 = data.get('x0', '')
    precision = data.get('precision', 2)
    max_iterations = data.get('max_iterations', 30)

    x, i, log = gauss_seidel(variable_matrix, constant_matrix, x0, precision, max_iterations)

    return jsonify({'result': {'x': x, 'iterations': i,  'log': log}})


@app.route('/api/lagrange', methods=['POST'])
def lagrange_flask():
    data = request.json

    x = data.get('x_values', '')
    y = data.get('y_values', '')
    x_intersection = data.get('x_intersection', '')

    final_result, x_intersection, log = lagrange(x, y, x_intersection)

    return jsonify({'result': {'solution': final_result, 'x_intersection': x_intersection,  'log': log}})


@app.route('/api/interpolador_newton', methods=['POST'])
def interpolador_newton_flask():
    data = request.json

    x = data.get('x_values', '')
    y = data.get('y_values', '')
    x_intersection = data.get('x_intersection', '')
    points = len(x)

    fx, result, log = inter_newton(x, y, points, x_intersection)

    return jsonify({'result': {'function': fx, 'solution': result, 'log': log}})


@app.route('/api/interpolador_newton_inv', methods=['POST'])
def interpolador_newton_inv_flask():
    data = request.json

    x = data.get('x_values', '')
    y = data.get('y_values', '')
    y_intersection = data.get('y_intersection', '')
    points = len(x)

    fx ,result, log = inter_newton_inv(y, x, points, y_intersection)

    return jsonify({'result': {'function': fx, 'solution': result, 'log': log}})


@app.route('/api/extrapolacao', methods=['POST'])
def extrapolacao_flask():
    data = request.json

    x = data.get('x_values', '')
    y = data.get('y_values', '')
    grau = data.get('grau', 2)

    polinomio, log = extrapolar(x, y, grau)

    return jsonify({'result': {'polinomio': polinomio, 'log': log}})

@app.route('/api/trapezio_composto', methods=['POST'])
def trapezio_flask():
    data = request.json
    
    func = data.get('func', '')
    if func != "":
        intervalo_0 = data.get('intervalo_0', '')
        intervalo_1 = data.get('intervalo_1', '')
        points = data.get('points', '')
        x_values = ''
        y_values = ''
        choice = 0
    else:
        intervalo_0 = ''
        intervalo_1 = ''
        points = ''
        x_values = data.get('x_values', '')
        y_values = data.get('y_values', '')
        choice = 1
    
    result, log = newton_colis(func, x_values, y_values, (intervalo_0, intervalo_1), points, choice)

    return jsonify({'result': {'integral': result, 'log': log}})



if __name__ == '__main__':
    app.run(debug=True)