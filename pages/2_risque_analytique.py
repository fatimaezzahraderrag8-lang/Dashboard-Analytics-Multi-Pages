import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from script.database import get_risk_data
from script.utils import sidebar_filters

st.title(" Analyse des Risques")

# DATA
df = get_risk_data()

# FILTRES 
df = sidebar_filters(df)

#  SCATTER 
st.markdown("### Score Crédit vs Montant")

fig_scatter = px.scatter(
    df,
    x="score_credit_client",
    y="montant_eur",
    color="categorie_risque"
)

st.plotly_chart(fig_scatter, use_container_width=True)

# TOP RISK =
st.markdown("### Top 10 Clients à Risque")

top_risk = df.sort_values(
    by=["score_credit_client", "montant_eur"],
    ascending=[True, False]
).head(10)

st.dataframe(top_risk)

# HEATMAP
st.markdown("###  Corrélation")

cols = ["score_credit_client", "montant_eur"]

corr = df[cols].corr()

fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)

st.pyplot(fig)