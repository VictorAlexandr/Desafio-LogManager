# Parte 1: Importações e Configuração Inicial
import streamlit as st
import requests
import uuid

# --- CONFIGURAÇÃO DA PÁGINA E DO ESTADO DA SESSÃO ---

# Configura o título da página, ícone, etc., que aparece na aba do navegador
st.set_page_config(page_title="Chat Marmitaria", page_icon="🍲")

# Título principal que aparece na aplicação web
st.title("🍲 Chatbot da Marmitaria Delícia")

# ==============================================================================
# IMPORTANTE: COLE A SUA URL DE PRODUÇÃO DO WEBHOOK DO N8N AQUI
# 1. Abra seu workflow no n8n.
# 2. Clique no nó "Webhook".
# 3. Vá para a aba "Production URL" e copie a URL.
# 4. ATIVE seu workflow no n8n no canto superior direito.
N8N_WEBHOOK_URL = "https://victoraleofc.app.n8n.cloud/webhook/7373fb99-636a-4cf9-bc17-04badf91f7a8"
# ==============================================================================


# Parte 2: Gerenciamento da Sessão (A memória do frontend)

# Inicializa o histórico do chat na sessão se ele ainda não existir.
# Isso garante que a conversa não se perca quando o usuário interage.
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Gera e armazena um ID de usuário único para esta sessão de navegador específica.
# Isso permite que o backend (n8n) saiba qual histórico de conversa buscar.
if 'user_id' not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())


# Parte 4: Função de Comunicação com o Backend (n8n)

def send_message_to_n8n(user_message, user_id):
    """
    Envia a mensagem do usuário para o webhook do n8n e retorna a resposta da IA.
    """
    # Monta o payload JSON exatamente como o n8n espera receber.
    payload = {
        "userId": user_id,
        "message": user_message
    }
    try:
        # Faz a requisição POST para o backend.
        response = requests.post(N8N_WEBHOOK_URL, json=payload)
        # Verifica se a resposta foi bem-sucedida (código de status 2xx).
        response.raise_for_status()
        
        # Extrai o JSON da resposta e pega o valor da chave "reply".
        # O .get() é uma forma segura que evita erros se a chave "reply" não existir.
        ai_reply = response.json().get("reply", "Desculpe, não recebi uma resposta válida do servidor.")
        return ai_reply

    except requests.exceptions.RequestException as e:
        # Mostra um erro amigável na interface se a conexão com o n8n falhar.
        st.error(f"Erro de conexão com o chatbot: {e}")
        return "Desculpe, estou com problemas de conexão no momento. Tente novamente mais tarde."


# Parte 3: Lógica da Interface do Chat (O que o usuário vê)

# Exibe todas as mensagens do histórico guardado na sessão.
# Este loop roda toda vez que a tela é atualizada.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Cria o campo de entrada de texto no final da página.
# O `if prompt := ...` só executa o bloco de código quando o usuário envia uma mensagem.
if prompt := st.chat_input("Faça seu pedido ou diga 'oi' para começar"):
    
    # Adiciona a mensagem do usuário ao histórico da sessão.
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Exibe a mensagem do usuário na tela imediatamente.
    with st.chat_message("user"):
        st.markdown(prompt)

    # Mostra um indicador de "carregando" enquanto espera a resposta do backend.
    with st.spinner("O atendente está digitando..."):
        # Envia a mensagem para o n8n e armazena a resposta.
        ai_response = send_message_to_n8n(prompt, st.session_state.user_id)
        
        # Adiciona a resposta da IA ao histórico da sessão.
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        # Exibe a resposta da IA na tela.
        with st.chat_message("assistant"):
            st.markdown(ai_response)