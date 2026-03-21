from flask import Flask, render_template, request
# Importando sua lógica da pasta calculo
from calculo.funcoes import calcular_linha_vida

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
        # Pegando os dados do formulário
        vao = float(request.form.get('vao', 0))
        pessoas = int(request.form.get('pessoas', 0))
        ruptura = float(request.form.get('ruptura', 0)) # Variável em português
        
        # CORREÇÃO AQUI: Mudamos 'rupture' para 'ruptura' para o Python não se perder
        resultado = calcular_linha_vida(vao, pessoas, ruptura)
    
    return render_template('calculadora.html', resultado=resultado)

@app.route('/contato', methods=['POST'])
def contato():
    nome = request.form.get('nome')
    return f"Olá {nome}, recebemos sua solicitação!"

if __name__ == '__main__':
    app.run(debug=True)