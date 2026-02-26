from flask import Flask, render_template, request

app = Flask(__name__)

servicos_mecanica = [
    {"titulo": "Projetos 3D & FEA", "icon": "bi-cpu", "desc": "Modelagem avançada e Análise de Elementos Finitos para validação estrutural."},
    {"titulo": "Adequação NR-12", "desc": "Laudos, vistorias e projetos de segurança para máquinas e equipamentos."},
    {"titulo": "Projetos NR-13 / NR-35", "desc": "Inspeção de integridade e projetos de linha de vida e ancoragens."},
    {"titulo": "Laudos e ART", "desc": "Documentação técnica legal com garantia de responsabilidade técnica."}
]

@app.route('/')
def home():
    return render_template('index.html', servicos=servicos_mecanica)

@app.route('/contato', methods=['POST'])
def contato():
    nome = request.form.get('nome')
    return f"Recebemos seu pedido, Engenheiro {nome}! Entraremos em contato em breve."

if __name__ == '__main__':
    app.run(debug=True)