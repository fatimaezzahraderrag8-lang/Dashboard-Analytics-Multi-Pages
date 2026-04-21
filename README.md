#### Fonctionnalités

    Tableau de Bord Exécutif : Visualisation des KPIs clés (Transactions, CA, Clients) avec filtrage par agence et segment.

    Analyse des Risques : Identification des clients à haut risque et analyse de corrélation entre score de crédit et montants.

    Données en Temps Réel : Connexion directe à une base de données PostgreSQL.

## Stack Technique

    Langage : Python 3.x

    Interface : Streamlit

    Base de données : PostgreSQL & SQLAlchemy

    Visualisation : Plotly, Seaborn & Matplotlib

## Structure du Projet

    app.py : Page d'accueil.

    pages/ : Rapports détaillés (Exécutif & Risque).

    script/ : Logique de connexion (database.py) et filtres (utils.py).

    .env : Configuration des accès à la base de données (exclu du Git).

## Installation

    Installer les dépendances

    Configurer le fichier .env avec vos identifiants PostgreSQL.

    Lancer l'application : streamlit run app.py
