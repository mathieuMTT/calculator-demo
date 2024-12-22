import streamlit as st
from utils import (
    format_number, 
    add_percentage
)
from finance import Property, Loan

st.title("_Renta_ Calculator :bar_chart:")


# -------------------------------------------------- #
# Proporty data
col1, col2 , col3 = st.columns(3)
property_value = col1.number_input("Prix d'achat", min_value=0, value=100000)
agency_fees_rate = col2.number_input("Frais d'agence %", min_value=0.0, value=5.78)
notary_fees_rate = col3.number_input("Frais de notaire %", min_value=0.0, value=8.0)

# Fees calculation
property_value_with_agency_fees, agency_fee_value = add_percentage(property_value, agency_fees_rate)
property_value_with_notary_fees, notary_fee_value = add_percentage(property_value_with_agency_fees, notary_fees_rate)
acquisition_price = property_value_with_notary_fees

# Print results
col1.metric(label="Prix d'achat (Frais d'agence et notaire inclus)", value=f"{format_number(acquisition_price)}")
col2.metric(label="Frais d'agence", value=f"{format_number(agency_fee_value)}")
col3.metric(label="Frais de notaire", value=f"{format_number(notary_fee_value)}")


# -------------------------------------------------- #
# Investment data
st.subheader("Données sur l'investissement", divider="gray")
col1, col2 = st.columns(2)
property_work = col1.number_input("Travaux", min_value=0, value=0)
expenses = col1.number_input("Charges annuelles (Taxe foncière, copro, entretien, etc)", min_value=0, value=2000)
monthly_rent = col2.number_input("Loyer mensuel", min_value=0, value=750)
rental_vacancies = col2.number_input("Vacances locatives (mois)", min_value=0, value=1)


# -------------------------------------------------- #
# Banking data
st.subheader("Données bancaires", divider="gray")
col1, col2 = st.columns(2)
contribution = col2.number_input("Apport", min_value=0, value=0)
bank_interest_rate = col2.slider("Taux d'intérêts", 0.01, 8.00, 3.59)
loan_duration_year = col2.slider("Durée de l'emprunt", 1, 25, 20)
monthly_loan_insurance_cost = col2.number_input("Coût assurance emprunteur (mois)", min_value=0, value=50)
monthly_pno_insurance_cost = col2.number_input("Coût assurance propriétaire non occupant (mois)", min_value=0, value=10)

# Creation of Property and Loan objects
property_instance = Property(
    value=acquisition_price,
    work_cost=property_work,
    contribution=contribution,
    monthly_rent=monthly_rent,
    rental_vacancies=rental_vacancies,
    expenses=expenses
)

loan_instance = Loan(
    amount=acquisition_price + property_work - contribution,
    interest_rate=bank_interest_rate,
    duration_years=loan_duration_year,
    loan_insurance_cost=monthly_loan_insurance_cost,
    pno_insurance_cost=monthly_pno_insurance_cost
)

# Calculs
profitability = property_instance.profitability()
loan_amount = property_instance.total_value()
monthly_payment = loan_instance.calculate_monthly_payment()
total_loan_cost = loan_instance.total_cost()
loan_cost = loan_instance.loan_cost()
monthly_cashflow_pretax = property_instance.calculate_cashflow_pretax(monthly_payment)
monthly_payment_with_expenses = loan_instance.calculate_loan_and_expenses(monthly_payment, expenses)

# Print results
col1.metric(label="Montant à emprunter", value=f"{format_number(loan_amount)}")
col1.metric(label="Coût total du crédit", value=f"{format_number(total_loan_cost)}")
col1.metric(label="Mensualités de crédit", value=f"{format_number(monthly_payment)}")
st.info("Des frais de dossier et de garantie peuvent s'ajouter, selon la banque. En général, ces frais représentent environ 1,5 fois le montant du prix du bien.", icon="ℹ️")


# -------------------------------------------------- #
# Print results
st.subheader("Kpis", divider="gray")
col1, col2, col3 = st.columns(3)
col1.metric(label="Rentabilité", value=f"{profitability:.1f}%")
col2.metric(label="Emprunt et charges (mois)", value=f"{format_number(monthly_payment_with_expenses)}")
col3.metric(label="Cashflow avant impôts (mois)", value=f"{format_number(monthly_cashflow_pretax)}")