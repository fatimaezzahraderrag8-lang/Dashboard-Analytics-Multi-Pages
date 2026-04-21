from sqlalchemy import create_engine
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

@st.cache_resource
def get_engine():
    return create_engine(
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )

engine = get_engine()

# KPI 

@st.cache_data
def get_kpi_global():
    return pd.read_sql("SELECT * FROM kpi_global", engine)

@st.cache_data
def get_kpi_mensuel():
    return pd.read_sql("SELECT * FROM kpi_mensuel", engine)

@st.cache_data
def get_risk_data():
    query = """
    SELECT 
        c.client_id,
        c.score_credit as score_credit_client,
        c.categorie_risque,
        t.montant_eur,
        t.date_transaction
    FROM client c
    JOIN transaction t ON c.client_id = t.client_id
    """
    return pd.read_sql(query, engine)