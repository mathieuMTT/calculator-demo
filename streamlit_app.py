import streamlit as st
from utils import (
    format_number, 
    add_percentage
)
from finance import (
    calculate_loan_amount,
    calculate_profitability_percentage,
    calculate_loan_cost,
    calculate_cashflow_pretax,
    calculate_loan_and_expenses
)

st.title("_Renta_ Calculator :bar_chart:")

col1, col2 , col3 = st.columns(3)
property_value = col1.number_input("Prix d'achat", min_value=0, value=100000)
agency_fees_rate = col2.number_input("Frais d'agence %", min_value=0.0, value=5.78)
notary_fees_rate = col3.number_input("Frais de notaire %", min_value=0.0, value=8.0)

property_value_with_agency_fees, agency_fee_value = add_percentage(property_value, agency_fees_rate)
property_value_with_notary_fees, notary_fee_value = add_percentage(property_value_with_agency_fees, notary_fees_rate)
acquisition_price = property_value_with_notary_fees

col1.metric(label="Prix d'achat (Frais d'agence et notaire inclus)", value=f"{format_number(acquisition_price)}")
col2.metric(label="Frais d'agence", value=f"{format_number(agency_fee_value)}")
col3.metric(label="Frais de notaire", value=f"{format_number(notary_fee_value)}")



st.subheader("Données sur l'investissement", divider="gray")
col1, col2 = st.columns(2)
property_work = col1.number_input("Travaux", min_value=0, value=0)
expenses = col1.number_input("Charges annuelles (Taxe foncière, copro, entretien, etc)", min_value=0, value=2000)
monthly_rent = col2.number_input("Loyer mensuel", min_value=0, value=750)
rental_vacancies = col2.number_input("Vacances locatives (mois)", min_value=0, value=1)


st.subheader("Données bancaires", divider="gray")
col1, col2 = st.columns(2)
contribution = col2.number_input("Apport", min_value=0, value=0)
bank_interest_rate = col2.slider("Taux d'intérêts", 0.01, 8.00, 3.59)
loan_duration_year = col2.slider("Durée de l'emprunt", 1, 25, 20)
monthly_loan_insurance_cost = col2.number_input("Coût assurance emprunteur (mois)", min_value=0, value=50)
monthly_pno_insurance_cost = col2.number_input("Coût assurance propriétaire non occupant (mois)", min_value=0, value=10)

total_property_loan = calculate_loan_amount(acquisition_price, property_work, contribution)
profitability = calculate_profitability_percentage(monthly_rent, rental_vacancies, expenses, acquisition_price, property_work, contribution)

monthly_payment, total_loan_cost, loan_cost,  = calculate_loan_cost(total_property_loan, bank_interest_rate, loan_duration_year, monthly_loan_insurance_cost, monthly_pno_insurance_cost)
col1.metric(label="Montant emprunté", value=f"{format_number(total_property_loan)}")
col1.metric(label="Coût total du crédit", value=f"{format_number(total_loan_cost)}")
col1.metric(label="Mensualités de crédit", value=f"{format_number(monthly_payment)}")
st.info("Des frais de dossier et de garantie peuvent s'ajouter, selon la banque. En général, ces frais représentent environ 1,5 fois le montant du prix du bien.", icon="ℹ️")


monthly_cashflow_pretax = calculate_cashflow_pretax(monthly_rent, monthly_payment, expenses)
monthly_payment_with_expenses = calculate_loan_and_expenses(monthly_payment, expenses)


st.subheader("Kpis", divider="gray")
col1, col2, col3 = st.columns(3)
col1.metric(label="Rentabilité", value=f"{profitability:.1f}%")
col2.metric(label="Emprunt et charges (mois)", value=f"{format_number(monthly_payment_with_expenses)}") # à remplacer par les charges mensuelles
col3.metric(label="Cashflow avant impôts (mois)", value=f"{format_number(monthly_cashflow_pretax)}")