import streamlit as st

st.title("_Dossier_ Bancaire :bank:")

# -------------------------------------------------- #
st.subheader("Informations sur l'emprunteur", divider="gray")
col1, col2, col3 = st.columns(3)
last_name = col1.text_input("Nom", label_visibility="collapsed", placeholder="Nom")
first_name = col2.text_input(
    "Prénom", label_visibility="collapsed", placeholder="Prénom"
)
age = col1.number_input(
    "Age",
    label_visibility="collapsed",
    min_value=18,
    max_value=100,
    value=None,
    placeholder="Age",
)
# = col2.text_input("", label_visibility="collapsed", placeholder="Prénom")

personal_situation = col2.selectbox(
    "Situation matrimonial",
    ("marié", "pacsé", "divorcé", "séparé", "célibataire", "veuf"),
    label_visibility="collapsed",
    index=None,
    placeholder="Situation matrimonial",
)
st.write("")
st.write("")

# Ajouter le financier : PEA, Livrets, épargne -> Partie patrimoniale


# -------------------------------------------------- #
st.subheader("Situation professionnelle de l'emprunteur", divider="gray")
col1, col2, col3 = st.columns(3)
profession = col1.text_input(
    "Profession", label_visibility="collapsed", placeholder="Profession"
)
company = col2.text_input(
    "Société", label_visibility="collapsed", placeholder="Société"
)
monthly_revenue = col1.number_input(
    "Revenu mensuel (net avant impôts)",
    label_visibility="collapsed",
    min_value=0,
    max_value=1000000,
    value=None,
    placeholder="Revenu net mensuel avant impôts",
)
contract = col2.selectbox(
    "Type de contrat",
    ("CDI", "CDD", "Indépendant", "Intermittent", "Alternant", "Portage salarial"),
    label_visibility="collapsed",
    index=None,
    placeholder="Type de contrat",
)
trial_period = col1.selectbox(
    "Période d'éssai",
    ("Oui", "Non"),
    label_visibility="collapsed",
    index=None,
    placeholder="Période d'éssai",
)
seniority = col2.text_input(
    "Ancienneté", label_visibility="collapsed", placeholder="Ancienneté"
)


st.write("")
st.write("")
# -------------------------------------------------- #
st.subheader("Situation bancaire", divider="gray")
col1, col2, col3 = st.columns(3)
current_loan_cnt = col1.number_input(
    "",
    label_visibility="collapsed",
    min_value=0,
    max_value=100,
    value=None,
    placeholder="Nombre de crédit en cours",
)
