from flask import Flask, render_template, request
import math

# Importando sua lógica da pasta calculo
from calculo.funcoes import calcular_linha_vida
from calculo.funcoes_nr13 import calcular_volume_cilindro, calcular_volume_tampo, calcular_pv_nr13

app = Flask(__name__)

# --- VITRINE COMERCIAL ---
servicos_mecanica = [
    {"titulo": "Projetos 3D & Análise FEA", "desc": "Modelagem avançada no Autodesk Inventor com validação estrutural por Elementos Finitos."},
    {"titulo": "Adequação NR-12", "desc": "Projetos completos de segurança, laudos e vistorias para conformidade de máquinas."},
    {"titulo": "Inspeção NR-13 & NR-35", "desc": "Laudos de vasos de pressão e projetos de linha de vida com máxima segurança operacional."},
    {"titulo": "Treinamento em Soldagem", "desc": "Capacitação técnica in-company (MIG/MAG, TIG, ER) unindo 15 anos de prática à engenharia."},
    {"titulo": "Consultoria e ART", "desc": "Emissão de laudos técnicos e responsabilidade técnica para projetos e fabricação industrial."}
]

@app.route('/')
def home():
    return render_template('index.html', servicos=servicos_mecanica)

@app.route('/ferramentas')
def ferramentas():
    return render_template('ferramentas.html')

@app.route('/calculadora_nr35', methods=['GET', 'POST'])
def calculadora_nr35():
    resultado = None
    if request.method == 'POST':
        vao = float(request.form.get('vao', 0))
        pessoas = int(request.form.get('pessoas', 0))
        ruptura = float(request.form.get('ruptura', 0))
        resultado = calcular_linha_vida(vao, pessoas, ruptura)
    return render_template('calculadora.html', resultado=resultado)

@app.route('/calculadora_nr13', methods=['GET', 'POST'])
def calculadora_nr13():
    resultado = None
    if request.method == 'POST':
        try:
            p = float(request.form.get('pressao', 0))
            d = float(request.form.get('diametro', 0))
            h = float(request.form.get('altura', 0))
            tipo_tampo = request.form.get('tipo_tampo')
            classe = request.form.get('classe_fluido')
            
            v_casco = calcular_volume_cilindro(d, h)
            # Multiplicamos por 2 para considerar os dois tampos do vaso
            v_tampo = calcular_volume_tampo(tipo_tampo, d) * 2 
            v_total = v_casco + v_tampo
            
            pv, categoria = calcular_pv_nr13(p, v_total, classe)
            
            resultado = {
                'volume': round(v_total, 3),
                'pv': pv,
                'categoria': categoria
            }
        except Exception as e:
            print(f"Erro no cálculo: {e}")
            
    return render_template('calculadora_nr13.html', resultado=resultado)

@app.route('/contato', methods=['POST'])
def contato():
    nome = request.form.get('nome')
    return f"Olá {nome}, recebemos sua solicitação!"
@app.route('/calculadora_nr12', methods=['GET', 'POST'])
def calculadora_nr12():
    # Como o checklist que te passei é processado via JavaScript no navegador,
    # a rota só precisa renderizar o template.
    return render_template('calculadora_nr12.html')

if __name__ == '__main__':
    app.run(debug=True)