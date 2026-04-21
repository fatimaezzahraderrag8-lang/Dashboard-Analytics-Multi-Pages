import streamlit as st
import plotly.express as px
from script.database import get_kpi_global, get_kpi_mensuel

#  TITLE
st.title(" Tableau de Bord Exécutif")

#  DATA (Originale)
df_global = get_kpi_global()
df_mensuel = get_kpi_mensuel()

#  SIDEBAR 
st.sidebar.header(" Filtres")

agences = sorted(df_global["agence_id"].unique())
selected_agence = st.sidebar.selectbox("Choisir une Agence :", options=agences)

segments = sorted(df_global["segment_id"].unique())
selected_segment = st.sidebar.selectbox("Choisir un Segment :", options=segments)

# FILTRAGE 
df_filtered = df_global[
    (df_global["agence_id"] == selected_agence) & 
    (df_global["segment_id"] == selected_segment)
]

#  KPIs 
st.subheader("Indicateurs Clés de Performance (KPIs)")

if not df_filtered.empty:
    total_tx = df_filtered["nb_transactions"].sum()
    ca_total = df_filtered["total_montant"].sum()
    clients = df_filtered["nb_clients"].sum()
    moyenne = df_filtered["moyenne_montant"].mean()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Transactions", int(total_tx))
    col2.metric("CA Total", f"{ca_total:,.2f}")
    col3.metric("Clients", int(clients))
    col4.metric("Moyenne", f"{moyenne:.2f}")

    #  CHARTS
    st.subheader("Visualisations")
    
    fig_bar = px.bar(
        df_filtered, 
        x="agence_id",
        y="total_montant",
        title="CA par Agence (Filtré)"
    )
    st.plotly_chart(fig_bar)

    fig_pie = px.pie(
        df_filtered, 
        names="segment_id",
        values="nb_clients",
        title="Segments Clients (Filtré)"
    )
    st.plotly_chart(fig_pie)
else:
    st.warning("Il n’y a aucune donnée avec ces options. Essayez un autre filtre..")
    
# DEBUG (Optional)
with st.expander(" Aperçu des données filtrées"):
    st.write(df_filtered)