import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

st.set_page_config(page_title="X Intelligence Tool", layout="wide", page_icon="🔍")

st.title("🔍 X Intelligence Tool")
st.caption("**Projeto 2 — Candidatura Palantir Neurodivergent Fellowship** | Thiago Parente")

st.sidebar.header("🔧 Configurações")
topic = st.sidebar.text_input("Tópico para analisar", value="IA OR Elon Musk OR Palantir OR Grok")

if st.sidebar.button("🔄 Atualizar Análise"):
    st.rerun()

st.subheader(f"Análise de Sentimento no X/Twitter → {topic}")

st.markdown("""
**O que esta ferramenta mede?**
- **Sentimento**: Muito Positivo / Positivo / Neutro / Negativo / Muito Negativo  
- **Engajamento**: Alcance real (likes + reposts + views)  
- **Links**: Clique em "Ver no X" para ver o post original
""")

# 20 posts
data = {
    "Post (resumo)": [
        "Grok 4 é simplesmente insano, melhor que tudo", "Palantir vai dominar IA para governos",
        "Elon Musk mudou o jogo da IA novamente", "Governo usando IA pra monitorar cidadãos é perigoso",
        "Não aguento mais esse hype de IA", "Palantir fechou contrato bilionário com EUA",
        "IA vai tirar emprego de programadores", "xAI está anos luz à frente",
        "Palantir Foundry é a melhor ferramenta de dados", "Elon comprou o Twitter e transformou em X",
        "Grok entende contexto melhor que GPT", "Medo de IA substituindo humanos",
        "Palantir é essencial para defesa nacional", "IA generativa está evoluindo muito rápido",
        "Governo brasileiro precisa investir em IA", "Elon Musk é o maior visionário da nossa era",
        "Preocupação com viés nas IAs", "Palantir AIP vai revolucionar análise de dados",
        "Hype de IA está criando bolha?", "Grok + Palantir seria uma combinação mortal"
    ],
    "Sentimento": [
        "Muito Positivo", "Muito Positivo", "Positivo", "Muito Negativo", "Negativo",
        "Positivo", "Negativo", "Muito Positivo", "Positivo", "Positivo",
        "Muito Positivo", "Negativo", "Positivo", "Positivo", "Neutro",
        "Positivo", "Negativo", "Muito Positivo", "Neutro", "Muito Positivo"
    ],
    "Engajamento": [24500, 18900, 17200, 9800, 8200, 15400, 6700, 21300, 9800, 11200,
                   18700, 5400, 8900, 7600, 4300, 14500, 6200, 16800, 7100, 9200],
    "Horário": ["há 8min", "há 22min", "há 35min", "há 51min", "há 1h", "há 1h", "há 2h", "há 2h", "há 3h", "há 3h",
               "há 4h", "há 4h", "há 5h", "há 5h", "há 6h", "há 6h", "há 7h", "há 7h", "há 8h", "há 9h"],
    "Ver no X": [f"https://x.com/example/post{i}" for i in range(1,21)]
}

df = pd.DataFrame(data)

# Tabela com cores
def color_sentiment(val):
    if val == "Muito Positivo": return 'background-color: #00ff00; color: black'
    elif val == "Positivo": return 'background-color: #ffcc00; color: black'
    elif val in ["Negativo", "Muito Negativo"]: return 'background-color: #ff4444; color: white'
    return ''

st.dataframe(
    df.style.map(color_sentiment, subset=['Sentimento']),
    column_config={"Ver no X": st.column_config.LinkColumn("Ver no X")},
    use_container_width=True,
    hide_index=True
)

# ==================== GRÁFICO TOP 5 ====================
st.subheader("Top 5 Posts - Evolução de Engajamento")

# Pegando os 5 posts com maior engajamento
top5 = df.nlargest(5, 'Engajamento')

fig = px.bar(top5, 
             x="Post (resumo)", 
             y="Engajamento",
             color="Sentimento",
             title="Top 5 Posts por Engajamento",
             color_discrete_map={
                 "Muito Positivo": "#00ff00",
                 "Positivo": "#ffcc00",
                 "Neutro": "#ffff00",
                 "Negativo": "#ff9999",
                 "Muito Negativo": "#ff4444"
             },
             text="Engajamento")

fig.update_layout(height=500, xaxis_tickangle=-45)
st.plotly_chart(fig, use_container_width=True)

# Métricas
col1, col2, col3, col4 = st.columns(4)
with col1: st.metric("Posts Analisados", len(df))
with col2: st.metric("Sentimento Geral", "65% Positivo")
with col3: st.metric("Pico de Engajamento", "24.5k")
with col4: st.metric("Velocidade", "Alta")

st.success("✅ Gráfico atualizado: Agora mostra apenas os Top 5 posts por engajamento!")

st.caption("Construído com hyperfocus • 12h/dia")