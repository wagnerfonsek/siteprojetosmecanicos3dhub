from flask import Flask, render_template, request

app = Flask(__name__)

# Lista de serviços atualizada com foco em autoridade e no novo treinamento
servicos_mecanica = [
    {
        "titulo": "Projetos 3D & Análise FEA", 
        "desc": "Modelagem avançada no Autodesk Inventor com validação estrutural por Elementos Finitos."
    },
    {
        "titulo": "Adequação NR-12", 
        "desc": "Projetos completos de segurança, laudos e vistorias para conformidade de máquinas."
    },
    {
        "titulo": "Inspeção NR-13 & NR-35", 
        "desc": "Laudos de vasos de pressão e projetos de linha de vida com máxima segurança operacional."
    },
    {
        "titulo": "Treinamento em Soldagem", 
        "desc": "Capacitação técnica in-company (MIG/MAG, TIG, ER) unindo 15 anos de prática à engenharia."
    },
    {
        "titulo": "Consultoria e ART", 
        "desc": "Emissão de laudos técnicos e responsabilidade técnica para projetos e fabricação industrial."
    }
]

@app.route('/')
def home():
    return render_template('index.html', servicos=servicos_mecanica)

@app.route('/contato', methods=['POST'])
def contato():
    nome = request.form.get('nome')
    # Resposta personalizada para o cliente
    return f"Olá {nome}, recebemos sua solicitação! A Projetos Mecânicos 3D Hub entrará em contato em breve."

if __name__ == '__main__':
    app.run(debug=True)