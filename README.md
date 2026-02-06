# 🧠 Assistente Visual com IA

Um **Assistente Visual Inteligente** que permite fazer perguntas em linguagem natural sobre imagens enviadas.  
O projeto utiliza **ViLT** para Visual Question Answering (VQA) e **OpenAI GPT** para gerar explicações detalhadas.

---

## 🚀 Funcionalidades

- 📷 Upload de imagens (jpg, png, jpeg)  
- 💬 Perguntas em português sobre:  
  - Quantidade de pessoas ou objetos  
  - Presença de objetos  
  - Cores  
  - Ações simples  
- 🧠 Tradução automática para inglês via OpenAI GPT  
- ✅ Resposta do modelo ViLT com confiança  
- 📊 Explicação detalhada do raciocínio via LLM  
- 🔒 Chave OpenAI segura usando `.env`  
- 🖥️ Interface web interativa via Streamlit

---

## ⚡ Tecnologias Utilizadas

- Python 3.11  
- [Streamlit](https://streamlit.io/)  
- [Transformers](https://huggingface.co/docs/transformers/index)  
- [ViLT (Visual Language Transformer)](https://huggingface.co/dandelin/vilt-b32-finetuned-vqa)  
- [OpenAI GPT-3.5-turbo](https://platform.openai.com/)  
- Pillow  
- python-dotenv

---

## 📦 Instalação

```bash
git clone https://github.com/daniellwendyson/assistente-virtual.git
cd assistente-virtual
Instalar dependências:

bash
py -3.11 -m pip install -r requirements.txt
Criar arquivo .env na raiz do projeto:


OPENAI_API_KEY=SUA_CHAVE_AQUI
```

## ▶️ Executar
```bash
py -3.11 -m streamlit run app.py
Abra o link que aparecer no terminal para acessar a interface web.
```

## 📝 Uso
Clique em Upload e selecione uma imagem (jpg, png ou jpeg).

Digite sua pergunta sobre a imagem no chat.

O sistema mostrará:

```
- Resposta do modelo ViLT
- Confiança (%)
- Explicação detalhada via OpenAI GPT
```


## 🔐 Boas Práticas
```Adicione .env ao .gitignore para não subir a chave para o GitHub.

Crie um arquivo .env.example para servir de modelo:

```
OPENAI_API_KEY=your_key_here
```
Nunca compartilhe sua chave OpenAI publicamente.
``` 

## 📂 Estrutura do Projeto
```
assistente-virtual/
├── app.py
├── requirements.txt
├── .env            # sua chave local, não subir no git
├── .env.example    # modelo de chave
└── images/         # coloque suas imagens aqui
```

## 📖 Licença
MIT License
Use livremente para estudos e projetos pessoais.


💡 Observações
O modelo ViLT funciona melhor para quantidade, cores, objetos simples e ações básicas.

Perguntas complexas podem gerar respostas imprecisas.

O sistema é voltado para projetos acadêmicos ou portfólio.
