import pandas as pd
import streamlit as st

def sidebar_filters(df):
    st.sidebar.header("Filtres")

    # Agence
    if "agence_id" in df.columns:
        agences = st.sidebar.multiselect(
            "Agence",
            df["agence_id"].dropna().unique(),
            default=df["agence_id"].dropna().unique()
        )
        df = df[df["agence_id"].isin(agences)]

    # Segment
    if "segment_id" in df.columns:
        segments = st.sidebar.multiselect(
            "Segment",
            df["segment_id"].dropna().unique(),
            default=df["segment_id"].dropna().unique()
        )
        df = df[df["segment_id"].isin(segments)]

    # Date
    if "date_transaction" in df.columns:
        df["date_transaction"] = pd.to_datetime(df["date_transaction"], errors="coerce")

        min_date = df["date_transaction"].min()
        max_date = df["date_transaction"].max()

        date_range = st.sidebar.date_input(
            "Période",
            [min_date, max_date]
        )

        if len(date_range) == 2:
            df = df[
                (df["date_transaction"] >= pd.to_datetime(date_range[0])) &
                (df["date_transaction"] <= pd.to_datetime(date_range[1]))
            ]

    return df