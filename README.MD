# Desafio Técnico - Agente de IA para Marmitaria (LogManager)

## Visão Geral

Este projeto implementa um agente de IA conversacional totalmente funcional, capaz de simular o atendimento de um restaurante de marmitas. O agente guia o usuário desde a apresentação do cardápio até a confirmação e registro do pedido, aceitando personalizações em linguagem natural.

O projeto foi desenvolvido como solução para o Desafio Técnico para a vaga de Engenheiro de IA na LogManager.

---

## Arquitetura do Projeto

A solução foi construída utilizando uma arquitetura moderna e desacoplada, separando o frontend da lógica de backend:

- **Frontend:** Uma interface de chat web desenvolvida com **Streamlit**, rodando em um ambiente **GitHub Codespaces**.
- **Backend (Automação):** O fluxo de conversação e a lógica de negócios foram implementados na plataforma de automação **n8n Cloud**.
- **Inteligência Artificial (IA):** O cérebro do agente é o modelo **Claude 3 Haiku**, acessado via **AWS Bedrock**, responsável por entender o usuário e conduzir a conversa.
- **Banco de Dados:** Duas planilhas no **Google Sheets** são utilizadas para persistir os dados: uma para o histórico de conversas (memória do bot) e outra para o registro dos pedidos finalizados.

**Fluxo de Dados:**
`Usuário (Browser) -> Streamlit (Codespaces) -> n8n Webhook -> AWS Bedrock & Google Sheets`

---

## Funcionalidades Implementadas

- **Apresentação de Cardápio:** O agente inicia a conversa apresentando um cardápio claro e com múltiplas opções.
- **Personalização de Pedidos:** Entende e processa solicitações de personalização, como troca de acompanhamentos, adição de itens extras (com custo) e remoção de ingredientes.
- **Cálculo de Valor Total:** O agente calcula o valor final do pedido com base nos itens e adicionais escolhidos.
- **Confirmação de Pedido:** Antes de finalizar, o agente resume o pedido completo e pede a confirmação do usuário.
- **Registro de Pedidos:** Após a confirmação, o pedido é automaticamente registrado em uma planilha Google Sheets para consulta.
- **Memória de Conversa:** O agente mantém o contexto da conversa, permitindo um diálogo fluido e de múltiplos passos com cada usuário.

---

## Como Testar a Aplicação

### Link Público para Testes

Você pode interagir com o chatbot diretamente através do link abaixo, gerado pelo ambiente de desenvolvimento do GitHub Codespaces.

**🔗 Link do Chatbot:** https://supreme-space-pancake-7gv67w74vjqfr4p5-8501.app.github.dev

### Instruções de Teste

1.  Abra o link acima.
2.  Inicie a conversa com uma saudação, como "oi" ou "olá".
3.  O agente irá apresentar o cardápio. Escolha um ou mais itens.
4.  Responda às perguntas do agente sobre personalizações (tente adicionar um ovo, trocar o arroz por macarrão, etc.).
5.  Quando o agente apresentar o resumo do pedido, confirme com uma mensagem como "sim" ou "pode confirmar".
6.  Após a confirmação, o agente exibirá uma mensagem de sucesso, e o pedido será registrado na planilha de backend.

---

## Estrutura do Repositório

- `app.py`: O código-fonte da aplicação frontend em Streamlit.
- `requirements.txt`: As dependências Python necessárias para rodar a aplicação.
- `README.md`: Este documento.
- `/prints/`: Pasta contendo screenshots do workflow implementado no n8n.

*(Certifique-se de criar uma pasta chamada "prints" e adicionar seus screenshots do n8n lá dentro)*.