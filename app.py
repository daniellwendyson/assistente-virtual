import os
import streamlit as st
from transformers import pipeline
from PIL import Image
from openai import OpenAI
from dotenv import load_dotenv


# ======================================
# LOAD ENV
# ======================================

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    st.error("❌ Chave OpenAI não encontrada no arquivo .env")
    st.stop()

client = OpenAI(api_key=OPENAI_API_KEY)


# ======================================
# CONFIG STREAMLIT
# ======================================

st.set_page_config(
    page_title="Assistente Visual IA",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Assistente Visual com IA")
st.write("Envie uma imagem e faça perguntas sobre ela.")


# ======================================
# CARREGAR MODELO VQA
# ======================================

@st.cache_resource
def carregar_vqa():
    return pipeline(
        "visual-question-answering",
        model="dandelin/vilt-b32-finetuned-vqa"
    )


vqa = carregar_vqa()


# ======================================
# FUNÇÕES
# ======================================

def traduzir_para_ingles(pergunta):

    prompt = f"""
Traduza para inglês esta pergunta sobre uma imagem,
mantendo o sentido original:

{pergunta}
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()


# --------------------------------------


def responder_vqa(imagem, pergunta):

    resultado = vqa(
        image=imagem,
        question=pergunta
    )

    return resultado[0]["answer"], resultado[0]["score"]


# --------------------------------------


def explicar_llm(pergunta, resposta, score):

    prompt = f"""
Um sistema analisou uma imagem.

Pergunta: {pergunta}
Resposta: {resposta}
Confiança: {round(score,2)}

Explique em português como chegou nessa resposta.
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content


# ======================================
# INTERFACE
# ======================================

uploaded_file = st.file_uploader(
    "📷 Envie uma imagem",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file:

    imagem = Image.open(uploaded_file).convert("RGB")

    st.image(
        imagem,
        caption="Imagem enviada",
        use_container_width=True
    )

    pergunta = st.chat_input("Faça sua pergunta sobre a imagem...")

    if pergunta:

        if len(pergunta.strip()) < 3:
            st.warning("Digite uma pergunta válida.")
            st.stop()

        # USER
        with st.chat_message("user"):
            st.write(pergunta)

        # TRADUÇÃO
        with st.spinner("Traduzindo pergunta..."):
            pergunta_en = traduzir_para_ingles(pergunta)

        # VQA
        with st.spinner("Analisando imagem..."):
            resposta, score = responder_vqa(imagem, pergunta_en)

        confianca = round(score * 100, 1)

        # ASSISTANT
        with st.chat_message("assistant"):

            st.markdown(f"""
### 📌 Resposta

**{resposta}**

Confiança: `{confianca}%`
""")

            # EXPLICAÇÃO
            with st.spinner("Gerando explicação..."):

                explicacao = explicar_llm(
                    pergunta,
                    resposta,
                    score
                )

            st.markdown("### 🧠 Explicação")
            st.write(explicacao)

else:

    st.info("👆 Envie uma imagem para começar.")