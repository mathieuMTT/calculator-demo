import streamlit as st
from finance import (
    calculate_loan_amount,
    calculate_profitability_percentage,
    calculate_loan_cost,
    calculate_cashflow_pretax,
    calculate_loan_and_expenses
)

st.title("_Renta_ Calculator :bar_chart:")

st.subheader("Données sur l'investissement", divider="gray")
col1, col2 = st.columns(2)
property_value = col1.number_input("Prix d'achat (Frais d'agence et notaire inclus)", min_value=0, value=100000)
property_work = col1.number_input("Travaux", min_value=0, value=0)
expenses = col1.number_input("Charges annuelles (Taxe foncière, copro, entretien, etc)", min_value=0, value=2000)
contribution = col2.number_input("Apport", min_value=0, value=10000)
monthly_rent = col2.number_input("Loyer mensuel", min_value=0, value=1000)
rental_vacancies = col2.number_input("Vacances locatives (mois)", min_value=0, value=1)


total_property_loan = calculate_loan_amount(property_value, property_work, contribution)
profitability = calculate_profitability_percentage(monthly_rent, rental_vacancies, expenses, property_value, property_work, contribution)


st.subheader("Données bancaires", divider="gray")
col1, col2 = st.columns(2)
bank_interest_rate = col2.slider("Taux d'intérêts", 0.00, 8.00, 1.00)
loan_duration_year = col2.slider("Durée de l'emprunt", 0, 25, 20)
monthly_loan_insurance_cost = col2.number_input("Coût assurance emrpunteur (mois)", min_value=0, value=30)
monthly_pno_insurance_cost = col2.number_input("Coût assurance propriétaire non occupant (mois)", min_value=0, value=15)
monthly_payment, total_loan_cost, loan_cost,  = calculate_loan_cost(total_property_loan, bank_interest_rate, loan_duration_year, monthly_loan_insurance_cost, monthly_pno_insurance_cost)
col1.metric(label="Montant emprunté", value=f"{total_property_loan}")
col1.metric(label="Coût total du crédit", value=f"{total_loan_cost:.2f}")
col1.metric(label="Mensualités de crédit", value=f"{monthly_payment:.2f}")


monthly_cashflow_pretax = calculate_cashflow_pretax(monthly_rent, monthly_payment, expenses)
monthly_payment_with_expenses = calculate_loan_and_expenses(monthly_payment, expenses)


st.subheader("Kpis", divider="gray")
col1, col2, col3 = st.columns(3)
col1.metric(label="Rentabilité", value=f"{profitability:.1f}%")
col2.metric(label="Emprunt et charges (mois)", value=f"{monthly_payment_with_expenses:.2f}") # à remplacer par les charges mensuelles
col3.metric(label="Cashflow avant impôts (mois)", value=f"{monthly_cashflow_pretax:.2f}")