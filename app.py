import os
import json 
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

# --- CONFIGURAÇÃO DA API ---
# COLOQUE SUA CHAVE AQUI DENTRO DAS ASPAS
try:
    # 👇👇👇 (LINHA MODIFICADA) 👇👇👇
    minha_chave_secreta = os.environ.get("GOOGLE_API_KEY")
    genai.configure(api_key=minha_chave_secreta)
except Exception as e:
    print(f"Erro ao configurar a API do Google: {e}")
    print("Verifique se o .env foi criado e se a chave GOOGLE_API_KEY está lá.")

# --- FIM DA CONFIGURAÇÃO ---


# Simulação da API (para testar sem gastar)
def simular_api_ai(email_texto):
    if "feliz natal" in email_texto.lower() or "obrigado" in email_texto.lower():
        return {
            "classificacao": "Improdutivo",
            "sugestao_resposta": "Nenhuma ação necessária. Arquivar."
        }
    elif "suporte" in email_texto.lower() or "problema" in email_texto.lower():
        return {
            "classificacao": "Produtivo",
            "sugestao_resposta": "Olá! Recebemos sua solicitação de suporte. Nossa equipe já está analisando o problema e retornaremos em breve. Obrigado."
        }
    else:
         return {
            "classificacao": "Produtivo",
            "sugestao_resposta": "Olá. Recebemos seu email. Poderia fornecer mais detalhes sobre [assunto principal do email]? Atenciosamente."
        }

# Função que chama a API do Google Gemini
def chamar_api_ai_real(email_texto):
    """
    Função que chama a API do Google Gemini para análise.
    """
    
    # O prompt que faz a mágica
    prompt = """
    Analise o seguinte email e retorne APENAS um objeto JSON.
    
    Classifique o email em "Produtivo" (requer ação) ou "Improdutivo" (não requer ação, como spam ou felicitações).
    Sugira uma resposta breve e profissional se for "Produtivo", ou uma ação (ex: "Arquivar.") se for "Improdutivo".
    
    O JSON deve ter duas chaves: "classificacao" e "sugestao_resposta".
    
    Não inclua nenhuma outra palavra na sua resposta, apenas o JSON.
    
    Email para analisar:
    ---
    {}
    ---
    """.format(email_texto)
    
    try:
        # Configura o modelo
        # A nova linha (correta):
        model = genai.GenerativeModel('models/gemini-2.5-flash')
        
        # Gera o conteúdo
        response = model.generate_content(prompt)
        
        # Limpa a resposta para extrair SÓ o JSON
        json_response_text = response.text.strip().replace("```json", "").replace("```", "")
        
        # Converte o texto JSON em um dicionário Python
        return json.loads(json_response_text)
        
    except Exception as e:
        print(f"Erro ao chamar a API do Gemini: {e}")
        # Retorna um erro padronizado para o frontend
        return {
            "classificacao": "Erro",
            "sugestao_resposta": f"Erro ao processar na IA: {e}"
        }

# 3. Criação dos Endpoints do Flask
app = Flask(__name__)

@app.route('/')
def index():
    """ Rota principal que serve a página HTML. """
    return render_template('index.html')

@app.route('/analisar', methods=['POST'])
def analisar_email():
    """ Rota da API que recebe o texto do email e retorna a análise. """
    try:
        data = request.get_json()
        email_texto = data.get('email_texto')

        if not email_texto:
            return jsonify({"error": "Nenhuma texto de email fornecido."}), 400
        
        # ---- TROQUE AQUI PARA TESTAR ----
        
        # Use a simulação para testes rápidos
        # resultado_ia = simular_api_ai(email_texto)
        
        # Use a chamada real para o deploy final
        resultado_ia = chamar_api_ai_real(email_texto)

        return jsonify(resultado_ia)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)